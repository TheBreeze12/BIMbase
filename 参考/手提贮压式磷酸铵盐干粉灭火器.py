from pyp3d import *
# import MepElement

# class 手提贮压式磷酸铵盐干粉灭火器(MepElement.灭火器):
class 手提贮压式磷酸铵盐干粉灭火器(Component):
    def __init__(self):
        # MepElement.灭火器.__init__(self)
        Component.__init__(self)
        self['手提贮压式磷酸铵盐干粉灭火器'] = Attr(None, show = True)
        self['型号'] = Attr('MFZ/ABC1', obvious = True, combo = ['MFZ/ABC1', 'MFZ/ABC2', 'MFZ/ABC3', 'MFZ/ABC4', 'MFZ/ABC5', 'MFZ/ABC6', 'MFZ/ABC8'], group = "型号", description = "型号选择")
        self['属地'] = Attr('浙江杭消', obvious = True, combo = ['浙江杭消', '广东胜捷', '广东平安'], group = "型号", description = "型号选择")
        self['直径'] = Attr(0, obvious = True, readonly = True, group = "尺寸", description = "单位(mm)")
        self['高度'] = Attr(0, obvious = True, readonly = True, group = "尺寸", description = "单位(mm)")
        # #专业属性
        # self['Manufacturer'] = '通用'           #厂家       Type: cstring
        # self['EQPType'] = '001'                 #设备型号   Type: cstring
        # self['ExtinguisherType'] = 1            #灭火器类型         Type: int        属性值: 1,手提式 2,推车式 999,其他
        # self['AgentType'] = 3                   #灭火剂形式	        Type: int        属性值:1,水基水灭火剂 2, 水基泡沫灭火剂 3,干粉灭火剂  4,二氧化碳灭火剂 5,洁净气体灭火剂 999,其他
        # self['ServicePressure'] = 0.0           #工作压力MPa        Type: double
        # self['MaxServicePressure'] = 0.0        #最大工作压力MPa    Type: double
        # self['EffectDischargeTime'] = 0.0       #有效喷射时间S      Type: double
        # self['DelayedActionTime'] = 0.0         #喷后滞后时间       Type: double
        # self['BulkRange'] = 0.0                 #喷射距离m          Type: double
        # self['FireType'] = 1                    #火灾类别           Type: int        属性值：  1、A （A类火灾） 2、B（B、C类火灾） 
        # self['LevelNum'] = 3.0                  #灭火级别           Type: double
    @export
    def replace(self):
        list = {
            'MFZ/ABC1':{
                '浙江杭消':{'DN':93.6 ,'A':88, 'H':300, 'h':250, "a":1},
                '广东胜捷':{'DN':99 ,'A':100, 'H':293, 'h':216, "a":1},
                '广东平安':{'DN':90 ,'A':109, 'H':318, 'h':234, "a":1}
            },
            'MFZ/ABC2':{
                '浙江杭消':{'DN':111.6 ,'A':105, 'H':370, 'h':300, "a":1},
                '广东胜捷':{'DN':99 ,'A':100, 'H':429, 'h':352, "a":1},
                '广东平安':{'DN':115 ,'A':109, 'H':372, 'h':288, "a":1}
            },
            'MFZ/ABC3':{
                '浙江杭消':{'DN':131.6 ,'A':105, 'H':410, 'h':343, "a":2},
                '广东胜捷':{'DN':131 ,'A':120, 'H':423, 'h':338, "a":2},
                '广东平安':{'DN':132 ,'A':124, 'H':415, 'h':327, "a":2}
            },
            'MFZ/ABC4':{
                '浙江杭消':{'DN':131.6 ,'A':120, 'H':480, 'h':405, "a":2},
                '广东胜捷':{'DN':131 ,'A':120, 'H':484, 'h':400, "a":2},
                '广东平安':{'DN':138 ,'A':124, 'H':470, 'h':382, "a":2}
            },
            'MFZ/ABC5':{
                '浙江杭消':{'DN':147 ,'A':120, 'H':490, 'h':410, "a":3},
                '广东胜捷':{'DN':131 ,'A':120, 'H':574, 'h':490, "a":3},
                '广东平安':{'DN':145 ,'A':124, 'H':520, 'h':432, "a":3}
            },
            'MFZ/ABC6':{
                '广东胜捷':{'DN':165 ,'A':120, 'H':477, 'h':392, "a":3}
            },
            'MFZ/ABC8':{
                '浙江杭消':{'DN':165 ,'A':120, 'H':580, 'h':512, "a":4},
                '广东胜捷':{'DN':165 ,'A':120, 'H':592, 'h':507, "a":4},
                '广东平安':{'DN':165 ,'A':124, 'H':610, 'h':522, "a":4}
            }
        }
        type = list[self['型号']]
        parameter = type[self['属地']]
        DN = parameter['DN']
        A = parameter['A']
        H = parameter['H']
        h = parameter['h']
        self['直径'] = parameter['DN']
        self['高度'] = parameter['H']
        self['LevelNum'] = float(parameter['a'])

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
        if self['型号'] == 'MFZ/ABC1' or self['型号'] == 'MFZ/ABC2' or self['型号'] == 'MFZ/ABC3':
            tap = translate(-DN/2+30,0,h+11)*Cone(Vec3(5,0,0),Vec3(-25,0,0),5,10).color(1,1,1,1)
        if self['型号'] == 'MFZ/ABC4' or self['型号'] == 'MFZ/ABC5' or self['型号'] == 'MFZ/ABC6' or self['型号'] == 'MFZ/ABC8':
            tap = Combine(
                translate(-DN/2+30,0,h-41)*TorusPipe(Vec3(0,0,0),Vec3(-1,0,0),Vec3(0,0,1),50,6,pi/2),
                translate(-DN/2-20,0,200)*Cone(Vec3(0,0,0),Vec3(0,0,h-241),6,6),
                translate(-DN/2-20,0,200)*Cone(Vec3(0,0,0),Vec3(0,0,-50),6,10)
            )
        out = Combine(
            translate(0,0,h)*Cone(Vec3(0,0,0),Vec3(0,0,1),10,10),
            translate(0,0,h+1)*Cone(Vec3(0,0,0),Vec3(0,0,20),DN/2-30,DN/2-30).color(1,215/255,0,1),
            tap
        )

        ##把手
        precision = 40  #精度
        hand_section = []
        for i in range(precision):
            hand_section.append(translate((A-10)/precision*i,0,(H-h-35)*sin(pi/2/precision*i))*Section(Vec2(3,10-5*sin(pi/2/precision*i)),Vec2(-3,10-5*sin(pi/2/precision*i)),Vec2(-3,-10+5*sin(pi/2/precision*i)),Vec2(3,-10+5*sin(pi/2/precision*i))))
        hand = Loft(hand_section)
        hand_group = Combine(
            translate(0,0,h+21)*Box(Vec3(-10,-10,0),Vec3(-10,-10,15),Vec3(1,0,0),Vec3(0,1,0),20,20,20,20),
            translate(0,0,h+21)*rotate(Vec3(0,1,0),15*pi/180)*hand,
            translate(0,0,h+36)*hand
        ).color(1,0,0,1)

        ##压力表
        pressure_gage = translate(0,-DN/2+30,h+11)*Combine(
            Cone(Vec3(0,0,0),Vec3(0,-5,0),15,15).color(0,0,0,1),
            Cone(Vec3(0,-5,0),Vec3(0,-5.5,0),13,13).color(1,1,1,1)
        )

        ##标签
        logo = translate(0,0,H/2)*Swept(rotate(Vec3(0,0,1),-pi/4)*translate(DN/2,0)*rotate(Vec3(1,0,0),pi/2)*Section(Vec2(0,20),Vec2(0.5,20),Vec2(0.5,-20),Vec2(0,-20)), Line(Arc(-pi/2))).color(1,215/255,0,1)

        self['手提贮压式磷酸铵盐干粉灭火器'] = Combine(
            cylinder,
            out,
            hand_group,
            pressure_gage,
            logo
        ) 
        # self['手提贮压式磷酸铵盐干粉灭火器'] =out 

if __name__ == "__main__":
    finalgeometry = 手提贮压式磷酸铵盐干粉灭火器()
    finalgeometry.replace()
    place(finalgeometry)