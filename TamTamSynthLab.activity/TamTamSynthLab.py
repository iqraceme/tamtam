import locale
locale.setlocale(locale.LC_NUMERIC, 'C')
import signal , time , sys , os, shutil
import pygtk
pygtk.require( '2.0' )
import gtk

import gobject
import time

import common.Config as Config
from   common.Util.CSoundClient import new_csound_client
from   common.Util.Profiler import TP

from   SynthLab.SynthLabMain import SynthLabMain
from   common.Util.Trackpad import Trackpad
from   gettext import gettext as _
import commands
from sugar.activity import activity

class TamTamSynthLab(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        for snd in ['mic1','mic2','mic3','mic4','lab1','lab2','lab3','lab4', 'lab5', 'lab6']:
            if not os.path.isfile(os.path.join(Config.DATA_DIR, snd)):
                shutil.copyfile(Config.SOUNDS_DIR + '/' + snd , Config.DATA_DIR + '/' + snd)
                os.system('chmod 0777 ' + Config.DATA_DIR + '/' + snd + ' &')

        color = gtk.gdk.color_parse(Config.WS_BCK_COLOR)
        self.modify_bg(gtk.STATE_NORMAL, color)

        self.set_title('TamTam SynthLab')
        self.set_resizable(False)

        self.trackpad = Trackpad( self )

        self.preloadTimeout = None

        self.connect('notify::active', self.onActive)
        self.connect('destroy', self.onDestroy)

        #load the sugar toolbar
        self.toolbox = activity.ActivityToolbox(self)
        self.set_toolbox(self.toolbox)

        self.activity_toolbar = self.toolbox.get_activity_toolbar()
        self.activity_toolbar.share.hide()
        self.activity_toolbar.keep.hide()

        self.toolbox.show()

        self.trackpad.setContext('synthLab')
        self.synthLab = SynthLabMain(self)
        self.connect('key-press-event', self.synthLab .onKeyPress)
        self.connect('key-release-event', self.synthLab .onKeyRelease)

        self.connect( "key-press-event", self.synthLab.onKeyPress )
        self.connect( "key-release-event", self.synthLab.onKeyRelease )


        self.set_canvas( self.synthLab )

        self.synthLab.onActivate(arg = None)
        self.show()

    def onPreloadTimeout( self ):
        if Config.DEBUG > 4: print "TamTam::onPreloadTimeout", self.preloadList

        t = time.time()
        if self.preloadList[0].load( t + 0.100 ): # finished preloading this object
            self.preloadList.pop(0)
            if not len(self.preloadList):
                if Config.DEBUG > 1: print "TamTam::finished preloading", time.time() - t
                self.preloadTimeout = False
                return False # finished preloading everything

        if Config.DEBUG > 4: print "TamTam::preload returned after", time.time() - t

        return True

    def onActive(self, widget = None, event = None):
        if widget.props.active == False:
            Config.logwrite(1, 'TamTamSynthLab.onActivate disconnecting csound')
            csnd = new_csound_client()
            csnd.connect(False)
        else:
            Config.logwrite(1, 'TamTamSynthLab.onActivate connecting csound')
            csnd = new_csound_client()
            csnd.connect(True)

    def onKeyPress(self, widget, event):
        pass

    def onKeyRelease(self, widget, event):
        pass

    def onDestroy(self, arg2):
        if Config.DEBUG: print 'DEBUG: TamTam::onDestroy()'

        self.synthLab.onDestroy()

        csnd = new_csound_client()
        csnd.connect(False)
        csnd.destroy()

        gtk.main_quit()

# No more dir created by TamTam
    def ensure_dir(self, dir, perms=0777, rw=os.R_OK|os.W_OK):
        if not os.path.isdir( dir ):
            try:
                os.makedirs(dir, perms)
            except OSError, e:
                print 'ERROR: failed to make dir %s: %i (%s)\n' % (dir, e.errno, e.strerror)
        if not os.access(dir, rw):
            print 'ERROR: directory %s is missing required r/w access\n' % dir

    def read_file(self,file_path):
        self.synthLab.handleJournalLoad(file_path)

    def write_file(self,file_path):
        self.synthLab.handleJournalSave(file_path)
