from pyp3d import *
class 灭火器(Component):
    def __init__(self):
        Component.__init__(self)
        self['种类']=Attr('ABC干粉',obvious=True,combo=["ABC干粉","CO2","水基型"])
        self['充装量']=Attr("1kg",obvious = True, group = "尺寸",combo=["1kg","2kg","3kg","4kg","5kg"])
        
        self['总高度']=Attr(0, obvious = True, readonly = True, group = "尺寸")
        self['主体高度']=Attr(0, obvious = True, readonly = True, group = "尺寸")
        self['瓶体的外径']=Attr(0, obvious = True, readonly = True, group = "尺寸")
        self['是否配备压力指示器']=Attr(True,obvious=True,group="压力表")
        self['压力表的表盘直径']=Attr(0, obvious = True, readonly = True, group = "压力表")
        self['喷射组件的类型']=Attr('直喷嘴',obvious=True,combo=['直喷嘴','软管+喷枪','软管+喇叭筒'])
        self['喷射软管的长度']=Attr(0,  obvious = True, readonly = True)
        self['CO2喇叭筒的长度']=Attr(0,obvious=True,readonly=True)
        self['CO2喇叭筒的直径']=Attr(0,obvious=True,readonly=True)
        self['铭牌上的文本信息']=Attr("",obvious=True,readonly=True)
        self['是否生成墙壁挂架']=Attr(False,obvious=True)
        self['灭火器']=Attr(None,show=True)
        self.replace()
    @export
    def replace(self):
        
        if self['种类']=='ABC干粉':
            self['充装量']=Attr(self['充装量'], obvious = True, group = "尺寸",combo=["1kg","2kg","3kg","4kg","5kg"])
        elif self['种类']=='CO2':
            self['充装量']=Attr(self['充装量'], obvious = True, group = "尺寸",combo=["2kg","3kg","5kg","7kg"])
        elif self['种类']=='水基型':
            self['充装量']=Attr(self['充装量'], obvious = True, group = "尺寸",combo=["2L","3L","4L","6L","9L"])
        # ABC干粉灭火器参数表
        abc_extinguisher_data = {
            "1kg": {
                "型号": "MFZ/ABC1",
                "充装量": "1kg",
                "总高度": 320,  # 300-340mm的中间值
                "主体高度": 250,
                "外径": 117.5,  # 110-125mm的中间值
                "压力表直径": 35,
                "喷射组件": ["直喷嘴","软管+喷枪"],
                "软管长度": 250,  # 400-450mm的中间值
                "喇叭筒": "不适用"
            },
            
            "2kg": {
                "型号": "MFZ/ABC2", 
                "充装量": "2kg",
                "总高度": 395,  # 380-410mm的中间值
                "主体高度": 320,
                "外径": 130,    # 125-135mm的中间值
                "压力表直径": 35,
                "喷射组件": ["软管+喷枪"],
                "软管长度": 250,
                "喇叭筒": "不适用"
            },
            
            "3kg": {
                "型号": "MFZ/ABC3",
                "充装量": "3kg",
                "总高度": 450,  # 440-460mm的中间值
                "主体高度": 380,
                "外径": 150,    # 145-155mm的中间值
                "压力表直径": 35,
                "喷射组件": ["软管+喷枪"],
                "软管长度": 250,
                "喇叭筒": "不适用"
            },
            "4kg": {
                "型号": "MFZ/ABC4",
                "充装量": "4kg", 
                "总高度": 500,  # 480-520mm的中间值
                "主体高度": 420,
                "外径": 150,    # 145-155mm的中间值
                "压力表直径": 35,
                "喷射组件": ["软管+喷枪"],
                "软管长度": 400,
                "喇叭筒": "不适用"
            },
            "5kg": {
                "型号": "MFZ/ABC5",
                "充装量": "5kg",
                "总高度": 535,  # 520-550mm的中间值
                "主体高度": 440,
                "外径": 155,    # 150-160mm的中间值
                "压力表直径": 35,
                "喷射组件": ["软管+喷枪"], 
                "软管长度": 400,
                "喇叭筒": "不适用"
            }
        }
        # CO2灭火器参数表
        co2_extinguisher_data = {
            "2kg": {
                "型号": "MFZ/CO22",
                "充装量": "2kg",
                "总高度": 525,
                "主体高度": 440,
                "外径": 145,
                "压力表直径": 0,
                "喷射组件": ["软管+喇叭筒"],
                "软管长度": 350,
                "喇叭筒": "适用",
                "喇叭筒长度": 200,
                "喇叭筒直径": 40
            },
            "3kg": {
                "型号": "MFZ/CO23",
                "充装量": "3kg",
                "总高度": 600,
                "主体高度": 520,
                "外径": 160,
                "压力表直径": 0,
                "喷射组件": ["软管+喇叭筒"],
                "软管长度": 350,
                "喇叭筒": "适用",
                "喇叭筒长度": 200,
                "喇叭筒直径": 40
            },
            "5kg": {
                "型号": "MFZ/CO25",
                "充装量": "5kg",
                "总高度": 720,
                "主体高度": 640,
                "外径": 180,
                "压力表直径": 0,
                "喷射组件": ["软管+喇叭筒"],
                "软管长度": 400,
                "喇叭筒": "适用",
                "喇叭筒长度": 200,
                "喇叭筒直径": 40
            },
            "7kg": {
                "型号": "MFZ/CO27",
                "充装量": "7kg",
                "总高度": 850,
                "主体高度": 730,
                "外径": 200,
                "压力表直径": 0,
                "喷射组件": ["软管+喇叭筒"],
                "软管长度": 500,
                "喇叭筒": "适用",
                "喇叭筒长度": 200,
                "喇叭筒直径": 40
            }
        }
        # 水基型灭火器参数表
        water_extinguisher_data = {
            "2L": {
                "型号": "MFZ/W2L",
                "充装量": "2L",
                "总高度": 350,
                "主体高度": 280,
                "外径": 125,
                "压力表直径": 35,
                "喷射组件": ["直喷嘴","软管+喷枪"],
                "软管长度": 300,
                "喇叭筒": "不适用"
            },
            "3L": {
                "型号": "MFZ/W3L",
                "充装量": "3L",
                "总高度": 380,
                "主体高度": 310,
                "外径": 130,
                "压力表直径": 35,
                "喷射组件": ["软管+喷枪"],
                "软管长度": 300,
                "喇叭筒": "不适用"
            },
            "4L": {
                "型号": "MFZ/W4L",
                "充装量": "4L",
                "总高度": 450,
                "主体高度": 380,
                "外径": 145,
                "压力表直径": 35,
                "喷射组件": ["软管+喷枪"],
                "软管长度": 400,
                "喇叭筒": "不适用"
            },
            "6L": {
                "型号": "MFZ/W6L",
                "充装量": "6L",
                "总高度": 535,
                "主体高度": 440,
                "外径": 155,
                "压力表直径": 35,
                "喷射组件": ["软管+喷枪"],
                "软管长度": 400,
                "喇叭筒": "不适用"
            },
            "9L": {
                "型号": "MFZ/W9L",
                "充装量": "9L",
                "总高度": 650,
                "主体高度": 550,
                "外径": 140,
                "压力表直径": 35,
                "喷射组件": ["软管+喷枪"],
                "软管长度": 400,
                "喇叭筒": "不适用"
            }
        }
        
        # 根据种类和充装量获取参数
        if self['种类'] == 'ABC干粉':
            if self['充装量'] not in abc_extinguisher_data:
                self['充装量']='1kg'
            if self['充装量'] in abc_extinguisher_data:
                data = abc_extinguisher_data[self['充装量']]
                self['总高度'] = data['总高度']
                self['瓶体的外径'] = data['外径']
                self['主体高度'] = data['主体高度']
                self['压力表的表盘直径'] = data['压力表直径']
                self['喷射软管的长度'] = data['软管长度']
                self['铭牌上的文本信息'] = data['型号']
                if self['喷射组件的类型'] == '软管+喇叭筒':
                    self['喷射组件的类型'] = "软管+喷枪"
        elif self['种类'] == 'CO2':
            if self['充装量'] not in co2_extinguisher_data:
                self['充装量']='2kg'
            self['充装量']=Attr(self['充装量'], obvious = True, group = "尺寸",combo=["2kg","3kg","5kg","7kg"])
            if self['充装量'] in co2_extinguisher_data:
                data = co2_extinguisher_data[self['充装量']]
                self['总高度'] = data['总高度']
                self['瓶体的外径'] = data['外径']
                self['主体高度'] = data['主体高度']
                self['压力表的表盘直径'] = data['压力表直径']
                self['喷射软管的长度'] = data['软管长度']
                self['CO2喇叭筒的长度'] = data['喇叭筒长度']
                self['CO2喇叭筒的直径'] = data['喇叭筒直径']
                self['是否配备压力指示器'] = False
                self['铭牌上的文本信息'] = data['型号']
            self['喷射组件的类型'] = "软管+喇叭筒"
        elif self['种类'] == '水基型':
            if self['充装量'] not in water_extinguisher_data:
                self['充装量']='2L'
            if self['充装量'] in water_extinguisher_data:
                data = water_extinguisher_data[self['充装量']]
                self['总高度'] = data['总高度']
                self['瓶体的外径'] = data['外径']
                self['主体高度'] = data['主体高度']
                self['压力表的表盘直径'] = data['压力表直径']
                self['喷射软管的长度'] = data['软管长度']
                self['铭牌上的文本信息'] = data['型号']
                if self['喷射组件的类型'] == '软管+喇叭筒':
                    self['喷射组件的类型'] = "软管+喷枪"
        DN = self['瓶体的外径']  # 从数据表获取
        H = self['总高度']       # 从数据表获取
        h = self['主体高度']  # 瓶体主体高度约为总高度的82%
        A = 100  # 把手参数，可以根据需要调整
        l = self['喷射软管的长度']

        # 1.钢瓶
        cylinder = Swept(rotate(Vec3(1,0,0),pi/2)*Section(
            Vec2(0,0),
            translate(DN/2-5,5)*rotate(Vec3(0,0,1),-pi/2)*scale(5)*Arc(pi/2),
            translate(DN/2-1,40)*Arc(pi/2),
            translate(DN/2-1,44)*rotate(Vec3(0,0,1),-pi/2)*Arc(pi/2),
            translate(DN/2-30,h-10-40)*scale(30,40)*Arc(pi/2),
            Vec2(DN/2-30,h),
            Vec2(0,h)
        ), Line(Arc(2*pi))).color(255/255,48/255,48/255,1)
        # 2.阀门总成+喷射装置 位于瓶体顶部的复杂组件，包括阀体、提把、压把和保险销TODO
        if self['喷射组件的类型']=='直喷嘴':
            tap = translate(-DN/2+30,0,h+11)*Cone(Vec3(5,0,0),Vec3(-25,0,0),8,15).color(1,1,1,1)
        elif self['喷射组件的类型']=='软管+喷枪':
            tap = Combine(
                translate(-DN/2+30,0,h-41)*TorusPipe(Vec3(0,0,0),Vec3(-1,0,0),Vec3(0,0,1),50,6,pi/2),
                translate(-DN/2-20,0,h-41-l+50*pi/2)*Cone(Vec3(0,0,0),Vec3(0,0,l-50*pi/2),6,6),
                translate(-DN/2-20,0,h-41-l+50*pi/2)*Cone(Vec3(0,0,0),Vec3(0,0,-50),6,10)
            )
        else:
            l=self['CO2喇叭筒的长度']
            d=self['CO2喇叭筒的直径']
            tap = Combine(
                translate(-DN/2+30,0,h-41)*TorusPipe(Vec3(0,0,0),Vec3(-1,0,0),Vec3(0,0,1),50,6,pi/2),
                translate(-DN/2-20,0,50+l)*Cone(Vec3(0,0,0),Vec3(0,0,h-91-l),6,6),
                translate(-DN/2-20,0,50)*Cone(Vec3(0,0,0),Vec3(0,0,l),d/2,d/2-10)
            )
        out = Combine(
            translate(0,0,h)*Cone(Vec3(0,0,0),Vec3(0,0,1),10,10),
            translate(0,0,h+1)*Cone(Vec3(0,0,0),Vec3(0,0,20),DN/2-30,DN/2-30).color(1,215/255,0,1),
            tap
        )
        # 3.把手
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
        
        # 4. 压力表
        if self['是否配备压力指示器']:
            w = self['压力表的表盘直径']
            pressure_gage = translate(0,-DN/2+30,h+11)*Combine(
                Cone(Vec3(0,0,0),Vec3(0,-5,0),w/2,w/2).color(0,0,0,1),
                Cone(Vec3(0,-5,0),Vec3(0,-5.5,0),w/2-2,w/2-2).color(1,1,1,1)
            )
      
      
        # 5.TODO铭牌
        # 使用Swept方法创建标签，参考手提贮压式磷酸铵盐干粉灭火器.py
        logo = translate(0,0,H/2)*Swept(rotate(Vec3(0,0,1),-pi/4)*translate(DN/2,0)*rotate(Vec3(1,0,0),pi/2)*Section(Vec2(0,20),Vec2(0.5,20),Vec2(0.5,-20),Vec2(0,-20)), Line(Arc(-pi/2))).color(1,215/255,0,1)
        # text=translate(-DN/2,-DN/2,H/2)*rotate(Vec3(1,0,0),pi/2)*Text(self['铭牌上的文本信息'], 10,10).color(1,1,1,1)
        text_group = Combine(logo)
        
        # 6.墙壁挂架
        if self['是否生成墙壁挂架']:
            
             # 1. 圆环参数
            ring_t =6
            ring_r = DN/2 + 8
            ring_w = 12
            ring_up_z = 0.7*h
            ring_down_z = 0.3*h
            
            # 2. 背板
            back_height = h
            back_width = 60
            back_thick = 6
            back_plate = Box(
                Vec3(-back_width/2, DN/2+ring_t+3,0),
                Vec3(back_width/2, DN/2+ring_t+3, 0),
                Vec3(0,1,0), Vec3(0,0,1),
                back_thick, back_height,back_thick,back_height
            ).color(0.5,0.1,0,1)
            
            # 底板
            bottom_lenth=2/3*DN
            bottom_width=back_width
            bottom_thick=back_thick
            bottom_plate=Box(
                Vec3(-back_width/2, DN/2+ring_t+3+bottom_thick, -back_thick),
                Vec3(back_width/2, DN/2+ring_t+3+bottom_thick, -back_thick),
                Vec3(0,1,0), Vec3(0,0,1),
                -bottom_lenth, bottom_thick,-bottom_lenth,bottom_thick
            ).color(0.5,0.1,0,1)
            
            back_plate=Combine(back_plate,bottom_plate)
            

            # 3. 上下圆环
            ring_up =translate(0, 0, ring_up_z)*rotate(Vec3(1,0,0),pi/2)* TorusPipe(
                Vec3(0,0,0), Vec3(0,0,1), Vec3(1,0,0),
                ring_r, ring_t, 2*pi
            ).color(0.5,0.1,0,1)
            ring_down = translate(0, 0, ring_down_z)*rotate(Vec3(1,0,0),pi/2)*TorusPipe(
                Vec3(0,0,0), Vec3(0,0,1), Vec3(1,0,0),
                ring_r, ring_t, 2*pi
            ).color(0.5,0.1,0,1)


            # 4. 组合
            wall_bracket = Combine(
                back_plate,
                ring_up, ring_down,
            )
        
        # 7.灭火器
        self['灭火器']=Combine(cylinder,out,hand_group,text_group)
        if self['是否生成墙壁挂架']:
            self['灭火器']=Combine(self['灭火器'],wall_bracket)
        if self['是否配备压力指示器']:
            self['灭火器']=Combine(self['灭火器'],pressure_gage)
      
            
if __name__=="__main__":
    final=灭火器()
    place(final)
