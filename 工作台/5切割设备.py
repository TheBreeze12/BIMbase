import traceback
from pyp3d import *

class 切割设备(Component):
    def __init__(self):
        Component.__init__(self)
        # 左导轨横梁
        self['左导轨长度']=Attr(5000,obvious=True,group="左导轨")
        self['左导轨横梁宽度']=Attr(150,obvious=True,group="左导轨")
        self['左导轨横梁高度']=Attr(20,obvious=True,group="左导轨")
        # 左导轨轨道
        self['左导轨宽度']=Attr(10,obvious=True,group="左导轨")
        self['左导轨高度']=Attr(100,obvious=True,group="左导轨")
        # 左导轨支撑腿
        self['左支撑腿数量']=Attr(5,obvious=True,group="左导轨")
        self['左支撑腿长度']=Attr(150,obvious=True,group="左导轨")
        self['左支撑腿宽度']=Attr(150,obvious=True,group="左导轨")
        self['左支撑腿高度']=Attr(500,obvious=True,group="左导轨")
        self['地脚座长度']=Attr(200,obvious=True,group="地脚座")
        self['地脚座宽度']=Attr(200,obvious=True,group="地脚座")
        self['地脚座高度']=Attr(10,obvious=True,group="地脚座")
        # 右导轨横梁
        self['右导轨横梁长度']=Attr(5000,obvious=True,group="右导轨")
        self['右导轨横梁宽度']=Attr(150,obvious=True,group="右导轨")
        self['右导轨横梁高度']=Attr(150,obvious=True,group="左导轨")
        # 右导轨支撑腿
        self['右支撑腿数量']=Attr(4,obvious=True,group="右导轨")
        self['右支撑腿长度']=Attr(150,obvious=True,group="右导轨")
        self['右支撑腿宽度']=Attr(150,obvious=True,group="右导轨")
        self['右支撑腿高度']=Attr(500,obvious=True,group="右导轨")
        # 电缆
        self['电缆拖链节数']=Attr(30,obvious=True,group='电缆拖链')
        self['每一节长度']=Attr(150,obvious=True,group='电缆拖链')
        self['每一节宽度']=Attr(50,obvious=True,group='电缆拖链')
        self['每一节高度']=Attr(50,obvious=True,group='电缆拖链')
        # 滑架相关
        self['滑动比例(y方向)']=Attr(0.5,obvious=True,group='移动')
        self['滑动比例(x方向)']=Attr(0.5,obvious=True,group='移动')
        self['滑动比例(z方向)']=Attr(0.5,obvious=True,group='移动')
        self['导轨滑块长度']=Attr(200,obvious=True,group='导轨滑块')
        self['导轨滑块宽度']=Attr(100,obvious=True,group='导轨滑块')
        self['导轨滑块高度']=Attr(70,obvious=True,group='导轨滑块')
        self['主动滑架长度']=Attr(1200,obvious=True,group='滑架')
        self['主动滑架宽度']=Attr(300,obvious=True,group='滑架')
        self['主动滑架高度']=Attr(300,obvious=True,group='滑架')
        self['从动滑架长度']=Attr(200,obvious=True,group='滑架')
        self['从动滑架宽度']=Attr(20,obvious=True,group='滑架')
        self['从动滑架高度']=Attr(0,obvious=True,group='滑架',readonly=True)
        self['横梁长度']=Attr(3000,obvious=True,group='横梁')
        self['横梁宽度']=Attr(0,obvious=True,group='横梁',readonly=True)
        self['横梁高度']=Attr(150,obvious=True,group='横梁')
        # 小车相关
        self['小车轨道长度']=Attr(0,obvious=True,group='小车',readonly=True)
        self['小车轨道宽度']=Attr(50,obvious=True,group='小车')
        self['小车轨道高度']=Attr(20,obvious=True,group='小车')
        self['小车驱动电机直径']=Attr(100,obvious=True,group='小车')
        self['小车驱动电机高度']=Attr(200,obvious=True,group='小车')
        self['小车减速器长度']=Attr(100,obvious=True,group='小车')
        self['小车减速器宽度']=Attr(100,obvious=True,group='小车')
        self['小车减速器高度']=Attr(200,obvious=True,group='小车')
        self['小车联轴器长度']=Attr(120,obvious=True,group='小车')
        self['小车联轴器宽度']=Attr(120,obvious=True,group='小车')
        self['小车联轴器高度']=Attr(50,obvious=True,group='小车')
        # 横梁电机相关
        self['横梁驱动电机直径']=Attr(100,obvious=True,group='横梁电机')
        self['横梁驱动电机高度']=Attr(200,obvious=True,group='横梁电机')
        self['横梁减速器长度']=Attr(100,obvious=True,group='横梁电机')
        self['横梁减速器宽度']=Attr(100,obvious=True,group='横梁电机')
        self['横梁减速器高度']=Attr(200,obvious=True,group='横梁电机')
        self['横梁联轴器长度']=Attr(120,obvious=True,group='横梁电机')
        self['横梁联轴器宽度']=Attr(120,obvious=True,group='横梁电机')
        self['横梁联轴器高度']=Attr(50,obvious=True,group='横梁电机')
        
        # z轴相关
        self['三角形边长']=Attr(150,obvious=True,group='Z轴安装')
        self['三角形厚度']=Attr(50,obvious=True,group='Z轴安装')
        self['Z轴升降装置长度']=Attr(300,obvious=True,group='Z轴安装')
        self['Z轴升降装置宽度']=Attr(200,obvious=True,group='Z轴安装')
        self['Z轴升降装置高度']=Attr(1000,obvious=True,group='Z轴安装')
        
        # 防撞装置
        self['凸起部分直径']=Attr(100,obvious=True,group='防撞装置')
        self['凹陷部分直径']=Attr(70,obvious=True,group='防撞装置')
        self['厚度']=Attr(15,obvious=True,group='防撞装置')
        self['圈数']=Attr(5,obvious=True,group='防撞装置')
        
        # 割炬座
        self['直线部分长度']=Attr(200,obvious=True,group='割炬座')
        self['弧线部分半径（连防撞装置）']=Attr(50,obvious=True,group='割炬座')
        self['弧线部分半径（连切割头）']=Attr(40,obvious=True,group='割炬座')
        # 切割头
        self['割炬长度']=Attr(400,obvious=True,group='切割头')
        self['割炬直径']=Attr(60,obvious=True,group='切割头')
        self['炬枪长度']=Attr(40,obvious=True,group='切割头')
        self['炬枪底面直径']=Attr(40,obvious=True,group='切割头')


        self['切割设备']=Attr(None,show=True)
        self.replace()
    @export
    
    def replace(self):
        # 变量
        ratio_y=self['滑动比例(y方向)']
        ratio_x=self['滑动比例(x方向)']
        ratio_z=self['滑动比例(z方向)']
        left_L= self['左导轨长度']
        left_num=self['左支撑腿数量']
        left_leg_L=self['左支撑腿长度']
        lr_d=self['横梁长度']-0.5*self['右导轨横梁宽度']-0.5*self['主动滑架宽度']
        linkh=100
        basel=self['地脚座长度']
        basew=self['地脚座宽度']
        baseh=self['地脚座高度']
        left_leg_W=self['左支撑腿宽度']
        left_leg_H=self['左支撑腿高度']
        left_beam_W= self['左导轨横梁宽度']
        left_beam_H= self['左导轨横梁高度']
        left_rail_W=self['左导轨宽度']
        left_rail_H=self['左导轨高度']
        
        right_L= self['右导轨横梁长度']
        right_num=self['右支撑腿数量']
        right_leg_L=self['右支撑腿长度']
        right_leg_H=self['右支撑腿高度']
        right_leg_W=self['右支撑腿宽度']
        right_beam_W= self['右导轨横梁宽度']
        right_beam_H= self['右导轨横梁高度']
        
        slider_l=self['导轨滑块长度']
        slider_w=self['导轨滑块宽度']
        slider_h=self['导轨滑块高度']
        a_carriage_l=self['主动滑架长度']
        a_carriage_w=self['主动滑架宽度']
        a_carriage_h=self['主动滑架高度']
        beam_motor_d=self['横梁驱动电机直径']
        beam_motor_h=self['横梁驱动电机高度']
        beam_reducer_l=self['横梁减速器长度']
        beam_reducer_w=self['横梁减速器宽度']
        beam_reducer_h=self['横梁减速器高度']
        beam_coupling_l=self['横梁联轴器长度']
        beam_coupling_w=self['横梁联轴器宽度']
        beam_coupling_h=self['横梁联轴器高度']
        d_carriage_l=self['从动滑架长度']
        d_carriage_w=self['从动滑架宽度']
        beam_L= self['横梁长度']
        beam_W= d_carriage_l
        self['横梁宽度']=beam_W
        beam_H=self['横梁高度']
        cartrack_l=beam_L
        self['小车轨道长度']=cartrack_l
        cartrack_w=self['小车轨道宽度']
        cartrack_h=self['小车轨道高度']
        motor_d=self['小车驱动电机直径']
        motor_h=self['小车驱动电机高度']
        reducer_l=self['小车减速器长度']
        reducer_w=self['小车减速器宽度']
        reducer_h=self['小车减速器高度']
        coupling_l=self['小车联轴器长度']
        coupling_w=self['小车联轴器宽度']
        coupling_h=self['小车联轴器高度']
        
        triangle_l=self['三角形边长']
        triangle_h=self['三角形厚度']
        z_lift_l=self['Z轴升降装置长度']
        z_lift_w=self['Z轴升降装置宽度']   
        z_lift_h=self['Z轴升降装置高度']
        
        bump_d=self['凸起部分直径']
        bump_d2=self['凹陷部分直径']
        bump_h=self['厚度']
        bump_num=self['圈数']
        bump_r=bump_d/2
        bump_r2=bump_d2/2
       
        gashot_l=self['直线部分长度']
        gashot_r=self['弧线部分半径（连防撞装置）']
        gashot_r2=self['弧线部分半径（连切割头）']
        
        torch_l=self['割炬长度']
        torch_d=self['割炬直径']
        gun_l=self['炬枪长度']
        gun_d=self['炬枪底面直径']

        # 1.左导轨相关部分
        # 地脚座
        base=scale(basel,basew,baseh)*Cube()
        bases=Array(base)
        for i in linspace(Vec3(0,0,0),Vec3(0,left_L,0),left_num):  # 生成11个点
            bases.append(translate(i))
        bases=trans(-(basel)/2,-0.5*basew,0)*bases
        # 支撑腿
        transZ=baseh
        link1=trans(0.5*left_leg_L,0.5*left_leg_W,transZ+left_leg_H)*createLink(left_leg_L,left_leg_W,linkh)
        left_leg=trans(0,0,transZ)*scale(left_leg_L,left_leg_W,left_leg_H)*Cube()
        left_leg=Combine(left_leg,link1)
        left_legs = Array(left_leg)
        for i in linspace(Vec3(0,0,0),Vec3(0,left_L,0),left_num):  # 生成11个点
            left_legs.append(translate(i))
        left_legs=trans(-0.5*left_leg_L,-0.5*left_leg_W,0)*left_legs 
        # 横梁
        transZ+=left_leg_H+linkh
        left_beam=trans(-left_beam_W/2,0,transZ)*scale(left_beam_W,left_L,left_beam_H)*Cube()
        # 导轨
        transZ+=left_beam_H
        left_rail=trans(-0.5*left_rail_W,0,transZ)*scale(left_rail_W,left_L,left_rail_H)*Cube()
        # 挡板
        barrier=Combine(scale(0.5*left_beam_W,15,left_rail_H*1.6)*Cube(),\
            Cone(Vec3(left_beam_W/4,15,left_rail_H*1.25),Vec3(left_beam_W/4,15+30,left_rail_H*1.25),left_rail_H/4,left_rail_H/4))
        barrier1=trans(-0.25*left_beam_W,-45,transZ-left_beam_H)*barrier
        barrier2=trans(0.25*left_beam_W,left_L+45,transZ-left_beam_H)*rotz(pi)*barrier
        barriers=Combine(barrier1,barrier2)
        LeftPart=Combine(bases,left_beam,left_legs,left_rail,barriers)
        
         # 2.右导轨相关部分
        # 地脚座
        bases_r=Array(base)
        for i in linspace(Vec3(0,0,0),Vec3(0,right_L-right_leg_W,0),right_num):  # 生成11个点
            bases_r.append(translate(i))
        bases_r=trans(-(basel)/2,-0.5*(basew-right_leg_W),0)*bases_r
        # 支撑腿
        transZ=baseh
        right_leg=trans(0,0,transZ)*scale(right_leg_L,right_leg_W,right_leg_H)*Cube()
        right_legs = Array(right_leg)
        for i in linspace(Vec3(0,0,0),Vec3(0,right_L-right_leg_W,0),right_num):  # 生成11个点
            right_legs.append(translate(i))
        right_legs=trans(-0.5*right_leg_L,0,0)*right_legs 
        # 横梁
        transZ2=transZ
        transZ+=left_leg_H
        transZ2+=right_leg_H
        right_beam=scale(right_beam_W,right_L,right_beam_H)*Cube()
        right_beam1=scale(right_beam_W-10,right_L,right_beam_H-10)*Cube()
        right_beam-=trans(5,0,5)*right_beam1
        right_beam=trans(-right_beam_W/2,0,transZ2)*right_beam
        RightPart=trans(lr_d,0,0)*Combine(right_legs,right_beam,bases_r)
        
        # 3.电缆拖链
        l= self['每一节长度']
        w= self['每一节宽度']
        h= self['每一节高度']
        d=beam_H+motor_h-2*h
        num=self['电缆拖链节数']
        Cable=trans(ratio_x*beam_L+0.5*motor_d,ratio_y*left_L,\
            d+h+transZ+linkh+left_beam_H+left_rail_H+0.5*slider_h+a_carriage_h)*\
            createCable(l,w,h,d,num)
        
        # 4.滑架相关部分
        # 导轨滑块
        slider=scale(slider_w,slider_l,slider_h)*Cube()-\
            trans((slider_w-(left_rail_W+10))/2,0,0)*scale(left_rail_W+10,slider_l,slider_h/2)*Cube()
        transZ+=linkh+left_beam_H+left_rail_H
        slider=trans(-slider_w/2,ratio_y*left_L,transZ-0.5*slider_h)*Combine(slider).color(0.2,0.2,0.2,1)
        # 主动滑架
        temp1=max(beam_motor_d,beam_reducer_w,beam_coupling_w)
        temp2=max(beam_reducer_l,beam_motor_d,beam_coupling_l)
        removecube=scale(temp1,temp2,a_carriage_h)*Cube()
        a_carriage=trans(-0.5*a_carriage_w,ratio_y*left_L-0.5*a_carriage_l+slider_l/2,transZ+0.5*slider_h)*Combine(scale(a_carriage_w,a_carriage_l,a_carriage_h)*Cube()-trans(0,0.5*(a_carriage_l-temp2),0)*removecube).color(194/255, 124/255, 2/255,1)
        # 横梁电机相关
        beam_motor=trans(-beam_motor_d/2,ratio_y*left_L+0.5*slider_l,transZ-left_rail_H)*\
            rotz(-0.5*pi)*createDrivemotor(20,beam_motor_d,beam_motor_h,beam_reducer_l,beam_reducer_w,beam_reducer_h,beam_coupling_l,beam_coupling_w,beam_coupling_h)
        # 从动滑架
        d_carriage_h=transZ+0.5*slider_h+a_carriage_h-right_beam_H-right_leg_H+20+ beam_H-baseh
        d_carriage=scale(d_carriage_w,d_carriage_l,d_carriage_h)*Cube().color(194/255, 124/255, 2/255,1)
        cone=trans(0,0.5*d_carriage_l,50)*Combine(Cone(Vec3(0,0,0),Vec3(-20,0,0),30,30),Cone(Vec3(d_carriage_w+20,0,0),Vec3(-30,0,0),10,10))
        d_carriage=trans(lr_d+.5*right_beam_W,ratio_y*left_L-d_carriage_l,right_beam_H+right_leg_H-20+baseh)*Combine(d_carriage,cone)
        # 横梁
        transZ+=0.5*slider_h+a_carriage_h
        beam1=trans(-0.5*a_carriage_w,ratio_y*left_L-beam_W,transZ)*scale(beam_L,beam_W,beam_H)*Cube().color(194/255, 124/255, 2/255,1)
        beam2=trans(a_carriage_w/2,ratio_y*left_L,transZ-a_carriage_h/3)*\
            Box(Vec3(0,0,0),Vec3(beam_L-a_carriage_w,0,0),Vec3(0,0,1),Vec3(0,1,0),a_carriage_h/3,0.5*a_carriage_l,a_carriage_h/3,d_carriage_l)\
                .color(194/255, 124/255, 2/255,1)
        beam=Combine(beam1,beam2)
        LinkPart=Combine(slider,a_carriage,d_carriage,beam,beam_motor)
        
        # 5.小车相关
        # 小车轨道
        cartrack=trans(-0.5*a_carriage_w,ratio_y*left_L-beam_W-0.5*cartrack_w,transZ+beam_H)*scale(cartrack_l,cartrack_w,cartrack_h)*Cube()
        # 驱动电机
        motor=trans(ratio_x*beam_L,motor_d/2+ratio_y*left_L-beam_W+0.5*cartrack_w,transZ+beam_H)*\
            rotz(pi)*createDrivemotor(cartrack_h,motor_d,motor_h,reducer_l,reducer_w,reducer_h,coupling_l,coupling_w,coupling_h)
        Trolley=Combine(cartrack,motor)
       
       # 6.z轴相关
        # 三角形
        tri1=trans(ratio_x*beam_L+motor_d/2+20,ratio_y*left_L-beam_W-0.5*cartrack_w,transZ+beam_H+4*cartrack_h+20)*\
                Sweep(Section(Vec3(0,triangle_l,0),Vec3(0,0,0),Vec3(0,0,triangle_l)),\
                    Line(Vec3(0,0,0),Vec3(triangle_h,0,0)))
        tri2=trans(-motor_d-20-70,0,0)*tri1
        # 升降装置
        z_lift=scale(z_lift_l,z_lift_w,z_lift_h)*Cube().color(0.3,0.3,0.3,1)
        remove1=Sweep(Section(Vec3(0,0,0),Vec3(20,0,0),Vec3(20,20,0)),Line(Vec3(0,0,0),Vec3(0,0,z_lift_h)))
        remove2=Sweep(Section(Vec3(20,0,0),Vec3(0,0,0),Vec3(0,20,0)),Line(Vec3(0,0,0),Vec3(0,0,z_lift_h)))
        z_lift=Combine(z_lift-remove2-trans(z_lift_l-20,0,0)*remove1)
        z_lift=trans(ratio_x*beam_L-0.5*z_lift_l,ratio_y*left_L-beam_W-0.5*cartrack_w-z_lift_w,\
            transZ+beam_H-0.3*z_lift_h)*z_lift
        hh=z_lift_h*0.6
        Section1=trans(-z_lift_l*0.5,0,-0.5*hh)*Section(Vec3(0,0,0),Vec3(z_lift_l,0,0),Vec3(z_lift_l,0,hh),Vec3(0,0,hh))
        Section2=Section(Vec3(0.4*z_lift_l,0,0.25*hh),trans(0,0,0.25*hh)*rotx(0.5*pi)*scale(0.4*z_lift_l)*Arc(pi),\
            Vec3(-0.4*z_lift_l,0,-0.25*hh),trans(0,0,-0.25*hh)*rotx(0.5*pi)*scale(0.4*z_lift_l)*Arc(-pi)\
                ,Vec3(z_lift_l*.4,0,-hh*0.25))
        z_lift_up=trans(ratio_x*beam_L,ratio_y*left_L-beam_W-0.5*cartrack_w-20,\
            transZ+beam_H+0.7*z_lift_h+0.5*hh)*Sweep(Section1-Section2,Line(Vec3(0,0,0),Vec3(0,20,0)))
        logo =trans(ratio_x*beam_L-0.5*100,ratio_y*left_L-beam_W-0.5*cartrack_w-z_lift_w,\
            transZ+beam_H+0.2*z_lift_h)*rotx(0.5*pi)*createLogo(size=100, thickness=3, relief_height=2)
        Zabout=Combine(tri1,tri2,z_lift,z_lift_up,logo)
        
        # 7.防撞装置
        cone1=Cone(Vec3(0,0,0),Vec3(0,0,bump_h),bump_r,bump_r)
        cone2=Cone(Vec3(0,0,bump_h),Vec3(0,0,bump_h/2*3),bump_r2,bump_r2)
        cone=Combine(cone1,cone2)
        Avoidance=[]
        for i in range(bump_num):
            Avoidance.append(trans(0,0,i*bump_h/2*3)*cone)
        Avoidance=trans(ratio_x*beam_L,ratio_y*left_L-beam_W-0.5*cartrack_w-z_lift_w*0.5,\
            transZ+beam_H-0.3*z_lift_h-bump_num*bump_h/2*3)*Avoidance
        
        # 8.割炬座
        # gashot_l=self['直线部分长度']
        # gashot_r=self['弧线部分半径（连防撞装置）']
        # gashot_r2=self['弧线部分半径（连切割头）']  
        sec=Section(Vec3(0,0,0),Vec3(gashot_l,0,0),trans(gashot_l,gashot_r,0)*rotz(-0.5*pi)*scale(gashot_r)*Arc(pi),\
            Vec3(gashot_l,2*gashot_r,0),Vec3(0,2*gashot_r,0),trans(0,gashot_r,0)*rotz(0.5*pi)*scale(gashot_r)*Arc(pi))
        holder1=rotz(0.5*pi)*trans(-0.5*gashot_l,-gashot_r,0)*Sweep(sec,Line(Vec3(0,0,0),Vec3(0,0,20)))
        hodler2=Cone(Vec3(0,gashot_l*0.5,20),Vec3(0,gashot_l*0.5,80),gashot_r*0.4,gashot_r*0.4)
        hodler3=Cone(Vec3(0,-gashot_l*0.5,20),Vec3(0,-gashot_l*0.5,50),gashot_r2,gashot_r2)
        
        Hodler=trans(ratio_x*beam_L,ratio_y*left_L-beam_W-0.5*cartrack_w-z_lift_w*0.5-0.5*gashot_l,\
            transZ+beam_H-0.3*z_lift_h-bump_num*bump_h/2*3-60)*Combine(holder1,hodler2,hodler3)
        # 9.切割头 
        # torch_l=self['割炬长度']
        # torch_d=self['割炬直径']
        # gun_l=self['炬枪长度']
        # gun_d=self['炬枪底面直径']
        cone1=Cone(Vec3(0,0,0),Vec3(0,0,torch_l),torch_d/2,torch_d/2)   
        cone2=Cone(Vec3(0,0,0),Vec3(0,0,-gun_l),torch_d/2,gun_d/2).color(194/255, 124/255, 2/255,1)    
        Torch=trans(ratio_x*beam_L,ratio_y*left_L-beam_W-0.5*cartrack_w-z_lift_w*0.5-gashot_l,\
            transZ+beam_H-0.3*z_lift_h-0.6*torch_l)*Combine(cone1,cone2) 
        # 10.电线
        l1=1.3*z_lift_h-0.4*torch_l
        w1=gashot_l+0.5*z_lift_w+0.5*left_rail_W+beam_W+0.5*l
        #   transZ+=0.5*slider_h+a_carriage_h
        temph=transZ+d+2*h-20
        templ= transZ+beam_H-0.3*z_lift_h+.4*torch_l+l1-temph
        l2=l1-templ
        y1=motor_d
        R=w1/2*0.75
        wire1 =trans(ratio_x*beam_L,ratio_y*left_L-beam_W-0.5*cartrack_w-z_lift_w*0.5-gashot_l,transZ+beam_H-0.3*z_lift_h+0.4*torch_l)*rotz(-0.5*pi)* \
            FilletPipe([Vec3(0,0,0),Vec3(0,0,l1),Vec3(-w1,0,l1),Vec3(-w1,0,l2),Vec3(-w1,R,l2)], [0,R,R,20,0], 20).color(0.1,0.1,0.1,1)
        R=0.5*motor_d+0.5*a_carriage_w
        l1=R+ratio_x*beam_L
        
        wire2=trans(ratio_x*beam_L+0.5*motor_d,ratio_y*left_L+l-15,transZ+h-15)*\
                trans()*createWire(l1,R,a_carriage_h,15)
        wire3=trans(ratio_x*beam_L+0.5*motor_d,ratio_y*left_L+0.4*l-15,transZ+h-15)*\
                trans()*createWire(l1,R,a_carriage_h,5) 
        wire4=trans(ratio_x*beam_L+0.5*motor_d,ratio_y*left_L+0.2*l-15,transZ+h-15)*\
                trans()*createWire(l1,R,a_carriage_h,5)
        box=trans(-0.5*200-0.5*a_carriage_w,ratio_y*left_L+l+2*R+250,transZ-a_carriage_h)\
            *scale(200,100,100)*Cube().color(0,0,0,1)
        Wire=Combine(wire1,wire2,wire3,wire4,box)
        self['切割设备']=combine(LeftPart,RightPart,LinkPart,Trolley,Cable,Zabout,Avoidance,Hodler,Torch,Wire)
        
        
