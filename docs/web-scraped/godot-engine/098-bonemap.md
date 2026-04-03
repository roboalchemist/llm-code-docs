# BoneMap

# BoneMap

Inherits:Resource<RefCounted<Object
Describes a mapping of bone names for retargetingSkeleton3Dinto common names defined by aSkeletonProfile.

## Description

This class contains a dictionary that uses a list of bone names inSkeletonProfileas key names.
By assigning the actualSkeleton3Dbone name as the key value, it maps theSkeleton3Dto theSkeletonProfile.

## Tutorials

- Retargeting 3D Skeletons
Retargeting 3D Skeletons

## Properties

| SkeletonProfile | profile |

SkeletonProfile
profile

## Methods

| StringName | find_profile_bone_name(skeleton_bone_name:StringName)const |
|---|---|
| StringName | get_skeleton_bone_name(profile_bone_name:StringName)const |
| void | set_skeleton_bone_name(profile_bone_name:StringName, skeleton_bone_name:StringName) |

StringName
find_profile_bone_name(skeleton_bone_name:StringName)const
StringName
get_skeleton_bone_name(profile_bone_name:StringName)const
void
set_skeleton_bone_name(profile_bone_name:StringName, skeleton_bone_name:StringName)

## Signals

bone_map_updated()🔗
This signal is emitted when change the key value in theBoneMap. This is used to validate mapping and to updateBoneMapeditor.
profile_updated()🔗
This signal is emitted when change the value in profile or change the reference of profile. This is used to update key names in theBoneMapand to redraw theBoneMapeditor.

## Property Descriptions

SkeletonProfileprofile🔗

- voidset_profile(value:SkeletonProfile)
voidset_profile(value:SkeletonProfile)
- SkeletonProfileget_profile()
SkeletonProfileget_profile()
ASkeletonProfileof the mapping target. Key names in theBoneMapare synchronized with it.

## Method Descriptions

StringNamefind_profile_bone_name(skeleton_bone_name:StringName)const🔗
Returns a profile bone name havingskeleton_bone_name. If not found, an emptyStringNamewill be returned.
In the retargeting process, the returned bone name is the bone name of the target skeleton.
StringNameget_skeleton_bone_name(profile_bone_name:StringName)const🔗
Returns a skeleton bone name is mapped toprofile_bone_name.
In the retargeting process, the returned bone name is the bone name of the source skeleton.
voidset_skeleton_bone_name(profile_bone_name:StringName, skeleton_bone_name:StringName)🔗
Maps a skeleton bone name toprofile_bone_name.
In the retargeting process, the setting bone name is the bone name of the source skeleton.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
