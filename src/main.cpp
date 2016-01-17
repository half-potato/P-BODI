#include <iostream>
#include <numeric>
#include <vector>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <math.h>
//#include "Perspective.cpp"

using namespace cv;
using namespace std;


int main ( int argc, char** args )
{
	if (argc != 5) 
	{
		cout << "Usage: PerspectiveWindow <Image> <X> <Y> <Z>, where x y z are camera perspective" << endl;
	}
	vector<int> a1 {1, 2, 3};
	vector<int> b1 {2, 3, 4};
	//cout << a1 << b1 << endl;
	int c = dot(a1, b1);
	cout << c << endl;
}