def createWire(l1,R,a_carriage_h,r):
    return FilletPipe([Vec3(0,0,0),Vec3(-l1+R,0,0),Vec3(-l1+R,2*R,0),Vec3(-l1,2*R,0),Vec3(-l1,2*R,-a_carriage_h),Vec3(-l1,2*R+300,-a_carriage_h)],[0,R,R,r+5,r+5,0],r).color(0.1,0.1,0.1,1)     
       
def createDrivemotor(cartrack_h,motor_d,motor_h,reducer_l,reducer_w,reducer_h,coupling_l,coupling_w,coupling_h):
    r=motor_d/2
    cone1=Cone(Vec3(0,0,0),Vec3(0,0,cartrack_h),r,r)
    cone2=Cone(Vec3(0,0,cartrack_h),Vec3(0,0,2*cartrack_h),r*0.8,r*0.8)
    cone3=Cone(Vec3(0,0,2*cartrack_h),Vec3(0,0,motor_h),r*0.3,r*0.3)
    cone4=Cone(Vec3(0,0,3*cartrack_h),Vec3(0,0,motor_h),r,r).color(50/255, 166/255, 1,1)
    motor=Combine(cone1,cone2,cone3,cone4)
    reducer=scale(reducer_l,reducer_w,reducer_h)*Cube()
    remove1=trans(0,0,10)*scale(reducer_l*0.2,reducer_w*0.2,reducer_h-10)*Cube()
    remove2=trans(reducer_l*0.8,0,0)*remove1
    remove3=trans(0,reducer_w*0.8,0)*remove1
    remove4=trans(0,reducer_w*0.8,0)*remove2
    box1=trans(0.35*reducer_l,-30,reducer_h-reducer_l*0.3)*scale(reducer_l*0.3,reducer_l*0.3,30)*Cube()
    box2=trans(0,0,-0.5*reducer_l)*box1
    reducer=trans(-0.5*reducer_l,-0.5*reducer_w,motor_h+coupling_h)*Combine(reducer-remove1-remove2-remove3-remove4,box1,box2).color(0.2,0.2,0.2,1)
   
    # 外壳
    out=Combine(trans(-(motor_d+140)/2,-50-r,2*cartrack_h)*scale(motor_d+140,50,2*cartrack_h)*Cube(),\
                    trans(-(motor_d+140)/2,-50-r,4*cartrack_h)*scale(50,100+motor_d,20)*Cube(),\
                         trans((motor_d+140)/2-50,-50-r,4*cartrack_h)*scale(50,100+motor_d,20)*Cube())
    coupling=trans(-0.5*coupling_l,-0.5*coupling_w,motor_h)*scale(coupling_l,coupling_w,coupling_h)*Cube()
    return  Combine(motor,reducer,coupling,out)
