# SeeSaw Firmware
Use with https://github.com/adafruit/seesaw/


## Set Up Build Environment

Until our library is allowed to be included into the adafruit/seesaw repository, you must clone this repository and the seesaw repository.

```
git clone https://github.com/robotics-masters/mm1-hat-seesaw
git clone https://github.com/adafruit/seesaw/
cd seesaw/
cp -r ../mm1-hat-seesaw/firmware/mm1_hat boards/mm1_hat
```

## Build commands

The default board is `debug`. You can build a different one using:

```
make -j8 BOARD=mm1_hat
```

## Output

```
seesaw/builds
```

## Convert to UF2
```
# For programs with 0x2000 offset (default)
uf2conv.py -c -o build-mm1_hat/firmware.uf2 build-mm1_hat/firmware.bin

```

# Changing Pin Functions

SeeSaw has the ability to let you choose if a pin is PWM, ADC, SERCOM or other functions.  To edit the function of a pin, change the `mm1_hat/board_config.h` file and update the respective library pins. 

**For Example**

Original - SERVO 5 & SERVO 6 configured as PWM outputs.
```
#define CONFIG_TIMER_PWM_OUT4 1
#define CONFIG_TIMER_PWM_OUT4_IS_TCC
#define CONFIG_TIMER_PWM_OUT4_TC NOT_ON_TC
#define CONFIG_TIMER_PWM_OUT4_TCC TCC1
#define CONFIG_TIMER_PWM_OUT4_WO 0
#define CONFIG_TIMER_PWM_OUT4_PIN 10	   //PA10 - SERVO_05

#define CONFIG_TIMER_PWM_OUT5 1
#define CONFIG_TIMER_PWM_OUT5_IS_TCC
#define CONFIG_TIMER_PWM_OUT5_TC NOT_ON_TC
#define CONFIG_TIMER_PWM_OUT5_TCC TCC1
#define CONFIG_TIMER_PWM_OUT5_WO 1
#define CONFIG_TIMER_PWM_OUT5_PIN 11	   //PA11 - SERVO_06
```

Changed - SERVO 5 & SERVO 6 configured as ADC inputs
```
#define CONFIG_ADC_INPUT_4 0 // not used
#define CONFIG_ADC_INPUT_4_PIN 10 	  //PA10 - SERV0_05
#define CONFIG_ADC_INPUT_4_CHANNEL 18

#define CONFIG_ADC_INPUT_5 0 // not used
#define CONFIG_ADC_INPUT_5_PIN 11 	  //PA11 - SERV0_06
#define CONFIG_ADC_INPUT_5_CHANNEL 19
```

**NOTE:**  A pin can only be configured for a single use.  Please ensure that you comment out any other functions associated with that pin. 
