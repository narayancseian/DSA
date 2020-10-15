/* Tournament Method :
   Divide the array into two parts and compare the maximums and minimums
   of the two parts to get the maximum and the minimum of the whole array.
*/

#include<bits/stdc++.h>
using namespace std;

struct Pair{
	int min;
	int max;
};

struct Pair getMinMax(int a[], int low, int high) {
	struct Pair minmax, mml, mmr;
	int mid;
	
	// If there is only one element
	if(low == high) {
		minmax.min = a[low];
		minmax.max = a[low];
		return minmax;
	}
	
	// If there are two elements
	if(high == low+1) {
		if(a[low] > a[high]) {
			minmax.min = a[high];
			minmax.max = a[low];
		}
		
		else {
			minmax.min = a[low];
			minmax.max = a[high];
		}
		return minmax;
	}
	
	// If there are more than 2 elements
	mid = (low + high) / 2;
	mml = getMinMax(a, low, mid);
	mmr = getMinMax(a, mid+1, high);
	
	// Compare minimums of two parts
	if(mml.min < mmr.min)
	minmax.min = mml.min;
	else
	minmax.min = mmr.min;
	
	// Compare maximum of two parts
	if(mml.max > mmr.max)
	minmax.max = mml.max;
	else
	minmax.max = mmr.max;
	
	return minmax;
}

int main() {
	int n;
	cin>>n;
	int a[n];
	for(int i = 0; i < n; i++)
	cin>>a[i];
	
	struct Pair minmax = getMinMax(a, 0, n-1);
	
	cout<<"Minimum element is "<<minmax.min<<endl;
	
	cout<<"Maximum element is "<<minmax.max<<endl;
	
	return 0;
}
