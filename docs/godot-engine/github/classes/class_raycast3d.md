:github_url: hide



# RayCast3D

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A ray in 3D space, used to find the first collision object it intersects.


## Description

A raycast represents a ray from its origin to its [target_position<class_RayCast3D_property_target_position>] that finds the closest object along its path, if it intersects any.

\ **RayCast3D** can ignore some objects by adding them to an exception list, by making its detection reporting ignore [Area3D<class_Area3D>]\ s ([collide_with_areas<class_RayCast3D_property_collide_with_areas>]) or [PhysicsBody3D<class_PhysicsBody3D>]\ s ([collide_with_bodies<class_RayCast3D_property_collide_with_bodies>]), or by configuring physics layers.

\ **RayCast3D** calculates intersection every physics frame, and it holds the result until the next physics frame. For an immediate raycast, or if you want to configure a **RayCast3D** multiple times within the same physics frame, use [force_raycast_update()<class_RayCast3D_method_force_raycast_update>].

To sweep over a region of 3D space, you can approximate the region with multiple **RayCast3D**\ s or use [ShapeCast3D<class_ShapeCast3D>].


## Tutorials

- [../tutorials/physics/ray-casting](Ray-casting .md)

- [3D Voxel Demo ](https://godotengine.org/asset-library/asset/2755)_


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`       | :ref:`collide_with_areas<class_RayCast3D_property_collide_with_areas>`             | ``false``             |
> +-------------------------------+------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`       | :ref:`collide_with_bodies<class_RayCast3D_property_collide_with_bodies>`           | ``true``              |
> +-------------------------------+------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`         | :ref:`collision_mask<class_RayCast3D_property_collision_mask>`                     | ``1``                 |
> +-------------------------------+------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`     | :ref:`debug_shape_custom_color<class_RayCast3D_property_debug_shape_custom_color>` | ``Color(0, 0, 0, 1)`` |
> +-------------------------------+------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`         | :ref:`debug_shape_thickness<class_RayCast3D_property_debug_shape_thickness>`       | ``2``                 |
> +-------------------------------+------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`       | :ref:`enabled<class_RayCast3D_property_enabled>`                                   | ``true``              |
> +-------------------------------+------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`       | :ref:`exclude_parent<class_RayCast3D_property_exclude_parent>`                     | ``true``              |
> +-------------------------------+------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`       | :ref:`hit_back_faces<class_RayCast3D_property_hit_back_faces>`                     | ``true``              |
> +-------------------------------+------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`       | :ref:`hit_from_inside<class_RayCast3D_property_hit_from_inside>`                   | ``false``             |
> +-------------------------------+------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`target_position<class_RayCast3D_property_target_position>`                   | ``Vector3(0, -1, 0)`` |
> +-------------------------------+------------------------------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`add_exception<class_RayCast3D_method_add_exception>`\ (\ node\: :ref:`CollisionObject3D<class_CollisionObject3D>`\ )                                    |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`add_exception_rid<class_RayCast3D_method_add_exception_rid>`\ (\ rid\: :ref:`RID<class_RID>`\ )                                                         |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`clear_exceptions<class_RayCast3D_method_clear_exceptions>`\ (\ )                                                                                        |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`force_raycast_update<class_RayCast3D_method_force_raycast_update>`\ (\ )                                                                                |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`   | :ref:`get_collider<class_RayCast3D_method_get_collider>`\ (\ ) |const|                                                                                        |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`         | :ref:`get_collider_rid<class_RayCast3D_method_get_collider_rid>`\ (\ ) |const|                                                                                |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collider_shape<class_RayCast3D_method_get_collider_shape>`\ (\ ) |const|                                                                            |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_collision_face_index<class_RayCast3D_method_get_collision_face_index>`\ (\ ) |const|                                                                |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`get_collision_mask_value<class_RayCast3D_method_get_collision_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`\ ) |const|                          |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_collision_normal<class_RayCast3D_method_get_collision_normal>`\ (\ ) |const|                                                                        |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_collision_point<class_RayCast3D_method_get_collision_point>`\ (\ ) |const|                                                                          |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`is_colliding<class_RayCast3D_method_is_colliding>`\ (\ ) |const|                                                                                        |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`remove_exception<class_RayCast3D_method_remove_exception>`\ (\ node\: :ref:`CollisionObject3D<class_CollisionObject3D>`\ )                              |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`remove_exception_rid<class_RayCast3D_method_remove_exception_rid>`\ (\ rid\: :ref:`RID<class_RID>`\ )                                                   |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_collision_mask_value<class_RayCast3D_method_set_collision_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`, value\: :ref:`bool<class_bool>`\ ) |
> +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **collide_with_areas** = `false` [🔗<class_RayCast3D_property_collide_with_areas>]


