:github_url: hide



# PhysicsTestMotionResult3D

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Describes the motion and collision result from [PhysicsServer3D.body_test_motion()<class_PhysicsServer3D_method_body_test_motion>].


## Description

Describes the motion and collision result from [PhysicsServer3D.body_test_motion()<class_PhysicsServer3D_method_body_test_motion>].


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`   | :ref:`get_collider<class_PhysicsTestMotionResult3D_method_get_collider>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|                           |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collider_id<class_PhysicsTestMotionResult3D_method_get_collider_id>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|                     |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`         | :ref:`get_collider_rid<class_PhysicsTestMotionResult3D_method_get_collider_rid>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|                   |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collider_shape<class_PhysicsTestMotionResult3D_method_get_collider_shape>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|               |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_collider_velocity<class_PhysicsTestMotionResult3D_method_get_collider_velocity>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|         |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collision_count<class_PhysicsTestMotionResult3D_method_get_collision_count>`\ (\ ) |const|                                                          |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_collision_depth<class_PhysicsTestMotionResult3D_method_get_collision_depth>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|             |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collision_local_shape<class_PhysicsTestMotionResult3D_method_get_collision_local_shape>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const| |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_collision_normal<class_PhysicsTestMotionResult3D_method_get_collision_normal>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|           |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_collision_point<class_PhysicsTestMotionResult3D_method_get_collision_point>`\ (\ collision_index\: :ref:`int<class_int>` = 0\ ) |const|             |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_collision_safe_fraction<class_PhysicsTestMotionResult3D_method_get_collision_safe_fraction>`\ (\ ) |const|                                          |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_collision_unsafe_fraction<class_PhysicsTestMotionResult3D_method_get_collision_unsafe_fraction>`\ (\ ) |const|                                      |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_remainder<class_PhysicsTestMotionResult3D_method_get_remainder>`\ (\ ) |const|                                                                      |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_travel<class_PhysicsTestMotionResult3D_method_get_travel>`\ (\ ) |const|                                                                            |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Object<class_Object>] **get_collider**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_collider>]

Returns the colliding body's attached [Object<class_Object>] given a collision index (the deepest collision by default), if a collision occurred.


----



[int<class_int>] **get_collider_id**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_collider_id>]

Returns the unique instance ID of the colliding body's attached [Object<class_Object>] given a collision index (the deepest collision by default), if a collision occurred. See [Object.get_instance_id()<class_Object_method_get_instance_id>].


----



[RID<class_RID>] **get_collider_rid**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_collider_rid>]

Returns the colliding body's [RID<class_RID>] used by the [PhysicsServer3D<class_PhysicsServer3D>] given a collision index (the deepest collision by default), if a collision occurred.


----



[int<class_int>] **get_collider_shape**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_collider_shape>]

Returns the colliding body's shape index given a collision index (the deepest collision by default), if a collision occurred. See [CollisionObject3D<class_CollisionObject3D>].


----



[Vector3<class_Vector3>] **get_collider_velocity**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_collider_velocity>]

Returns the colliding body's velocity given a collision index (the deepest collision by default), if a collision occurred.


----



[int<class_int>] **get_collision_count**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_collision_count>]

Returns the number of detected collisions.


----



[float<class_float>] **get_collision_depth**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_collision_depth>]

Returns the length of overlap along the collision normal given a collision index (the deepest collision by default), if a collision occurred.


----



[int<class_int>] **get_collision_local_shape**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_collision_local_shape>]

Returns the moving object's colliding shape given a collision index (the deepest collision by default), if a collision occurred.


----



[Vector3<class_Vector3>] **get_collision_normal**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_collision_normal>]

Returns the colliding body's shape's normal at the point of collision given a collision index (the deepest collision by default), if a collision occurred.


----



[Vector3<class_Vector3>] **get_collision_point**\ (\ collision_index\: [int<class_int>] = 0\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_collision_point>]

Returns the point of collision in global coordinates given a collision index (the deepest collision by default), if a collision occurred.


----



[float<class_float>] **get_collision_safe_fraction**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_collision_safe_fraction>]

Returns the maximum fraction of the motion that can occur without a collision, between `0` and `1`.


----



[float<class_float>] **get_collision_unsafe_fraction**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_collision_unsafe_fraction>]

Returns the minimum fraction of the motion needed to collide, if a collision occurred, between `0` and `1`.


----



[Vector3<class_Vector3>] **get_remainder**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_remainder>]

Returns the moving object's remaining movement vector.


----



[Vector3<class_Vector3>] **get_travel**\ (\ ) |const| [🔗<class_PhysicsTestMotionResult3D_method_get_travel>]

Returns the moving object's travel before collision.

