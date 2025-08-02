from re import T
from pyp3d import *

class 电缆拖链(Component):
    def __init__(self):
        Component.__init__(self)
        self['电缆拖链节数']=Attr(30,obvious=True)
        self['每一节长度']=Attr(150,obvious=True)
        self['每一节宽度']=Attr(50,obvious=True)
        self['每一节高度']=Attr(100,obvious=True)
        self['转弯直径']=Attr(400,obvious=True)
        self['电缆拖链']=Attr(None,show=True)
        self.replace()
    @export
    
    def replace(self):
        l= self['每一节长度']
        w= self['每一节宽度']
        h= self['每一节高度']
        d=self['转弯直径']
        num=self['电缆拖链节数']
        
        num_r=(int)(pi*d/2/w)
        num_l=(int)((num-num_r)/2)
        num_r=(int)(num-num_l*2)
        cube=Combine(scale(w-1,l,h)*Cube(),trans(w-1)*scale(1,l,h)*Cube().color(0,0,0,1))
        cubes1=[]
        for i in range(0,num_l):
            cubes1.append(trans(i*w,0,0)*cube)
        r=d/2
        c=num_r*w
        rcube=RotationalSweep([Vec3(0,0,r),Vec3(0,l,r),Vec3(0,l,h+r),Vec3(0,0,h+r)],Vec3(0,0,0),Vec3(0,1,0),((w-1)/c)*pi)
        rcube1=roty(((w-1)/c)*pi)*RotationalSweep([Vec3(0,0,r),Vec3(0,l,r),Vec3(0,l,h+r),Vec3(0,0,h+r)],Vec3(0,0,0),Vec3(0,1,0),((1)/c)*pi).color(0,0,0,1)
        rcube=Combine(rcube,rcube1)
        rcubes=[]
        for i in range(0,num_r):
            rcubes.append(roty(i*w/c*pi)*rcube)
        rcubes=trans(num_l*w,0,-r)*rcubes
        cubes2=trans(0,0,-d-h)*cubes1
        self['电缆拖链']=Combine(cubes1,rcubes,cubes2)

if __name__=="__main__":
    final=电缆拖链()
    place(final)