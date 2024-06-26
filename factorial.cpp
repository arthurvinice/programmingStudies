// Have the function FirstFactorial(num) take the num parameter being passed
// and return the factorial of it. 
// For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
// For the test cases, the range will be between 1 and 18 and the input will always be an integer.
// A challenge available on CoderByte.com


#include <iostream>
#include <string>
using namespace std;

int FirstFactorial(int num) {
    for (int i=num-1; i>0 ; i--) {
        num = num * i;
    }
    return num;
}

int main(void) {
    int entry;
    cin >> entry;
    cout << FirstFactorial(entry);
}
