# TwoBoneIK3D

# TwoBoneIK3D
Inherits:IKModifier3D<SkeletonModifier3D<Node3D<Node<Object
Rotation based intersection of two circles inverse kinematics solver.

## Description
ThisIKModifier3Drequires a pole target. It provides deterministic results by constructing a plane from each joint and pole target and finding the intersection of two circles (disks in 3D).
This IK can handle twist by setting the pole direction. If there are more than one bone between each set bone, their rotations are ignored, and the straight line connecting the root-middle and middle-end joints are treated as virtual bones.

## Properties

| int | setting_count | 0 |

setting_count

## Methods

| int | get_end_bone(index:int)const |
|---|---|
| BoneDirection | get_end_bone_direction(index:int)const |
| float | get_end_bone_length(index:int)const |
| String | get_end_bone_name(index:int)const |
| int | get_middle_bone(index:int)const |
| String | get_middle_bone_name(index:int)const |
| SecondaryDirection | get_pole_direction(index:int)const |
| Vector3 | get_pole_direction_vector(index:int)const |
| NodePath | get_pole_node(index:int)const |
| int | get_root_bone(index:int)const |
| String | get_root_bone_name(index:int)const |
| NodePath | get_target_node(index:int)const |
| bool | is_end_bone_extended(index:int)const |
| bool | is_using_virtual_end(index:int)const |
| void | set_end_bone(index:int, bone:int) |
| void | set_end_bone_direction(index:int, bone_direction:BoneDirection) |
| void | set_end_bone_length(index:int, length:float) |
| void | set_end_bone_name(index:int, bone_name:String) |
| void | set_extend_end_bone(index:int, enabled:bool) |
| void | set_middle_bone(index:int, bone:int) |
| void | set_middle_bone_name(index:int, bone_name:String) |
| void | set_pole_direction(index:int, direction:SecondaryDirection) |
| void | set_pole_direction_vector(index:int, vector:Vector3) |
| void | set_pole_node(index:int, pole_node:NodePath) |
| void | set_root_bone(index:int, bone:int) |
| void | set_root_bone_name(index:int, bone_name:String) |
| void | set_target_node(index:int, target_node:NodePath) |
| void | set_use_virtual_end(index:int, enabled:bool) |

get_end_bone(index:int)const
BoneDirection
get_end_bone_direction(index:int)const
float
get_end_bone_length(index:int)const
String
get_end_bone_name(index:int)const
get_middle_bone(index:int)const
String
get_middle_bone_name(index:int)const
SecondaryDirection
get_pole_direction(index:int)const
Vector3
get_pole_direction_vector(index:int)const
NodePath
get_pole_node(index:int)const
get_root_bone(index:int)const
String
get_root_bone_name(index:int)const
NodePath
get_target_node(index:int)const
bool
is_end_bone_extended(index:int)const
bool
is_using_virtual_end(index:int)const
void
set_end_bone(index:int, bone:int)
void
set_end_bone_direction(index:int, bone_direction:BoneDirection)
void
set_end_bone_length(index:int, length:float)
void
set_end_bone_name(index:int, bone_name:String)
void
set_extend_end_bone(index:int, enabled:bool)
void
set_middle_bone(index:int, bone:int)
void
set_middle_bone_name(index:int, bone_name:String)
void
set_pole_direction(index:int, direction:SecondaryDirection)
void
set_pole_direction_vector(index:int, vector:Vector3)
void
set_pole_node(index:int, pole_node:NodePath)
void
set_root_bone(index:int, bone:int)
void
set_root_bone_name(index:int, bone_name:String)
void
set_target_node(index:int, target_node:NodePath)
void
set_use_virtual_end(index:int, enabled:bool)

## Property Descriptions
intsetting_count=0🔗
- voidset_setting_count(value:int)
voidset_setting_count(value:int)
- intget_setting_count()
intget_setting_count()
The number of settings.

## Method Descriptions
intget_end_bone(index:int)const🔗
Returns the end bone index.
BoneDirectionget_end_bone_direction(index:int)const🔗
Returns the end bone's tail direction whenis_end_bone_extended()istrue.
floatget_end_bone_length(index:int)const🔗
Returns the end bone tail length of the bone chain whenis_end_bone_extended()istrue.
Stringget_end_bone_name(index:int)const🔗
Returns the end bone name.
intget_middle_bone(index:int)const🔗
Returns the middle bone index.
Stringget_middle_bone_name(index:int)const🔗
Returns the middle bone name.
SecondaryDirectionget_pole_direction(index:int)const🔗
Returns the pole direction.
Vector3get_pole_direction_vector(index:int)const🔗
Returns the pole direction vector.
Ifget_pole_direction()isSkeletonModifier3D.SECONDARY_DIRECTION_NONE, this method returnsVector3(0,0,0).
NodePathget_pole_node(index:int)const🔗
Returns the pole target node that constructs a plane which the joints are all on and the pole is trying to direct.
intget_root_bone(index:int)const🔗
Returns the root bone index.
Stringget_root_bone_name(index:int)const🔗
Returns the root bone name.
NodePathget_target_node(index:int)const🔗
Returns the target node that the end bone is trying to reach.
boolis_end_bone_extended(index:int)const🔗
Returnstrueif the end bone is extended to have a tail.
boolis_using_virtual_end(index:int)const🔗
Returnstrueif the end bone is extended from the middle bone as a virtual bone.
voidset_end_bone(index:int, bone:int)🔗
Sets the end bone index.
voidset_end_bone_direction(index:int, bone_direction:BoneDirection)🔗
Sets the end bone tail direction whenis_end_bone_extended()istrue.
voidset_end_bone_length(index:int, length:float)🔗
Sets the end bone tail length whenis_end_bone_extended()istrue.
voidset_end_bone_name(index:int, bone_name:String)🔗
Sets the end bone name.
Note:The end bone must be a child of the middle bone.
voidset_extend_end_bone(index:int, enabled:bool)🔗
Ifenabledistrue, the end bone is extended to have a tail.
voidset_middle_bone(index:int, bone:int)🔗
Sets the middle bone index.
voidset_middle_bone_name(index:int, bone_name:String)🔗
Sets the middle bone name.
Note:The middle bone must be a child of the root bone.
voidset_pole_direction(index:int, direction:SecondaryDirection)🔗
Sets the pole direction.
The pole is on the middle bone and will direct to the pole target.
The rotation axis is a vector that is orthogonal to this and the forward vector.
Note:The pole direction and the forward vector shouldn't be colinear to avoid unintended rotation.
voidset_pole_direction_vector(index:int, vector:Vector3)🔗
Sets the pole direction vector.
This vector is normalized by an internal process.
If the vector length is0, it is considered synonymous withSkeletonModifier3D.SECONDARY_DIRECTION_NONE.
voidset_pole_node(index:int, pole_node:NodePath)🔗
Sets the pole target node that constructs a plane which the joints are all on and the pole is trying to direct.
voidset_root_bone(index:int, bone:int)🔗
Sets the root bone index.
voidset_root_bone_name(index:int, bone_name:String)🔗
Sets the root bone name.
voidset_target_node(index:int, target_node:NodePath)🔗
Sets the target node that the end bone is trying to reach.
voidset_use_virtual_end(index:int, enabled:bool)🔗
Ifenabledistrue, the end bone is extended from the middle bone as a virtual bone.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.