#include <iostream>
#include <fstream>

#include <opencv/cv.h>
#include <opencv2/opencv.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace std;
using namespace cv;



bool isBitSet(char ch, int pos) {
	
	ch = ch >> pos;
	if (ch & 1)
		return true;
	return false;
}

int main() {

	

	// Ū���Ϲ�
	Mat image = imread("stego1.bmp");
	if (image.empty()) {
		cout << "Image Error\n";
		exit(-1);
	}

	
	char ch = 0;
	int bit_count = 0;

	
	for (int row = 0; row < image.rows; row++) {
		for (int col = 0; col < image.cols; col++) {
			for (int color = 0; color < 3; color++) {

				// �I�s�����Irgb
				Vec3b pixel = image.at<Vec3b>(Point(row, col));

				// Ū��LSB�G�i��
				if (isBitSet(pixel.val[color], 0))
					ch |= 1;

				// �U�@��
				bit_count++;

				// 8bit���@����ASCII
				if (bit_count == 8) {

					
					if (ch == '\0')
						goto OUT;

					bit_count = 0;
					cout << ch;
					ch = 0;
				}
				else {
					ch = ch << 1;
				}

			}
			
		}
		
	}
	OUT:;
	cout << endl;

	system("pause");
	return 0;
}