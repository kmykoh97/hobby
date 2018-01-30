/*
#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;
int main()
{
	void primenumber();
	void calculate();
	cout << "10000 之内的素数为：";
	void primenumber();
	cout << endl;
	cout << "个位数为 1,3,5,7,9 的素数之和为:";
	void calculate();
	cout << endl;
	return 0;
}
void primenumber() {
	ofstream outfile("file1.txt");
	if (!outfile) {
		cerr << "cannot open file!" << endl;
		exit(1);
	}
	int a, b;
	bool abc = false;
	for (a = 1; a <= 10000; a++)
	{
		b = 2;
		if (b < a)
		{
			for (b = 2; b < a; b++)
			{
				if (a%b != 0)
				{
					abc = true;
				}
				else
				{
					abc = false;
					break;
				}
			}
		}
		if (a == 1 || a==2)
		{
			outfile.put(a);
			cout << a << ' ';
		}
		if (abc == true)
		{
			outfile.put(a);
			cout << a << ' ';
		}
	}
	cout << endl;
	outfile.close();
}


void calculate()
{
	int a, b = 0;
	ifstream infile("file1.txt", ios::in);
	if (!infile)
	{
		cerr << "cannot open file!" << endl;
		exit(1);
	}
	while (!infile.eof())
	{
		infile >> a;
		if (a % 10 == 1)
		{
			b = b + a;
		}
	    if (a % 10 == 3)
		{
			b = b + a;
		}
		if (a % 10 == 5)
		{
			b = b + a;
		}
		if (a % 10 == 7)
		{
			b = b + a;
		}
		if (a % 10 == 9)
		{
			b = b + a;
		}
	}
	cout << b;
	infile.close();
}
*/

#include <iostream>
using namespace std;

void printSomething(int x) {
  switch(x) {
    case 0:
      cout << "Too little" << endl;
      break;
    case 5:
      cout << "Too much" << "Second text \n";
      break;
    default:
      cout << "Hello" << "nothing";
  }
}

int main() {
  // simple printing
  int myNumber;
  cout << "Please enter a value:";
  cin >> myNumber;
  cout << "your number is " << myNumber << endl;
  // for, while loop
  for(int newVar = 0; newVar < 2; newVar++) {
    int a = 1;
    while(a<3) {
      cout << newVar << myNumber << "\n";
      a++;
			printSomething(myNumber);
    }
  }
  // arrays,loops
  int myList[2][2] = {{1,1}, {2,3}};
  cout << myList[0][1] << endl;
  int arr[] = {1,2,3,4,5,6,7,8,9,0};
  int sum = 0;
  for(int x=0; x<10; x++) {
    if(arr[x] >= 1) {
      sum += arr[x];
    }
  }
	cout << sum;
}
