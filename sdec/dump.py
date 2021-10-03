import click
import serial
from rich import print


@click.command()
def dump():
    # TODO Find a way to not hardcode this
    ser = serial.Serial("/dev/cu.usbserial-140")
    ser.flushInput()
    ser.baudrate = 115200
    ser.timeout = 3

    while True:
        try:
            readings = ser.readline().decode("utf-8").split('\t')
            print('[red] {0} [orange] {0} [yellow] {0} [green] {0} [blue] {0} [violet] {0}'.format(*readings), end='\r')
        except KeyboardInterrupt:
            print("[red] :x: Keyboard interrupt")
            break
