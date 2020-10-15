#include<bits/stdc++.h>
using namespace std;

struct Pair{
	int min;
	int max;
};

struct Pair getMinMax(int a[], int n) {
	struct Pair minmax;
	int i;
	
	if(n==1) {
		minmax.min = a[0];
		minmax.max = a[0];
	}
	
	if(a[0] > a[1]) {
		minmax.min = a[1];
		minmax.max = a[0];
	}
	else {
		minmax.min = a[0];
		minmax.max = a[1];
	}
	
	for(int i = 2; i < n; i++) {
		if(a[i] > minmax.max) 
		minmax.max = a[i];
		
		else if(a[i] < minmax.min)
		minmax.min = a[i];
	}
	return minmax;
}
int main() {
	int n;
	cin>>n;
	int a[n];
	for(int i = 0; i < n; i++)
	cin>>a[i];
	
	struct Pair minmax = getMinMax(a, n);
	
	cout<<"Minimum element is "<<minmax.min<<endl;
	
	cout<<"Maximum element is "<<minmax.max<<endl;
	
	return 0;
}
