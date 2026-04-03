:github_url: hide



# Sprite2D

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

General-purpose sprite node.


## Description

A node that displays a 2D texture. The texture displayed can be a region from a larger atlas texture, or a frame from a sprite sheet animation.


## Tutorials

- [Instancing Demo ](https://godotengine.org/asset-library/asset/2716)_


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`           | :ref:`centered<class_Sprite2D_property_centered>`                                     | ``true``              |
> +-----------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`           | :ref:`flip_h<class_Sprite2D_property_flip_h>`                                         | ``false``             |
> +-----------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`           | :ref:`flip_v<class_Sprite2D_property_flip_v>`                                         | ``false``             |
> +-----------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`             | :ref:`frame<class_Sprite2D_property_frame>`                                           | ``0``                 |
> +-----------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Vector2i<class_Vector2i>`   | :ref:`frame_coords<class_Sprite2D_property_frame_coords>`                             | ``Vector2i(0, 0)``    |
> +-----------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`             | :ref:`hframes<class_Sprite2D_property_hframes>`                                       | ``1``                 |
> +-----------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Vector2<class_Vector2>`     | :ref:`offset<class_Sprite2D_property_offset>`                                         | ``Vector2(0, 0)``     |
> +-----------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`           | :ref:`region_enabled<class_Sprite2D_property_region_enabled>`                         | ``false``             |
> +-----------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`           | :ref:`region_filter_clip_enabled<class_Sprite2D_property_region_filter_clip_enabled>` | ``false``             |
> +-----------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Rect2<class_Rect2>`         | :ref:`region_rect<class_Sprite2D_property_region_rect>`                               | ``Rect2(0, 0, 0, 0)`` |
> +-----------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`texture<class_Sprite2D_property_texture>`                                       |                       |
> +-----------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`             | :ref:`vframes<class_Sprite2D_property_vframes>`                                       | ``1``                 |
> +-----------------------------------+---------------------------------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>` | :ref:`get_rect<class_Sprite2D_method_get_rect>`\ (\ ) |const|                                                    |
> +---------------------------+------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`is_pixel_opaque<class_Sprite2D_method_is_pixel_opaque>`\ (\ pos\: :ref:`Vector2<class_Vector2>`\ ) |const| |
> +---------------------------+------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**frame_changed**\ (\ ) [🔗<class_Sprite2D_signal_frame_changed>]

Emitted when the [frame<class_Sprite2D_property_frame>] changes.


----



**texture_changed**\ (\ ) [🔗<class_Sprite2D_signal_texture_changed>]

Emitted when the [texture<class_Sprite2D_property_texture>] changes.


----


## Property Descriptions



[bool<class_bool>] **centered** = `true` [🔗<class_Sprite2D_property_centered>]


- |void| **set_centered**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_centered**\ (\ )

If `true`, texture is centered.

\ **Note:** For games with a pixel art aesthetic, textures may appear deformed when centered. This is caused by their position being between pixels. To prevent this, set this property to `false`, or consider enabling [ProjectSettings.rendering/2d/snap/snap_2d_vertices_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_vertices_to_pixel>] and [ProjectSettings.rendering/2d/snap/snap_2d_transforms_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_transforms_to_pixel>].


----



[bool<class_bool>] **flip_h** = `false` [🔗<class_Sprite2D_property_flip_h>]


- |void| **set_flip_h**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_flipped_h**\ (\ )

If `true`, texture is flipped horizontally.


----



[bool<class_bool>] **flip_v** = `false` [🔗<class_Sprite2D_property_flip_v>]


- |void| **set_flip_v**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_flipped_v**\ (\ )

If `true`, texture is flipped vertically.


----



[int<class_int>] **frame** = `0` [🔗<class_Sprite2D_property_frame>]


- |void| **set_frame**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_frame**\ (\ )

Current frame to display from sprite sheet. [hframes<class_Sprite2D_property_hframes>] or [vframes<class_Sprite2D_property_vframes>] must be greater than 1. This property is automatically adjusted when [hframes<class_Sprite2D_property_hframes>] or [vframes<class_Sprite2D_property_vframes>] are changed to keep pointing to the same visual frame (same column and row). If that's impossible, this value is reset to `0`.


----



[Vector2i<class_Vector2i>] **frame_coords** = `Vector2i(0, 0)` [🔗<class_Sprite2D_property_frame_coords>]


- |void| **set_frame_coords**\ (\ value\: [Vector2i<class_Vector2i>]\ )
- [Vector2i<class_Vector2i>] **get_frame_coords**\ (\ )

Coordinates of the frame to display from sprite sheet. This is as an alias for the [frame<class_Sprite2D_property_frame>] property. [hframes<class_Sprite2D_property_hframes>] or [vframes<class_Sprite2D_property_vframes>] must be greater than 1.


----



[int<class_int>] **hframes** = `1` [🔗<class_Sprite2D_property_hframes>]


- |void| **set_hframes**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_hframes**\ (\ )

The number of columns in the sprite sheet. When this property is changed, [frame<class_Sprite2D_property_frame>] is adjusted so that the same visual frame is maintained (same row and column). If that's impossible, [frame<class_Sprite2D_property_frame>] is reset to `0`.


----



[Vector2<class_Vector2>] **offset** = `Vector2(0, 0)` [🔗<class_Sprite2D_property_offset>]


- |void| **set_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_offset**\ (\ )

The texture's drawing offset.

\ **Note:** When you increase [offset<class_Sprite2D_property_offset>].y in Sprite2D, the sprite moves downward on screen (i.e., +Y is down).


----



[bool<class_bool>] **region_enabled** = `false` [🔗<class_Sprite2D_property_region_enabled>]


- |void| **set_region_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_region_enabled**\ (\ )

If `true`, texture is cut from a larger atlas texture. See [region_rect<class_Sprite2D_property_region_rect>].

\ **Note:** When using a custom [Shader<class_Shader>] on a **Sprite2D**, the `UV` shader built-in will refer to the entire texture space. Use the `REGION_RECT` built-in to get the currently visible region defined in [region_rect<class_Sprite2D_property_region_rect>] instead. See [../tutorials/shaders/shader_reference/canvas_item_shader](CanvasItem shaders .md) for details.


----



[bool<class_bool>] **region_filter_clip_enabled** = `false` [🔗<class_Sprite2D_property_region_filter_clip_enabled>]


- |void| **set_region_filter_clip_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_region_filter_clip_enabled**\ (\ )

If `true`, the area outside of the [region_rect<class_Sprite2D_property_region_rect>] is clipped to avoid bleeding of the surrounding texture pixels. [region_enabled<class_Sprite2D_property_region_enabled>] must be `true`.


----



[Rect2<class_Rect2>] **region_rect** = `Rect2(0, 0, 0, 0)` [🔗<class_Sprite2D_property_region_rect>]


- |void| **set_region_rect**\ (\ value\: [Rect2<class_Rect2>]\ )
- [Rect2<class_Rect2>] **get_region_rect**\ (\ )

The region of the atlas texture to display. [region_enabled<class_Sprite2D_property_region_enabled>] must be `true`.


----



[Texture2D<class_Texture2D>] **texture** [🔗<class_Sprite2D_property_texture>]


- |void| **set_texture**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture**\ (\ )

[Texture2D<class_Texture2D>] object to draw.


----



[int<class_int>] **vframes** = `1` [🔗<class_Sprite2D_property_vframes>]


- |void| **set_vframes**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_vframes**\ (\ )

The number of rows in the sprite sheet. When this property is changed, [frame<class_Sprite2D_property_frame>] is adjusted so that the same visual frame is maintained (same row and column). If that's impossible, [frame<class_Sprite2D_property_frame>] is reset to `0`.


----


## Method Descriptions



[Rect2<class_Rect2>] **get_rect**\ (\ ) |const| [🔗<class_Sprite2D_method_get_rect>]

Returns a [Rect2<class_Rect2>] representing the Sprite2D's boundary in local coordinates.

\ **Example:** Detect if the Sprite2D was clicked:


> **TABS**
>

    func _input(event):
        if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
            if get_rect().has_point(to_local(event.position)):
                print("A click!")


    public override void _Input(InputEvent @event)
    {
        if (@event is InputEventMouseButton inputEventMouse)
        {
            if (inputEventMouse.Pressed && inputEventMouse.ButtonIndex == MouseButton.Left)
            {
                if (GetRect().HasPoint(ToLocal(inputEventMouse.Position)))
                {
                    GD.Print("A click!");
## }
## }




----



[bool<class_bool>] **is_pixel_opaque**\ (\ pos\: [Vector2<class_Vector2>]\ ) |const| [🔗<class_Sprite2D_method_is_pixel_opaque>]

Returns `true` if the pixel at the given position is opaque, `false` otherwise. Also returns `false` if the given position is out of bounds or this sprite's [texture<class_Sprite2D_property_texture>] is `null`. `pos` is in local coordinates.

