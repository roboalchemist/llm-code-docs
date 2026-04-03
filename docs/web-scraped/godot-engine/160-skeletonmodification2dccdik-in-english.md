# SkeletonModification2DCCDIK in English

# SkeletonModification2DCCDIK

Experimental:This class may be changed or removed in future versions.
Inherits:SkeletonModification2D<Resource<RefCounted<Object
A modification that uses CCDIK to manipulate a series of bones to reach a target in 2D.

## Description

ThisSkeletonModification2Duses an algorithm called Cyclic Coordinate Descent Inverse Kinematics, or CCDIK, to manipulate a chain of bones in aSkeleton2Dso it reaches a defined target.
CCDIK works by rotating a set of bones, typically called a "bone chain", on a single axis. Each bone is rotated to face the target from the tip (by default), which over a chain of bones allow it to rotate properly to reach the target. Because the bones only rotate on a single axis, CCDIKcanlook more robotic than other IK solvers.
Note:The CCDIK modifier hasccdik_joints, which are the data objects that hold the data for each joint in the CCDIK chain. This is different from a bone! CCDIK joints hold the data needed for each bone in the bone chain used by CCDIK.
CCDIK also fully supports angle constraints, allowing for more control over how a solution is met.

## Properties

| int | ccdik_data_chain_length | 0 |
|---|---|---|
| NodePath | target_nodepath | NodePath("") |
| NodePath | tip_nodepath | NodePath("") |

ccdik_data_chain_length
NodePath
target_nodepath
NodePath("")
NodePath
tip_nodepath
NodePath("")

## Methods

| NodePath | get_ccdik_joint_bone2d_node(joint_idx:int)const |
|---|---|
| int | get_ccdik_joint_bone_index(joint_idx:int)const |
| bool | get_ccdik_joint_constraint_angle_invert(joint_idx:int)const |
| float | get_ccdik_joint_constraint_angle_max(joint_idx:int)const |
| float | get_ccdik_joint_constraint_angle_min(joint_idx:int)const |
| bool | get_ccdik_joint_enable_constraint(joint_idx:int)const |
| bool | get_ccdik_joint_rotate_from_joint(joint_idx:int)const |
| void | set_ccdik_joint_bone2d_node(joint_idx:int, bone2d_nodepath:NodePath) |
| void | set_ccdik_joint_bone_index(joint_idx:int, bone_idx:int) |
| void | set_ccdik_joint_constraint_angle_invert(joint_idx:int, invert:bool) |
| void | set_ccdik_joint_constraint_angle_max(joint_idx:int, angle_max:float) |
| void | set_ccdik_joint_constraint_angle_min(joint_idx:int, angle_min:float) |
| void | set_ccdik_joint_enable_constraint(joint_idx:int, enable_constraint:bool) |
| void | set_ccdik_joint_rotate_from_joint(joint_idx:int, rotate_from_joint:bool) |

NodePath
get_ccdik_joint_bone2d_node(joint_idx:int)const
get_ccdik_joint_bone_index(joint_idx:int)const
bool
get_ccdik_joint_constraint_angle_invert(joint_idx:int)const
float
get_ccdik_joint_constraint_angle_max(joint_idx:int)const
float
get_ccdik_joint_constraint_angle_min(joint_idx:int)const
bool
get_ccdik_joint_enable_constraint(joint_idx:int)const
bool
get_ccdik_joint_rotate_from_joint(joint_idx:int)const
void
set_ccdik_joint_bone2d_node(joint_idx:int, bone2d_nodepath:NodePath)
void
set_ccdik_joint_bone_index(joint_idx:int, bone_idx:int)
void
set_ccdik_joint_constraint_angle_invert(joint_idx:int, invert:bool)
void
set_ccdik_joint_constraint_angle_max(joint_idx:int, angle_max:float)
void
set_ccdik_joint_constraint_angle_min(joint_idx:int, angle_min:float)
void
set_ccdik_joint_enable_constraint(joint_idx:int, enable_constraint:bool)
void
set_ccdik_joint_rotate_from_joint(joint_idx:int, rotate_from_joint:bool)

