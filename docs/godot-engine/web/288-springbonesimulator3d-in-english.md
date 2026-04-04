# SpringBoneSimulator3D in English

# SpringBoneSimulator3D

Inherits:SkeletonModifier3D<Node3D<Node<Object
ASkeletonModifier3Dto apply inertial wavering to bone chains.

## Description

ThisSkeletonModifier3Dcan be used to wiggle hair, cloth, and tails. This modifier behaves differently fromPhysicalBoneSimulator3Das it attempts to return the original pose after modification.
If you setupset_root_bone()andset_end_bone(), it is treated as one bone chain. Note that it does not support a branched chain like Y-shaped chains.
When a bone chain is created, an array is generated from the bones that exist in between and listed in the joint list.
Several properties can be applied to each joint, such asset_joint_stiffness(),set_joint_drag(), andset_joint_gravity().
For simplicity, you can set values to all joints at the same time by using aCurve. If you want to specify detailed values individually, setset_individual_config()totrue.
For physical simulation,SpringBoneSimulator3Dcan have children as self-standing collisions that are not related toPhysicsServer3D, see alsoSpringBoneCollision3D.
Warning:A scaledSpringBoneSimulator3Dwill likely not behave as expected. Make sure that the parentSkeleton3Dand its bones are not scaled.

## Properties

| Vector3 | external_force | Vector3(0,0,0) |
|---|---|---|
| bool | mutable_bone_axes | true |
| int | setting_count | 0 |

Vector3
external_force
Vector3(0,0,0)
bool
mutable_bone_axes
true
setting_count

## Methods

| bool | are_all_child_collisions_enabled(index:int)const |
|---|---|
| void | clear_collisions(index:int) |
| void | clear_exclude_collisions(index:int) |
| void | clear_settings() |
| int | get_center_bone(index:int)const |
| String | get_center_bone_name(index:int)const |
| CenterFrom | get_center_from(index:int)const |
| NodePath | get_center_node(index:int)const |
| int | get_collision_count(index:int)const |
| NodePath | get_collision_path(index:int, collision:int)const |
| float | get_drag(index:int)const |
| Curve | get_drag_damping_curve(index:int)const |
| int | get_end_bone(index:int)const |
| BoneDirection | get_end_bone_direction(index:int)const |
| float | get_end_bone_length(index:int)const |
| String | get_end_bone_name(index:int)const |
| int | get_exclude_collision_count(index:int)const |
| NodePath | get_exclude_collision_path(index:int, collision:int)const |
| float | get_gravity(index:int)const |
| Curve | get_gravity_damping_curve(index:int)const |
| Vector3 | get_gravity_direction(index:int)const |
| int | get_joint_bone(index:int, joint:int)const |
| String | get_joint_bone_name(index:int, joint:int)const |
| int | get_joint_count(index:int)const |
| float | get_joint_drag(index:int, joint:int)const |
| float | get_joint_gravity(index:int, joint:int)const |
| Vector3 | get_joint_gravity_direction(index:int, joint:int)const |
| float | get_joint_radius(index:int, joint:int)const |
| RotationAxis | get_joint_rotation_axis(index:int, joint:int)const |
| Vector3 | get_joint_rotation_axis_vector(index:int, joint:int)const |
| float | get_joint_stiffness(index:int, joint:int)const |
| float | get_radius(index:int)const |
| Curve | get_radius_damping_curve(index:int)const |
| int | get_root_bone(index:int)const |
| String | get_root_bone_name(index:int)const |
| RotationAxis | get_rotation_axis(index:int)const |
| Vector3 | get_rotation_axis_vector(index:int)const |
| float | get_stiffness(index:int)const |
| Curve | get_stiffness_damping_curve(index:int)const |
| bool | is_config_individual(index:int)const |
| bool | is_end_bone_extended(index:int)const |
| void | reset() |
| void | set_center_bone(index:int, bone:int) |
| void | set_center_bone_name(index:int, bone_name:String) |
| void | set_center_from(index:int, center_from:CenterFrom) |
| void | set_center_node(index:int, node_path:NodePath) |
| void | set_collision_count(index:int, count:int) |
| void | set_collision_path(index:int, collision:int, node_path:NodePath) |
| void | set_drag(index:int, drag:float) |
| void | set_drag_damping_curve(index:int, curve:Curve) |
| void | set_enable_all_child_collisions(index:int, enabled:bool) |
| void | set_end_bone(index:int, bone:int) |
| void | set_end_bone_direction(index:int, bone_direction:BoneDirection) |
| void | set_end_bone_length(index:int, length:float) |
| void | set_end_bone_name(index:int, bone_name:String) |
| void | set_exclude_collision_count(index:int, count:int) |
| void | set_exclude_collision_path(index:int, collision:int, node_path:NodePath) |
| void | set_extend_end_bone(index:int, enabled:bool) |
| void | set_gravity(index:int, gravity:float) |
| void | set_gravity_damping_curve(index:int, curve:Curve) |
| void | set_gravity_direction(index:int, gravity_direction:Vector3) |
| void | set_individual_config(index:int, enabled:bool) |
| void | set_joint_drag(index:int, joint:int, drag:float) |
| void | set_joint_gravity(index:int, joint:int, gravity:float) |
| void | set_joint_gravity_direction(index:int, joint:int, gravity_direction:Vector3) |
| void | set_joint_radius(index:int, joint:int, radius:float) |
| void | set_joint_rotation_axis(index:int, joint:int, axis:RotationAxis) |
| void | set_joint_rotation_axis_vector(index:int, joint:int, vector:Vector3) |
| void | set_joint_stiffness(index:int, joint:int, stiffness:float) |
| void | set_radius(index:int, radius:float) |
| void | set_radius_damping_curve(index:int, curve:Curve) |
| void | set_root_bone(index:int, bone:int) |
| void | set_root_bone_name(index:int, bone_name:String) |
| void | set_rotation_axis(index:int, axis:RotationAxis) |
| void | set_rotation_axis_vector(index:int, vector:Vector3) |
| void | set_stiffness(index:int, stiffness:float) |
| void | set_stiffness_damping_curve(index:int, curve:Curve) |

