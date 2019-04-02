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
"""
`rmasters_robohat`
==========================

Convenience library for using the Robotics Masters Robo HAT robotics boards.

* Author(s): wallarug

Implementation Notes
--------------------

**Hardware:**

   `Adafruit Crickit for Circuit Playground Express <https://www.adafruit.com/3093>`_
   `Adafruit Crickit FeatherWing <https://www.adafruit.com/3343>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
"""

import sys

import board
import busio

from micropython import const

#pylint: disable=wrong-import-position
try:
    lib_index = sys.path.index("/lib")        # pylint: disable=invalid-name
    if lib_index < sys.path.index(".frozen"):
        # Prefer frozen modules over those in /lib.
        sys.path.insert(lib_index, ".frozen")
except ValueError:
    # Don't change sys.path if it doesn't contain "lib" or ".frozen".
    pass

from adafruit_seesaw.seesaw import Seesaw
from adafruit_seesaw.robohat import MM1_Pinmap
from adafruit_seesaw.pwmout import PWMOut
from adafruit_motor.servo import Servo, ContinuousServo
from adafruit_motor.motor import DCMotor
from adafruit_motor.stepper import StepperMotor

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Crickit.git"


_SERVO1 = const(16)
_SERVO2 = const(17)
_SERVO3 = const(18)
_SERVO4 = const(19)
_SERVO5 = const(11)
_SERVO6 = const(10)
_SERVO7 = const(9)
_SERVO8 = const(8)

_servoPins = [_SERVO1, _SERVO2, _SERVO3, _SERVO4,
           _SERVO5, _SERVO6, _SERVO7, _SERVO8]

_RCH1 = const(7)
_RCH2 = const(6)
_RCH3 = const(5)
_RCH4 = const(4)

_NEOPIXEL = const(20)

#pylint: disable=too-few-public-methods
class MM1TouchIn:
    """Imitate touchio.TouchIn."""
    def __init__(self, seesaw, pin):
        self._seesaw = seesaw
        self._pin = pin
        self.threshold = self.raw_value + 100

    @property
    def raw_value(self):
        """The raw touch measurement as an `int`. (read-only)"""
        return self._seesaw.touch_read(self._pin)

    @property
    def value(self):
        """Whether the touch pad is being touched or not. (read-only)"""
        return self.raw_value > self.threshold


