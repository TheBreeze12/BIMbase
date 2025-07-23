import pyp3d as p3d
from pyp3d import *
import math

def wall_door(data: p3d.P3DData) -> None:
    # 获取参数
    door_width = data['门洞宽度']
    door_height = data['门洞高度']
    door_offset = data['门偏移量']
    door_frame_thickness = data['门框厚度']
    door_has_window = data['门上带窗']
    open_left = data['左开门']
    door_open_angle = data['门开启角度']
    
    # 计算墙体最小尺寸要求
    min_wall_width = door_offset + door_width + 2 * door_frame_thickness + 100  # 门框两侧各留50mm余量
    min_wall_height = door_height + door_frame_thickness + 100  # 门框上下各留50mm余量
    
    # 限制墙体尺寸最小值
    wall_width = max(data['墙体总宽度'], min_wall_width)
    wall_height = max(data['墙体总高度'], min_wall_height)
    wall_thickness = data['墙体厚度']
    
    # 如果参数被调整，更新数据
    if wall_width != data['墙体总宽度']:
        print(f"警告：墙体宽度已从 {data['墙体总宽度']}mm 调整为 {wall_width}mm（最小值要求）")
        data['墙体总宽度'] = wall_width
    if wall_height != data['墙体总高度']:
        print(f"警告：墙体高度已从 {data['墙体总高度']}mm 调整为 {wall_height}mm（最小值要求）")
        data['墙体总高度'] = wall_height
    
    # 解析颜色参数
    wall_color = [float(x) for x in data['墙体颜色'].split(',')]
    door_color = [float(x) for x in data['门扇颜色'].split(',')]
    frame_color = [float(x) for x in data['门框颜色'].split(',')]
    handle_color = [float(x) for x in data['五金颜色'].split(',')]
    
    # 计算依赖参数
    left_panel_width = door_offset
    right_panel_width = wall_width - door_offset - (door_width + 2 * door_frame_thickness)
    lintel_panel_height = wall_height - (door_height + door_frame_thickness)
    
    print(f"参数依赖计算:")
    print(f"左墙板宽度: {left_panel_width:.1f}mm")
    print(f"右墙板宽度: {right_panel_width:.1f}mm")
    print(f"过梁高度: {lintel_panel_height:.1f}mm")
    
    components = []
    
    # 1. 左墙板
    if left_panel_width > 0:
        left_panel = p3d.Box(
            p3d.Vec3(0, 0, 0),
            p3d.Vec3(0, 0, wall_thickness),
            p3d.Vec3(1, 0, 0), p3d.Vec3(0, 1, 0),
            left_panel_width, wall_height, left_panel_width, wall_height
        ).color(wall_color[0], wall_color[1], wall_color[2], 1)
        components.append(left_panel)
    
    # 2. 右墙板
    if right_panel_width > 0:
        right_panel_x = door_offset + door_width + 2 * door_frame_thickness
        right_panel = p3d.Box(
            p3d.Vec3(right_panel_x, 0, 0),
            p3d.Vec3(right_panel_x, 0, wall_thickness),
            p3d.Vec3(1, 0, 0), p3d.Vec3(0, 1, 0),
            right_panel_width, wall_height, right_panel_width, wall_height
        ).color(wall_color[0], wall_color[1], wall_color[2], 1)
        components.append(right_panel)
    
    # 3. 过梁墙板
    if lintel_panel_height > 0:
        lintel_width = door_width + 2 * door_frame_thickness
        lintel_y = door_height + door_frame_thickness
        lintel_panel = p3d.Box(
            p3d.Vec3(door_offset, lintel_y, 0),
            p3d.Vec3(door_offset, lintel_y, wall_thickness),
            p3d.Vec3(1, 0, 0), p3d.Vec3(0, 1, 0),
            lintel_width, lintel_panel_height, lintel_width, lintel_panel_height
        ).color(wall_color[0], wall_color[1], wall_color[2], 1)
        components.append(lintel_panel)
    
    # 4. 门框（U型结构）
    
    # 左门框
    left_frame = p3d.Box(
        p3d.Vec3(door_offset, door_frame_thickness, 0),
        p3d.Vec3(door_offset, door_frame_thickness, wall_thickness),
        p3d.Vec3(1, 0, 0), p3d.Vec3(0, 1, 0),
        door_frame_thickness, door_height, door_frame_thickness, door_height
    ).color(frame_color[0], frame_color[1], frame_color[2], 1)
    components.append(left_frame)
    
    # 右门框
    right_frame_x = door_offset + door_frame_thickness + door_width
    right_frame = p3d.Box(
        p3d.Vec3(right_frame_x, door_frame_thickness, 0),
        p3d.Vec3(right_frame_x, door_frame_thickness, wall_thickness),
        p3d.Vec3(1, 0, 0), p3d.Vec3(0, 1, 0),
        door_frame_thickness, door_height, door_frame_thickness, door_height
    ).color(frame_color[0], frame_color[1], frame_color[2], 1)
    components.append(right_frame)
    
    # 上门框
    top_frame_y = door_height + door_frame_thickness
    top_frame = p3d.Box(
        p3d.Vec3(door_offset, top_frame_y, 0),
        p3d.Vec3(door_offset, top_frame_y, wall_thickness),
        p3d.Vec3(1, 0, 0), p3d.Vec3(0, 1, 0),
        door_width + 2 * door_frame_thickness, door_frame_thickness,
        door_width + 2 * door_frame_thickness, door_frame_thickness
    ).color(frame_color[0], frame_color[1], frame_color[2], 1)
    components.append(top_frame)
    
    # 5. 门扇及其附件（修复：正确的旋转实现）
    door_leaf_thickness = 40.0  # 门扇厚度固定为40mm
    door_leaf_y = door_frame_thickness
    door_leaf_z_offset = (wall_thickness - door_leaf_thickness) / 2
    
    # 计算最终门扇位置
    final_door_x = door_offset + door_frame_thickness  # 门扇左边缘
    
    # 计算铰链轴心位置
    if open_left:
        hinge_x = final_door_x  # 左铰链，门扇左边缘
    else:
        hinge_x = final_door_x + door_width  # 右铰链，门扇右边缘
    
    print(f"\n=== 旋转调试信息 ===")
    print(f"门扇参数:")
    print(f"  door_width: {door_width}")
    print(f"  door_height: {door_height}")
    print(f"  door_leaf_thickness: {door_leaf_thickness}")
    print(f"  final_door_x: {final_door_x}")
    print(f"  hinge_x: {hinge_x}")
    print(f"  door_leaf_y: {door_leaf_y}")
    print(f"  door_leaf_z_offset: {door_leaf_z_offset}")
    print(f"  open_left: {open_left}")
    print(f"  door_open_angle: {door_open_angle}")
    
    # 5.1 创建门扇 - 关键修复：使用正确的pyp3d变换顺序
    print(f"\n=== 门扇几何体创建 ===")
    
    # 计算旋转参数
    if door_open_angle != 0:
        rotation_angle = door_open_angle if open_left else -door_open_angle
        rotation_radians = rotation_angle * pi / 180
    else:
        rotation_radians = 0
    
    # 创建门扇主体
    # 根据pyp3d文档，变换顺序从右到左：Cube -> scale -> translate/rotate
    # 要实现绕指定点旋转：先平移到原点，旋转，再平移回去
    
    # 先定义门扇的变换（与门扇主体一致）
    if open_left:
        door_transform = (
            translate(hinge_x, door_leaf_y, door_leaf_z_offset + door_leaf_thickness/2) *
            rotation(Vec3(0, 1, 0), rotation_radians)
        )
    else:
        door_transform = (
            translate(hinge_x, door_leaf_y, door_leaf_z_offset + door_leaf_thickness/2) *
            rotation(Vec3(0, 1, 0), rotation_radians) *
            translate(-door_width, 0, 0)
        )
    
    if open_left:
        # 左开门：铰链在x=0处
        if door_open_angle != 0:
            # 有旋转：直接绕原点旋转即可
            door_leaf = (translate(hinge_x, door_leaf_y, door_leaf_z_offset + door_leaf_thickness/2) * 
                        rotation(Vec3(0, 1, 0), rotation_radians) * 
                        scale(door_width, door_height, door_leaf_thickness) * 
                        Cube())
        else:
            # 无旋转
            door_leaf = (translate(hinge_x, door_leaf_y, door_leaf_z_offset + door_leaf_thickness/2) * 
                        scale(door_width, door_height, door_leaf_thickness) * 
                        Cube())
    else:
        # 右开门：铰链在x=door_width处
        if door_open_angle != 0:
            # 需要先平移使铰链到原点，旋转，再平移回去
            door_leaf = (translate(hinge_x, door_leaf_y, door_leaf_z_offset + door_leaf_thickness/2) * 
                        rotation(Vec3(0, 1, 0), rotation_radians) * 
                        translate(-door_width, 0, 0) * 
                        scale(door_width, door_height, door_leaf_thickness) * 
                        Cube())
        else:
            # 无旋转，但需要调整位置
            door_leaf = (translate(final_door_x, door_leaf_y, door_leaf_z_offset + door_leaf_thickness/2) * 
                        scale(door_width, door_height, door_leaf_thickness) * 
                        Cube())
    
    door_leaf = door_leaf.color(door_color[0], door_color[1], door_color[2], 1)
    print(f"  门扇基础几何体创建完成")
    
    # 门窗（可选）
    if door_has_window:
        window_width = door_width * 0.5
        window_height = door_height * 0.2
        window_x_offset = door_width * 0.25
        window_y_offset = door_height * 0.6
        window_depth = door_leaf_thickness * 0.6  # 窗户凹进深度
        window_thickness = door_leaf_thickness * 0.4  # 窗户玻璃厚度
        
        print(f"  窗户参数: 宽度={window_width:.1f}, 高度={window_height:.1f}, 凹进深度={window_depth:.1f}")
        
        # 创建窗户凹槽（从门扇中减去）
        if open_left:
            if door_open_angle != 0:
                window_cutout = (translate(hinge_x, door_leaf_y, door_leaf_z_offset + door_leaf_thickness/2) * 
                                rotation(Vec3(0, 1, 0), rotation_radians) * 
                                translate(window_x_offset, window_y_offset, -window_depth/2) * 
                                scale(window_width, window_height, window_depth) * 
                                Cube())
            else:
                window_cutout = (translate(hinge_x + window_x_offset, door_leaf_y + window_y_offset, 
                                         door_leaf_z_offset + door_leaf_thickness/2 - window_depth/2) * 
                                scale(window_width, window_height, window_depth) * 
                                Cube())
        else:
            if door_open_angle != 0:
                window_cutout = (translate(hinge_x, door_leaf_y, door_leaf_z_offset + door_leaf_thickness/2) * 
                                rotation(Vec3(0, 1, 0), rotation_radians) * 
                                translate(-door_width + window_x_offset, window_y_offset, -window_depth/2) * 
                                scale(window_width, window_height, window_depth) * 
                                Cube())
            else:
                window_cutout = (translate(final_door_x + window_x_offset, door_leaf_y + window_y_offset, 
                                         door_leaf_z_offset + door_leaf_thickness/2 - window_depth/2) * 
                                scale(window_width, window_height, window_depth) * 
                                Cube())
        
        # 创建窗户玻璃（凹进部分）
        if open_left:
            if door_open_angle != 0:
                door_window = (translate(hinge_x, door_leaf_y, door_leaf_z_offset + door_leaf_thickness/2) * 
                              rotation(Vec3(0, 1, 0), rotation_radians) * 
                              translate(window_x_offset, window_y_offset, -window_depth + window_thickness/2) * 
                              scale(window_width, window_height, window_thickness) * 
                              Cube())
            else:
                door_window = (translate(hinge_x + window_x_offset, door_leaf_y + window_y_offset, 
                                       door_leaf_z_offset + door_leaf_thickness/2 - window_depth + window_thickness/2) * 
                              scale(window_width, window_height, window_thickness) * 
                              Cube())
        else:
            if door_open_angle != 0:
                door_window = (translate(hinge_x, door_leaf_y, door_leaf_z_offset + door_leaf_thickness/2) * 
                              rotation(Vec3(0, 1, 0), rotation_radians) * 
                              translate(-door_width + window_x_offset, window_y_offset, -window_depth + window_thickness/2) * 
                              scale(window_width, window_height, window_thickness) * 
                              Cube())
            else:
                door_window = (translate(final_door_x + window_x_offset, door_leaf_y + window_y_offset, 
                                       door_leaf_z_offset + door_leaf_thickness/2 - window_depth + window_thickness/2) * 
                              scale(window_width, window_height, window_thickness) * 
                              Cube())
        
        # 设置窗户玻璃颜色（半透明蓝色）
        door_window = door_window.color(0.7, 0.9, 1.0, 0.6)
        
        # 从门扇中减去窗户凹槽，然后添加窗户玻璃
        door_leaf = door_leaf - window_cutout
        door_leaf = p3d.combine(door_leaf, door_window)
        print(f"  门窗添加完成（凹进深度: {window_depth:.1f}mm）")
    
    # === 7字型门把手和门锁与门扇同步变换 ===
    # 门扇本地坐标下的基准点
    if open_left:
        handle_x_local = door_width - 80.0
    else:
        handle_x_local = 80.0
    handle_y_local = 950.0
    handle_z_local = 0.0

    # 计算最大允许的横向长度，避免穿墙
    max_b_length = door_width - handle_x_local - 10.0  # 10mm安全边距
    handle_b_length = min(150.0, max_b_length)

    # 7字型门把手
    handle_a_length = 30.0
    handle_radius = 10.0
    # A段：垂直于门面
    a_start = p3d.Vec3(handle_x_local, handle_y_local, 0)
    a_end = p3d.Vec3(handle_x_local, handle_y_local, handle_a_length)
    handle_a = p3d.Cone(a_start, a_end, handle_radius, handle_radius)
    # 斜连杆（45°，长度20mm）
    diag_length = 20.0
    diag_dx = diag_length / math.sqrt(2)
    diag_dz = diag_length / math.sqrt(2)
    diag_start = a_end
    diag_end = p3d.Vec3(handle_x_local + diag_dx, handle_y_local, handle_a_length + diag_dz)
    handle_diag = p3d.Cone(diag_start, diag_end, handle_radius, handle_radius)
    # B段：平行于门面，朝右
    b_start = diag_end
    b_end = p3d.Vec3(handle_x_local + diag_dx + handle_b_length, handle_y_local, handle_a_length + diag_dz)
    handle_b = p3d.Cone(b_start, b_end, handle_radius, handle_radius)
    door_handle = p3d.combine(handle_a, handle_diag, handle_b)
    door_handle = door_transform * door_handle
    door_handle = door_handle.color(handle_color[0], handle_color[1], handle_color[2], 1)
    components.append(door_handle)
    print(f"  7字型门把手（圆润连接）添加完成，随门运动，本地x={handle_x_local:.1f}, y={handle_y_local:.1f}, 横向段长度={handle_b_length:.1f}")

    # 门锁：贴片，跟随门扇
    lock_width = 40.0
    lock_height = 20.0
    lock_thickness = 2.0
    lock_x_local = handle_x_local
    lock_y_local = handle_y_local - 80.0
    lock_z_local = 1.0
    lock_local = p3d.Box(
        p3d.Vec3(lock_x_local - lock_width/2, lock_y_local - lock_height/2, lock_z_local),
        p3d.Vec3(lock_x_local + lock_width/2, lock_y_local + lock_height/2, lock_z_local + lock_thickness),
        p3d.Vec3(1, 0, 0), p3d.Vec3(0, 1, 0),
        lock_width, lock_height, lock_width, lock_height
    )
    lock = door_transform * lock_local
    lock = lock.color(0.2, 0.2, 0.2, 1)
    components.append(lock)
    print(f"  门锁贴片添加完成，随门运动，本地x={lock_x_local:.1f}, y={lock_y_local:.1f}")
    
    # 将门扇添加到组件列表
    components.append(door_leaf)
    
    print(f"\n=== 门扇变换应用完成 ===")
    print(f"  门扇最终位置: 铰链在({hinge_x}, {door_leaf_y}, {door_leaf_z_offset + door_leaf_thickness/2})")
    
    # 6. 铰链（简化表示）
    hinge_count = 3
    for i in range(hinge_count):
        hinge_y = door_frame_thickness + (i + 1) * door_height / (hinge_count + 1)
        hinge = p3d.Box(
            p3d.Vec3(hinge_x - 15, hinge_y - 50, door_leaf_z_offset),
            p3d.Vec3(hinge_x - 15, hinge_y - 50, door_leaf_z_offset + 10),
            p3d.Vec3(1, 0, 0), p3d.Vec3(0, 1, 0),
            30, 100, 30, 100
        ).color(handle_color[0], handle_color[1], handle_color[2], 1)
        components.append(hinge)
    
    # 组合所有部件
    data['墙门模型'] = p3d.combine(*components)
    
    print(f"参数化墙门模型创建完成")
    print(f"开门方向: {'左开' if open_left else '右开'}")
    print(f"开启角度: {door_open_angle:.1f}度")

