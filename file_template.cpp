#include <iostream>
#include <cstdint>

using namespace std;


void solve() {

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
