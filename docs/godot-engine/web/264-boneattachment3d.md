# BoneAttachment3D

# BoneAttachment3D
Inherits:Node3D<Node<Object
А node that dynamically copies or overrides the 3D transform of a bone in its parentSkeleton3D.

## Description
This node selects a bone in aSkeleton3Dand attaches to it. This means that theBoneAttachment3Dnode will either dynamically copy or override the 3D transform of the selected bone.

## Properties

| int | bone_idx | -1 |
|---|---|---|
| String | bone_name | "" |
| NodePath | external_skeleton |  |
| bool | override_pose | false |
| PhysicsInterpolationMode | physics_interpolation_mode | 2(overridesNode) |
| bool | use_external_skeleton | false |

bone_idx
String
bone_name
NodePath
external_skeleton
bool
override_pose
false
PhysicsInterpolationMode
physics_interpolation_mode
2(overridesNode)
bool
use_external_skeleton
false

## Methods

| Skeleton3D | get_skeleton() |
|---|---|
| void | on_skeleton_update() |

Skeleton3D
get_skeleton()
void
on_skeleton_update()

## Property Descriptions
intbone_idx=-1🔗
- voidset_bone_idx(value:int)
voidset_bone_idx(value:int)
- intget_bone_idx()
intget_bone_idx()
The index of the attached bone.
Stringbone_name=""🔗
- voidset_bone_name(value:String)
voidset_bone_name(value:String)
- Stringget_bone_name()
Stringget_bone_name()
The name of the attached bone.
NodePathexternal_skeleton🔗
- voidset_external_skeleton(value:NodePath)
voidset_external_skeleton(value:NodePath)
- NodePathget_external_skeleton()
NodePathget_external_skeleton()
TheNodePathto the externalSkeleton3Dnode.
booloverride_pose=false🔗
- voidset_override_pose(value:bool)
voidset_override_pose(value:bool)
- boolget_override_pose()
boolget_override_pose()
Whether theBoneAttachment3Dnode will override the bone pose of the bone it is attached to. When set totrue, theBoneAttachment3Dnode can change the pose of the bone. When set tofalse, theBoneAttachment3Dwill always be set to the bone's transform.
Note:This override performs interruptively in the skeleton update process using signals due to the old design. It may cause unintended behavior when used at the same time withSkeletonModifier3D.
booluse_external_skeleton=false🔗
- voidset_use_external_skeleton(value:bool)
voidset_use_external_skeleton(value:bool)
- boolget_use_external_skeleton()
boolget_use_external_skeleton()
Whether theBoneAttachment3Dnode will use an externalSkeleton3Dnode rather than attempting to use its parent node as theSkeleton3D. When set totrue, theBoneAttachment3Dnode will use the externalSkeleton3Dnode set inexternal_skeleton.

## Method Descriptions
Skeleton3Dget_skeleton()🔗
Returns the parent or externalSkeleton3Dnode if it exists, otherwise returnsnull.
voidon_skeleton_update()🔗
A function that is called automatically when theSkeleton3Dis updated. This function is where theBoneAttachment3Dnode updates its position so it is correctly bound when it isnotset to override the bone pose.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.