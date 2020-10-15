#include<bits/stdc++.h>
using namespace std;

void reverseArray(int a[], int start, int end) {
	if(start >= end)
	return;
	
	else {
		int temp = a[start];
		a[start] = a[end];
		a[end] = temp;
		
		reverseArray(a, start++, end--);
	}
}

void printArray(int a[], int size) {
	for(int i = 0; i < size; i++) {
		cout<<a[i]<<" ";
	}
	cout<<endl;
}

int main() {
	int n;
	cin>>n;
	int a[n];
	for(int i = 0; i<n; i++)
	cin>>a[i];
	
	reverseArray(a, 0, n-1);
	
	cout<<"Reversed array is "<<endl;
	printArray(a, 6);
	return 0;
}
