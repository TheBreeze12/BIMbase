from nt import link
from poplib import CR
from tokenize import group
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
        L1=self['货叉长度']
        W1=self['单个货叉宽度']
        H1=self['货叉厚度']
        L2=self['货叉尖端斜面长度']
        removecube=Sweep(Section(Vec3(L1-L2,0,0),Vec3(L1,0,0),Vec3(L1,0,H1)),Line(Vec3(0,0,0),Vec3(0,W1,0)))
        basey=self['货叉总宽度']
        SingleFork1=scale(L1,W1,H1)*Cube()-removecube
        SingleFork2=trans(0,basey-W1,0)*SingleFork1
        width=200
        thick=10
        targety=basey-200-thick
        TestBox=Box(Vec3(0,0,H1),Vec3(0,200,400+H1),Vec3(1,0,0),Vec3(0,1,0),width,basey,width,basey-200*2)
        TestBox1=Box(Vec3(0,thick,H1),Vec3(0,200+thick,400+H1-thick),Vec3(1,0,0),Vec3(0,1,0),width-thick,basey-2*thick,width-thick,targety-200-thick)
        TestBox-=TestBox1
        LinkCube=translate(width/2,thick,H1/2)*scale(width/2,basey-2*thick,H1/2)*Cube()
        
        # 额定载重铭牌
        texttest = translate(width+1,basey/2-150,H+50)*rotz(pi/2)*rotx(pi/2)* Text(self['额定载重'], 50,50).color(255/255,255/255,255/255,1)
        cubetest = translate(width+1,basey/2-150,H) * scale(-1,300,150) * Cube().color(1,1,1,1)
        model1=translate(0,0,H)*Combine((SingleFork1+SingleFork2+TestBox+LinkCube).color(1,60/255,0,1),texttest,cubetest)
        
        # 2.液压泵与转向总成
        Trans_angle=self['转向角度']
        global_trans=rotate(Vec3(0,0,1),Trans_angle/180*pi)
        
         #转向轮
        QL_R = self['转向轮直径']/2
        QL_W=self['转向轮宽度']
        qianlun_1 = Sweep(Section(scale(205/234*QL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,QL_W/10))).color(238/255,232/255,170/255)
        qianlun_2 = trans(0,0,QL_W/10)*Sweep(Section(scale(QL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,QL_W))).color(238/255,232/255,170/255)
        qianlun_3 = trans(0,0,QL_W/10+QL_W)*Sweep(Section(scale(150/240*QL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,QL_W/10))).color(238/255,232/255,170/255)
        qianlun_4 = trans(0,0,QL_W/10)*Sweep(Section(scale(QL_R)*Arc())-Section(205/234*scale(QL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,QL_W+QL_W/5)))
        qianlun1 =translate(0,basey/2-25,QL_R)*rotx(1/2*pi)*Combine(qianlun_1,qianlun_2,qianlun_3,qianlun_4)
        qianlun2 =translate(0,basey/2+25,QL_R)*rotx(-1/2*pi)*Combine(qianlun_1,qianlun_2,qianlun_3,qianlun_4)
        转向轮 = Combine(qianlun1,qianlun2)
        
        # 转向轴承
        Cone1=translate(0,basey/2+25,QL_R)*rotx(1/2*pi)*Cone(Vec3(0,0,0),Vec3(0,0,50),QL_R/4,QL_R/4)
        Cone2=translate(0,basey/2,QL_R)*Cone(Vec3(0,0,0),Vec3(0,0,H1+H+400-QL_R-thick),25,25)
        Box1=trans(-QL_R,basey/2-(QL_R*2+50)/2,QL_R*2)*scale(QL_R*2,QL_R*2+50,20)*Cube()
        转向轴承=Combine(Cone1,Cone2,Box1)
        
        # 油泵壳体
        Hosing_H=self["油泵壳体高度"]
        Hosing_R=self['油泵壳体直径']/2
        Cone3=translate(0,basey/2,QL_R*2+20)*Cone(Vec3(0,0,0),Vec3(0,0,Hosing_H),Hosing_R,Hosing_R).color(0.1,0.1,0.1,1)
        Box2=trans(-Hosing_R*3,basey/2-Hosing_R,QL_R*2+20)*scale(Hosing_R*3,Hosing_R*2,Hosing_H/2)*Cube().color(0.1,0.1,0.1,1)
        油泵壳体=Combine(Cone3,Box2)
        model2=trans(25,0,0)*Combine(转向轮,转向轴承,油泵壳体)
        model2=trans(25,basey/2,0)*global_trans*trans(-25,-basey/2,0)*model2
        
        # 3.操作手柄总成
        SB_L=self['手柄总长度']
        SB_R=self['手柄杆直径']/2
        Angle=self['手柄俯仰角']
        手柄=translate(-Hosing_R*2,basey/2,QL_R*2+Hosing_H/4)*Sweep(Section(roty(-pi/2+Angle/180*pi)*scale(SB_R)*Arc()),Line(Vec3(0,0,0),Vec3(-SB_L*cos(Angle/180*pi),0,SB_L*sin(Angle/180*pi))))
        # 握把
        WB_width=self['握把长度'];
        WB_R=self['握把直径']/2
        GripAngle=self['握把角度']/180*pi
        # WB_width/(2*x)=tan(angle) 
        WB_H=WB_width/(2*tan(GripAngle))
        TestFilletPipe1 = FilletPipe([Vec3(0,basey/2,WB_H),Vec3(0,basey/2-WB_width/2,WB_H),Vec3(0,basey/2,0)],# 轨迹拐点
        [0,50,0],WB_R # 管半径。弯折半径必须全部大于管半径。第一个和最后一个点除外。
        )
        TestFilletPipe2=trans(0,basey,0)*mirror_xoz()*TestFilletPipe1
        L=SB_L-WB_H
        TestFilletPipe=trans(-cos(Angle/180*pi)*L,0,L*sin(Angle/180*pi))*translate(-Hosing_R*2,0,QL_R*2+Hosing_H/4)*roty(-pi/2+Angle/180*pi)*Combine(TestFilletPipe1,TestFilletPipe2)
         # 控制拨片
        Ctrl_L=self['控制拨片长度']
        Ctrl=trans(-cos(Angle/180*pi)*(L+WB_H/4*3),0,(L+WB_H/4*3)*sin(Angle/180*pi))*translate(-Hosing_R*2,basey/2-SB_R,QL_R*2+Hosing_H/4)*roty(-pi/2+Angle/180*pi)*Sweep(Section(Vec3(0,0,0),Vec3(0,0,-30),Vec3(0,-cos(30/180*pi)*Ctrl_L,-30-sin(30/180*pi)*Ctrl_L)),Line(Vec3(0,0,0),Vec3(10,0,0))).color(0.1,0.1,0.1,1)
        model3=trans(25,0,0)*Combine(手柄,TestFilletPipe,Ctrl)
        model3=trans(25,basey/2,0)*global_trans*trans(-25,-basey/2,0)*model3
        # 4.前端承重轮连杆机构
        # 连杆1
        CZ_D=self['承重轮直径']
        Cube1=trans(0,W1/3,H)*scale(L1-L2-2*CZ_D,W1/3,H1/2)*Cube()
        Cube2=trans(0,basey-W1,0)*Cube1
        
        # 承重轮
        CZ_R=CZ_D/2
        CZ_1 = Sweep(Section(scale(205/234*CZ_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,CZ_R/10))).color(238/255,232/255,170/255)
        CZ_2 = trans(0,0,CZ_R/10)*Sweep(Section(scale(CZ_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,CZ_R/10*8))).color(238/255,232/255,170/255)
        CZ_3 = trans(0,0,CZ_R/10*9)*Sweep(Section(scale(150/240*CZ_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,CZ_R/10))).color(238/255,232/255,170/255)
        CZ_4 = trans(0,0,0)*Sweep(Section(scale(CZ_R)*Arc())-Section(205/234*scale(CZ_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,CZ_R)))
        CZ=rotx(1/2*pi)*Combine(CZ_1,CZ_2,CZ_3,CZ_4)
        CZ1 =translate(0,W1/2+CZ_R/2,CZ_R)*CZ
        CZ2 =translate(CZ_D,0,0)*CZ1
        CZ3=trans(0,basey-W1,0)*Combine(CZ1,CZ2)
        CZ_L=sqrt(CZ_D**2+(self['最高高度']+H1/2-CZ_R)**2)
        x=L1-L2-2*CZ_D+CZ_R-CZ_D+sqrt(CZ_L**2-(H+H1/2-CZ_R)**2)
        承重轮 = trans(x,0,0)*Combine(CZ1,CZ2,CZ3)
        
        #连杆2
        Link1=trans(x,W1/2-+CZ_R/2-4,CZ_R/2)*scale(CZ_D,5,CZ_R)*Cube()
        Link2=trans(0,basey-W1+CZ_R+5,0)*Link1
        LinkCone1=Cone(Vec3(L1-L2-2*CZ_D-10,W1/2-CZ_R/2-10,H+H1/4),Vec3(x+CZ_R,W1/2-CZ_R/2-10,CZ_R),10,10)
        LinkCone2=trans(0,basey-W1+CZ_R+20,0)*LinkCone1
       
        model4=Combine(Cube1,Cube2,承重轮,Link1,Link2,LinkCone1,LinkCone2)
        self['液压搬运车']=Combine(model1,model2,model3,model4)
if __name__ == "__main__":
    app = 液压搬运车()
    place(app)