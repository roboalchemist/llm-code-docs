:github_url: hide



# Texture2D

**Inherits:** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [AnimatedTexture<class_AnimatedTexture>], [AtlasTexture<class_AtlasTexture>], [CameraTexture<class_CameraTexture>], [CanvasTexture<class_CanvasTexture>], [CompressedTexture2D<class_CompressedTexture2D>], [CurveTexture<class_CurveTexture>], [CurveXYZTexture<class_CurveXYZTexture>], [DPITexture<class_DPITexture>], [ExternalTexture<class_ExternalTexture>], [GradientTexture1D<class_GradientTexture1D>], [GradientTexture2D<class_GradientTexture2D>], [ImageTexture<class_ImageTexture>], [MeshTexture<class_MeshTexture>], [NoiseTexture2D<class_NoiseTexture2D>], [PlaceholderTexture2D<class_PlaceholderTexture2D>], [PortableCompressedTexture2D<class_PortableCompressedTexture2D>], [Texture2DRD<class_Texture2DRD>], [ViewportTexture<class_ViewportTexture>]

Texture for 2D and 3D.


## Description

A texture works by registering an image in the video hardware, which then can be used in 3D models or 2D [Sprite2D<class_Sprite2D>] or GUI [Control<class_Control>].

Textures are often created by loading them from a file. See [@GDScript.load()<class_@GDScript_method_load>].

\ **Texture2D** is a base for other resources. It cannot be used directly.

