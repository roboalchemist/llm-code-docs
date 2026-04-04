:github_url: hide



# ParallaxBackground

**Deprecated:** Use the [Parallax2D<class_Parallax2D>] node instead.

**Inherits:** [CanvasLayer<class_CanvasLayer>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A node used to create a parallax scrolling background.


## Description

A ParallaxBackground uses one or more [ParallaxLayer<class_ParallaxLayer>] child nodes to create a parallax effect. Each [ParallaxLayer<class_ParallaxLayer>] can move at a different speed using [ParallaxLayer.motion_offset<class_ParallaxLayer_property_motion_offset>]. This creates an illusion of depth in a 2D game. If not used with a [Camera2D<class_Camera2D>], you must manually calculate the [scroll_offset<class_ParallaxBackground_property_scroll_offset>].

\ **Note:** Each **ParallaxBackground** is drawn on one specific [Viewport<class_Viewport>] and cannot be shared between multiple [Viewport<class_Viewport>]\ s, see [CanvasLayer.custom_viewport<class_CanvasLayer_property_custom_viewport>]. When using multiple [Viewport<class_Viewport>]\ s, for example in a split-screen game, you need create an individual **ParallaxBackground** for each [Viewport<class_Viewport>] you want it to be drawn on.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | layer                                                                                         | ``-100`` (overrides :ref:`CanvasLayer<class_CanvasLayer_property_layer>`) |
> +-------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`scroll_base_offset<class_ParallaxBackground_property_scroll_base_offset>`               | ``Vector2(0, 0)``                                                         |
> +-------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`scroll_base_scale<class_ParallaxBackground_property_scroll_base_scale>`                 | ``Vector2(1, 1)``                                                         |
> +-------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`scroll_ignore_camera_zoom<class_ParallaxBackground_property_scroll_ignore_camera_zoom>` | ``false``                                                                 |
> +-------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`scroll_limit_begin<class_ParallaxBackground_property_scroll_limit_begin>`               | ``Vector2(0, 0)``                                                         |
> +-------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`scroll_limit_end<class_ParallaxBackground_property_scroll_limit_end>`                   | ``Vector2(0, 0)``                                                         |
> +-------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`scroll_offset<class_ParallaxBackground_property_scroll_offset>`                         | ``Vector2(0, 0)``                                                         |
> +-------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
>

----


## Property Descriptions



[Vector2<class_Vector2>] **scroll_base_offset** = `Vector2(0, 0)` [🔗<class_ParallaxBackground_property_scroll_base_offset>]


- |void| **set_scroll_base_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_scroll_base_offset**\ (\ )

The base position offset for all [ParallaxLayer<class_ParallaxLayer>] children.


----



[Vector2<class_Vector2>] **scroll_base_scale** = `Vector2(1, 1)` [🔗<class_ParallaxBackground_property_scroll_base_scale>]


- |void| **set_scroll_base_scale**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_scroll_base_scale**\ (\ )

The base motion scale for all [ParallaxLayer<class_ParallaxLayer>] children.


----



[bool<class_bool>] **scroll_ignore_camera_zoom** = `false` [🔗<class_ParallaxBackground_property_scroll_ignore_camera_zoom>]


- |void| **set_ignore_camera_zoom**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_ignore_camera_zoom**\ (\ )

If `true`, elements in [ParallaxLayer<class_ParallaxLayer>] child aren't affected by the zoom level of the camera.


----



[Vector2<class_Vector2>] **scroll_limit_begin** = `Vector2(0, 0)` [🔗<class_ParallaxBackground_property_scroll_limit_begin>]


- |void| **set_limit_begin**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_limit_begin**\ (\ )

Top-left limits for scrolling to begin. If the camera is outside of this limit, the background will stop scrolling. Must be lower than [scroll_limit_end<class_ParallaxBackground_property_scroll_limit_end>] to work.


----



[Vector2<class_Vector2>] **scroll_limit_end** = `Vector2(0, 0)` [🔗<class_ParallaxBackground_property_scroll_limit_end>]


- |void| **set_limit_end**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_limit_end**\ (\ )

Bottom-right limits for scrolling to end. If the camera is outside of this limit, the background will stop scrolling. Must be higher than [scroll_limit_begin<class_ParallaxBackground_property_scroll_limit_begin>] to work.


----



[Vector2<class_Vector2>] **scroll_offset** = `Vector2(0, 0)` [🔗<class_ParallaxBackground_property_scroll_offset>]


- |void| **set_scroll_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_scroll_offset**\ (\ )

The ParallaxBackground's scroll value. Calculated automatically when using a [Camera2D<class_Camera2D>], but can be used to manually manage scrolling when no camera is present.

