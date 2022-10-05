/*  C++ Program to implement Insertion Sort using Array  */

#include<iostream>

using namespace std;

int main()
{
    int i,j,n,temp,a[30];

    cout<<"Enter size of Array :: ";
    cin>>n;
    cout<<"\nEnter elements to the array :: \n";

    for(i=0;i<n;++i)
    {
        cout<<"\nEnter "<<i+1<<" element :: ";
        cin>>a[i];
    }

    for(i=1;i<=n-1;i++)
    {
        temp=a[i];
        j=i-1;

        while((temp<a[j])&&(j>=0))
        {
            a[j+1]=a[j];
            j=j-1;
        }

        a[j+1]=temp;
    }

    cout<<"\nAfter Insertion Sort, Sorted list is :: \n\n";
    for(i=0;i<n;i++)
    {
        cout<<a[i]<<"  ";
    }
    cout<<"\n";

    return 0;
}
