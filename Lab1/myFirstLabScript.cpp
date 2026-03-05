#include <iostream>
#include <string>

using namespace std;
int main() {
    string name;
    string studentID;
    cout << "What is your name?" << std::endl;
    getline(std::cin, name);
    cout << "Hello " << name << "." << std::endl;
    cout << "What is your Student ID?" << std::endl;
    cin >> studentID;

    cout << "Your ID is " << studentID << "." << std::endl;

    return 0;
}