# PhysicsServer3D

# PhysicsServer3D
Inherits:Object
Inherited By:PhysicsServer3DExtension
A server interface for low-level 3D physics access.

## Description
PhysicsServer3D is the server responsible for all 3D physics. It can directly create and manipulate all physics objects:
- Aspaceis a self-contained world for a physics simulation. It contains bodies, areas, and joints. Its state can be queried for collision and intersection information, and several parameters of the simulation can be modified.
Aspaceis a self-contained world for a physics simulation. It contains bodies, areas, and joints. Its state can be queried for collision and intersection information, and several parameters of the simulation can be modified.
- Ashapeis a geometric shape such as a sphere, a box, a cylinder, or a polygon. It can be used for collision detection by adding it to a body/area, possibly with an extra transformation relative to the body/area's origin. Bodies/areas can have multiple (transformed) shapes added to them, and a single shape can be added to bodies/areas multiple times with different local transformations.
Ashapeis a geometric shape such as a sphere, a box, a cylinder, or a polygon. It can be used for collision detection by adding it to a body/area, possibly with an extra transformation relative to the body/area's origin. Bodies/areas can have multiple (transformed) shapes added to them, and a single shape can be added to bodies/areas multiple times with different local transformations.
- Abodyis a physical object which can be in static, kinematic, or rigid mode. Its state (such as position and velocity) can be queried and updated. A force integration callback can be set to customize the body's physics.
Abodyis a physical object which can be in static, kinematic, or rigid mode. Its state (such as position and velocity) can be queried and updated. A force integration callback can be set to customize the body's physics.
- Anareais a region in space which can be used to detect bodies and areas entering and exiting it. A body monitoring callback can be set to report entering/exiting body shapes, and similarly an area monitoring callback can be set. Gravity and damping can be overridden within the area by setting area parameters.
Anareais a region in space which can be used to detect bodies and areas entering and exiting it. A body monitoring callback can be set to report entering/exiting body shapes, and similarly an area monitoring callback can be set. Gravity and damping can be overridden within the area by setting area parameters.
- Ajointis a constraint, either between two bodies or on one body relative to a point. Parameters such as the joint bias and the rest length of a spring joint can be adjusted.
Ajointis a constraint, either between two bodies or on one body relative to a point. Parameters such as the joint bias and the rest length of a spring joint can be adjusted.
Physics objects inPhysicsServer3Dmay be created and manipulated independently; they do not have to be tied to nodes in the scene tree.
Note:All the 3D physics nodes use the physics server internally. Adding a physics node to the scene tree will cause a corresponding physics object to be created in the physics server. A rigid body node registers a callback that updates the node's transform with the transform of the respective body object in the physics server (every physics update). An area node registers a callback to inform the area node about overlaps with the respective area object in the physics server. The raycast node queries the direct state of the relevant space in the physics server.

## Methods

| void | area_add_shape(area:RID, shape:RID, transform:Transform3D= Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), disabled:bool= false) |
|---|---|
| void | area_attach_object_instance_id(area:RID, id:int) |
| void | area_clear_shapes(area:RID) |
| RID | area_create() |
| int | area_get_collision_layer(area:RID)const |
| int | area_get_collision_mask(area:RID)const |
| int | area_get_object_instance_id(area:RID)const |
| Variant | area_get_param(area:RID, param:AreaParameter)const |
| RID | area_get_shape(area:RID, shape_idx:int)const |
| int | area_get_shape_count(area:RID)const |
| Transform3D | area_get_shape_transform(area:RID, shape_idx:int)const |
| RID | area_get_space(area:RID)const |
| Transform3D | area_get_transform(area:RID)const |
| void | area_remove_shape(area:RID, shape_idx:int) |
| void | area_set_area_monitor_callback(area:RID, callback:Callable) |
| void | area_set_collision_layer(area:RID, layer:int) |
| void | area_set_collision_mask(area:RID, mask:int) |
| void | area_set_monitor_callback(area:RID, callback:Callable) |
| void | area_set_monitorable(area:RID, monitorable:bool) |
| void | area_set_param(area:RID, param:AreaParameter, value:Variant) |
| void | area_set_ray_pickable(area:RID, enable:bool) |
| void | area_set_shape(area:RID, shape_idx:int, shape:RID) |
| void | area_set_shape_disabled(area:RID, shape_idx:int, disabled:bool) |
| void | area_set_shape_transform(area:RID, shape_idx:int, transform:Transform3D) |
| void | area_set_space(area:RID, space:RID) |
| void | area_set_transform(area:RID, transform:Transform3D) |
| void | body_add_collision_exception(body:RID, excepted_body:RID) |
| void | body_add_constant_central_force(body:RID, force:Vector3) |
| void | body_add_constant_force(body:RID, force:Vector3, position:Vector3= Vector3(0, 0, 0)) |
| void | body_add_constant_torque(body:RID, torque:Vector3) |
| void | body_add_shape(body:RID, shape:RID, transform:Transform3D= Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), disabled:bool= false) |
| void | body_apply_central_force(body:RID, force:Vector3) |
| void | body_apply_central_impulse(body:RID, impulse:Vector3) |
| void | body_apply_force(body:RID, force:Vector3, position:Vector3= Vector3(0, 0, 0)) |
| void | body_apply_impulse(body:RID, impulse:Vector3, position:Vector3= Vector3(0, 0, 0)) |
| void | body_apply_torque(body:RID, torque:Vector3) |
| void | body_apply_torque_impulse(body:RID, impulse:Vector3) |
| void | body_attach_object_instance_id(body:RID, id:int) |
| void | body_clear_shapes(body:RID) |
| RID | body_create() |
| int | body_get_collision_layer(body:RID)const |
| int | body_get_collision_mask(body:RID)const |
| float | body_get_collision_priority(body:RID)const |
| Vector3 | body_get_constant_force(body:RID)const |
| Vector3 | body_get_constant_torque(body:RID)const |
| PhysicsDirectBodyState3D | body_get_direct_state(body:RID) |
| int | body_get_max_contacts_reported(body:RID)const |
| BodyMode | body_get_mode(body:RID)const |
| int | body_get_object_instance_id(body:RID)const |
| Variant | body_get_param(body:RID, param:BodyParameter)const |
| RID | body_get_shape(body:RID, shape_idx:int)const |
| int | body_get_shape_count(body:RID)const |
| Transform3D | body_get_shape_transform(body:RID, shape_idx:int)const |
| RID | body_get_space(body:RID)const |
| Variant | body_get_state(body:RID, state:BodyState)const |
| bool | body_is_axis_locked(body:RID, axis:BodyAxis)const |
| bool | body_is_continuous_collision_detection_enabled(body:RID)const |
| bool | body_is_omitting_force_integration(body:RID)const |
| void | body_remove_collision_exception(body:RID, excepted_body:RID) |
| void | body_remove_shape(body:RID, shape_idx:int) |
| void | body_reset_mass_properties(body:RID) |
| void | body_set_axis_lock(body:RID, axis:BodyAxis, lock:bool) |
| void | body_set_axis_velocity(body:RID, axis_velocity:Vector3) |
| void | body_set_collision_layer(body:RID, layer:int) |
| void | body_set_collision_mask(body:RID, mask:int) |
| void | body_set_collision_priority(body:RID, priority:float) |
| void | body_set_constant_force(body:RID, force:Vector3) |
| void | body_set_constant_torque(body:RID, torque:Vector3) |
| void | body_set_enable_continuous_collision_detection(body:RID, enable:bool) |
| void | body_set_force_integration_callback(body:RID, callable:Callable, userdata:Variant= null) |
| void | body_set_max_contacts_reported(body:RID, amount:int) |
| void | body_set_mode(body:RID, mode:BodyMode) |
| void | body_set_omit_force_integration(body:RID, enable:bool) |
| void | body_set_param(body:RID, param:BodyParameter, value:Variant) |
| void | body_set_ray_pickable(body:RID, enable:bool) |
| void | body_set_shape(body:RID, shape_idx:int, shape:RID) |
| void | body_set_shape_disabled(body:RID, shape_idx:int, disabled:bool) |
| void | body_set_shape_transform(body:RID, shape_idx:int, transform:Transform3D) |
| void | body_set_space(body:RID, space:RID) |
| void | body_set_state(body:RID, state:BodyState, value:Variant) |
| void | body_set_state_sync_callback(body:RID, callable:Callable) |
| bool | body_test_motion(body:RID, parameters:PhysicsTestMotionParameters3D, result:PhysicsTestMotionResult3D= null) |
| RID | box_shape_create() |
| RID | capsule_shape_create() |
| RID | concave_polygon_shape_create() |
| float | cone_twist_joint_get_param(joint:RID, param:ConeTwistJointParam)const |
| void | cone_twist_joint_set_param(joint:RID, param:ConeTwistJointParam, value:float) |
| RID | convex_polygon_shape_create() |
| RID | custom_shape_create() |
| RID | cylinder_shape_create() |
| void | free_rid(rid:RID) |
| bool | generic_6dof_joint_get_flag(joint:RID, axis:Axis, flag:G6DOFJointAxisFlag)const |
| float | generic_6dof_joint_get_param(joint:RID, axis:Axis, param:G6DOFJointAxisParam)const |
| void | generic_6dof_joint_set_flag(joint:RID, axis:Axis, flag:G6DOFJointAxisFlag, enable:bool) |
| void | generic_6dof_joint_set_param(joint:RID, axis:Axis, param:G6DOFJointAxisParam, value:float) |
| int | get_process_info(process_info:ProcessInfo) |
| RID | heightmap_shape_create() |
| bool | hinge_joint_get_flag(joint:RID, flag:HingeJointFlag)const |
| float | hinge_joint_get_param(joint:RID, param:HingeJointParam)const |
| void | hinge_joint_set_flag(joint:RID, flag:HingeJointFlag, enabled:bool) |
| void | hinge_joint_set_param(joint:RID, param:HingeJointParam, value:float) |
| void | joint_clear(joint:RID) |
| RID | joint_create() |
| void | joint_disable_collisions_between_bodies(joint:RID, disable:bool) |
| int | joint_get_solver_priority(joint:RID)const |
| JointType | joint_get_type(joint:RID)const |
| bool | joint_is_disabled_collisions_between_bodies(joint:RID)const |
| void | joint_make_cone_twist(joint:RID, body_A:RID, local_ref_A:Transform3D, body_B:RID, local_ref_B:Transform3D) |
| void | joint_make_generic_6dof(joint:RID, body_A:RID, local_ref_A:Transform3D, body_B:RID, local_ref_B:Transform3D) |
| void | joint_make_hinge(joint:RID, body_A:RID, hinge_A:Transform3D, body_B:RID, hinge_B:Transform3D) |
| void | joint_make_pin(joint:RID, body_A:RID, local_A:Vector3, body_B:RID, local_B:Vector3) |
| void | joint_make_slider(joint:RID, body_A:RID, local_ref_A:Transform3D, body_B:RID, local_ref_B:Transform3D) |
| void | joint_set_solver_priority(joint:RID, priority:int) |
| Vector3 | pin_joint_get_local_a(joint:RID)const |
| Vector3 | pin_joint_get_local_b(joint:RID)const |
| float | pin_joint_get_param(joint:RID, param:PinJointParam)const |
| void | pin_joint_set_local_a(joint:RID, local_A:Vector3) |
| void | pin_joint_set_local_b(joint:RID, local_B:Vector3) |
| void | pin_joint_set_param(joint:RID, param:PinJointParam, value:float) |
| RID | separation_ray_shape_create() |
| void | set_active(active:bool) |
| Variant | shape_get_data(shape:RID)const |
| float | shape_get_margin(shape:RID)const |
| ShapeType | shape_get_type(shape:RID)const |
| void | shape_set_data(shape:RID, data:Variant) |
| void | shape_set_margin(shape:RID, margin:float) |
| float | slider_joint_get_param(joint:RID, param:SliderJointParam)const |
| void | slider_joint_set_param(joint:RID, param:SliderJointParam, value:float) |
| void | soft_body_add_collision_exception(body:RID, body_b:RID) |
| void | soft_body_apply_central_force(body:RID, force:Vector3) |
| void | soft_body_apply_central_impulse(body:RID, impulse:Vector3) |
| void | soft_body_apply_point_force(body:RID, point_index:int, force:Vector3) |
| void | soft_body_apply_point_impulse(body:RID, point_index:int, impulse:Vector3) |
| RID | soft_body_create() |
| AABB | soft_body_get_bounds(body:RID)const |
| int | soft_body_get_collision_layer(body:RID)const |
| int | soft_body_get_collision_mask(body:RID)const |
| float | soft_body_get_damping_coefficient(body:RID)const |
| float | soft_body_get_drag_coefficient(body:RID)const |
| float | soft_body_get_linear_stiffness(body:RID)const |
| Vector3 | soft_body_get_point_global_position(body:RID, point_index:int)const |
| float | soft_body_get_pressure_coefficient(body:RID)const |
| float | soft_body_get_shrinking_factor(body:RID)const |
| int | soft_body_get_simulation_precision(body:RID)const |
| RID | soft_body_get_space(body:RID)const |
| Variant | soft_body_get_state(body:RID, state:BodyState)const |
| float | soft_body_get_total_mass(body:RID)const |
| bool | soft_body_is_point_pinned(body:RID, point_index:int)const |
| void | soft_body_move_point(body:RID, point_index:int, global_position:Vector3) |
| void | soft_body_pin_point(body:RID, point_index:int, pin:bool) |
| void | soft_body_remove_all_pinned_points(body:RID) |
| void | soft_body_remove_collision_exception(body:RID, body_b:RID) |
| void | soft_body_set_collision_layer(body:RID, layer:int) |
| void | soft_body_set_collision_mask(body:RID, mask:int) |
| void | soft_body_set_damping_coefficient(body:RID, damping_coefficient:float) |
| void | soft_body_set_drag_coefficient(body:RID, drag_coefficient:float) |
| void | soft_body_set_linear_stiffness(body:RID, stiffness:float) |
| void | soft_body_set_mesh(body:RID, mesh:RID) |
| void | soft_body_set_pressure_coefficient(body:RID, pressure_coefficient:float) |
| void | soft_body_set_ray_pickable(body:RID, enable:bool) |
| void | soft_body_set_shrinking_factor(body:RID, shrinking_factor:float) |
| void | soft_body_set_simulation_precision(body:RID, simulation_precision:int) |
| void | soft_body_set_space(body:RID, space:RID) |
| void | soft_body_set_state(body:RID, state:BodyState, variant:Variant) |
| void | soft_body_set_total_mass(body:RID, total_mass:float) |
| void | soft_body_set_transform(body:RID, transform:Transform3D) |
| void | soft_body_update_rendering_server(body:RID, rendering_server_handler:PhysicsServer3DRenderingServerHandler) |
| RID | space_create() |
| PhysicsDirectSpaceState3D | space_get_direct_state(space:RID) |
| float | space_get_param(space:RID, param:SpaceParameter)const |
| bool | space_is_active(space:RID)const |
| void | space_set_active(space:RID, active:bool) |
| void | space_set_param(space:RID, param:SpaceParameter, value:float) |
| RID | sphere_shape_create() |
| RID | world_boundary_shape_create() |

