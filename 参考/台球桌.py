from pyp3d import *
class main(Component):
    def __init__(self):
        Component.__init__(self)
        self['main'] = Attr(None, show = True)
        self.replace()

    @export
    def replace(self):
        # 0 切除平面
        cutSection1 = Section(arc_of_radius_points_3D(Vec3(40,65/2,0),Vec3(40,-65/2,0),-42),arc_of_radius_points_3D(Vec3(-40,-65/2,0),Vec3(-40,65/2,0),-42))
        cutPart1 = Sweep(cutSection1,Line(Vec3(0,0,0),Vec3(0,0,100)))
        cutSection2 = Section(arc_of_radius_points_3D(Vec3(200,75/2,0),Vec3(200,-75/2,0),-42),arc_of_radius_points_3D(Vec3(-200,-75/2,0),Vec3(-200,75/2,0),-42))
        cutPart2 = Sweep(cutSection2,Line(Vec3(0,0,0),Vec3(0,0,100)))
        cutSection3 = Section(Vec3(-75,0,0),Vec3(75,0,0),Vec3(0,60,0))
        cutPart3 = Sweep(cutSection3,Line(Vec3(0,0,0),Vec3(0,0,83.68)))
        cutPart4 = Sweep(Section(scale(75/2)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,83.68)))
        # 0 填充平面
        fillPart1 = cutPart3- trans(0,-63,0)*cutPart4
                                                                                                                                              
        # 1 桌子腿
        # 1.1 建模
        tableLegs1 = Cone(Vec3(0,0,0),Vec3(0,0,17.5),52.5,52.5)
        tableLegs2 = Cone(Vec3(0,0,0),Vec3(0,0,10),44.375,44.375)
        tableLegs3 = Sweep(rotate(Vec3(1,0,0),0.5*pi)*Section(Vec3(0,0,0),arc_of_radius_points_3D(Vec3(52.5,0,0),Vec3(52.5,60,0),50),Vec3(0,60,0)),\
                           Line(Arc()))
        tableLegs4 = Cone(Vec3(0,0,0),Vec3(0,0,192.22),50,50) 
        tableLegs41 = trans(0,50,0)*Sweep(Section(Vec3(-5,0,0),Vec3(5,0,0),Vec3(0,12,0)),Line(Vec3(0,0,0),Vec3(0,0,192.22)))
        tableLegs41Array = Array(tableLegs41)
        for i in linspace(0,2 *55/56,56):
            tableLegs41Array.append(rotate(Vec3(0,0,1),2*i*pi))
        tableLegs4 = combine(tableLegs4,tableLegs41Array)
        tableLegs5 = Sweep(rotate(Vec3(1,0,0),0.5*pi)*Section(Vec3(0,0,0),arc_of_radius_points_3D(Vec3(46.31,0,0),Vec3(46.31,20.17,0),30),Vec3(0,20.17,0)),\
                           Line(Arc()))
        tableLegs6 = Cone(Vec3(0,0,0),Vec3(0,0,24.69),46.31,60)
        tableLegs7 = Cone(Vec3(0,0,0),Vec3(0,0,16.85),60,60)
        tableLegs8 = Sweep(rotate(Vec3(1,0,0),0.5*pi)*Section(Vec3(0,0,0),arc_of_radius_points_3D(Vec3(60,0,0),Vec3(41.1,55.74,0),40),Vec3(0,55.74,0)),\
                           Line(Arc()))
        tableLegs9 = Cone(Vec3(0,0,0),Vec3(0,0,63.11),65,65)
        tableLegs10 = Sweep(
            (Section(rectangle_central_symmetry(134.68/2,134.68/2,9))-\
            trans(0,-63,0)*Section(Vec3(-20,0,0),Vec3(20,0,0),Vec3(20,-5,0),Vec3(-20,-5,0))-\
            rotate(Vec3(0,0,1),0.5*pi)*trans(0,-63,0)*Section(Vec3(-20,0,0),Vec3(20,0,0),Vec3(20,-5,0),Vec3(-20,-5,0))-\
            rotate(Vec3(0,0,1),1*pi)*trans(0,-63,0)*Section(Vec3(-20,0,0),Vec3(20,0,0),Vec3(20,-5,0),Vec3(-20,-5,0))-\
            rotate(Vec3(0,0,1),1.5*pi)*trans(0,-63,0)*Section(Vec3(-20,0,0),Vec3(20,0,0),Vec3(20,-5,0),Vec3(-20,-5,0))),\
            Line(Vec3(0,0,0),Vec3(0,0,141.61))
            )
        # 1.2 定位
        tableLeg = combine(tableLegs1,trans(0,0,17.5)*tableLegs2,trans(0,0,27.5)*tableLegs3,\
                           trans(0,0,27.5+60)*tableLegs4,trans(0,0,27.5+60+192.22)*tableLegs5,\
                           trans(0,0,27.5+60+192.22+20.17)*tableLegs6,\
                            trans(0,0,27.5+60+192.22+20.17+24.69)*tableLegs7,\
                           trans(0,0,27.5+60+192.22+20.17+24.69+16.85)*tableLegs8,\
                            trans(0,0,27.5+60+192.22+20.17+24.69+16.85+55.74)*tableLegs9,\
                                   trans(0,0,27.5+60+192.22+20.17+24.69+16.85+55.74+63.11)*tableLegs10).color(187/255,191/255,188/255)
        # 2 桌底
        # 2.1 建模
        tableBottom1 = Sweep(Section(rectangle_central_symmetry(2138.25/2,1036.98/2,0)),Line(Vec3(0,0,0),Vec3(0,0,30)))
        tableBottom2 = trans(0,0,30)*Sweep(Section(rectangle_central_symmetry(2168.25/2,1066.98/2,0)),Line(Vec3(0,0,0),Vec3(0,0,35)))
        tableBottom3 = trans(0,0,30+35)*Sweep(Section(rectangle_central_symmetry(2198.25/2,1096.98/2,0)),Line(Vec3(0,0,0),Vec3(0,0,40)))
        tableBottom4 = Sweep(Section(rectangle_central_symmetry(1147.70,1200/2,0)),Line(Vec3(0,0,0),Vec3(0,0,83.68)))\
            -trans(-(1160.45-5),612.64-5,0)*rotate(Vec3(0,0,1),-1/4*pi)*cutPart1-trans(-(1167.45-12.5),-(619.64-12.5),0)*rotate(Vec3(0,0,1),0.25*pi)*cutPart1\
            -trans((1167.45-12.5),-(619.64-12.5),0)*rotate(Vec3(0,0,1),0.75*pi)*cutPart1-trans((1167.45-12.5),(619.64-12.5),0)*rotate(Vec3(0,0,1),1.25*pi)*cutPart1
        tableBottom4fill = cutPart3-trans(0,40,0)*cutPart4
        tableBottom4 = combine(tableBottom4,trans(0,600,0)*tableBottom4fill,trans(0,-600,0)*mirror_xoz()*tableBottom4fill)
        tableBottom4 = trans(0,0,30+35+40)*tableBottom4
        # 2.2 定位
        tableBottom = combine(tableBottom1,tableBottom2,tableBottom3,tableBottom4).color(128/255,128/255,128/255)
        # 3 桌顶
        # 3.1 桌顶边
        topMargin11 = Sweep((Section(rectangle_central_symmetry(1250,701.74,160))-\
                           Section(rectangle_central_symmetry(1171.71,623.40,0))),Line(Vec3(0,0,0),Vec3(0,0,66)))
        topMargin22 = Sweep((Section(rectangle_central_symmetry(1171.71,623.40,0))-\
                           Section(rectangle_central_symmetry(1147.7,600,0))),Line(Vec3(0,0,0),Vec3(0,0,66)))
        # testMargin = Sweep(Section(rectangle_central_symmetry(1147.7,600,0)),Line(Vec3(0,0,0),Vec3(0,0,30)))

        topMarginCut = combine(trans(-1250,701.74,0)*rotate(Vec3(0,0,1),-1/4*pi)*cutPart2,trans(-1250,-701.74,0)*rotate(Vec3(0,0,1),1/4*pi)*cutPart2,\
        trans(1250,701.74,0)*rotate(Vec3(0,0,1),1/4*pi)*cutPart2,trans(1250,-701.74,0)*rotate(Vec3(0,0,1),-1/4*pi)*cutPart2,trans(0,597,0)*cutPart3,\
            trans(0,-597,0)*mirror_xoz()*cutPart3,trans(0,637,0)*cutPart4,trans(0,-637,0)*cutPart4)
        topMargin2 = topMargin22 - topMarginCut
        topMargin1 = topMargin11 - topMarginCut
        topMargin = combine(topMargin1.color(218/255,222/255,219/255),topMargin2.color(128/255,128/255,128/255))
        # 3.2 边袋
        SideBag = Sweep(Section(Vec3(0,0,0),arc_of_radius_points_3D(Vec3(0,15.44,0),Vec3(150,164.87,0),-121),\
                        Vec3(165,164.87,0),Vec3(165,78.62,0),(Vec3(87.51,78.62,0),Vec3(87.51,0,0))),Line(Vec3(0,0,0),Vec3(0,0,70)))
        SideBag = (trans(-87.51,-78.62,0)*SideBag - rotate(Vec3(0,0,1),-1/4*pi)*cutPart1).color(1,1,1)
        SideBagSum = combine(trans(-1250,701.74,0)*rotate(Vec3(0,0,1),-1/4*pi)*cutPart2,trans(-1250,-701.74,0)*rotate(Vec3(0,0,1),1/4*pi)*cutPart2,\
        trans(1250,701.74,0)*rotate(Vec3(0,0,1),1/4*pi)*cutPart2,trans(1250,-701.74,0)*rotate(Vec3(0,0,1),-1/4*pi)*cutPart2)
        # 3.3 中袋
        middleBag = (Sweep(Section(rectangle_central_symmetry(105/2,105/2,0)),Line(Vec3(0,0,0),Vec3(0,0,70)))-\
            trans(0,-105/2,0)*cutPart3-trans(0,-12.65,0)*cutPart4).color(1,1,1)
        # 4 桌面修饰
        # 4.1 球杆
        ballArm = rotate(Vec3(0,1,0),0.5*pi)*Combine(Loft(Section(scale(12)*Arc()),trans(0,0,1300)*Section(scale(3)*Arc())),\
                          trans(0,0,1300)*Loft(Section(scale(3)*Arc()),trans(0,0,4)*Section(scale(2)*Arc())).color(79/255,79/255,198/255))
        # 4.2 台球
        def ballPure(R,G,B):
            return scale(25)*Sphere().color(R,G,B)
        def ballMax(R,G,B):
            return Combine(scale(25)*Sphere().color(1,1,1),Loft(trans(0,0,10)*Section(scale(23.5)*Arc()),\
                                                                Section(scale(25.5)*Arc()),trans(0,0,-10)*Section(scale(23.5)*Arc())).color(R,G,B))
        # 4.3 台球组
        ballMaxSum = combine(trans(-110,0,0)*ballMax(88/255,0/255,161/255),trans(-55,0,0)*ballPure(1,1,0),ballMax(1,0,0),trans(55,0,0)*ballPure(0,184/255,0),trans(110,0,0)*ballMax(158/255,92/255,90/255),\
                             trans(-(55/2+55),55,0)*ballPure(183/255,110/255,108/255),trans(-55/2,55,0)*ballMax(0/255,0/255,241/255),trans(55/2,55,0)*ballPure(255/255,187/255,110/255),trans(55/2+55,55,0)*ballPure(107/255,0/255,188/255),\
                             trans(-55,55*2,0)*ballPure(255/255,0/255,0/255),trans(0,55*2,0)*ballPure(74/255,74/255,74/255),trans(55,55*2,0)*ballMax(0/255,162/255,0/255),\
                             trans(-55/2,55*3,0)*ballMax(237/255,146/255,83/255),trans(55/2,55*3,0)*ballMax(224/255,228/255,0/255),\
                             trans(0,55*4,0)*ballPure(0,0,1),trans(0,-30,-25)*\
                             Sweep((Section(Vec3(-170,0,0),Vec3(170,0,0),Vec3(0,320,0))-Section(Vec3(-165,3,0),Vec3(165,3,0),Vec3(0,313,0))),Line(Vec3(0,0,0),Vec3(0,0,30))).color(1,1,1))
        # 4.4 网兜
        net1 = FilletPipe([Vec3(0,-45/2,0),Vec3(-17,-45/2,-8),Vec3(-17-229,-45/2,-8-12),Vec3(-17-229,45/2,-8-12),Vec3(-17,45/2,-8),Vec3(0,45/2,0)], [0,50,10,10,50,0], 2.5).color(1,1,0,1)
        net2 = FilletPipe([Vec3(0,0,0),Vec3(-23,0,-18),Vec3(-23-220,0,-18-30),Vec3(-23-220-28,0,-18-30+27)], [0,10,10,0], 2.5).color(1,1,0,1)
        net3 = FilletPipe([Vec3(0,0,0),Vec3(-111,0,73)], [0,0], 1.5).color(1,1,0,1)
        net = combine(net1,trans(28,0,0)*net2,trans(-244,0,-22)*net3).color(210/255,145/255,102/255)
        baginentity1 = Loft(trans(0,0,-37)*(Section(scale(75/2)*Arc())-Section(scale(73/2)*Arc())),trans(0,0,-87)*(Section(scale(52/2)*Arc())-Section(scale(50/2)*Arc()))).color(134/255,135/255,73/255,0.01)
        baginentity2 = Loft((Section(scale(52/2)*Arc())-Section(scale(50/2)*Arc())),trans(0,0,-10)*(Section(scale(52/2)*Arc())-Section(scale(50/2)*Arc()))).color(134/255,135/255,73/255,)
        baginentity3 = Loft(trans(-25,40-5,-37)*(rotate(Vec3(0,0,1),-1/4*pi)*cutSection1-scale(0.95)*rotate(Vec3(0,0,1),-1/4*pi)*cutSection1),trans(0,0,-87)*(Section(scale(52/2)*Arc())-Section(scale(50/2)*Arc()))).color(134/255,135/255,73/255,0.01)
        # baginentity3 = Loft(cutSection1-scale(0.95)*cutSection1,trans(0,0,-10)*(Section(scale(52/2)*Arc())-Section(scale(50/2)*Arc()))).color(134/255,135/255,73/255,)
        bagin1 = combine(baginentity1,trans(0,0,-87)*baginentity2)
        bagin2 = combine(baginentity3,trans(0,0,-87)*baginentity2)
        netmiddleSum = combine(net,trans(10,0,90)*bagin1)
        netSideSum = combine(net,trans(10,0,90)*bagin2)
        # 5 汇总定位
        mainSum = combine(tableBottom,trans(0,451.4,-601.89)*tableLeg,trans(0,-451.4,-601.89)*tableLeg,\
                          trans(1001,451.4,-601.89)*tableLeg,trans(1001,-451.4,-601.89)*tableLeg,\
                          trans(-1001,451.4,-601.89)*tableLeg,trans(-1001,-451.4,-601.89)*tableLeg,\
                          trans(0,0,30+35+40+83.68)*topMargin,\
                          trans(-1167.45,619.64,190.50)*SideBag,trans(-1167.45,-619.64,190.50)*rotate(Vec3(0,0,1),0.5*pi)*SideBag,\
                          trans(1167.45,-619.64,190.50)*rotate(Vec3(0,0,1),1*pi)*SideBag,trans(1167.45,619.64,190.50)*rotate(Vec3(0,0,1),1.5*pi)*SideBag,\
                          trans(0,653,190.50)*middleBag,trans(0,-649.64,190.50)*mirror_xoz()*middleBag,trans(0,649.64,190.50)*middleBag,\
                          trans(-1380,300.64,300-15)*rotate(Vec3(0,0,1),-0.02*pi)*ballArm,trans(-1380,-300.64,300-15)*rotate(Vec3(0,0,1),0.1*pi)*ballArm,\
                          trans(600,0,30+35+40+83.68+30)*rotate(Vec3(0,0,1),0.5*pi)*ballMaxSum,\
                          trans(1167.45,640,140)*mirror_xoz()*netSideSum,trans(1167.45,-640,140)*netSideSum,\
                          trans(-1167.45,640,140)*mirror_yoz()*mirror_xoz()*netSideSum,trans(-1167.45,-640,140)*mirror_yoz()*netSideSum,\
                          trans(-10,640,140)*netmiddleSum,trans(-10,-640,140)*netmiddleSum)


        self['main'] = mainSum
        
if __name__ == "__main__":
    FinalGeometry = main()
    place(FinalGeometry)
