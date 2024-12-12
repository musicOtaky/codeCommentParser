#include <stdio.h>
#include <stdlib.h> // Standard library for general purposes

/*
  This program demonstrates comment removal.
  The main function prints out a message.
  We'll remove all these comments!
*/

int add(int a, int b) {
    return a + b; // Simple addition
}

int main() {
    // Print a greeting
    printf("Starting the program...\n");

    /* Now we do something else:
       We'll add two numbers and print their sum.
       The add function is defined above.
    */
    int x = 5;
    int y = 10;
    int sum = add(x, y); /* sum should be 15 after this line */
    printf("The sum of %d and %d is %d\n", x, y, sum);

    // Here's a tricky line: 
    // It prints something else and then we have a comment right after.
    printf("This line had some comments.\n"); // This is just a trailing comment

    /*
    Another multi-line comment block
    that should be removed entirely.
    Maybe we have some trailing spaces:
    
    */

    // Final line before returning
    return 0; // and we don't want this comment either
}
