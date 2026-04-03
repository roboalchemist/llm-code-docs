# Skeleton3D

# Skeleton3D
Inherits:Node3D<Node<Object
A node containing a bone hierarchy, used to create a 3D skeletal animation.

## Description
Skeleton3Dprovides an interface for managing a hierarchy of bones, including pose, rest and animation (seeAnimation). It can also use ragdoll physics.
The overall transform of a bone with respect to the skeleton is determined by bone pose. Bone rest defines the initial transform of the bone pose.
Note that "global pose" below refers to the overall transform of the bone with respect to skeleton, so it is not the actual global/world transform of the bone.

## Tutorials
- Third Person Shooter (TPS) Demo
Third Person Shooter (TPS) Demo

## Properties

| bool | animate_physical_bones | true |
|---|---|---|
| ModifierCallbackModeProcess | modifier_callback_mode_process | 1 |
| float | motion_scale | 1.0 |
| bool | show_rest_only | false |

bool
animate_physical_bones
true
ModifierCallbackModeProcess
modifier_callback_mode_process
float
motion_scale
bool
show_rest_only
false

## Methods

| int | add_bone(name:String) |
|---|---|
| void | advance(delta:float) |
| void | clear_bones() |
| void | clear_bones_global_pose_override() |
| Skin | create_skin_from_rest_transforms() |
| int | find_bone(name:String)const |
| void | force_update_all_bone_transforms() |
| void | force_update_bone_child_transform(bone_idx:int) |
| PackedInt32Array | get_bone_children(bone_idx:int)const |
| int | get_bone_count()const |
| Transform3D | get_bone_global_pose(bone_idx:int)const |
| Transform3D | get_bone_global_pose_no_override(bone_idx:int)const |
| Transform3D | get_bone_global_pose_override(bone_idx:int)const |
| Transform3D | get_bone_global_rest(bone_idx:int)const |
| Variant | get_bone_meta(bone_idx:int, key:StringName)const |
| Array[StringName] | get_bone_meta_list(bone_idx:int)const |
| String | get_bone_name(bone_idx:int)const |
| int | get_bone_parent(bone_idx:int)const |
| Transform3D | get_bone_pose(bone_idx:int)const |
| Vector3 | get_bone_pose_position(bone_idx:int)const |
| Quaternion | get_bone_pose_rotation(bone_idx:int)const |
| Vector3 | get_bone_pose_scale(bone_idx:int)const |
| Transform3D | get_bone_rest(bone_idx:int)const |
| StringName | get_concatenated_bone_names()const |
| PackedInt32Array | get_parentless_bones()const |
| int | get_version()const |
| bool | has_bone_meta(bone_idx:int, key:StringName)const |
| bool | is_bone_enabled(bone_idx:int)const |
| void | localize_rests() |
| void | physical_bones_add_collision_exception(exception:RID) |
| void | physical_bones_remove_collision_exception(exception:RID) |
| void | physical_bones_start_simulation(bones:Array[StringName] = []) |
| void | physical_bones_stop_simulation() |
| SkinReference | register_skin(skin:Skin) |
| void | reset_bone_pose(bone_idx:int) |
| void | reset_bone_poses() |
| void | set_bone_enabled(bone_idx:int, enabled:bool= true) |
| void | set_bone_global_pose(bone_idx:int, pose:Transform3D) |
| void | set_bone_global_pose_override(bone_idx:int, pose:Transform3D, amount:float, persistent:bool= false) |
| void | set_bone_meta(bone_idx:int, key:StringName, value:Variant) |
| void | set_bone_name(bone_idx:int, name:String) |
| void | set_bone_parent(bone_idx:int, parent_idx:int) |
| void | set_bone_pose(bone_idx:int, pose:Transform3D) |
| void | set_bone_pose_position(bone_idx:int, position:Vector3) |
| void | set_bone_pose_rotation(bone_idx:int, rotation:Quaternion) |
| void | set_bone_pose_scale(bone_idx:int, scale:Vector3) |
| void | set_bone_rest(bone_idx:int, rest:Transform3D) |
| void | unparent_bone_and_rest(bone_idx:int) |

