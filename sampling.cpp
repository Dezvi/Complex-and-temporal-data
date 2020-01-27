#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(void){
    // Your code here!
    int aciertos=0;
    int num_valores=20;
    int Q3_num_valores=num_valores*3/4;
    int num_intentos=10000000;
    int k = 2;
    vector<int> valores;
    for(int i = 0; i < num_valores; ++i){
        valores.push_back(i);
    }
    for(int i = 0; i < num_intentos; ++i){
        random_shuffle(valores.begin(), valores.end());
        for(int j = 0; j < k; ++j){
            if(valores[j]>=Q3_num_valores){
                ++aciertos;
                break;
            }
        }
                
    }
    cout << "Probabilidad de error :" << (num_intentos-1.0*aciertos)/num_intentos << endl;
}