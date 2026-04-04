# SkeletonModification2DPhysicalBones in English

# SkeletonModification2DPhysicalBones

Experimental:Physical bones may be changed in the future to perform the position update ofBone2Don their own, without needing this resource.
Inherits:SkeletonModification2D<Resource<RefCounted<Object
A modification that applies the transforms ofPhysicalBone2Dnodes toBone2Dnodes.

## Description

This modification takes the transforms ofPhysicalBone2Dnodes and applies them toBone2Dnodes. This allows theBone2Dnodes to react to physics thanks to the linkedPhysicalBone2Dnodes.

## Properties

| int | physical_bone_chain_length | 0 |

physical_bone_chain_length

## Methods

| void | fetch_physical_bones() |
|---|---|
| NodePath | get_physical_bone_node(joint_idx:int)const |
| void | set_physical_bone_node(joint_idx:int, physicalbone2d_node:NodePath) |
| void | start_simulation(bones:Array[StringName] = []) |
| void | stop_simulation(bones:Array[StringName] = []) |

void
fetch_physical_bones()
NodePath
get_physical_bone_node(joint_idx:int)const
void
set_physical_bone_node(joint_idx:int, physicalbone2d_node:NodePath)
void
start_simulation(bones:Array[StringName] = [])
void
stop_simulation(bones:Array[StringName] = [])

## Property Descriptions

intphysical_bone_chain_length=0🔗

- voidset_physical_bone_chain_length(value:int)
voidset_physical_bone_chain_length(value:int)
- intget_physical_bone_chain_length()
intget_physical_bone_chain_length()
The number ofPhysicalBone2Dnodes linked in this modification.

## Method Descriptions

voidfetch_physical_bones()🔗
Empties the list ofPhysicalBone2Dnodes and populates it with allPhysicalBone2Dnodes that are children of theSkeleton2D.
NodePathget_physical_bone_node(joint_idx:int)const🔗
Returns thePhysicalBone2Dnode atjoint_idx.
voidset_physical_bone_node(joint_idx:int, physicalbone2d_node:NodePath)🔗
Sets thePhysicalBone2Dnode atjoint_idx.
Note:This is just the index used for this modification, not the bone index used in theSkeleton2D.
voidstart_simulation(bones:Array[StringName] = [])🔗
Tell thePhysicalBone2Dnodes to start simulating and interacting with the physics world.
Optionally, an array of bone names can be passed to this function, and that will cause onlyPhysicalBone2Dnodes with those names to start simulating.
voidstop_simulation(bones:Array[StringName] = [])🔗
Tell thePhysicalBone2Dnodes to stop simulating and interacting with the physics world.
Optionally, an array of bone names can be passed to this function, and that will cause onlyPhysicalBone2Dnodes with those names to stop simulating.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
