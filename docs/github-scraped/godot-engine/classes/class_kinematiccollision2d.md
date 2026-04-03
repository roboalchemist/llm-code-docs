:github_url: hide



# KinematicCollision2D

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Holds collision data from the movement of a [PhysicsBody2D<class_PhysicsBody2D>].


## Description

Holds collision data from the movement of a [PhysicsBody2D<class_PhysicsBody2D>], usually from [PhysicsBody2D.move_and_collide()<class_PhysicsBody2D_method_move_and_collide>]. When a [PhysicsBody2D<class_PhysicsBody2D>] is moved, it stops if it detects a collision with another body. If a collision is detected, a **KinematicCollision2D** object is returned.

The collision data includes the colliding object, the remaining motion, and the collision position. This data can be used to determine a custom response to the collision.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_angle<class_KinematicCollision2D_method_get_angle>`\ (\ up_direction\: :ref:`Vector2<class_Vector2>` = Vector2(0, -1)\ ) |const| |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`   | :ref:`get_collider<class_KinematicCollision2D_method_get_collider>`\ (\ ) |const|                                                          |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collider_id<class_KinematicCollision2D_method_get_collider_id>`\ (\ ) |const|                                                    |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`         | :ref:`get_collider_rid<class_KinematicCollision2D_method_get_collider_rid>`\ (\ ) |const|                                                  |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`   | :ref:`get_collider_shape<class_KinematicCollision2D_method_get_collider_shape>`\ (\ ) |const|                                              |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collider_shape_index<class_KinematicCollision2D_method_get_collider_shape_index>`\ (\ ) |const|                                  |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_collider_velocity<class_KinematicCollision2D_method_get_collider_velocity>`\ (\ ) |const|                                        |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_depth<class_KinematicCollision2D_method_get_depth>`\ (\ ) |const|                                                                |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`   | :ref:`get_local_shape<class_KinematicCollision2D_method_get_local_shape>`\ (\ ) |const|                                                    |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_normal<class_KinematicCollision2D_method_get_normal>`\ (\ ) |const|                                                              |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_position<class_KinematicCollision2D_method_get_position>`\ (\ ) |const|                                                          |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_remainder<class_KinematicCollision2D_method_get_remainder>`\ (\ ) |const|                                                        |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_travel<class_KinematicCollision2D_method_get_travel>`\ (\ ) |const|                                                              |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[float<class_float>] **get_angle**\ (\ up_direction\: [Vector2<class_Vector2>] = Vector2(0, -1)\ ) |const| [🔗<class_KinematicCollision2D_method_get_angle>]

Returns the collision angle according to `up_direction`, which is [Vector2.UP<class_Vector2_constant_UP>] by default. This value is always positive.


----



[Object<class_Object>] **get_collider**\ (\ ) |const| [🔗<class_KinematicCollision2D_method_get_collider>]

Returns the colliding body's attached [Object<class_Object>].


----



[int<class_int>] **get_collider_id**\ (\ ) |const| [🔗<class_KinematicCollision2D_method_get_collider_id>]

Returns the unique instance ID of the colliding body's attached [Object<class_Object>]. See [Object.get_instance_id()<class_Object_method_get_instance_id>].


----



[RID<class_RID>] **get_collider_rid**\ (\ ) |const| [🔗<class_KinematicCollision2D_method_get_collider_rid>]

Returns the colliding body's [RID<class_RID>] used by the [PhysicsServer2D<class_PhysicsServer2D>].


----



[Object<class_Object>] **get_collider_shape**\ (\ ) |const| [🔗<class_KinematicCollision2D_method_get_collider_shape>]

Returns the colliding body's shape.


----



[int<class_int>] **get_collider_shape_index**\ (\ ) |const| [🔗<class_KinematicCollision2D_method_get_collider_shape_index>]

Returns the colliding body's shape index. See [CollisionObject2D<class_CollisionObject2D>].


----



[Vector2<class_Vector2>] **get_collider_velocity**\ (\ ) |const| [🔗<class_KinematicCollision2D_method_get_collider_velocity>]

Returns the colliding body's velocity.


----



[float<class_float>] **get_depth**\ (\ ) |const| [🔗<class_KinematicCollision2D_method_get_depth>]

Returns the colliding body's length of overlap along the collision normal.


----



[Object<class_Object>] **get_local_shape**\ (\ ) |const| [🔗<class_KinematicCollision2D_method_get_local_shape>]

Returns the moving object's colliding shape.


----



[Vector2<class_Vector2>] **get_normal**\ (\ ) |const| [🔗<class_KinematicCollision2D_method_get_normal>]

Returns the colliding body's shape's normal at the point of collision.


----



[Vector2<class_Vector2>] **get_position**\ (\ ) |const| [🔗<class_KinematicCollision2D_method_get_position>]

Returns the point of collision in global coordinates.


----



[Vector2<class_Vector2>] **get_remainder**\ (\ ) |const| [🔗<class_KinematicCollision2D_method_get_remainder>]

Returns the moving object's remaining movement vector.


----



[Vector2<class_Vector2>] **get_travel**\ (\ ) |const| [🔗<class_KinematicCollision2D_method_get_travel>]

Returns the moving object's travel before collision.

