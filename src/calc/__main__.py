import click

from commands import calc_cli


@click.group()
def cli():
    pass


# this line add the commands.power function to the command line group cli
cli.add_command(calc_cli)
