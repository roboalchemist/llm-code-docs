:github_url: hide



# KinematicCollision3D

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Holds collision data from the movement of a [PhysicsBody3D<class_PhysicsBody3D>].


## Description

Holds collision data from the movement of a [PhysicsBody3D<class_PhysicsBody3D>], usually from [PhysicsBody3D.move_and_collide()<class_PhysicsBody3D_method_move_and_collide>]. When a [PhysicsBody3D<class_PhysicsBody3D>] is moved, it stops if it detects a collision with another body. If a collision is detected, a **KinematicCollision3D** object is returned.

The collision data includes the colliding object, the remaining motion, and the collision position. This data can be used to determine a custom response to the collision.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_angle<class_KinematicCollision3D_method_get_angle>`\ (\ collision_index\: :ref:`int<class_int>` = 0, up_direction\: :ref:`Vector3<class_Vector3>` = Vector3(0, 1, 0)\ ) |const| |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`   | :ref:`get_collider<class_KinematicCollision3D_method_get_collider>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|                                                            |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collider_id<class_KinematicCollision3D_method_get_collider_id>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|                                                      |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`         | :ref:`get_collider_rid<class_KinematicCollision3D_method_get_collider_rid>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|                                                    |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`   | :ref:`get_collider_shape<class_KinematicCollision3D_method_get_collider_shape>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|                                                |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collider_shape_index<class_KinematicCollision3D_method_get_collider_shape_index>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|                                    |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_collider_velocity<class_KinematicCollision3D_method_get_collider_velocity>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|                                          |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collision_count<class_KinematicCollision3D_method_get_collision_count>`\ (\ ) |const|                                                                                           |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_depth<class_KinematicCollision3D_method_get_depth>`\ (\ ) |const|                                                                                                               |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`   | :ref:`get_local_shape<class_KinematicCollision3D_method_get_local_shape>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|                                                      |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_normal<class_KinematicCollision3D_method_get_normal>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|                                                                |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_position<class_KinematicCollision3D_method_get_position>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|                                                            |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_remainder<class_KinematicCollision3D_method_get_remainder>`\ (\ ) |const|                                                                                                       |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_travel<class_KinematicCollision3D_method_get_travel>`\ (\ ) |const|                                                                                                             |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[float<class_float>] **get_angle**\ (\ collision_index\: [int<class_int>] = 0, up_direction\: [Vector3<class_Vector3>] = Vector3(0, 1, 0)\ ) |const| [🔗<class_KinematicCollision3D_method_get_angle>]

Returns the collision angle according to `up_direction`, which is [Vector3.UP<class_Vector3_constant_UP>] by default. This value is always positive.


----



[Object<class_Object>] **get_collider**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_KinematicCollision3D_method_get_collider>]

Returns the colliding body's attached [Object<class_Object>] given a collision index (the deepest collision by default).


----



[int<class_int>] **get_collider_id**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_KinematicCollision3D_method_get_collider_id>]

Returns the unique instance ID of the colliding body's attached [Object<class_Object>] given a collision index (the deepest collision by default). See [Object.get_instance_id()<class_Object_method_get_instance_id>].


----



[RID<class_RID>] **get_collider_rid**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_KinematicCollision3D_method_get_collider_rid>]

Returns the colliding body's [RID<class_RID>] used by the [PhysicsServer3D<class_PhysicsServer3D>] given a collision index (the deepest collision by default).


----



[Object<class_Object>] **get_collider_shape**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_KinematicCollision3D_method_get_collider_shape>]

Returns the colliding body's shape given a collision index (the deepest collision by default).


----



[int<class_int>] **get_collider_shape_index**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_KinematicCollision3D_method_get_collider_shape_index>]

Returns the colliding body's shape index given a collision index (the deepest collision by default). See [CollisionObject3D<class_CollisionObject3D>].


----



[Vector3<class_Vector3>] **get_collider_velocity**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_KinematicCollision3D_method_get_collider_velocity>]

Returns the colliding body's velocity given a collision index (the deepest collision by default).


----



[int<class_int>] **get_collision_count**\ (\ ) |const| [🔗<class_KinematicCollision3D_method_get_collision_count>]

Returns the number of detected collisions.


----



[float<class_float>] **get_depth**\ (\ ) |const| [🔗<class_KinematicCollision3D_method_get_depth>]

Returns the colliding body's length of overlap along the collision normal.


----



[Object<class_Object>] **get_local_shape**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_KinematicCollision3D_method_get_local_shape>]

Returns the moving object's colliding shape given a collision index (the deepest collision by default).


----



[Vector3<class_Vector3>] **get_normal**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_KinematicCollision3D_method_get_normal>]

Returns the colliding body's shape's normal at the point of collision given a collision index (the deepest collision by default).


----



[Vector3<class_Vector3>] **get_position**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_KinematicCollision3D_method_get_position>]

Returns the point of collision in global coordinates given a collision index (the deepest collision by default).


----



[Vector3<class_Vector3>] **get_remainder**\ (\ ) |const| [🔗<class_KinematicCollision3D_method_get_remainder>]

Returns the moving object's remaining movement vector.


----



[Vector3<class_Vector3>] **get_travel**\ (\ ) |const| [🔗<class_KinematicCollision3D_method_get_travel>]

Returns the moving object's travel before collision.

