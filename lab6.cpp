
#include <iostream>
using namespace std;

double harmonic_series(int n) {
    if (n == 1) {
        return 1;
    } else {
        return 1.0 / n + harmonic_series(n - 1);
    }
}

int main() {
    int n;
    cout << "enter the value of n: ";
    cin >> n;
    cout << "harmonic series sum for n=" << n << " is " << harmonic_series(n) << endl;
    return 0;
}

#include <iostream>
using namespace std;

double harmonic_series(int n) {
    if (n == 1) {
        return 1;
    } else {
        return 1.0 / n + harmonic_series(n - 1);
    }
}

double harmonic_series() {
    int n;
    cout << "enter the value of n: ";
    cin >> n;

    return harmonic_series(n);
}

int main() {
    cout << "harmonic series sum is " << harmonic_series() << endl;
    return 0;
}
