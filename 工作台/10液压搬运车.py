from tokenize import Comment
from pyp3d import *

class 液压搬运车(Component):
    def __init__(self):
       Component.__init__(self)
    #    self['整体长度']=Attr(1500,obvious=True) # 似乎没用
       self['额定载重']=Attr("3000kg",obvious=True,group='车架与货叉总成')
       self['货叉长度']=Attr(1500,obvious=True,group='车架与货叉总成')
       self['货叉总宽度']=Attr(700,obvious=True,group='车架与货叉总成')
       self['单个货叉宽度']=Attr(180,obvious=True,group='车架与货叉总成')
       self['货叉内间距']=Attr(self['货叉总宽度']-self['单个货叉宽度']*2,obvious=True,readonly=True,group='车架与货叉总成')
       self['货叉厚度']=Attr(80,obvious=True,group='车架与货叉总成')
       self['货叉尖端斜面长度']=Attr(100,obvious=True,group='车架与货叉总成')
       self['升降比例']=Attr(0.0,obvious=True,group='控制参数')
       self['最低高度']=Attr(100,obvious=True,group='控制参数')
       self['最高高度']=Attr(150,obvious=True,group='控制参数')
       self['油泵壳体高度']=Attr(200,obvious=True,group='液压泵与转向总成')
       self['油泵壳体直径']=Attr(100,obvious=True,group='液压泵与转向总成')
    #    self['油泵活塞行程']=Attr(100,obvious=True) # 似乎没用
       self['转向轮直径']=Attr(200,obvious=True,group='液压泵与转向总成')
       self['转向轮宽度']=Attr(40,obvious=True,group='液压泵与转向总成')
       self['手柄总长度']=Attr(1000,obvious=True,group='操作手柄总成')    
       self['手柄杆直径']=Attr(50,obvious=True,group='操作手柄总成')
       self['握把长度']=Attr(500,obvious=True,group='操作手柄总成')
       self['握把直径']=Attr(40,obvious=True,group='操作手柄总成')
       self['握把角度']=Attr(40,obvious=True,group='操作手柄总成') 
       self['控制拨片长度']=Attr(80,obvious=True,group='操作手柄总成')
       self['承重轮直径']=Attr(100,obvious=True)
       self['转向角度']=Attr(0,obvious=True,group='控制参数')
       self['手柄俯仰角']=Attr(90,obvious=True,group='控制参数')
       self['液压搬运车']=Attr(None,show=True)
       self.replace()
    @export
       
    def replace(self):
        # 1.车架与货叉总成
        H=self['最低高度']+self['升降比例']*(self['最高高度']-self['最低高度'])
        Y=self['货叉总宽度']
        L1=self['货叉长度']
        W=self['单个货叉宽度']
        fork_t=self['货叉厚度']
        L2=self['货叉尖端斜面长度']
        removecube=Sweep(Section(Vec3(L1-L2,0,0),Vec3(L1,0,0),Vec3(L1,0,fork_t)),Line(Vec3(0,0,0),Vec3(0,W,0)))
        SingleFork1=scale(L1,W,fork_t)*Cube()-removecube
        SingleFork2=trans(0,Y-W,0)*SingleFork1
        width=200
        thick=10
        targety=Y-200-thick
        FrontBox=Box(Vec3(0,0,fork_t),Vec3(0,200,400+fork_t),Vec3(1,0,0),Vec3(0,1,0),width,Y,width,Y-200*2)
        TestBox1=Box(Vec3(0,thick,fork_t),Vec3(0,200+thick,400+fork_t-thick),Vec3(1,0,0),Vec3(0,1,0),width-thick,Y-2*thick,width-thick,targety-200-thick)
        FrontBox-=TestBox1
        LinkCube=translate(width/2,thick,fork_t/2)*scale(width/2,Y-2*thick,fork_t/2)*Cube()
        
        # 额定载重铭牌
        nameplate_text = translate(width+1,Y/2-150,H+50)*rotz(pi/2)*rotx(pi/2)* Text(self['额定载重'], 50,50).color(255/255,255/255,255/255,1)
        nameplate_cube = translate(width+1,Y/2-150,H) * scale(-1,300,150) * Cube().color(1,1,1,1)
        车架与货叉总成=translate(0,-Y/2,H)*Combine((SingleFork1+SingleFork2+FrontBox+LinkCube).color(1,60/255,0,1),nameplate_text,nameplate_cube)
        
        # 2.液压泵与转向总成
         #转向轮
        QL_R = self['转向轮直径']/2
        QL_W=self['转向轮宽度']
        qianlun1 =translate(0,-25,QL_R)*rotx(1/2*pi)*createWheel(QL_R,QL_W)
        qianlun2 =translate(0,+25,QL_R)*rotx(-1/2*pi)*createWheel(QL_R,QL_W)
        转向轮 = Combine(qianlun1,qianlun2)
        
        # 转向轴承
        Cone1=translate(0,+25,QL_R)*rotx(1/2*pi)*Cone(Vec3(0,0,0),Vec3(0,0,50),QL_R/4,QL_R/4)
        Cone2=translate(0,0,QL_R)*Cone(Vec3(0,0,0),Vec3(0,0,fork_t+H+400-QL_R-thick),25,25)
        Box1=trans(-QL_R,-(QL_R*2+50)/2,QL_R*2)*scale(QL_R*2,QL_R*2+50,20)*Cube()
        转向轴承=Combine(Cone1,Cone2,Box1)
        
        # 油泵壳体
        Hosing_H=self["油泵壳体高度"]
        Hosing_R=self['油泵壳体直径']/2
        Cone3=translate(0,0,QL_R*2+20)*Cone(Vec3(0,0,0),Vec3(0,0,Hosing_H),Hosing_R,Hosing_R).color(0.1,0.1,0.1,1)
        Box2=trans(-Hosing_R*3,-Hosing_R,QL_R*2+20)*scale(Hosing_R*3,Hosing_R*2,Hosing_H/2)*Cube().color(0.1,0.1,0.1,1)
        油泵壳体=Combine(Cone3,Box2)
        液压泵与转向总成=trans(25,0,0)*Combine(转向轮,转向轴承,油泵壳体)
       
        
        # 3.操作手柄总成
        SB_L=self['手柄总长度']
        SB_R=self['手柄杆直径']/2
        Angle=self['手柄俯仰角']
        手柄=translate(-Hosing_R*2,0,QL_R*2+Hosing_H/4)*Sweep(Section(roty(-pi/2+Angle/180*pi)*scale(SB_R)*Arc()),Line(Vec3(0,0,0),Vec3(-SB_L*cos(Angle/180*pi),0,SB_L*sin(Angle/180*pi))))
        # 握把
        WB_width=self['握把长度'];
        WB_R=self['握把直径']/2
        GripAngle=self['握把角度']/180*pi
        WB_H=WB_width/(2*tan(GripAngle))
        TestFilletPipe1 = FilletPipe([Vec3(0,0,WB_H),Vec3(0,0-WB_width/2,WB_H),Vec3(0,0,0)],[0,50,0],WB_R)
        TestFilletPipe2=mirror_xoz()*TestFilletPipe1
        L=SB_L-WB_H
        TestFilletPipe=trans(-cos(Angle/180*pi)*L,0,L*sin(Angle/180*pi))*translate(-Hosing_R*2,0,QL_R*2+Hosing_H/4)*roty(-pi/2+Angle/180*pi)*Combine(TestFilletPipe1,TestFilletPipe2)
         # 控制拨片
        Ctrl_L=self['控制拨片长度']
        Ctrl=trans(-cos(Angle/180*pi)*(L+WB_H/4*3),0,(L+WB_H/4*3)*sin(Angle/180*pi))*translate(-Hosing_R*2,-SB_R,QL_R*2+Hosing_H/4)*roty(-pi/2+Angle/180*pi)*Sweep(Section(Vec3(0,0,0),Vec3(0,0,-30),Vec3(0,-cos(30/180*pi)*Ctrl_L,-30-sin(30/180*pi)*Ctrl_L)),Line(Vec3(0,0,0),Vec3(10,0,0))).color(0.1,0.1,0.1,1)
        操作手柄总成=trans(25,0,0)*Combine(手柄,TestFilletPipe,Ctrl)
         
        # 4.转向
        Trans_angle=self['转向角度']
        global_trans=rotate(Vec3(0,0,1),Trans_angle/180*pi)
        液压泵与转向总成=trans(25,0,0)*global_trans*trans(-25,0,0)*液压泵与转向总成
        操作手柄总成=trans(25,0,0)*global_trans*trans(-25,0,0)*操作手柄总成
        
        # 5.前端承重轮连杆机构
        # 连杆1
        CZ_D=self['承重轮直径']
        Cube1=trans(0,W/3,H)*scale(L1-L2-2*CZ_D,W/3,fork_t/2)*Cube()
        Cube2=trans(0,Y-W,0)*Cube1
        
        # 承重轮
        CZ_R=CZ_D/2
        CZ=rotx(1/2*pi)*createWheel(CZ_R,CZ_R)
        CZ1 =translate(0,W/2+CZ_R/2,CZ_R)*CZ
        CZ2 =translate(CZ_D,0,0)*CZ1
        CZ3=trans(0,Y-W,0)*Combine(CZ1,CZ2)
        CZ_L=sqrt(CZ_D**2+(self['最高高度']+fork_t/2-CZ_R)**2)
        x=L1-L2-2*CZ_D+CZ_R-CZ_D+sqrt(CZ_L**2-(H+fork_t/2-CZ_R)**2)
        承重轮 = trans(x,0,0)*Combine(CZ1,CZ2,CZ3)
        
        #连杆2
        Link1=trans(x,W/2-+CZ_R/2-4,CZ_R/2)*scale(CZ_D,5,CZ_R)*Cube()
        Link2=trans(0,Y-W+CZ_R+5,0)*Link1
        LinkCone1=Cone(Vec3(L1-L2-2*CZ_D-10,W/2-CZ_R/2-10,H+fork_t/4),Vec3(x+CZ_R,W/2-CZ_R/2-10,CZ_R),10,10)
        LinkCone2=trans(0,Y-W+CZ_R+20,0)*LinkCone1
       
        前端承重轮连杆机构=trans(0,-Y/2,0)*Combine(Cube1,Cube2,承重轮,Link1,Link2,LinkCone1,LinkCone2)
        self['液压搬运车']=Combine(车架与货叉总成,液压泵与转向总成,操作手柄总成,前端承重轮连杆机构)

def createWheel(R,W):
    wheel1 = Sweep(Section(scale(205/234*R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,W/10))).color(238/255,232/255,170/255)
    wheel2 = trans(0,0,W/10)*Sweep(Section(scale(R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,W*0.8))).color(238/255,232/255,170/255)
    wheel3 = trans(0,0,0.9*W)*Sweep(Section(scale(150/240*R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,W/10))).color(238/255,232/255,170/255)
    wheel4 = trans(0,0,0)*Sweep(Section(scale(R)*Arc())-Section(205/234*scale(R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,W)))
    return Combine(wheel1,wheel2,wheel3,wheel4)


if __name__ == "__main__":
    final = 液压搬运车()
    place(final)