import random

class GenerationConstants:

    TWO_ROOT_TWELVE = pow( 2, 1./12 )
    MAX_NOTES_PER_BAR = 12

    PHRASE_LENGTH = 4
    PHRASE_COMPLEXITY = .5

    TABLE_ONSET_VALUES = [ 3, 6, 3, 4, 3, 6, 12, 6, 8, 6, 12, 18, 12, 24, 18, 36, 24, 36, 48 ]

    # scaling constants
    MAJOR = 0
    HARMONIC_MINOR = 1
    NATURAL_MINOR = 2
    PHRYGIEN = 3
    DORIEN = 4
    LYDIEN = 5
    MYXOLYDIEN = 6
                               
    SCALES = { MAJOR : [ -12, -10, -8, -7, -5, -3, -1, 0, 2, 4, 5, 7, 9, 11, 12 ],    
                        HARMONIC_MINOR : [ -12, -10, -9, -7, -5, -4, -1, 0, 2, 3, 5, 7, 8, 11, 12 ],
                        NATURAL_MINOR : [ -12, -10, -9, -7, -5, -4, -2, 0, 2, 3, 5, 7, 8, 10, 12 ],
                        PHRYGIEN : [ -12, -11, -9, -7, -5, -4, -2, 0, 1, 3, 5, 7, 8, 10, 12 ], 
                        DORIEN : [ -12, -10, -9, -7, -5, -3, -2, 0, 2, 3, 5, 7, 9, 10, 12 ], 
                        LYDIEN : [ -12, -10, -8, -6, -5, -3, -1, 0, 2, 4, 6, 7, 9, 11, 12 ], 
                        MYXOLYDIEN : [ -12, -10, -8, -7, -5, -3, -2, 0, 2, 4, 5, 7, 9, 10, 12 ]}


    # Default parameters for algorithmic generation

    RYTHM_DENSITY_BANK = [.4, 1., .92, .8, .22]
    RYTHM_REGU_BANK = [.75, .8, .85, .66, .5]
    PITCH_REGU_BANK = [.5, .8, .5, 0, .9]
    PITCH_STEP_BANK = [.5, .7, .15, .8, .15] 
    DURATION_BANK = [.8, .8, .8, .87, 1]
    SILENCE_BANK = [.2, .5, .4, .45, .12]
    PATTERN_BANK = [0, 3, 1, 2, 1]
    SCALE_BANK = [MAJOR, NATURAL_MINOR, LYDIEN, HARMONIC_MINOR, MYXOLYDIEN]

    chooseDefault = random.randint(0,4)
    DEFAULT_DENSITY = RYTHM_DENSITY_BANK[chooseDefault]
    DEFAULT_RYTHM_REGULARITY = RYTHM_REGU_BANK[chooseDefault]
    DEFAULT_PITCH_REGULARITY = PITCH_REGU_BANK[chooseDefault]
    DEFAULT_STEP = PITCH_STEP_BANK[chooseDefault]
    DEFAULT_DURATION = DURATION_BANK[chooseDefault]
    DEFAULT_SILENCE = SILENCE_BANK[chooseDefault]
    DEFAULT_PATTERN = PATTERN_BANK[chooseDefault]
    DEFAULT_SCALE = SCALE_BANK[chooseDefault]

    DEFAULT_RYTHM_METHOD = 0
    DEFAULT_PITCH_METHOD = 0
    DEFAULT_PAN = 0.5

    DEFAULT_PITCH_VARIATION = 0  # 0 = 'melodic' 1 = 'harmonic' 
    DEFAULT_RYTHM_VARIATION = 0  # 0 = 'Cellule' 1 = 'Xnoise'

    DEFAULT_TONIQUE = 36

    I = [ 0, 2, 4, 7, 9, 11, 14 ]
    II = [ 1, 3, 5, 8, 10, 12 ]
    III = [ 2, 4, 6, 9, 11, 13 ]
    IV = [ 0, 3, 5, 7, 10, 12, 14 ]
    V = [ 1, 4, 6, 8, 11, 13 ]
    VI = [ 0, 2, 5, 7, 9, 12, 14 ]
    VII = [ 1, 3, 6, 8, 10, 13 ]

    CHORDS_TABLE = [ I, V, I, II, V, I, VI, II, V, I, IV, VI, II, V, I, V, VI ]