## Property Descriptions

intccdik_data_chain_length=0🔗

- voidset_ccdik_data_chain_length(value:int)
voidset_ccdik_data_chain_length(value:int)
- intget_ccdik_data_chain_length()
intget_ccdik_data_chain_length()
The number of CCDIK joints in the CCDIK modification.
NodePathtarget_nodepath=NodePath("")🔗
- voidset_target_node(value:NodePath)
voidset_target_node(value:NodePath)
- NodePathget_target_node()
NodePathget_target_node()
The NodePath to the node that is the target for the CCDIK modification. This node is what the CCDIK chain will attempt to rotate the bone chain to.
NodePathtip_nodepath=NodePath("")🔗
- voidset_tip_node(value:NodePath)
voidset_tip_node(value:NodePath)
- NodePathget_tip_node()
NodePathget_tip_node()
The end position of the CCDIK chain. Typically, this should be a child of aBone2Dnode attached to the finalBone2Din the CCDIK chain.

## Method Descriptions

NodePathget_ccdik_joint_bone2d_node(joint_idx:int)const🔗
Returns theBone2Dnode assigned to the CCDIK joint atjoint_idx.
intget_ccdik_joint_bone_index(joint_idx:int)const🔗
Returns the index of theBone2Dnode assigned to the CCDIK joint atjoint_idx.
boolget_ccdik_joint_constraint_angle_invert(joint_idx:int)const🔗
Returns whether the CCDIK joint atjoint_idxuses an inverted joint constraint. Seeset_ccdik_joint_constraint_angle_invert()for details.
floatget_ccdik_joint_constraint_angle_max(joint_idx:int)const🔗
Returns the maximum angle constraint for the joint atjoint_idx.
floatget_ccdik_joint_constraint_angle_min(joint_idx:int)const🔗
Returns the minimum angle constraint for the joint atjoint_idx.
boolget_ccdik_joint_enable_constraint(joint_idx:int)const🔗
Returns whether angle constraints on the CCDIK joint atjoint_idxare enabled.
boolget_ccdik_joint_rotate_from_joint(joint_idx:int)const🔗
Returns whether the joint atjoint_idxis set to rotate from the joint,true, or to rotate from the tip,false. The default is to rotate from the tip.
voidset_ccdik_joint_bone2d_node(joint_idx:int, bone2d_nodepath:NodePath)🔗
Sets theBone2Dnode assigned to the CCDIK joint atjoint_idx.
voidset_ccdik_joint_bone_index(joint_idx:int, bone_idx:int)🔗
Sets the bone index,bone_idx, of the CCDIK joint atjoint_idx. When possible, this will also update thebone2d_nodeof the CCDIK joint based on data provided by the linked skeleton.
voidset_ccdik_joint_constraint_angle_invert(joint_idx:int, invert:bool)🔗
Sets whether the CCDIK joint atjoint_idxuses an inverted joint constraint.
An inverted joint constraint only constraints the CCDIK joint to the anglesoutside ofthe inputted minimum and maximum angles. For this reason, it is referred to as an inverted joint constraint, as it constraints the joint to the outside of the inputted values.
voidset_ccdik_joint_constraint_angle_max(joint_idx:int, angle_max:float)🔗
Sets the maximum angle constraint for the joint atjoint_idx.
voidset_ccdik_joint_constraint_angle_min(joint_idx:int, angle_min:float)🔗
Sets the minimum angle constraint for the joint atjoint_idx.
voidset_ccdik_joint_enable_constraint(joint_idx:int, enable_constraint:bool)🔗
Determines whether angle constraints on the CCDIK joint atjoint_idxare enabled. Whentrue, constraints will be enabled and taken into account when solving.
voidset_ccdik_joint_rotate_from_joint(joint_idx:int, rotate_from_joint:bool)🔗
Sets whether the joint atjoint_idxis set to rotate from the joint,true, or to rotate from the tip,false.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
