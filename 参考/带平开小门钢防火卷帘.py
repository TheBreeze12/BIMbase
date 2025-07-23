from pyp3d import *
# import Door

# class 带平开小门钢防火卷帘(Door.卷帘门):
class 带平开小门钢防火卷帘(Component):
    def __init__(self):
        # Door.卷帘门.__init__(self)
        Component.__init__(self)
        self['带平开小门钢防火卷帘'] = Attr(None, show = True)
        self['门宽'] = Attr(900 , obvious = True)
        self['门高'] = Attr(2100 , obvious = True)
        self['门框宽度'] = Attr(50 , obvious = True)
        self['门框厚度'] = Attr(100 , obvious = True)
        self['门板厚度'] = Attr(50 , obvious = True)


    @export
    def replace(self):
        if self['门宽'] > 3000:
            W = self['门宽']
        else :
            W = 3000
        if self['门高'] > 3000:
            H = self['门高']
        else:
            H = 3000
        frame_w = self['门框宽度']
        frame_t = self['门框厚度']
        board_t = self['门板厚度']

        ##控制箱
        box = Box(Vec3(-W/2,0,H),Vec3(-W/2,0,H-500),Vec3(1,0,0),Vec3(0,1,0),W,5*frame_t,W,5*frame_t)

        ##卷帘门
        section = Section(
            Vec2(W/2-2*frame_w-1200,5),
            Vec2(W/2-2*frame_w-1200,10),
            Vec2(-W/2+2*frame_w,10),
            Vec2(-W/2+2*frame_w,5)
        )
        precision = 100
        section_group = []
        for i in range(0,precision+1,1):
            section_group.append(translate(0,sin(50*pi/2/precision*i),(H-500)/precision*i)*section)
        door_group = Combine(
            translate(W/2,0)*Box(Vec3(-frame_w,0,0),Vec3(-frame_w,0,H-500),Vec3(1,0,0),Vec3(0,1,0),frame_w,frame_t,frame_w,frame_t),
            translate(W/2-frame_w-1200,0)*Box(Vec3(-frame_w,0,0),Vec3(-frame_w,0,H-500),Vec3(1,0,0),Vec3(0,1,0),frame_w,frame_t-10,frame_w,frame_t-10),
            translate(-W/2,0)*Box(Vec3(0,0,0),Vec3(0,0,H-500),Vec3(1,0,0),Vec3(0,1,0),frame_w,frame_t,frame_w,frame_t),
            translate(-W/2+frame_w,0)*Box(Vec3(0,0,0),Vec3(0,0,H-500),Vec3(1,0,0),Vec3(0,1,0),frame_w,frame_t-10,frame_w,frame_t-10),
            Loft(*section_group).color(192/255,192/255,192/255,1)
        )


        ##控制板
        control = translate(-W/2-350,0,1500)*Box(Vec3(-100,0,0),Vec3(-100,0,300),Vec3(1,0,0),Vec3(0,1,0),200,50,200,50)

        self['带平开小门钢防火卷帘'] = translate(0,0,200)*rotate(Vec3(1,0,0),-pi/2)*Combine(
            box,
            door_group,
            control
        )

if __name__ == "__main__":
    finalgeometry = 带平开小门钢防火卷帘()
    finalgeometry.replace()
    place(finalgeometry)