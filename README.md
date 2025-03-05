# RGB led controller for Blackview MP100
This repository contains a simple python implementation of the RGB_LED_Tool.exe available bundled with Windows and available on any Blackview MP100 Mini PC. 

```
usage: led_control.py [-h] --port PORT --mode {1,2,3,4,5} --brightness {1,2,3,4,5} [--speed {1,2,3,4,5}]

LED Control CLI Tool

options:
  -h, --help            show this help message and exit
  --port PORT           Serial port (e.g., COM3 or /dev/ttyUSB0)
  --mode {1,2,3,4,5}    LED mode (1: rainbow, 2: breathing, 3: color loop, 4: off, 5: auto)
  --brightness {1,2,3,4,5}
                        Brightness level (1-5)
  --speed {1,2,3,4,5}   Speed level (1-5), default is 3
```
