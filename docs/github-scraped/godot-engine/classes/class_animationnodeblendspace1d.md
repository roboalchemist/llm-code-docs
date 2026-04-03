:github_url: hide



# AnimationNodeBlendSpace1D

**Inherits:** [AnimationRootNode<class_AnimationRootNode>] **<** [AnimationNode<class_AnimationNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A set of [AnimationRootNode<class_AnimationRootNode>]\ s placed on a virtual axis, crossfading between the two adjacent ones. Used by [AnimationTree<class_AnimationTree>].


## Description

A resource used by [AnimationNodeBlendTree<class_AnimationNodeBlendTree>].

\ **AnimationNodeBlendSpace1D** represents a virtual axis on which any type of [AnimationRootNode<class_AnimationRootNode>]\ s can be added using [add_blend_point()<class_AnimationNodeBlendSpace1D_method_add_blend_point>]. Outputs the linear blend of the two [AnimationRootNode<class_AnimationRootNode>]\ s adjacent to the current value.

You can set the extents of the axis with [min_space<class_AnimationNodeBlendSpace1D_property_min_space>] and [max_space<class_AnimationNodeBlendSpace1D_property_max_space>].


## Tutorials

- [../tutorials/animation/animation_tree](Using AnimationTree .md)


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------+--------------------------------------------------------------------------+-------------+
> | :ref:`BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>` | :ref:`blend_mode<class_AnimationNodeBlendSpace1D_property_blend_mode>`   | ``0``       |
> +------------------------------------------------------------+--------------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>`                                  | :ref:`max_space<class_AnimationNodeBlendSpace1D_property_max_space>`     | ``1.0``     |
> +------------------------------------------------------------+--------------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>`                                  | :ref:`min_space<class_AnimationNodeBlendSpace1D_property_min_space>`     | ``-1.0``    |
> +------------------------------------------------------------+--------------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>`                                  | :ref:`snap<class_AnimationNodeBlendSpace1D_property_snap>`               | ``0.1``     |
> +------------------------------------------------------------+--------------------------------------------------------------------------+-------------+
> | :ref:`bool<class_bool>`                                    | :ref:`sync<class_AnimationNodeBlendSpace1D_property_sync>`               | ``false``   |
> +------------------------------------------------------------+--------------------------------------------------------------------------+-------------+
> | :ref:`String<class_String>`                                | :ref:`value_label<class_AnimationNodeBlendSpace1D_property_value_label>` | ``"value"`` |
> +------------------------------------------------------------+--------------------------------------------------------------------------+-------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`add_blend_point<class_AnimationNodeBlendSpace1D_method_add_blend_point>`\ (\ node\: :ref:`AnimationRootNode<class_AnimationRootNode>`, pos\: :ref:`float<class_float>`, at_index\: :ref:`int<class_int>` = -1\ ) |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`get_blend_point_count<class_AnimationNodeBlendSpace1D_method_get_blend_point_count>`\ (\ ) |const|                                                                                                               |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AnimationRootNode<class_AnimationRootNode>` | :ref:`get_blend_point_node<class_AnimationNodeBlendSpace1D_method_get_blend_point_node>`\ (\ point\: :ref:`int<class_int>`\ ) |const|                                                                                  |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                         | :ref:`get_blend_point_position<class_AnimationNodeBlendSpace1D_method_get_blend_point_position>`\ (\ point\: :ref:`int<class_int>`\ ) |const|                                                                          |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`remove_blend_point<class_AnimationNodeBlendSpace1D_method_remove_blend_point>`\ (\ point\: :ref:`int<class_int>`\ )                                                                                              |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_blend_point_node<class_AnimationNodeBlendSpace1D_method_set_blend_point_node>`\ (\ point\: :ref:`int<class_int>`, node\: :ref:`AnimationRootNode<class_AnimationRootNode>`\ )                                |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_blend_point_position<class_AnimationNodeBlendSpace1D_method_set_blend_point_position>`\ (\ point\: :ref:`int<class_int>`, pos\: :ref:`float<class_float>`\ )                                                 |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **BlendMode**: [🔗<enum_AnimationNodeBlendSpace1D_BlendMode>]



[BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>] **BLEND_MODE_INTERPOLATED** = `0`

The interpolation between animations is linear.



[BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>] **BLEND_MODE_DISCRETE** = `1`

The blend space plays the animation of the animation node which blending position is closest to. Useful for frame-by-frame 2D animations.



[BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>] **BLEND_MODE_DISCRETE_CARRY** = `2`

Similar to [BLEND_MODE_DISCRETE<class_AnimationNodeBlendSpace1D_constant_BLEND_MODE_DISCRETE>], but starts the new animation at the last animation's playback position.


----


## Property Descriptions



[BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>] **blend_mode** = `0` [🔗<class_AnimationNodeBlendSpace1D_property_blend_mode>]


- |void| **set_blend_mode**\ (\ value\: [BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>]\ )
- [BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>] **get_blend_mode**\ (\ )

Controls the interpolation between animations.


----



[float<class_float>] **max_space** = `1.0` [🔗<class_AnimationNodeBlendSpace1D_property_max_space>]


- |void| **set_max_space**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_max_space**\ (\ )

The blend space's axis's upper limit for the points' position. See [add_blend_point()<class_AnimationNodeBlendSpace1D_method_add_blend_point>].


----



[float<class_float>] **min_space** = `-1.0` [🔗<class_AnimationNodeBlendSpace1D_property_min_space>]


- |void| **set_min_space**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_min_space**\ (\ )

The blend space's axis's lower limit for the points' position. See [add_blend_point()<class_AnimationNodeBlendSpace1D_method_add_blend_point>].


----



[float<class_float>] **snap** = `0.1` [🔗<class_AnimationNodeBlendSpace1D_property_snap>]


- |void| **set_snap**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_snap**\ (\ )

Position increment to snap to when moving a point on the axis.


----



[bool<class_bool>] **sync** = `false` [🔗<class_AnimationNodeBlendSpace1D_property_sync>]


- |void| **set_use_sync**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_sync**\ (\ )

If `false`, the blended animations' frame are stopped when the blend value is `0`.

If `true`, forcing the blended animations to advance frame.


----



[String<class_String>] **value_label** = `"value"` [🔗<class_AnimationNodeBlendSpace1D_property_value_label>]


- |void| **set_value_label**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_value_label**\ (\ )

Label of the virtual axis of the blend space.


----


## Method Descriptions



|void| **add_blend_point**\ (\ node\: [AnimationRootNode<class_AnimationRootNode>], pos\: [float<class_float>], at_index\: [int<class_int>] = -1\ ) [🔗<class_AnimationNodeBlendSpace1D_method_add_blend_point>]

Adds a new point that represents a `node` on the virtual axis at a given position set by `pos`. You can insert it at a specific index using the `at_index` argument. If you use the default value for `at_index`, the point is inserted at the end of the blend points array.


----



[int<class_int>] **get_blend_point_count**\ (\ ) |const| [🔗<class_AnimationNodeBlendSpace1D_method_get_blend_point_count>]

Returns the number of points on the blend axis.


----



[AnimationRootNode<class_AnimationRootNode>] **get_blend_point_node**\ (\ point\: [int<class_int>]\ ) |const| [🔗<class_AnimationNodeBlendSpace1D_method_get_blend_point_node>]

Returns the [AnimationNode<class_AnimationNode>] referenced by the point at index `point`.


----



[float<class_float>] **get_blend_point_position**\ (\ point\: [int<class_int>]\ ) |const| [🔗<class_AnimationNodeBlendSpace1D_method_get_blend_point_position>]

Returns the position of the point at index `point`.


----



|void| **remove_blend_point**\ (\ point\: [int<class_int>]\ ) [🔗<class_AnimationNodeBlendSpace1D_method_remove_blend_point>]

Removes the point at index `point` from the blend axis.


----



|void| **set_blend_point_node**\ (\ point\: [int<class_int>], node\: [AnimationRootNode<class_AnimationRootNode>]\ ) [🔗<class_AnimationNodeBlendSpace1D_method_set_blend_point_node>]

Changes the [AnimationNode<class_AnimationNode>] referenced by the point at index `point`.


----



|void| **set_blend_point_position**\ (\ point\: [int<class_int>], pos\: [float<class_float>]\ ) [🔗<class_AnimationNodeBlendSpace1D_method_set_blend_point_position>]

Updates the position of the point at index `point` on the blend axis.

