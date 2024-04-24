#include <iostream>
using namespace std;

int fibo(int valor){
    if (valor == 0) {
        return 0;
    }
    if (valor == 1) {
        return 1;
    } else {
        int atual = fibo(valor-1) + fibo(valor-2);
        return atual;
    }
}

int main() {
    
    int teste = 5;
    cout << fibo(teste);
    return 0;
}