- |void| **set_collide_with_areas**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_collide_with_areas_enabled**\ (\ )

If `true`, collisions with [Area3D<class_Area3D>]\ s will be reported.


----



[bool<class_bool>] **collide_with_bodies** = `true` [🔗<class_RayCast3D_property_collide_with_bodies>]


- |void| **set_collide_with_bodies**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_collide_with_bodies_enabled**\ (\ )

If `true`, collisions with [PhysicsBody3D<class_PhysicsBody3D>]\ s will be reported.


----



[int<class_int>] **collision_mask** = `1` [🔗<class_RayCast3D_property_collision_mask>]


- |void| **set_collision_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_mask**\ (\ )

The ray's collision mask. Only objects in at least one collision layer enabled in the mask will be detected. See [Collision layers and masks ](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)_ in the documentation for more information.


----



[Color<class_Color>] **debug_shape_custom_color** = `Color(0, 0, 0, 1)` [🔗<class_RayCast3D_property_debug_shape_custom_color>]


- |void| **set_debug_shape_custom_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_debug_shape_custom_color**\ (\ )

The custom color to use to draw the shape in the editor and at run-time if **Visible Collision Shapes** is enabled in the **Debug** menu. This color will be highlighted at run-time if the **RayCast3D** is colliding with something.

If set to `Color(0.0, 0.0, 0.0)` (by default), the color set in [ProjectSettings.debug/shapes/collision/shape_color<class_ProjectSettings_property_debug/shapes/collision/shape_color>] is used.


----



[int<class_int>] **debug_shape_thickness** = `2` [🔗<class_RayCast3D_property_debug_shape_thickness>]


- |void| **set_debug_shape_thickness**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_debug_shape_thickness**\ (\ )

If set to `1`, a line is used as the debug shape. Otherwise, a truncated pyramid is drawn to represent the **RayCast3D**. Requires **Visible Collision Shapes** to be enabled in the **Debug** menu for the debug shape to be visible at run-time.


----



[bool<class_bool>] **enabled** = `true` [🔗<class_RayCast3D_property_enabled>]


- |void| **set_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_enabled**\ (\ )

If `true`, collisions will be reported.


----



[bool<class_bool>] **exclude_parent** = `true` [🔗<class_RayCast3D_property_exclude_parent>]


- |void| **set_exclude_parent_body**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_exclude_parent_body**\ (\ )

If `true`, this raycast will not report collisions with its parent node. This property only has an effect if the parent node is a [CollisionObject3D<class_CollisionObject3D>]. See also [Node.get_parent()<class_Node_method_get_parent>] and [add_exception()<class_RayCast3D_method_add_exception>].


----



[bool<class_bool>] **hit_back_faces** = `true` [🔗<class_RayCast3D_property_hit_back_faces>]


- |void| **set_hit_back_faces**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_hit_back_faces_enabled**\ (\ )

If `true`, the ray will hit back faces with concave polygon shapes with back face enabled or heightmap shapes.


----



[bool<class_bool>] **hit_from_inside** = `false` [🔗<class_RayCast3D_property_hit_from_inside>]


- |void| **set_hit_from_inside**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_hit_from_inside_enabled**\ (\ )

If `true`, the ray will detect a hit when starting inside shapes. In this case the collision normal will be `Vector3(0, 0, 0)`. Does not affect shapes with no volume like concave polygon or heightmap.


----



[Vector3<class_Vector3>] **target_position** = `Vector3(0, -1, 0)` [🔗<class_RayCast3D_property_target_position>]


- |void| **set_target_position**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_target_position**\ (\ )

The ray's destination point, relative to this raycast's [Node3D.position<class_Node3D_property_position>].


----


## Method Descriptions



|void| **add_exception**\ (\ node\: [CollisionObject3D<class_CollisionObject3D>]\ ) [🔗<class_RayCast3D_method_add_exception>]

Adds a collision exception so the ray does not report collisions with the specified `node`.


----



|void| **add_exception_rid**\ (\ rid\: [RID<class_RID>]\ ) [🔗<class_RayCast3D_method_add_exception_rid>]

Adds a collision exception so the ray does not report collisions with the specified [RID<class_RID>].


----



|void| **clear_exceptions**\ (\ ) [🔗<class_RayCast3D_method_clear_exceptions>]

Removes all collision exceptions for this ray.


----



|void| **force_raycast_update**\ (\ ) [🔗<class_RayCast3D_method_force_raycast_update>]

Updates the collision information for the ray immediately, without waiting for the next `_physics_process` call. Use this method, for example, when the ray or its parent has changed state.

\ **Note:** [enabled<class_RayCast3D_property_enabled>] does not need to be `true` for this to work.


----



