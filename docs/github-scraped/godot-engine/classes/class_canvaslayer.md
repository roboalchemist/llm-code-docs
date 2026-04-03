:github_url: hide



# CanvasLayer

**Inherits:** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [ParallaxBackground<class_ParallaxBackground>]

A node used for independent rendering of objects within a 2D scene.


## Description

[CanvasItem<class_CanvasItem>]-derived nodes that are direct or indirect children of a **CanvasLayer** will be drawn in that layer. The layer is a numeric index that defines the draw order. The default 2D scene renders with index `0`, so a **CanvasLayer** with index `-1` will be drawn below, and a **CanvasLayer** with index `1` will be drawn above. This order will hold regardless of the [CanvasItem.z_index<class_CanvasItem_property_z_index>] of the nodes within each layer.

\ **CanvasLayer**\ s can be hidden and they can also optionally follow the viewport. This makes them useful for HUDs like health bar overlays (on layers `1` and higher) or backgrounds (on layers `-1` and lower).

\ **Note:** Embedded [Window<class_Window>]\ s are placed on layer `1024`. [CanvasItem<class_CanvasItem>]\ s on layers `1025` and higher appear in front of embedded windows.

\ **Note:** Each **CanvasLayer** is drawn on one specific [Viewport<class_Viewport>] and cannot be shared between multiple [Viewport<class_Viewport>]\ s, see [custom_viewport<class_CanvasLayer_property_custom_viewport>]. When using multiple [Viewport<class_Viewport>]\ s, for example in a split-screen game, you need to create an individual **CanvasLayer** for each [Viewport<class_Viewport>] you want it to be drawn on.


## Tutorials

- [../tutorials/2d/2d_transforms](Viewport and canvas transforms .md)

- [../tutorials/2d/canvas_layers](Canvas layers .md)

