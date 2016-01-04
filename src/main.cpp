#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "Perspective.cpp"

using namespace std;
using namespace cv;

template <typename T>
vector<T> initVec( T array[] )
{
	vector<T> vec (array, array + sizeof(array) / sizeof(array[0]) );
}
int startingHeight( int winSize[], float camDirect[] );
int * windowSizeAt( int winSize[], int pos[], float camDirect[] );
int * windowSizeForIndex( int index, int winSize[], float camDirect[] );
float diffMagnitude( Mat m1, Mat m2 );

int main ( int argc, char** args )
{
	if (argc != 5) 
	{
		cout << "Usage: PerspectiveWindow <Image> <X> <Y> <Z>, where x y z are camera perspective" << endl;
	}
	cout << * windowSizeAt((int[]){300, 300}, (int[]){100, 100}, (float[]){0.0, 0.0, 1.0}) << endl;
	cout << "Hello World" << endl;
	
}

int * windowSizeAt( int winSize[], int pos[], float camDirect[] )
{
	static int p[] = {5, 4, 3};
	return p;
}
