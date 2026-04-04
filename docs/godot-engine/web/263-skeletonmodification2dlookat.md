# SkeletonModification2DLookAt

# SkeletonModification2DLookAt
Experimental:This class may be changed or removed in future versions.
Inherits:SkeletonModification2D<Resource<RefCounted<Object
A modification that rotates aBone2Dnode to look at a target.

## Description
ThisSkeletonModification2Drotates a bone to look a target. This is extremely helpful for moving character's head to look at the player, rotating a turret to look at a target, or any other case where you want to make a bone rotate towards something quickly and easily.

## Properties

| NodePath | bone2d_node | NodePath("") |
|---|---|---|
| int | bone_index | -1 |
| NodePath | target_nodepath | NodePath("") |

NodePath
bone2d_node
NodePath("")
bone_index
NodePath
target_nodepath
NodePath("")

## Methods

| float | get_additional_rotation()const |
|---|---|
| bool | get_constraint_angle_invert()const |
| float | get_constraint_angle_max()const |
| float | get_constraint_angle_min()const |
| bool | get_enable_constraint()const |
| void | set_additional_rotation(rotation:float) |
| void | set_constraint_angle_invert(invert:bool) |
| void | set_constraint_angle_max(angle_max:float) |
| void | set_constraint_angle_min(angle_min:float) |
| void | set_enable_constraint(enable_constraint:bool) |

float
get_additional_rotation()const
bool
get_constraint_angle_invert()const
float
get_constraint_angle_max()const
float
get_constraint_angle_min()const
bool
get_enable_constraint()const
void
set_additional_rotation(rotation:float)
void
set_constraint_angle_invert(invert:bool)
void
set_constraint_angle_max(angle_max:float)
void
set_constraint_angle_min(angle_min:float)
void
set_enable_constraint(enable_constraint:bool)

## Property Descriptions
NodePathbone2d_node=NodePath("")🔗
- voidset_bone2d_node(value:NodePath)
voidset_bone2d_node(value:NodePath)
- NodePathget_bone2d_node()
NodePathget_bone2d_node()
TheBone2Dnode that the modification will operate on.
intbone_index=-1🔗
- voidset_bone_index(value:int)
voidset_bone_index(value:int)
- intget_bone_index()
intget_bone_index()
The index of theBone2Dnode that the modification will operate on.
NodePathtarget_nodepath=NodePath("")🔗
- voidset_target_node(value:NodePath)
voidset_target_node(value:NodePath)
- NodePathget_target_node()
NodePathget_target_node()
The NodePath to the node that is the target for the LookAt modification. This node is what the modification will rotate theBone2Dto.

## Method Descriptions
floatget_additional_rotation()const🔗
Returns the amount of additional rotation that is applied after the LookAt modification executes.
boolget_constraint_angle_invert()const🔗
Returns whether the constraints to this modification are inverted or not.
floatget_constraint_angle_max()const🔗
Returns the constraint's maximum allowed angle.
floatget_constraint_angle_min()const🔗
Returns the constraint's minimum allowed angle.
boolget_enable_constraint()const🔗
Returnstrueif the LookAt modification is using constraints.
voidset_additional_rotation(rotation:float)🔗
Sets the amount of additional rotation that is to be applied after executing the modification. This allows for offsetting the results by the inputted rotation amount.
voidset_constraint_angle_invert(invert:bool)🔗
Whentrue, the modification will use an inverted joint constraint.
An inverted joint constraint only constraints theBone2Dto the anglesoutside ofthe inputted minimum and maximum angles. For this reason, it is referred to as an inverted joint constraint, as it constraints the joint to the outside of the inputted values.
voidset_constraint_angle_max(angle_max:float)🔗
Sets the constraint's maximum allowed angle.
voidset_constraint_angle_min(angle_min:float)🔗
Sets the constraint's minimum allowed angle.
voidset_enable_constraint(enable_constraint:bool)🔗
Sets whether this modification will use constraints or not. Whentrue, constraints will be applied when solving the LookAt modification.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.