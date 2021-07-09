import os


if __name__ == '__main__':
    print("这TM是模块，单独运行有鸟用？！")
    input()
    exit()

def 本土化异常(err):
    if('index' in err):
        #注意不要颠倒 x y
        return '定义域警告_杨超越，是不是x,y写反了？'
    if('defined' in err):
        return '没定义或变量名写错了？'
    if('argument' in err):
        return '变量给少了？给多了？'
    if('type' in err):
        return '类型错误，牛头不对马嘴！'
    return '无语'


def 显示标题界面():
    os.system('cls')
    print('██████████████████████████████')
    print('           瓦鲁多 OS          ')
    print('         -- ver 0.1 --        ')
    print('')
    print('          SnowmanGao         ')
    print('       莅临寒序，不胜感激      ')
    print('██████████████████████████████')
    print('\n 按空格键继续...')


def 抛出错误(e='未知', text='无'):
    os.system('cls')
    print('〼〼〼〼〼〼〼〼〼〼〼〼〼〼〼〼〼〼')
    print('           程序：停博           ')
    print('')
    print('               :<               ')
    print('           -瓦鲁多 OS-         ')
    print('')
    print('错误梗概：', text)
    print('发生异常：', e)
    print('可能：    ', 本土化异常(str(e)))
    print('〼〼〼〼〼〼〼〼〼〼〼〼〼〼〼〼〼〼')
    print('\n 按回车键关闭程序并默哀...')
    input()
    exit()