from pyp3d import *
# 扫掠体

class 扫掠(Component):
    def __init__(self):
        Component.__init__(self)
        self['角度'] = Attr(90.0, obvious=True)
        self['边长'] = Attr(500.0, obvious=True)
        self['扫掠体'] = Attr(None, show=True)

        self.replace()
    @export
    def replace(self):
        r = self['角度']
        L = self['边长']
        sectionOut = rotate(Vec3(1,0,0), 0.5*pi) * Section(Vec2(0,0), Vec2(L,0), Vec2(L,L), Vec2(0,L))
        section_1 = trans(200,0,0)*rotate(Vec3(1,0,0), 0.5*pi) * Section(Vec2(80,80), Vec2(60,80), Vec2(60,60), Vec2(80,60))
        # section_2 = translation(200,0,0) * rotate(Vec3(1,0,0), 0.5*pi) * Section(Vec2(50,50), Vec2(20,50), Vec2(20,20), Vec2(50,20))
        # testarc = Arc(Vec2(0,0),Vec2(L,L),Vec2(0,L*2))
        line1 = Line(Arc(r*pi/180)) # 只取角度值，半径取决于截面到原点距离
        line2 = Line(Vec2(100,-100), Vec2(-100,100)) # Sweep只能进行两点线段的扫掠
        sweep1 = Sweep(section_1, line1) 
        sweep2 = sweep_stere(section_1,line2) # 多段线扫掠需要使用 sweep_stere函数
        self['扫掠体'] = sweep1

if __name__ == "__main__":
    FinalGeometry = 扫掠()
    FinalGeometry.replace()
    place(FinalGeometry)

