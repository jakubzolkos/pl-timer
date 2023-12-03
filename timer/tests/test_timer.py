from unittest import TestCase, mock
from timer.timer import Timer

class TimerTests(TestCase):
    """
    Test Timer.
    """
    def setUp(self):
        self.app = Timer()

    def test_run(self):
        """
        Test the run code.
        """
        args = ['--time', '2']

        with mock.patch('builtins.print') as mock_print:
            options = self.app.parse_args(args)
            self.app.run(options)
            self.assertEqual(options.time, 2)
            mock_print.assert_any_call(f"Ran for {options.time} seconds")

