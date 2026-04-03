# SkeletonModification2DTwoBoneIK in English

# SkeletonModification2DTwoBoneIK
Experimental:This class may be changed or removed in future versions.
Inherits:SkeletonModification2D<Resource<RefCounted<Object
A modification that rotates two bones using the law of cosines to reach the target.

## Description
ThisSkeletonModification2Duses an algorithm typically called TwoBoneIK. This algorithm works by leveraging the law of cosines and the lengths of the bones to figure out what rotation the bones currently have, and what rotation they need to make a complete triangle, where the first bone, the second bone, and the target form the three vertices of the triangle. Because the algorithm works by making a triangle, it can only operate on two bones.
TwoBoneIK is great for arms, legs, and really any joints that can be represented by just two bones that bend to reach a target. This solver is more lightweight thanSkeletonModification2DFABRIK, but gives similar, natural looking results.

## Properties

| bool | flip_bend_direction | false |
|---|---|---|
| float | target_maximum_distance | 0.0 |
| float | target_minimum_distance | 0.0 |
| NodePath | target_nodepath | NodePath("") |

bool
flip_bend_direction
false
float
target_maximum_distance
float
target_minimum_distance
NodePath
target_nodepath
NodePath("")

## Methods

| NodePath | get_joint_one_bone2d_node()const |
|---|---|
| int | get_joint_one_bone_idx()const |
| NodePath | get_joint_two_bone2d_node()const |
| int | get_joint_two_bone_idx()const |
| void | set_joint_one_bone2d_node(bone2d_node:NodePath) |
| void | set_joint_one_bone_idx(bone_idx:int) |
| void | set_joint_two_bone2d_node(bone2d_node:NodePath) |
| void | set_joint_two_bone_idx(bone_idx:int) |

NodePath
get_joint_one_bone2d_node()const
get_joint_one_bone_idx()const
NodePath
get_joint_two_bone2d_node()const
get_joint_two_bone_idx()const
void
set_joint_one_bone2d_node(bone2d_node:NodePath)
void
set_joint_one_bone_idx(bone_idx:int)
void
set_joint_two_bone2d_node(bone2d_node:NodePath)
void
set_joint_two_bone_idx(bone_idx:int)

## Property Descriptions
boolflip_bend_direction=false🔗
- voidset_flip_bend_direction(value:bool)
voidset_flip_bend_direction(value:bool)
- boolget_flip_bend_direction()
boolget_flip_bend_direction()
Iftrue, the bones in the modification will bend outward as opposed to inwards when contracting. Iffalse, the bones will bend inwards when contracting.
floattarget_maximum_distance=0.0🔗
- voidset_target_maximum_distance(value:float)
voidset_target_maximum_distance(value:float)
- floatget_target_maximum_distance()
floatget_target_maximum_distance()
The maximum distance the target can be at. If the target is farther than this distance, the modification will solve as if it's at this maximum distance. When set to0, the modification will solve without distance constraints.
floattarget_minimum_distance=0.0🔗
- voidset_target_minimum_distance(value:float)
voidset_target_minimum_distance(value:float)
- floatget_target_minimum_distance()
floatget_target_minimum_distance()
The minimum distance the target can be at. If the target is closer than this distance, the modification will solve as if it's at this minimum distance. When set to0, the modification will solve without distance constraints.
NodePathtarget_nodepath=NodePath("")🔗
- voidset_target_node(value:NodePath)
voidset_target_node(value:NodePath)
- NodePathget_target_node()
NodePathget_target_node()
The NodePath to the node that is the target for the TwoBoneIK modification. This node is what the modification will use when bending theBone2Dnodes.

## Method Descriptions
NodePathget_joint_one_bone2d_node()const🔗
Returns theBone2Dnode that is being used as the first bone in the TwoBoneIK modification.
intget_joint_one_bone_idx()const🔗
Returns the index of theBone2Dnode that is being used as the first bone in the TwoBoneIK modification.
NodePathget_joint_two_bone2d_node()const🔗
Returns theBone2Dnode that is being used as the second bone in the TwoBoneIK modification.
intget_joint_two_bone_idx()const🔗
Returns the index of theBone2Dnode that is being used as the second bone in the TwoBoneIK modification.
voidset_joint_one_bone2d_node(bone2d_node:NodePath)🔗
Sets theBone2Dnode that is being used as the first bone in the TwoBoneIK modification.
voidset_joint_one_bone_idx(bone_idx:int)🔗
Sets the index of theBone2Dnode that is being used as the first bone in the TwoBoneIK modification.
voidset_joint_two_bone2d_node(bone2d_node:NodePath)🔗
Sets theBone2Dnode that is being used as the second bone in the TwoBoneIK modification.
voidset_joint_two_bone_idx(bone_idx:int)🔗
Sets the index of theBone2Dnode that is being used as the second bone in the TwoBoneIK modification.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.