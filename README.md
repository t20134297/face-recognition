  1.该程序的功能为借助腾讯云的接口，制作简单的gui操作，实现人脸识别功能。
  2.我所用的系统为ubuntu14.04,使用的编程语言为python,版本为python3
  3.首先需要注册腾讯云账号，然后安装腾讯云的 ‘Python-SDK-图像识别’ 集成文档，下载地址为 https://github.com/tencentyun/image-python-sdk-v2.0
  4.利用 upload_photos.py 一张一张的上传本地图片，作为人脸库
  5.编写 GetphotoPath.py 程序，以操作界面的形式选择要识别的人脸图片
  6.利用python3 自带的 tkinter 库显示图片（注意这块在运行的时候可能报错，显示没有PIL库，此时只要安装PIL库就可以了，安装命令为 sudo pip3 install Pillow）
  7.运行 recognition.sh 这个shell文件，就可以实现人脸识别的功能了。
