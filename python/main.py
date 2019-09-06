import os
import time
#os.system('adb shell screencap -p /sdcard/01.png')
#os.system('adb pull /sdcard/01.png tmp/01.png')
#os.system('adb shell input tap 53 1885')
#os.system('adb shell input swipe 100 300 500 300')
#rateW = 1080(手机屏幕的宽) / 1602(event里0035的max) = 0.674
#rateH = 1920(手机屏幕的高) / 2503(event里0036的max) = 0.767
#screenW = width*rateW = 833*0.674 = 561
#screenH = height*rateH = 2284*0.767 = 1751‘
while 1:
	os.system('adb shell input tap 100 100')
	os.system('adb shell input tap 380 627')#312
	os.system('adb shell input tap 460 576')#265
	os.system('adb shell input tap 600 519')
	os.system('adb shell input tap 710 603')
	os.system('adb shell input tap 990 777')
	os.system('adb shell input tap 1264 537')
	os.system('adb shell input tap 1428 643')
	os.system('adb shell input tap 1541 675')
	os.system('adb shell input tap 1707 656')
	os.system('adb shell input tap 1512 1050')
	os.system('adb shell input tap 1733 977')
	os.system('adb shell input tap 460 895')
	os.system('adb shell input tap 1511 948')
	os.system('adb shell input tap 1521 1057')
	os.system('adb shell input tap 1647 1014')
	os.system('adb shell input tap 1339 1024')
	os.system('adb shell input tap 100 100')
	time.sleep(5)