bool
are_all_child_collisions_enabled(index:int)const
void
clear_collisions(index:int)
void
clear_exclude_collisions(index:int)
void
clear_settings()
get_center_bone(index:int)const
String
get_center_bone_name(index:int)const
CenterFrom
get_center_from(index:int)const
NodePath
get_center_node(index:int)const
get_collision_count(index:int)const
NodePath
get_collision_path(index:int, collision:int)const
float
get_drag(index:int)const
Curve
get_drag_damping_curve(index:int)const
get_end_bone(index:int)const
BoneDirection
get_end_bone_direction(index:int)const
float
get_end_bone_length(index:int)const
String
get_end_bone_name(index:int)const
get_exclude_collision_count(index:int)const
NodePath
get_exclude_collision_path(index:int, collision:int)const
float
get_gravity(index:int)const
Curve
get_gravity_damping_curve(index:int)const
Vector3
get_gravity_direction(index:int)const
get_joint_bone(index:int, joint:int)const
String
get_joint_bone_name(index:int, joint:int)const
get_joint_count(index:int)const
float
get_joint_drag(index:int, joint:int)const
float
get_joint_gravity(index:int, joint:int)const
Vector3
get_joint_gravity_direction(index:int, joint:int)const
float
get_joint_radius(index:int, joint:int)const
RotationAxis
get_joint_rotation_axis(index:int, joint:int)const
Vector3
get_joint_rotation_axis_vector(index:int, joint:int)const
float
get_joint_stiffness(index:int, joint:int)const
float
get_radius(index:int)const
Curve
get_radius_damping_curve(index:int)const
get_root_bone(index:int)const
String
get_root_bone_name(index:int)const
RotationAxis
get_rotation_axis(index:int)const
Vector3
get_rotation_axis_vector(index:int)const
float
get_stiffness(index:int)const
Curve
get_stiffness_damping_curve(index:int)const
bool
is_config_individual(index:int)const
bool
is_end_bone_extended(index:int)const
void
reset()
void
set_center_bone(index:int, bone:int)
void
set_center_bone_name(index:int, bone_name:String)
void
set_center_from(index:int, center_from:CenterFrom)
void
set_center_node(index:int, node_path:NodePath)
void
set_collision_count(index:int, count:int)
void
set_collision_path(index:int, collision:int, node_path:NodePath)
void
set_drag(index:int, drag:float)
void
set_drag_damping_curve(index:int, curve:Curve)
void
set_enable_all_child_collisions(index:int, enabled:bool)
void
set_end_bone(index:int, bone:int)
void
set_end_bone_direction(index:int, bone_direction:BoneDirection)
void
set_end_bone_length(index:int, length:float)
void
set_end_bone_name(index:int, bone_name:String)
void
set_exclude_collision_count(index:int, count:int)
void
set_exclude_collision_path(index:int, collision:int, node_path:NodePath)
void
set_extend_end_bone(index:int, enabled:bool)
void
set_gravity(index:int, gravity:float)
void
set_gravity_damping_curve(index:int, curve:Curve)
void
set_gravity_direction(index:int, gravity_direction:Vector3)
void
set_individual_config(index:int, enabled:bool)
void
set_joint_drag(index:int, joint:int, drag:float)
void
set_joint_gravity(index:int, joint:int, gravity:float)
void
set_joint_gravity_direction(index:int, joint:int, gravity_direction:Vector3)
void
set_joint_radius(index:int, joint:int, radius:float)
void
set_joint_rotation_axis(index:int, joint:int, axis:RotationAxis)
void
set_joint_rotation_axis_vector(index:int, joint:int, vector:Vector3)
void
set_joint_stiffness(index:int, joint:int, stiffness:float)
void
set_radius(index:int, radius:float)
void
set_radius_damping_curve(index:int, curve:Curve)
void
set_root_bone(index:int, bone:int)
void
set_root_bone_name(index:int, bone_name:String)
void
set_rotation_axis(index:int, axis:RotationAxis)
void
set_rotation_axis_vector(index:int, vector:Vector3)
void
set_stiffness(index:int, stiffness:float)
void
set_stiffness_damping_curve(index:int, curve:Curve)

