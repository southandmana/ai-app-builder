import unittest
import signal
from cli_interface import chat_interface

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Test timed out")

class TestChatInterface(unittest.TestCase):

    def setUp(self):
        """Set up a timeout for each test."""
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(5)  # Set a 5-second timeout

    def tearDown(self):
        """Disable the timeout after each test."""
        signal.alarm(0)

    def test_valid_inputs(self):
        """Test chat interface with valid inputs."""
        print("[DEBUG] Running test_valid_inputs...")
        test_inputs = ["2", "3"]  # View progress, then exit
        try:
            chat_interface(test_inputs=test_inputs)
        except TimeoutException:
            self.fail("test_valid_inputs timed out")
        except Exception as e:
            self.fail(f"chat_interface raised an exception unexpectedly: {e}")

    def test_invalid_input(self):
        """Test chat interface with an invalid input."""
        print("[DEBUG] Running test_invalid_input...")
        test_inputs = ["invalid", "3"]  # Invalid input, then exit
        try:
            chat_interface(test_inputs=test_inputs)
        except TimeoutException:
            self.fail("test_invalid_input timed out")
        except Exception as e:
            self.fail(f"chat_interface raised an exception unexpectedly: {e}")

    def test_interrupted_input(self):
        """Test chat interface with simulated interruption."""
        print("[DEBUG] Running test_interrupted_input...")
        test_inputs = []  # Simulate no input (EOFError)
        try:
            chat_interface(test_inputs=test_inputs)
        except TimeoutException:
            self.fail("test_interrupted_input timed out")
        except Exception as e:
            self.fail(f"chat_interface raised an exception unexpectedly: {e}")

if __name__ == "__main__":
    # Run tests individually to isolate issues
    suite = unittest.TestSuite()
    suite.addTest(TestChatInterface("test_valid_inputs"))
    suite.addTest(TestChatInterface("test_invalid_input"))
    suite.addTest(TestChatInterface("test_interrupted_input"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
