# Robo HAT MM1 - SeeSaw Python Libraries

These two libraries allow the SeeSaw to communicate with Python running on a Raspberry Pi or other CircuitPython boards.

## Adafruit_CircuitPython_Seesaw

This includes add-on scripts to be used with the [Adafruit_CircuitPython_seesaw](https://github.com/adafruit/Adafruit_CircuitPython_seesaw/) library.  The file(s) in this repository need to be copied into the correct directory that seesaw gets installed for Python.

## Adafruit_CircuitPython_RoboHat

This includes add-on scripts to enable communciation between the Robo HAT MM1 and the [Adafruit_CircuitPython_seesaw](https://github.com/adafruit/Adafruit_CircuitPython_seesaw/) library.  The file(s) in this repository need to be copied into the correct directory that seesaw gets installed for Python.

# Install

Please run all of the below commands in order.

**Map File**
```
git clone https://github.com/robotics-masters/mm1-hat-seesaw
cd mm1-hat-seesaw/circuitpython/Adafruit_CircuitPython_seesaw
cp robohat.py ~/.local/lib/python3.5/site-packages/adafruit_seesaw/robohat.py
```

**Control Library**
```
cd ../Adafruit_CircuitPython_RoboHat
cp rm_robohat.py ~/.local/lib/python3.5/site-packages/rm_robohat.py
```

# Usage - CircuitPython

Open up Python3 terminal.

## Geting Started.
```
>>> from rm_robohat.py import robohat.py
```

## Servo Control
```
>>> robohat.servo_1.angle = 90
```

## Signal Control
```
>>> ss = robohat.seesaw
>>> led = robohat.LED
>>> ss.pin_mode(led, OUTPUT)
>>> ss.digital_write(led, True)
```


Further instruction can be found using the [CircuitPython/SeeSaw guide by Adafruit Learn](https://learn.adafruit.com/adafruit-crickit-hat-for-raspberry-pi-linux-computers/python-installation).