void
area_add_shape(area:RID, shape:RID, transform:Transform3D= Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), disabled:bool= false)
void
area_attach_object_instance_id(area:RID, id:int)
void
area_clear_shapes(area:RID)
area_create()
area_get_collision_layer(area:RID)const
area_get_collision_mask(area:RID)const
area_get_object_instance_id(area:RID)const
Variant
area_get_param(area:RID, param:AreaParameter)const
area_get_shape(area:RID, shape_idx:int)const
area_get_shape_count(area:RID)const
Transform3D
area_get_shape_transform(area:RID, shape_idx:int)const
area_get_space(area:RID)const
Transform3D
area_get_transform(area:RID)const
void
area_remove_shape(area:RID, shape_idx:int)
void
area_set_area_monitor_callback(area:RID, callback:Callable)
void
area_set_collision_layer(area:RID, layer:int)
void
area_set_collision_mask(area:RID, mask:int)
void
area_set_monitor_callback(area:RID, callback:Callable)
void
area_set_monitorable(area:RID, monitorable:bool)
void
area_set_param(area:RID, param:AreaParameter, value:Variant)
void
area_set_ray_pickable(area:RID, enable:bool)
void
area_set_shape(area:RID, shape_idx:int, shape:RID)
void
area_set_shape_disabled(area:RID, shape_idx:int, disabled:bool)
void
area_set_shape_transform(area:RID, shape_idx:int, transform:Transform3D)
void
area_set_space(area:RID, space:RID)
void
area_set_transform(area:RID, transform:Transform3D)
void
body_add_collision_exception(body:RID, excepted_body:RID)
void
body_add_constant_central_force(body:RID, force:Vector3)
void
body_add_constant_force(body:RID, force:Vector3, position:Vector3= Vector3(0, 0, 0))
void
body_add_constant_torque(body:RID, torque:Vector3)
void
body_add_shape(body:RID, shape:RID, transform:Transform3D= Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), disabled:bool= false)
void
body_apply_central_force(body:RID, force:Vector3)
void
body_apply_central_impulse(body:RID, impulse:Vector3)
void
body_apply_force(body:RID, force:Vector3, position:Vector3= Vector3(0, 0, 0))
void
body_apply_impulse(body:RID, impulse:Vector3, position:Vector3= Vector3(0, 0, 0))
void
body_apply_torque(body:RID, torque:Vector3)
void
body_apply_torque_impulse(body:RID, impulse:Vector3)
void
body_attach_object_instance_id(body:RID, id:int)
void
body_clear_shapes(body:RID)
body_create()
body_get_collision_layer(body:RID)const
body_get_collision_mask(body:RID)const
float
body_get_collision_priority(body:RID)const
Vector3
body_get_constant_force(body:RID)const
Vector3
body_get_constant_torque(body:RID)const
PhysicsDirectBodyState3D
body_get_direct_state(body:RID)
body_get_max_contacts_reported(body:RID)const
BodyMode
body_get_mode(body:RID)const
body_get_object_instance_id(body:RID)const
Variant
body_get_param(body:RID, param:BodyParameter)const
body_get_shape(body:RID, shape_idx:int)const
body_get_shape_count(body:RID)const
Transform3D
body_get_shape_transform(body:RID, shape_idx:int)const
body_get_space(body:RID)const
Variant
body_get_state(body:RID, state:BodyState)const
bool
body_is_axis_locked(body:RID, axis:BodyAxis)const
bool
body_is_continuous_collision_detection_enabled(body:RID)const
bool
body_is_omitting_force_integration(body:RID)const
void
body_remove_collision_exception(body:RID, excepted_body:RID)
void
body_remove_shape(body:RID, shape_idx:int)
void
body_reset_mass_properties(body:RID)
void
body_set_axis_lock(body:RID, axis:BodyAxis, lock:bool)
void
body_set_axis_velocity(body:RID, axis_velocity:Vector3)
void
body_set_collision_layer(body:RID, layer:int)
void
body_set_collision_mask(body:RID, mask:int)
void
body_set_collision_priority(body:RID, priority:float)
void
body_set_constant_force(body:RID, force:Vector3)
void
body_set_constant_torque(body:RID, torque:Vector3)
void
body_set_enable_continuous_collision_detection(body:RID, enable:bool)
void
body_set_force_integration_callback(body:RID, callable:Callable, userdata:Variant= null)
void
body_set_max_contacts_reported(body:RID, amount:int)
void
body_set_mode(body:RID, mode:BodyMode)
void
body_set_omit_force_integration(body:RID, enable:bool)
void
body_set_param(body:RID, param:BodyParameter, value:Variant)
void
body_set_ray_pickable(body:RID, enable:bool)
void
body_set_shape(body:RID, shape_idx:int, shape:RID)
void
body_set_shape_disabled(body:RID, shape_idx:int, disabled:bool)
void
body_set_shape_transform(body:RID, shape_idx:int, transform:Transform3D)
void
body_set_space(body:RID, space:RID)
void
body_set_state(body:RID, state:BodyState, value:Variant)
void
body_set_state_sync_callback(body:RID, callable:Callable)
bool
body_test_motion(body:RID, parameters:PhysicsTestMotionParameters3D, result:PhysicsTestMotionResult3D= null)
box_shape_create()
capsule_shape_create()
concave_polygon_shape_create()
float
cone_twist_joint_get_param(joint:RID, param:ConeTwistJointParam)const
void
cone_twist_joint_set_param(joint:RID, param:ConeTwistJointParam, value:float)
convex_polygon_shape_create()
custom_shape_create()
cylinder_shape_create()
void
free_rid(rid:RID)
bool
generic_6dof_joint_get_flag(joint:RID, axis:Axis, flag:G6DOFJointAxisFlag)const
float
generic_6dof_joint_get_param(joint:RID, axis:Axis, param:G6DOFJointAxisParam)const
void
generic_6dof_joint_set_flag(joint:RID, axis:Axis, flag:G6DOFJointAxisFlag, enable:bool)
void
generic_6dof_joint_set_param(joint:RID, axis:Axis, param:G6DOFJointAxisParam, value:float)
get_process_info(process_info:ProcessInfo)
heightmap_shape_create()
bool
hinge_joint_get_flag(joint:RID, flag:HingeJointFlag)const
float
hinge_joint_get_param(joint:RID, param:HingeJointParam)const
void
hinge_joint_set_flag(joint:RID, flag:HingeJointFlag, enabled:bool)
void
hinge_joint_set_param(joint:RID, param:HingeJointParam, value:float)
void
joint_clear(joint:RID)
joint_create()
void
joint_disable_collisions_between_bodies(joint:RID, disable:bool)
joint_get_solver_priority(joint:RID)const
JointType
joint_get_type(joint:RID)const
bool
joint_is_disabled_collisions_between_bodies(joint:RID)const
void
joint_make_cone_twist(joint:RID, body_A:RID, local_ref_A:Transform3D, body_B:RID, local_ref_B:Transform3D)
void
joint_make_generic_6dof(joint:RID, body_A:RID, local_ref_A:Transform3D, body_B:RID, local_ref_B:Transform3D)
void
joint_make_hinge(joint:RID, body_A:RID, hinge_A:Transform3D, body_B:RID, hinge_B:Transform3D)
void
joint_make_pin(joint:RID, body_A:RID, local_A:Vector3, body_B:RID, local_B:Vector3)
void
joint_make_slider(joint:RID, body_A:RID, local_ref_A:Transform3D, body_B:RID, local_ref_B:Transform3D)
void
joint_set_solver_priority(joint:RID, priority:int)
Vector3
pin_joint_get_local_a(joint:RID)const
Vector3
pin_joint_get_local_b(joint:RID)const
float
pin_joint_get_param(joint:RID, param:PinJointParam)const
void
pin_joint_set_local_a(joint:RID, local_A:Vector3)
void
pin_joint_set_local_b(joint:RID, local_B:Vector3)
void
pin_joint_set_param(joint:RID, param:PinJointParam, value:float)
separation_ray_shape_create()
void
set_active(active:bool)
Variant
shape_get_data(shape:RID)const
float
shape_get_margin(shape:RID)const
ShapeType
shape_get_type(shape:RID)const
void
shape_set_data(shape:RID, data:Variant)
void
shape_set_margin(shape:RID, margin:float)
float
slider_joint_get_param(joint:RID, param:SliderJointParam)const
void
slider_joint_set_param(joint:RID, param:SliderJointParam, value:float)
void
soft_body_add_collision_exception(body:RID, body_b:RID)
void
soft_body_apply_central_force(body:RID, force:Vector3)
void
soft_body_apply_central_impulse(body:RID, impulse:Vector3)
void
soft_body_apply_point_force(body:RID, point_index:int, force:Vector3)
void
soft_body_apply_point_impulse(body:RID, point_index:int, impulse:Vector3)
soft_body_create()
AABB
soft_body_get_bounds(body:RID)const
soft_body_get_collision_layer(body:RID)const
soft_body_get_collision_mask(body:RID)const
float
soft_body_get_damping_coefficient(body:RID)const
float
soft_body_get_drag_coefficient(body:RID)const
float
soft_body_get_linear_stiffness(body:RID)const
Vector3
soft_body_get_point_global_position(body:RID, point_index:int)const
float
soft_body_get_pressure_coefficient(body:RID)const
float
soft_body_get_shrinking_factor(body:RID)const
soft_body_get_simulation_precision(body:RID)const
soft_body_get_space(body:RID)const
Variant
soft_body_get_state(body:RID, state:BodyState)const
float
soft_body_get_total_mass(body:RID)const
bool
soft_body_is_point_pinned(body:RID, point_index:int)const
void
soft_body_move_point(body:RID, point_index:int, global_position:Vector3)
void
soft_body_pin_point(body:RID, point_index:int, pin:bool)
void
soft_body_remove_all_pinned_points(body:RID)
void
soft_body_remove_collision_exception(body:RID, body_b:RID)
void
soft_body_set_collision_layer(body:RID, layer:int)
void
soft_body_set_collision_mask(body:RID, mask:int)
void
soft_body_set_damping_coefficient(body:RID, damping_coefficient:float)
void
soft_body_set_drag_coefficient(body:RID, drag_coefficient:float)
void
soft_body_set_linear_stiffness(body:RID, stiffness:float)
void
soft_body_set_mesh(body:RID, mesh:RID)
void
soft_body_set_pressure_coefficient(body:RID, pressure_coefficient:float)
void
soft_body_set_ray_pickable(body:RID, enable:bool)
void
soft_body_set_shrinking_factor(body:RID, shrinking_factor:float)
void
soft_body_set_simulation_precision(body:RID, simulation_precision:int)
void
soft_body_set_space(body:RID, space:RID)
void
soft_body_set_state(body:RID, state:BodyState, variant:Variant)
void
soft_body_set_total_mass(body:RID, total_mass:float)
void
soft_body_set_transform(body:RID, transform:Transform3D)
void
soft_body_update_rendering_server(body:RID, rendering_server_handler:PhysicsServer3DRenderingServerHandler)
space_create()
PhysicsDirectSpaceState3D
space_get_direct_state(space:RID)
float
space_get_param(space:RID, param:SpaceParameter)const
bool
space_is_active(space:RID)const
void
space_set_active(space:RID, active:bool)
void
space_set_param(space:RID, param:SpaceParameter, value:float)
sphere_shape_create()
world_boundary_shape_create()