\ **Note:** The maximum texture size is 16384×16384 pixels due to graphics hardware limitations. Larger textures may fail to import.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`_draw<class_Texture2D_private_method__draw>`\ (\ to_canvas_item\: :ref:`RID<class_RID>`, pos\: :ref:`Vector2<class_Vector2>`, modulate\: :ref:`Color<class_Color>`, transpose\: :ref:`bool<class_bool>`\ ) |virtual| |const|                                                                                                           |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`_draw_rect<class_Texture2D_private_method__draw_rect>`\ (\ to_canvas_item\: :ref:`RID<class_RID>`, rect\: :ref:`Rect2<class_Rect2>`, tile\: :ref:`bool<class_bool>`, modulate\: :ref:`Color<class_Color>`, transpose\: :ref:`bool<class_bool>`\ ) |virtual| |const|                                                                    |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`_draw_rect_region<class_Texture2D_private_method__draw_rect_region>`\ (\ to_canvas_item\: :ref:`RID<class_RID>`, rect\: :ref:`Rect2<class_Rect2>`, src_rect\: :ref:`Rect2<class_Rect2>`, modulate\: :ref:`Color<class_Color>`, transpose\: :ref:`bool<class_bool>`, clip_uv\: :ref:`bool<class_bool>`\ ) |virtual| |const|             |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`_get_height<class_Texture2D_private_method__get_height>`\ (\ ) |virtual| |required| |const|                                                                                                                                                                                                                                            |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`_get_width<class_Texture2D_private_method__get_width>`\ (\ ) |virtual| |required| |const|                                                                                                                                                                                                                                              |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`_has_alpha<class_Texture2D_private_method__has_alpha>`\ (\ ) |virtual| |const|                                                                                                                                                                                                                                                         |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`_is_pixel_opaque<class_Texture2D_private_method__is_pixel_opaque>`\ (\ x\: :ref:`int<class_int>`, y\: :ref:`int<class_int>`\ ) |virtual| |const|                                                                                                                                                                                       |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Resource<class_Resource>` | :ref:`create_placeholder<class_Texture2D_method_create_placeholder>`\ (\ ) |const|                                                                                                                                                                                                                                                           |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`draw<class_Texture2D_method_draw>`\ (\ canvas_item\: :ref:`RID<class_RID>`, position\: :ref:`Vector2<class_Vector2>`, modulate\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1), transpose\: :ref:`bool<class_bool>` = false\ ) |const|                                                                                                 |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`draw_rect<class_Texture2D_method_draw_rect>`\ (\ canvas_item\: :ref:`RID<class_RID>`, rect\: :ref:`Rect2<class_Rect2>`, tile\: :ref:`bool<class_bool>`, modulate\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1), transpose\: :ref:`bool<class_bool>` = false\ ) |const|                                                               |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`draw_rect_region<class_Texture2D_method_draw_rect_region>`\ (\ canvas_item\: :ref:`RID<class_RID>`, rect\: :ref:`Rect2<class_Rect2>`, src_rect\: :ref:`Rect2<class_Rect2>`, modulate\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1), transpose\: :ref:`bool<class_bool>` = false, clip_uv\: :ref:`bool<class_bool>` = true\ ) |const| |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`get_height<class_Texture2D_method_get_height>`\ (\ ) |const|                                                                                                                                                                                                                                                                           |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Image<class_Image>`       | :ref:`get_image<class_Texture2D_method_get_image>`\ (\ ) |const|                                                                                                                                                                                                                                                                             |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`   | :ref:`get_size<class_Texture2D_method_get_size>`\ (\ ) |const|                                                                                                                                                                                                                                                                               |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`get_width<class_Texture2D_method_get_width>`\ (\ ) |const|                                                                                                                                                                                                                                                                             |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`has_alpha<class_Texture2D_method_has_alpha>`\ (\ ) |const|                                                                                                                                                                                                                                                                             |
> +---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **_draw**\ (\ to_canvas_item\: [RID<class_RID>], pos\: [Vector2<class_Vector2>], modulate\: [Color<class_Color>], transpose\: [bool<class_bool>]\ ) |virtual| |const| [🔗<class_Texture2D_private_method__draw>]

Called when the entire **Texture2D** is requested to be drawn over a [CanvasItem<class_CanvasItem>], with the top-left offset specified in `pos`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

\ **Note:** This is only used in 2D rendering, not 3D.


----



|void| **_draw_rect**\ (\ to_canvas_item\: [RID<class_RID>], rect\: [Rect2<class_Rect2>], tile\: [bool<class_bool>], modulate\: [Color<class_Color>], transpose\: [bool<class_bool>]\ ) |virtual| |const| [🔗<class_Texture2D_private_method__draw_rect>]

Called when the **Texture2D** is requested to be drawn onto [CanvasItem<class_CanvasItem>]'s specified `rect`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

\ **Note:** This is only used in 2D rendering, not 3D.


----



|void| **_draw_rect_region**\ (\ to_canvas_item\: [RID<class_RID>], rect\: [Rect2<class_Rect2>], src_rect\: [Rect2<class_Rect2>], modulate\: [Color<class_Color>], transpose\: [bool<class_bool>], clip_uv\: [bool<class_bool>]\ ) |virtual| |const| [🔗<class_Texture2D_private_method__draw_rect_region>]

Called when a part of the **Texture2D** specified by `src_rect`'s coordinates is requested to be drawn onto [CanvasItem<class_CanvasItem>]'s specified `rect`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

\ **Note:** This is only used in 2D rendering, not 3D.


----



[int<class_int>] **_get_height**\ (\ ) |virtual| |required| |const| [🔗<class_Texture2D_private_method__get_height>]

Called when the **Texture2D**'s height is queried.


----



[int<class_int>] **_get_width**\ (\ ) |virtual| |required| |const| [🔗<class_Texture2D_private_method__get_width>]

Called when the **Texture2D**'s width is queried.


----



[bool<class_bool>] **_has_alpha**\ (\ ) |virtual| |const| [🔗<class_Texture2D_private_method__has_alpha>]

Called when the presence of an alpha channel in the **Texture2D** is queried.


----



[bool<class_bool>] **_is_pixel_opaque**\ (\ x\: [int<class_int>], y\: [int<class_int>]\ ) |virtual| |const| [🔗<class_Texture2D_private_method__is_pixel_opaque>]

Called when a pixel's opaque state in the **Texture2D** is queried at the specified `(x, y)` position.


----



[Resource<class_Resource>] **create_placeholder**\ (\ ) |const| [🔗<class_Texture2D_method_create_placeholder>]

Creates a placeholder version of this resource ([PlaceholderTexture2D<class_PlaceholderTexture2D>]).


----



|void| **draw**\ (\ canvas_item\: [RID<class_RID>], position\: [Vector2<class_Vector2>], modulate\: [Color<class_Color>] = Color(1, 1, 1, 1), transpose\: [bool<class_bool>] = false\ ) |const| [🔗<class_Texture2D_method_draw>]

Draws the texture using a [CanvasItem<class_CanvasItem>] with the [RenderingServer<class_RenderingServer>] API at the specified `position`.


----



|void| **draw_rect**\ (\ canvas_item\: [RID<class_RID>], rect\: [Rect2<class_Rect2>], tile\: [bool<class_bool>], modulate\: [Color<class_Color>] = Color(1, 1, 1, 1), transpose\: [bool<class_bool>] = false\ ) |const| [🔗<class_Texture2D_method_draw_rect>]

Draws the texture using a [CanvasItem<class_CanvasItem>] with the [RenderingServer<class_RenderingServer>] API.


----



|void| **draw_rect_region**\ (\ canvas_item\: [RID<class_RID>], rect\: [Rect2<class_Rect2>], src_rect\: [Rect2<class_Rect2>], modulate\: [Color<class_Color>] = Color(1, 1, 1, 1), transpose\: [bool<class_bool>] = false, clip_uv\: [bool<class_bool>] = true\ ) |const| [🔗<class_Texture2D_method_draw_rect_region>]

Draws a part of the texture using a [CanvasItem<class_CanvasItem>] with the [RenderingServer<class_RenderingServer>] API.


----



[int<class_int>] **get_height**\ (\ ) |const| [🔗<class_Texture2D_method_get_height>]

Returns the texture height in pixels.


----



[Image<class_Image>] **get_image**\ (\ ) |const| [🔗<class_Texture2D_method_get_image>]

Returns an [Image<class_Image>] that is a copy of data from this **Texture2D** (a new [Image<class_Image>] is created each time). [Image<class_Image>]\ s can be accessed and manipulated directly.

\ **Note:** This will return `null` if this **Texture2D** is invalid.

\ **Note:** This will fetch the texture data from the GPU, which might cause performance problems when overused. Avoid calling [get_image()<class_Texture2D_method_get_image>] every frame, especially on large textures.


----



[Vector2<class_Vector2>] **get_size**\ (\ ) |const| [🔗<class_Texture2D_method_get_size>]

Returns the texture size in pixels.


----



[int<class_int>] **get_width**\ (\ ) |const| [🔗<class_Texture2D_method_get_width>]

Returns the texture width in pixels.


----



[bool<class_bool>] **has_alpha**\ (\ ) |const| [🔗<class_Texture2D_method_has_alpha>]

Returns `true` if this **Texture2D** has an alpha channel.

