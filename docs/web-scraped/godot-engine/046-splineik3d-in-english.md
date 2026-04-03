# SplineIK3D in English

# SplineIK3D
Inherits:ChainIK3D<IKModifier3D<SkeletonModifier3D<Node3D<Node<Object
ASkeletonModifier3Dfor aligning bones along aPath3D.

## Description
ASkeletonModifier3Dfor aligning bones along aPath3D. The smoothness of the fitting depends on theCurve3D.bake_interval.
If you want thePath3Dto attach to a specific bone, it is recommended to place aModifierBoneTarget3Dbefore theSplineIK3Din theSkeletonModifier3Dlist (children of theSkeleton3D), and then place aPath3Das theModifierBoneTarget3D's child.
Bone twist is determined based on theCurve3D.get_point_tilt().
If the root bone joint and the start point of theCurve3Dare separated, it assumes that there is a linear line segment between them. This means that the vector pointing toward the start point of theCurve3Dtakes precedence over the shortest intersection point along theCurve3D.
If the end bone joint exceeds the path length, it is bent as close as possible to the end point of theCurve3D.

## Properties

| int | setting_count | 0 |

setting_count

## Methods

| NodePath | get_path_3d(index:int)const |
|---|---|
| int | get_tilt_fade_in(index:int)const |
| int | get_tilt_fade_out(index:int)const |
| bool | is_tilt_enabled(index:int)const |
| void | set_path_3d(index:int, path_3d:NodePath) |
| void | set_tilt_enabled(index:int, enabled:bool) |
| void | set_tilt_fade_in(index:int, size:int) |
| void | set_tilt_fade_out(index:int, size:int) |

NodePath
get_path_3d(index:int)const
get_tilt_fade_in(index:int)const
get_tilt_fade_out(index:int)const
bool
is_tilt_enabled(index:int)const
void
set_path_3d(index:int, path_3d:NodePath)
void
set_tilt_enabled(index:int, enabled:bool)
void
set_tilt_fade_in(index:int, size:int)
void
set_tilt_fade_out(index:int, size:int)

## Property Descriptions
intsetting_count=0🔗
- voidset_setting_count(value:int)
voidset_setting_count(value:int)
- intget_setting_count()
intget_setting_count()
The number of settings.

## Method Descriptions
NodePathget_path_3d(index:int)const🔗
Returns the node path of thePath3Dwhich is describing the path.
intget_tilt_fade_in(index:int)const🔗
Returns the tilt interpolation method used between the root bone and the start point of theCurve3Dwhen they are apart. See alsoset_tilt_fade_in().
intget_tilt_fade_out(index:int)const🔗
Returns the tilt interpolation method used between the end bone and the end point of theCurve3Dwhen they are apart. See alsoset_tilt_fade_out().
boolis_tilt_enabled(index:int)const🔗
Returns if the tilt property of theCurve3Daffects the bone twist.
voidset_path_3d(index:int, path_3d:NodePath)🔗
Sets the node path of thePath3Dwhich is describing the path.
voidset_tilt_enabled(index:int, enabled:bool)🔗
Sets if the tilt property of theCurve3Dshould affect the bone twist.
voidset_tilt_fade_in(index:int, size:int)🔗
Ifsizeis greater than0, the tilt is interpolated betweensizestart bones from the start point of theCurve3Dwhen they are apart.
Ifsizeis equal0, the tilts between the root bone head and the start point of theCurve3Dare unified with a tilt of the start point of theCurve3D.
Ifsizeis less than0, the tilts between the root bone and the start point of theCurve3Dare0.0.
voidset_tilt_fade_out(index:int, size:int)🔗
Ifsizeis greater than0, the tilt is interpolated betweensizeend bones from the end point of theCurve3Dwhen they are apart.
Ifsizeis equal0, the tilts between the end bone tail and the end point of theCurve3Dare unified with a tilt of the end point of theCurve3D.
Ifsizeis less than0, the tilts between the end bone and the end point of theCurve3Dare0.0.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.