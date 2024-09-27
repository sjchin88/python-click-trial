""" main entry point for calc cli
"""
import click

from calc.commands import calc_cli


@click.group()
def cli():
    """ create the cli group
    """
    pass


# this line add the calc_cli group command to the command line group cli
cli.add_command(calc_cli)
