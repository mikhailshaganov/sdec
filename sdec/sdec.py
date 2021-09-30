from sdec.actuate import actuate
from sdec.flash import flash
from sdec.dump import dump
import click


@click.group(help="CLI tool for interacting with the SDR embedded controller.")
def cli():
    pass


cli.add_command(actuate)
cli.add_command(dump)
cli.add_command(flash)

if __name__ == "main":
    cli()
