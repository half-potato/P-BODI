#include <vector>
#include "LinearAlgebra.cpp"

using namespace std;

class Object {
	public:
		int id;
		// Along a semi-circle where the bottom is 0 and the top is pi
		float typicalHeight;
};

class RoomObjects {
	vector<Object> typical;
	public:
		float matchProbability(vector<Object> currentObjects);
};
