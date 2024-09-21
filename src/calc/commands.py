import click
# This line import the power_mod function from calculator module
from calculator import power_mod


@click.group()
def calc_cli():
    pass

# First calc_cli.command() wrap this function to be a command under calc_cli group
# Second and third wrapper add the options to the command
# Note the arguments of the function will match the option name specified,
# click will try to find matching arg parsed and pass to the function


@calc_cli.command()
@click.option('--base', default=1, help='base of a number')
@click.option('--power', default=0, help='power for the number')
def power(base, power):
    """ Simple program that calculate base number raise to the poer
    """
    click.echo(power_mod.powerup(base, power))
