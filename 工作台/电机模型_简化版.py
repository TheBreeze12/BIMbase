import pyp3d as p3d
from pyp3d import *

class 三相异步电机_简化版(Component):
    def __init__(self):
        Component.__init__(self)
        # 电机基本参数
        self['电机外径(mm)'] = Attr(200, obvious=True)
        self['电机长度(mm)'] = Attr(300, obvious=True)
        self['输出轴直径(mm)'] = Attr(30, obvious=True)
        self['输出轴长度(mm)'] = Attr(100, obvious=True)
        self['底座长度(mm)'] = Attr(350, obvious=True)
        self['底座宽度(mm)'] = Attr(150, obvious=True)
        self['底座高度(mm)'] = Attr(20, obvious=True)
        self['接线盒尺寸(mm)'] = Attr(80, obvious=True)
        
        # 公共属性
        self['场布类型'] = Attr('机电设备', obvious=True, readonly=True, group='公共属性')
        self['构件类型'] = Attr('电机', obvious=True, readonly=True, group='公共属性')
        self['构件名称'] = Attr('三相异步电机', obvious=True)
        
        self['电机总成']=Attr(None,show=True)
        
        self.replace()
    
    @export
    def replace(self):
        # 获取参数
        outer_dia = self['电机外径(mm)']
        motor_length = self['电机长度(mm)']
        shaft_dia = self['输出轴直径(mm)']
        shaft_length = self['输出轴长度(mm)']
        base_length = self['底座长度(mm)']
        base_width = self['底座宽度(mm)']
        base_height = self['底座高度(mm)']
        junction_box_size = self['接线盒尺寸(mm)']
        
        # 1. 创建底座
        base = translate(0, 0, base_height/2) * Box(
            Vec3(-base_length/2, -base_width/2, 0),
            Vec3(-base_length/2, -base_width/2, base_height),
            Vec3(1, 0, 0),
            Vec3(0, 1, 0),
            base_length, base_width,
            base_length, base_width
        ).color(0.8, 0.5, 0.2, 1)
        
        # 2. 创建定子外壳（紫色圆筒）
        stator_shell = translate(0, 0, motor_length/2) * Cone(
            Vec3(0, 0, 0), 
            Vec3(0, 0, motor_length), 
            outer_dia/2, 
            outer_dia/2
        ).color(0.6, 0.4, 0.8, 1)
        
        # 3. 创建定子铁芯（橙色）
        stator_core_outer = outer_dia/2 - 10
        stator_core_inner = outer_dia/2 - 40
        stator_core_length = motor_length - 20
        
        stator_core = translate(0, 0, motor_length/2) * Cone(
            Vec3(0, 0, -stator_core_length/2), 
            Vec3(0, 0, stator_core_length/2), 
            stator_core_outer, 
            stator_core_outer
        ).color(0.8, 0.5, 0.2, 1)
        
        stator_inner_hole = translate(0, 0, motor_length/2) * Cone(
            Vec3(0, 0, -stator_core_length/2 - 2.5), 
            Vec3(0, 0, stator_core_length/2 + 2.5), 
            stator_core_inner, 
            stator_core_inner
        )
        stator_core = stator_core - stator_inner_hole
        
        # 4. 创建转子（黄色）
        rotor_dia = stator_core_inner - 5
        rotor_length = motor_length - 40
        
        rotor = translate(0, 0, motor_length/2) * Cone(
            Vec3(0, 0, -rotor_length/2), 
            Vec3(0, 0, rotor_length/2), 
            rotor_dia/2, 
            rotor_dia/2
        ).color(0.9, 0.9, 0.2, 1)
        
        rotor_hole = translate(0, 0, motor_length/2) * Cone(
            Vec3(0, 0, -rotor_length/2 - 2.5), 
            Vec3(0, 0, rotor_length/2 + 2.5), 
            shaft_dia/2, 
            shaft_dia/2
        )
        rotor = rotor - rotor_hole
        
        # 5. 创建输出轴
        total_shaft_length = shaft_length + motor_length/2
        shaft = translate(0, 0, total_shaft_length/2) * Cone(
            Vec3(0, 0, 0), 
            Vec3(0, 0, total_shaft_length), 
            shaft_dia/2, 
            shaft_dia/2
        ).color(0.7, 0.7, 0.7, 1)
        
        # 6. 创建端盖
        end_cover_thickness = 15
        end_cover_dia = outer_dia + 5
        
        # 前端盖
        front_cover = translate(0, 0, motor_length + end_cover_thickness/2) * Cone(
            Vec3(0, 0, 0), 
            Vec3(0, 0, end_cover_thickness), 
            end_cover_dia/2, 
            end_cover_dia/2
        ).color(0.6, 0.6, 0.6, 1)
        
        bearing_hole_front = translate(0, 0, motor_length + end_cover_thickness/2) * Cone(
            Vec3(0, 0, -2.5), 
            Vec3(0, 0, end_cover_thickness + 2.5), 
            shaft_dia/2 + 5, 
            shaft_dia/2 + 5
        )
        front_cover = front_cover - bearing_hole_front
        
        # 后端盖
        rear_cover = translate(0, 0, -end_cover_thickness/2) * Cone(
            Vec3(0, 0, 0), 
            Vec3(0, 0, end_cover_thickness), 
            end_cover_dia/2, 
            end_cover_dia/2
        ).color(0.6, 0.6, 0.6, 1)
        
        bearing_hole_rear = translate(0, 0, -end_cover_thickness/2) * Cone(
            Vec3(0, 0, -2.5), 
            Vec3(0, 0, end_cover_thickness + 2.5), 
            shaft_dia/2 + 5, 
            shaft_dia/2 + 5
        )
        rear_cover = rear_cover - bearing_hole_rear
        
        # 7. 创建接线盒
        junction_box = translate(0, outer_dia/2 + junction_box_size/2, motor_length/2) * Box(
            Vec3(-junction_box_size/2, -junction_box_size/2, 0),
            Vec3(-junction_box_size/2, -junction_box_size/2, junction_box_size/2),
            Vec3(1, 0, 0),
            Vec3(0, 1, 0),
            junction_box_size, junction_box_size,
            junction_box_size, junction_box_size
        ).color(0.8, 0.5, 0.2, 1)
        
        # 组装所有部件
        motor_assembly = Combine(
            base,
            stator_shell,
            stator_core,
            rotor,
            shaft,
            front_cover,
            rear_cover,
            junction_box
        )
        
        self['电机总成'] = motor_assembly

if __name__ == "__main__":
    motor = 三相异步电机_简化版()
    place(motor) 