## Enumerations
enumJointType:🔗
JointTypeJOINT_TYPE_PIN=0
TheJoint3Dis aPinJoint3D.
JointTypeJOINT_TYPE_HINGE=1
TheJoint3Dis aHingeJoint3D.
JointTypeJOINT_TYPE_SLIDER=2
TheJoint3Dis aSliderJoint3D.
JointTypeJOINT_TYPE_CONE_TWIST=3
TheJoint3Dis aConeTwistJoint3D.
JointTypeJOINT_TYPE_6DOF=4
TheJoint3Dis aGeneric6DOFJoint3D.
JointTypeJOINT_TYPE_MAX=5
Represents the size of theJointTypeenum.
enumPinJointParam:🔗
PinJointParamPIN_JOINT_BIAS=0
The strength with which the pinned objects try to stay in positional relation to each other.
The higher, the stronger.
PinJointParamPIN_JOINT_DAMPING=1
The strength with which the pinned objects try to stay in velocity relation to each other.
The higher, the stronger.
PinJointParamPIN_JOINT_IMPULSE_CLAMP=2
If above 0, this value is the maximum value for an impulse that this Joint3D puts on its ends.
enumHingeJointParam:🔗
HingeJointParamHINGE_JOINT_BIAS=0
The speed with which the two bodies get pulled together when they move in different directions.
HingeJointParamHINGE_JOINT_LIMIT_UPPER=1
The maximum rotation across the Hinge.
HingeJointParamHINGE_JOINT_LIMIT_LOWER=2
The minimum rotation across the Hinge.
HingeJointParamHINGE_JOINT_LIMIT_BIAS=3
The speed with which the rotation across the axis perpendicular to the hinge gets corrected.
HingeJointParamHINGE_JOINT_LIMIT_SOFTNESS=4
There is currently no description for this enum. Please help us bycontributing one!
HingeJointParamHINGE_JOINT_LIMIT_RELAXATION=5
The lower this value, the more the rotation gets slowed down.
HingeJointParamHINGE_JOINT_MOTOR_TARGET_VELOCITY=6
Target speed for the motor.
HingeJointParamHINGE_JOINT_MOTOR_MAX_IMPULSE=7
Maximum acceleration for the motor.
enumHingeJointFlag:🔗
HingeJointFlagHINGE_JOINT_FLAG_USE_LIMIT=0
Iftrue, the Hinge has a maximum and a minimum rotation.
HingeJointFlagHINGE_JOINT_FLAG_ENABLE_MOTOR=1
Iftrue, a motor turns the Hinge.
enumSliderJointParam:🔗
SliderJointParamSLIDER_JOINT_LINEAR_LIMIT_UPPER=0
The maximum difference between the pivot points on their X axis before damping happens.
SliderJointParamSLIDER_JOINT_LINEAR_LIMIT_LOWER=1
The minimum difference between the pivot points on their X axis before damping happens.
SliderJointParamSLIDER_JOINT_LINEAR_LIMIT_SOFTNESS=2
A factor applied to the movement across the slider axis once the limits get surpassed. The lower, the slower the movement.
SliderJointParamSLIDER_JOINT_LINEAR_LIMIT_RESTITUTION=3
The amount of restitution once the limits are surpassed. The lower, the more velocity-energy gets lost.
SliderJointParamSLIDER_JOINT_LINEAR_LIMIT_DAMPING=4
The amount of damping once the slider limits are surpassed.
SliderJointParamSLIDER_JOINT_LINEAR_MOTION_SOFTNESS=5
A factor applied to the movement across the slider axis as long as the slider is in the limits. The lower, the slower the movement.
SliderJointParamSLIDER_JOINT_LINEAR_MOTION_RESTITUTION=6
The amount of restitution inside the slider limits.
SliderJointParamSLIDER_JOINT_LINEAR_MOTION_DAMPING=7
The amount of damping inside the slider limits.
SliderJointParamSLIDER_JOINT_LINEAR_ORTHOGONAL_SOFTNESS=8
A factor applied to the movement across axes orthogonal to the slider.
SliderJointParamSLIDER_JOINT_LINEAR_ORTHOGONAL_RESTITUTION=9
The amount of restitution when movement is across axes orthogonal to the slider.
SliderJointParamSLIDER_JOINT_LINEAR_ORTHOGONAL_DAMPING=10
The amount of damping when movement is across axes orthogonal to the slider.
SliderJointParamSLIDER_JOINT_ANGULAR_LIMIT_UPPER=11
The upper limit of rotation in the slider.
SliderJointParamSLIDER_JOINT_ANGULAR_LIMIT_LOWER=12
The lower limit of rotation in the slider.
SliderJointParamSLIDER_JOINT_ANGULAR_LIMIT_SOFTNESS=13
A factor applied to the all rotation once the limit is surpassed.
SliderJointParamSLIDER_JOINT_ANGULAR_LIMIT_RESTITUTION=14
The amount of restitution of the rotation when the limit is surpassed.
SliderJointParamSLIDER_JOINT_ANGULAR_LIMIT_DAMPING=15
The amount of damping of the rotation when the limit is surpassed.
SliderJointParamSLIDER_JOINT_ANGULAR_MOTION_SOFTNESS=16
A factor that gets applied to the all rotation in the limits.
SliderJointParamSLIDER_JOINT_ANGULAR_MOTION_RESTITUTION=17
The amount of restitution of the rotation in the limits.
SliderJointParamSLIDER_JOINT_ANGULAR_MOTION_DAMPING=18
The amount of damping of the rotation in the limits.
SliderJointParamSLIDER_JOINT_ANGULAR_ORTHOGONAL_SOFTNESS=19
A factor that gets applied to the all rotation across axes orthogonal to the slider.
SliderJointParamSLIDER_JOINT_ANGULAR_ORTHOGONAL_RESTITUTION=20
The amount of restitution of the rotation across axes orthogonal to the slider.
SliderJointParamSLIDER_JOINT_ANGULAR_ORTHOGONAL_DAMPING=21
The amount of damping of the rotation across axes orthogonal to the slider.
SliderJointParamSLIDER_JOINT_MAX=22
Represents the size of theSliderJointParamenum.
enumConeTwistJointParam:🔗
ConeTwistJointParamCONE_TWIST_JOINT_SWING_SPAN=0
Swing is rotation from side to side, around the axis perpendicular to the twist axis.
The swing span defines, how much rotation will not get corrected along the swing axis.
Could be defined as looseness in theConeTwistJoint3D.
If below 0.05, this behavior is locked.
ConeTwistJointParamCONE_TWIST_JOINT_TWIST_SPAN=1
Twist is the rotation around the twist axis, this value defined how far the joint can twist.
Twist is locked if below 0.05.
ConeTwistJointParamCONE_TWIST_JOINT_BIAS=2
The speed with which the swing or twist will take place.
The higher, the faster.
ConeTwistJointParamCONE_TWIST_JOINT_SOFTNESS=3
The ease with which the Joint3D twists, if it's too low, it takes more force to twist the joint.
ConeTwistJointParamCONE_TWIST_JOINT_RELAXATION=4
Defines, how fast the swing- and twist-speed-difference on both sides gets synced.
enumG6DOFJointAxisParam:🔗
G6DOFJointAxisParamG6DOF_JOINT_LINEAR_LOWER_LIMIT=0
The minimum difference between the pivot points' axes.
G6DOFJointAxisParamG6DOF_JOINT_LINEAR_UPPER_LIMIT=1
The maximum difference between the pivot points' axes.
G6DOFJointAxisParamG6DOF_JOINT_LINEAR_LIMIT_SOFTNESS=2
A factor that gets applied to the movement across the axes. The lower, the slower the movement.
G6DOFJointAxisParamG6DOF_JOINT_LINEAR_RESTITUTION=3
The amount of restitution on the axes movement. The lower, the more velocity-energy gets lost.
G6DOFJointAxisParamG6DOF_JOINT_LINEAR_DAMPING=4
The amount of damping that happens at the linear motion across the axes.
G6DOFJointAxisParamG6DOF_JOINT_LINEAR_MOTOR_TARGET_VELOCITY=5
The velocity that the joint's linear motor will attempt to reach.
G6DOFJointAxisParamG6DOF_JOINT_LINEAR_MOTOR_FORCE_LIMIT=6
The maximum force that the linear motor can apply while trying to reach the target velocity.
G6DOFJointAxisParamG6DOF_JOINT_LINEAR_SPRING_STIFFNESS=7
There is currently no description for this enum. Please help us bycontributing one!
G6DOFJointAxisParamG6DOF_JOINT_LINEAR_SPRING_DAMPING=8
There is currently no description for this enum. Please help us bycontributing one!
G6DOFJointAxisParamG6DOF_JOINT_LINEAR_SPRING_EQUILIBRIUM_POINT=9
There is currently no description for this enum. Please help us bycontributing one!
G6DOFJointAxisParamG6DOF_JOINT_ANGULAR_LOWER_LIMIT=10
The minimum rotation in negative direction to break loose and rotate around the axes.
G6DOFJointAxisParamG6DOF_JOINT_ANGULAR_UPPER_LIMIT=11
The minimum rotation in positive direction to break loose and rotate around the axes.
G6DOFJointAxisParamG6DOF_JOINT_ANGULAR_LIMIT_SOFTNESS=12
A factor that gets multiplied onto all rotations across the axes.
G6DOFJointAxisParamG6DOF_JOINT_ANGULAR_DAMPING=13
The amount of rotational damping across the axes. The lower, the more damping occurs.
G6DOFJointAxisParamG6DOF_JOINT_ANGULAR_RESTITUTION=14
The amount of rotational restitution across the axes. The lower, the more restitution occurs.
G6DOFJointAxisParamG6DOF_JOINT_ANGULAR_FORCE_LIMIT=15
The maximum amount of force that can occur, when rotating around the axes.
G6DOFJointAxisParamG6DOF_JOINT_ANGULAR_ERP=16
When correcting the crossing of limits in rotation across the axes, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.
G6DOFJointAxisParamG6DOF_JOINT_ANGULAR_MOTOR_TARGET_VELOCITY=17
Target speed for the motor at the axes.
G6DOFJointAxisParamG6DOF_JOINT_ANGULAR_MOTOR_FORCE_LIMIT=18
Maximum acceleration for the motor at the axes.
G6DOFJointAxisParamG6DOF_JOINT_ANGULAR_SPRING_STIFFNESS=19
There is currently no description for this enum. Please help us bycontributing one!
G6DOFJointAxisParamG6DOF_JOINT_ANGULAR_SPRING_DAMPING=20
There is currently no description for this enum. Please help us bycontributing one!
G6DOFJointAxisParamG6DOF_JOINT_ANGULAR_SPRING_EQUILIBRIUM_POINT=21
There is currently no description for this enum. Please help us bycontributing one!
G6DOFJointAxisParamG6DOF_JOINT_MAX=22
Represents the size of theG6DOFJointAxisParamenum.
enumG6DOFJointAxisFlag:🔗
G6DOFJointAxisFlagG6DOF_JOINT_FLAG_ENABLE_LINEAR_LIMIT=0
If set, linear motion is possible within the given limits.
G6DOFJointAxisFlagG6DOF_JOINT_FLAG_ENABLE_ANGULAR_LIMIT=1
If set, rotational motion is possible.
G6DOFJointAxisFlagG6DOF_JOINT_FLAG_ENABLE_ANGULAR_SPRING=2
There is currently no description for this enum. Please help us bycontributing one!
G6DOFJointAxisFlagG6DOF_JOINT_FLAG_ENABLE_LINEAR_SPRING=3
There is currently no description for this enum. Please help us bycontributing one!
G6DOFJointAxisFlagG6DOF_JOINT_FLAG_ENABLE_MOTOR=4
If set, there is a rotational motor across these axes.
G6DOFJointAxisFlagG6DOF_JOINT_FLAG_ENABLE_LINEAR_MOTOR=5
If set, there is a linear motor on this axis that targets a specific velocity.
G6DOFJointAxisFlagG6DOF_JOINT_FLAG_MAX=6
Represents the size of theG6DOFJointAxisFlagenum.
enumShapeType:🔗
ShapeTypeSHAPE_WORLD_BOUNDARY=0
Constant for creating a world boundary shape (used by theWorldBoundaryShape3Dresource).
ShapeTypeSHAPE_SEPARATION_RAY=1
Constant for creating a separation ray shape (used by theSeparationRayShape3Dresource).
ShapeTypeSHAPE_SPHERE=2
Constant for creating a sphere shape (used by theSphereShape3Dresource).
ShapeTypeSHAPE_BOX=3
Constant for creating a box shape (used by theBoxShape3Dresource).
ShapeTypeSHAPE_CAPSULE=4
Constant for creating a capsule shape (used by theCapsuleShape3Dresource).
ShapeTypeSHAPE_CYLINDER=5
Constant for creating a cylinder shape (used by theCylinderShape3Dresource).
ShapeTypeSHAPE_CONVEX_POLYGON=6
Constant for creating a convex polygon shape (used by theConvexPolygonShape3Dresource).
ShapeTypeSHAPE_CONCAVE_POLYGON=7
Constant for creating a concave polygon (trimesh) shape (used by theConcavePolygonShape3Dresource).
ShapeTypeSHAPE_HEIGHTMAP=8
Constant for creating a heightmap shape (used by theHeightMapShape3Dresource).
ShapeTypeSHAPE_SOFT_BODY=9
Constant used internally for a soft body shape. Any attempt to create this kind of shape results in an error.
ShapeTypeSHAPE_CUSTOM=10
Constant used internally for a custom shape. Any attempt to create this kind of shape results in an error when using Godot Physics or Jolt Physics.
enumAreaParameter:🔗
AreaParameterAREA_PARAM_GRAVITY_OVERRIDE_MODE=0
Constant to set/get gravity override mode in an area. SeeAreaSpaceOverrideModefor possible values.
AreaParameterAREA_PARAM_GRAVITY=1
Constant to set/get gravity strength in an area.
AreaParameterAREA_PARAM_GRAVITY_VECTOR=2
Constant to set/get gravity vector/center in an area.
AreaParameterAREA_PARAM_GRAVITY_IS_POINT=3
Constant to set/get whether the gravity vector of an area is a direction, or a center point.
AreaParameterAREA_PARAM_GRAVITY_POINT_UNIT_DISTANCE=4
Constant to set/get the distance at which the gravity strength is equal to the gravity controlled byAREA_PARAM_GRAVITY. For example, on a planet 100 meters in radius with a surface gravity of 4.0 m/s², set the gravity to 4.0 and the unit distance to 100.0. The gravity will have falloff according to the inverse square law, so in the example, at 200 meters from the center the gravity will be 1.0 m/s² (twice the distance, 1/4th the gravity), at 50 meters it will be 16.0 m/s² (half the distance, 4x the gravity), and so on.
The above is true only when the unit distance is a positive number. When this is set to 0.0, the gravity will be constant regardless of distance.
AreaParameterAREA_PARAM_LINEAR_DAMP_OVERRIDE_MODE=5
Constant to set/get linear damping override mode in an area. SeeAreaSpaceOverrideModefor possible values.
AreaParameterAREA_PARAM_LINEAR_DAMP=6
Constant to set/get the linear damping factor of an area.
AreaParameterAREA_PARAM_ANGULAR_DAMP_OVERRIDE_MODE=7
Constant to set/get angular damping override mode in an area. SeeAreaSpaceOverrideModefor possible values.
AreaParameterAREA_PARAM_ANGULAR_DAMP=8
Constant to set/get the angular damping factor of an area.
AreaParameterAREA_PARAM_PRIORITY=9
Constant to set/get the priority (order of processing) of an area.
AreaParameterAREA_PARAM_WIND_FORCE_MAGNITUDE=10
Constant to set/get the magnitude of area-specific wind force. This wind force only applies toSoftBody3Dnodes. Other physics bodies are currently not affected by wind.
AreaParameterAREA_PARAM_WIND_SOURCE=11
Constant to set/get the 3D vector that specifies the origin from which an area-specific wind blows.
AreaParameterAREA_PARAM_WIND_DIRECTION=12
Constant to set/get the 3D vector that specifies the direction in which an area-specific wind blows.
AreaParameterAREA_PARAM_WIND_ATTENUATION_FACTOR=13
Constant to set/get the exponential rate at which wind force decreases with distance from its origin.
enumAreaSpaceOverrideMode:🔗
AreaSpaceOverrideModeAREA_SPACE_OVERRIDE_DISABLED=0
This area does not affect gravity/damp. These are generally areas that exist only to detect collisions, and objects entering or exiting them.
AreaSpaceOverrideModeAREA_SPACE_OVERRIDE_COMBINE=1
This area adds its gravity/damp values to whatever has been calculated so far. This way, many overlapping areas can combine their physics to make interesting effects.
AreaSpaceOverrideModeAREA_SPACE_OVERRIDE_COMBINE_REPLACE=2
This area adds its gravity/damp values to whatever has been calculated so far. Then stops taking into account the rest of the areas, even the default one.
AreaSpaceOverrideModeAREA_SPACE_OVERRIDE_REPLACE=3
This area replaces any gravity/damp, even the default one, and stops taking into account the rest of the areas.
AreaSpaceOverrideModeAREA_SPACE_OVERRIDE_REPLACE_COMBINE=4
This area replaces any gravity/damp calculated so far, but keeps calculating the rest of the areas, down to the default one.
enumBodyMode:🔗
BodyModeBODY_MODE_STATIC=0
Constant for static bodies. In this mode, a body can be only moved by user code and doesn't collide with other bodies along its path when moved.
BodyModeBODY_MODE_KINEMATIC=1
Constant for kinematic bodies. In this mode, a body can be only moved by user code and collides with other bodies along its path.
BodyModeBODY_MODE_RIGID=2
Constant for rigid bodies. In this mode, a body can be pushed by other bodies and has forces applied.
BodyModeBODY_MODE_RIGID_LINEAR=3
Constant for linear rigid bodies. In this mode, a body can not rotate, and only its linear velocity is affected by external forces.
enumBodyParameter:🔗
BodyParameterBODY_PARAM_BOUNCE=0
Constant to set/get a body's bounce factor.
BodyParameterBODY_PARAM_FRICTION=1
Constant to set/get a body's friction.
BodyParameterBODY_PARAM_MASS=2
Constant to set/get a body's mass.
BodyParameterBODY_PARAM_INERTIA=3
Constant to set/get a body's inertia.
BodyParameterBODY_PARAM_CENTER_OF_MASS=4
Constant to set/get a body's center of mass position in the body's local coordinate system.
BodyParameterBODY_PARAM_GRAVITY_SCALE=5
Constant to set/get a body's gravity multiplier.
BodyParameterBODY_PARAM_LINEAR_DAMP_MODE=6
Constant to set/get a body's linear damping mode. SeeBodyDampModefor possible values.
BodyParameterBODY_PARAM_ANGULAR_DAMP_MODE=7
Constant to set/get a body's angular damping mode. SeeBodyDampModefor possible values.
BodyParameterBODY_PARAM_LINEAR_DAMP=8
Constant to set/get a body's linear damping factor.
BodyParameterBODY_PARAM_ANGULAR_DAMP=9
Constant to set/get a body's angular damping factor.
BodyParameterBODY_PARAM_MAX=10
Represents the size of theBodyParameterenum.
enumBodyDampMode:🔗
BodyDampModeBODY_DAMP_MODE_COMBINE=0
The body's damping value is added to any value set in areas or the default value.
BodyDampModeBODY_DAMP_MODE_REPLACE=1
The body's damping value replaces any value set in areas or the default value.
enumBodyState:🔗
BodyStateBODY_STATE_TRANSFORM=0
Constant to set/get the current transform matrix of the body.
BodyStateBODY_STATE_LINEAR_VELOCITY=1
Constant to set/get the current linear velocity of the body.
BodyStateBODY_STATE_ANGULAR_VELOCITY=2
Constant to set/get the current angular velocity of the body.
BodyStateBODY_STATE_SLEEPING=3
Constant to sleep/wake up a body, or to get whether it is sleeping.
BodyStateBODY_STATE_CAN_SLEEP=4
Constant to set/get whether the body can sleep.
enumAreaBodyStatus:🔗
AreaBodyStatusAREA_BODY_ADDED=0
The value of the first parameter and area callback function receives, when an object enters one of its shapes.
AreaBodyStatusAREA_BODY_REMOVED=1
The value of the first parameter and area callback function receives, when an object exits one of its shapes.
enumProcessInfo:🔗
ProcessInfoINFO_ACTIVE_OBJECTS=0
Constant to get the number of objects that are not sleeping.
ProcessInfoINFO_COLLISION_PAIRS=1
Constant to get the number of possible collisions.
ProcessInfoINFO_ISLAND_COUNT=2
Constant to get the number of space regions where a collision could occur.
enumSpaceParameter:🔗
SpaceParameterSPACE_PARAM_CONTACT_RECYCLE_RADIUS=0
Constant to set/get the maximum distance a pair of bodies has to move before their collision status has to be recalculated.
SpaceParameterSPACE_PARAM_CONTACT_MAX_SEPARATION=1
Constant to set/get the maximum distance a shape can be from another before they are considered separated and the contact is discarded.
SpaceParameterSPACE_PARAM_CONTACT_MAX_ALLOWED_PENETRATION=2
Constant to set/get the maximum distance a shape can penetrate another shape before it is considered a collision.
SpaceParameterSPACE_PARAM_CONTACT_DEFAULT_BIAS=3
Constant to set/get the default solver bias for all physics contacts. A solver bias is a factor controlling how much two objects "rebound", after overlapping, to avoid leaving them in that state because of numerical imprecision.
SpaceParameterSPACE_PARAM_BODY_LINEAR_VELOCITY_SLEEP_THRESHOLD=4
Constant to set/get the threshold linear velocity of activity. A body marked as potentially inactive for both linear and angular velocity will be put to sleep after the time given.
SpaceParameterSPACE_PARAM_BODY_ANGULAR_VELOCITY_SLEEP_THRESHOLD=5
Constant to set/get the threshold angular velocity of activity. A body marked as potentially inactive for both linear and angular velocity will be put to sleep after the time given.
SpaceParameterSPACE_PARAM_BODY_TIME_TO_SLEEP=6
Constant to set/get the maximum time of activity. A body marked as potentially inactive for both linear and angular velocity will be put to sleep after this time.
SpaceParameterSPACE_PARAM_SOLVER_ITERATIONS=7
Constant to set/get the number of solver iterations for contacts and constraints. The greater the number of iterations, the more accurate the collisions and constraints will be. However, a greater number of iterations requires more CPU power, which can decrease performance.
enumBodyAxis:🔗
BodyAxisBODY_AXIS_LINEAR_X=1
There is currently no description for this enum. Please help us bycontributing one!
BodyAxisBODY_AXIS_LINEAR_Y=2
There is currently no description for this enum. Please help us bycontributing one!
BodyAxisBODY_AXIS_LINEAR_Z=4
There is currently no description for this enum. Please help us bycontributing one!
BodyAxisBODY_AXIS_ANGULAR_X=8
There is currently no description for this enum. Please help us bycontributing one!
BodyAxisBODY_AXIS_ANGULAR_Y=16
There is currently no description for this enum. Please help us bycontributing one!
BodyAxisBODY_AXIS_ANGULAR_Z=32
There is currently no description for this enum. Please help us bycontributing one!

