#include <iostream>
#include <cstdint>

using namespace std;


void printStep(uint64_t currentState)
{
    cout << currentState << ' ';
}

void solve() {
    uint64_t n{};
    cin >> n;

    // simulation
    printStep(n);
    while (n > 1)
    {
        if (n & 1)
            n = n * 3 + 1;
        else
            n >>= 1;
        printStep(n);
    }
}

void printTestEnd() {
    cout << '\n';
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    uint32_t testsNumber{1};
//    Uncomment, if several test cases are needed.
//    cin >> testsNumber;
    for (uint32_t i = 0; i < testsNumber; ++i) {
        solve();
        printTestEnd();
    }

    return 0;
}
