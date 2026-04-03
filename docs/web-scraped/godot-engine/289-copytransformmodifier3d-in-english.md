# CopyTransformModifier3D in English

# CopyTransformModifier3D
Inherits:BoneConstraint3D<SkeletonModifier3D<Node3D<Node<Object
ASkeletonModifier3Dthat apply transform to the bone which copied from reference.

## Description
Apply the copied transform of the bone set byBoneConstraint3D.set_reference_bone()to the bone set byBoneConstraint3D.set_apply_bone()with processing it with some masks and options.
There are 4 ways to apply the transform, depending on the combination ofset_relative()andset_additive().
Relative + Additive:
- Extract reference pose relative to the rest and add it to the apply bone's pose.
Extract reference pose relative to the rest and add it to the apply bone's pose.
Relative + Not Additive:
- Extract reference pose relative to the rest and add it to the apply bone's rest.
Extract reference pose relative to the rest and add it to the apply bone's rest.
Not Relative + Additive:
- Extract reference pose absolutely and add it to the apply bone's pose.
Extract reference pose absolutely and add it to the apply bone's pose.
Not Relative + Not Additive:
- Extract reference pose absolutely and the apply bone's pose is replaced with it.
Extract reference pose absolutely and the apply bone's pose is replaced with it.
Note:Relative option is available only in the caseBoneConstraint3D.get_reference_type()isBoneConstraint3D.REFERENCE_TYPE_BONE. See alsoReferenceType.

## Properties

| int | setting_count | 0 |

setting_count

## Methods

| BitField[AxisFlag] | get_axis_flags(index:int)const |
|---|---|
| BitField[TransformFlag] | get_copy_flags(index:int)const |
| BitField[AxisFlag] | get_invert_flags(index:int)const |
| bool | is_additive(index:int)const |
| bool | is_axis_x_enabled(index:int)const |
| bool | is_axis_x_inverted(index:int)const |
| bool | is_axis_y_enabled(index:int)const |
| bool | is_axis_y_inverted(index:int)const |
| bool | is_axis_z_enabled(index:int)const |
| bool | is_axis_z_inverted(index:int)const |
| bool | is_position_copying(index:int)const |
| bool | is_relative(index:int)const |
| bool | is_rotation_copying(index:int)const |
| bool | is_scale_copying(index:int)const |
| void | set_additive(index:int, enabled:bool) |
| void | set_axis_flags(index:int, axis_flags:BitField[AxisFlag]) |
| void | set_axis_x_enabled(index:int, enabled:bool) |
| void | set_axis_x_inverted(index:int, enabled:bool) |
| void | set_axis_y_enabled(index:int, enabled:bool) |
| void | set_axis_y_inverted(index:int, enabled:bool) |
| void | set_axis_z_enabled(index:int, enabled:bool) |
| void | set_axis_z_inverted(index:int, enabled:bool) |
| void | set_copy_flags(index:int, copy_flags:BitField[TransformFlag]) |
| void | set_copy_position(index:int, enabled:bool) |
| void | set_copy_rotation(index:int, enabled:bool) |
| void | set_copy_scale(index:int, enabled:bool) |
| void | set_invert_flags(index:int, axis_flags:BitField[AxisFlag]) |
| void | set_relative(index:int, enabled:bool) |

BitField[AxisFlag]
get_axis_flags(index:int)const
BitField[TransformFlag]
get_copy_flags(index:int)const
BitField[AxisFlag]
get_invert_flags(index:int)const
bool
is_additive(index:int)const
bool
is_axis_x_enabled(index:int)const
bool
is_axis_x_inverted(index:int)const
bool
is_axis_y_enabled(index:int)const
bool
is_axis_y_inverted(index:int)const
bool
is_axis_z_enabled(index:int)const
bool
is_axis_z_inverted(index:int)const
bool
is_position_copying(index:int)const
bool
is_relative(index:int)const
bool
is_rotation_copying(index:int)const
bool
is_scale_copying(index:int)const
void
set_additive(index:int, enabled:bool)
void
set_axis_flags(index:int, axis_flags:BitField[AxisFlag])
void
set_axis_x_enabled(index:int, enabled:bool)
void
set_axis_x_inverted(index:int, enabled:bool)
void
set_axis_y_enabled(index:int, enabled:bool)
void
set_axis_y_inverted(index:int, enabled:bool)
void
set_axis_z_enabled(index:int, enabled:bool)
void
set_axis_z_inverted(index:int, enabled:bool)
void
set_copy_flags(index:int, copy_flags:BitField[TransformFlag])
void
set_copy_position(index:int, enabled:bool)
void
set_copy_rotation(index:int, enabled:bool)
void
set_copy_scale(index:int, enabled:bool)
void
set_invert_flags(index:int, axis_flags:BitField[AxisFlag])
void
set_relative(index:int, enabled:bool)

## Enumerations
flagsTransformFlag:🔗
TransformFlagTRANSFORM_FLAG_POSITION=1
If set, allows to copy the position.
TransformFlagTRANSFORM_FLAG_ROTATION=2
If set, allows to copy the rotation.
TransformFlagTRANSFORM_FLAG_SCALE=4
If set, allows to copy the scale.
TransformFlagTRANSFORM_FLAG_ALL=7
If set, allows to copy the position/rotation/scale.
flagsAxisFlag:🔗
AxisFlagAXIS_FLAG_X=1
If set, allows to process the X-axis.
AxisFlagAXIS_FLAG_Y=2
If set, allows to process the Y-axis.
AxisFlagAXIS_FLAG_Z=4
If set, allows to process the Z-axis.
AxisFlagAXIS_FLAG_ALL=7
If set, allows to process the all axes.