## Enumerations

enumCenterFrom:🔗
CenterFromCENTER_FROM_WORLD_ORIGIN=0
The world origin is defined as center.
CenterFromCENTER_FROM_NODE=1
TheNode3Dspecified byset_center_node()is defined as center.
IfNode3Dis not found, the parentSkeleton3Dis treated as center.
CenterFromCENTER_FROM_BONE=2
The bone pose origin of the parentSkeleton3Dspecified byset_center_bone()is defined as center.
IfNode3Dis not found, the parentSkeleton3Dis treated as center.

## Property Descriptions

Vector3external_force=Vector3(0,0,0)🔗

- voidset_external_force(value:Vector3)
voidset_external_force(value:Vector3)
- Vector3get_external_force()
Vector3get_external_force()
The constant force that always affected bones. It is equal to the result when the parentSkeleton3Dmoves at this speed in the opposite direction.
This is useful for effects such as wind and anti-gravity.
boolmutable_bone_axes=true🔗
- voidset_mutable_bone_axes(value:bool)
voidset_mutable_bone_axes(value:bool)
- boolare_bone_axes_mutable()
boolare_bone_axes_mutable()
Iftrue, the solver retrieves the bone axis from the bone pose every frame.
Iffalse, the solver retrieves the bone axis from the bone rest and caches it, which increases performance slightly, but position changes in the bone pose made before processing thisSpringBoneSimulator3Dare ignored.
intsetting_count=0🔗
- voidset_setting_count(value:int)
voidset_setting_count(value:int)
- intget_setting_count()
intget_setting_count()
The number of settings.

## Method Descriptions

