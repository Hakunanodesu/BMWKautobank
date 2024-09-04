import keyboard
import time
import datetime

try:
    import pyi_splash
    pyi_splash.close()
except ImportError:
    pass
print("----------Warning----------")
print("如需退出程序请在一轮结束取钱传送后约20s加载时间中关闭程序")
print("----------Warning----------\n")
load_time = input("请输入使用缩地符后加载所需的时间，点击回车确认：")
print("\n三秒后开始运行，请聚焦游戏窗口\n")
time.sleep(3)
count = 1
while True:
    print(f"{datetime.datetime.now()}    ----------开始第{count}轮取钱----------")
    print(f"{datetime.datetime.now()}    正在重置视角")
    keyboard.press_and_release("e")
    time.sleep(3.5)
    keyboard.press_and_release("esc")
    time.sleep(2)

    print(f"{datetime.datetime.now()}    正在移动至目的地")
    keyboard.press("shift")
    keyboard.press("s + d")
    time.sleep(0.5)
    keyboard.release("s")
    time.sleep(1.1)
    keyboard.release("d")
    keyboard.press("w")
    time.sleep(4)
    keyboard.press("a")
    time.sleep(1.5)
    keyboard.release("w + a")

    print(f"{datetime.datetime.now()}    开始变身自爆")
    flag = 0
    while flag < 20:
        keyboard.press_and_release("4")
        time.sleep(0.1)
        flag += 1
    print(f"{datetime.datetime.now()}    ----------结束第{count}轮取钱----------")
    keyboard.release("shift")
    time.sleep(5)
    print(f"{datetime.datetime.now()}    传送")
    keyboard.press_and_release("q")
    time.sleep(int(load_time))

