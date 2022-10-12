#include<iostream>
using namespace std;
int main()
{
int array[50], position,i,n, value, ch;

cout<<"\nEnter the no.of elements in array:";
cin>>n;
cout<<"Enter \t" << n << "  Elements:";

for(i=0;i<n;i++)
cin>>array[i];

cout<<"\nPress 1 to insert at end or 0 to insert at specified position:";
cin>>ch;


if(ch==1){

position=n+1;
cout<<"Please enter the value:";
cin>>value;
}
else{
cout<<"Please enter the location of the value where you want to insert new element:";
cin>>position;
cout<<"Please enter the value:";
cin>>value;
}

for(i=n-1;i>=position-1;i--)
array[i+1]= array[i];
array[position-1]= value;
cout<<"\n Resultant array is:";

for(i=0;i<=n; i++)
cout<<array[i]<<"  ";

return 0;

}

