#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main() {
    // TASK 1
    int pos, steps = 0;
    cout << "Enter positive integer greater than 1: ";
    cin >> pos;
    int current=pos;
    while (current>1){
        cout << current << " → ";
        if (current%2==0){
            current=current/2;
        } else{
            current=3*current+1;
        }
        steps++;
    }
    cout << 1 << endl;
    cout << "Total steps: " << steps << endl;
   // TASK 2
    int n;
    while (true) {
        cout << "\nPlease enter a number between 10 and 100: ";
        cin >> n;
        if (n >= 10 && n <= 100) {
            break;
        }
        cout << "Invalid input. ";
    }



    // TASK 3
    int n_star;
    cout << "Enter a number between 3 and 9: ";
    cin >> n_star;
    for (int i=1; i<=2*n_star-1; i++) {
        int k=n_star-abs(n_star - i);
        for (int j=0; j<k; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
