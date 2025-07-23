# 说明 卷帘门基类中 门宽是900 而任务中是2390  基类门高是2100 任务是2900


from pyp3d import *
# import Door

# class 侧装钢防火卷帘(Door.卷帘门):
class 侧装钢防火卷帘(Component):
    # 定义各个参数及其默认值
    def __init__(self):
        # Door.卷帘门.__init__(self)
        Component.__init__(self)
        self['顶部箱体宽度'] = Attr(300 , obvious = True , group = '顶部箱体')      
        self['侧装钢防火卷帘'] = Attr(None , show=True)
        self['门宽'] = Attr(2390 , obvious = True , group = '底座')
        self['门高'] = Attr(2900 , obvious = True , group = '底座')

    
    @export
    def replace(self):
        # 设置变量，同时调用参数      
        W = self['顶部箱体宽度'] 
        doorW = self['门宽']
        doorH = self['门高']
                
        # 开始写模型
        # 顶部箱体
        box = translate(- doorW/2 , - W/2 , 2400/2900 * doorH) * \
            scale(doorW , W , 500/2900 * doorH) * Cube()


        # 左边大柱子
        big_pillar = translate(- doorW/2 , 230/600 * W , 0) * \
            scale(70/2390 * doorW , 70/600 * W , 2400/2900 * doorH) * Cube()
        # 右边大柱子
        right_pillar = translate(2320/2390 * doorW , 0 , 0) * big_pillar


        # 左边小柱子
        small_left = translate(- 1125/2390 * doorW , 240/600 * W , 0) * \
            scale(75/2390 * doorW , 60/600 * W , 2400/2900 * doorH) * Cube()
        # 右边小柱子
        small_right = translate(2175/2390 * doorW , 0 , 0) * small_left


        # 中间卷条
        bar = translate(- 1125/2390 * doorW , 265/600 * W , - 12/2900 * doorH) * \
            scale(2250/2390 * doorW , 10/600 * W , 24/2900 * doorH) * Cube()
        # # 转换成Array （数组）  
        test_bar = Array(bar)
        # for 循环  线性排布
        for i in linspace(Vec3(0 , 0 , 12/2900 * doorH) , Vec3(0 , 0 , 2388/2900 * doorH) , 100):
               test_bar.append(translate(i))


        # 右边大方块
        right_big_box = translate(doorW/2 + 80/2390 * doorW , 270/600 * W , 1575/2900 * doorH) * \
            scale(100/2390 * doorW , 30/600 * W , 150/2900 * doorH) * Cube()
        # 右边小方块
        right_small_box = translate(doorW/2 + 120/2390 * doorW , 290/600 * W , 1225/2900 * doorH) * \
            scale(30/2390 * doorW , 10/600 * W , 150/2900 * doorH) * Cube()


        # 组合一下 下部为插入点
        self['侧装钢防火卷帘'] = rotate(Vec3(1 , 0 , 0) , - pi/2) *translate(0 , - 270/600 * W , 0) *  \
            Combine(box , big_pillar , right_pillar , small_left , small_right , test_bar , right_big_box , right_small_box) . \
                color(128/255 , 128/255 , 128/255 , 1)

if __name__ == "__main__":
    FinalGeometry = 侧装钢防火卷帘()
    # 实现旋转布置
    RotationPlace.RotationFunction(FinalGeometry)
    FinalGeometry.replace()
    place(FinalGeometry)


