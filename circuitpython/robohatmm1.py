# The MIT License (MIT)
#
# Copyright (c) 2019 wallarug for Robotics Masters
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# pylint: disable=missing-docstring,invalid-name,too-many-public-methods,too-few-public-methods

from micropython import const

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_seesaw.git"

# The ordering here reflects the seesaw firmware pinmap for crickit,
# not logical ordering of the crickit terminals.

_MM1HAT_SIGNAL1 = const(2)
_MM1HAT_SIGNAL2 = const(3)
_MM1HAT_SIGNAL3 = const(40)
_MM1HAT_SIGNAL4 = const(41)
_MM1HAT_SIGNAL5 = const(11)
_CRICKIT_SIGNAL6 = const(10)
_CRICKIT_SIGNAL7 = const(9)
_CRICKIT_SIGNAL8 = const(8)

_CRICKIT_SERVO4 = const(14)
_CRICKIT_SERVO3 = const(15)
_CRICKIT_SERVO2 = const(16)
_CRICKIT_SERVO1 = const(17)

_CRICKIT_MOTOR2B = const(18)
_CRICKIT_MOTOR2A = const(19)
_CRICKIT_MOTOR1A = const(22)
_CRICKIT_MOTOR1B = const(23)
_CRICKIT_DRIVE4 = const(42)
_CRICKIT_DRIVE3 = const(43)
_CRICKIT_DRIVE2 = const(12)
_CRICKIT_DRIVE1 = const(13)

_CRICKIT_CAPTOUCH1 = const(4)
_CRICKIT_CAPTOUCH2 = const(5)
_CRICKIT_CAPTOUCH3 = const(6)
_CRICKIT_CAPTOUCH4 = const(7)

# seesaw firmware has indexed lists of pins by function.
# These "pin" numbers map to real PAxx, PBxx pins on the board implementing seesaaw
# They may or may not match.
# See seesaw/include/SeesawConfig.h and seesaw/boards/crickit/board_config.h for the pin choices.
# You must look at both files and combine the defaults in SeesawConfig.h with the
# overrides in crickit/board_config.h.
# PA<nn> pins are nn
# PB<nn> pins are 32+nn

class Crickit_Pinmap:
    # seesaw firmware analog pin map:
    # analog[0]: 2    analog[1]: 3    analog[2]:40    analog[3]:41
    # analog[4]:11    analog[5]:10    analog[6]: 9    analog[7]: 8
    # no special remapping: same order as constants above
    analog_pins = (_CRICKIT_SIGNAL1, _CRICKIT_SIGNAL2,
                   _CRICKIT_SIGNAL3, _CRICKIT_SIGNAL4,
                   _CRICKIT_SIGNAL5, _CRICKIT_SIGNAL6,
                   _CRICKIT_SIGNAL7, _CRICKIT_SIGNAL8)

    pwm_width = 16

    # seesaw firmware pwm pin map:
    # pwm[0]:14    pwm[1]:15    pwm[2]:16    pwm[3]:17    pwm[4]:18    pwm[5]:19
    # pwm[6]:22    pwm[7]:23    pwm[8]:42    pwm[9]:43    pwm[10]:12   pwm[11]:13
    # Note that servo pins are in reverse order (17-14), and motor pins are shuffled.
    pwm_pins = (_CRICKIT_SERVO4, _CRICKIT_SERVO3, _CRICKIT_SERVO2, _CRICKIT_SERVO1,
                _CRICKIT_MOTOR2B, _CRICKIT_MOTOR2A,
                _CRICKIT_MOTOR1A, _CRICKIT_MOTOR1B,
                _CRICKIT_DRIVE4, _CRICKIT_DRIVE3,
                _CRICKIT_DRIVE2, _CRICKIT_DRIVE1)

    # seesaw firmware touch pin map:
    # touch[0]: 4    touch[1]: 5    touch[2]: 6    touch[3]: 7
touch_pins = (_CRICKIT_CAPTOUCH1, _CRICKIT_CAPTOUCH2, _CRICKIT_CAPTOUCH3, _CRICKIT_CAPTOUCH4)
