// Here is a simple recursive implementation of the Fibonacci algorithm in C++.
#include <iostream>
using namespace std;

int fibo(int v){
    if (v == 0) {
        return 0;
    }
    if (v == 1) {
        return 1;
    } else {
        int n = fibo(v-1) + fibo(v-2);
        return n;
    }
}

int main() {
    
    int test = 5;
    cout << fibo(test);
    return 0;
}
