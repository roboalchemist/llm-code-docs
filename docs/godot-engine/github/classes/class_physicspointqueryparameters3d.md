:github_url: hide



# PhysicsPointQueryParameters3D

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Provides parameters for [PhysicsDirectSpaceState3D.intersect_point()<class_PhysicsDirectSpaceState3D_method_intersect_point>].


## Description

By changing various properties of this object, such as the point position, you can configure the parameters for [PhysicsDirectSpaceState3D.intersect_point()<class_PhysicsDirectSpaceState3D_method_intersect_point>].


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------+
> | :ref:`bool<class_bool>`                            | :ref:`collide_with_areas<class_PhysicsPointQueryParameters3D_property_collide_with_areas>`   | ``false``            |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------+
> | :ref:`bool<class_bool>`                            | :ref:`collide_with_bodies<class_PhysicsPointQueryParameters3D_property_collide_with_bodies>` | ``true``             |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`                              | :ref:`collision_mask<class_PhysicsPointQueryParameters3D_property_collision_mask>`           | ``4294967295``       |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------+
> | :ref:`Array<class_Array>`\[:ref:`RID<class_RID>`\] | :ref:`exclude<class_PhysicsPointQueryParameters3D_property_exclude>`                         | ``[]``               |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>`                      | :ref:`position<class_PhysicsPointQueryParameters3D_property_position>`                       | ``Vector3(0, 0, 0)`` |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------+
>

----


## Property Descriptions



[bool<class_bool>] **collide_with_areas** = `false` [🔗<class_PhysicsPointQueryParameters3D_property_collide_with_areas>]


- |void| **set_collide_with_areas**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_collide_with_areas_enabled**\ (\ )

If `true`, the query will take [Area3D<class_Area3D>]\ s into account.


----



[bool<class_bool>] **collide_with_bodies** = `true` [🔗<class_PhysicsPointQueryParameters3D_property_collide_with_bodies>]


- |void| **set_collide_with_bodies**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_collide_with_bodies_enabled**\ (\ )

If `true`, the query will take [PhysicsBody3D<class_PhysicsBody3D>]\ s into account.


----



[int<class_int>] **collision_mask** = `4294967295` [🔗<class_PhysicsPointQueryParameters3D_property_collision_mask>]


- |void| **set_collision_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_mask**\ (\ )

The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. See [Collision layers and masks ](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)_ in the documentation for more information.


----



[Array<class_Array>]\[[RID<class_RID>]\] **exclude** = `[]` [🔗<class_PhysicsPointQueryParameters3D_property_exclude>]


- |void| **set_exclude**\ (\ value\: [Array<class_Array>]\[[RID<class_RID>]\]\ )
- [Array<class_Array>]\[[RID<class_RID>]\] **get_exclude**\ (\ )

The list of object [RID<class_RID>]\ s that will be excluded from collisions. Use [CollisionObject3D.get_rid()<class_CollisionObject3D_method_get_rid>] to get the [RID<class_RID>] associated with a [CollisionObject3D<class_CollisionObject3D>]-derived node.

\ **Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.


----



[Vector3<class_Vector3>] **position** = `Vector3(0, 0, 0)` [🔗<class_PhysicsPointQueryParameters3D_property_position>]


- |void| **set_position**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_position**\ (\ )

The position being queried for, in global coordinates.

