from pyp3d import *
# import MepElement

# class 手提贮压式二氧化碳灭火器(MepElement.灭火器):
class 手提贮压式二氧化碳灭火器(Component):
    def __init__(self):
        # MepElement.灭火器.__init__(self)
        Component.__init__(self)
        self['手提贮压式二氧化碳灭火器'] = Attr(None, show = True)
        self['型号'] = Attr('MTZ/2', obvious = True, combo = ['MTZ/2', 'MTZ/3', 'MTZ/5'], group = "型号", description = "型号选择")
        self['直径'] = Attr(0, obvious = True, readonly = True, group = "尺寸", description = "单位(mm)")
        self['高度'] = Attr(0, obvious = True, readonly = True, group = "尺寸", description = "单位(mm)")
        # #专业属性
        # self['Manufacturer'] = '通用'           #厂家       Type: cstring
        # self['EQPType'] = '001'                 #设备型号   Type: cstring
        # self['ExtinguisherType'] = 1            #灭火器类型         Type: int        属性值: 1,手提式 2,推车式 999,其他
        # self['AgentType'] = 4                   #灭火剂形式	        Type: int        属性值:1,水基水灭火剂 2, 水基泡沫灭火剂 3,干粉灭火剂  4,二氧化碳灭火剂 5,洁净气体灭火剂 999,其他
        # self['ServicePressure'] = 0.0           #工作压力MPa        Type: double
        # self['MaxServicePressure'] = 0.0        #最大工作压力MPa    Type: double
        # self['EffectDischargeTime'] = 0.0       #有效喷射时间S      Type: double
        # self['DelayedActionTime'] = 0.0         #喷后滞后时间       Type: double
        # self['BulkRange'] = 0.0                 #喷射距离m          Type: double
        # self['FireType'] = 2                    #火灾类别           Type: int        属性值：  1、A （A类火灾） 2、B（B、C类火灾） 
        # self['LevelNum'] = 3.0                  #灭火级别           Type: double
    @export
    def replace(self):
        list = {
            'MTZ/2':{'DN':116, 'H':495, 'h':400, "b":21},
            'MTZ/3':{'DN':116, 'H':645, 'h':550, "b":21},
            'MTZ/5':{'DN':154, 'H':615, 'h':520, "b":34}
        }
        parameter = list[self['型号']]
        DN = parameter['DN']
        H = parameter['H']
        h = parameter['h']
        self['直径'] = parameter['DN']
        self['高度'] = parameter['H']
        self['LevelNum'] = float(parameter['b'])

        ##钢瓶
        cylinder = Swept(rotate(Vec3(1,0,0),pi/2)*Section(
            Vec2(0,0),
            translate(DN/2-5,5)*rotate(Vec3(0,0,1),-pi/2)*scale(5)*Arc(pi/2),
            translate(DN/2-1,40)*Arc(pi/2),
            translate(DN/2-1,44)*rotate(Vec3(0,0,1),-pi/2)*Arc(pi/2),
            translate(DN/2-30,h-10-40)*scale(30,40)*Arc(pi/2),
            Vec2(DN/2-30,h),
            Vec2(0,h)
        ), Line(Arc(2*pi))).color(255/255,48/255,48/255,1)

        ##阀体总成和喷嘴
        tap = Combine(
            translate(DN/2-30,0,h-41)*TorusPipe(Vec3(0,0,0),Vec3(1,0,0),Vec3(0,0,1),50,6,pi/2),
            translate(DN/2+20,0,200)*Cone(Vec3(0,0,0),Vec3(0,0,h-241),6,6),
            translate(DN/2+20,0,200)*Cone(Vec3(0,0,0),Vec3(0,0,-100),6,10)
        ).color(0,0,0,1)
        out = Combine(
            translate(0,0,h)*Cone(Vec3(0,0,0),Vec3(0,0,1),10,10),
            translate(0,0,h+1)*Cone(Vec3(0,0,0),Vec3(0,0,20),DN/2-30,DN/2-30).color(1,215/255,0,1),
            Cone(Vec3(0,0,h+11),Vec3(-DN/2+20,0,h+11),5,5),
            tap
        )

        ##把手
        hand_group = translate(0,0,h+21)*Cone(Vec3(0,0,0),Vec3(0,0,H-h-21),DN/2-45,DN/2-45).color(255/255,48/255,48/255,1)

        ##压力表
        pressure_gage = translate(0,-DN/2+30,h+11)*Combine(
            Cone(Vec3(0,0,0),Vec3(0,-5,0),15,15).color(0,0,0,1),
            Cone(Vec3(0,-5,0),Vec3(0,-5.5,0),13,13).color(1,1,1,1)
        )

        ##标签
        logo = translate(0,0,H/2)*Swept(rotate(Vec3(0,0,1),-pi/4)*translate(DN/2,0)*rotate(Vec3(1,0,0),pi/2)*Section(Vec2(0,20),Vec2(0.5,20),Vec2(0.5,-20),Vec2(0,-20)), Line(Arc(-pi/2))).color(1,215/255,0,1)

        self['手提贮压式二氧化碳灭火器'] = Combine(
            cylinder,
            out,
            hand_group,
            pressure_gage,
            logo
        )
        # self['手提贮压式二氧化碳灭火器'] = out

if __name__ == "__main__":
    finalgeometry = 手提贮压式二氧化碳灭火器()
    finalgeometry.replace()
    place(finalgeometry)