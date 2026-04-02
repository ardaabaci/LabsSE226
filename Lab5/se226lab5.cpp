#include <iostream>
using namespace std;
double alternating_sum(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1.0;
    
    if (n%2==1) {
        return alternating_sum(n - 1) + (1.0 / n);
    } else {
        return alternating_sum(n - 1) - (1.0 / n);
    }}
int main(){
    int n;
    cin >> n;
    cout << alternating_sum(n) << endl;
    return 0;
}