boolare_all_child_collisions_enabled(index:int)const🔗
Returnstrueif all childSpringBoneCollision3Ds are contained in the collision list atindexin the settings.
voidclear_collisions(index:int)🔗
Clears all collisions from the collision list atindexin the settings whenare_all_child_collisions_enabled()isfalse.
voidclear_exclude_collisions(index:int)🔗
Clears all exclude collisions from the collision list atindexin the settings whenare_all_child_collisions_enabled()istrue.
voidclear_settings()🔗
Clears all settings.
intget_center_bone(index:int)const🔗
Returns the center bone index of the bone chain.
Stringget_center_bone_name(index:int)const🔗
Returns the center bone name of the bone chain.
CenterFromget_center_from(index:int)const🔗
Returns what the center originates from in the bone chain.
NodePathget_center_node(index:int)const🔗
Returns the center node path of the bone chain.
intget_collision_count(index:int)const🔗
Returns the collision count of the bone chain's collision list whenare_all_child_collisions_enabled()isfalse.
NodePathget_collision_path(index:int, collision:int)const🔗
Returns the node path of theSpringBoneCollision3Datcollisionin the bone chain's collision list whenare_all_child_collisions_enabled()isfalse.
floatget_drag(index:int)const🔗
Returns the drag force damping curve of the bone chain.
Curveget_drag_damping_curve(index:int)const🔗
Returns the drag force damping curve of the bone chain.
intget_end_bone(index:int)const🔗
Returns the end bone index of the bone chain.
BoneDirectionget_end_bone_direction(index:int)const🔗
Returns the tail direction of the end bone of the bone chain whenis_end_bone_extended()istrue.
floatget_end_bone_length(index:int)const🔗
Returns the end bone tail length of the bone chain whenis_end_bone_extended()istrue.
Stringget_end_bone_name(index:int)const🔗
Returns the end bone name of the bone chain.
intget_exclude_collision_count(index:int)const🔗
Returns the exclude collision count of the bone chain's exclude collision list whenare_all_child_collisions_enabled()istrue.
NodePathget_exclude_collision_path(index:int, collision:int)const🔗
Returns the node path of theSpringBoneCollision3Datcollisionin the bone chain's exclude collision list whenare_all_child_collisions_enabled()istrue.
floatget_gravity(index:int)const🔗
Returns the gravity amount of the bone chain.
Curveget_gravity_damping_curve(index:int)const🔗
Returns the gravity amount damping curve of the bone chain.
Vector3get_gravity_direction(index:int)const🔗
Returns the gravity direction of the bone chain.
intget_joint_bone(index:int, joint:int)const🔗
Returns the bone index atjointin the bone chain's joint list.
Stringget_joint_bone_name(index:int, joint:int)const🔗
Returns the bone name atjointin the bone chain's joint list.
intget_joint_count(index:int)const🔗
Returns the joint count of the bone chain's joint list.
floatget_joint_drag(index:int, joint:int)const🔗
Returns the drag force atjointin the bone chain's joint list.
floatget_joint_gravity(index:int, joint:int)const🔗
Returns the gravity amount atjointin the bone chain's joint list.
Vector3get_joint_gravity_direction(index:int, joint:int)const🔗
Returns the gravity direction atjointin the bone chain's joint list.
floatget_joint_radius(index:int, joint:int)const🔗
Returns the radius atjointin the bone chain's joint list.
RotationAxisget_joint_rotation_axis(index:int, joint:int)const🔗
Returns the rotation axis atjointin the bone chain's joint list.
Vector3get_joint_rotation_axis_vector(index:int, joint:int)const🔗
Returns the rotation axis vector for the specified joint in the bone chain. This vector represents the axis around which the joint can rotate. It is determined based on the rotation axis set for the joint.
Ifget_joint_rotation_axis()isSkeletonModifier3D.ROTATION_AXIS_ALL, this method returnsVector3(0,0,0).
floatget_joint_stiffness(index:int, joint:int)const🔗
Returns the stiffness force atjointin the bone chain's joint list.
floatget_radius(index:int)const🔗
Returns the joint radius of the bone chain.
Curveget_radius_damping_curve(index:int)const🔗
Returns the joint radius damping curve of the bone chain.
intget_root_bone(index:int)const🔗
Returns the root bone index of the bone chain.
Stringget_root_bone_name(index:int)const🔗
Returns the root bone name of the bone chain.
RotationAxisget_rotation_axis(index:int)const🔗
Returns the rotation axis of the bone chain.
Vector3get_rotation_axis_vector(index:int)const🔗
Returns the rotation axis vector of the bone chain. This vector represents the axis around which the bone chain can rotate. It is determined based on the rotation axis set for the bone chain.
Ifget_rotation_axis()isSkeletonModifier3D.ROTATION_AXIS_ALL, this method returnsVector3(0,0,0).
floatget_stiffness(index:int)const🔗
Returns the stiffness force of the bone chain.
Curveget_stiffness_damping_curve(index:int)const🔗
Returns the stiffness force damping curve of the bone chain.
boolis_config_individual(index:int)const🔗
Returnstrueif the config can be edited individually for each joint.
boolis_end_bone_extended(index:int)const🔗
Returnstrueif the end bone is extended to have a tail.
voidreset()🔗
Resets a simulating state with respect to the current bone pose.
It is useful to prevent the simulation result getting violent. For example, calling this immediately after a call toAnimationPlayer.play()without a fading, or within the previousSkeletonModifier3D.modification_processedsignal if it's condition changes significantly.
voidset_center_bone(index:int, bone:int)🔗
Sets the center bone index of the bone chain.
voidset_center_bone_name(index:int, bone_name:String)🔗
Sets the center bone name of the bone chain.
voidset_center_from(index:int, center_from:CenterFrom)🔗
Sets what the center originates from in the bone chain.
Bone movement is calculated based on the difference in relative distance between center and bone in the previous and next frames.
For example, if the parentSkeleton3Dis used as the center, the bones are considered to have not moved if theSkeleton3Dmoves in the world.
In this case, only a change in the bone pose is considered to be a bone movement.
voidset_center_node(index:int, node_path:NodePath)🔗
Sets the center node path of the bone chain.
voidset_collision_count(index:int, count:int)🔗
Sets the number of collisions in the collision list atindexin the settings whenare_all_child_collisions_enabled()isfalse.
voidset_collision_path(index:int, collision:int, node_path:NodePath)🔗
Sets the node path of theSpringBoneCollision3Datcollisionin the bone chain's collision list whenare_all_child_collisions_enabled()isfalse.
voidset_drag(index:int, drag:float)🔗
Sets the drag force of the bone chain. The greater the value, the more suppressed the wiggling.
The value is scaled byset_drag_damping_curve()and cached in each joint setting in the joint list.
voidset_drag_damping_curve(index:int, curve:Curve)🔗
Sets the drag force damping curve of the bone chain.
voidset_enable_all_child_collisions(index:int, enabled:bool)🔗
Ifenabledistrue, all childSpringBoneCollision3Ds are colliding andset_exclude_collision_path()is enabled as an exclusion list atindexin the settings.
Ifenabledisfalse, you need to manually register all valid collisions withset_collision_path().
voidset_end_bone(index:int, bone:int)🔗
Sets the end bone index of the bone chain.
voidset_end_bone_direction(index:int, bone_direction:BoneDirection)🔗
Sets the end bone tail direction of the bone chain whenis_end_bone_extended()istrue.
voidset_end_bone_length(index:int, length:float)🔗
Sets the end bone tail length of the bone chain whenis_end_bone_extended()istrue.
voidset_end_bone_name(index:int, bone_name:String)🔗
Sets the end bone name of the bone chain.
Note:End bone must be the root bone or a child of the root bone. If they are the same, the tail must be extended byset_extend_end_bone()to jiggle the bone.
voidset_exclude_collision_count(index:int, count:int)🔗
Sets the number of exclude collisions in the exclude collision list atindexin the settings whenare_all_child_collisions_enabled()istrue.
voidset_exclude_collision_path(index:int, collision:int, node_path:NodePath)🔗
Sets the node path of theSpringBoneCollision3Datcollisionin the bone chain's exclude collision list whenare_all_child_collisions_enabled()istrue.
voidset_extend_end_bone(index:int, enabled:bool)🔗
Ifenabledistrue, the end bone is extended to have a tail.
The extended tail config is allocated to the last element in the joint list. In other words, if you setenabledtofalse, the config of the last element in the joint list has no effect in the simulated result.
voidset_gravity(index:int, gravity:float)🔗
Sets the gravity amount of the bone chain. This value is not an acceleration, but a constant velocity of movement inset_gravity_direction().
Ifgravityis not0, the modified pose will not return to the original pose since it is always affected by gravity.
The value is scaled byset_gravity_damping_curve()and cached in each joint setting in the joint list.
voidset_gravity_damping_curve(index:int, curve:Curve)🔗
Sets the gravity amount damping curve of the bone chain.
voidset_gravity_direction(index:int, gravity_direction:Vector3)🔗
Sets the gravity direction of the bone chain. This value is internally normalized and then multiplied byset_gravity().
The value is cached in each joint setting in the joint list.
voidset_individual_config(index:int, enabled:bool)🔗
Ifenabledistrue, the config can be edited individually for each joint.
voidset_joint_drag(index:int, joint:int, drag:float)🔗
Sets the drag force atjointin the bone chain's joint list whenis_config_individual()istrue.
voidset_joint_gravity(index:int, joint:int, gravity:float)🔗
Sets the gravity amount atjointin the bone chain's joint list whenis_config_individual()istrue.
voidset_joint_gravity_direction(index:int, joint:int, gravity_direction:Vector3)🔗
Sets the gravity direction atjointin the bone chain's joint list whenis_config_individual()istrue.
voidset_joint_radius(index:int, joint:int, radius:float)🔗
Sets the joint radius atjointin the bone chain's joint list whenis_config_individual()istrue.
voidset_joint_rotation_axis(index:int, joint:int, axis:RotationAxis)🔗
Sets the rotation axis atjointin the bone chain's joint list whenis_config_individual()istrue.
The axes are based on theSkeleton3D.get_bone_rest()'s space, ifaxisisSkeletonModifier3D.ROTATION_AXIS_CUSTOM, you can specify any axis.
Note:The rotation axis and the forward vector shouldn't be colinear to avoid unintended rotation sinceSpringBoneSimulator3Ddoes not factor in twisting forces.
voidset_joint_rotation_axis_vector(index:int, joint:int, vector:Vector3)🔗
Sets the rotation axis vector for the specified joint in the bone chain.
This vector is normalized by an internal process and represents the axis around which the bone chain can rotate.
If the vector length is0, it is considered synonymous withSkeletonModifier3D.ROTATION_AXIS_ALL.
voidset_joint_stiffness(index:int, joint:int, stiffness:float)🔗
Sets the stiffness force atjointin the bone chain's joint list whenis_config_individual()istrue.
voidset_radius(index:int, radius:float)🔗
Sets the joint radius of the bone chain. It is used to move and slide with theSpringBoneCollision3Din the collision list.
The value is scaled byset_radius_damping_curve()and cached in each joint setting in the joint list.
voidset_radius_damping_curve(index:int, curve:Curve)🔗
Sets the joint radius damping curve of the bone chain.
voidset_root_bone(index:int, bone:int)🔗
Sets the root bone index of the bone chain.
voidset_root_bone_name(index:int, bone_name:String)🔗
Sets the root bone name of the bone chain.
voidset_rotation_axis(index:int, axis:RotationAxis)🔗
Sets the rotation axis of the bone chain. If set to a specific axis, it acts like a hinge joint. The value is cached in each joint setting in the joint list.
The axes are based on theSkeleton3D.get_bone_rest()'s space, ifaxisisSkeletonModifier3D.ROTATION_AXIS_CUSTOM, you can specify any axis.
Note:The rotation axis vector and the forward vector shouldn't be colinear to avoid unintended rotation sinceSpringBoneSimulator3Ddoes not factor in twisting forces.
voidset_rotation_axis_vector(index:int, vector:Vector3)🔗
Sets the rotation axis vector of the bone chain. The value is cached in each joint setting in the joint list.
This vector is normalized by an internal process and represents the axis around which the bone chain can rotate.
If the vector length is0, it is considered synonymous withSkeletonModifier3D.ROTATION_AXIS_ALL.
voidset_stiffness(index:int, stiffness:float)🔗
Sets the stiffness force of the bone chain. The greater the value, the faster it recovers to its initial pose.
Ifstiffnessis0, the modified pose will not return to the original pose.
The value is scaled byset_stiffness_damping_curve()and cached in each joint setting in the joint list.
voidset_stiffness_damping_curve(index:int, curve:Curve)🔗
Sets the stiffness force damping curve of the bone chain.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
