:github_url: hide



# CollisionPolygon2D

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A node that provides a polygon shape to a [CollisionObject2D<class_CollisionObject2D>] parent.


## Description

A node that provides a polygon shape to a [CollisionObject2D<class_CollisionObject2D>] parent and allows it to be edited. The polygon can be concave or convex. This can give a detection shape to an [Area2D<class_Area2D>], turn a [PhysicsBody2D<class_PhysicsBody2D>] into a solid object, or give a hollow shape to a [StaticBody2D<class_StaticBody2D>].

\ **Warning:** A non-uniformly scaled **CollisionPolygon2D** will likely not behave as expected. Make sure to keep its scale the same on all axes and adjust its polygon instead.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`BuildMode<enum_CollisionPolygon2D_BuildMode>` | :ref:`build_mode<class_CollisionPolygon2D_property_build_mode>`                             | ``0``                    |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`disabled<class_CollisionPolygon2D_property_disabled>`                                 | ``false``                |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`one_way_collision<class_CollisionPolygon2D_property_one_way_collision>`               | ``false``                |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`float<class_float>`                           | :ref:`one_way_collision_margin<class_CollisionPolygon2D_property_one_way_collision_margin>` | ``1.0``                  |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>` | :ref:`polygon<class_CollisionPolygon2D_property_polygon>`                                   | ``PackedVector2Array()`` |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------+--------------------------+
>

----


## Enumerations



enum **BuildMode**: [🔗<enum_CollisionPolygon2D_BuildMode>]



[BuildMode<enum_CollisionPolygon2D_BuildMode>] **BUILD_SOLIDS** = `0`

Collisions will include the polygon and its contained area. In this mode the node has the same effect as several [ConvexPolygonShape2D<class_ConvexPolygonShape2D>] nodes, one for each convex shape in the convex decomposition of the polygon (but without the overhead of multiple nodes).



[BuildMode<enum_CollisionPolygon2D_BuildMode>] **BUILD_SEGMENTS** = `1`

Collisions will only include the polygon edges. In this mode the node has the same effect as a single [ConcavePolygonShape2D<class_ConcavePolygonShape2D>] made of segments, with the restriction that each segment (after the first one) starts where the previous one ends, and the last one ends where the first one starts (forming a closed but hollow polygon).


----


## Property Descriptions



[BuildMode<enum_CollisionPolygon2D_BuildMode>] **build_mode** = `0` [🔗<class_CollisionPolygon2D_property_build_mode>]


- |void| **set_build_mode**\ (\ value\: [BuildMode<enum_CollisionPolygon2D_BuildMode>]\ )
- [BuildMode<enum_CollisionPolygon2D_BuildMode>] **get_build_mode**\ (\ )

Collision build mode.


----



[bool<class_bool>] **disabled** = `false` [🔗<class_CollisionPolygon2D_property_disabled>]


- |void| **set_disabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_disabled**\ (\ )

If `true`, no collisions will be detected. This property should be changed with [Object.set_deferred()<class_Object_method_set_deferred>].


----



[bool<class_bool>] **one_way_collision** = `false` [🔗<class_CollisionPolygon2D_property_one_way_collision>]


- |void| **set_one_way_collision**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_one_way_collision_enabled**\ (\ )

If `true`, only edges that face up, relative to **CollisionPolygon2D**'s rotation, will collide with other objects.

\ **Note:** This property has no effect if this **CollisionPolygon2D** is a child of an [Area2D<class_Area2D>] node.


----



[float<class_float>] **one_way_collision_margin** = `1.0` [🔗<class_CollisionPolygon2D_property_one_way_collision_margin>]


- |void| **set_one_way_collision_margin**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_one_way_collision_margin**\ (\ )

The margin used for one-way collision (in pixels). Higher values will make the shape thicker, and work better for colliders that enter the polygon at a high velocity.


----



[PackedVector2Array<class_PackedVector2Array>] **polygon** = `PackedVector2Array()` [🔗<class_CollisionPolygon2D_property_polygon>]


- |void| **set_polygon**\ (\ value\: [PackedVector2Array<class_PackedVector2Array>]\ )
- [PackedVector2Array<class_PackedVector2Array>] **get_polygon**\ (\ )

The polygon's list of vertices. Each point will be connected to the next, and the final point will be connected to the first.

\ **Note:** The returned vertices are in the local coordinate space of the given **CollisionPolygon2D**.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array<class_PackedVector2Array>] for more details.

