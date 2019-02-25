# SeeSaw Firmware
Use with https://github.com/adafruit/seesaw/

### boards/roboticsmasters_mm1/

## Build Steps

```
git clone https://github.com/adafruit/seesaw/
cd seesaw/
make BOARD=roboticsmasters_mm1
```

## Output

```
seesaw/builds
```


## Convert to UF2
```
# For programs with 0x2000 offset (default)
uf2conv.py -c -o build-circuitplayground_express/firmware.uf2 build-circuitplayground_express/firmware.bin

```


