# PhysicsPointQueryParameters2D

# PhysicsPointQueryParameters2D
Inherits:RefCounted<Object
Provides parameters forPhysicsDirectSpaceState2D.intersect_point().

## Description
By changing various properties of this object, such as the point position, you can configure the parameters forPhysicsDirectSpaceState2D.intersect_point().

## Properties

| int | canvas_instance_id | 0 |
|---|---|---|
| bool | collide_with_areas | false |
| bool | collide_with_bodies | true |
| int | collision_mask | 4294967295 |
| Array[RID] | exclude | [] |
| Vector2 | position | Vector2(0,0) |

canvas_instance_id
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
position
Vector2(0,0)

## Property Descriptions
intcanvas_instance_id=0🔗
- voidset_canvas_instance_id(value:int)
voidset_canvas_instance_id(value:int)
- intget_canvas_instance_id()
intget_canvas_instance_id()
If different from0, restricts the query to a specific canvas layer specified by its instance ID. SeeObject.get_instance_id().
If0, restricts the query to the Viewport's default canvas layer.
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
Vector2position=Vector2(0,0)🔗
- voidset_position(value:Vector2)
voidset_position(value:Vector2)
- Vector2get_position()
Vector2get_position()
The position being queried for, in global coordinates.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.