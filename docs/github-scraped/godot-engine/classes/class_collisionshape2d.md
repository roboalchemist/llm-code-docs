:github_url: hide



# CollisionShape2D

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A node that provides a [Shape2D<class_Shape2D>] to a [CollisionObject2D<class_CollisionObject2D>] parent.


## Description

A node that provides a [Shape2D<class_Shape2D>] to a [CollisionObject2D<class_CollisionObject2D>] parent and allows it to be edited. This can give a detection shape to an [Area2D<class_Area2D>] or turn a [PhysicsBody2D<class_PhysicsBody2D>] into a solid object.


## Tutorials

- [../tutorials/physics/physics_introduction](Physics introduction .md)

- [2D Dodge The Creeps Demo ](https://godotengine.org/asset-library/asset/2712)_

- [2D Pong Demo ](https://godotengine.org/asset-library/asset/2728)_

- [2D Kinematic Character Demo ](https://godotengine.org/asset-library/asset/2719)_


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`     | :ref:`debug_color<class_CollisionShape2D_property_debug_color>`                           | ``Color(0, 0, 0, 0)`` |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`       | :ref:`disabled<class_CollisionShape2D_property_disabled>`                                 | ``false``             |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`       | :ref:`one_way_collision<class_CollisionShape2D_property_one_way_collision>`               | ``false``             |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`     | :ref:`one_way_collision_margin<class_CollisionShape2D_property_one_way_collision_margin>` | ``1.0``               |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Shape2D<class_Shape2D>` | :ref:`shape<class_CollisionShape2D_property_shape>`                                       |                       |
> +-------------------------------+-------------------------------------------------------------------------------------------+-----------------------+
>

----


## Property Descriptions



[Color<class_Color>] **debug_color** = `Color(0, 0, 0, 0)` [🔗<class_CollisionShape2D_property_debug_color>]


- |void| **set_debug_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_debug_color**\ (\ )

The collision shape color that is displayed in the editor, or in the running project if **Debug > Visible Collision Shapes** is checked at the top of the editor.

\ **Note:** The default value is [ProjectSettings.debug/shapes/collision/shape_color<class_ProjectSettings_property_debug/shapes/collision/shape_color>]. The `Color(0, 0, 0, 0)` value documented here is a placeholder, and not the actual default debug color.


----



[bool<class_bool>] **disabled** = `false` [🔗<class_CollisionShape2D_property_disabled>]


- |void| **set_disabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_disabled**\ (\ )

A disabled collision shape has no effect in the world. This property should be changed with [Object.set_deferred()<class_Object_method_set_deferred>].


----



[bool<class_bool>] **one_way_collision** = `false` [🔗<class_CollisionShape2D_property_one_way_collision>]


- |void| **set_one_way_collision**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_one_way_collision_enabled**\ (\ )

Sets whether this collision shape should only detect collision on one side (top or bottom).

\ **Note:** This property has no effect if this **CollisionShape2D** is a child of an [Area2D<class_Area2D>] node.


----



[float<class_float>] **one_way_collision_margin** = `1.0` [🔗<class_CollisionShape2D_property_one_way_collision_margin>]


- |void| **set_one_way_collision_margin**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_one_way_collision_margin**\ (\ )

The margin used for one-way collision (in pixels). Higher values will make the shape thicker, and work better for colliders that enter the shape at a high velocity.


----



[Shape2D<class_Shape2D>] **shape** [🔗<class_CollisionShape2D_property_shape>]


- |void| **set_shape**\ (\ value\: [Shape2D<class_Shape2D>]\ )
- [Shape2D<class_Shape2D>] **get_shape**\ (\ )

The actual shape owned by this collision shape.

