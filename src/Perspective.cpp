#include <vector>

class PBOD
{
	float height;

	float pHeight;
	float pWidth;

	float fovX;
	float fovY;

	vector<float> camDirect;

	PBOD init(height, pHeight, pWidth, fovX, fovY, camDirect = [1.0, 0.0, 0.0])
	{
		self.height = height;
		self.pHeight = pHeight;
		self.pWidth = pWidth;
		self.fovX = fovX;
		self.fovY = fovY;
		self.camDirect = camDirect;
	}
}
