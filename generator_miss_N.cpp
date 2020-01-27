
#include <algorithm>    // std::random_shuffle
#include <vector>       // std::vector
#include <fstream>
#include <iostream>

int main(){
    int x = 0;
    int N = 0;
    std::cout << "Insert x: " << std::endl;
    std::cin >> x;
    std::cout << "Insert N: " << std::endl;
    std::cin >> N;
    std::vector<int> myvector;
    int i;
    for(i = 1; i < x; ++i)
        myvector.push_back(i);
    i += 1;
    while(i < N){
        myvector.push_back(i);
        ++i;
    }
    std::random_shuffle (myvector.begin(), myvector.end());
    std::ofstream outFile("my_missing_values_file.txt");
    for (const auto &e : myvector) outFile << e << "\n";
}