## Property Descriptions
intsetting_count=0🔗
- voidset_setting_count(value:int)
voidset_setting_count(value:int)
- intget_setting_count()
intget_setting_count()
The number of settings in the modifier.

## Method Descriptions
BitField[AxisFlag]get_axis_flags(index:int)const🔗
Returns the axis flags of the setting atindex.
BitField[TransformFlag]get_copy_flags(index:int)const🔗
Returns the copy flags of the setting atindex.
BitField[AxisFlag]get_invert_flags(index:int)const🔗
Returns the invert flags of the setting atindex.
boolis_additive(index:int)const🔗
Returnstrueif the additive option is enabled in the setting atindex.
boolis_axis_x_enabled(index:int)const🔗
Returnstrueif the enable flags has the flag for the X-axis in the setting atindex. See alsoset_axis_flags().
boolis_axis_x_inverted(index:int)const🔗
Returnstrueif the invert flags has the flag for the X-axis in the setting atindex. See alsoset_invert_flags().
boolis_axis_y_enabled(index:int)const🔗
Returnstrueif the enable flags has the flag for the Y-axis in the setting atindex. See alsoset_axis_flags().
boolis_axis_y_inverted(index:int)const🔗
Returnstrueif the invert flags has the flag for the Y-axis in the setting atindex. See alsoset_invert_flags().
boolis_axis_z_enabled(index:int)const🔗
Returnstrueif the enable flags has the flag for the Z-axis in the setting atindex. See alsoset_axis_flags().
boolis_axis_z_inverted(index:int)const🔗
Returnstrueif the invert flags has the flag for the Z-axis in the setting atindex. See alsoset_invert_flags().
boolis_position_copying(index:int)const🔗
Returnstrueif the copy flags has the flag for the position in the setting atindex. See alsoset_copy_flags().
boolis_relative(index:int)const🔗
Returnstrueif the relative option is enabled in the setting atindex.
boolis_rotation_copying(index:int)const🔗
Returnstrueif the copy flags has the flag for the rotation in the setting atindex. See alsoset_copy_flags().
boolis_scale_copying(index:int)const🔗
Returnstrueif the copy flags has the flag for the scale in the setting atindex. See alsoset_copy_flags().
voidset_additive(index:int, enabled:bool)🔗
Sets additive option in the setting atindextoenabled. This mainly affects the process of applying transform to theBoneConstraint3D.set_apply_bone().
If setsenabledtotrue, the processed transform is added to the pose of the current apply bone.
If setsenabledtofalse, the pose of the current apply bone is replaced with the processed transform. However, if setset_relative()totrue, the transform is relative to rest.
voidset_axis_flags(index:int, axis_flags:BitField[AxisFlag])🔗
Sets the flags to copy axes. If the flag is valid, the axis is copied.
voidset_axis_x_enabled(index:int, enabled:bool)🔗
If setsenabledtotrue, the X-axis will be copied.
voidset_axis_x_inverted(index:int, enabled:bool)🔗
If setsenabledtotrue, the X-axis will be inverted.
voidset_axis_y_enabled(index:int, enabled:bool)🔗
If setsenabledtotrue, the Y-axis will be copied.
voidset_axis_y_inverted(index:int, enabled:bool)🔗
If setsenabledtotrue, the Y-axis will be inverted.
voidset_axis_z_enabled(index:int, enabled:bool)🔗
If setsenabledtotrue, the Z-axis will be copied.
voidset_axis_z_inverted(index:int, enabled:bool)🔗
If setsenabledtotrue, the Z-axis will be inverted.
voidset_copy_flags(index:int, copy_flags:BitField[TransformFlag])🔗
Sets the flags to process the transform operations. If the flag is valid, the transform operation is processed.
Note:If the rotation is valid for only one axis, it respects the roll of the valid axis. If the rotation is valid for two axes, it discards the roll of the invalid axis.
voidset_copy_position(index:int, enabled:bool)🔗
If setsenabledtotrue, the position will be copied.
voidset_copy_rotation(index:int, enabled:bool)🔗
If setsenabledtotrue, the rotation will be copied.
voidset_copy_scale(index:int, enabled:bool)🔗
If setsenabledtotrue, the scale will be copied.
voidset_invert_flags(index:int, axis_flags:BitField[AxisFlag])🔗
Sets the flags to inverte axes. If the flag is valid, the axis is copied.
Note:An inverted scale means an inverse number, not a negative scale. For example, inverting2.0means0.5.
Note:An inverted rotation flips the elements of the quaternion. For example, a two-axis inversion will flip the roll of each axis, and a three-axis inversion will flip the final orientation. However, be aware that flipping only one axis may cause unintended rotation by the unflipped axes, due to the characteristics of the quaternion.
voidset_relative(index:int, enabled:bool)🔗
Sets relative option in the setting atindextoenabled.
If setsenabledtotrue, the extracted and applying transform is relative to the rest.
If setsenabledtofalse, the extracted transform is absolute.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.