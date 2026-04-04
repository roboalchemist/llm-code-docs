:github_url: hide



# PhysicsRayQueryParameters2D

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Provides parameters for [PhysicsDirectSpaceState2D.intersect_ray()<class_PhysicsDirectSpaceState2D_method_intersect_ray>].


## Description

By changing various properties of this object, such as the ray position, you can configure the parameters for [PhysicsDirectSpaceState2D.intersect_ray()<class_PhysicsDirectSpaceState2D_method_intersect_ray>].


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------+--------------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                            | :ref:`collide_with_areas<class_PhysicsRayQueryParameters2D_property_collide_with_areas>`   | ``false``         |
> +----------------------------------------------------+--------------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                            | :ref:`collide_with_bodies<class_PhysicsRayQueryParameters2D_property_collide_with_bodies>` | ``true``          |
> +----------------------------------------------------+--------------------------------------------------------------------------------------------+-------------------+
> | :ref:`int<class_int>`                              | :ref:`collision_mask<class_PhysicsRayQueryParameters2D_property_collision_mask>`           | ``4294967295``    |
> +----------------------------------------------------+--------------------------------------------------------------------------------------------+-------------------+
> | :ref:`Array<class_Array>`\[:ref:`RID<class_RID>`\] | :ref:`exclude<class_PhysicsRayQueryParameters2D_property_exclude>`                         | ``[]``            |
> +----------------------------------------------------+--------------------------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>`                      | :ref:`from<class_PhysicsRayQueryParameters2D_property_from>`                               | ``Vector2(0, 0)`` |
> +----------------------------------------------------+--------------------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`                            | :ref:`hit_from_inside<class_PhysicsRayQueryParameters2D_property_hit_from_inside>`         | ``false``         |
> +----------------------------------------------------+--------------------------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>`                      | :ref:`to<class_PhysicsRayQueryParameters2D_property_to>`                                   | ``Vector2(0, 0)`` |
> +----------------------------------------------------+--------------------------------------------------------------------------------------------+-------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PhysicsRayQueryParameters2D<class_PhysicsRayQueryParameters2D>` | :ref:`create<class_PhysicsRayQueryParameters2D_method_create>`\ (\ from\: :ref:`Vector2<class_Vector2>`, to\: :ref:`Vector2<class_Vector2>`, collision_mask\: :ref:`int<class_int>` = 4294967295, exclude\: :ref:`Array<class_Array>`\[:ref:`RID<class_RID>`\] = []\ ) |static| |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **collide_with_areas** = `false` [🔗<class_PhysicsRayQueryParameters2D_property_collide_with_areas>]


- |void| **set_collide_with_areas**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_collide_with_areas_enabled**\ (\ )

If `true`, the query will take [Area2D<class_Area2D>]\ s into account.


----



[bool<class_bool>] **collide_with_bodies** = `true` [🔗<class_PhysicsRayQueryParameters2D_property_collide_with_bodies>]


- |void| **set_collide_with_bodies**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_collide_with_bodies_enabled**\ (\ )

If `true`, the query will take [PhysicsBody2D<class_PhysicsBody2D>]\ s into account.


----



[int<class_int>] **collision_mask** = `4294967295` [🔗<class_PhysicsRayQueryParameters2D_property_collision_mask>]


- |void| **set_collision_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_mask**\ (\ )

The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. See [Collision layers and masks ](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)_ in the documentation for more information.


----



[Array<class_Array>]\[[RID<class_RID>]\] **exclude** = `[]` [🔗<class_PhysicsRayQueryParameters2D_property_exclude>]


- |void| **set_exclude**\ (\ value\: [Array<class_Array>]\[[RID<class_RID>]\]\ )
- [Array<class_Array>]\[[RID<class_RID>]\] **get_exclude**\ (\ )

The list of object [RID<class_RID>]\ s that will be excluded from collisions. Use [CollisionObject2D.get_rid()<class_CollisionObject2D_method_get_rid>] to get the [RID<class_RID>] associated with a [CollisionObject2D<class_CollisionObject2D>]-derived node.

\ **Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.


----



[Vector2<class_Vector2>] **from** = `Vector2(0, 0)` [🔗<class_PhysicsRayQueryParameters2D_property_from>]


- |void| **set_from**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_from**\ (\ )

The starting point of the ray being queried for, in global coordinates.


----



[bool<class_bool>] **hit_from_inside** = `false` [🔗<class_PhysicsRayQueryParameters2D_property_hit_from_inside>]


- |void| **set_hit_from_inside**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_hit_from_inside_enabled**\ (\ )

If `true`, the query will detect a hit when starting inside shapes. In this case the collision normal will be `Vector2(0, 0)`. Does not affect concave polygon shapes.


----



[Vector2<class_Vector2>] **to** = `Vector2(0, 0)` [🔗<class_PhysicsRayQueryParameters2D_property_to>]


- |void| **set_to**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_to**\ (\ )

The ending point of the ray being queried for, in global coordinates.


----


## Method Descriptions



[PhysicsRayQueryParameters2D<class_PhysicsRayQueryParameters2D>] **create**\ (\ from\: [Vector2<class_Vector2>], to\: [Vector2<class_Vector2>], collision_mask\: [int<class_int>] = 4294967295, exclude\: [Array<class_Array>]\[[RID<class_RID>]\] = []\ ) |static| [🔗<class_PhysicsRayQueryParameters2D_method_create>]

Returns a new, pre-configured **PhysicsRayQueryParameters2D** object. Use it to quickly create query parameters using the most common options.

::

    var query = PhysicsRayQueryParameters2D.create(global_position, global_position + Vector2(0, 100))
    var collision = get_world_2d().direct_space_state.intersect_ray(query)

