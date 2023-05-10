import sys
import unittest
from src import IsWSL

# To test if IsWSL works correctly, we must know whether we trully are in WSL or not.
# Doing that automatically would be circular logic, so instead we pass it as an argument
# from outside.
platform = ""


def usage() -> str:
    return """Usage:

python3 is_wsl_test.py --help        Print this message and exit.
python3 is_wsl_test.py PLATFORM      Run the test suite.

PLATFORM
    The machine or container you're running the tests in. Either WSL or something else.
"""


class TestIsWSL(unittest.TestCase):
    def test_IsWsl(self):
        got = IsWSL()

        if platform.lower() == "wsl":
            self.assertTrue(
                got, f"expected IsWSL to return true in platform {platform}"
            )
            return

        self.assertFalse(got, f"expected IsWSL to return false in platform {platform}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(usage())
        sys.exit(5)
    if sys.argv[1] == "--help":
        print(usage())
        sys.exit(0)

    platform = sys.argv[1]
    runner = unittest.TextTestRunner()

    suite = unittest.TestSuite()
    suite.addTests([unittest.TestLoader().loadTestsFromTestCase(TestIsWSL)])

    r = runner.run(suite)
    if r.wasSuccessful():
        sys.exit(0)
    sys.exit(1)