from pyp3d import *
import math

class 铁质门(Component):
    def __init__(self):
        Component.__init__(self)
        # 定义参数（单位：cm）
        self['门板宽'] = Attr(240.0, obvious=True)
        self['门板高'] = Attr(390.0, obvious=True)
        self['门板厚'] = Attr(7.0, obvious=True)
        self['门框厚'] = Attr(44.0, obvious=True)  # 门框总厚度
        self['左右门框宽'] = Attr(20.0, obvious=True)
        self['上门框高'] = Attr(23.0, obvious=True)
        self['下门框高'] = Attr(30.0, obvious=True)
        self['把手深入'] = Attr(10.0, obvious=True)
        self['把手厚'] = Attr(7.0, obvious=True)
        self['把手高'] = Attr(40.0, obvious=True)
        self['连接杆直径'] = Attr(3.0, obvious=True)
        self['边距系数'] = Attr(0.15, obvious=True)  # 横杆距离门框边缘的比例
        self['门'] = Attr(None, show=True)
        self.replace()

    @export
    def replace(self):
        # 提取参数
        w_door = self['门板宽']
        h_door = self['门板高']
        t_door = self['门板厚']
        t_frame = self['门框厚']
        w_side_frame = self['左右门框宽']
        h_top_frame = self['上门框高']
        h_bottom_frame = self['下门框高']
        d_handle = self['把手深入']
        t_handle = self['把手厚']
        h_handle = self['把手高']
        d_rod = self['连接杆直径']
        margin_ratio = self['边距系数']

        # 计算门框内部宽度
        inner_width = w_door - 2 * w_side_frame
        
        # 动态计算横杆长度（确保不超出门框）
        l_rod = inner_width * (1 - 2 * margin_ratio)
        
        # 计算横杆起点和终点位置（确保左右对称）
        rod_start = w_side_frame + inner_width * margin_ratio
        rod_end = rod_start + l_rod

        # 计算门框前后突出量（对称分布）
        frame_offset = (t_frame - t_door) / 2

        # 铁质材质颜色设置
        iron_color = (0.2, 0.2, 0.2, 0.9)
        handle_color = (0.3, 0.3, 0.3, 1.0)

        # 1. 铁质门板
        door_panel = translate(0, 0, frame_offset) * scale(w_door, h_door, t_door) * Cube()
        door_panel = door_panel.color(*iron_color)

        # 2. 铁质门框
        left_frame = translate(-w_side_frame, 0, 0) * scale(w_side_frame, h_door, t_frame) * Cube()
        right_frame = translate(w_door, 0, 0) * scale(w_side_frame, h_door, t_frame) * Cube()
        top_frame = translate(-w_side_frame, h_door, 0) * scale(w_door + 2*w_side_frame, h_top_frame, t_frame) * Cube()
        bottom_frame = translate(-w_side_frame, -h_bottom_frame, 0) * scale(w_door + 2*w_side_frame, h_bottom_frame, t_frame) * Cube()
        
        left_frame = left_frame.color(*iron_color)
        right_frame = right_frame.color(*iron_color)
        top_frame = top_frame.color(*iron_color)
        bottom_frame = bottom_frame.color(*iron_color)

        # 3. 金属把手与连接杆（动态定位）
        rod = Cone(
            Vec3(rod_start, 168, frame_offset + t_door + d_handle/2),
            Vec3(rod_end, 168, frame_offset + t_door + d_handle/2),
            d_rod/2,
            d_rod/2
        ).color(*handle_color)

        left_handle = translate(rod_start - t_handle/2, 168 - h_handle/2, frame_offset + t_door) * scale(t_handle, h_handle, d_handle) * Cube()
        right_handle = translate(rod_end - t_handle/2, 168 - h_handle/2, frame_offset + t_door) * scale(t_handle, h_handle, d_handle) * Cube()
        
        left_handle = left_handle.color(*handle_color)
        right_handle = right_handle.color(*handle_color)
        
        handle_system = combine(left_handle, right_handle, rod)

        # 4. 整体组合
        self['门'] = combine(
            door_panel,
            left_frame, right_frame, top_frame, bottom_frame,
            handle_system
        )

if __name__ == "__main__":
    # 创建铁质材质
    iron_material = create_material(
        name='IronMaterial',
        Color=[0.2, 0.2, 0.2],
        specularColor=[0.8, 0.8, 0.8],
        specularFactor=0.7,
        transparency=0.1
    )
    
    iron_door = 铁质门()
    iron_door['门'].material('IronMaterial')
    place(iron_door)