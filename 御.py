import keyboard
import time

if __name__ == '__main__':
    print("这TM是模块，单独运行有鸟用？！")
    input()
    exit()

人坐标 = [0, 0]
画布尺寸 = [[]]
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3


def 御_init(人坐标_, 画布尺寸_):
    global 人坐标, 画布尺寸

    人坐标 = 人坐标_
    画布尺寸 = 画布尺寸_


def 处理键盘事件():
    global 人坐标, 画布尺寸

    if keyboard.is_pressed('w'):
        print('Up    ')
        移动(UP)
    elif keyboard.is_pressed('s'):
        print('Down  ')
        移动(DOWN)
    elif keyboard.is_pressed('a'):
        print('Left  ')
        移动(LEFT)
    elif keyboard.is_pressed('d'):
        print('Right ')
        移动(RIGHT)
    elif keyboard.is_pressed('c'):
        print('C     ')
        人坐标 = [画布尺寸[1], 画布尺寸[0]//2]
    elif keyboard.is_pressed('enter'):
        print('Enter!')
    elif keyboard.is_pressed('esc'):
        print('Quit!   ')
        time.sleep(0.5)
        exit()


def 移动(direc=0, step=1):
    # direc: 0上 1下 2左 3右
    人坐标[not direc//2] = {
        0: 人坐标[1] - step,
        1: 人坐标[1] + step,
        2: 人坐标[0] - 2 * step,
        3: 人坐标[0] + 2 * step
    }[direc]
    
    if(人坐标[0]>=画布尺寸[1] or 人坐标[1]>=画布尺寸[0]):
        raise ValueError('越界')
