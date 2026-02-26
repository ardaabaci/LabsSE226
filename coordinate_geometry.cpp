//
// Created by ML103 on 2/26/2026.
//

#include "../coordinate_geometry.h"
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double x1, y1, x2, y2, distance;

    cout << "Enter x1 and y1: ";
    cin >> x1 >> y1;

    cout << "Enter x2 and y2: ";
    cin >> x2 >> y2;

    double dx = x2 - x1;
    double dy = y2 - y1;
    distance = sqrt(dx * dx + dy * dy);

    cout << "The distance between the points is: " << distance << endl;

    return 0;
}