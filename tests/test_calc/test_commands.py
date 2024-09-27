from click.testing import CliRunner
from calc import commands


def test_power():
    """ Test the power cli
    """
    runner = CliRunner()
    result = runner.invoke(commands.power, ['--base', '2', '--powers', '3'])
    assert result.exit_code == 0
    assert result.output.rstrip() == '8'
