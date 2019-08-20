int main()
{
int n;

cin>>n;

int height[n];
for(int i=0;i<n;i++)
cin>>height[i];
int *large=max_element (height,height+n);
int blown = count(height,height+n,*large);
cout<<blown;
return 0;
}