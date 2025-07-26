from pyp3d import *

class 卷帘门(Component):
    def __init__(self):
        Component.__init__(self)
        self['洞口宽度']=Attr(3000.0, obvious=True, group='洞口参数', description='洞口宽度（毫米）')
        self['洞口高度']=Attr(2500.0, obvious=True, group='洞口参数', description='洞口高度（毫米）')
        self['帘片高度']=Attr( 100.0,obvious=True, group='帘片参数', description='帘片高度（毫米）')
        self['帘片厚度']=Attr( 5.0,obvious=True, group='帘片参数', description='帘片厚度（毫米）')
        self['导轨宽度']=Attr( 80.0,obvious=True, group='导轨参数', description='侧面U型导轨的宽度（毫米）')
        self['导轨深度']=Attr( 60.0,obvious=True, group='导轨参数', description='侧面U型导轨的深度（毫米）')
        self['轨道类型']=Attr( '标准提升',obvious=True, group='导轨参数', description='提升轨道类型', combo = ['标准提升','高位提升'])
        self['卷轴直径']=Attr( 200.0,obvious=True, group='卷轴参数', description='门帘卷起的中心轴管直径（毫米）')
        self['是否带罩壳']=Attr(True,obvious=True, group='卷轴参数', description='是否在卷轴上方安装保护罩壳')
        self['开启比例']=Attr( 0.3,obvious=True, group='控制参数', description='控制门的开启程度（0-1，0为全关，1为全开）')
        self['高位卷曲比例']=Attr( 0.0,obvious=True, group='控制参数', description='高位卷曲比例（0-1，0为全关，1为全开）')
        self['帘片颜色']=Attr( "0.8,0.8,0.8", obvious=True, group='材质', description='帘片颜色RGB（逗号分隔）')
        self['导轨颜色']=Attr("0.6,0.6,0.6", obvious=True, group='材质', description='导轨颜色RGB（逗号分隔）')
        self['卷轴颜色']=Attr( "0.4,0.4,0.4",obvious=True, group='材质', description='卷轴颜色RGB（逗号分隔）')
        self['罩壳颜色']=Attr("0.7,0.7,0.7", obvious=True, group='材质', description='罩壳颜色RGB（逗号分隔）')
        self['底部横梁颜色']=Attr( "0.5,0.5,0.5", obvious=True, group='材质', description='底部横梁颜色RGB（逗号分隔）')
        self['卷帘门']=Attr(None,show=True)
        self.replace()
    @export
    def replace(self):
        # 限制各个参数在一定范围
        if self['开启比例']>1.0:
            self['开启比例']=1.0
        elif self['开启比例']<0.0:
            self['开启比例']=0.0
        if self['高位卷曲比例']>1.0:
            self['高位卷曲比例']=1.0
        elif self['高位卷曲比例']<0.0:
            self['高位卷曲比例']=0.0
        if self['洞口宽度'] < 1000.0 or self['洞口宽度'] > 5000.0:
            raise ValueError("洞口宽度必须在1000mm到5000mm之间")
        if self['洞口高度'] < 1000.0 or self['洞口高度'] > 5000.0:
            raise ValueError("洞口高度必须在1000mm到3000mm之间")
        if self['帘片高度'] < 50 or self['帘片高度'] > 500:
            raise ValueError("帘片高度必须在50mm到500mm之间")
        if self['帘片厚度'] < 2 or self['帘片厚度'] > 20:
            raise ValueError("帘片厚度必须在2mm到20mm之间")
        if self['导轨宽度'] < 50 or self['导轨宽度'] > 200:
            raise ValueError("导轨宽度必须在50mm到200mm之间")
        if self['导轨深度'] < 30 or self['导轨深度'] > 100:
            raise ValueError("导轨深度必须在30mm到100mm之间")
        if self['卷轴直径'] < 100 or self['卷轴直径'] > 500:
            raise ValueError("卷轴直径必须在100mm到500mm之间")
        if self['高位卷曲比例'] > 0 and self['轨道类型'] != '高位提升':
            self['高位卷曲比例']=0.0
        if self['帘片颜色'] == '':
            self['帘片颜色'] = '0.8,0.8,0.8'
        if self['导轨颜色'] == '':
            self['导轨颜色'] = '0.6,0.6,0.6'
        if self['卷轴颜色'] == '':
            self['卷轴颜色'] = '0.4,0.4,0.4'
        if self['罩壳颜色'] == '':
            self['罩壳颜色'] = '0.7,0.7,0.7'
        if self['底部横梁颜色'] == '':
            self['底部横梁颜色'] = '0.5,0.5,0.5'
        
        
        # 获取参数
        door_width = self['洞口宽度']
        door_height = self['洞口高度']
        curtain_height = self['帘片高度']
        curtain_thickness = self['帘片厚度']
        guide_width = self['导轨宽度']
        guide_depth = self['导轨深度']
        track_type = self['轨道类型']
        high_ratio = self['高位卷曲比例']
        roller_diameter = self['卷轴直径']
        has_canopy = self['是否带罩壳']
        open_ratio = self['开启比例']  # 0-1，0为全关，1为全开
        
        
        # 计算依赖参数
        curtain_count = int(door_height / curtain_height)  # 帘片数量
        actual_curtain_height = door_height / curtain_count  # 实际帘片高度
        
        
        # 解析颜色参数
        curtain_color = [float(x) for x in self['帘片颜色'].split(',')]
        guide_color = [float(x) for x in self['导轨颜色'].split(',')]
        roller_color = [float(x) for x in self['卷轴颜色'].split(',')]
        canopy_color = [float(x) for x in self['罩壳颜色'].split(',')]
        bottom_rail_color = [float(x) for x in self['底部横梁颜色'].split(',')]
        
      
        
        # 1. 侧导轨 (Side Guides)
        if self['轨道类型'] == '标准提升':
            guide_height = door_height
        else:
            guide_height = door_height *2
        guide_height+=roller_diameter/2
        guide_thickness = (guide_width-curtain_thickness)/2
        left_guide_x = 0 -  guide_thickness
        left_guide =Sweep(Section(
             Vec3(left_guide_x, 0, -guide_thickness),
             Vec3(left_guide_x, 0, guide_thickness+curtain_thickness),
             Vec3(guide_depth, 0,  guide_thickness+curtain_thickness),
             Vec3(guide_depth, 0, curtain_thickness),
             Vec3(0, 0, curtain_thickness),
             Vec3(0, 0, 0),
             Vec3(guide_depth, 0, 0),
             Vec3(guide_depth, 0, -guide_thickness),
        ), Line(Vec3(0,0,0),Vec3(0,guide_height,0))).color(guide_color[0], guide_color[1], guide_color[2], 1)
    
        right_guide_x = door_width+guide_thickness
        right_guide =  Sweep( Section(
             Vec3(right_guide_x, 0, -guide_thickness),
             Vec3(right_guide_x, 0, guide_thickness+curtain_thickness),
             Vec3(right_guide_x-guide_depth-guide_thickness, 0,  guide_thickness+curtain_thickness),
             Vec3(right_guide_x-guide_depth-guide_thickness, 0, curtain_thickness),
             Vec3(right_guide_x-guide_thickness, 0, curtain_thickness),
             Vec3(right_guide_x-guide_thickness, 0, 0),
             Vec3(right_guide_x-guide_depth-guide_thickness, 0, 0),
             Vec3(right_guide_x-guide_depth-guide_thickness, 0, -guide_thickness),
        ), Line(Vec3(0,0,0),Vec3(0,guide_height,0))).color(guide_color[0], guide_color[1], guide_color[2], 1)
        print(f"侧导轨创建完成: 宽度={guide_width}mm, 深度={guide_depth}mm, 高度={guide_height}mm")
        
        
        # 2. 卷轴总成 (Roller Assembly)
        roller_extra = 300 # 卷轴比门宽多出的长度
        roller_length = door_width + roller_extra
        roller_x0 = -roller_extra/2
        roller_x1 = door_width + roller_extra/2
        roller_y = door_height + roller_diameter/2  # 卷轴中心在门洞正上方
        roller_z = roller_diameter/2
        roller =  Cone(
             Vec3(roller_x0, roller_y, roller_z),
             Vec3(roller_x1, roller_y, roller_z),
            roller_diameter/2, roller_diameter/2
        ).color(roller_color[0], roller_color[1], roller_color[2], 1)
        end_cap_radius = roller_diameter/2 + 5
        left_end_cap =  Cone(
             Vec3(roller_x0, roller_y, roller_z),
             Vec3(roller_x0 - 10, roller_y, roller_z),
            end_cap_radius, end_cap_radius
        ).color(roller_color[0], roller_color[1], roller_color[2], 1)
        right_end_cap =  Cone(
             Vec3(roller_x1, roller_y, roller_z),
             Vec3(roller_x1 + 10, roller_y, roller_z),
            end_cap_radius, end_cap_radius
        ).color(roller_color[0], roller_color[1], roller_color[2], 1)

        if self['轨道类型'] == '高位提升':
            roller= translate(Vec3(0,door_height,0))*roller
            left_end_cap= translate(Vec3(0,door_height,0))*left_end_cap
            right_end_cap= translate(Vec3(0,door_height,0))*right_end_cap
        # components.extend([left_end_cap, right_end_cap])
        print(f"卷轴总成创建完成: 直径={roller_diameter}mm, 长度={roller_length}mm")

        # 将门帘收起的部分缠绕在卷轴上
        if self['轨道类型'] == '标准提升':
            rolled_length = door_height*open_ratio
            trans= translate(Vec3(0,0,0))
        else:
            if open_ratio == 1:
                rolled_length = door_height*high_ratio
                trans= translate(Vec3(0,door_height,0))
                print(f"收起帘片缠绕长度: {rolled_length}mm")
            else:
                rolled_length = 0
        D1=roller_diameter
        if rolled_length > 0:
            # 假设每圈帘片厚度为curtain_thickness
            D0 = roller_diameter
            t = curtain_thickness
            L = rolled_length
            D1 = D0+2*L/(math.pi*D0)*t
            # 用加粗的圆柱体表现卷绕层
            rolled_curtain = trans*  Cone(
                 Vec3(0, roller_y, roller_z),
                 Vec3(door_width, roller_y, roller_z),
                D1/2, D1/2
            ).color(curtain_color[0], curtain_color[1], curtain_color[2], 1)
            print(f"收起帘片缠绕层: 外径={D1:.1f}mm, 卷绕长度={L:.1f}mm")
            roller=Combine(rolled_curtain,roller)
            
        # 3. 门帘 (Curtain) - 顶部与洞口顶部对齐
        # 底部横梁
        bottom_rail_height = 60
        if  self['轨道类型'] == '标准提升':
            visible_height = door_height * (1 - open_ratio) + roller_diameter/2
            trans= translate(Vec3(0,0,0))
        else:
            if open_ratio == 1:
                visible_height = door_height*(1-high_ratio)+roller_diameter/2
                trans= translate(Vec3(0,door_height,0))
            else:
                visible_height = door_height+roller_diameter/2
                trans= translate(Vec3(0,door_height*open_ratio,0))
        visible_curtain_count = int(visible_height / actual_curtain_height)
        curtain_parts = []
        print(f"可见帘片数量: {visible_curtain_count}/{curtain_count}")
        curtain_top_y = door_height+ roller_diameter/2 +bottom_rail_height # 门帘顶部与门洞顶部对齐
        curtain_bottom_y = curtain_top_y - visible_curtain_count * actual_curtain_height
        for i in range(visible_curtain_count):
            curtain_y = curtain_top_y - (i + 1) * actual_curtain_height
            curtain_panel = trans* Box(
                 Vec3(0, curtain_y, 0),
                 Vec3(0, curtain_y, curtain_thickness),
                 Vec3(1, 0, 0),  Vec3(0, 1, 0),
                door_width, actual_curtain_height, door_width, actual_curtain_height
            ).color(curtain_color[0], curtain_color[1], curtain_color[2], 1)
            hinge_count = 3
            for j in range(hinge_count):
                hinge_x = (j + 1) * door_width / (hinge_count + 1)
                hinge = trans* Box(
                     Vec3(hinge_x - 5, curtain_y + actual_curtain_height - 10, curtain_thickness),
                     Vec3(hinge_x + 5, curtain_y + actual_curtain_height, curtain_thickness + 5),
                     Vec3(1, 0, 0),  Vec3(0, 1, 0),
                    10, 10, 10, 10
                ).color(0.3, 0.3, 0.3, 1)
                curtain_panel =  combine(curtain_panel, hinge)
            curtain_parts.append(curtain_panel)
        if curtain_parts:
            curtain =  combine(*curtain_parts)
            print(f"门帘创建完成: {len(curtain_parts)}个帘片")
        bottom_rail_thickness = curtain_thickness
        bottom=trans* Box(
             Vec3(0,curtain_bottom_y-bottom_rail_height, 0),
             Vec3(0, curtain_bottom_y-bottom_rail_height, bottom_rail_thickness),
             Vec3(1, 0, 0),  Vec3(0, 1, 0),
            door_width, bottom_rail_height, door_width, bottom_rail_height
        ).color(bottom_rail_color[0], bottom_rail_color[1], bottom_rail_color[2], 1)
         
        # 5. 罩壳 (Canopy Cover) - 可选
        if has_canopy:
            max_d=roller_diameter+door_height/(pi*roller_diameter)*curtain_thickness*2
            canopy_width = door_width + 600
            canopy_height = roller_diameter+300
            canopy_depth =   roller_diameter + 100
            canopy_x0 = -300  # 罩壳左侧位置
            canopy_y = roller_y - max_d/2
            canopy =  translate(Vec3(0,0,max_d/2))*  Sweep(
                 Section(Vec3(canopy_x0,canopy_y,-canopy_depth/2),Vec3(canopy_x0,canopy_y+canopy_height,-canopy_depth/2), \
                    Vec3(canopy_x0,canopy_y+canopy_height,canopy_depth/4),Vec3(canopy_x0,canopy_y+canopy_height/2,canopy_height/2),\
                        Vec3(canopy_x0,canopy_y,canopy_height/2)),\
                         Line(Vec3(0,0,0),Vec3(canopy_width,0,0))
            ).color(canopy_color[0], canopy_color[1], canopy_color[2], 1)
            if  self['轨道类型'] == '高位提升':
                canopy= translate(Vec3(0,door_height,0))*canopy
            print(f"罩壳创建完成: 尺寸={canopy_width}x{canopy_height}x{canopy_depth}mm")

        # 6.控制系统
        control_box_width = 120
        control_box_height = 80
        control_box_depth = 40
        control_box_x = door_width + 150
        control_box_y = door_height/2
        control_box =  Box(
             Vec3(control_box_x, control_box_y - control_box_height/2, 0),
             Vec3(control_box_x, control_box_y -control_box_height/2, control_box_depth),
             Vec3(1, 0, 0),  Vec3(0, 1, 0),
            control_box_width, control_box_height, control_box_width, control_box_height
        ).color(0.1, 0.1, 0.1, 1)
        if has_canopy:
            self['卷帘门']=Combine(canopy,control_box,left_guide,right_guide,roller,left_end_cap,right_end_cap,curtain,bottom)
        else:
            self['卷帘门']=Combine(control_box,left_guide,right_guide,roller,left_end_cap,right_end_cap,curtain,bottom)
        print(f"控制系统创建完成")
        print(f"\n=== 卷帘门模型创建完成 ===")
        print(f"开启状态: {open_ratio*100:.1f}%")
        print(f"可见帘片: {visible_curtain_count}/{curtain_count}")
        print(f"轨道类型: {track_type}")


if __name__=="__main__":
    final=卷帘门()
    place(final)