- [2D Dodge The Creeps Demo ](https://godotengine.org/asset-library/asset/2712)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------+------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Node<class_Node>`               | :ref:`custom_viewport<class_CanvasLayer_property_custom_viewport>`                 |                                   |
> +---------------------------------------+------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`follow_viewport_enabled<class_CanvasLayer_property_follow_viewport_enabled>` | ``false``                         |
> +---------------------------------------+------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`float<class_float>`             | :ref:`follow_viewport_scale<class_CanvasLayer_property_follow_viewport_scale>`     | ``1.0``                           |
> +---------------------------------------+------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`int<class_int>`                 | :ref:`layer<class_CanvasLayer_property_layer>`                                     | ``1``                             |
> +---------------------------------------+------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Vector2<class_Vector2>`         | :ref:`offset<class_CanvasLayer_property_offset>`                                   | ``Vector2(0, 0)``                 |
> +---------------------------------------+------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`float<class_float>`             | :ref:`rotation<class_CanvasLayer_property_rotation>`                               | ``0.0``                           |
> +---------------------------------------+------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Vector2<class_Vector2>`         | :ref:`scale<class_CanvasLayer_property_scale>`                                     | ``Vector2(1, 1)``                 |
> +---------------------------------------+------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Transform2D<class_Transform2D>` | :ref:`transform<class_CanvasLayer_property_transform>`                             | ``Transform2D(1, 0, 0, 1, 0, 0)`` |
> +---------------------------------------+------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`visible<class_CanvasLayer_property_visible>`                                 | ``true``                          |
> +---------------------------------------+------------------------------------------------------------------------------------+-----------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                 | :ref:`get_canvas<class_CanvasLayer_method_get_canvas>`\ (\ ) |const|                   |
> +---------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Transform2D<class_Transform2D>` | :ref:`get_final_transform<class_CanvasLayer_method_get_final_transform>`\ (\ ) |const| |
> +---------------------------------------+----------------------------------------------------------------------------------------+
> | |void|                                | :ref:`hide<class_CanvasLayer_method_hide>`\ (\ )                                       |
> +---------------------------------------+----------------------------------------------------------------------------------------+
> | |void|                                | :ref:`show<class_CanvasLayer_method_show>`\ (\ )                                       |
> +---------------------------------------+----------------------------------------------------------------------------------------+
>

----


## Signals



**visibility_changed**\ (\ ) [🔗<class_CanvasLayer_signal_visibility_changed>]

Emitted when visibility of the layer is changed. See [visible<class_CanvasLayer_property_visible>].


----


## Property Descriptions



[Node<class_Node>] **custom_viewport** [🔗<class_CanvasLayer_property_custom_viewport>]


- |void| **set_custom_viewport**\ (\ value\: [Node<class_Node>]\ )
- [Node<class_Node>] **get_custom_viewport**\ (\ )

The custom [Viewport<class_Viewport>] node assigned to the **CanvasLayer**. If `null`, uses the default viewport instead.


----



[bool<class_bool>] **follow_viewport_enabled** = `false` [🔗<class_CanvasLayer_property_follow_viewport_enabled>]


- |void| **set_follow_viewport**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_following_viewport**\ (\ )

If enabled, the **CanvasLayer** maintains its position in world space. If disabled, the **CanvasLayer** stays in a fixed position on the screen.

Together with [follow_viewport_scale<class_CanvasLayer_property_follow_viewport_scale>], this can be used for a pseudo-3D effect.


----



[float<class_float>] **follow_viewport_scale** = `1.0` [🔗<class_CanvasLayer_property_follow_viewport_scale>]


- |void| **set_follow_viewport_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_follow_viewport_scale**\ (\ )

Scales the layer when using [follow_viewport_enabled<class_CanvasLayer_property_follow_viewport_enabled>]. Layers moving into the foreground should have increasing scales, while layers moving into the background should have decreasing scales.


----



[int<class_int>] **layer** = `1` [🔗<class_CanvasLayer_property_layer>]


- |void| **set_layer**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_layer**\ (\ )

Layer index for draw order. Lower values are drawn behind higher values.

\ **Note:** If multiple CanvasLayers have the same layer index, [CanvasItem<class_CanvasItem>] children of one CanvasLayer are drawn behind the [CanvasItem<class_CanvasItem>] children of the other CanvasLayer. Which CanvasLayer is drawn in front is non-deterministic.

\ **Note:** The layer index should be between [RenderingServer.CANVAS_LAYER_MIN<class_RenderingServer_constant_CANVAS_LAYER_MIN>] and [RenderingServer.CANVAS_LAYER_MAX<class_RenderingServer_constant_CANVAS_LAYER_MAX>] (inclusive). Any other value will wrap around.


----



[Vector2<class_Vector2>] **offset** = `Vector2(0, 0)` [🔗<class_CanvasLayer_property_offset>]


- |void| **set_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_offset**\ (\ )

The layer's base offset.


----



[float<class_float>] **rotation** = `0.0` [🔗<class_CanvasLayer_property_rotation>]


- |void| **set_rotation**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_rotation**\ (\ )

The layer's rotation in radians.


----



[Vector2<class_Vector2>] **scale** = `Vector2(1, 1)` [🔗<class_CanvasLayer_property_scale>]


- |void| **set_scale**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_scale**\ (\ )

The layer's scale.


----



[Transform2D<class_Transform2D>] **transform** = `Transform2D(1, 0, 0, 1, 0, 0)` [🔗<class_CanvasLayer_property_transform>]


- |void| **set_transform**\ (\ value\: [Transform2D<class_Transform2D>]\ )
- [Transform2D<class_Transform2D>] **get_transform**\ (\ )

The layer's transform.


----



[bool<class_bool>] **visible** = `true` [🔗<class_CanvasLayer_property_visible>]


- |void| **set_visible**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_visible**\ (\ )

If `false`, any [CanvasItem<class_CanvasItem>] under this **CanvasLayer** will be hidden.

Unlike [CanvasItem.visible<class_CanvasItem_property_visible>], visibility of a **CanvasLayer** isn't propagated to underlying layers.


----


## Method Descriptions



[RID<class_RID>] **get_canvas**\ (\ ) |const| [🔗<class_CanvasLayer_method_get_canvas>]

Returns the RID of the canvas used by this layer.


----



[Transform2D<class_Transform2D>] **get_final_transform**\ (\ ) |const| [🔗<class_CanvasLayer_method_get_final_transform>]

Returns the transform from the **CanvasLayer**\ s coordinate system to the [Viewport<class_Viewport>]\ s coordinate system.


----



|void| **hide**\ (\ ) [🔗<class_CanvasLayer_method_hide>]

Hides any [CanvasItem<class_CanvasItem>] under this **CanvasLayer**. This is equivalent to setting [visible<class_CanvasLayer_property_visible>] to `false`.


----



|void| **show**\ (\ ) [🔗<class_CanvasLayer_method_show>]

Shows any [CanvasItem<class_CanvasItem>] under this **CanvasLayer**. This is equivalent to setting [visible<class_CanvasLayer_property_visible>] to `true`.

