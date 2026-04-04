:github_url: hide



# Sprite3D

**Inherits:** [SpriteBase3D<class_SpriteBase3D>] **<** [GeometryInstance3D<class_GeometryInstance3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

2D sprite node in a 3D world.


## Description

A node that displays a 2D texture in a 3D environment. The texture displayed can be a region from a larger atlas texture, or a frame from a sprite sheet animation. See also [SpriteBase3D<class_SpriteBase3D>] where properties such as the billboard mode are defined.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`             | :ref:`frame<class_Sprite3D_property_frame>`                   | ``0``                 |
> +-----------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`Vector2i<class_Vector2i>`   | :ref:`frame_coords<class_Sprite3D_property_frame_coords>`     | ``Vector2i(0, 0)``    |
> +-----------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`             | :ref:`hframes<class_Sprite3D_property_hframes>`               | ``1``                 |
> +-----------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`           | :ref:`region_enabled<class_Sprite3D_property_region_enabled>` | ``false``             |
> +-----------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`Rect2<class_Rect2>`         | :ref:`region_rect<class_Sprite3D_property_region_rect>`       | ``Rect2(0, 0, 0, 0)`` |
> +-----------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`texture<class_Sprite3D_property_texture>`               |                       |
> +-----------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`             | :ref:`vframes<class_Sprite3D_property_vframes>`               | ``1``                 |
> +-----------------------------------+---------------------------------------------------------------+-----------------------+
>

----


## Signals



**frame_changed**\ (\ ) [🔗<class_Sprite3D_signal_frame_changed>]

Emitted when the [frame<class_Sprite3D_property_frame>] changes.


----



**texture_changed**\ (\ ) [🔗<class_Sprite3D_signal_texture_changed>]

Emitted when the [texture<class_Sprite3D_property_texture>] changes.


----


## Property Descriptions



[int<class_int>] **frame** = `0` [🔗<class_Sprite3D_property_frame>]


- |void| **set_frame**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_frame**\ (\ )

Current frame to display from sprite sheet. [hframes<class_Sprite3D_property_hframes>] or [vframes<class_Sprite3D_property_vframes>] must be greater than 1. This property is automatically adjusted when [hframes<class_Sprite3D_property_hframes>] or [vframes<class_Sprite3D_property_vframes>] are changed to keep pointing to the same visual frame (same column and row). If that's impossible, this value is reset to `0`.


----



[Vector2i<class_Vector2i>] **frame_coords** = `Vector2i(0, 0)` [🔗<class_Sprite3D_property_frame_coords>]


- |void| **set_frame_coords**\ (\ value\: [Vector2i<class_Vector2i>]\ )
- [Vector2i<class_Vector2i>] **get_frame_coords**\ (\ )

Coordinates of the frame to display from sprite sheet. This is as an alias for the [frame<class_Sprite3D_property_frame>] property. [hframes<class_Sprite3D_property_hframes>] or [vframes<class_Sprite3D_property_vframes>] must be greater than 1.


----



[int<class_int>] **hframes** = `1` [🔗<class_Sprite3D_property_hframes>]


- |void| **set_hframes**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_hframes**\ (\ )

The number of columns in the sprite sheet. When this property is changed, [frame<class_Sprite3D_property_frame>] is adjusted so that the same visual frame is maintained (same row and column). If that's impossible, [frame<class_Sprite3D_property_frame>] is reset to `0`.


----



[bool<class_bool>] **region_enabled** = `false` [🔗<class_Sprite3D_property_region_enabled>]


- |void| **set_region_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_region_enabled**\ (\ )

If `true`, the sprite will use [region_rect<class_Sprite3D_property_region_rect>] and display only the specified part of its texture.


----



[Rect2<class_Rect2>] **region_rect** = `Rect2(0, 0, 0, 0)` [🔗<class_Sprite3D_property_region_rect>]


- |void| **set_region_rect**\ (\ value\: [Rect2<class_Rect2>]\ )
- [Rect2<class_Rect2>] **get_region_rect**\ (\ )

The region of the atlas texture to display. [region_enabled<class_Sprite3D_property_region_enabled>] must be `true`.


----



[Texture2D<class_Texture2D>] **texture** [🔗<class_Sprite3D_property_texture>]


- |void| **set_texture**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture**\ (\ )

[Texture2D<class_Texture2D>] object to draw. If [GeometryInstance3D.material_override<class_GeometryInstance3D_property_material_override>] is used, this will be overridden. The size information is still used.


----



[int<class_int>] **vframes** = `1` [🔗<class_Sprite3D_property_vframes>]


- |void| **set_vframes**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_vframes**\ (\ )

The number of rows in the sprite sheet. When this property is changed, [frame<class_Sprite3D_property_frame>] is adjusted so that the same visual frame is maintained (same row and column). If that's impossible, [frame<class_Sprite3D_property_frame>] is reset to `0`.

