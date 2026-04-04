# PhysicsRayQueryParameters2D

# PhysicsRayQueryParameters2D

Inherits:RefCounted<Object
Provides parameters forPhysicsDirectSpaceState2D.intersect_ray().

## Description

By changing various properties of this object, such as the ray position, you can configure the parameters forPhysicsDirectSpaceState2D.intersect_ray().

## Properties

| bool | collide_with_areas | false |
|---|---|---|
| bool | collide_with_bodies | true |
| int | collision_mask | 4294967295 |
| Array[RID] | exclude | [] |
| Vector2 | from | Vector2(0,0) |
| bool | hit_from_inside | false |
| Vector2 | to | Vector2(0,0) |

bool
collide_with_areas
false
bool
collide_with_bodies
true
collision_mask
4294967295
Array[RID]
exclude
Vector2
from
Vector2(0,0)
bool
hit_from_inside
false
Vector2
Vector2(0,0)

## Methods

| PhysicsRayQueryParameters2D | create(from:Vector2, to:Vector2, collision_mask:int= 4294967295, exclude:Array[RID] = [])static |

PhysicsRayQueryParameters2D
create(from:Vector2, to:Vector2, collision_mask:int= 4294967295, exclude:Array[RID] = [])static

## Property Descriptions

boolcollide_with_areas=false🔗

- voidset_collide_with_areas(value:bool)
voidset_collide_with_areas(value:bool)
- boolis_collide_with_areas_enabled()
boolis_collide_with_areas_enabled()
Iftrue, the query will takeArea2Ds into account.
boolcollide_with_bodies=true🔗
- voidset_collide_with_bodies(value:bool)
voidset_collide_with_bodies(value:bool)
- boolis_collide_with_bodies_enabled()
boolis_collide_with_bodies_enabled()
Iftrue, the query will takePhysicsBody2Ds into account.
intcollision_mask=4294967295🔗
- voidset_collision_mask(value:int)
voidset_collision_mask(value:int)
- intget_collision_mask()
intget_collision_mask()
The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. SeeCollision layers and masksin the documentation for more information.
Array[RID]exclude=[]🔗
- voidset_exclude(value:Array[RID])
voidset_exclude(value:Array[RID])
- Array[RID]get_exclude()
Array[RID]get_exclude()
The list of objectRIDs that will be excluded from collisions. UseCollisionObject2D.get_rid()to get theRIDassociated with aCollisionObject2D-derived node.
Note:The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.
Vector2from=Vector2(0,0)🔗
- voidset_from(value:Vector2)
voidset_from(value:Vector2)
- Vector2get_from()
Vector2get_from()
The starting point of the ray being queried for, in global coordinates.
boolhit_from_inside=false🔗
- voidset_hit_from_inside(value:bool)
voidset_hit_from_inside(value:bool)
- boolis_hit_from_inside_enabled()
boolis_hit_from_inside_enabled()
Iftrue, the query will detect a hit when starting inside shapes. In this case the collision normal will beVector2(0,0). Does not affect concave polygon shapes.
Vector2to=Vector2(0,0)🔗
- voidset_to(value:Vector2)
voidset_to(value:Vector2)
- Vector2get_to()
Vector2get_to()
The ending point of the ray being queried for, in global coordinates.

## Method Descriptions

PhysicsRayQueryParameters2Dcreate(from:Vector2, to:Vector2, collision_mask:int= 4294967295, exclude:Array[RID] = [])static🔗
Returns a new, pre-configuredPhysicsRayQueryParameters2Dobject. Use it to quickly create query parameters using the most common options.

```
var query = PhysicsRayQueryParameters2D.create(global_position, global_position + Vector2(0, 100))
var collision = get_world_2d().direct_space_state.intersect_ray(query)
```

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
