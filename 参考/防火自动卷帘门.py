from pyp3d import *
# 定义参数化模型
class 防火自动卷帘门(Component):
    # 定义各个参数及其默认值
    def __init__(self):
        Component.__init__(self)
        self['防火自动卷帘门'] = Attr(None, show=True)
        self['门板厚度'] = Attr(50, show=True, obvious=True)
        self['门高'] = Attr(4000, show=True, obvious=True)
        self['门宽'] = Attr(4200, show=True, obvious=True)
        self.replace()
    @export
    def replace(self):
        h = self['门高']
        L = self['门宽']
        W = self['门板厚度']     
    
        #门框
        self['左门框'] =  Box(Vec3(0,0,0),Vec3(0,0,h),Vec3(1,0,0),Vec3(0,1,0), 42, W, 42, W).color(0,0,0,0)
        self['右门框'] =  Box(Vec3(L-42,0,0),Vec3(L-42,0,h),Vec3(1,0,0),Vec3(0,1,0), 42, W, 42, W).color(0,0,0,0)
        self['下边框'] =  Box(Vec3(42,0,0),Vec3(42,0,42),Vec3(1,0,0),Vec3(0,1,0), L-84, W, L-84, W).color(0,0,0,0)

        #门主体
        self['门主体'] = Box(Vec3(42,0,h/2),Vec3(42,0,h),Vec3(1,0,0),Vec3(0,1,0), L-82, W/5, L-82, W/5).color(0.8,0.98,0.98)

        #自动收取器
        self['主体截面1'] = Section(Vec3(0,0,3400),Vec3(0,519.6,3100),Vec3(0,1039.2,3400),Vec3(0,1039.2,4000),Vec3(0,519.6,4300),Vec3(0,0,4000))
        self['主体截面2'] = Section(Vec3(L,0,3400),Vec3(L,519.6,3100),Vec3(L,1039.2,3400),Vec3(L,1039.2,4000),Vec3(L,519.6,4300),Vec3(L,0,4000))
        self['收取器'] = Loft(self['主体截面1'],self['主体截面2'])
        self['布尔减'] = (self['门主体']-self['收取器']).color(0.8,0.98,0.98)

        #开关
        self['开关'] = Cone(Vec3(L+500,-300,h/3),Vec3(L+500,0,h/3),100,100)
        
        #组合
        self['防火自动卷帘门'] = combine(self['左门框'],self['右门框'],self['下边框'], self['布尔减'],self['收取器'],self['开关'])

#输出模型
if __name__ == "__main__":
    FinalGeometry = 防火自动卷帘门()
    place(FinalGeometry)



    