add_bone(name:String)
void
advance(delta:float)
void
clear_bones()
void
clear_bones_global_pose_override()
Skin
create_skin_from_rest_transforms()
find_bone(name:String)const
void
force_update_all_bone_transforms()
void
force_update_bone_child_transform(bone_idx:int)
PackedInt32Array
get_bone_children(bone_idx:int)const
get_bone_count()const
Transform3D
get_bone_global_pose(bone_idx:int)const
Transform3D
get_bone_global_pose_no_override(bone_idx:int)const
Transform3D
get_bone_global_pose_override(bone_idx:int)const
Transform3D
get_bone_global_rest(bone_idx:int)const
Variant
get_bone_meta(bone_idx:int, key:StringName)const
Array[StringName]
get_bone_meta_list(bone_idx:int)const
String
get_bone_name(bone_idx:int)const
get_bone_parent(bone_idx:int)const
Transform3D
get_bone_pose(bone_idx:int)const
Vector3
get_bone_pose_position(bone_idx:int)const
Quaternion
get_bone_pose_rotation(bone_idx:int)const
Vector3
get_bone_pose_scale(bone_idx:int)const
Transform3D
get_bone_rest(bone_idx:int)const
StringName
get_concatenated_bone_names()const
PackedInt32Array
get_parentless_bones()const
get_version()const
bool
has_bone_meta(bone_idx:int, key:StringName)const
bool
is_bone_enabled(bone_idx:int)const
void
localize_rests()
void
physical_bones_add_collision_exception(exception:RID)
void
physical_bones_remove_collision_exception(exception:RID)
void
physical_bones_start_simulation(bones:Array[StringName] = [])
void
physical_bones_stop_simulation()
SkinReference
register_skin(skin:Skin)
void
reset_bone_pose(bone_idx:int)
void
reset_bone_poses()
void
set_bone_enabled(bone_idx:int, enabled:bool= true)
void
set_bone_global_pose(bone_idx:int, pose:Transform3D)
void
set_bone_global_pose_override(bone_idx:int, pose:Transform3D, amount:float, persistent:bool= false)
void
set_bone_meta(bone_idx:int, key:StringName, value:Variant)
void
set_bone_name(bone_idx:int, name:String)
void
set_bone_parent(bone_idx:int, parent_idx:int)
void
set_bone_pose(bone_idx:int, pose:Transform3D)
void
set_bone_pose_position(bone_idx:int, position:Vector3)
void
set_bone_pose_rotation(bone_idx:int, rotation:Quaternion)
void
set_bone_pose_scale(bone_idx:int, scale:Vector3)
void
set_bone_rest(bone_idx:int, rest:Transform3D)
void
unparent_bone_and_rest(bone_idx:int)

## Signals
bone_enabled_changed(bone_idx:int)🔗
Emitted when the bone atbone_idxis toggled withset_bone_enabled(). Useis_bone_enabled()to check the new value.
bone_list_changed()🔗
Emitted when the list of bones changes, such as when callingadd_bone(),set_bone_parent(),unparent_bone_and_rest(), orclear_bones().
pose_updated()🔗
Emitted when the pose is updated.
Note:During the update process, this signal is not fired, so modification bySkeletonModifier3Dis not detected.
rest_updated()🔗
Emitted when the rest is updated.
show_rest_only_changed()🔗
Emitted when the value ofshow_rest_onlychanges.
skeleton_updated()🔗
Emitted when the final pose has been calculated will be applied to the skin in the update process.
This means that allSkeletonModifier3Dprocessing is complete. In order to detect the completion of the processing of eachSkeletonModifier3D, useSkeletonModifier3D.modification_processed.

## Enumerations
enumModifierCallbackModeProcess:🔗
ModifierCallbackModeProcessMODIFIER_CALLBACK_MODE_PROCESS_PHYSICS=0
Set a flag to process modification during physics frames (seeNode.NOTIFICATION_INTERNAL_PHYSICS_PROCESS).
ModifierCallbackModeProcessMODIFIER_CALLBACK_MODE_PROCESS_IDLE=1
Set a flag to process modification during process frames (seeNode.NOTIFICATION_INTERNAL_PROCESS).
ModifierCallbackModeProcessMODIFIER_CALLBACK_MODE_PROCESS_MANUAL=2
Do not process modification. Useadvance()to process the modification manually.

## Constants
NOTIFICATION_UPDATE_SKELETON=50🔗
Notification received when this skeleton's pose needs to be updated. In that case, this is called only once per frame in a deferred process.

## Property Descriptions
boolanimate_physical_bones=true🔗
- voidset_animate_physical_bones(value:bool)
voidset_animate_physical_bones(value:bool)
- boolget_animate_physical_bones()
boolget_animate_physical_bones()
Deprecated:This property may be changed or removed in future versions.
If you follow the recommended workflow and explicitly havePhysicalBoneSimulator3Das a child ofSkeleton3D, you can control whether it is affected by raycasting without runningphysical_bones_start_simulation(), by itsSkeletonModifier3D.active.
However, for old (deprecated) configurations,Skeleton3Dhas an internal virtualPhysicalBoneSimulator3Dfor compatibility. This property controls the internal virtualPhysicalBoneSimulator3D'sSkeletonModifier3D.active.
ModifierCallbackModeProcessmodifier_callback_mode_process=1🔗
- voidset_modifier_callback_mode_process(value:ModifierCallbackModeProcess)
voidset_modifier_callback_mode_process(value:ModifierCallbackModeProcess)
- ModifierCallbackModeProcessget_modifier_callback_mode_process()
ModifierCallbackModeProcessget_modifier_callback_mode_process()
Sets the processing timing for the Modifier.
floatmotion_scale=1.0🔗
- voidset_motion_scale(value:float)
voidset_motion_scale(value:float)
- floatget_motion_scale()
floatget_motion_scale()
Multiplies the 3D position track animation.
Note:Unless this value is1.0, the key value in animation will not match the actual position value.
boolshow_rest_only=false🔗
- voidset_show_rest_only(value:bool)
voidset_show_rest_only(value:bool)
- boolis_show_rest_only()
boolis_show_rest_only()
Iftrue, forces the bones in their default rest pose, regardless of their values. In the editor, this also prevents the bones from being edited.

