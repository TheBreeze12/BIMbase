from pyp3d import *


#定义参数
class 叉车(Component):
    def __init__(self):
        Component.__init__(self)
        self['叉车'] = Attr(None, show=True)
        self['叉车底座宽1'] = Attr(925.8, obvious = True, group = '底座')
        self['叉车底座宽2'] = Attr(1330, obvious = True, group = '底座')
        self['后轮半径'] = Attr(240, obvious = True, group = '轮胎')
        self['前轮半径'] = Attr(234, obvious = True, group = '轮胎')
        self['叉车架高'] = Attr(2216.4, obvious = True, group = '叉车架')
        self['叉车架长'] = Attr(1144.3, obvious = True, group = '叉车架')
        self['放大倍数'] = Attr(1.0, obvious = True, group = '放大')

        self.replace()
    @export
    def replace(self):
        F_W1 = self['叉车底座宽1']
        F_W2 = self['叉车底座宽2']

        #叉车底座
        sec_1 = Section(Vec2(833.5,258.4),Arc(Vec2(833.5,258.4),Vec2(1240.9,322.3),Vec2(963.4,627.2)),Arc(Vec2(873.8,986.3),Vec2(488.5,895.2),Vec2(94.7,937.4)),\
                        Vec2(94.7,798.9),Arc(Vec2(-1226.8,798.8),Vec2(-1369.6,747.5),Vec2(-1446.9,616.9)),Arc(Vec2(-1446.9,616.9),Vec2(-1451.2,482.6),Vec2(-1413.8,353.4)),Vec2(-1238.4,258.4))
        temp_1 = trans(0,-1/2*F_W1,0)*Sweep(rotx(1/2*pi)*sec_1,Line(Vec3(0,0,0),Vec3(0,F_W1,0)))

        
        sec_2 = Section(Vec2(452.3,258.4),Arc(Vec2(452.3,258.4),Vec2(489,448.8),Vec2(561.9,628.5)),Arc(Vec2(561.9,628.5),Vec2(-212.3,1099.7),Vec2(-1063.3,1411.4)),\
                        Arc(Vec2(-1063.3,1411.4),Vec2(-1245.6,1357.4),Vec2(-1422.6,1287.7)),Arc(Vec2(-1422.6,1287.7),Vec2(-1464.7,1254.7),Vec2(-1486.2,1205.6)),\
                        Arc(Vec2(-1486.2,1205.6),Vec2(-1519.2,851.8),Vec2(-1500.9,496.8)),Arc(Vec2(-1500.9,496.8),Vec2(-1485.7,434.2),Vec2(-1456.7,376.7)),\
                        Arc(Vec2(-1413.8,353.4),Vec2(-1451.2,482.6),Vec2(-1446.9,616.9)),Arc(Vec2(-1446.9,616.9),Vec2(-1369.6,747.5),Vec2(-1226.8,798.9)),\
                        Arc(Vec2(-981.8,798.9),Vec2(-836.7,764.4),Vec2(-722.6,668.4)),Arc(Vec2(-722.6,668.4),Vec2(-620,474.3),Vec2(-580,258.4)))
        temp_2 = trans(0,-1/2*F_W2,0)*Sweep(rotx(1/2*pi)*sec_2,Line(Vec3(0,0,0),Vec3(0,F_W2,0)))
        
        sec_3 = Section(Arc(Vec2(0,-1/2*F_W2),Vec2(-476.7,0),Vec2(0,1/2*F_W2)),Arc(Vec2(0,1/2*F_W2+1000),Vec2(-476.7-1000,0),Vec2(0,-1/2*F_W2-1000)))
        temp_3 = trans(-1063.3,0,0)*Sweep(sec_3,Line(Vec3(0,0,0),Vec3(0,0,3000)))

        #后轮
        HL_R = self['后轮半径']
        houlun_1 = Sweep(Section(scale(100/240*HL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,50))).color(238/255,232/255,170/255)
        houlun_2 = trans(0,0,50)*Sweep(Section(scale(HL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,115))).color(238/255,232/255,170/255)
        houlun_3 = trans(0,0,50+115)*Sweep(Section(scale(170/240*HL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,10))).color(238/255,232/255,170/255)
        houlun_4 = trans(0,0,50)*Sweep(Section(scale(360/240*HL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,115)))
        houlun_5 = trans(0,0,50)*Sweep(Section(scale(HL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,115)))
        houlun1 = trans(-779.1-240,-1/2*F_W1,360)*rotx(1/2*pi)*Combine(houlun_1,houlun_2,houlun_3,(houlun_4-houlun_5).color(0,0,0))
        houlun2 = trans(-779.1-240,1/2*F_W1,360)*rotx(-1/2*pi)*Combine(houlun_1,houlun_2,houlun_3,(houlun_4-houlun_5).color(0,0,0))
        temp_4 = Combine(houlun1,houlun2)


        #轮架
        sec_4 = Section(Arc(Vec2(472.4,258.4),Vec2(713.6,781),Vec2(1175.5,869)),Arc(Vec2(1182.6,887.7),Vec2(561.9,628.5),Vec2(452.4,258.4)))
        lunjia_1 = trans(0,-1/2*F_W1,0)*rotx(1/2*pi)*Sweep(sec_4,Line(Vec3(0,0,0),Vec3(0,0,1/2*(F_W2-F_W1))))
        lunjia_2 = mirror(GeTransform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0]]),'xz')*lunjia_1
        temp_5 = Combine(lunjia_1,lunjia_2)

        #前轮
        QL_R = self['前轮半径']
        qianlun_1 = Sweep(Section(scale(205/234*QL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,32))).color(238/255,232/255,170/255)
        qianlun_2 = trans(0,0,32)*Sweep(Section(scale(QL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,140))).color(238/255,232/255,170/255)
        qianlun_3 = trans(0,0,32+140)*Sweep(Section(scale(150/240*QL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,30))).color(238/255,232/255,170/255)
        qianlun_4 = trans(0,0,32)*Sweep(Section(scale(400/240*QL_R)*Arc())-Section(scale(QL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,200)))
        # qianlun_5 = trans(0,0,32)*Sweep(Section(scale(QL_R)*Arc()),Line(Vec3(0,0,0),Vec3(0,0,200)))
        # qianlun1 = trans(785.8+234,-1/2*F_W1,400)*rotx(1/2*pi)*Combine(qianlun_1,qianlun_2,qianlun_3,(qianlun_4-qianlun_5).color(0,0,0))
        qianlun1 = trans(785.8+234,-1/2*F_W1,400)*rotx(1/2*pi)*Combine(qianlun_1,qianlun_2,qianlun_3,qianlun_4)
        
        # qianlun2 = trans(785.8+234,1/2*F_W1,400)*rotx(-1/2*pi)*Combine(qianlun_1,qianlun_2,qianlun_3,(qianlun_4-qianlun_5).color(0,0,0))
        temp_6 = Combine(qianlun1)

        #叉车架
        C_H = self['叉车架高']
        C_L = self['叉车架长']
        C_W = 463.1/925.8*F_W1
        sec_5 = Section(Vec2(0,0),Vec2(120,0),Vec2(120,-220),Vec2(0,-220),Vec2(0,-140),Vec2(40,-140),Vec2(40,-60),Vec2(0,-60))
        cha_1 = Sweep(sec_5,Line(Vec3(0,0,0),Vec3(0,0,C_H)))
        sec_6 = Section(Vec2(0,0),Vec2(240,0),Arc(Vec2(240,-143.7),Vec2(157.8,-177.8),Vec2(123.7,-260)),Vec2(0,-260))
        cha_2 = trans(133.7,-120,C_H)*rotz(1/2*pi)*rotx(1/2*pi)*Sweep(sec_6,Line(Vec3(0,0,0),Vec3(0,0,-93.7)))
        cha_3 = trans(120,0,C_H)*scale(-C_W-120*2,50,-85)*Cube()
        
        sec_7 = Section(Vec2(595/925.8*F_W1,219.6/2216.4*C_H),Vec2(595/925.8*F_W1,-219.6/2216.4*C_H),Vec2(-595/925.8*F_W1,-219.6/2216.4*C_H),Vec2(-595/925.8*F_W1,219.6/2216.4*C_H))
        
        sec_8 = Section(Vec2(351.5/925.8*F_W1,91.8/2216.4*C_H),Arc(Vec2(471.5/925.8*F_W1,112.9/2216.4*C_H),Vec2(487.9/925.8*F_W1,108.6/2216.4*C_H),Vec2(495/925.8*F_W1,93.2/2216.4*C_H)),\
                        Arc(Vec2(495/925.8*F_W1,-93.2/2216.4*C_H),Vec2(487.9/925.8*F_W1,-108.6/2216.4*C_H),Vec2(471.5/925.8*F_W1,-112.9/2216.4*C_H)),Vec2(351.5/925.8*F_W1,-91.8/2216.4*C_H),\
                        Vec2(-351.5/925.8*F_W1,-91.8/2216.4*C_H),Arc(Vec2(-471.5/925.8*F_W1,-112.9/2216.4*C_H),Vec2(-487.9/925.8*F_W1,-108.6/2216.4*C_H),Vec2(-495/925.8*F_W1,-93.2/2216.4*C_H)),\
                        Arc(Vec2(-495/925.8*F_W1,93.2/2216.4*C_H),Vec2(-487.9/925.8*F_W1,108.6/2216.4*C_H),Vec2(-471.5/925.8*F_W1,112.9/2216.4*C_H)),Vec2(-351.5/925.8*F_W1,91.8/2216.4*C_H))
        cha_4 = trans(0,-220,263.3/2216.4*C_H)*rotx(1/2*pi)*Sweep((sec_7 - sec_8),Line(Vec3(0,0,0),Vec3(0,0,55)))

        chache_1 = trans(1/2*C_W,0,0)*Combine(cha_1,cha_2,cha_3)
        chache_2 = mirror(GeTransform([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]),'yz')*chache_1
        sec_9 = Section(Vec2(0,0),Arc(Vec2(0,-614.6),Vec2(7.5,-632.4),Vec2(25.4,-639.6)),Vec2(C_L,-618.7),Vec2(C_L,-597.4),\
                        Arc(Vec2(75,-597.4),Vec2(57.3,-590.1),Vec2(50,-572.4)),Vec2(50,0))
        cha_5 = trans(1/2*C_W,-220-55,550/2216.4*C_H)*rotz(-1/2*pi)*rotx(1/2*pi)*Sweep(sec_9,Line(Vec3(0,0,0),Vec3(0,0,-120)))
        cha_6 = mirror(GeTransform([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]),'yz')*cha_5

        temp_7 = trans(1209,0,112)*rotz(1/2*pi)*Combine(chache_1,chache_2,cha_4,cha_5,cha_6)

        #驾驶位
        sec_10 = Section(Arc(Vec2(972.5,585.5),Vec2(891.3,1101.2),Vec3(597.6,1532.7)),Arc(Vec2(597.6,1532.7),Vec2(570,1545.8),Vec2(540,1540.4)),\
                         Arc(Vec2(503.4,1520.9),Vec2(491.3,1506.2),Vec2(493.1,1487.1)))
        seat_1 = trans(0,-150,0)*Sweep(rotx(1/2*pi)*sec_10,Line(Vec3(0,0,0),Vec3(0,300,0))).color(238/255,232/255,170/255)

        sec_11 = Section(Vec2(15.8,0),Vec2(15.8,55.7),Vec2(10,55.7),Vec2(10,122.7),Vec2(35,122.7),Arc(Vec2(35,127.7),Vec2(18.3,135.6),Vec2(0,138.3)))
        sec_12 = Section(trans(110,137.7)*scale(12)*Arc())
        seat_2 = trans(526.3,0,1513.9)*roty(-28/180*pi)*Sweep(rotx(1/2*pi)*sec_11,Line(Arc()))
        seat_3 = trans(526.3,0,1513.9)*roty(-28/180*pi)*Sweep(rotx(1/2*pi)*sec_12,Line(Arc()))

        sec_13 = Section(Vec2(0,0),Arc(Vec2(408.3,0),Vec2(446.8,81.2),Vec2(460,170)),Vec2(460,235),Vec2(0,235))
        sec_14 = Section(Vec2(0,0),Arc(Vec2(460,0),Vec2(490.7,35),Vec2(512.3,76.2)),Arc(Vec2(512.3,76.2),Vec2(511.4,92.4),Vec2(498.7,102.5)),\
                         Arc(Vec2(498.7,102.5),Vec2(304.6,127.2),Vec2(143.9,110.4)),Arc(Vec2(143.9,110.4),Vec2(121.2,107.6),Vec2(98.4,108.8)),\
                        Arc(Vec2(98.4,108.8),Vec2(91.6,361.2),Vec2(-48.2,571.5)),Arc(Vec2(-48.2,571.5),Vec2(-94.6,575.3),Vec2(-113.2,532.6)))
        seat_4 = trans(0,-200,0)*Sweep(rotx(1/2*pi)*sec_13,Line(Vec3(0,0,0),Vec3(0,400,0)))
        seat_5 = trans(0,-200,360)*Sweep(rotx(1/2*pi)*sec_14,Line(Vec3(0,0,0),Vec3(0,400,0)))
        
        seat_9 = trans(-210,0,893.6)*Combine(seat_4,seat_5)

        tanhuang_1 = scale(460,400,125)*Cube()
        sec_15 = Section(Vec2(0,0),Arc(Vec2(0,16.1),Vec2(-3.7,26.2),Vec2(-13.2,31.6)),Arc(Vec2(-13.2,31.6),Vec2(0,47),Vec2(-13.2,62.5)),Arc(Vec2(-13.2,62.5),Vec2(0,78),Vec2(-13.2,93.4)),\
                         Arc(Vec2(-13.2,93.4),Vec2(-3.7,98.8),Vec2(0,108.9)),Vec2(0,125),Vec2(10,125),Vec2(10,0))
        tanhuang_2 = trans(460,0,0)*Sweep(rotx(1/2*pi)*sec_15,Line(Vec3(0,0,0),Vec3(0,400,0)))
        sec_16 = mirror(GeTransform([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]),'yz')*sec_15
        tanhuang_3 = Sweep(rotx(1/2*pi)*sec_16,Line(Vec3(0,0,0),Vec3(0,400,0)))
        tanhuang_4 = Sweep(rotz(1/2*pi)*rotx(1/2*pi)*sec_16,Line(Vec3(0,0,0),Vec3(460,0,0)))
        tanhuang_5 = trans(0,400,0)*mirror(GeTransform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0]]),'xz')*tanhuang_4

        seat_10 = trans(-210.3,-200,1128.6)*(tanhuang_1 - tanhuang_2 - tanhuang_3 - tanhuang_4 - tanhuang_5)

        line_1 = rotx(1/2*pi)*Line(Arc(Vec2(0,0),Vec2(596.5,858.2),Vec2(1478.1,873.6)))
        seat_11 = Sweep(Section(scale(40)*Arc()),line_1)
        seat_12 = trans(1478.1,0,873.6)*Sweep(Section(scale(40)*Arc()),Line(Vec3(0,0,0),Vec3(468.6,0,-1634.1)))
        line_2 = rotx(1/2*pi)*Line(Arc(Vec2(0,0),Vec2(797.4,-307.4),Vec2(1524.9,-756)))
        seat_13 = Sweep(Section(roty(74.37/180*pi)*scale(40)*Arc()),line_2)
        seat_14 = trans(469.4,0,-160.4)*Sweep(roty(-24.25/180*pi)*Section(scale(40)*Arc()),Line(Vec3(0,0,0),Vec3(119.8,0,1015.5)))
        seat_15 = trans(0,-584.1/1330*F_W2,0)*rotz(6/180*pi)*Combine(seat_11,seat_12,seat_13,seat_14)
        seat_16 = mirror(GeTransform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0]]),'xz')*seat_15
        seat_17 = trans(-957.4,0,1377.2)*Combine(seat_15,seat_16)
        #trans(-957.4,-584.1/1330*F_W2,1377.2)*rotz(6/180*pi)*Vec2(1478.1,0,873.6)

        seat_18 = trans(-503.4,-1/2*1073/1330*F_W2,1052)*roty(7/180*pi)*scale(20,1073/1330*F_W2,400)*Cube()
        seat_19 = Cone(Vec3(506.9,-460/1330*F_W2,2258.1),Vec3(506.9,460/1330*F_W2,2258.1),40)
        # a = trans(-957.4,-584.1/1330*F_W2,1377.2)*rotz(6/180*pi)*Vec2(1478.1,0,873.6)
        # b = mirror(GeTransform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0]]),'xz')*trans(-957.4,-584.1/1330*F_W2,1377.2)*rotz(6/180*pi)*Vec2(1478.1,0,873.6)
        # seat_19 = Cone(a,b,40)
        seat_20 = Cone(Vec3(-369.4,-1/2*1073/1330*F_W2,2245.4),Vec3(-369.4,1/2*1073/1330*F_W2,2245.4),40)
        temp_8 = Combine(seat_1,seat_2,seat_3,seat_9,seat_10,seat_17,seat_18,seat_19,seat_20)
        
        #顶
        sec_17 = Section(Arc(Vec2(-369.4,2245.4),Vec2(30.4,2323),Vec2(507.9,2260.9)),Arc(Vec2(509.1,2264.7),Vec2(33.3,2327.3),Vec2(-370.8,2249.1)))
        # temp_9 = trans(0,-528.1,0)*Sweep(rotx(1/2*pi)*sec_17,Line(Vec3(0,-528.1,0),Vec3(0,528.1,0)))
        temp_9 = trans(0,-1/2*1073/1330*F_W2,0)*Sweep(rotx(1/2*pi)*sec_17,Line(Vec3(0,-1/2*1073/1330*F_W2,0),Vec3(0,1/2*1073/1330*F_W2,0)))
        sec_18 = Section(Vec2(-369.4,-1/2*1073/1330*F_W2),Vec2(510,-480/1330*F_W2),Vec2(510,-1000/1330*F_W2))
        temp_10 = Sweep(sec_18,Line(Vec3(0,0,0),Vec3(0,0,5000)))
        temp_11 = mirror(GeTransform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0]]),'xz')*temp_10
        temp_12 = temp_9 - temp_10 - temp_11

        a = self['放大倍数']


        # self['叉车'] = seat_15
        
        self['叉车'] = temp_6
    
if __name__ == "__main__":
    FinalGeometry = 叉车()
    place(FinalGeometry)