#    CHORDS_TABLE = [I, V, I, V, I, V, I, V, I, V, I, V, I, V ]
    # pitch patterns constants
 #   PITCH_PATTERNS = [ 'Drunk', 'DroneAndJump', 'Repeter', 'Loopseg' ]

    # Parameters for probability scaling function
    REPETITION_SCALE_MIN_MAPPING = 0
    REPETITION_SCALE_MAX_MAPPING = 25
    REPETITION_SCALE_STEPS = 25
    DENSITY_SCALE_MIN_MAPPING = 0
    DENSITY_SCALE_MAX_MAPPING = 38
    DENSITY_SCALE_STEPS = 38
    ARTICULATION_SCALE_MIN_MAPPING = .6
    ARTICULATION_SCALE_MAX_MAPPING = 1
    ARTICULATION_SCALE_STEPS = 10

    # Rythmic durations, in ticks, and how many to complete figure (celluleRythmSequence)
    DOUBLE_TICK_DUR = 3
    DOUBLE_HOW_MANY = 2
    HALF_TRIPLET_TICK_DUR = 4
    HALF_TRIPLET_HOW_MANY = 3
    HOLE_TRIPLET_TICK_DUR = 8
    HOLE_TRIPLET_HOW_MANY = 3

    # Random generators default values (xnoiseRythmSequence)
    RANDOM_BETA_PARAM = 0.004
    RANDOM_EXPO_PARAM = 5
    RANDOM_GAUSS_PARAM1 = 0.5
    RANDOM_GAUSS_PARAM2 = 0.1
    RANDOM_WEIBULL_PARAM1 = 0.5

    RANDOM_WEIBULL_PARAM2 = 2.5

    # Onsets probability tables (drumRythmSequence)

    PUNCH_ACCENTS = [ [],
                      [ 0 ],
                      [ 0, 1 ],
                      [ 0, 2, 1 ],
                      [ 0, 2, 3, 1 ],
                      [ 0, 3, 2, 4, 1],
                      [ 0, 3, 2, 5, 1, 4 ],
                      [ 0, 2, 4, 6, 5, 3, 1 ],
                      [ 0, 4, 2, 6, 3, 7, 5, 1 ],
                      [ 0, 4, 6, 2, 8, 5, 3, 7, 1],
                      [ 0, 6, 4, 8, 2, 5, 7, 3, 9, 1],
                      [ 0, 4, 6, 10, 8, 2, 5, 7, 9, 3, 1],
                      [0, 6, 4, 2, 8, 10, 7, 5, 3, 9, 11, 1] ]

 
    LOW_ACCENTS = [ [],
                    [ 0 ],
                    [ 0, 1 ],
                    [ 0, 2, 1 ],
                    [ 0, 2, 3, 1 ],
                    [ 0, 3, 2, 4, 1 ],
                    [ 0, 3, 2, 5, 1, 4 ],
                    [ 0, 2, 4, 6, 5, 3, 1 ],
                    [ 0, 4, 2, 6, 3, 7, 5, 1 ],
                    [ 0, 4, 6, 2, 8, 5, 3, 7, 1 ],
                    [ 0, 6, 4, 8, 2, 5, 7, 3, 9, 1 ],
                    [ 0, 4, 6, 10, 8, 2, 5, 7, 9, 3, 1 ],
                    [0, 6, 4, 2, 8, 10, 7, 5, 3, 9, 11, 1 ] ]
                                          
    MID_ACCENTS = [   [],
        [ 0, 1 ],
        [ 0, 2, 3, 1 ],
        [ 0, 2, 4, 3, 1, 5 ],    
        [ 0, 4, 6, 2, 7, 1, 3, 5 ],
        [ 0, 6, 4, 8, 2, 1, 5, 3, 9, 7 ],
        [ 0, 6, 11, 5, 3, 9, 10, 2, 8, 7, 1, 4 ],
        [ 0, 4, 8, 12, 10, 13, 11, 9, 3, 2, 6, 5, 7, 1 ],
        [ 0, 8, 4, 12, 6, 14, 2, 10, 7, 15, 1, 9, 3, 11, 5, 13 ],
        [ 0, 8, 16, 4, 12, 14, 6, 2, 10, 7, 15, 1, 9, 3, 17, 11, 5, 13],
        [ 0, 10, 8, 4, 16, 12, 6, 14, 18, 2, 7, 9, 15, 3, 1, 19, 5, 11, 13, 17],
        [ 0, 8, 10, 16, 4, 20, 6, 12, 18, 14, 2, 9, 7, 3, 15, 21, 19, 1, 5, 11, 17, 13],
        [ 0, 10, 8, 4, 16, 6, 20, 22, 18, 12, 2, 14, 7, 9, 15, 3, 19, 1, 21, 5, 23, 17, 11, 13]  ]

    HIGH_ACCENTS = [   [],
        [ 1, 0 ],
        [ 1, 3, 2, 0 ],
        [ 5, 1, 3, 4, 2, 0 ],    
        [ 5, 3, 1, 7, 2, 6, 4, 0 ],
        [ 7, 9, 3, 5, 1, 2, 8, 4, 6, 0 ],
        [ 4, 1, 7, 5, 3, 9, 10, 2, 8, 11, 6, 0 ],
        [ 1, 7, 8, 5, 10, 13, 11, 9, 3, 2, 6, 12, 4, 0 ],
        [ 13, 5, 11, 3, 9, 1, 15, 10, 7, 2, 14, 6, 12, 4, 8, 0 ],
        [ 13, 5, 11, 17, 3, 9, 1, 15, 7, 10, 2, 6, 14, 12, 4, 16, 8, 0 ],
        [ 17, 13, 11, 5, 19, 1, 3, 15, 9, 7, 2, 18, 14, 6, 12, 16, 4, 8, 10, 0 ],
        [ 13, 17, 11, 5, 1, 19, 21, 15, 3, 7, 9, 2, 14, 18, 12, 6, 20, 4, 16, 10, 8, 0 ],
        [ 13, 11, 17, 23, 5, 21, 1, 19, 3, 15, 9, 7, 14, 2, 12, 18, 22, 20, 6, 16, 4, 8, 10, 0 ]  ]

    DRUM_PUNCH_ACCENTS = [[], [0], [0, 12], [0, 24, 12], [0, 24, 36, 12], [0, 36, 24, 48, 12], [0, 36, 24, 60, 12, 48], [0, 24, 48, 72, 60, 36, 12], [0, 48, 24, 72, 36, 84, 60, 12], [0, 48, 72, 24, 96, 60, 36, 84, 12], [0, 72, 48, 96, 24, 60, 84, 36, 108, 12], [0, 48, 72, 120, 96, 24, 60, 84, 108, 36, 12], [0, 72, 48, 24, 96, 120, 84, 60, 36, 108, 132, 12]]
    DRUM_LOW_ACCENTS = [[], [0], [0, 12], [0, 24, 12], [0, 24, 36, 12], [0, 36, 24, 48, 12], [0, 36, 24, 60, 12, 48], [0, 24, 48, 72, 60, 36, 12], [0, 48, 24, 72, 36, 84, 60, 12], [0, 48, 72, 24, 96, 60, 36, 84, 12], [0, 72, 48, 96, 24, 60, 84, 36, 108, 12], [0, 48, 72, 120, 96, 24, 60, 84, 108, 36, 12], [0, 72, 48, 24, 96, 120, 84, 60, 36, 108, 132, 12]]
    DRUM_MID_ACCENTS = [[], [0, 6], [0, 12, 18, 6], [0, 12, 24, 18, 6, 30], [0, 24, 36, 12, 42, 6, 18, 30], [0, 36, 24, 48, 12, 6, 30, 18, 54, 42], [0, 36, 66, 30, 18, 54, 60, 12, 48, 42, 6, 24], [0, 24, 48, 72, 60, 78, 66, 54, 18, 12, 36, 30, 42, 6], [0, 48, 24, 72, 36, 84, 12, 60, 42, 90, 6, 54, 18, 66, 30, 78], [0, 48, 96, 24, 72, 84, 36, 12, 60, 42, 90, 6, 54, 18, 102, 66, 30, 78], [0, 60, 48, 24, 96, 72, 36, 84, 108, 12, 42, 54, 90, 18, 6, 114, 30, 66, 78, 102], [0, 48, 60, 96, 24, 120, 36, 72, 108, 84, 12, 54, 42, 18, 90, 126, 114, 6, 30, 66, 102, 78], [0, 60, 48, 24, 96, 36, 120, 132, 108, 72, 12, 84, 42, 54, 90, 18, 114, 6, 126, 30, 138, 102, 66, 78]]
    DRUM_HIGH_ACCENTS = [[], [6, 0], [6, 18, 12, 0], [30, 6, 18, 24, 12, 0], [30, 18, 6, 42, 12, 36, 24, 0], [42, 54, 18, 30, 6, 12, 48, 24, 36, 0], [24, 6, 42, 30, 18, 54, 60, 12, 48, 66, 36, 0], [6, 42, 48, 30, 60, 78, 66, 54, 18, 12, 36, 72, 24, 0], [78, 30, 66, 18, 54, 6, 90, 60, 42, 12, 84, 36, 72, 24, 48, 0], [78, 30, 66, 102, 18, 54, 6, 90, 42, 60, 12, 36, 84, 72, 24, 96, 48, 0], [102, 78, 66, 30, 114, 6, 18, 90, 54, 42, 12, 108, 84, 36, 72, 96, 24, 48, 60, 0], [78, 102, 66, 30, 6, 114, 126, 90, 18, 42, 54, 12, 84, 108, 72, 36, 120, 24, 96, 60, 48, 0], [78, 66, 102, 138, 30, 126, 6, 114, 18, 90, 54, 42, 84, 12, 72, 108, 132, 120, 36, 96, 24, 48, 60, 0]]

    # Gain boundaries
    GAIN_MAX_BOUNDARY = 1.
    GAIN_MID_MAX_BOUNDARY = .9
    GAIN_MID_MIN_BOUNDARY = .75
    GAIN_MIN_BOUNDARY = .65

    # pitch mapping for drum kit
    DRUMPITCH = {25: 24, 27: 26, 29: 28, 31: 30, 33: 32, 35: 34, 37: 36, 39: 38, 41: 40, 43: 42, 45: 44, 47: 46 }

    DRUM_COMPLEXITY1 = [ [ 24 ], [30] , [ 40 ], [ 46 ]  ]
    DRUM_COMPLEXITY2 = [ [ 24, 28 ], [ 30, 32 ], [ 36, 38, 40 ], [ 46, 48 ]  ]
    DRUM_COMPLEXITY3 = [ [ 24, 26, 28 ], [ 30, 32, 34 ], [ 38, 40 ], [ 42, 46, 48 ]  ] 
    DRUM_COMPLEXITY4 = [ [ 24, 26, 28 ], [ 30, 32, 34 ], [ 38, 40 ], [ 42, 44, 46, 48 ]  ] 
 
    TRANSPOSE = [0.5, 0.52973154717964765, 0.56123102415468651, 0.59460355750136051, 0.6299605249474366, 0.66741992708501718, 0.70710678118654757, 0.74915353843834076, 0.79370052598409979, 0.8408964152537145, 0.89089871814033927, 0.94387431268169353, 1.0, 1.0594630943592953, 1.122462048309373, 1.189207115002721, 1.2599210498948732, 1.3348398541700344, 1.4142135623730951, 1.4983070768766815, 1.5874010519681994, 1.681792830507429, 1.7817974362806785, 1.8877486253633868, 2.0]

    CELLULES_MARKERS = [ 8, 16, 21, 24 ]
    CELLULES = [ [ 3, 3, 3, 3 ], [ 3, 3, 6 ], [ 3, 6, 3 ], [ 6, 3, 3 ], [ 4, 4, 4 ], [ 4, 8 ], [ 8, 4 ], [ 6, 6 ], [ 12 ], [ 6, 12, 6 ], [ 8, 8, 8 ], [ 8, 16 ], [ 16, 8 ], [ 12, 12 ], [ 18, 6 ], 
                                [ 6, 18 ], [ 24 ], [ 12, 12, 12 ], [ 18, 18 ], [ 24, 12 ], [ 12, 24 ], [ 36 ], [ 12, 24, 12 ], [ 24, 24 ], [ 48 ] ]

