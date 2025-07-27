from pyp3d import *

class 转弯传送带(Component):
    def __init__(self):
        Component.__init__(self)
        self['转弯角度']=Attr(60,obvious=True,group='弧形框架')
        self['中心线半径']=Attr(1000,obvious=True,group='弧形框架')
        self['传送带宽度']=Attr(1000,obvious=True,group='承载面')
        self['传送带类型']=Attr('皮带式',obvious=True,combo=['皮带式','滚筒式'],group='承载面')
        self['框架高度']=Attr(200,obvious=True,group='弧形框架')
        self['框架厚度']=Attr(50,obvious=True,group='弧形框架')
        self['护栏高度']=Attr(200,obvious=True,group='弧形框架')
        self['护栏厚度']=Attr(30,obvious=True,group='弧形框架')
        self['皮带材质']=Attr(0,obvious=True,group='皮带')
        self['皮带厚度']=Attr(20,obvious=True,group='皮带')
        self['滚筒直径']=Attr(40,obvious=True,group='滚筒')
        self['滚筒间距']=Attr(20,obvious=True,group='滚筒')
        self['滚筒类型']=Attr("Straight",obvious=True,group='滚筒',combo=['Tapered', 'Straight'])# TODO
        self['驱动方式']=Attr('头部驱动',obvious=True,group='驱动',combo=['头部驱动','中心驱动'])
        self['电机功率(W)']=Attr(1000,obvious=True,group='驱动')
        self['传送速度(m/s)']=Attr(1,obvious=True,group='驱动')
        self['是否带支架']=Attr(True,obvious=True,group='支架')
        self['支架离地高度']=Attr(1000,obvious=True,group='支架')
        self['支架数量']=Attr(2,obvious=True,group='支架')
        self['支架型材尺寸']=Attr("100*100",obvious=True,group='支架',combo=['100*100','100*200','100*300'])
        self['运行状态']=Attr(0,obvious=True,group='运行状态')
        self['转弯传送带']=Attr(None,show=True)
        self.replace()
    @export
    
    def replace(self):
        # 参数      
        center_r=self['中心线半径']
        W=self['传送带宽度']
        r=center_r-0.5*W
        R=center_r+0.5*W
        A=self['转弯角度']
        # 1.框架
        frame_h=self['框架高度']
        frame_t=self['框架厚度']
        frame1=createFrame(r,frame_t,frame_h,A,False).color(0.5,0.5,1,1)
        frame2=createFrame(R,frame_t,frame_h,A,True).color(0.5,0.5,1,1)
        frame=Combine(frame1,frame2)
        # 护栏
        guard_h=self['护栏高度']
        guard_t=self['护栏厚度']
        guard1=createFrame(r-frame_t+guard_t,guard_t,guard_h,A,False)
        guard2=createFrame(R+frame_t-guard_t,guard_t,guard_h,A,True)
        guard=trans(0,0,frame_h+10)*Combine(guard1,guard2)        
        
       # 框架与护栏的连接
        Link10=Box(Vec3(0,0,0),Vec3(0,-50,-1/4*guard_h),Vec3(1,0,0),Vec3(0,0,-1),50,0.5*(guard_h+frame_h),50,0.25*(guard_h+frame_h))
        Link20= mirror(trans(0,0,0) ,'XZ') * Link10
        a=A/2/180*pi
        Link1=trans((r-frame_t)*sin(a),(r-frame_t)*cos(a),frame_h+10+guard_h/2)*rotz(-A/180*pi/2)*Link10
        Link2=trans((R+frame_t)*sin(a),(R+frame_t)*cos(a),frame_h+10+guard_h/2)*rotz(-A/180*pi/2)*Link20
        
        # Link1=trans(L/2,0,frame_h+10+guard_h/2)*Link1
        # Link2=trans(L/2,W+2*frame_t,frame_h+10+guard_h/2)*Link2
        Link=Combine(Link1,Link2)
        框架总成=Combine(frame,guard,Link)
        
        #2. 承载面 
       # 皮带与滑板 : 如果传送带类型为皮带，则此部件为环形皮带及支撑皮带的底板。
        if self['传送带类型']=='皮带式':
           # 滑板
           belt_t=self['皮带厚度']
           board_w=W
           board_h=(frame_h-2*belt_t)/2
           board=trans(0,0,belt_t+board_h)*createFrame(r,board_w,board_h,A,True)
           # 皮带
           belt1=createFrame(r,board_w,belt_t,A,True)
           belt2=trans(0,0,frame_h-belt_t)*belt1
           Section1=Section(Vec3(0,0,0),trans(0,frame_h/2,0)*rotz(0.5*pi)*scale(frame_h/2)*Arc(pi))
           r2=frame_h/2-belt_t  
           Section2=trans(0,belt_t,0)*Section(Vec3(0,0,0),trans(0,r2,0)*rotz(0.5*pi)*scale(r2)*Arc(pi))
           belt3=trans(0,r,frame_h)*rotx(-pi*0.5)*Sweep(Section1-Section2,Line(Vec3(0,0,0),Vec3(0,0,W)))
           belt4=rotz(-A/180*pi)*trans(0,r,0)*roty(pi)*rotx(-pi*0.5)*Sweep(Section1-Section2,Line(Vec3(0,0,0),Vec3(0,0,W)))
           belt=Combine(belt1,belt2,belt3,belt4).color(0.2,0.2,0.2,1)
           承载面=Combine(board,belt)
           
       # 滚筒阵列 : 如果传送带类型为滚筒，则此部件由一系列平行排列的滚筒组成。
        else:
       # TODO:若为滚轮，则先创建一个滚筒子模型（滚筒直径，长度为Belt_Width）。然后，沿中心线弧路径，根据滚筒间距进行环形阵列，生成滚筒阵列。如果滚筒间距为Tapered，则滚筒应为锥形。
       # 对于锥形滚筒，可以绘制一个梯形截面，然后进行旋转操作生成。锥度应经过计算，以确保在转弯时内外侧的线速度匹配，公式为：内侧直径/外侧直径 = 内侧半径/外侧半径。

           roller_d=self['滚筒直径']
           roller_r=roller_d/2
           gap=self['滚筒间距']
           roller_num=(int)(center_r*A/180*pi/(roller_d+gap))
           cone1=trans(-roller_r,r-frame_t,0)*createRoller(roller_r,W,roller_r,frame_t,frame_h-roller_r)
           cones = []
           for i in linspace(0,A/180*pi,roller_num): 
              cones.append(rotz(-i)*cone1)
           承载面=Combine(cones)
      
        # 3.头/尾滚筒总成
        Cone1=trans(0,r,frame_h/2)*Cone(Vec3(0,0,0),Vec3(0,W,0),frame_h*3/8,frame_h*3/8)
        Cone2=rotz(-A/180*pi)*Cone1
        头尾滚筒总成=Combine(Cone1,Cone2).color(0.1,0.2,0.3,1)
        
       # 4.支撑腿总成  仅在是否带支架为True时生成。通常为H型结构，可调节高度。
        if self['是否带支架']:
           # 获取尺寸字符串
           size_str = self['支架型材尺寸']
           length,width = size_str.split('*')
           width_num = int(width)
           length_num = int(length)
           bracket_h=self['支架离地高度']
           bracket_num=self['支架数量']
           bracket_w=W+2*frame_t-width_num
           brackets=trans(0,0,-bracket_h+100)*createBrackets(bracket_num,A,bracket_w,length_num,width_num,bracket_h,r-frame_t,center_r)
           支撑架=Combine(brackets)        
        # 5.驱动单元
        驱动单元=createMotor()
        
        self['转弯传送带']=Combine(框架总成,承载面,头尾滚筒总成,驱动单元)
        if self['是否带支架']:
           self['转弯传送带']=Combine(self['转弯传送带'],支撑架)
