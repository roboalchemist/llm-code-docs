:github_url: hide



# CollisionPolygon3D

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A node that provides a thickened polygon shape (a prism) to a [CollisionObject3D<class_CollisionObject3D>] parent.


## Description

A node that provides a thickened polygon shape (a prism) to a [CollisionObject3D<class_CollisionObject3D>] parent and allows it to be edited. The polygon can be concave or convex. This can give a detection shape to an [Area3D<class_Area3D>] or turn a [PhysicsBody3D<class_PhysicsBody3D>] into a solid object.

\ **Warning:** A non-uniformly scaled [CollisionShape3D<class_CollisionShape3D>] will likely not behave as expected. Make sure to keep its scale the same on all axes and adjust its shape resource instead.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-------------------------------------------------------------------+--------------------------+
> | :ref:`Color<class_Color>`                           | :ref:`debug_color<class_CollisionPolygon3D_property_debug_color>` | ``Color(0, 0, 0, 0)``    |
> +-----------------------------------------------------+-------------------------------------------------------------------+--------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`debug_fill<class_CollisionPolygon3D_property_debug_fill>`   | ``true``                 |
> +-----------------------------------------------------+-------------------------------------------------------------------+--------------------------+
> | :ref:`float<class_float>`                           | :ref:`depth<class_CollisionPolygon3D_property_depth>`             | ``1.0``                  |
> +-----------------------------------------------------+-------------------------------------------------------------------+--------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`disabled<class_CollisionPolygon3D_property_disabled>`       | ``false``                |
> +-----------------------------------------------------+-------------------------------------------------------------------+--------------------------+
> | :ref:`float<class_float>`                           | :ref:`margin<class_CollisionPolygon3D_property_margin>`           | ``0.04``                 |
> +-----------------------------------------------------+-------------------------------------------------------------------+--------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>` | :ref:`polygon<class_CollisionPolygon3D_property_polygon>`         | ``PackedVector2Array()`` |
> +-----------------------------------------------------+-------------------------------------------------------------------+--------------------------+
>

----


## Property Descriptions



[Color<class_Color>] **debug_color** = `Color(0, 0, 0, 0)` [🔗<class_CollisionPolygon3D_property_debug_color>]


- |void| **set_debug_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_debug_color**\ (\ )

The collision shape color that is displayed in the editor, or in the running project if **Debug > Visible Collision Shapes** is checked at the top of the editor.

\ **Note:** The default value is [ProjectSettings.debug/shapes/collision/shape_color<class_ProjectSettings_property_debug/shapes/collision/shape_color>]. The `Color(0, 0, 0, 0)` value documented here is a placeholder, and not the actual default debug color.


----



[bool<class_bool>] **debug_fill** = `true` [🔗<class_CollisionPolygon3D_property_debug_fill>]


- |void| **set_enable_debug_fill**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enable_debug_fill**\ (\ )

If `true`, when the shape is displayed, it will show a solid fill color in addition to its wireframe.


----



[float<class_float>] **depth** = `1.0` [🔗<class_CollisionPolygon3D_property_depth>]


- |void| **set_depth**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_depth**\ (\ )

Length that the resulting collision extends in either direction perpendicular to its 2D polygon.


----



[bool<class_bool>] **disabled** = `false` [🔗<class_CollisionPolygon3D_property_disabled>]


- |void| **set_disabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_disabled**\ (\ )

If `true`, no collision will be produced. This property should be changed with [Object.set_deferred()<class_Object_method_set_deferred>].


----



[float<class_float>] **margin** = `0.04` [🔗<class_CollisionPolygon3D_property_margin>]


- |void| **set_margin**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_margin**\ (\ )

The collision margin for the generated [Shape3D<class_Shape3D>]. See [Shape3D.margin<class_Shape3D_property_margin>] for more details.


----



[PackedVector2Array<class_PackedVector2Array>] **polygon** = `PackedVector2Array()` [🔗<class_CollisionPolygon3D_property_polygon>]


- |void| **set_polygon**\ (\ value\: [PackedVector2Array<class_PackedVector2Array>]\ )
- [PackedVector2Array<class_PackedVector2Array>] **get_polygon**\ (\ )

Array of vertices which define the 2D polygon in the local XY plane.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array<class_PackedVector2Array>] for more details.