## Method Descriptions
intadd_bone(name:String)🔗
Adds a new bone with the given name. Returns the new bone's index, or-1if this method fails.
Note:Bone names should be unique, non empty, and cannot include the:and/characters.
voidadvance(delta:float)🔗
Manually advance the childSkeletonModifier3Ds by the specified time (in seconds).
Note:Thedeltais temporarily accumulated in theSkeleton3D, and the deferred process uses the accumulated value to process the modification.
voidclear_bones()🔗
Clear all the bones in this skeleton.
voidclear_bones_global_pose_override()🔗
Deprecated:This method may be changed or removed in future versions.
Removes the global pose override on all bones in the skeleton.
Skincreate_skin_from_rest_transforms()🔗
There is currently no description for this method. Please help us bycontributing one!
intfind_bone(name:String)const🔗
Returns the bone index that matchesnameas its name. Returns-1if no bone with this name exists.
voidforce_update_all_bone_transforms()🔗
Deprecated:This method should only be called internally.
Force updates the bone transforms/poses for all bones in the skeleton.
voidforce_update_bone_child_transform(bone_idx:int)🔗
Force updates the bone transform for the bone atbone_idxand all of its children.
PackedInt32Arrayget_bone_children(bone_idx:int)const🔗
Returns an array containing the bone indexes of all the child node of the passed in bone,bone_idx.
intget_bone_count()const🔗
Returns the number of bones in the skeleton.
Transform3Dget_bone_global_pose(bone_idx:int)const🔗
Returns the overall transform of the specified bone, with respect to the skeleton. Being relative to the skeleton frame, this is not the actual "global" transform of the bone.
Note:This is the global pose you set to the skeleton in the process, the final global pose can get overridden by modifiers in the deferred process, if you want to access the final global pose, useSkeletonModifier3D.modification_processed.
Transform3Dget_bone_global_pose_no_override(bone_idx:int)const🔗
Deprecated:This method may be changed or removed in future versions.
Returns the overall transform of the specified bone, with respect to the skeleton, but without any global pose overrides. Being relative to the skeleton frame, this is not the actual "global" transform of the bone.
Transform3Dget_bone_global_pose_override(bone_idx:int)const🔗
Deprecated:This method may be changed or removed in future versions.
Returns the global pose override transform forbone_idx.
Transform3Dget_bone_global_rest(bone_idx:int)const🔗
Returns the global rest transform forbone_idx.
Variantget_bone_meta(bone_idx:int, key:StringName)const🔗
Returns the metadata with the givenkeyfor the bone at indexbone_idx.
Array[StringName]get_bone_meta_list(bone_idx:int)const🔗
Returns the list of all metadata keys for the bone at indexbone_idx.
Stringget_bone_name(bone_idx:int)const🔗
Returns the name of the bone at indexbone_idx.
intget_bone_parent(bone_idx:int)const🔗
Returns the bone index which is the parent of the bone atbone_idx. If -1, then bone has no parent.
Note:The parent bone returned will always be less thanbone_idx.
Transform3Dget_bone_pose(bone_idx:int)const🔗
Returns the pose transform of the specified bone.
Note:This is the pose you set to the skeleton in the process, the final pose can get overridden by modifiers in the deferred process, if you want to access the final pose, useSkeletonModifier3D.modification_processed.
Vector3get_bone_pose_position(bone_idx:int)const🔗
Returns the pose position of the bone atbone_idx. The returnedVector3is in the local coordinate space of theSkeleton3Dnode.
Quaternionget_bone_pose_rotation(bone_idx:int)const🔗
Returns the pose rotation of the bone atbone_idx. The returnedQuaternionis local to the bone with respect to the rotation of any parent bones.
Vector3get_bone_pose_scale(bone_idx:int)const🔗
Returns the pose scale of the bone atbone_idx.
Transform3Dget_bone_rest(bone_idx:int)const🔗
Returns the rest transform for a bonebone_idx.
StringNameget_concatenated_bone_names()const🔗
Returns all bone names concatenated with commas (,) as a singleStringName.
It is useful to set it as a hint for the enum property.
PackedInt32Arrayget_parentless_bones()const🔗
Returns an array with all of the bones that are parentless. Another way to look at this is that it returns the indexes of all the bones that are not dependent or modified by other bones in the Skeleton.
intget_version()const🔗
Returns the number of times the bone hierarchy has changed within this skeleton, including renames.
The Skeleton version is not serialized: only use within a single instance of Skeleton3D.
Use for invalidating caches in IK solvers and other nodes which process bones.
boolhas_bone_meta(bone_idx:int, key:StringName)const🔗
Returnstrueif the bone at indexbone_idxhas metadata with the givenkey.
boolis_bone_enabled(bone_idx:int)const🔗
Returns whether the bone pose for the bone atbone_idxis enabled.
voidlocalize_rests()🔗
Returns all bones in the skeleton to their rest poses.
voidphysical_bones_add_collision_exception(exception:RID)🔗
Deprecated:This method may be changed or removed in future versions.
Adds a collision exception to the physical bone.
Works just like theRigidBody3Dnode.
voidphysical_bones_remove_collision_exception(exception:RID)🔗
Deprecated:This method may be changed or removed in future versions.
Removes a collision exception to the physical bone.
Works just like theRigidBody3Dnode.
voidphysical_bones_start_simulation(bones:Array[StringName] = [])🔗
Deprecated:This method may be changed or removed in future versions.
Tells thePhysicalBone3Dnodes in the Skeleton to start simulating and reacting to the physics world.
Optionally, a list of bone names can be passed-in, allowing only the passed-in bones to be simulated.
voidphysical_bones_stop_simulation()🔗
Deprecated:This method may be changed or removed in future versions.
Tells thePhysicalBone3Dnodes in the Skeleton to stop simulating.
SkinReferenceregister_skin(skin:Skin)🔗
Binds the given Skin to the Skeleton.
voidreset_bone_pose(bone_idx:int)🔗
Sets the bone pose to rest forbone_idx.
voidreset_bone_poses()🔗
Sets all bone poses to rests.
voidset_bone_enabled(bone_idx:int, enabled:bool= true)🔗
Disables the pose for the bone atbone_idxiffalse, enables the bone pose iftrue.
voidset_bone_global_pose(bone_idx:int, pose:Transform3D)🔗
Sets the global pose transform,pose, for the bone atbone_idx.
Note:If other bone poses have been changed, this method executes a dirty poses recalculation and will cause performance to deteriorate. If you know that multiple global poses will be applied, consider usingset_bone_pose()with precalculation.
voidset_bone_global_pose_override(bone_idx:int, pose:Transform3D, amount:float, persistent:bool= false)🔗
Deprecated:This method may be changed or removed in future versions.
Sets the global pose transform,pose, for the bone atbone_idx.
amountis the interpolation strength that will be used when applying the pose, andpersistentdetermines if the applied pose will remain.
Note:The pose transform needs to be a global pose! To convert a world transform from aNode3Dto a global bone pose, multiply theTransform3D.affine_inverse()of the node'sNode3D.global_transformby the desired world transform.
voidset_bone_meta(bone_idx:int, key:StringName, value:Variant)🔗
Sets the metadata with the givenkeytovaluefor the bone at indexbone_idx.
voidset_bone_name(bone_idx:int, name:String)🔗
Sets the bone name,name, for the bone atbone_idx.
voidset_bone_parent(bone_idx:int, parent_idx:int)🔗
Sets the bone indexparent_idxas the parent of the bone atbone_idx. If -1, then bone has no parent.
Note:parent_idxmust be less thanbone_idx.
voidset_bone_pose(bone_idx:int, pose:Transform3D)🔗
Sets the pose transform,pose, for the bone atbone_idx.
voidset_bone_pose_position(bone_idx:int, position:Vector3)🔗
Sets the pose position of the bone atbone_idxtoposition.positionis aVector3describing a position local to theSkeleton3Dnode.
voidset_bone_pose_rotation(bone_idx:int, rotation:Quaternion)🔗
Sets the pose rotation of the bone atbone_idxtorotation.rotationis aQuaterniondescribing a rotation in the bone's local coordinate space with respect to the rotation of any parent bones.
voidset_bone_pose_scale(bone_idx:int, scale:Vector3)🔗
Sets the pose scale of the bone atbone_idxtoscale.
voidset_bone_rest(bone_idx:int, rest:Transform3D)🔗
Sets the rest transform for bonebone_idx.
voidunparent_bone_and_rest(bone_idx:int)🔗
Unparents the bone atbone_idxand sets its rest position to that of its parent prior to being reset.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.