def createFrame(r,t,h,A,isout):
    if isout:
        return RotationalSweep([Vec3(0,r,0),Vec3(0,r+t,0),Vec3(0,r+t,h),Vec3(0,r,h)],Vec3(0,0,0),Vec3(0,0,1),-A/180*pi)
    else:
        return RotationalSweep([Vec3(0,r,0),Vec3(0,r-t,0),Vec3(0,r-t,h),Vec3(0,r,h)],Vec3(0,0,0),Vec3(0,0,1),-A/180*pi)  
  
def createRoller(roller_r,roller_w,x,y,z):
        cone=trans(x,y,z)*Cone(Vec3(0,0,0),Vec3(0,roller_w,0),roller_r,roller_r)
        return cone

def createBrackets(num,A,bracket_w,l,w,h,r,center_r):
    temph=h-100
    bracket1=trans(0,bracket_w,0)*scale(l,w,temph)*Cube()+scale(l,w,temph)*Cube()
    bracket1=trans(0,r,0)*bracket1
    cube1=trans(0,w+r,temph-50)*scale(l,bracket_w-w,50)*Cube()
    cube2=trans(0,0,-temph/4)*cube1
    cube3=trans(0,r+w,10)*scale(l,bracket_w-w,50)*Cube()
    link1=cube1+cube2+cube3
    foot1=trans(l/2,w/2+r,-100)*Combine(Cone(Vec3(0,0,50),Vec3(0,0,100),15,15),Cone(Vec3(0,0,0),Vec3(0,0,50),w/2,20).color(0,0,0,1))
    foot1=Combine(foot1,trans(0,bracket_w,0)*foot1)
    brackets=[]
    bracket1=trans(-l/2,0,0)*Combine(bracket1,foot1,link1)
    brackets.append(bracket1)
    
    for i in range(1,num):
        brackets.append(rotz(-A/180*pi/(num-1)*i)*bracket1)
        brackets.append(trans(0,0,10)*createFrame(center_r,100,50,A,True))
    return Combine(brackets)


def createMotor():
    # TODO
    return 

if __name__=="__main__":
    fianl=转弯传送带()
    place(fianl)