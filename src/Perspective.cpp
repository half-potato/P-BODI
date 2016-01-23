#include <vector>
#include <numeric>
#include <math.h>
#include "LinearAlgebra.cpp"

using namespace std;

class PBOD
{
	float height;

	int pHeight;
	float pWidth;

	float fovX;
	float fovY;

	vector<float> camDirect;

	public:
		PBOD(float height, float pHeight, float pWidth, float fovX, float fovY, vector<float> camDirect) : height(height), pHeight(pHeight), pWidth(pWidth), fovX(fovX), fovY(fovY), camDirect(camDirect) {}
		float yAngleInView(int height);
		float getAngleFromCamera(int height);
		float getAngleFromGround();
		float getDistanceAtHeight(int height, float incline = 0.0);
		vector<float> getAngularSize(int x, int y, float objectH, float objectW, float objectZ, float incline = 0.0);
		vector<float> getWindow(int x, int y, float objectW, float objectH, float objectZ, float incline = 0.0);
		vector<vector<float> > getWindows(float objectW, float objectH, float objectZ, int imw, int imh, float stepSize, float incline = 0);
};

float PBOD::yAngleInView(int height)
{
	return (float(height) / this->pHeight) * this->fovY;
}

float PBOD::getAngleFromGround()
{
	vector<float> b;
	b.push_back(this->camDirect[0]);
	b.push_back(0.0);
	b.push_back(this->camDirect[2]);
	return M_PI_2 - vacos(b, this->camDirect);
}

float PBOD::getAngleFromCamera(int height)
{
	return this->getAngleFromGround() - (this->fovY / 2.0) + this->yAngleInView(height);
}

float PBOD::getDistanceAtHeight(int height, float incline)
{
	float A = this->getAngleFromCamera(height);
	float X = M_PI_2 - incline;
	float H = M_PI - (X + A);
	float x = this->height * sin(X) / sin(H);
	return x;
}

vector<float> PBOD::getAngularSize(int x, int y, float objectH, float objectW, float objectZ, float incline)
{
	float d = this->getDistanceAtHeight(y);
	float dist = 1.0;
	if (d == d) (dist = d);
	float farend = dist + objectZ;

	//float dist_to_bot_end = sqrt(pow(farend, 2) + pow(this->height, 2.0));
	float dist_to_top_end = sqrt(pow(this->height - objectH, 2.0) + pow(farend, 2.0));
	float dist_to_top_close = sqrt(pow(this->height - objectH, 2.0) + pow(dist, 2.0));
	float dist_to_bot_close = sqrt(pow(farend, 2) + pow(this->height, 2.0));
	
	float AF = acos((pow(dist_to_top_close, 2.0) + pow(dist_to_bot_close, 2.0) - pow(objectH, 2.0)) / (2.0 * dist_to_top_close * dist_to_bot_close));
	float AT = acos((pow(dist_to_top_close, 2.0) + pow(dist_to_top_end, 2.0) - pow(objectZ, 2.0)) / (2.0 * dist_to_top_close * dist_to_top_end));

	// Lazy method
	float w = (AF / objectH) * objectW;
	
	vector<float> retval;
	retval.push_back(AT);
	retval.push_back(AF);
	retval.push_back(w);

	return retval;
}

vector<float> PBOD::getWindow(int x, int y, float objectW, float objectH, float objectZ, float incline)
{
	vector<float> aSize = this->getAngularSize(x, y, objectW, objectH, objectZ, incline);
	float windW = aSize[2] * (float(this->pHeight) / this->fovY);
	float windH = (aSize[0] + aSize[1]) * (float(this->pHeight) / this->fovY);
	vector<float> retval;
	retval.push_back(x);
	retval.push_back(y);
	retval.push_back((int)windW);
	retval.push_back((int)windH);
	return retval;
}

vector<vector<float> > PBOD::getWindows(float objectW, float objectH, float objectZ, int imw, int imh, float stepSize, float incline)
{
	vector<vector<float> > retval;
	for (int x = 0; x < imw; x+=stepSize)
	{
		for (int y = 0; y < imh; y += stepSize)
		{
			retval.push_back(this->getWindow(x, y, objectW, objectH, objectZ, incline));
		}
	}
	return retval;
}