def create_screw(length=50, diameter=8, head_diameter=15, head_height=5):  
    # 1. 螺丝头部 - 使用圆柱形锥体（上下半径相同）
    head_start = Vec3(0, 0, 0)
    head_end = Vec3(0, 0, head_height)
    head = Cone(head_start, head_end, head_diameter/2, head_diameter/2)
    
    # 2. 螺丝杆主体 - 使用圆柱形锥体（上下半径相同）
    body_length = length - head_height*2
    body_start = Vec3(0, 0, head_height)
    body_end = Vec3(0, 0, head_height + body_length)
    body = Cone(body_start, body_end, diameter/2, diameter/2)
    
    # 3.螺丝尾部
    end_start = Vec3(0, 0, head_height+body_length)
    end_end = Vec3(0, 0, length)
    end = Cone(end_start, end_end, head_diameter/2, head_diameter/2)
    # 组合所有部件
    screw_parts = Combine(head, body, end)
    
    return screw_parts

def createLink(l,w,h):
    cube1=trans(-(l+60)/2,-(w+60)/2,0)*scale(l+60,w+60,10)*Cube()
    cube2=trans(-(l+100)/2,-(w+100)/2,h-10)*scale(l+100,w+100,10)*Cube()
    screws=[]
    screw1=create_screw(length=h+50)
    screw2=trans(0,w-30,0)*screw1
    screw3=trans(l-30,w-30,0)*screw1
    screw4=trans(l-30,0,0)*screw1
    screws.append(screw1)
    screws.append(screw2)
    screws.append(screw3)
    screws.append(screw4)
    screws=trans(-l/2+15,-w/2+15,-25)*screws
    return Combine(cube1,cube2,screws)

