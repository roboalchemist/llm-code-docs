# KinematicCollision3D in English

# KinematicCollision3D

Inherits:RefCounted<Object
Holds collision data from the movement of aPhysicsBody3D.

## Description

Holds collision data from the movement of aPhysicsBody3D, usually fromPhysicsBody3D.move_and_collide(). When aPhysicsBody3Dis moved, it stops if it detects a collision with another body. If a collision is detected, aKinematicCollision3Dobject is returned.
The collision data includes the colliding object, the remaining motion, and the collision position. This data can be used to determine a custom response to the collision.

## Methods

| float | get_angle(collision_index:int= 0, up_direction:Vector3= Vector3(0, 1, 0))const |
|---|---|
| Object | get_collider(collision_index:int= 0)const |
| int | get_collider_id(collision_index:int= 0)const |
| RID | get_collider_rid(collision_index:int= 0)const |
| Object | get_collider_shape(collision_index:int= 0)const |
| int | get_collider_shape_index(collision_index:int= 0)const |
| Vector3 | get_collider_velocity(collision_index:int= 0)const |
| int | get_collision_count()const |
| float | get_depth()const |
| Object | get_local_shape(collision_index:int= 0)const |
| Vector3 | get_normal(collision_index:int= 0)const |
| Vector3 | get_position(collision_index:int= 0)const |
| Vector3 | get_remainder()const |
| Vector3 | get_travel()const |

float
get_angle(collision_index:int= 0, up_direction:Vector3= Vector3(0, 1, 0))const
Object
get_collider(collision_index:int= 0)const
get_collider_id(collision_index:int= 0)const
get_collider_rid(collision_index:int= 0)const
Object
get_collider_shape(collision_index:int= 0)const
get_collider_shape_index(collision_index:int= 0)const
Vector3
get_collider_velocity(collision_index:int= 0)const
get_collision_count()const
float
get_depth()const
Object
get_local_shape(collision_index:int= 0)const
Vector3
get_normal(collision_index:int= 0)const
Vector3
get_position(collision_index:int= 0)const
Vector3
get_remainder()const
Vector3
get_travel()const

## Method Descriptions

floatget_angle(collision_index:int= 0, up_direction:Vector3= Vector3(0, 1, 0))const🔗
Returns the collision angle according toup_direction, which isVector3.UPby default. This value is always positive.
Objectget_collider(collision_index:int= 0)const🔗
Returns the colliding body's attachedObjectgiven a collision index (the deepest collision by default).
intget_collider_id(collision_index:int= 0)const🔗
Returns the unique instance ID of the colliding body's attachedObjectgiven a collision index (the deepest collision by default). SeeObject.get_instance_id().
RIDget_collider_rid(collision_index:int= 0)const🔗
Returns the colliding body'sRIDused by thePhysicsServer3Dgiven a collision index (the deepest collision by default).
Objectget_collider_shape(collision_index:int= 0)const🔗
Returns the colliding body's shape given a collision index (the deepest collision by default).
intget_collider_shape_index(collision_index:int= 0)const🔗
Returns the colliding body's shape index given a collision index (the deepest collision by default). SeeCollisionObject3D.
Vector3get_collider_velocity(collision_index:int= 0)const🔗
Returns the colliding body's velocity given a collision index (the deepest collision by default).
intget_collision_count()const🔗
Returns the number of detected collisions.
floatget_depth()const🔗
Returns the colliding body's length of overlap along the collision normal.
Objectget_local_shape(collision_index:int= 0)const🔗
Returns the moving object's colliding shape given a collision index (the deepest collision by default).
Vector3get_normal(collision_index:int= 0)const🔗
Returns the colliding body's shape's normal at the point of collision given a collision index (the deepest collision by default).
Vector3get_position(collision_index:int= 0)const🔗
Returns the point of collision in global coordinates given a collision index (the deepest collision by default).
Vector3get_remainder()const🔗
Returns the moving object's remaining movement vector.
Vector3get_travel()const🔗
Returns the moving object's travel before collision.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