[Object<class_Object>] **get_collider**\ (\ ) |const| [🔗<class_RayCast3D_method_get_collider>]

Returns the first object that the ray intersects, or `null` if no object is intersecting the ray (i.e. [is_colliding()<class_RayCast3D_method_is_colliding>] returns `false`).

\ **Note:** This object is not guaranteed to be a [CollisionObject3D<class_CollisionObject3D>]. For example, if the ray intersects a [CSGShape3D<class_CSGShape3D>] or a [GridMap<class_GridMap>], the method will return a [CSGShape3D<class_CSGShape3D>] or [GridMap<class_GridMap>] instance.


----



[RID<class_RID>] **get_collider_rid**\ (\ ) |const| [🔗<class_RayCast3D_method_get_collider_rid>]

Returns the [RID<class_RID>] of the first object that the ray intersects, or an empty [RID<class_RID>] if no object is intersecting the ray (i.e. [is_colliding()<class_RayCast3D_method_is_colliding>] returns `false`).


----



[int<class_int>] **get_collider_shape**\ (\ ) |const| [🔗<class_RayCast3D_method_get_collider_shape>]

Returns the shape ID of the first object that the ray intersects, or `0` if no object is intersecting the ray (i.e. [is_colliding()<class_RayCast3D_method_is_colliding>] returns `false`).

To get the intersected shape node, for a [CollisionObject3D<class_CollisionObject3D>] target, use:


> **TABS**
>

    var target = get_collider() # A CollisionObject3D.
    var shape_id = get_collider_shape() # The shape index in the collider.
    var owner_id = target.shape_find_owner(shape_id) # The owner ID in the collider.
    var shape = target.shape_owner_get_owner(owner_id)


    var target = (CollisionObject3D)GetCollider(); // A CollisionObject3D.
    var shapeId = GetColliderShape(); // The shape index in the collider.
    var ownerId = target.ShapeFindOwner(shapeId); // The owner ID in the collider.
    var shape = target.ShapeOwnerGetOwner(ownerId);




----



[int<class_int>] **get_collision_face_index**\ (\ ) |const| [🔗<class_RayCast3D_method_get_collision_face_index>]

Returns the collision object's face index at the collision point, or `-1` if the shape intersecting the ray is not a [ConcavePolygonShape3D<class_ConcavePolygonShape3D>].


----



[bool<class_bool>] **get_collision_mask_value**\ (\ layer_number\: [int<class_int>]\ ) |const| [🔗<class_RayCast3D_method_get_collision_mask_value>]

Returns whether or not the specified layer of the [collision_mask<class_RayCast3D_property_collision_mask>] is enabled, given a `layer_number` between 1 and 32.


----



[Vector3<class_Vector3>] **get_collision_normal**\ (\ ) |const| [🔗<class_RayCast3D_method_get_collision_normal>]

Returns the normal of the intersecting object's shape at the collision point, or `Vector3(0, 0, 0)` if the ray starts inside the shape and [hit_from_inside<class_RayCast3D_property_hit_from_inside>] is `true`.

\ **Note:** Check that [is_colliding()<class_RayCast3D_method_is_colliding>] returns `true` before calling this method to ensure the returned normal is valid and up-to-date.


----



[Vector3<class_Vector3>] **get_collision_point**\ (\ ) |const| [🔗<class_RayCast3D_method_get_collision_point>]

Returns the collision point at which the ray intersects the closest object, in the global coordinate system. If [hit_from_inside<class_RayCast3D_property_hit_from_inside>] is `true` and the ray starts inside of a collision shape, this function will return the origin point of the ray.

\ **Note:** Check that [is_colliding()<class_RayCast3D_method_is_colliding>] returns `true` before calling this method to ensure the returned point is valid and up-to-date.


----



[bool<class_bool>] **is_colliding**\ (\ ) |const| [🔗<class_RayCast3D_method_is_colliding>]

Returns whether any object is intersecting with the ray's vector (considering the vector length).


----



|void| **remove_exception**\ (\ node\: [CollisionObject3D<class_CollisionObject3D>]\ ) [🔗<class_RayCast3D_method_remove_exception>]

Removes a collision exception so the ray can report collisions with the specified `node`.


----



|void| **remove_exception_rid**\ (\ rid\: [RID<class_RID>]\ ) [🔗<class_RayCast3D_method_remove_exception_rid>]

Removes a collision exception so the ray can report collisions with the specified [RID<class_RID>].


----



|void| **set_collision_mask_value**\ (\ layer_number\: [int<class_int>], value\: [bool<class_bool>]\ ) [🔗<class_RayCast3D_method_set_collision_mask_value>]

Based on `value`, enables or disables the specified layer in the [collision_mask<class_RayCast3D_property_collision_mask>], given a `layer_number` between 1 and 32.

