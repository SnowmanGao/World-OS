from time import sleep
import keyboard
from 杂 import 框之内否


if __name__ == '__main__':
    print("这TM是模块，单独运行有鸟用？！")
    input()
    exit()

人坐标 = [0, 0]
画布尺寸 = ()
画布规范尺寸 = ()
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3


def 御_init(人坐标_, 画布尺寸_, 画布规范尺寸_):
    global 人坐标, 画布尺寸,画布规范尺寸 

    人坐标 = 人坐标_
    画布尺寸 = 画布尺寸_
    画布规范尺寸 = 画布规范尺寸_


def 设置人坐标(x,y):
    global 人坐标
    人坐标[0] = x
    人坐标[1] = y


def 键盘事件初始化():
    global 人坐标, 画布尺寸, 画布规范尺寸

    keyboard.add_hotkey('c',lambda:(
        # print('C     '),
        设置人坐标(画布尺寸[1]//2, 画布尺寸[0]//2)
    ))

    keyboard.add_hotkey('enter',print,args=('Enter!'))
    keyboard.add_hotkey('esc',lambda:(
        print('Quit!   '),
        sleep(0.5),
        exit()
    ))



def 键盘事件处理():
    
    if keyboard.is_pressed('w'):
        # print('Up    ')
        移动(UP)
    elif keyboard.is_pressed('s'):
        # print('Down  ')
        移动(DOWN)
    elif keyboard.is_pressed('a'):
        # print('Left  ')
        移动(LEFT)
    elif keyboard.is_pressed('d'):
        # print('Right ')
        移动(RIGHT)
    


def 移动(direc=0, step=1):
    # direc: 0上 1下 2左 3右
    人坐标[not direc//2] = {
        0: 人坐标[1] - step,
        1: 人坐标[1] + step,
        2: 人坐标[0] - step,
        3: 人坐标[0] + step
    }[direc]
    
    # print(人坐标,画布尺寸)

    if(not 框之内否(人坐标,(0,0),画布规范尺寸)):
        raise ValueError('-sb 坐标越界异常-')
