import unittest
import sys
import io
import os
from unittest.mock import patch
from pathlib import Path

# We import the main function from your script
from remove_comments import main

class TestRemoveComments(unittest.TestCase):
    def setUp(self):
        # Define paths to input and expected output files
        self.input_file = Path(__file__).parent / "test_input.c"
        self.expected_file = Path(__file__).parent / "expected_output.c"
        
        # Make sure these files exist
        if not self.input_file.is_file():
            self.fail(f"Input file not found: {self.input_file}")
        if not self.expected_file.is_file():
            self.fail(f"Expected output file not found: {self.expected_file}")

    def test_comment_removal(self):
        # Read expected output
        with open(self.expected_file, 'r') as ef:
            expected_output = ef.read()

        # Capture stdout to compare after running main()
        captured_output = io.StringIO()
        with patch.object(sys, 'argv', ['remove_comments', str(self.input_file)]):
            with patch('sys.stdout', new=captured_output):
                main()

        # Get the printed output from the script
        actual_output = captured_output.getvalue()

        # Compare actual and expected
        self.assertEqual(
            actual_output,
            expected_output,
            "The output after comment removal does not match the expected output."
        )

if __name__ == '__main__':
    unittest.main()
