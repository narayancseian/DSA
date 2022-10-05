/*  C++ Program to implement Selection Sort using Array  */

#include<iostream>

using namespace std;

int main()
{
    int i,j,n,loc,temp,min,a[30];

    cout<<"Enter size of Array :: ";
    cin>>n;
    cout<<"\nEnter elements to the array :: \n";

    for(i=0;i<n;++i)
    {
        cout<<"\nEnter "<<i+1<<" element :: ";
        cin>>a[i];
    }

    for(i=0;i<n-1;i++)
    {
        min=a[i];
        loc=i;
        for(j=i+1;j<n;j++)
        {
            if(min>a[j])
            {
                min=a[j];
                loc=j;
            }
        }

        temp=a[i];
        a[i]=a[loc];
        a[loc]=temp;
    }

    cout<<"\nAfter Selection Sort, Sorted list is :: \n\n";
    for(i=0;i<n;i++)
    {
        cout<<a[i]<<"  ";
    }
    cout<<"\n";

    return 0;
}
