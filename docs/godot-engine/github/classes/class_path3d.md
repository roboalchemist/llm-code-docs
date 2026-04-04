:github_url: hide



# Path3D

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Contains a [Curve3D<class_Curve3D>] path for [PathFollow3D<class_PathFollow3D>] nodes to follow.


## Description

Can have [PathFollow3D<class_PathFollow3D>] child nodes moving along the [Curve3D<class_Curve3D>]. See [PathFollow3D<class_PathFollow3D>] for more information on the usage.

Note that the path is considered as relative to the moved nodes (children of [PathFollow3D<class_PathFollow3D>]). As such, the curve should usually start with a zero vector `(0, 0, 0)`.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+---------------------------------------------------------------------+-----------------------+
> | :ref:`Curve3D<class_Curve3D>` | :ref:`curve<class_Path3D_property_curve>`                           |                       |
> +-------------------------------+---------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`     | :ref:`debug_custom_color<class_Path3D_property_debug_custom_color>` | ``Color(0, 0, 0, 1)`` |
> +-------------------------------+---------------------------------------------------------------------+-----------------------+
>

----


## Signals



**curve_changed**\ (\ ) [🔗<class_Path3D_signal_curve_changed>]

Emitted when the [curve<class_Path3D_property_curve>] changes.


----



**debug_color_changed**\ (\ ) [🔗<class_Path3D_signal_debug_color_changed>]

Emitted when the [debug_custom_color<class_Path3D_property_debug_custom_color>] changes.


----


## Property Descriptions



[Curve3D<class_Curve3D>] **curve** [🔗<class_Path3D_property_curve>]


- |void| **set_curve**\ (\ value\: [Curve3D<class_Curve3D>]\ )
- [Curve3D<class_Curve3D>] **get_curve**\ (\ )

A [Curve3D<class_Curve3D>] describing the path.


----



[Color<class_Color>] **debug_custom_color** = `Color(0, 0, 0, 1)` [🔗<class_Path3D_property_debug_custom_color>]


- |void| **set_debug_custom_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_debug_custom_color**\ (\ )

The custom color used to draw the path in the editor. If set to [Color.BLACK<class_Color_constant_BLACK>] (as by default), the color set in [ProjectSettings.debug/shapes/paths/geometry_color<class_ProjectSettings_property_debug/shapes/paths/geometry_color>] is used.

