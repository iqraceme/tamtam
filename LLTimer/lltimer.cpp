#include "Python.h"
#include "Numeric/arrayobject.h"


#include <pthread.h>
//#include <sys/timeb.h>
#include <signal.h>


//typedef pthread_t ThreadHandle;
//typedef pthread_mutex_t StreamMutex;

//  #define MUTEX_INITIALIZE(A) pthread_mutex_init(A, NULL)
//  #define MUTEX_DESTROY(A)    pthread_mutex_destroy(A);
//  #define MUTEX_LOCK(A)       pthread_mutex_lock(A)
//  #define MUTEX_UNLOCK(A)     pthread_mutex_unlock(A)



static int lltimerState=0;
static int callbackSet=0;
static unsigned long lltimerMSecs=1000;
static PyObject * LltimerError;
static PyObject * pyCbFunction;
static PyObject * arglist = Py_BuildValue("()");


static pthread_t thread;

extern "C" 
{

  //return a timestamp in msecs

  //this is a millisecond timestamp. 
  static timeval startTime;
  static int startTimeInit=0;
  static unsigned long timestamp()  {
    if (startTimeInit==0) {
      gettimeofday(&startTime,NULL);
      startTimeInit=1;
      return 0;
    } 
    timeval currTime;
    gettimeofday(&currTime,NULL);
    return (unsigned long)((currTime.tv_sec - startTime.tv_sec)*1000 + (currTime.tv_usec - startTime.tv_usec)/1000) ;
  }

  //this is a millisecond delta timestamp
  static timeval lastTime;
  static int startDTimeInit=0;
  static unsigned long dtimestamp()  {
    if (startDTimeInit==0) {
      gettimeofday(&lastTime,NULL);
      startDTimeInit=1;
      return 0;
    } 
    timeval currTime;
    gettimeofday(&currTime,NULL);
    unsigned long retval= (unsigned long)((currTime.tv_sec - lastTime.tv_sec)*1000 + (currTime.tv_usec - lastTime.tv_usec)/1000) ;
    lastTime.tv_sec=currTime.tv_sec;
    lastTime.tv_usec=currTime.tv_usec;
    return retval;
  }



  //this is the signal handler that gets called by the timer
  void sigalrm(int sig) {
    //printf("Dtime %li\n",dtimestamp());
    PyEval_CallObject(pyCbFunction, arglist);
  }

  void * periodicTimer(void * ignore) {
    
    if (callbackSet==0) {
      printf("No callback set!\n");
      //return 1;
    } else {


      //setup the timer (Thanks again to Gary Scavone @ McGill Univ. and his RtAudio for help on this!)
      struct sigaction sa;
      sigset_t samask;
      sa.sa_handler=sigalrm;
      sa.sa_flags=0;
      samask=sa.sa_mask;
      
      struct itimerval iv;
      iv.it_interval.tv_sec=0; 
      iv.it_interval.tv_usec=lltimerMSecs*1000;
      iv.it_value.tv_sec=0;
      iv.it_value.tv_usec=lltimerMSecs*1000;
      int result = setitimer(ITIMER_REAL,&iv,NULL);
      if (result==-1) {
	printf("Cannot initialize realtime timer\n");
	return NULL;
      }
      result = sigaction(SIGALRM, &sa, NULL);
      if (result==-1) {
	printf("Cannot initialize sig handler\n");
	return NULL;
      }

      struct sched_param param;
      param.sched_priority = 90;   // Is this the best number?
      result = sched_setscheduler( 0, SCHED_RR, &param);
      printf("Reult for setscheduler %i\n",result);
   

      // Check we have done what we hoped.
      int sched = sched_getscheduler(0);
      switch (sched) {
      case SCHED_RR:
	printf( " RR \n" );   // running as root I now get this.
	break;
      case SCHED_FIFO:
	printf( " FIFO \n" );
	break;
      default:
	printf( " priority =  %d \n",sched );
      }
      printf("Max is %i\n",sched_get_priority_max(SCHED_RR));

      //sigemptyset(&samask);
      //sigsuspend(&samask);  //this will start the timer

    }
    return NULL;
  }    


  //creates and starts timer. 
  static PyObject *  lltimer_timeout_add(PyObject * self, PyObject * args) {
    int msecs=1000;
    //parse args to be sure it was called as lltimer.start()
    if (!PyArg_ParseTuple(args, "iO:timeout_add", &msecs,&pyCbFunction)) {
      printf("Error in LLTimer.start. Syntax: lltimer.timeout_add(msecs,callback)\n");
      return NULL;
    }

    lltimerMSecs=(unsigned long) msecs; 

    if (!PyCallable_Check(pyCbFunction)) {
      PyErr_SetString(PyExc_TypeError, "Callback function must be callable");
      return NULL;
    }
    Py_XINCREF(pyCbFunction);         /* Add a reference to new callback */
    callbackSet=1;

    if (lltimerState==0) {
      printf("Initializing thread\n");
      //create and start the timer (Thanks to Gary Scavone @ McGill Univ. and his RtAudio for help on this!)
      pthread_attr_t attr;
      pthread_attr_init(&attr);
      //pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);
      pthread_attr_setschedpolicy(&attr, SCHED_RR);
      int err = pthread_create(&thread, &attr, periodicTimer, NULL);
      //pthread_attr_destroy(&attr);
      if (err) {
	printf("Error initializing pthread\n");
	lltimerState=0;
      } else {
	printf("PThread initialized\n");
	lltimerState=1;
      }
    }	else {
      printf("Timer already started\n");
    }
    
    return Py_BuildValue("i", lltimerState);
  }



  static PyObject *  lltimer_stop(PyObject * self, PyObject * args) {
    char *argStr;
    if (!PyArg_ParseTuple(args, "", &argStr)) {
      printf("Error in LLTimer stop. Syntax: stop()\n");
      return NULL;
    }
    lltimerState=0;
    return Py_BuildValue("i", 0);
  }

  static PyObject *  lltimer_set_callback(PyObject * self, PyObject * args) {
    if (!PyArg_ParseTuple(args, "O:set_callback", &pyCbFunction))
      return NULL;
    if (!PyCallable_Check(pyCbFunction)) {
      PyErr_SetString(PyExc_TypeError, "parameter must be callable");
      return NULL;
    }
    Py_XINCREF(pyCbFunction);         /* Add a reference to new callback */
    callbackSet=1;
    return Py_BuildValue("i", 0);
  }
}  



static PyMethodDef LltimerMethods[] = {
  {"stop",  lltimer_stop, METH_VARARGS},
  {"timeout_add",  lltimer_timeout_add, METH_VARARGS},
  {"set_callback",  lltimer_set_callback, METH_VARARGS},
  {NULL,      NULL}        /* Sentinel */
};


extern "C" 
{
  void  initlltimer() {
    PyObject *m, *d;
    m = Py_InitModule("lltimer", LltimerMethods);
    d = PyModule_GetDict(m);
    LltimerError = PyErr_NewException("lltimer.error", NULL, NULL);
    PyDict_SetItemString(d, "error", LltimerError);
    import_array();
  }
}
