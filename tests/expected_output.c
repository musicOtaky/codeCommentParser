#include <stdio.h>
#include <stdlib.h> 


int add(int a, int b) {
    return a + b; 
}

int main() {
    printf("Starting the program...\n");

    int x = 5;
    int y = 10;
    int sum = add(x, y); 
    printf("The sum of %d and %d is %d\n", x, y, sum);

    printf("This line had some comments.\n"); 


    return 0; 
}
