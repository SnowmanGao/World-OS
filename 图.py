from 杂 import 初始化画布


if __name__ == '__main__':
    print("这TM是模块，单独运行有鸟用？！")
    input()
    exit()



class 区块:
    # 采用稀疏矩阵压缩法
    def __init__(self, size, bg, data, setting = {}) -> None:
        '''
        * size = (int, int)  横纵坐标
        * bg = (int)  方块id
        * data = {(int, int) : int, ...}
        * [setting] = {...}
        '''
        self.size = size
        self.bg = bg
        self.data = data
        self.setting = setting

    def 合成(self) -> list:
        canvas = []
        canvas = 初始化画布(canvas, self.size, self.bg)
        for i in self.data:
            canvas[i[0]][i[1]] = self.data[i]
        return canvas

    def 信息(self) -> str:
        info = ''
        info += '面积    ：%s\n' % str(self.size)
        info += '背景    ：%d\n' % self.bg
        info += '实际大小：%s\n' % len(self.data)
        if(self.setting):
            # setting对象非空
            info += '-设置-  ：%s\n' % str(self.setting)
        info += '细节    ：%s\n' % str(self.data)
        return info


class 世界:
    # 区块矩阵
    def __init__(self, data={}, setting={}) -> None:
        '''
        * data = {(int, int) : (区块), ...}
        * !!! data 以 (x,y) 作索引 !!!
        * setting = {None}
        '''
        self.data = data
        self.setting = setting

    def 取区块源数据(self, pos) -> list:
        # pos = (int,int) 横纵坐标

        return self.data[pos]

    def 取区块(self, pos) -> list:
        # pos = (int,int) 横纵坐标
        # 已经帮你合成了亲

        return self.取区块源数据(pos).合成()

    def 设区块源数据(self, *args) -> None:
        ''' 
        * 1个参数：{(int, int) : (区块), ...} 类似世界型
        * 2,4,6,...个参数：(int, int), (区块), ...
        '''
        
        try:
            if(len(args) == 1):
                arg = args[0]
                for pos, chunk in arg.items():
                    self.data[pos] = chunk
            else:
                for pos, chunk in zip(args[::2],args[1::2]):
                    self.data[pos] = chunk
        except Exception as e:
            # 抛出错误(e, '区块数据格式 发生错误')
            print('error')

    def 信息(self) -> str:
        info = ''
        info += '区块数  ：%d\n' % len(self.data)
        if(self.setting):
            # setting对象非空
            info += '-设置-  ：%s\n' % str(self.setting)
        info += '细节    ：%s\n' % str(self.data)
        return info


当前世界 = 世界()
主视野地形 = [[]]


def 生成世界():
    global 当前世界

    chk = 区块((25, 40), 1, {(1, 2): 4, (2, 3): 3, (0, 0): 1, (4, 4): 2}, {5464: 54})
    # b = 区块((5, 5), 1, {(1, 3): 2, (4, 3): 3, (1, 1): 9, (4, 4): 2})
    当前世界.设区块源数据((0,0),chk)


def 加载区块(pos = (0,0)) -> list:
    global 当前世界

    return 当前世界.取区块(pos)
    

生成世界()


