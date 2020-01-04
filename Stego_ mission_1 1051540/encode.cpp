#include <iostream>
#include <fstream>

#include <opencv/cv.h>
#include <opencv2/opencv.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace std;
using namespace cv;

// 確認是否為最後一位

bool isBitSet(char ch, int pos) {
	ch = ch >> pos;
	if (ch & 1)
		return true;
	return false;
}

int main(int argc, char** argv) {

	
	// 讀取圖像
	Mat image = imread("1.jpg");
	if (image.empty()) {
		cout << "Image Error\n";
		
		exit(-1);
	}

	// 設定隱寫內容
	ifstream file("message.txt");
	if (!file.is_open()) {
		cout << "File Error\n";
		
		exit(-1);
	}

	
	char ch;
	file.get(ch);
	int bit_count = 0;
	bool last_null_char = false;
	bool encoded = false;
	
	
	for (int row = 0; row < image.rows; row++) {
		for (int col = 0; col < image.cols; col++) {
			for (int color = 0; color < 3; color++) {

				// 呼叫像素點rgb
				Vec3b pixel = image.at<Vec3b>(Point(row, col));

				//改變1或0儲存需要資訊
				if (isBitSet(ch, 7 - bit_count))
					pixel.val[color] |= 1;
				else
					pixel.val[color] &= ~1;

				// 存進圖像
				image.at<Vec3b>(Point(row, col)) = pixel;

				// 下一bit
				bit_count++;

				// 輸入完資訊跳出
				if (last_null_char && bit_count == 8) {
					encoded = true;
					goto OUT;
				}

				// 一個字元8bits
				if (bit_count == 8) {
					bit_count = 0;
					file.get(ch);

					// 檔案最後確認
					if (file.eof()) {
						last_null_char = true;
						ch = '\0';
					}
				}

			}
		}
	}
OUT:;

	if (!encoded) {
		cout << "Message too big. Try with larger image.\n";
		exit(-1);
	}

	// 製作圖檔
	imwrite("stego1.bmp", image);
	system("pause");
	return 0;
}