if __name__ == "__main__":
    data = p3d.P3DData({
        '墙体总宽度': 4000.0,     # mm
        '墙体总高度': 3000.0,     # mm
        '墙体厚度': 200.0,        # mm
        '门洞宽度': 900.0,        # mm（不含门框）
        '门洞高度': 2100.0,       # mm（不含门框）
        '门偏移量': 500.0,        # mm（门框左侧到墙体左侧距离）
        '门框厚度': 50.0,         # mm
        '门上带窗': True,         # 门上是否带窗
        '左开门': True,           # 开门方向（True=左开，False=右开）
        '门开启角度': 0.0,        # 度（关闭状态）
        '墙体颜色': "0.8,0.8,0.8",
        '门扇颜色': "0.6,0.4,0.2",
        '门框颜色': "0.9,0.9,0.9",
        '五金颜色': "0.8,0.8,0.8",
        '构件名称': '参数化墙门'
    })
    
    data.set_view(-0.125*p3d.pi, -0.125*p3d.pi)
    data.setup('墙门模型', show=True)
    
    # 墙体参数组
    data.setup('墙体总宽度', obvious=True, group='墙体参数', description='墙体总宽度（毫米）')
    data.setup('墙体总高度', obvious=True, group='墙体参数', description='墙体总高度（毫米）')
    data.setup('墙体厚度', obvious=True, group='墙体参数', description='墙体厚度（毫米）')
    
    # 门参数组
    data.setup('门洞宽度', obvious=True, group='门参数', description='门洞宽度（毫米，不含门框）')
    data.setup('门洞高度', obvious=True, group='门参数', description='门洞高度（毫米，不含门框）')
    data.setup('门偏移量', obvious=True, group='门参数', description='门偏移量（毫米，门框左侧到墙体左侧距离）')
    data.setup('门框厚度', obvious=True, group='门参数', description='门框厚度（毫米）')
    data.setup('门上带窗', obvious=True, group='门参数', description='门上是否带窗')
    data.setup('左开门', obvious=True, group='门参数', description='开门方向（True=左开，False=右开）')
    data.setup('门开启角度', obvious=True, group='门参数', description='门开启角度（度）')
    
    # 材质参数组
    data.setup('墙体颜色', obvious=True, group='材质', description='墙体颜色RGB（逗号分隔）')
    data.setup('门扇颜色', obvious=True, group='材质', description='门扇颜色RGB（逗号分隔）')
    data.setup('门框颜色', obvious=True, group='材质', description='门框颜色RGB（逗号分隔）')
    data.setup('五金颜色', obvious=True, group='材质', description='五金颜色RGB（逗号分隔）')
    
    data.setup('构件名称', obvious=True)
    data['replace'] = wall_door
    wall_door(data)
    p3d.launchData(data)