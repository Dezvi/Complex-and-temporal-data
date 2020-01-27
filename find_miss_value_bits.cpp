#define NUMBERS_SIZE 10
#include <iostream>
#include <iterator>
#include <fstream>
#include <bitset>
#include <cmath> 

int main(){
    std::ifstream inFile("my_missing_values_file.txt");
    std::bitset<NUMBERS_SIZE> bset;
    bset.set();
    int number = 0;
    while (inFile >> number) {
		//Add the number to the end of the array
        bset.set(number, 0);
	}

	//Close the file stream
	inFile.close();
    std::cout << "The missing number is: " << std::log2(bset.to_ulong()) << std::endl;
}