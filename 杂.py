import ctypes
from tqdm import tqdm
import time
import os

if __name__ == '__main__':
    print("这TM是模块，单独运行有鸟用？！")
    input()
    exit()


def 初始化画布(canvas, size=(5, 5), bg=1):
    """
    @description  :生成纯块画布
    ---------
    @param  :(list)canvas 画布 (x,y)size 画布大小，(int)bg 画布背景方块id
    -------
    @return :(list) 处理完的画布
    --------
    """

    if(not isinstance(size, tuple) or size==(0,0)):
        print('初始化画布：参数错误，要求(N1,N2)，而你TM输入了' + str(size))
        return

    canvas = [bg] * size[0]
    for i in range(len(canvas)):
        canvas[i] = [bg] * size[1]

    return canvas


def 转录(block_id):
    """
    @description  :将方块id转换为具体渲染字符
    ---------
    @param  :(int)block_id 方块id
    -------
    @Returns  :(str) 渲染字符
    -------
    """

    return {
        0: '  ',
        1: '██',
        2: '□',
        3: '〼',
        4: '☑',
        5: '★',
    }[block_id]


class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    def __init__(self, x, y):
        self.X = x
        self.Y = y


STD_OUTPUT_HANDLE = -11
hOut = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def 设置光标(x=0, y=0):
    """
    @description  :设置命令行光标位置
    ---------
    @param  :(int)x 横坐标，(int)y纵坐标
    -------
    """

    ctypes.windll.kernel32.SetConsoleCursorPosition(hOut, COORD(x, y))


def 初始化加载(textList=['加载资源', '加载操蛋', '加载你妈', '就绪...']):
    pbar = tqdm(range(100))
    for i in pbar:
        pbar.set_description("Processing {0}".format(textList[i//30]))
        time.sleep(0.01)
    os.system('cls')

