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

	

	// 讀取圖像
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

				// 呼叫像素點rgb
				Vec3b pixel = image.at<Vec3b>(Point(row, col));

				// 讀取LSB二進位
				if (isBitSet(pixel.val[color], 0))
					ch |= 1;

				// 下一位
				bit_count++;

				// 8bit為一組轉ASCII
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