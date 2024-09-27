from calculator import power_mod

TEST_BASE = 2
TEST_POWER = 3
TEST_OUTCOME = 8


def test_power_up():
    actual_return = power_mod.powerup(base=TEST_BASE, power=TEST_POWER)
    assert actual_return == TEST_OUTCOME
