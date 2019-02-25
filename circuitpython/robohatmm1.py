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

# The ordering here reflects the seesaw firmware (mm1_hat) pinmap for Robo HAT MM1,
# not logical ordering of the HAT terminals.

_ROBOMM1_SIGNAL1 = const(34) # PWM
_ROBOMM1_SIGNAL2 = const(35) # PWM
_ROBOMM1_SIGNAL3 = const(40) # ADC/PWM
_ROBOMM1_SIGNAL4 = const(41) # ADC/PWM
_ROBOMM1_SIGNAL5 = const(15) # PWM
_ROBOMM1_SIGNAL6 = const(18) # PWM
_ROBOMM1_SIGNAL7 = const(54) # not used, serial port
_ROBOMM1_SIGNAL8 = const(55) # not used, serial port
_ROBOMM1_SIGNAL9 = const(2)  # ADC
_ROBOMM1_SIGNAL10 = const(3) # ADC
_ROBOMM1_SIGNAL11 = const(12) # BOOT_LED

_ROBOMM1_SERVO8 = const(17)
_ROBOMM1_SERVO7 = const(16)
_ROBOMM1_SERVO6 = const(11)
_ROBOMM1_SERVO5 = const(10)
_ROBOMM1_SERVO4 = const(21)
_ROBOMM1_SERVO3 = const(20)
_ROBOMM1_SERVO2 = const(43)
_ROBOMM1_SERVO1 = const(42)

_ROBOMM1_RCH1 = const(4)
_ROBOMM1_RCH2 = const(5)
_ROBOMM1_RCH3 = const(6)
_ROBOMM1_RCH4 = const(7)

# seesaw firmware has indexed lists of pins by function.
# These "pin" numbers map to real PAxx, PBxx pins on the board implementing seesaaw
# They may or may not match.
# See seesaw/include/SeesawConfig.h and seesaw/boards/crickit/board_config.h for the pin choices.
# You must look at both files and combine the defaults in SeesawConfig.h with the
# overrides in crickit/board_config.h.
# PA<nn> pins are nn
# PB<nn> pins are 32+nn

class Robohat_Pinmap:
    # seesaw firmware (mm1_hat) analog pin map:
    # analog[0]:34    analog[1]:35    analog[2]: 2    analog[3]: 3
    # analog[4]:40    analog[5]:41    analog[6]:10    analog[7]:11
    # note:  analog[4:7] not enabled by default.
    # note:  analog[4:5] swappable with pwm[10:11]
    # note:  analog[6:7] swappable with pwm[4:5]
    # 
    analog_pins = (_CRICKIT_SIGNAL1, _CRICKIT_SIGNAL2,
                   _CRICKIT_SIGNAL9, _CRICKIT_SIGNAL10)#,
                   #_CRICKIT_SIGNAL3, _CRICKIT_SIGNAL4,
                   #_CRICKIT_SERVO5, _CRICKIT_SERVO6)

    pwm_width = 16

    # seesaw firmware (mm1_hat) pwm pin map:
    # pwm[0]:42    pwm[1]:43    pwm[2]:20    pwm[3]:21    pwm[4]:10    pwm[5]:11
    # pwm[6]:16    pwm[7]:17    pwm[8]:15    pwm[9]:18    pwm[10]:40   pwm[11]:41
    # note: pwm[10:11] swappable with analog[4:5]
    #
    pwm_pins = (_CRICKIT_SERVO1, _CRICKIT_SERVO2, _CRICKIT_SERVO3, _CRICKIT_SERVO4,
                _CRICKIT_SERVO5, _CRICKIT_SERVO6, _CRICKIT_SERVO7, _CRICKIT_SERVO8,
                _CRICKIT_SIGNAL5, _CRICKIT_SIGNAL6,
                _CRICKIT_SIGNAL3, _CRICKIT_SIGNAL4)

    # seesaw firmware touch pin map:
    # touch[0]: 4    touch[1]: 5    touch[2]: 6    touch[3]: 7
    touch_pins = (_CRICKIT_RCH1, _CRICKIT_RCH2, _CRICKIT_RCH3, _CRICKIT_RCH4)
