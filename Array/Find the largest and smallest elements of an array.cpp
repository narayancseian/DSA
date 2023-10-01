#include <iostream>

int main() {
    int arr[] = {4, 2, 9, 5, 1, 7, 8};
    int n = sizeof(arr) / sizeof(arr[0]);

    if (n == 0) {
        std::cout << "The array is empty." << std::endl;
        return 1;
    }

    int minElement = arr[0];
    int maxElement = arr[0];

    for (int i = 1; i < n; ++i) {
        if (arr[i] < minElement) {
            minElement = arr[i];
        }
        if (arr[i] > maxElement) {
            maxElement = arr[i];
        }
    }

    std::cout << "Smallest element: " << minElement << std::endl;
    std::cout << "Largest element: " << maxElement << std::endl;

    return 0;
}
								