#pylint: disable=too-many-public-methods
class RoboMM1:
    """Represents a Robo HAT MM1 board. Provides a number of devices available via properties, such as
    ``servo_1``. Devices are created on demand the first time they are referenced.

    It's fine to refer a device multiple times via its property, but it's faster and results
    in more compact code to assign a device to a variable.

    .. code-block:: python

      import time
      from adafruit_crickit import crickit

      # This is fine:
      crickit.servo_1.angle = 0
      time.sleep(1)
      crickit.servo_1.angle = 90
      time.sleep(1)

      # This is slightly faster and more compact:
      servo_1 = crickit.servo_1
      servo_1.angle = 0
      time.sleep(1)
      servo_1.angle = 90
      time.sleep(1)
    """
    SIGNAL0 = 55 # (RX to RPI_TX)
    SIGNAL1 = 54 # (TX to RPI_RX)
    SIGNAL2 = 48 # ADC (GPS_RX)
    SIGNAL3 = 47 # ADC (GPS_TX)
    SIGNAL4 = 0 # (GPS_SDA)
    SIGNAL5 = 1 # (GPS_SCL)
    SIGNAL6 = 2 # (POWER_ENABLE)
    SIGNAL7 = 3 # (BUTTON)
    SIGNAL8 = 20 # (NEOPIXEL) 
    SIGNAL9 =  43 # PWM (SPI_SCK)
    SIGNAL10 = 41 # PWM (SPI_SS)
    SIGNAL11 = 42 # PWM (SPI_MOSI)
    SIGNAL12 = 40 # PWM (SPI_MISO)
    SIGNAL13 = 21 # BOOT_LED

    def __init__(self, seesaw):
        self._seesaw = seesaw
        self._seesaw.pin_mapping = MM1_Pinmap
        # Associate terminal(s) with certain devices.
        # Used to find existing devices.
        self._devices = dict()
        self._neopixel = None

    @property
    def seesaw(self):
        """The Seesaw object that talks to the Crickit. Use this object to manipulate the
        signal pins that correspond to Crickit terminals.

        .. code-block:: python

          from adafruit_crickit import crickit

          ss = crickit.seesaw
          ss.pin_mode(crickit.SIGNAL4, ss.OUTPUT)
          ss.digital_write(crickit.SIGNAL4], True)
        """

        return self._seesaw

    @property
    def servo_1(self):
        """``adafruit_motor.servo.Servo`` object on Servo 1 terminal"""
        return self._servo(_SERVO1, Servo)

    @property
    def servo_2(self):
        """``adafruit_motor.servo.Servo`` object on Servo 2 terminal"""
        return self._servo(_SERVO2, Servo)

    @property
    def servo_3(self):
        """``adafruit_motor.servo.Servo`` object on Servo 3 terminal"""
        return self._servo(_SERVO3, Servo)

    @property
    def servo_4(self):
        """``adafruit_motor.servo.Servo`` object on Servo 4 terminal"""
        return self._servo(_SERVO4, Servo)

    @property
    def servo_5(self):
        """``adafruit_motor.servo.Servo`` object on Servo 5 terminal"""
        return self._servo(_SERVO5, Servo)

    @property
    def servo_6(self):
        """``adafruit_motor.servo.Servo`` object on Servo 6 terminal"""
        return self._servo(_SERVO6, Servo)

    @property
    def servo_7(self):
        """``adafruit_motor.servo.Servo`` object on Servo 7 terminal"""
        return self._servo(_SERVO7, Servo)

    @property
    def servo_8(self):
        """``adafruit_motor.servo.Servo`` object on Servo 8 terminal"""
        return self._servo(_SERVO8, Servo)
    

    @property
    def continuous_servo_1(self):
        """``adafruit_motor.servo.ContinuousServo`` object on Servo 1 terminal"""
        return self._servo(_SERVO1, ContinuousServo)

    @property
    def continuous_servo_2(self):
        """``adafruit_motor.servo.ContinuousServo`` object on Servo 2 terminal"""
        return self._servo(_SERVO2, ContinuousServo)

    @property
    def continuous_servo_3(self):
        """``adafruit_motor.servo.ContinuousServo`` object on Servo 3 terminal"""
        return self._servo(_SERVO3, ContinuousServo)

    @property
    def continuous_servo_4(self):
        """``adafruit_motor.servo.ContinuousServo`` object on Servo 4 terminal"""
        return self._servo(_SERVO4, ContinuousServo)

    @property
    def continuous_servo_5(self):
        """``adafruit_motor.servo.ContinuousServo`` object on Servo 5 terminal"""
        return self._servo(_SERVO5, ContinuousServo)

    @property
    def continuous_servo_6(self):
        """``adafruit_motor.servo.ContinuousServo`` object on Servo 6 terminal"""
        return self._servo(_SERVO6, ContinuousServo)

    @property
    def continuous_servo_7(self):
        """``adafruit_motor.servo.ContinuousServo`` object on Servo 7 terminal"""
        return self._servo(_SERVO7, ContinuousServo)

    @property
    def continuous_servo_8(self):
        """``adafruit_motor.servo.ContinuousServo`` object on Servo 8 terminal"""
        return self._servo(_SERVO8, ContinuousServo)

    @property
    def anyservo(self, terminal):
        return self._servo(terminal, Servo)
    
    def _servo(self, terminal, servo_class):
        device = self._devices.get(terminal, None)
        if not isinstance(device, servo_class):
            pwm = PWMOut(self._seesaw, terminal)
            pwm.frequency = 50
            device = servo_class(pwm)
            self._devices[terminal] = device
        return device
        
    def _pulseout(self, terminal):
        device = self._devices.get(terminal, None)
        if not isinstance(device, Servo):
            pwm = PWMOut(self._seesaw, terminal)
            pwm.frequency = 50
            device = pwm
            self._devices[terminal] = device
        return device
            


    @property
    def touch_1(self):
        """``adafruit_crickit.CrickitTouchIn`` object on Touch 1 terminal"""
        return self._touch(_RCH1)

    @property
    def touch_2(self):
        """``adafruit_crickit.CrickitTouchIn`` object on Touch 2 terminal"""
        return self._touch(_RCH2)

    @property
    def touch_3(self):
        """``adafruit_crickit.CrickitTouchIn`` object on Touch 3 terminal"""
        return self._touch(_RCH3)

    @property
    def touch_4(self):
        """``adafruit_crickit.CrickitTouchIn`` object on Touch 4 terminal"""
        return self._touch(_RCH4)

    def _touch(self, terminal):
        touch_in = self._devices.get(terminal, None)
        if not touch_in:
            touch_in = MM1TouchIn(self._seesaw, terminal)
            self._devices[terminal] = touch_in
        return touch_in

    @property
    def neopixel(self):
        """```adafruit_seesaw.neopixel`` object on NeoPixel terminal.
        Raises ValueError if ``init_neopixel`` has not been called.
        """
        if not self._neopixel:
            raise ValueError("Call init_neopixel first")
        return self._neopixel


    def init_neopixel(self, n, *, bpp=3, brightness=1.0, auto_write=True, pixel_order=None):
        """Set up a seesaw.NeoPixel object

        .. note:: On the CPX Crickit board, the NeoPixel terminal is by default
          controlled by CPX pin A1, and is not controlled by seesaw. So this object
          will not be usable. Instead, use the regular NeoPixel library
          and specify ``board.A1`` as the pin.

        You can change the jumper connection on the bottom of the CPX Crickit board
        to move control of the NeoPixel terminal to seesaw pin #20 (terminal.NEOPIXEL).
        In addition, the Crickit FeatherWing always uses seesaw pin #20.
        In either of those cases, this object will work.

        .. code-block:: python

          from adafruit_crickit.crickit import crickit

          crickit.init_neopixel(24)
          crickit.neopixel.fill((100, 0, 0))
        """
        from adafruit_seesaw.neopixel import NeoPixel
        self._neopixel = NeoPixel(self._seesaw, _NEOPIXEL, n, bpp=bpp,
                                  brightness=brightness, auto_write=auto_write,
                                  pixel_order=pixel_order)

    def reset(self):
        """Reset the whole Crickit board."""
        self._seesaw.sw_reset()

robohat = None # pylint: disable=invalid-name
"""A singleton instance to control a single Crickit board, controlled by the default I2C pins."""

# Sphinx's board is missing real pins so skip the constructor in that case.
if "SCL" in dir(board):
    robohat = RoboMM1(Seesaw(busio.I2C(board.SCL, board.SDA))) # pylint: disable=invalid-name
