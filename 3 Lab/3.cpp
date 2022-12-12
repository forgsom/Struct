#include <iostream>

using namespace std;

int main() {
  int swt, len = 0, n;
  cout << "N = ";
  cin >> n;
  int *arr = new int[n];
  do {
    int i = n - 2;
    cout << "\n1. Add" << endl;
    cout << "2. Del" << endl;
    cout << "3. Top" << endl;
    cout << "0. End" << endl;
    cin >> swt;

    switch (swt) {
    case 1: {
      for (int f = 0; f < n - 1; f++) {
        arr[i + 1] = arr[i];
        i--;
      }
      cout << "Enter number: ";
      cin >> arr[0];
      break;
    }
    case 2: {
      for (int d = 1; d <= n - 1; d++) {
        arr[d - 1] = arr[d];
      }
      break;
    }

    case 3: {
      cout << arr[0] << endl;
      break;
    }
    }
  } while (swt != 0);
}