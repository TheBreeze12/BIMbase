import pyp3d as p3d
from pyp3d import *
class 硬化路面转弯(Component):
    def __init__(self):
        Component.__init__(self)
        self['路面宽度(mm)'] = Attr(3500, obvious = True)
        self['路面厚度(mm)'] = Attr(200, obvious = True)
        self['转弯角度(角度制)'] = Attr(90, obvious = True)
        self['转弯半径(沿道路内侧)'] = Attr(3500, obvious = True)
        self['水平方向上的旋转角度（角度制）'] = Attr(0.00, obvious = True)
        self['硬化路面类型二'] = Attr(None, show = True)
        self['场布类型'] = Attr('道路交通',obvious=True,readonly=True,group='公共属性',description='场布类型')
        self['构件类型'] = Attr('硬化路面',obvious=True,readonly=True,group='公共属性',description='构件类型')
        self['构件名称'] = Attr('硬化路面转弯',obvious=True)


        self.replace()
    @export
    def replace(self):
        
        K = self['路面宽度(mm)']
        H = self['路面厚度(mm)']
        R = self['转弯角度(角度制)']
        R1 = self['转弯半径(沿道路内侧)']
        Rotation = self['水平方向上的旋转角度（角度制）']

        #旋转扫描
        A = RotationalSweep([Vec3(-K/2,0,-H/2),Vec3(K/2,0,-H/2),Vec3(K/2,0,H/2),Vec3(-K/2,0,H/2)],Vec3((K/2)+R1,0,0),Vec3(0,0,1),R/180*pi).color(0.5,0.5,0.5,1)
        self['硬化路面类型二'] = rotation(Vec3(0,0,1),Rotation/180*pi)*A
 



if __name__ == "__main__":
    FinalGeometry = 硬化路面转弯()
    place(FinalGeometry)