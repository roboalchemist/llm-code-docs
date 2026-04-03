# PhysicsTestMotionParameters2D in English

# PhysicsTestMotionParameters2D

Inherits:RefCounted<Object
Provides parameters forPhysicsServer2D.body_test_motion().

## Description

By changing various properties of this object, such as the motion, you can configure the parameters forPhysicsServer2D.body_test_motion().

## Properties

| bool | collide_separation_ray | false |
|---|---|---|
| Array[RID] | exclude_bodies | [] |
| Array[int] | exclude_objects | [] |
| Transform2D | from | Transform2D(1,0,0,1,0,0) |
| float | margin | 0.08 |
| Vector2 | motion | Vector2(0,0) |
| bool | recovery_as_collision | false |

bool
collide_separation_ray
false
Array[RID]
exclude_bodies
Array[int]
exclude_objects
Transform2D
from
Transform2D(1,0,0,1,0,0)
float
margin
0.08
Vector2
motion
Vector2(0,0)
bool
recovery_as_collision
false

## Property Descriptions

boolcollide_separation_ray=false🔗

- voidset_collide_separation_ray_enabled(value:bool)
voidset_collide_separation_ray_enabled(value:bool)
- boolis_collide_separation_ray_enabled()
boolis_collide_separation_ray_enabled()
If set totrue, shapes of typePhysicsServer2D.SHAPE_SEPARATION_RAYare used to detect collisions and can stop the motion. Can be useful when snapping to the ground.
If set tofalse, shapes of typePhysicsServer2D.SHAPE_SEPARATION_RAYare only used for separation when overlapping with other bodies. That's the main use for separation ray shapes.
Array[RID]exclude_bodies=[]🔗
- voidset_exclude_bodies(value:Array[RID])
voidset_exclude_bodies(value:Array[RID])
- Array[RID]get_exclude_bodies()
Array[RID]get_exclude_bodies()
Optional array of bodyRIDto exclude from collision. UseCollisionObject2D.get_rid()to get theRIDassociated with aCollisionObject2D-derived node.
Array[int]exclude_objects=[]🔗
- voidset_exclude_objects(value:Array[int])
voidset_exclude_objects(value:Array[int])
- Array[int]get_exclude_objects()
Array[int]get_exclude_objects()
Optional array of object unique instance ID to exclude from collision. SeeObject.get_instance_id().
Transform2Dfrom=Transform2D(1,0,0,1,0,0)🔗
- voidset_from(value:Transform2D)
voidset_from(value:Transform2D)
- Transform2Dget_from()
Transform2Dget_from()
Transform in global space where the motion should start. Usually set toNode2D.global_transformfor the current body's transform.
floatmargin=0.08🔗
- voidset_margin(value:float)
voidset_margin(value:float)
- floatget_margin()
floatget_margin()
Increases the size of the shapes involved in the collision detection.
Vector2motion=Vector2(0,0)🔗
- voidset_motion(value:Vector2)
voidset_motion(value:Vector2)
- Vector2get_motion()
Vector2get_motion()
Motion vector to define the length and direction of the motion to test.
boolrecovery_as_collision=false🔗
- voidset_recovery_as_collision_enabled(value:bool)
voidset_recovery_as_collision_enabled(value:bool)
- boolis_recovery_as_collision_enabled()
boolis_recovery_as_collision_enabled()
If set totrue, any depenetration from the recovery phase is reported as a collision; this is used e.g. byCharacterBody2Dfor improving floor detection during floor snapping.
If set tofalse, only collisions resulting from the motion are reported, which is generally the desired behavior.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
