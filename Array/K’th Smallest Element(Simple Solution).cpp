/*Method 1 (Simple Solution):
A simple solution is to sort the given array using a O(N log N)
sorting algorithm like Merge Sort, Heap Sort, etc and return the
element at index k-1 in the sorted array.

Time Complexity of this solution is O(N Log N)

*/

#include<bits/stdc++.h>
using namespace std;

int kthSmallest(int a[], int n, int k) {
	sort(a, a+n);
	return a[k-1];
}

int main() {
	int t, n;
	cin>>t;
	while(t--) {
		cin>>n;
	    int a[n], k;
	    for(int i = 0; i < n; i++)
	    cin>>a[i];
	    
	    cin>>k;
	    cout<<"K'th smallest element is "<<kthSmallest(a, n, k)<<endl;
	}
	return 0;
}
