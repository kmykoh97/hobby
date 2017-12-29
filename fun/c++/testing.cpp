
#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;
void prime_number()
{
	ofstream outfile("file1.dat");
	if (!outfile)
	{
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
	ifstream infile("file1.dat", ios::in);
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
	int main()
	{
		cout << "10000 之内的素数为：";
		void prime_number();
		cout << endl;
		cout << "个位数为 1,3,5,7,9 的素数之和为:";
		void calculate();
		cout << endl;
		system("pause");
		return 0;
	}
