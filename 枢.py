from os import system
from 杂 import *
from 御 import *
from 图 import *
from 示 import *

主视野地形 = [[]]
# (y,x) (纵,横)  遍历先[0]后[1]
画布尺寸 = (25, 40)
人坐标 = [画布尺寸[1],画布尺寸[0]//2]

def 渲染():
    # 覆盖式清屏
    设置光标(0, 0)

    terra = ''
    for i in range(画布尺寸[0]):
        for j in range(画布尺寸[1]):
            terra += 转录(主视野地形[i][j])
        terra += '\n'
    print(terra)

    设置光标(人坐标[0], 人坐标[1])
    print('你')
    # 设置光标(1, 画布尺寸[1])


    

# 主程序 & 循环

try:
    # 初始化加载()
    主视野地形 = 初始化画布(主视野地形, 画布尺寸, 1)
    御_init(人坐标, 画布尺寸)
except Exception as e:
    抛出错误(e, '初始化 过程崩溃')

try:
    显示标题界面()
    keyboard.wait(' ')
except Exception as e:
    抛出错误(e, '标题界面 崩溃')

os.system('cls')

while(1):
    try:
        渲染()
    except Exception as e:
        抛出错误(e, '渲染 过程崩溃')
    
    try:
        处理键盘事件()
    except Exception as e:
        抛出错误(e, '处理键盘事件 过程崩溃')
    
    time.sleep(0.05)