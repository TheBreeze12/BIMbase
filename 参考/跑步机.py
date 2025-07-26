from pyp3d import *
class 跑步机(Component):
    def __init__(self):
        Component.__init__(self)
        self['跑步机长度'] = Attr(1750, obvious = True,group='跑步机')
        self['跑步机宽度'] = Attr(840, obvious = True,group='跑步机')
        self['跑步机高度'] = Attr(1170, obvious = True,group='跑步机')
        
        self['跑步机'] = Attr(None, show = True)
    @export
    def replace(self): 
        
        L = self['跑步机长度']
        W = self['跑步机宽度']
        H = self['跑步机高度']
         
        #底部
        head_sec = rotx(0.5*pi)*Section(Vec2(0,0),Vec2(356.6,0),Arc(Vec2(356.6,153.6),Vec2(349.7,176.4),Vec2(330.6,190.4)),
                           Arc(Vec2(330.6,190.4),Vec2(162.5,175),Vec2(10.4,101.6)),
                           Arc(Vec2(10.4,101.6),Vec2(2.7,89.9),Vec2(0,76.2)))
        head_down = Loft(translate(0,-W/2,0)*head_sec,translate(0,W/2,0)*head_sec).color(141/255,182/255,223/255,1)
        wheel_sec = translate(0,-88.9,0)*Section(Arc(Vec2(25.4,0),Vec2(43.9,7.6),Vec2(51.5,26.1)),Vec2(51.5,88.9),Vec2(0,88.9),Vec2(0,0))
        wheel = rotz(0.5*pi)*Sweep(wheel_sec,roty(0.5*pi)*Line(Arc(2*pi)))
        wheel1 = translate(177.8,W/2-25.4,38.1)*wheel
        wheel2 = translate(177.8,-W/2+25.4,38.1)*rotz(pi)*wheel
        down_sec = rotz(pi/2)*rotx(pi/2)*Section(Vec2(W/2,0),Vec2(W/2,152.4),Arc(Vec2(W/2-101.6,152.4),Vec2(W/2-119.6,145),Vec2(W/2-127,127)),
                           Vec2(W/2-127,101.6),Vec2(-W/2+127,101.6),Arc(Vec2(-W/2+127,127),Vec2(-W/2+119.6,145),Vec2(-W/2+101.6,152.4)),
                           Vec2(-W/2,152.4),Vec2(-W/2,0))
        down = Loft(translate(356.6,0,0)*down_sec,translate(L,0,0)*down_sec).color(141/255,182/255,223/255,1)
        base_sec = rotx(0.5*pi)*Section(Vec2(0,0),Vec2(31,-50.8),Arc(Vec2(209.4,-50.8),Vec2(236.4,-39.6),Vec2(247.5,0)))
        base_down = translate(L-269,0,0)*Loft(translate(0,-W/2,0)*base_sec,translate(0,W/2,0)*base_sec)
        rug = translate(356.6,-W/2+127,101.6)*scale(L-356.6,W-127*2,25)*Cube()+Cone(Vec3(L,-W/2+127,101.6),Vec3(L,W/2-127,101.6),25,25)
        #支撑
        support1 = Box(Vec3(400,W/2,-50.8),Vec3(205,W/2,H-50.8*2),Vec3(1,0,0),Vec3(0,1,0),103,50.8,103,50.8).color(141/255,182/255,223/255,1)
        support2 = translate(0,-W-50.8,0)*support1
        #顶部
        panel_sec = rotz(-0.5*pi)*Section(Arc(Vec2(-W/2-76.2,141.3),Vec2(0,45),Vec2(W/2+76.2,141.3)),Vec2(W/2+76.2,432.8),
                            Arc(Vec2(W/2-116.8,432.8),Vec2(W/2-123.9,378),Vec2(W/2-152.4,330)),
                            Arc(Vec2(-W/2+152.4,330),Vec2(-W/2+123.9,378),Vec2(-W/2+116.8,432.8)),
                            Vec2(-W/2-76.2,432.8))
        panel = Loft(translate(0,0,H-50.8*2)*panel_sec,translate(0,0,H-50.8)*panel_sec).color(141/255,182/255,223/255,1)
        handrail = FilletPipe([Vec3(736.6,W/2-84.5,H-50.8-88.4),Vec3(202.8,W/2-84.5,H-50.8-88.4),Vec3(202.8,-W/2+84.5,H-50.8-88.4),
                               Vec3(736.6,-W/2+84.5,H-50.8-88.4)],[0,80,80,0],32)
        displayer_sec = rotx(0.5*pi)*Section(Vec2(180,0),Vec2(25.4,72.4),Vec2(25.4,152),Vec2(0,152),Vec2(0,0))
        displayer = translate(97,0,H-50.8)*Loft(translate(0,-W/2+200,0)*displayer_sec,translate(0,W/2-200,0)*displayer_sec).color(141/255,182/255,223/255,1)
        #最终结果head_down,wheel1,wheel2
        self['跑步机'] = Combine(head_down,wheel1,wheel2,down,base_down,rug,support1,support2,panel,handrail,displayer)
if __name__ == "__main__":
    FinalGeometry = 跑步机()
    FinalGeometry.replace()
    place(FinalGeometry)
