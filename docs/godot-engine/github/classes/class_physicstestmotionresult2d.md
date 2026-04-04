:github_url: hide



# PhysicsTestMotionResult2D

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Describes the motion and collision result from [PhysicsServer2D.body_test_motion()<class_PhysicsServer2D_method_body_test_motion>].


## Description

Describes the motion and collision result from [PhysicsServer2D.body_test_motion()<class_PhysicsServer2D_method_body_test_motion>].


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`   | :ref:`get_collider<class_PhysicsTestMotionResult2D_method_get_collider>`\ (\ ) |const|                                   |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collider_id<class_PhysicsTestMotionResult2D_method_get_collider_id>`\ (\ ) |const|                             |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`         | :ref:`get_collider_rid<class_PhysicsTestMotionResult2D_method_get_collider_rid>`\ (\ ) |const|                           |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collider_shape<class_PhysicsTestMotionResult2D_method_get_collider_shape>`\ (\ ) |const|                       |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_collider_velocity<class_PhysicsTestMotionResult2D_method_get_collider_velocity>`\ (\ ) |const|                 |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_collision_depth<class_PhysicsTestMotionResult2D_method_get_collision_depth>`\ (\ ) |const|                     |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collision_local_shape<class_PhysicsTestMotionResult2D_method_get_collision_local_shape>`\ (\ ) |const|         |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_collision_normal<class_PhysicsTestMotionResult2D_method_get_collision_normal>`\ (\ ) |const|                   |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_collision_point<class_PhysicsTestMotionResult2D_method_get_collision_point>`\ (\ ) |const|                     |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_collision_safe_fraction<class_PhysicsTestMotionResult2D_method_get_collision_safe_fraction>`\ (\ ) |const|     |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_collision_unsafe_fraction<class_PhysicsTestMotionResult2D_method_get_collision_unsafe_fraction>`\ (\ ) |const| |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_remainder<class_PhysicsTestMotionResult2D_method_get_remainder>`\ (\ ) |const|                                 |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_travel<class_PhysicsTestMotionResult2D_method_get_travel>`\ (\ ) |const|                                       |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Object<class_Object>] **get_collider**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult2D_method_get_collider>]

Returns the colliding body's attached [Object<class_Object>], if a collision occurred.


----



[int<class_int>] **get_collider_id**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult2D_method_get_collider_id>]

Returns the unique instance ID of the colliding body's attached [Object<class_Object>], if a collision occurred. See [Object.get_instance_id()<class_Object_method_get_instance_id>].


----



[RID<class_RID>] **get_collider_rid**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult2D_method_get_collider_rid>]

Returns the colliding body's [RID<class_RID>] used by the [PhysicsServer2D<class_PhysicsServer2D>], if a collision occurred.


----



[int<class_int>] **get_collider_shape**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult2D_method_get_collider_shape>]

Returns the colliding body's shape index, if a collision occurred. See [CollisionObject2D<class_CollisionObject2D>].


----



[Vector2<class_Vector2>] **get_collider_velocity**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult2D_method_get_collider_velocity>]

Returns the colliding body's velocity, if a collision occurred.


----



[float<class_float>] **get_collision_depth**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult2D_method_get_collision_depth>]

Returns the length of overlap along the collision normal, if a collision occurred.


----



[int<class_int>] **get_collision_local_shape**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult2D_method_get_collision_local_shape>]

Returns the moving object's colliding shape, if a collision occurred.


----



[Vector2<class_Vector2>] **get_collision_normal**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult2D_method_get_collision_normal>]

Returns the colliding body's shape's normal at the point of collision, if a collision occurred.


----



[Vector2<class_Vector2>] **get_collision_point**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult2D_method_get_collision_point>]

Returns the point of collision in global coordinates, if a collision occurred.


----



[float<class_float>] **get_collision_safe_fraction**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult2D_method_get_collision_safe_fraction>]

Returns the maximum fraction of the motion that can occur without a collision, between `0` and `1`.


----



[float<class_float>] **get_collision_unsafe_fraction**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult2D_method_get_collision_unsafe_fraction>]

Returns the minimum fraction of the motion needed to collide, if a collision occurred, between `0` and `1`.


----



[Vector2<class_Vector2>] **get_remainder**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult2D_method_get_remainder>]

Returns the moving object's remaining movement vector.


----



[Vector2<class_Vector2>] **get_travel**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult2D_method_get_travel>]

Returns the moving object's travel before collision.

