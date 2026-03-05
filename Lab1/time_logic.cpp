#include "../time_logic.h"
#include <iostream>
using namespace std;

int main() {
    int totalSeconds;
    int hours, minutes, seconds;

    cout << "Enter a total number of seconds: ";
    cin >> totalSeconds;

    hours = totalSeconds / 3600;
    minutes = (totalSeconds % 3600) / 60;
    seconds = totalSeconds % 60;

    cout << totalSeconds << " seconds is " << hours << " hours, "
         << minutes << " minutes, and " << seconds << " seconds." << endl;

    return 0;
}