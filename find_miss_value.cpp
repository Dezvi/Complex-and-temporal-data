#include <iostream>
#include <iterator>
#include <fstream>

int main(){
    float number_of_lines = 0;
    system("wc -l my_missing_values_file.txt > lines.txt");
    std::ifstream myfile("lines.txt");
    myfile >> number_of_lines;
	myfile.close();
	
        
    long int sum_all_numbers = (number_of_lines+1) * (number_of_lines+2)/2;
    int number = 0;
    std::ifstream inFile("my_missing_values_file.txt");
    while (inFile >> number) {
		//Add the number to the end of the array
        sum_all_numbers -= number;
	}
	inFile.close();

	//Close the file stream
    std::cout << "The missing number is: " << sum_all_numbers << std::endl;
}