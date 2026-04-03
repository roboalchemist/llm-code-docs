# RetargetModifier3D

# RetargetModifier3D
Inherits:SkeletonModifier3D<Node3D<Node<Object
A modifier to transfer parent skeleton poses (or global poses) to child skeletons in model space with different rests.

## Description
Retrieves the pose (or global pose) relative to the parent Skeleton's rest in model space and transfers it to the child Skeleton.
This modifier rewrites the pose of the child skeleton directly in the parent skeleton's update process. This means that it overwrites the mapped bone pose set in the normal process on the target skeleton. If you want to set the target skeleton bone pose after retargeting, you will need to add aSkeletonModifier3Dchild to the target skeleton and thereby modify the pose.
Note:When theuse_global_poseis enabled, even if it is an unmapped bone, it can cause visual problems because the global pose is applied ignoring the parent bone's poseif it has mapped bone children. See alsouse_global_pose.

## Properties

| BitField[TransformFlag] | enable | 7 |
|---|---|---|
| SkeletonProfile | profile |  |
| bool | use_global_pose | false |

BitField[TransformFlag]
enable
SkeletonProfile
profile
bool
use_global_pose
false

## Methods

| bool | is_position_enabled()const |
|---|---|
| bool | is_rotation_enabled()const |
| bool | is_scale_enabled()const |
| void | set_position_enabled(enabled:bool) |
| void | set_rotation_enabled(enabled:bool) |
| void | set_scale_enabled(enabled:bool) |

bool
is_position_enabled()const
bool
is_rotation_enabled()const
bool
is_scale_enabled()const
void
set_position_enabled(enabled:bool)
void
set_rotation_enabled(enabled:bool)
void
set_scale_enabled(enabled:bool)

## Enumerations
flagsTransformFlag:🔗
TransformFlagTRANSFORM_FLAG_POSITION=1
If set, allows to retarget the position.
TransformFlagTRANSFORM_FLAG_ROTATION=2
If set, allows to retarget the rotation.
TransformFlagTRANSFORM_FLAG_SCALE=4
If set, allows to retarget the scale.
TransformFlagTRANSFORM_FLAG_ALL=7
If set, allows to retarget the position/rotation/scale.

## Property Descriptions
BitField[TransformFlag]enable=7🔗
- voidset_enable_flags(value:BitField[TransformFlag])
voidset_enable_flags(value:BitField[TransformFlag])
- BitField[TransformFlag]get_enable_flags()
BitField[TransformFlag]get_enable_flags()
Flags to control the process of the transform elements individually whenuse_global_poseis disabled.
SkeletonProfileprofile🔗
- voidset_profile(value:SkeletonProfile)
voidset_profile(value:SkeletonProfile)
- SkeletonProfileget_profile()
SkeletonProfileget_profile()
SkeletonProfilefor retargeting bones with names matching the bone list.
booluse_global_pose=false🔗
- voidset_use_global_pose(value:bool)
voidset_use_global_pose(value:bool)
- boolis_using_global_pose()
boolis_using_global_pose()
Iffalse, in case the target skeleton has fewer bones than the source skeleton, the source bone parent's transform will be ignored.
Instead, it is possible to retarget between models with different body shapes, and position, rotation, and scale can be retargeted separately.
Iftrue, retargeting is performed taking into account global pose.
In case the target skeleton has fewer bones than the source skeleton, the source bone parent's transform is taken into account. However, bone length between skeletons must match exactly, if not, the bones will be forced to expand or shrink.
This is useful for using dummy bone with length0to match postures when retargeting between models with different number of bones.

## Method Descriptions
boolis_position_enabled()const🔗
ReturnstrueifenablehasTRANSFORM_FLAG_POSITION.
boolis_rotation_enabled()const🔗
ReturnstrueifenablehasTRANSFORM_FLAG_ROTATION.
boolis_scale_enabled()const🔗
ReturnstrueifenablehasTRANSFORM_FLAG_SCALE.
voidset_position_enabled(enabled:bool)🔗
SetsTRANSFORM_FLAG_POSITIONintoenable.
voidset_rotation_enabled(enabled:bool)🔗
SetsTRANSFORM_FLAG_ROTATIONintoenable.
voidset_scale_enabled(enabled:bool)🔗
SetsTRANSFORM_FLAG_SCALEintoenable.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.