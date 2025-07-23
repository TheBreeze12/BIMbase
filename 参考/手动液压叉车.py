from pyp3d import *
class 手动液压叉车(Component):
    # 定义各个参数及其默认值
    def __init__(self):
        Component.__init__(self)
        self['长1'] = Attr(1500, obvious = True)
        self['宽1'] = Attr(180, obvious = True, readonly = True)
        self['高1'] = Attr(80, obvious = True, readonly = True)
        
        self['底部原点'] = Attr(Vec3(-80,0,0), obvious = True)
        self['顶部原点'] = Attr(Vec3(-80,200,300), obvious = True)
        self['局部坐标系基矢x'] = Attr(Vec3(1,0,0), obvious = True)
        self['局部坐标系基矢y'] = Attr(Vec3(0,1,0), obvious = True)
        self['局部坐标系下底部X方向长度'] = Attr(80, obvious = True)
        self['局部坐标系下底部y方向长度'] = Attr(700, obvious = True)
        self['局部坐标系下顶部X方向长度'] = Attr(80, obvious = True)
        self['局部坐标系下顶部y方向长度'] = Attr(250, obvious = True)
        self['高2'] = Attr(100, obvious = True, readonly = True)
        self['长2']= Attr(100, obvious = True, readonly = True)
        self['把手半径']= Attr(30, obvious = True, readonly = True)
        self['把手高度']= Attr(1200, obvious = True, readonly = True)
        self['弯折半径'] = Attr(70.0, obvious = True)
        self['轮子半径']= Attr(80, obvious = True, readonly = True)
        self['轮子高度']= Attr(60, obvious = True, readonly = True)
        self['模型'] = Attr(None, show = True)
    # 模型造型
    def replace(self): 
        # 设置变量，同时调用参数(简化书写过程)
         L1 = self['长1']
         W1 = self['宽1']
         H1 = self['高1']
         baseorigin=self['底部原点']
         toporigin=self['顶部原点']
         vertorx= self['局部坐标系基矢x'] 
         vertory=self['局部坐标系基矢y']
         basex=self['局部坐标系下底部X方向长度']
         basey=self['局部坐标系下底部y方向长度']
         topx=self['局部坐标系下顶部X方向长度'] 
         topy=self['局部坐标系下顶部y方向长度']
         H2 = self['高2']
         L2 = self['长2']
         R1=self['把手半径']
         H_BS=self['把手高度']
         R2=self['弯折半径']
         R_LZ=self['轮子半径']
         H_LZ=self['轮子高度']
         # 绘制模型
        
         testcube1=scale(L1,W1,H1)*Cube()
         testcone1=trans(L1,W1/2,0)*Cone(Vec3(0,0,0),Vec3(0,0,H1), W1/2,W1/2)
         testmodel1=Combine(testcube1,testcone1).color(1,1,0,1)
         testmodel2=trans(0,basey-W1,0)*testmodel1
         testcube2=trans(-basex,0,0)*scale(basex,basey,H1)*Cube()
         testmodel=combine(testmodel1,testmodel2,testcube2)
         TestBox=Box(Vec3(-80,0,H1),Vec3(-80,200,400+H1),Vec3(1,0,0),Vec3(0,1,0),80,700,80,250)
         model=(testmodel+TestBox).color(1,240/255,0,1)
         
         testcube3=trans(-(basex+L2),(basey-topy)/2,0)*scale(L2,topy,H2)*Cube().color(0,0,0,1)
         testcone2=trans(-(basex+L2/2),basey/2,H2)*Cone(Vec3(0,0,0),Vec3(0,0,H_BS), R1,R1)
         
         TestFilletPipe1 = FilletPipe([Vec3(-(basex+L2/2),basey/2,H2+850),Vec3(-(basex+L2/2),basey/2-500,H2+H_BS-R1),Vec3(-(basex+L2/2),basey/2,H2+H_BS-R1)],# 轨迹拐点
        [0,R2,0],R1 # 管半径。弯折半径必须全部大于管半径。第一个和最后一个点除外。
        )
         TestFilletPipe2=trans(0,basey,0)*mirror_xoz()*TestFilletPipe1
         TestFilletPipe=Combine(TestFilletPipe1)
        #  轮子
         TestCone3 = trans(L1,(W1-H_LZ)/2,-R_LZ)*rotate(Vec3(1,0,0), -0.5 *pi) *Cone(Vec3(0,0,0),Vec3(0,0,H_LZ),R_LZ,R_LZ)
         TestCone4= trans(0,basey-W1,0)*TestCone3
         TestCone5=trans(-80-basex/2,basey/2-H_LZ/2,-R_LZ)*rotate(Vec3(1,0,0), -0.5 *pi) *Cone(Vec3(0,0,0),Vec3(0,0,H_LZ),R_LZ,R_LZ)
         TestCone_lz=combine(TestCone3,TestCone4,TestCone5)

         self['模型']=combine( TestCone_lz,TestFilletPipe,model,testcube3,testcone2)
         # 输出模型
if __name__ == "__main__":
    FinalGeometry = 手动液压叉车()
    FinalGeometry.replace()
    place(FinalGeometry)