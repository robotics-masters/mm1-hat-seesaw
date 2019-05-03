# Robo HAT MM1 - SeeSaw Repository.

## Introduction
This repository contains Examples and firmware files for Robo HAT MM1 for compatibility with SeeSaw.  [SeeSaw](https://github.com/adafruit/seesaw) is a GitHub Library currently maintained by Adafruit.

Seesaw is an open source microcontroller friend for other chips. It provides a
variety of capabilities such as UART, ADC, DAC, extra GPIO, etc. to chips that don't have them.

## Interfacing
- Arduino 
- CircuitPython
- Python

## Build SeeSaw

Please see the [mm1-hat-seesaw/firmware](https://github.com/robotics-masters/mm1-hat-seesaw/tree/master/firmware) folder for further instructions.

## Install SeeSaw for Python3.x

Please see the [mm1-hat-seesaw/circuitpython](https://github.com/robotics-masters/mm1-hat-seesaw/tree/master/circuitpython) folder for further instructions.

## Installing for Donkey Car

Assumes Python3 Installed.

```
pip install donkeycar[pi]
sudo pip install adafruit-circuitpython-seesaw
sudo pip install adafruit_circuitpython_motor
donkeycar createcar ~/mycar
```

Follow SeeSaw install instructions for circuitpython.
