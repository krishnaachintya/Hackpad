import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.keys import KC


keymap = [
    KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,  # Row 0
    KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,   # Row 1
    KC.A,  KC.S,  KC.D,  KC.F,  KC.G,   # Row 2
    KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,   # Row 3
]

encoders = [
    ((board.GP10, board.GP11, board.GP12), (KC.VOLU, KC.VOLD, KC.MUTE)),
    ((board.GP13, board.GP14, board.GP15), (KC.RIGHT, KC.LEFT, KC.ENTER)),
    ((board.GP16, board.GP17, board.GP18), (KC.UP, KC.DOWN, KC.SPACE)),
    ((board.GP19, board.GP20, board.GP21), (KC.MNXT, KC.MPRV, KC.MPLY)),
]

class Macropad(KMKKeyboard):
    def __init__(self):
        
        self.row_pins = [board.GP5, board.GP6, board.GP7, board.GP8]
        self.col_pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4]
        self.diode_orientation = 'COL2ROW' 
        
        
        self.encoder_handler = EncoderHandler()
        for (a, b, sw), (cw, ccw, press) in encoders:
            self.encoder_handler.pins.append((a, b, sw))
            self.encoder_handler.map.append((cw, ccw, press))
        self.modules.append(self.encoder_handler)
        
       
        self.matrix = KeysScanner(keymap)

keyboard = Macropad()
keyboard.go()