def createCable(l,w,h,d,num): 
    num_r=(int)(pi*d/2/w)
    num_l=(int)((num-num_r)/2)
    num_r=(int)(num-num_l*2)
    cube1=Combine(scale(w-1,l,h)*Cube(),trans(w-1)*scale(1,l,h)*Cube().color(0,0,0,1))
    cube2=Combine(scale(w,l,h)*Cube()).color(0,0,0,1)
    cubes1=[]
    for i in range(0,num_l):
        if i==0:
            cubes1.append(trans(i*w,0,0)*cube2)
        else:
            cubes1.append(trans(i*w,0,0)*cube1)
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
    return Combine(cubes1,rcubes,cubes2)

def createLogo(size=100, thickness=10, relief_height=5):
    # 1. 创建三角形背景
    triangle_section = Section(
        Vec3(0, 0, 0),           # 底边左端点
        Vec3(size, 0, 0),        # 底边右端点  
        Vec3(size/2, size*0.866, 0)  # 顶点 (等边三角形高度为边长*sqrt(3)/2)
    )
    
    # 拉伸三角形背景
    triangle_base = Sweep(triangle_section, Line(Vec3(0, 0, 0), Vec3(0, 0, thickness)))
    triangle_base = triangle_base.color(0.6, 0.8, 0.2, 1)  # 绿色背景
    
    # 2. 经典闪电形状 - 简单的7边形锯齿
    center_x = size * 0.5
    center_y = size * 0.4
    
    # 标准闪电的7个关键点，从图片分析得出
    lightning_points = [
        Vec3(center_x - size*0.01, center_y + size*0.15, 0),      
        Vec3(center_x + size*0.02, center_y + size*0.15, 0),      
        Vec3(center_x - size*0.06, center_y, 0),                 
        Vec3(center_x + size*0.04, center_y, 0),      
        Vec3(center_x - size*0.04, center_y - size*0.18, 0), 
        Vec3(center_x - size*0.01, center_y - size*0.18, 0), 
        Vec3(center_x - size*0.06, center_y - size*0.22, 0), 
        Vec3(center_x - size*0.10, center_y - size*0.18, 0),      
        Vec3(center_x - size*0.07, center_y - size*0.18, 0),      
        Vec3(center_x - size*0.01, center_y - size*0.03, 0),      
        Vec3(center_x - size*0.11, center_y - size*0.03, 0),
        # # 8. 回到起点
    ]
    
    # 创建闪电的Section
    lightning_section = Section(*lightning_points)
    
    # 3. 拉伸闪电形状
    lightning_relief =trans(0,0,thickness) *Sweep(lightning_section, Line(Vec3(0, 0, 0), Vec3(0, 0,relief_height)))
    lightning_relief = lightning_relief.color(0.8, 0.1, 0.1, 1)  # 红色闪电
    
    # 4. 组合logo
    logo = Combine(triangle_base,lightning_relief)
    
    return logo

if __name__=="__main__":
    final=切割设备()
    place(final)
    
    # 测试logo功能
    # logo = createLogo(size=200, thickness=15, relief_height=8)
    # place(logo)
    
    # a=createDrivemotor(20,100,200,120,120,200,120,120,50)
    # place(a)
    
    
    