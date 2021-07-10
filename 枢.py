from 杂 import *
from 示 import *
from 御 import *
from 图 import *


# (y,x) (纵,横)  遍历先[0]后[1]
画布尺寸 = (25, 40)
# (x,y) (横,纵)  为了方便而翻转倒x,y倒正常顺序
画布规范尺寸 = (画布尺寸[1], 画布尺寸[0])
# (x,y)
人坐标 = [画布尺寸[1]//2, 画布尺寸[0]//2]

渲染状态 = True


def 渲染():
    # 覆盖式清屏
    设置光标(0, 0)

    if(not 主视野地形):
        抛出错误('渲染：无路赛~', '主视野地形为空')

    terra = ''
    for i in range(画布尺寸[0]):
        for j in range(画布尺寸[1]):
            terra += 转录(主视野地形[i][j])
        terra += '\n'
    print(terra)

    设置光标(人坐标[0] * 2, 人坐标[1])
    print('你')
    

def 抛出错误(e='未知', text='无'):
    global 渲染状态

    渲染状态 = False
    显示错误界面(e, text)




# 初始化加载
try:
    process = 0  # 0
    # 初始化加载()
    process += 1  # 1
    键盘事件初始化()
    process += 1  # 2
    御_init(人坐标, 画布尺寸, 画布规范尺寸)
    process += 1  # 3
    主视野地形 = 加载区块()

    process += 1  # 4
except Exception as e:
    抛出错误(e, '初始化 过程崩溃 at %d' % process)


try:
    显示标题界面()
    pass
    keyboard.wait(' ')
except Exception as e:
    抛出错误(e, '标题界面 崩溃')



os.system('cls')



# 主程序 & 循环


def thread_jp():
    while(1):
        try:
            键盘事件处理()
        except Exception as e:
            抛出错误(e, '键盘事件处理 过程崩溃')
        sleep(0.05)

# 渲染线程 = 线程(1, '渲染线程', thread_xr)
键盘线程 = 线程(2, '键盘线程', thread_jp)
# 渲染线程.start()
键盘线程.start()

while(1):
    if(渲染状态 == False):
        break
    try:
        渲染()
    except Exception as e:
        抛出错误(e, '渲染 过程崩溃')
    sleep(0.01)



print('Q.E.D')
input()