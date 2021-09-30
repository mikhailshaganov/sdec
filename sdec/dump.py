import click
import serial
import sys


@click.command()
def dump():
    # TODO Find a way to not hardcode this
    ser = serial.Serial("/dev/cu.usbserial-140")
    ser.flushInput()
    ser.baudrate = 115200
    ser.timeout = 3

    while True:
        try:
            print(ser.readline().decode("utf-8"))
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            break
