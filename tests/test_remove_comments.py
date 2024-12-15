import unittest
import sys
import io
import os
from unittest.mock import patch
from pathlib import Path

from comment_parser import main

class TestSingleLine(unittest.TestCase):

    def setUp(self):
        # Define paths to input and expected output files
        self.input_file = Path(__file__).parent / "assets/test_single_line.c"
        self.expected_file = Path(__file__).parent / "assets/expected_single_line.c"

        if not self.input_file.is_file():
            self.fail(f"Input file not found: {self.input_file}")
        if not self.expected_file.is_file():
            self.fail(f"Expected output file not found: {self.expected_file}")

    def test_remove_comments(self):
        # Read expected output
        with open(self.expected_file, 'r') as ef:
            expected_output = ef.read()

        # Capture the output of the main function
        captured_output = io.StringIO()
        with patch.object(sys, 'argv', ['comment_parser', str(self.input_file)]):
            with patch('sys.stdout', new=captured_output):
                main()

        actual_output = captured_output.getvalue()

        # Directly compare the actual and expected outputs
        self.assertEqual(
            actual_output,
            expected_output,
            "The processed output does not match the expected output."
        )

class TestBlock(unittest.TestCase):

    def setUp(self):
        # Define paths to input and expected output files
        self.input_file = Path(__file__).parent / "assets/test_block.c"
        self.expected_file = Path(__file__).parent / "assets/expected_block.c"

        if not self.input_file.is_file():
            self.fail(f"Input file not found: {self.input_file}")
        if not self.expected_file.is_file():
            self.fail(f"Expected output file not found: {self.expected_file}")

    def test_remove_comments(self):
        # Read expected output
        with open(self.expected_file, 'r') as ef:
            expected_output = ef.read()

        # Capture the output of the main function
        captured_output = io.StringIO()
        with patch.object(sys, 'argv', ['comment_parser', str(self.input_file)]):
            with patch('sys.stdout', new=captured_output):
                main()

        actual_output = captured_output.getvalue()

        # Directly compare the actual and expected outputs
        self.assertEqual(
            actual_output,
            expected_output,
            "The processed output does not match the expected output."
        )

class TestMixed(unittest.TestCase):

    def setUp(self):
        # Define paths to input and expected output files
        self.input_file = Path(__file__).parent / "assets/test_mixed.c"
        self.expected_file = Path(__file__).parent / "assets/expected_mixed.c"

        if not self.input_file.is_file():
            self.fail(f"Input file not found: {self.input_file}")
        if not self.expected_file.is_file():
            self.fail(f"Expected output file not found: {self.expected_file}")

    def test_remove_comments(self):
        # Read expected output
        with open(self.expected_file, 'r') as ef:
            expected_output = ef.read()

        # Capture the output of the main function
        captured_output = io.StringIO()
        with patch.object(sys, 'argv', ['comment_parser', str(self.input_file)]):
            with patch('sys.stdout', new=captured_output):
                main()

        actual_output = captured_output.getvalue()

        # Directly compare the actual and expected outputs
        self.assertEqual(
            actual_output,
            expected_output,
            "The processed output does not match the expected output."
        )

class TestNoComments(unittest.TestCase):

    def setUp(self):
        # Define paths to input and expected output files
        self.input_file = Path(__file__).parent / "assets/test_no_comments.c"
        self.expected_file = Path(__file__).parent / "assets/expected_no_comments.c"

        if not self.input_file.is_file():
            self.fail(f"Input file not found: {self.input_file}")
        if not self.expected_file.is_file():
            self.fail(f"Expected output file not found: {self.expected_file}")

    def test_remove_comments(self):
        # Read expected output
        with open(self.expected_file, 'r') as ef:
            expected_output = ef.read()

        # Capture the output of the main function
        captured_output = io.StringIO()
        with patch.object(sys, 'argv', ['comment_parser', str(self.input_file)]):
            with patch('sys.stdout', new=captured_output):
                main()

        actual_output = captured_output.getvalue()

        # Directly compare the actual and expected outputs
        self.assertEqual(
            actual_output,
            expected_output,
            "The processed output does not match the expected output."
        )

class TestOnlyComments(unittest.TestCase):

    def setUp(self):
        # Define paths to input and expected output files
        self.input_file = Path(__file__).parent / "assets/test_only_comments.c"
        self.expected_file = Path(__file__).parent / "assets/expected_only_comments.c"

        if not self.input_file.is_file():
            self.fail(f"Input file not found: {self.input_file}")
        if not self.expected_file.is_file():
            self.fail(f"Expected output file not found: {self.expected_file}")

    def test_remove_comments(self):
        # Read expected output
        with open(self.expected_file, 'r') as ef:
            expected_output = ef.read()

        # Capture the output of the main function
        captured_output = io.StringIO()
        with patch.object(sys, 'argv', ['comment_parser', str(self.input_file)]):
            with patch('sys.stdout', new=captured_output):
                main()

        actual_output = captured_output.getvalue()

        # Directly compare the actual and expected outputs
        self.assertEqual(
            actual_output,
            expected_output,
            "The processed output does not match the expected output."
        )

if __name__ == '__main__':
    unittest.main()
