from msilib import CreateRecord
from pyp3d import *

class 直线传送带(Component):
    def __init__(self):
       Component.__init__(self)
       # TODO
       self['传送带长度']=Attr(3000,obvious=True,group='承载面')
       self['传送带宽度']=Attr(1000,obvious=True,group='承载面')
       self['倾斜角度']=Attr(0,obvious=True,group='承载面')# TODO
       self['传送带类型']=Attr('皮带+滑板',obvious=True,group='承载面',combo=['皮带+滑板','滚筒阵列'])
       self['框架型材高度']=Attr(200,obvious=True,group='框架')
       self['框架型材厚度']=Attr(30,obvious=True,group='框架')
       self['护栏高度']=Attr(200,obvious=True,group='框架')
       self['护栏厚度']=Attr(20,obvious=True,group='框架')
       self['滚筒直径']=Attr(50,obvious=True,group='滚筒')
       self['滚筒间距']=Attr(20,obvious=True,group='滚筒')
       self['皮带材质']=Attr(0,obvious=True,group='皮带') # 似乎没用到
       self['皮带厚度']=Attr(20,obvious=True,group='皮带')
       self['驱动方式']=Attr(0,obvious=True,group='驱动')# TODO
       self['电机功率']=Attr(1000,obvious=True,group='驱动')# TODO
       self['传送速度']=Attr(1000,obvious=True,group='驱动')# TODO
       self['是否带支架']=Attr(True,obvious=True,group='支架')
       self['支架间距']=Attr(1000,obvious=True,group='支架')
       self['支架离地高度(低端)']=Attr(1000,obvious=True,group='支架')
       self['支架型材尺寸']=Attr('100*100',obvious=True,group='支架',combo=['100*100','100*200','100*300'])
       self['运行状态']=Attr(0,obvious=True,group='运行')# TODO
       self['直线传送带']=Attr(None,show=True)
       self.replace()
    @export
    def replace(self):
       # 参数
       L=self['传送带长度']
       W=self['传送带宽度']
       angle=self['倾斜角度']
       
       # 1.框架总成
       # 框架
       frame_h=self['框架型材高度']
       frame_t=self['框架型材厚度']
       frame_l=L
       frame1=scale(frame_l,frame_t,frame_h)*Cube().color(0.5,0.5,1,1)
       frame2=trans(0,W+frame_t,0)*frame1
       frame=Combine(frame1,frame2)
       # 护栏
       guard_h=self['护栏高度']
       guard_t=self['护栏厚度']
       guard_l=L
       guard1=scale(guard_l,guard_t,guard_h)*Cube()
       guard2=trans(0,W+frame_t*2-guard_t,0)*guard1
       guard=trans(0,0,frame_h+10)*Combine(guard1,guard2)
       
       # 框架与护栏的连接
       Link1=Box(Vec3(0,0,0),Vec3(0,-50,-1/4*guard_h),Vec3(1,0,0),Vec3(0,0,-1),50,0.5*(guard_h+frame_h),50,0.25*(guard_h+frame_h))
       Link2= mirror(trans(0,0,0) ,'XZ') * Link1
       Link1=trans(L/2,0,frame_h+10+guard_h/2)*Link1
       Link2=trans(L/2,W+2*frame_t,frame_h+10+guard_h/2)*Link2
       Link=Combine(Link1,Link2)
       框架总成=Combine(frame,guard,Link)
       #2. 承载面 
       # 皮带与滑板 : 如果传送带类型为皮带，则此部件为环形皮带及支撑皮带的底板。
       if self['传送带类型']=='皮带+滑板':
           # 滑板
           belt_t=self['皮带厚度']
           board_w=W
           board_l=L-frame_h
           board_h=(frame_h-2*belt_t)/2
           board=trans(frame_h/2,frame_t,belt_t+board_h)*scale(board_l,board_w,board_h)*Cube()
           # 皮带
           r1=frame_h/2
           Section1=Section(Vec3(0,0,0),Vec3(L,0,0),trans(L,r1,0)*rotz(-0.5*pi)*scale(r1)*Arc(pi),Vec3(0,r1*2,0),trans(0,r1,0)*rotz(0.5*pi)*scale(r1)*Arc(pi))
           r2=frame_h/2-belt_t
           Section2=trans(0,belt_t,0)*Section(Vec3(0,0,0),Vec3(L,0,0),trans(L,r2,0)*rotz(-0.5*pi)*scale(r2)*Arc(pi),Vec3(0,2*r2,0),trans(0,r2,0)*rotz(0.5*pi)*scale(r2)*Arc(pi))
           belt=trans(0,frame_t,frame_h)*rotx(-pi*0.5)*Sweep(Section1-Section2,Line(Vec3(0,0,0),Vec3(0,0,W))).color(0.2,0.2,0.2,1)
           承载面=Combine(board,belt)
           
       # 滚筒阵列 : 如果传送带类型为滚筒，则此部件由一系列平行排列的滚筒组成。
       else:
           roller_d=self['滚筒直径']
           roller_r=roller_d/2
           gap=self['滚筒间距']
           roller_num=(int)(L/(roller_d+gap))
           cone1=createRoller(roller_r,W,roller_r,frame_t,frame_h-roller_r)
           cones = Array(cone1)
           for i in linspace(Vec3(0,0,0),Vec3(L-roller_d,0,0),roller_num): 
               cones.append(translate(i)) 
           # 链条
           
           承载面=Combine(cones)
      
       
       # 3.头/尾滚筒总成
       Cone1=trans(0,frame_t,frame_h/2)*Cone(Vec3(0,0,),Vec3(0,W,0),frame_h*3/8,frame_h*3/8)
       Cone2=trans(L,0,0)*Cone1
       头尾滚筒总成=Combine(Cone1,Cone2).color(0.1,0.2,0.3,1)
       
       # 4.支撑腿总成  仅在是否带支架为True时生成。通常为H型结构，可调节高度。
       if self['是否带支架']:
            # 获取尺寸字符串
           size_str = self['支架型材尺寸']  # '100*100'
           length,width = size_str.split('*')
           width_num = int(width)
           length_num = int(length)
           bracket_d=self['支架间距']
           bracket_h=self['支架离地高度(低端)']
           bracket_num=int(floor(L /(bracket_d+length_num) ) + 1)
           bracket_w=W+2*frame_t-width_num
           brackets=createBrackets(bracket_num,bracket_d,bracket_w,length_num,width_num,bracket_h)
           templ=L-bracket_num*length_num-(bracket_num-1)*bracket_d
           brackets=trans(templ/2,0,-bracket_h+100)*brackets
           支撑架=Combine(brackets)
           # TODO：倾斜角度的处理
       # TODO：5.驱动单元 : 包括电机和减速器，根据驱动方式安装在头部或中部。
       驱动单元=Cube()
       # TODO：倾斜角度
       框架总成=roty(-angle/180*pi)*框架总成
       承载面=roty(-angle/180*pi)*承载面
       头尾滚筒总成=roty(-angle/180*pi)*头尾滚筒总成
       
       self['直线传送带']=Combine(框架总成,承载面,头尾滚筒总成,驱动单元)
       if self['是否带支架']:
           self['直线传送带']=Combine(self['直线传送带'],支撑架)
    
