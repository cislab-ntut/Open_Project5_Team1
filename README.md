# 1051540 游登翔 #
===============================================================================
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

Visual studio 2017, opencv-3.4.0, windows, c++

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

# 1051555 余洪楓 #
===============================================================================
## Stego mission 3 Stego Image生成器 ##


### 所需工具和編譯環境: ###
Python3.7

### Demo ###
以Stego Mission 3原題所給灰色Image作為加密載體圖(載體圖片必須為肉眼所見的純色）</br>
輸入欲添加密文在圖中之坐標位置及密文內容：</br>
![image](https://github.com/cislab-yzu/Project1-5_Open/blob/master/StegoMission3_Creator_1051555/p1.png)
可以看到有Output Stego image生成：</br>
![image](https://github.com/cislab-yzu/Project1-5_Open/blob/master/StegoMission3_Creator_1051555/p2.png)
將生成的Stego image放入Project 3中寫的解密程式進行解密：</br>
![image](https://github.com/cislab-yzu/Project1-5_Open/blob/master/StegoMission3_Creator_1051555/p3.png)
可以看到除了有Stego Mission 3本身的密文外，新增了我們剛剛自行添加的密文



