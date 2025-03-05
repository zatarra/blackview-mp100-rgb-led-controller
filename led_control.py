#!/usr/bin/env python3
import serial
import time
import argparse
import sys

def compute_checksum(data):
    """Compute the checksum as the sum of the first 4 bytes modulo 256."""
    return sum(data) & 0xFF

def send_data(port, data):
    """Open the serial port, send each byte with a slight delay, and close the port."""
    try:
        ser = serial.Serial(
            port=port,
            baudrate=9600,
            bytesize=serial.EIGHTBITS,
            stopbits=serial.STOPBITS_ONE,
            parity=serial.PARITY_NONE,
            timeout=0.2
        )
    except Exception as e:
        print("Error opening serial port:", e)
        sys.exit(1)

    try:
        for byte in data:
            ser.write(bytearray([byte]))
            # A 5-microsecond delay between sending each byte (as in the original code)
            time.sleep(0.000005)
    finally:
        ser.close()

def main():
    parser = argparse.ArgumentParser(description="LED Control CLI Tool")
    parser.add_argument("--port", required=True, help="Serial port (e.g., COM3 or /dev/ttyUSB0)")
    parser.add_argument("--mode", type=int, choices=range(1, 6), required=True,
                        help="LED mode (1: rainbow, 2: breathing, 3: color loop, 4: off, 5: auto)")
    parser.add_argument("--brightness", type=int, choices=range(1, 6), required=True,
                        help="Brightness level (1-5)")
    parser.add_argument("--speed", type=int, choices=range(1, 6), default=3,
                        help="Speed level (1-5), default is 3")
    args = parser.parse_args()

    # Compute the values according to the original logic:
    # Brightness and speed values are sent as (6 - level)
    brightness_byte = 6 - args.brightness
    speed_byte = 6 - args.speed

    # Build the 5-byte message:
    # Byte0: 250, Byte1: mode, Byte2: brightness, Byte3: speed, Byte4: checksum
    message = bytearray([250, args.mode, brightness_byte, speed_byte, 0])
    message[4] = compute_checksum(message[0:4])

    print("Sending data:", list(message))
    send_data(args.port, message)
    print("Data sent successfully.")

if __name__ == '__main__':
    main()
