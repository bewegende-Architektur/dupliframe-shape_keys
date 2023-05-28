import bpy

# get object to work with
active_obj = bpy.context.active_object

# get name of active object
active_obj_name = active_obj.name_full

# define the base object
# (to work with the initial obj always)
base_obj = bpy.data.objects[active_obj_name]

# get start and end
start = bpy.context.scene.frame_start
end = bpy.context.scene.frame_end

# iterate trough frames
for frame in range(start, end):
    # change frame
    bpy.context.scene.frame_current = frame
        
    # copy base object
    new_obj = base_obj.copy()
    
    # copy properties
    new_obj.data = base_obj.data.copy()
    new_obj.animation_data.action = base_obj.animation_data.action.copy()
    
    # link to scene
    bpy.context.collection.objects.link(new_obj)
    
    # apply keyframes
    new_obj.animation_data_clear()
    
    # update scene
    bpy.context.view_layer.update()
    
    # select new object
    new_obj.select_set(True)
    
    # check for shape keys
    if new_obj.data.shape_keys:
        # create mix of current keys
        new_obj.shape_key_add(name='mix', from_mix=True)
        
        # delte keys
        for shapeKey in new_obj.data.shape_keys.key_blocks:
            new_obj.shape_key_remove(shapeKey)
    
    # copy material
    mat = new_obj.active_material
    if mat:
        new_mat = mat.copy()
        new_obj.active_material = new_mat
    
        # delete keyframes of material
        new_mat.animation_data_clear()
