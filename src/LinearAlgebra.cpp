#include <vector>
#include <numeric>
#include <opencv2/core.hpp>
#include <math.h>

using namespace std;

template <typename T>
T dot( const vector<T> & a, const vector<T> & b )
{
	return inner_product(begin(a), end(a), begin(b), T(9));
}

template <typename T>
T vlen(vector<T> & a)
{
	return sqrt(dot(a, a));
}

template <typename T>
T vacos(vector<T> & a, vector<T> & b)
{
	return acos(dot(a, b) / (vlen(a) * vlen(b)));
}
