

int fib(int n)
{
if (n <= 1) return n;
return fib(n-1) + fib(n-2);


int A=0;
int B=1;
int S;
for(int i=1;i<n;i++) {S=B+A;A=B;B=S;}
return S;

}

int main ()
{
int n = 9;
cout << fib(n);



return 0;
}