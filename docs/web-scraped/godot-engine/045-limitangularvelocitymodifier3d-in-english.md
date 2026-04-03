# LimitAngularVelocityModifier3D in English

# LimitAngularVelocityModifier3D
Inherits:SkeletonModifier3D<Node3D<Node<Object
Limit bone rotation angular velocity.

## Description
This modifier limits bone rotation angular velocity by comparing poses between previous and current frame.
You can add bone chains by specifying their root and end bones, then add the bones between them to a list. Modifier processes either that list or the bones excluding those in the list depending on the optionexclude.

## Properties

| int | chain_count | 0 |
|---|---|---|
| bool | exclude | false |
| int | joint_count | 0 |
| float | max_angular_velocity | 6.2831855 |

chain_count
bool
exclude
false
joint_count
float
max_angular_velocity
6.2831855

## Methods

| void | clear_chains() |
|---|---|
| int | get_end_bone(index:int)const |
| String | get_end_bone_name(index:int)const |
| int | get_root_bone(index:int)const |
| String | get_root_bone_name(index:int)const |
| void | reset() |
| void | set_end_bone(index:int, bone:int) |
| void | set_end_bone_name(index:int, bone_name:String) |
| void | set_root_bone(index:int, bone:int) |
| void | set_root_bone_name(index:int, bone_name:String) |

void
clear_chains()
get_end_bone(index:int)const
String
get_end_bone_name(index:int)const
get_root_bone(index:int)const
String
get_root_bone_name(index:int)const
void
reset()
void
set_end_bone(index:int, bone:int)
void
set_end_bone_name(index:int, bone_name:String)
void
set_root_bone(index:int, bone:int)
void
set_root_bone_name(index:int, bone_name:String)

## Property Descriptions
intchain_count=0🔗
- voidset_chain_count(value:int)
voidset_chain_count(value:int)
- intget_chain_count()
intget_chain_count()
The number of chains.
boolexclude=false🔗
- voidset_exclude(value:bool)
voidset_exclude(value:bool)
- boolis_exclude()
boolis_exclude()
Iftrue, the modifier processes bones not included in the bone list.
Iffalse, the bones processed by the modifier are equal to the bone list.
intjoint_count=0🔗
The number of joints in the list which created by chains dynamically.
floatmax_angular_velocity=6.2831855🔗
- voidset_max_angular_velocity(value:float)
voidset_max_angular_velocity(value:float)
- floatget_max_angular_velocity()
floatget_max_angular_velocity()
The maximum angular velocity per second.

## Method Descriptions
voidclear_chains()🔗
Clear all chains.
intget_end_bone(index:int)const🔗
Returns the end bone index of the bone chain.
Stringget_end_bone_name(index:int)const🔗
Returns the end bone name of the bone chain.
intget_root_bone(index:int)const🔗
Returns the root bone index of the bone chain.
Stringget_root_bone_name(index:int)const🔗
Returns the root bone name of the bone chain.
voidreset()🔗
Sets the reference pose for angle comparison to the current pose with the influence of constraints removed. This function is automatically triggered when joints change or upon activation.
voidset_end_bone(index:int, bone:int)🔗
Sets the end bone index of the bone chain.
voidset_end_bone_name(index:int, bone_name:String)🔗
Sets the end bone name of the bone chain.
Note:End bone must be the root bone or a child of the root bone.
voidset_root_bone(index:int, bone:int)🔗
Sets the root bone index of the bone chain.
voidset_root_bone_name(index:int, bone_name:String)🔗
Sets the root bone name of the bone chain.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.