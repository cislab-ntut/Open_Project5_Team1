# 1051540 游登翔 #
==========================================================================================================================================
## Stego mission 1 LSB製作 ##


### 所需工具和編譯環境: ###

HxD, windows

### 方法1: ###

1.打開HxD並編輯欲改變內容之底圖

2.依據LSB將最後一位改成所需資訊BITS轉換成16進位並存檔

3.輸出之圖與原本無異且已存入密文內容

### 成果顯示: ###

![原始底圖](https://github.com/cislab-yzu/Project1-5_Open/blob/master/Stego_%20mission_1%201051540/1.bmp "底圖")
                                    
                                                    原始底圖
                                                    
![原始底圖](https://github.com/cislab-yzu/Project1-5_Open/blob/master/Stego_%20mission_1%201051540/TEST1-1.png "底圖內容")

                                                    原始內容

![原始底圖](https://github.com/cislab-yzu/Project1-5_Open/blob/master/Stego_%20mission_1%201051540/TEST1-2.png "修改")

                                                 修改為所需密文內容

![原始底圖](https://github.com/cislab-yzu/Project1-5_Open/blob/master/Stego_%20mission_1%201051540/TEST.bmp "結果")

                                                     輸出結果




### 鑒於以上方法較簡單於是又想了另一方法實現LSB隱寫 ###


### 所需工具和編譯環境: ###

Visual stdio 2017, opencv-3.4.0, windows, c++

### 方法2: ###

1.選擇取名1.jpg的圖像為底圖

2.把欲加密字串寫入message.txt中

3.利用opencv中的Vec3b找出想改變的pixel中RGB的位置並且於每一位置最後一位做LSB隱藏資訊

4.輸出成果為stego1.bmp的圖像檔

### 成果顯示: ###

![原始底圖](https://github.com/cislab-yzu/Project1-5_Open/blob/master/Stego_%20mission_1%201051540/1.jpg "底圖")
                                    
                                                    原始底圖
                                                    
![原始底圖](https://github.com/cislab-yzu/Project1-5_Open/blob/master/Stego_%20mission_1%201051540/TEST2-1.png "加密密文")

                                                    欲加密密文

![原始底圖](https://github.com/cislab-yzu/Project1-5_Open/blob/master/Stego_%20mission_1%201051540/stego1.bmp "結果")

                                                     輸出結果

![原始底圖](https://github.com/cislab-yzu/Project1-5_Open/blob/master/Stego_%20mission_1%201051540/TEST2-2.png "解密")

                                                      解密結果
