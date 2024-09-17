// main.cpp
#include <iostream>

// Function declarations (so the main file knows about them)
void say_hello();
void say_goodbye();

int main() {
    say_hello();    // Call function from file1
    say_goodbye();  // Call function from file2
    return 0;
}
