import unittest
import sys
import io
import os
from unittest.mock import patch
from pathlib import Path

from comment_parser import remove_comments

class TestSingleLineCommentRemoval(unittest.TestCase):
    def test_single_line_comments(self):
        input_content = """#include <stdio.h>

// This is a single-line comment
int main() {
    printf("Hello World!\\n"); // print a greeting
    return 0; // end main
}
"""

        expected_output = """#include <stdio.h>


int main() {
    printf("Hello World!\\n"); 
    return 0; 
}
"""

        # Call the remove_comments function directly
        actual_output = remove_comments(input_content)

        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output, "The processed output does not match the expected output.")

class TestBlockCommentRemoval(unittest.TestCase):
    def test_single_line_comments(self):
        input_content = """#include <stdio.h>

/* This comment spans
   multiple lines and should
   be removed completely */

int main() {
    /* inline block comment */ printf("Hello\n");
    return 0;
}
"""

        expected_output = """#include <stdio.h>


int main() {
     printf("Hello\n");
    return 0;
}
"""

        # Call the remove_comments function directly
        actual_output = remove_comments(input_content)

        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output, "The processed output does not match the expected output.")

class TestMixedCommentRemoval(unittest.TestCase):
    def test_single_line_comments(self):
        input_content = """#include <stdio.h>
#include <stdlib.h> // std lib

/*
  Multi-line comment at top
  describing the program
*/

int main() {
    // single line before code
    printf("Starting...\n"); /* inline block comment */ printf("Done\n");
    
    /*
    Another multiline
    block
    */
    return 0; // trailing single-line
}
"""

        expected_output = """#include <stdio.h>
#include <stdlib.h> 


int main() {
    printf("Starting...\n");  printf("Done\n");
    
    return 0; 
}
"""

        # Call the remove_comments function directly
        actual_output = remove_comments(input_content)

        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output, "The processed output does not match the expected output.")

class TestNoCommentRemoval(unittest.TestCase):
    def test_single_line_comments(self):
        input_content = """#include <stdio.h>

int main() {
    printf("No comments here!\n");
    return 0;
}
"""

        expected_output = """#include <stdio.h>

int main() {
    printf("No comments here!\n");
    return 0;
}
"""

        # Call the remove_comments function directly
        actual_output = remove_comments(input_content)

        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output, "The processed output does not match the expected output.")


class TestAllCommentRemoval(unittest.TestCase):
    def test_single_line_comments(self):
        input_content = """// This file has no code, only comments

/* A multi-line
   comment only
*/

//
// Another single-line comment after an empty line

/* Ending block comment */

"""

        expected_output = """






"""

        # Call the remove_comments function directly
        actual_output = remove_comments(input_content)

        # Assert that the actual output matches the expected output
        self.assertEqual(actual_output, expected_output, "The processed output does not match the expected output.")


if __name__ == '__main__':
    unittest.main()
