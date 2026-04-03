:github_url: hide



# PathFollow2D

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Point sampler for a [Path2D<class_Path2D>].


## Description

This node takes its parent [Path2D<class_Path2D>], and returns the coordinates of a point within it, given a distance from the first vertex.

It is useful for making other nodes follow a path, without coding the movement pattern. For that, the nodes must be children of this node. The descendant nodes will then move accordingly when setting the [progress<class_PathFollow2D_property_progress>] in this node.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-------------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>`   | :ref:`cubic_interp<class_PathFollow2D_property_cubic_interp>`     | ``true`` |
> +---------------------------+-------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`h_offset<class_PathFollow2D_property_h_offset>`             | ``0.0``  |
> +---------------------------+-------------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>`   | :ref:`loop<class_PathFollow2D_property_loop>`                     | ``true`` |
> +---------------------------+-------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`progress<class_PathFollow2D_property_progress>`             | ``0.0``  |
> +---------------------------+-------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`progress_ratio<class_PathFollow2D_property_progress_ratio>` | ``0.0``  |
> +---------------------------+-------------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>`   | :ref:`rotates<class_PathFollow2D_property_rotates>`               | ``true`` |
> +---------------------------+-------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`v_offset<class_PathFollow2D_property_v_offset>`             | ``0.0``  |
> +---------------------------+-------------------------------------------------------------------+----------+
>

----


## Property Descriptions



[bool<class_bool>] **cubic_interp** = `true` [🔗<class_PathFollow2D_property_cubic_interp>]


- |void| **set_cubic_interpolation**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_cubic_interpolation**\ (\ )

If `true`, the position between two cached points is interpolated cubically, and linearly otherwise.

The points along the [Curve2D<class_Curve2D>] of the [Path2D<class_Path2D>] are precomputed before use, for faster calculations. The point at the requested offset is then calculated interpolating between two adjacent cached points. This may present a problem if the curve makes sharp turns, as the cached points may not follow the curve closely enough.

There are two answers to this problem: either increase the number of cached points and increase memory consumption, or make a cubic interpolation between two points at the cost of (slightly) slower calculations.


----



[float<class_float>] **h_offset** = `0.0` [🔗<class_PathFollow2D_property_h_offset>]


- |void| **set_h_offset**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_h_offset**\ (\ )

The node's offset along the curve.


----



[bool<class_bool>] **loop** = `true` [🔗<class_PathFollow2D_property_loop>]


- |void| **set_loop**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **has_loop**\ (\ )

If `true`, any offset outside the path's length will wrap around, instead of stopping at the ends. Use it for cyclic paths.


----



[float<class_float>] **progress** = `0.0` [🔗<class_PathFollow2D_property_progress>]


- |void| **set_progress**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_progress**\ (\ )

The distance along the path, in pixels. Changing this value sets this node's position to a point within the path.


----



[float<class_float>] **progress_ratio** = `0.0` [🔗<class_PathFollow2D_property_progress_ratio>]


- |void| **set_progress_ratio**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_progress_ratio**\ (\ )

The distance along the path as a number in the range 0.0 (for the first vertex) to 1.0 (for the last). This is just another way of expressing the progress within the path, as the offset supplied is multiplied internally by the path's length.

It can be set or get only if the **PathFollow2D** is the child of a [Path2D<class_Path2D>] which is part of the scene tree, and that this [Path2D<class_Path2D>] has a [Curve2D<class_Curve2D>] with a non-zero length. Otherwise, trying to set this field will print an error, and getting this field will return `0.0`.


----



[bool<class_bool>] **rotates** = `true` [🔗<class_PathFollow2D_property_rotates>]


- |void| **set_rotates**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_rotating**\ (\ )

If `true`, this node rotates to follow the path, with the +X direction facing forward on the path.


----



[float<class_float>] **v_offset** = `0.0` [🔗<class_PathFollow2D_property_v_offset>]


- |void| **set_v_offset**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_v_offset**\ (\ )

The node's offset perpendicular to the curve.

