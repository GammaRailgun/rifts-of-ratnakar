import math
import bpy

data = [
    ("PT-7-4-4", 3.745, 2.14, 1.718, 2.439, 3),
    ("PT-6-4-4", 3.39, 2.25, 1.556, 2.441, 3),
    ("PT-5-4-4", 2.99, 2.395, 1.372, 2.439, 3),
    ("PT-4-4-4", 2.58, 2.58, 1.184, 2.442, 3),
    ("ES-7-4-4", 4.085, 2.335, 1.874, 3.168, 3),
    ("ES-6-4-4", 3.685, 2.455, 1.691, 3.159, 3),
    ("ES-5-4-4", 3.265, 2.61, 1.498, 3.163, 3),
    ("ES-4-4-4", 2.815, 2.815, 1.292, 3.173, 3),
    ("CT-7-4-4", 4.51, 2.58, 2.305, 3.558, 3),
    ("CT-6-4-4", 4.07, 2.715, 2.081, 3.556, 3),
    ("CT-5-4-4", 3.605, 2.885, 1.843, 3.556, 3),
    ("CT-4-4-4", 3.105, 3.105, 1.587, 3.548, 3),
    ("DD-7-4-4", 4.945, 2.825, 2.528, 4.677, 3),
    ("DD-6-4-4", 4.465, 2.975, 2.282, 4.684, 3),
    ("DD-5-4-4", 3.95, 3.16, 2.019, 4.675, 3),
    ("DD-4-4-4", 3.405, 3.405, 1.741, 4.679, 3),
    ("FF-7-4-4", 5.4, 3.085, 2.961, 5.279, 3),
    ("FF-6-4-4", 4.875, 3.25, 2.673, 5.289, 3),
    ("FF-5-4-4", 4.315, 3.455, 2.366, 5.291, 3),
    ("FF-4-4-4", 3.72, 3.72, 2.04, 5.288, 3),
    ("CL-7-4-4", 6.8, 3.875, 3.728, 7.866, 4),
    ("CL-6-4-4", 6.15, 4.095, 3.372, 7.945, 4),
    ("CL-5-4-4", 5.45, 4.35, 2.988, 7.945, 4),
    ("CL-4-4-4", 4.69, 4.69, 2.571, 7.947, 4),
    ("CA-7-4-4", 7.4, 4.235, 4.057, 10.224, 4),
    ("CA-6-4-4", 6.7, 4.46, 3.673, 10.267, 4),
    ("CA-5-4-4", 5.9, 4.74, 3.235, 10.212, 4),
    ("CA-4-4-4", 5.1, 5.1, 2.796, 10.219, 4),
    ("BC-7-4-4", 7.95, 4.535, 4.359, 12.596, 4),
    ("BC-6-4-4", 7.15, 4.775, 3.92, 12.559, 4),
    ("BC-5-4-4", 6.35, 5.05, 3.481, 12.475, 4),
    ("BC-4-4-4", 5.45, 5.45, 2.988, 12.471, 4),
    ("BB-7-4-4", 8.4, 4.795, 4.605, 11.903, 5),
    ("BB-6-4-4", 7.55, 5.05, 4.139, 11.866, 5),
    ("BB-5-4-4", 6.7, 5.35, 3.673, 11.819, 5),
    ("BB-4-4-4", 5.8, 5.8, 3.18, 12.025, 5),
    ("DN-7-4-4", 8.8, 5.05, 4.659, 14.895, 5),
    ("DN-6-4-4", 7.95, 5.3, 4.209, 14.822, 5),
    ("DN-5-4-4", 7.05, 5.65, 3.733, 14.937, 5),
    ("DN-4-4-4", 6.05, 6.05, 3.203, 14.697, 5),
    ("SD-7-4-4", 9.2, 5.25, 4.871, 16.83, 5),
    ("SD-6-4-4", 8.3, 5.55, 4.395, 16.968, 5),
    ("SD-5-4-4", 7.35, 5.85, 3.892, 16.694, 5),
    ("SD-4-4-4", 6.35, 6.35, 3.362, 16.994, 5),
    ("LV-7-4-4", 9.55, 5.45, 5.057, 15.689, 6),
    ("LV-6-4-4", 8.6, 5.75, 4.554, 15.726, 6),
    ("LV-5-4-4", 7.6, 6.1, 4.024, 15.641, 6),
    ("LV-4-4-4", 6.55, 6.55, 3.468, 15.542, 6),
    ("TT-7-4-4", 9.8, 5.6, 5.563, 14.57, 6),
    ("TT-6-4-4", 8.85, 5.9, 5.024, 14.605, 6),
    ("TT-5-4-4", 7.85, 6.3, 4.456, 14.771, 6),
    ("TT-4-4-4", 6.75, 6.75, 3.832, 14.58, 6)
]

