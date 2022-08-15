#include <iostream>
using namespace std;

int main() 
{
	int* arr;
	int sum = 0;
	int temp;
	int num, target;
	cin >> num >> target;

	arr = (int*)malloc(sizeof(int)*num);
	for (int i = 0; i < num; i++) cin >> arr[i];
	for(int i=0; i<num-2; i++)
		for(int j=i+1; j<num-1; j++)
			for (int k = j + 1; k < num; k++)
			{
				temp = arr[i] + arr[j] + arr[k];
				if (temp<=target && abs(sum - target) > abs(temp - target))
				{
					sum = temp;
				}
			}
	cout << sum;
	delete[](arr);
	return 0;
}