:github_url: hide



# PhysicsTestMotionParameters3D

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Provides parameters for [PhysicsServer3D.body_test_motion()<class_PhysicsServer3D_method_body_test_motion>].


## Description

By changing various properties of this object, such as the motion, you can configure the parameters for [PhysicsServer3D.body_test_motion()<class_PhysicsServer3D_method_body_test_motion>].


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`bool<class_bool>`                            | :ref:`collide_separation_ray<class_PhysicsTestMotionParameters3D_property_collide_separation_ray>` | ``false``                                           |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`RID<class_RID>`\] | :ref:`exclude_bodies<class_PhysicsTestMotionParameters3D_property_exclude_bodies>`                 | ``[]``                                              |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`int<class_int>`\] | :ref:`exclude_objects<class_PhysicsTestMotionParameters3D_property_exclude_objects>`               | ``[]``                                              |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`              | :ref:`from<class_PhysicsTestMotionParameters3D_property_from>`                                     | ``Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`` |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`float<class_float>`                          | :ref:`margin<class_PhysicsTestMotionParameters3D_property_margin>`                                 | ``0.001``                                           |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`int<class_int>`                              | :ref:`max_collisions<class_PhysicsTestMotionParameters3D_property_max_collisions>`                 | ``1``                                               |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                      | :ref:`motion<class_PhysicsTestMotionParameters3D_property_motion>`                                 | ``Vector3(0, 0, 0)``                                |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`bool<class_bool>`                            | :ref:`recovery_as_collision<class_PhysicsTestMotionParameters3D_property_recovery_as_collision>`   | ``false``                                           |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **collide_separation_ray** = `false` [🔗<class_PhysicsTestMotionParameters3D_property_collide_separation_ray>]


- |void| **set_collide_separation_ray_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_collide_separation_ray_enabled**\ (\ )

If set to `true`, shapes of type [PhysicsServer3D.SHAPE_SEPARATION_RAY<class_PhysicsServer3D_constant_SHAPE_SEPARATION_RAY>] are used to detect collisions and can stop the motion. Can be useful when snapping to the ground.

If set to `false`, shapes of type [PhysicsServer3D.SHAPE_SEPARATION_RAY<class_PhysicsServer3D_constant_SHAPE_SEPARATION_RAY>] are only used for separation when overlapping with other bodies. That's the main use for separation ray shapes.


----



[Array<class_Array>]\[[RID<class_RID>]\] **exclude_bodies** = `[]` [🔗<class_PhysicsTestMotionParameters3D_property_exclude_bodies>]


- |void| **set_exclude_bodies**\ (\ value\: [Array<class_Array>]\[[RID<class_RID>]\]\ )
- [Array<class_Array>]\[[RID<class_RID>]\] **get_exclude_bodies**\ (\ )

Optional array of body [RID<class_RID>] to exclude from collision. Use [CollisionObject3D.get_rid()<class_CollisionObject3D_method_get_rid>] to get the [RID<class_RID>] associated with a [CollisionObject3D<class_CollisionObject3D>]-derived node.


----



[Array<class_Array>]\[[int<class_int>]\] **exclude_objects** = `[]` [🔗<class_PhysicsTestMotionParameters3D_property_exclude_objects>]


- |void| **set_exclude_objects**\ (\ value\: [Array<class_Array>]\[[int<class_int>]\]\ )
- [Array<class_Array>]\[[int<class_int>]\] **get_exclude_objects**\ (\ )

Optional array of object unique instance ID to exclude from collision. See [Object.get_instance_id()<class_Object_method_get_instance_id>].


----



[Transform3D<class_Transform3D>] **from** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗<class_PhysicsTestMotionParameters3D_property_from>]


- |void| **set_from**\ (\ value\: [Transform3D<class_Transform3D>]\ )
- [Transform3D<class_Transform3D>] **get_from**\ (\ )

Transform in global space where the motion should start. Usually set to [Node3D.global_transform<class_Node3D_property_global_transform>] for the current body's transform.


----



[float<class_float>] **margin** = `0.001` [🔗<class_PhysicsTestMotionParameters3D_property_margin>]


- |void| **set_margin**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_margin**\ (\ )

Increases the size of the shapes involved in the collision detection.


----



[int<class_int>] **max_collisions** = `1` [🔗<class_PhysicsTestMotionParameters3D_property_max_collisions>]


- |void| **set_max_collisions**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_max_collisions**\ (\ )

Maximum number of returned collisions, between `1` and `32`. Always returns the deepest detected collisions.


----



[Vector3<class_Vector3>] **motion** = `Vector3(0, 0, 0)` [🔗<class_PhysicsTestMotionParameters3D_property_motion>]


- |void| **set_motion**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_motion**\ (\ )

Motion vector to define the length and direction of the motion to test.


----



[bool<class_bool>] **recovery_as_collision** = `false` [🔗<class_PhysicsTestMotionParameters3D_property_recovery_as_collision>]


- |void| **set_recovery_as_collision_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_recovery_as_collision_enabled**\ (\ )

If set to `true`, any depenetration from the recovery phase is reported as a collision; this is used e.g. by [CharacterBody3D<class_CharacterBody3D>] for improving floor detection during floor snapping.

If set to `false`, only collisions resulting from the motion are reported, which is generally the desired behavior.

