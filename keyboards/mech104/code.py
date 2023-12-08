#KMK Layout for MECH-104 using YD-RP2040 board. If this is your first time be aware you have to desolder an LED,
# the USRKEY button, tap into the big LED to make enough pins available using this layout. The more correct way to
# this would be make a correct grid instead of filling spaces with KC.NO

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP6,  board.GP7,
                     board.GP8,  board.GP9,
                     board.GP10, board.GP11, 
                     board.GP12, board.GP13, 
                     board.GP14, board.GP15, 
                     board.GP16, board.GP17, 
                     board.GP18, board.GP19, 
                     board.GP20, board.GP21, 
                     board.GP22, board.GP23, 
                     board.BUTTON, board.LED, 
                     board.GP26, board.GP27,)


keyboard.row_pins = (board.GP0, board.GP1, board.GP2, 
                     board.GP3, board.GP4, board.GP5,)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.ESCAPE,  KC.NO,  KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.NO,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9,    KC.F10,   KC.F11,   KC.F12,           KC.PSCR,  KC.SLCK,  KC.PAUS,    KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.GRAVE,   KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5,  KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N0,  KC.MINUS, KC.EQL,   KC.NO,    KC.BSPACE,        KC.INS,   KC.HOME,  KC.PGUP,    KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS,
        KC.TAB,     KC.NO,  KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,     KC.LBRC,  KC.RBRC,  KC.BSLS,          KC.DEL,   KC.END,   KC.PGDN,    KC.P7,   KC.P8,   KC.P9,   KC.PPLS,
        KC.CAPS,    KC.NO,  KC.A,   KC.S,   KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   KC.L,   KC.SCLN,  KC.QUOT,  KC.ENTER, KC.NO,KC.NO,KC.NO,KC.NO,                          KC.P4,   KC.P5,   KC.P6,
        KC.NO, KC.NO,KC.LSHIFT, KC.Z, KC.X, KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM,KC.DOT, KC.SLSH,  KC.NO,    KC.RSHIFT,KC.NO,KC.NO,               KC.UP,   KC.NO,        KC.P1,   KC.P2,   KC.P3,   KC.PENT,
        KC.LCTRL,KC.LWIN,KC.NO,KC.LALT,KC.NO,KC.NO, KC.SPACE,KC.NO, KC.NO,  KC.NO,  KC.RALT,KC.RWIN,KC.NO,    KC.WINMENU,KC.RCTRL,                  KC.LEFT, KC.DOWN, KC.RIGHT,     KC.P0,KC.NO, KC.KP_DOT, 
    ]
]


if __name__ == '__main__':
    keyboard.go()