def createRoller(roller_r,roller_w,x,y,z):
        cone=trans(x,y,z)*Cone(Vec3(0,0,0),Vec3(0,roller_w,0),roller_r,roller_r)
        return cone
def createBrackets(num,bracket_d,bracket_w,l,w,h):
        temph=h-100
        bracket1=trans(0,bracket_w,0)*scale(l,w,temph)*Cube()+scale(l,w,temph)*Cube()
        cube1=trans(0,w,temph-50)*scale(l,bracket_w-w,50)*Cube()
        cube2=trans(0,0,-temph/4)*cube1
        cube3=trans(0,w,10)*scale(l,bracket_w-w,50)*Cube()
        link1=cube1+cube2+cube3
        foot1=trans(l/2,w/2,-100)*Combine(Cone(Vec3(0,0,50),Vec3(0,0,100),15,15),Cone(Vec3(0,0,0),Vec3(0,0,50),w/2,20).color(0,0,0,1))
        foot1=Combine(foot1,trans(0,bracket_w,0)*foot1)
        brackets=[]
        links=[]
        foots=[]
        boxs=[]
        links.append(link1)
        brackets.append(bracket1)
        foots.append(foot1)
        for i in range(1, num):  # 从1开始，因为第一个支架已经添加了
            brackets.append(trans(i*bracket_d,0,0)*bracket1)
            links.append(trans(i*bracket_d,0,0)*link1)
            foots.append(trans(i*bracket_d,0,0)*foot1)
            boxs.append(trans((i-1)*bracket_d,0,0)*trans(l,bracket_w/2,10)*scale(bracket_d-l,100,50)*Cube())
            
        return Combine(brackets,links,foots,boxs)
       
        
if __name__ == "__main__":
    final=直线传送带()
    place(final)