## Method Descriptions
voidarea_add_shape(area:RID, shape:RID, transform:Transform3D= Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), disabled:bool= false)🔗
Adds a shape to the area, along with a transform matrix. Shapes are usually referenced by their index, so you should track which shape has a given index.
voidarea_attach_object_instance_id(area:RID, id:int)🔗
Assigns the area to a descendant ofObject, so it can exist in the node tree.
voidarea_clear_shapes(area:RID)🔗
Removes all shapes from an area. It does not delete the shapes, so they can be reassigned later.
RIDarea_create()🔗
Creates a 3D area object in the physics server, and returns theRIDthat identifies it. The default settings for the created area include a collision layer and mask set to1, andmonitorableset tofalse.
Usearea_add_shape()to add shapes to it, usearea_set_transform()to set its transform, and usearea_set_space()to add the area to a space. If you want the area to be detectable usearea_set_monitorable().
intarea_get_collision_layer(area:RID)const🔗
Returns the physics layer or layers an area belongs to.
intarea_get_collision_mask(area:RID)const🔗
Returns the physics layer or layers an area can contact with.
intarea_get_object_instance_id(area:RID)const🔗
Gets the instance ID of the object the area is assigned to.
Variantarea_get_param(area:RID, param:AreaParameter)const🔗
Returns an area parameter value. A list of available parameters is on theAreaParameterconstants.
RIDarea_get_shape(area:RID, shape_idx:int)const🔗
Returns theRIDof the nth shape of an area.
intarea_get_shape_count(area:RID)const🔗
Returns the number of shapes assigned to an area.
Transform3Darea_get_shape_transform(area:RID, shape_idx:int)const🔗
Returns the transform matrix of a shape within an area.
RIDarea_get_space(area:RID)const🔗
Returns the space assigned to the area.
Transform3Darea_get_transform(area:RID)const🔗
Returns the transform matrix for an area.
voidarea_remove_shape(area:RID, shape_idx:int)🔗
Removes a shape from an area. It does not delete the shape, so it can be reassigned later.
voidarea_set_area_monitor_callback(area:RID, callback:Callable)🔗
Sets the area's area monitor callback. This callback will be called when any other (shape of an) area enters or exits (a shape of) the given area, and must take the following five parameters:
- an integerstatus: eitherAREA_BODY_ADDEDorAREA_BODY_REMOVEDdepending on whether the other area's shape entered or exited the area,
an integerstatus: eitherAREA_BODY_ADDEDorAREA_BODY_REMOVEDdepending on whether the other area's shape entered or exited the area,
- anRIDarea_rid: theRIDof the other area that entered or exited the area,
anRIDarea_rid: theRIDof the other area that entered or exited the area,
- an integerinstance_id: theObjectIDattached to the other area,
an integerinstance_id: theObjectIDattached to the other area,
- an integerarea_shape_idx: the index of the shape of the other area that entered or exited the area,
an integerarea_shape_idx: the index of the shape of the other area that entered or exited the area,
- an integerself_shape_idx: the index of the shape of the area where the other area entered or exited.
an integerself_shape_idx: the index of the shape of the area where the other area entered or exited.
By counting (or keeping track of) the shapes that enter and exit, it can be determined if an area (with all its shapes) is entering for the first time or exiting for the last time.
voidarea_set_collision_layer(area:RID, layer:int)🔗
Assigns the area to one or many physics layers.
voidarea_set_collision_mask(area:RID, mask:int)🔗
Sets which physics layers the area will monitor.
voidarea_set_monitor_callback(area:RID, callback:Callable)🔗
Sets the area's body monitor callback. This callback will be called when any other (shape of a) body enters or exits (a shape of) the given area, and must take the following five parameters:
- an integerstatus: eitherAREA_BODY_ADDEDorAREA_BODY_REMOVEDdepending on whether the other body shape entered or exited the area,
an integerstatus: eitherAREA_BODY_ADDEDorAREA_BODY_REMOVEDdepending on whether the other body shape entered or exited the area,
- anRIDbody_rid: theRIDof the body that entered or exited the area,
anRIDbody_rid: theRIDof the body that entered or exited the area,
- an integerinstance_id: theObjectIDattached to the body,
an integerinstance_id: theObjectIDattached to the body,
- an integerbody_shape_idx: the index of the shape of the body that entered or exited the area,
an integerbody_shape_idx: the index of the shape of the body that entered or exited the area,
- an integerself_shape_idx: the index of the shape of the area where the body entered or exited.
an integerself_shape_idx: the index of the shape of the area where the body entered or exited.
By counting (or keeping track of) the shapes that enter and exit, it can be determined if a body (with all its shapes) is entering for the first time or exiting for the last time.
voidarea_set_monitorable(area:RID, monitorable:bool)🔗
There is currently no description for this method. Please help us bycontributing one!
voidarea_set_param(area:RID, param:AreaParameter, value:Variant)🔗
Sets the value for an area parameter. A list of available parameters is on theAreaParameterconstants.
voidarea_set_ray_pickable(area:RID, enable:bool)🔗
Sets object pickable with rays.
voidarea_set_shape(area:RID, shape_idx:int, shape:RID)🔗
Substitutes a given area shape by another. The old shape is selected by its index, the new one by itsRID.
voidarea_set_shape_disabled(area:RID, shape_idx:int, disabled:bool)🔗
There is currently no description for this method. Please help us bycontributing one!
voidarea_set_shape_transform(area:RID, shape_idx:int, transform:Transform3D)🔗
Sets the transform matrix for an area shape.
voidarea_set_space(area:RID, space:RID)🔗
Assigns a space to the area.
voidarea_set_transform(area:RID, transform:Transform3D)🔗
Sets the transform matrix for an area.
voidbody_add_collision_exception(body:RID, excepted_body:RID)🔗
Adds a body to the list of bodies exempt from collisions.
voidbody_add_constant_central_force(body:RID, force:Vector3)🔗
Adds a constant directional force without affecting rotation that keeps being applied over time until cleared withbody_set_constant_force(body,Vector3(0,0,0)).
This is equivalent to usingbody_add_constant_force()at the body's center of mass.
voidbody_add_constant_force(body:RID, force:Vector3, position:Vector3= Vector3(0, 0, 0))🔗
Adds a constant positioned force to the body that keeps being applied over time until cleared withbody_set_constant_force(body,Vector3(0,0,0)).
positionis the offset from the body origin in global coordinates.
voidbody_add_constant_torque(body:RID, torque:Vector3)🔗
Adds a constant rotational force without affecting position that keeps being applied over time until cleared withbody_set_constant_torque(body,Vector3(0,0,0)).
voidbody_add_shape(body:RID, shape:RID, transform:Transform3D= Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), disabled:bool= false)🔗
Adds a shape to the body, along with a transform matrix. Shapes are usually referenced by their index, so you should track which shape has a given index.
voidbody_apply_central_force(body:RID, force:Vector3)🔗
Applies a directional force without affecting rotation. A force is time dependent and meant to be applied every physics update.
This is equivalent to usingbody_apply_force()at the body's center of mass.
voidbody_apply_central_impulse(body:RID, impulse:Vector3)🔗
Applies a directional impulse without affecting rotation.
An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).
This is equivalent to usingbody_apply_impulse()at the body's center of mass.
voidbody_apply_force(body:RID, force:Vector3, position:Vector3= Vector3(0, 0, 0))🔗
Applies a positioned force to the body. A force is time dependent and meant to be applied every physics update.
positionis the offset from the body origin in global coordinates.
voidbody_apply_impulse(body:RID, impulse:Vector3, position:Vector3= Vector3(0, 0, 0))🔗
Applies a positioned impulse to the body.
An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).
positionis the offset from the body origin in global coordinates.
voidbody_apply_torque(body:RID, torque:Vector3)🔗
Applies a rotational force without affecting position. A force is time dependent and meant to be applied every physics update.
voidbody_apply_torque_impulse(body:RID, impulse:Vector3)🔗
Applies a rotational impulse to the body without affecting the position.
An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).
voidbody_attach_object_instance_id(body:RID, id:int)🔗
Assigns the area to a descendant ofObject, so it can exist in the node tree.
voidbody_clear_shapes(body:RID)🔗
Removes all shapes from a body.
RIDbody_create()🔗
Creates a 3D body object in the physics server, and returns theRIDthat identifies it. The default settings for the created area include a collision layer and mask set to1, and body mode set toBODY_MODE_RIGID.
Usebody_add_shape()to add shapes to it, usebody_set_state()to set its transform, and usebody_set_space()to add the body to a space.
intbody_get_collision_layer(body:RID)const🔗
Returns the physics layer or layers a body belongs to.
intbody_get_collision_mask(body:RID)const🔗
Returns the physics layer or layers a body can collide with.
floatbody_get_collision_priority(body:RID)const🔗
Returns the body's collision priority.
Vector3body_get_constant_force(body:RID)const🔗
Returns the body's total constant positional forces applied during each physics update.
Seebody_add_constant_force()andbody_add_constant_central_force().
Vector3body_get_constant_torque(body:RID)const🔗
Returns the body's total constant rotational forces applied during each physics update.
Seebody_add_constant_torque().
PhysicsDirectBodyState3Dbody_get_direct_state(body:RID)🔗
Returns thePhysicsDirectBodyState3Dof the body. Returnsnullif the body is destroyed or removed from the physics space.
intbody_get_max_contacts_reported(body:RID)const🔗
Returns the maximum contacts that can be reported. Seebody_set_max_contacts_reported().
BodyModebody_get_mode(body:RID)const🔗
Returns the body mode.
intbody_get_object_instance_id(body:RID)const🔗
Gets the instance ID of the object the area is assigned to.
Variantbody_get_param(body:RID, param:BodyParameter)const🔗
Returns the value of a body parameter. A list of available parameters is on theBodyParameterconstants.
RIDbody_get_shape(body:RID, shape_idx:int)const🔗
Returns theRIDof the nth shape of a body.
intbody_get_shape_count(body:RID)const🔗
Returns the number of shapes assigned to a body.
Transform3Dbody_get_shape_transform(body:RID, shape_idx:int)const🔗
Returns the transform matrix of a body shape.
RIDbody_get_space(body:RID)const🔗
Returns theRIDof the space assigned to a body.
Variantbody_get_state(body:RID, state:BodyState)const🔗
Returns a body state.
boolbody_is_axis_locked(body:RID, axis:BodyAxis)const🔗
There is currently no description for this method. Please help us bycontributing one!
boolbody_is_continuous_collision_detection_enabled(body:RID)const🔗
Iftrue, the continuous collision detection mode is enabled.
boolbody_is_omitting_force_integration(body:RID)const🔗
Returnstrueif the body is omitting the standard force integration. Seebody_set_omit_force_integration().
voidbody_remove_collision_exception(body:RID, excepted_body:RID)🔗
Removes a body from the list of bodies exempt from collisions.
Continuous collision detection tries to predict where a moving body will collide, instead of moving it and correcting its movement if it collided.
voidbody_remove_shape(body:RID, shape_idx:int)🔗
Removes a shape from a body. The shape is not deleted, so it can be reused afterwards.
voidbody_reset_mass_properties(body:RID)🔗
Restores the default inertia and center of mass based on shapes to cancel any custom values previously set usingbody_set_param().
voidbody_set_axis_lock(body:RID, axis:BodyAxis, lock:bool)🔗
There is currently no description for this method. Please help us bycontributing one!
voidbody_set_axis_velocity(body:RID, axis_velocity:Vector3)🔗
Sets an axis velocity. The velocity in the given vector axis will be set as the given vector length. This is useful for jumping behavior.
voidbody_set_collision_layer(body:RID, layer:int)🔗
Sets the physics layer or layers a body belongs to.
voidbody_set_collision_mask(body:RID, mask:int)🔗
Sets the physics layer or layers a body can collide with.
voidbody_set_collision_priority(body:RID, priority:float)🔗
Sets the body's collision priority.
voidbody_set_constant_force(body:RID, force:Vector3)🔗
Sets the body's total constant positional forces applied during each physics update.
Seebody_add_constant_force()andbody_add_constant_central_force().
voidbody_set_constant_torque(body:RID, torque:Vector3)🔗
Sets the body's total constant rotational forces applied during each physics update.
Seebody_add_constant_torque().
voidbody_set_enable_continuous_collision_detection(body:RID, enable:bool)🔗
Iftrue, the continuous collision detection mode is enabled.
Continuous collision detection tries to predict where a moving body will collide, instead of moving it and correcting its movement if it collided.
voidbody_set_force_integration_callback(body:RID, callable:Callable, userdata:Variant= null)🔗
Sets the body's custom force integration callback function tocallable. Use an emptyCallable(Callable()) to clear the custom callback.
The functioncallablewill be called every physics tick, before the standard force integration (seebody_set_omit_force_integration()). It can be used for example to update the body's linear and angular velocity based on contact with other bodies.
Ifuserdatais notnull, the functioncallablemust take the following two parameters:
- state: aPhysicsDirectBodyState3D, used to retrieve and modify the body's state,
state: aPhysicsDirectBodyState3D, used to retrieve and modify the body's state,
- userdata: aVariant; its value will be theuserdatapassed into this method.
userdata: aVariant; its value will be theuserdatapassed into this method.
Ifuserdataisnull, thencallablemust take only thestateparameter.
voidbody_set_max_contacts_reported(body:RID, amount:int)🔗
Sets the maximum contacts to report. Bodies can keep a log of the contacts with other bodies. This is enabled by setting the maximum number of contacts reported to a number greater than 0.
voidbody_set_mode(body:RID, mode:BodyMode)🔗
Sets the body mode.
voidbody_set_omit_force_integration(body:RID, enable:bool)🔗
Sets whether the body omits the standard force integration. Ifenableistrue, the body will not automatically use applied forces, torques, and damping to update the body's linear and angular velocity. In this case,body_set_force_integration_callback()can be used to manually update the linear and angular velocity instead.
This method is called when the propertyRigidBody3D.custom_integratoris set.
voidbody_set_param(body:RID, param:BodyParameter, value:Variant)🔗
Sets a body parameter. A list of available parameters is on theBodyParameterconstants.
voidbody_set_ray_pickable(body:RID, enable:bool)🔗
Sets the body pickable with rays ifenableis set.
voidbody_set_shape(body:RID, shape_idx:int, shape:RID)🔗
Substitutes a given body shape by another. The old shape is selected by its index, the new one by itsRID.
voidbody_set_shape_disabled(body:RID, shape_idx:int, disabled:bool)🔗
There is currently no description for this method. Please help us bycontributing one!
voidbody_set_shape_transform(body:RID, shape_idx:int, transform:Transform3D)🔗
Sets the transform matrix for a body shape.
voidbody_set_space(body:RID, space:RID)🔗
Assigns a space to the body (seespace_create()).
voidbody_set_state(body:RID, state:BodyState, value:Variant)🔗
Sets a body state.
voidbody_set_state_sync_callback(body:RID, callable:Callable)🔗
Sets the body's state synchronization callback function tocallable. Use an emptyCallable(Callable()) to clear the callback.
The functioncallablewill be called every physics frame, assuming that the body was active during the previous physics tick, and can be used to fetch the latest state from the physics server.
The functioncallablemust take the following parameters:
- state: aPhysicsDirectBodyState3D, used to retrieve the body's state.
state: aPhysicsDirectBodyState3D, used to retrieve the body's state.
boolbody_test_motion(body:RID, parameters:PhysicsTestMotionParameters3D, result:PhysicsTestMotionResult3D= null)🔗
Returnstrueif a collision would result from moving along a motion vector from a given point in space.PhysicsTestMotionParameters3Dis passed to set motion parameters.PhysicsTestMotionResult3Dcan be passed to return additional information.
RIDbox_shape_create()🔗
Creates a 3D box shape in the physics server, and returns theRIDthat identifies it. Useshape_set_data()to set the box's half-extents.
RIDcapsule_shape_create()🔗
Creates a 3D capsule shape in the physics server, and returns theRIDthat identifies it. Useshape_set_data()to set the capsule's height and radius.
RIDconcave_polygon_shape_create()🔗
Creates a 3D concave polygon shape in the physics server, and returns theRIDthat identifies it. Useshape_set_data()to set the concave polygon's triangles.
floatcone_twist_joint_get_param(joint:RID, param:ConeTwistJointParam)const🔗
Gets a cone twist joint parameter.
voidcone_twist_joint_set_param(joint:RID, param:ConeTwistJointParam, value:float)🔗
Sets a cone twist joint parameter.
RIDconvex_polygon_shape_create()🔗
Creates a 3D convex polygon shape in the physics server, and returns theRIDthat identifies it. Useshape_set_data()to set the convex polygon's points.
RIDcustom_shape_create()🔗
Creates a custom shape in the physics server, and returns theRIDthat identifies it. Useshape_set_data()to set the shape's data.
Note:Custom shapes are not supported by the built-in physics servers, so calling this method always produces an error when using Godot Physics or Jolt Physics. Custom physics servers implemented as GDExtensions may support a custom shape.
RIDcylinder_shape_create()🔗
Creates a 3D cylinder shape in the physics server, and returns theRIDthat identifies it. Useshape_set_data()to set the cylinder's height and radius.
voidfree_rid(rid:RID)🔗
Destroys any of the objects created by PhysicsServer3D. If theRIDpassed is not one of the objects that can be created by PhysicsServer3D, an error will be sent to the console.
boolgeneric_6dof_joint_get_flag(joint:RID, axis:Axis, flag:G6DOFJointAxisFlag)const🔗
Returns the value of a generic 6DOF joint flag.
floatgeneric_6dof_joint_get_param(joint:RID, axis:Axis, param:G6DOFJointAxisParam)const🔗
Returns the value of a generic 6DOF joint parameter.
voidgeneric_6dof_joint_set_flag(joint:RID, axis:Axis, flag:G6DOFJointAxisFlag, enable:bool)🔗
Sets the value of a given generic 6DOF joint flag.
voidgeneric_6dof_joint_set_param(joint:RID, axis:Axis, param:G6DOFJointAxisParam, value:float)🔗
Sets the value of a given generic 6DOF joint parameter.
intget_process_info(process_info:ProcessInfo)🔗
Returns the value of a physics engine state specified byprocess_info.
RIDheightmap_shape_create()🔗
Creates a 3D heightmap shape in the physics server, and returns theRIDthat identifies it. Useshape_set_data()to set the heightmap's data.
boolhinge_joint_get_flag(joint:RID, flag:HingeJointFlag)const🔗
Gets a hinge joint flag.
floathinge_joint_get_param(joint:RID, param:HingeJointParam)const🔗
Gets a hinge joint parameter.
voidhinge_joint_set_flag(joint:RID, flag:HingeJointFlag, enabled:bool)🔗
Sets a hinge joint flag.
voidhinge_joint_set_param(joint:RID, param:HingeJointParam, value:float)🔗
Sets a hinge joint parameter.
voidjoint_clear(joint:RID)🔗
There is currently no description for this method. Please help us bycontributing one!
RIDjoint_create()🔗
There is currently no description for this method. Please help us bycontributing one!
voidjoint_disable_collisions_between_bodies(joint:RID, disable:bool)🔗
Sets whether the bodies attached to theJoint3Dwill collide with each other.
intjoint_get_solver_priority(joint:RID)const🔗
Gets the priority value of the Joint3D.
JointTypejoint_get_type(joint:RID)const🔗
Returns the type of the Joint3D.
booljoint_is_disabled_collisions_between_bodies(joint:RID)const🔗
Returns whether the bodies attached to theJoint3Dwill collide with each other.
voidjoint_make_cone_twist(joint:RID, body_A:RID, local_ref_A:Transform3D, body_B:RID, local_ref_B:Transform3D)🔗
There is currently no description for this method. Please help us bycontributing one!
voidjoint_make_generic_6dof(joint:RID, body_A:RID, local_ref_A:Transform3D, body_B:RID, local_ref_B:Transform3D)🔗
Make the joint a generic six degrees of freedom (6DOF) joint. Usegeneric_6dof_joint_set_flag()andgeneric_6dof_joint_set_param()to set the joint's flags and parameters respectively.
voidjoint_make_hinge(joint:RID, body_A:RID, hinge_A:Transform3D, body_B:RID, hinge_B:Transform3D)🔗
There is currently no description for this method. Please help us bycontributing one!
voidjoint_make_pin(joint:RID, body_A:RID, local_A:Vector3, body_B:RID, local_B:Vector3)🔗
There is currently no description for this method. Please help us bycontributing one!
voidjoint_make_slider(joint:RID, body_A:RID, local_ref_A:Transform3D, body_B:RID, local_ref_B:Transform3D)🔗
There is currently no description for this method. Please help us bycontributing one!
voidjoint_set_solver_priority(joint:RID, priority:int)🔗
Sets the priority value of the Joint3D.
Vector3pin_joint_get_local_a(joint:RID)const🔗
Returns position of the joint in the local space of body a of the joint.
Vector3pin_joint_get_local_b(joint:RID)const🔗
Returns position of the joint in the local space of body b of the joint.
floatpin_joint_get_param(joint:RID, param:PinJointParam)const🔗
Gets a pin joint parameter.
voidpin_joint_set_local_a(joint:RID, local_A:Vector3)🔗
Sets position of the joint in the local space of body a of the joint.
voidpin_joint_set_local_b(joint:RID, local_B:Vector3)🔗
Sets position of the joint in the local space of body b of the joint.
voidpin_joint_set_param(joint:RID, param:PinJointParam, value:float)🔗
Sets a pin joint parameter.
RIDseparation_ray_shape_create()🔗
Creates a 3D separation ray shape in the physics server, and returns theRIDthat identifies it. Useshape_set_data()to set the shape'slengthandslide_on_slopeproperties.
voidset_active(active:bool)🔗
Activates or deactivates the 3D physics engine.
Variantshape_get_data(shape:RID)const🔗
Returns the shape data that configures the shape, such as the half-extents of a box or the triangles of a concave (trimesh) shape. Seeshape_set_data()for the precise format of this data in each case.
floatshape_get_margin(shape:RID)const🔗
Returns the collision margin for the shape.
Note:This is not used in Godot Physics, so will always return0.
ShapeTypeshape_get_type(shape:RID)const🔗
Returns the shape's type.
voidshape_set_data(shape:RID, data:Variant)🔗
Sets the shape data that configures the shape. Thedatato be passed depends on the shape's type (seeshape_get_type()):
- SHAPE_WORLD_BOUNDARY: aPlane,
SHAPE_WORLD_BOUNDARY: aPlane,
- SHAPE_SEPARATION_RAY: a dictionary containing the key"length"with afloatvalue and the key"slide_on_slope"with aboolvalue,
SHAPE_SEPARATION_RAY: a dictionary containing the key"length"with afloatvalue and the key"slide_on_slope"with aboolvalue,
- SHAPE_SPHERE: afloatthat is the radius of the sphere,
SHAPE_SPHERE: afloatthat is the radius of the sphere,
- SHAPE_BOX: aVector3containing the half-extents of the box,
SHAPE_BOX: aVector3containing the half-extents of the box,
- SHAPE_CAPSULE: a dictionary containing the keys"height"and"radius"withfloatvalues,
SHAPE_CAPSULE: a dictionary containing the keys"height"and"radius"withfloatvalues,
- SHAPE_CYLINDER: a dictionary containing the keys"height"and"radius"withfloatvalues,
SHAPE_CYLINDER: a dictionary containing the keys"height"and"radius"withfloatvalues,
- SHAPE_CONVEX_POLYGON: aPackedVector3Arrayof points defining a convex polygon (the shape will be the convex hull of the points),
SHAPE_CONVEX_POLYGON: aPackedVector3Arrayof points defining a convex polygon (the shape will be the convex hull of the points),
- SHAPE_CONCAVE_POLYGON: a dictionary containing the key"faces"with aPackedVector3Arrayvalue (with a length divisible by 3, so that each 3-tuple of points forms a face) and the key"backface_collision"with aboolvalue,
SHAPE_CONCAVE_POLYGON: a dictionary containing the key"faces"with aPackedVector3Arrayvalue (with a length divisible by 3, so that each 3-tuple of points forms a face) and the key"backface_collision"with aboolvalue,
- SHAPE_HEIGHTMAP: a dictionary containing the keys"width"and"depth"withintvalues, and the key"heights"with a value that is a packed array offloats of lengthwidth*depth(that is aPackedFloat32Array, or aPackedFloat64Arrayif Godot was compiled with theprecision=doubleoption), and optionally the keys"min_height"and"max_height"withfloatvalues,
SHAPE_HEIGHTMAP: a dictionary containing the keys"width"and"depth"withintvalues, and the key"heights"with a value that is a packed array offloats of lengthwidth*depth(that is aPackedFloat32Array, or aPackedFloat64Arrayif Godot was compiled with theprecision=doubleoption), and optionally the keys"min_height"and"max_height"withfloatvalues,
- SHAPE_SOFT_BODY: the inputdatais ignored and this method has no effect,
SHAPE_SOFT_BODY: the inputdatais ignored and this method has no effect,
- SHAPE_CUSTOM: the inputdatais interpreted by a custom physics server, if it supports custom shapes.
SHAPE_CUSTOM: the inputdatais interpreted by a custom physics server, if it supports custom shapes.
voidshape_set_margin(shape:RID, margin:float)🔗
Sets the collision margin for the shape.
Note:This is not used in Godot Physics.
floatslider_joint_get_param(joint:RID, param:SliderJointParam)const🔗
Gets a slider joint parameter.
voidslider_joint_set_param(joint:RID, param:SliderJointParam, value:float)🔗
Gets a slider joint parameter.
voidsoft_body_add_collision_exception(body:RID, body_b:RID)🔗
Adds the given body to the list of bodies exempt from collisions.
voidsoft_body_apply_central_force(body:RID, force:Vector3)🔗
Distributes and applies a force to all points. A force is time dependent and meant to be applied every physics update.
voidsoft_body_apply_central_impulse(body:RID, impulse:Vector3)🔗
Distributes and applies an impulse to all points.
An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).
voidsoft_body_apply_point_force(body:RID, point_index:int, force:Vector3)🔗
Applies a force to a point. A force is time dependent and meant to be applied every physics update.
voidsoft_body_apply_point_impulse(body:RID, point_index:int, impulse:Vector3)🔗
Applies an impulse to a point.
An impulse is time-independent! Applying an impulse every frame would result in a framerate-dependent force. For this reason, it should only be used when simulating one-time impacts (use the "_force" functions otherwise).
RIDsoft_body_create()🔗
Creates a new soft body and returns its internalRID.
AABBsoft_body_get_bounds(body:RID)const🔗
Returns the bounds of the given soft body in global coordinates.
intsoft_body_get_collision_layer(body:RID)const🔗
Returns the physics layer or layers that the given soft body belongs to.
intsoft_body_get_collision_mask(body:RID)const🔗
Returns the physics layer or layers that the given soft body can collide with.
floatsoft_body_get_damping_coefficient(body:RID)const🔗
Returns the damping coefficient of the given soft body.
floatsoft_body_get_drag_coefficient(body:RID)const🔗
Returns the drag coefficient of the given soft body.
floatsoft_body_get_linear_stiffness(body:RID)const🔗
Returns the linear stiffness of the given soft body.
Vector3soft_body_get_point_global_position(body:RID, point_index:int)const🔗
Returns the current position of the given soft body point in global coordinates.
floatsoft_body_get_pressure_coefficient(body:RID)const🔗
Returns the pressure coefficient of the given soft body.
floatsoft_body_get_shrinking_factor(body:RID)const🔗
Returns the shrinking factor of the given soft body.
intsoft_body_get_simulation_precision(body:RID)const🔗
Returns the simulation precision of the given soft body.
RIDsoft_body_get_space(body:RID)const🔗
Returns theRIDof the space assigned to the given soft body.
Variantsoft_body_get_state(body:RID, state:BodyState)const🔗
Returns the given soft body state.
Note:Godot's default physics implementation does not supportBODY_STATE_LINEAR_VELOCITY,BODY_STATE_ANGULAR_VELOCITY,BODY_STATE_SLEEPING, orBODY_STATE_CAN_SLEEP.
floatsoft_body_get_total_mass(body:RID)const🔗
Returns the total mass assigned to the given soft body.
boolsoft_body_is_point_pinned(body:RID, point_index:int)const🔗
Returns whether the given soft body point is pinned.
voidsoft_body_move_point(body:RID, point_index:int, global_position:Vector3)🔗
Moves the given soft body point to a position in global coordinates.
voidsoft_body_pin_point(body:RID, point_index:int, pin:bool)🔗
Pins or unpins the given soft body point based on the value ofpin.
Note:Pinning a point effectively makes it kinematic, preventing it from being affected by forces, but you can still move it usingsoft_body_move_point().
voidsoft_body_remove_all_pinned_points(body:RID)🔗
Unpins all points of the given soft body.
voidsoft_body_remove_collision_exception(body:RID, body_b:RID)🔗
Removes the given body from the list of bodies exempt from collisions.
voidsoft_body_set_collision_layer(body:RID, layer:int)🔗
Sets the physics layer or layers the given soft body belongs to.
voidsoft_body_set_collision_mask(body:RID, mask:int)🔗
Sets the physics layer or layers the given soft body can collide with.
voidsoft_body_set_damping_coefficient(body:RID, damping_coefficient:float)🔗
Sets the damping coefficient of the given soft body. Higher values will slow down the body more noticeably when forces are applied.
voidsoft_body_set_drag_coefficient(body:RID, drag_coefficient:float)🔗
Sets the drag coefficient of the given soft body. Higher values increase this body's air resistance.
Note:This value is currently unused by Godot's default physics implementation.
voidsoft_body_set_linear_stiffness(body:RID, stiffness:float)🔗
Sets the linear stiffness of the given soft body. Higher values will result in a stiffer body, while lower values will increase the body's ability to bend. The value can be between0.0and1.0(inclusive).
voidsoft_body_set_mesh(body:RID, mesh:RID)🔗
Sets the mesh of the given soft body.
voidsoft_body_set_pressure_coefficient(body:RID, pressure_coefficient:float)🔗
Sets the pressure coefficient of the given soft body. Simulates pressure build-up from inside this body. Higher values increase the strength of this effect.
voidsoft_body_set_ray_pickable(body:RID, enable:bool)🔗
Sets whether the given soft body will be pickable when using object picking.
voidsoft_body_set_shrinking_factor(body:RID, shrinking_factor:float)🔗
Sets the shrinking factor of the given soft body.
voidsoft_body_set_simulation_precision(body:RID, simulation_precision:int)🔗
Sets the simulation precision of the given soft body. Increasing this value will improve the resulting simulation, but can affect performance. Use with care.
voidsoft_body_set_space(body:RID, space:RID)🔗
Assigns a space to the given soft body (seespace_create()).
voidsoft_body_set_state(body:RID, state:BodyState, variant:Variant)🔗
Sets the given body state for the given body.
Note:Godot's default physics implementation does not supportBODY_STATE_LINEAR_VELOCITY,BODY_STATE_ANGULAR_VELOCITY,BODY_STATE_SLEEPING, orBODY_STATE_CAN_SLEEP.
voidsoft_body_set_total_mass(body:RID, total_mass:float)🔗
Sets the total mass for the given soft body.
voidsoft_body_set_transform(body:RID, transform:Transform3D)🔗
Sets the global transform of the given soft body.
voidsoft_body_update_rendering_server(body:RID, rendering_server_handler:PhysicsServer3DRenderingServerHandler)🔗
Requests that the physics server updates the rendering server with the latest positions of the given soft body's points through therendering_server_handlerinterface.
RIDspace_create()🔗
Creates a space. A space is a collection of parameters for the physics engine that can be assigned to an area or a body. It can be assigned to an area witharea_set_space(), or to a body withbody_set_space().
PhysicsDirectSpaceState3Dspace_get_direct_state(space:RID)🔗
Returns the state of a space, aPhysicsDirectSpaceState3D. This object can be used to make collision/intersection queries.
floatspace_get_param(space:RID, param:SpaceParameter)const🔗
Returns the value of a space parameter.
boolspace_is_active(space:RID)const🔗
Returns whether the space is active.
voidspace_set_active(space:RID, active:bool)🔗
Marks a space as active. It will not have an effect, unless it is assigned to an area or body.
voidspace_set_param(space:RID, param:SpaceParameter, value:float)🔗
Sets the value for a space parameter. A list of available parameters is on theSpaceParameterconstants.
RIDsphere_shape_create()🔗
Creates a 3D sphere shape in the physics server, and returns theRIDthat identifies it. Useshape_set_data()to set the sphere's radius.
RIDworld_boundary_shape_create()🔗
Creates a 3D world boundary shape in the physics server, and returns theRIDthat identifies it. Useshape_set_data()to set the shape's normal direction and distance properties.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.