for values in data:
    name, length, width, qVal, engineLength, engineCount = values
    midpoint = (length + qVal + engineLength) / 2 - length

    bpy.ops.wm.read_homefile(app_template="")
    bpy.data.scenes['Scene'].render.film_transparent = True
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    bpy.ops.object.empty_add()

    bpy.ops.mesh.primitive_uv_sphere_add()
    bpy.data.objects['Sphere'].name = 'Hull'
    bpy.data.objects['Hull'].scale[0] = length
    bpy.data.objects['Hull'].scale[1] = width
    bpy.data.objects['Hull'].scale[2] = width
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.bisect(plane_co=(qVal, 0.0, 0.0), plane_no=(1, 0, 0), use_fill=True, clear_outer=True)
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.transform_apply()

    bpy.ops.mesh.primitive_cylinder_add()
    bpy.data.objects['Cylinder'].name = 'Engine'
    bpy.data.objects['Engine'].scale[0] = 1.5 / 2
    bpy.data.objects['Engine'].scale[1] = 1.5 / 2
    bpy.data.objects['Engine'].scale[2] = engineLength / 2
    bpy.data.objects['Engine'].rotation_euler[1] = -math.pi / 2
    bpy.data.objects['Engine'].location[0] = qVal + engineLength / 2
    bpy.data.objects['Engine'].location[2] = 0.75
    bpy.ops.object.transform_apply()

    bpy.ops.object.modifier_add(type='ARRAY')
    bpy.data.objects['Engine'].modifiers['Array'].count = engineCount
    bpy.data.objects['Engine'].modifiers['Array'].use_relative_offset = False
    bpy.data.objects['Engine'].modifiers['Array'].use_object_offset = True
    bpy.data.objects['Engine'].modifiers['Array'].offset_object = bpy.data.objects['Empty']
    bpy.data.objects['Empty'].rotation_euler[0] = math.pi * 2 / engineCount

    bpy.ops.object.light_add(location=(-20, -20, 20))
    bpy.data.lights['Point'].energy = 10000
    bpy.ops.object.light_add(location=(20, -20, 20))
    bpy.data.lights['Point.001'].energy = 6000

    bpy.ops.object.camera_add(location=(midpoint, 0, 20))
    bpy.data.cameras['Camera.001'].type = 'ORTHO'
    bpy.data.cameras['Camera.001'].ortho_scale = 40

    bpy.ops.object.camera_add(location=(midpoint, -20, 0))
    bpy.data.objects['Camera.001'].rotation_euler[0] = math.pi / 2
    bpy.data.cameras['Camera.002'].type = 'ORTHO'
    bpy.data.cameras['Camera.002'].ortho_scale = 40

    bpy.data.scenes['Scene'].camera = bpy.data.objects['Camera']
    output_file = f"D:\\senorpez\\OneDrive\\Documents\\SS Renders\\{name}-Top.png"
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.render.image_settings.file_format = "PNG"
    bpy.ops.render.render(write_still=True)
    bpy.data.images["Render Result"].save_render(output_file)

    bpy.data.scenes['Scene'].camera = bpy.data.objects['Camera.001']
    output_file = f"D:\\senorpez\\OneDrive\\Documents\\SS Renders\\{name}-Side.png"
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.render.image_settings.file_format = "PNG"
    bpy.ops.render.render(write_still=True)
    bpy.data.images["Render Result"].save_render(output_file)

    output_file = f"D:\\senorpez\\OneDrive\\Documents\\SS Renders\\{name}.blend"
    bpy.ops.wm.save_mainfile(filepath = output_file)
