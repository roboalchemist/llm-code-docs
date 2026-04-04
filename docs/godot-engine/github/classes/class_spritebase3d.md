:github_url: hide



# SpriteBase3D

**Inherits:** [GeometryInstance3D<class_GeometryInstance3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [AnimatedSprite3D<class_AnimatedSprite3D>], [Sprite3D<class_Sprite3D>]

2D sprite node in 3D environment.


## Description

A node that displays 2D texture information in a 3D environment. See also [Sprite3D<class_Sprite3D>] where many other properties are defined.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                       | :ref:`alpha_antialiasing_edge<class_SpriteBase3D_property_alpha_antialiasing_edge>` | ``0.0``               |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>` | :ref:`alpha_antialiasing_mode<class_SpriteBase3D_property_alpha_antialiasing_mode>` | ``0``                 |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>`             | :ref:`alpha_cut<class_SpriteBase3D_property_alpha_cut>`                             | ``0``                 |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                       | :ref:`alpha_hash_scale<class_SpriteBase3D_property_alpha_hash_scale>`               | ``1.0``               |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                       | :ref:`alpha_scissor_threshold<class_SpriteBase3D_property_alpha_scissor_threshold>` | ``0.5``               |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Axis<enum_Vector3_Axis>`                                  | :ref:`axis<class_SpriteBase3D_property_axis>`                                       | ``2``                 |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`BillboardMode<enum_BaseMaterial3D_BillboardMode>`         | :ref:`billboard<class_SpriteBase3D_property_billboard>`                             | ``0``                 |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`centered<class_SpriteBase3D_property_centered>`                               | ``true``              |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`double_sided<class_SpriteBase3D_property_double_sided>`                       | ``true``              |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`fixed_size<class_SpriteBase3D_property_fixed_size>`                           | ``false``             |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`flip_h<class_SpriteBase3D_property_flip_h>`                                   | ``false``             |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`flip_v<class_SpriteBase3D_property_flip_v>`                                   | ``false``             |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`                                       | :ref:`modulate<class_SpriteBase3D_property_modulate>`                               | ``Color(1, 1, 1, 1)`` |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`no_depth_test<class_SpriteBase3D_property_no_depth_test>`                     | ``false``             |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Vector2<class_Vector2>`                                   | :ref:`offset<class_SpriteBase3D_property_offset>`                                   | ``Vector2(0, 0)``     |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                       | :ref:`pixel_size<class_SpriteBase3D_property_pixel_size>`                           | ``0.01``              |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                                           | :ref:`render_priority<class_SpriteBase3D_property_render_priority>`                 | ``0``                 |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`shaded<class_SpriteBase3D_property_shaded>`                                   | ``false``             |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`TextureFilter<enum_BaseMaterial3D_TextureFilter>`         | :ref:`texture_filter<class_SpriteBase3D_property_texture_filter>`                   | ``3``                 |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                         | :ref:`transparent<class_SpriteBase3D_property_transparent>`                         | ``true``              |
> +-----------------------------------------------------------------+-------------------------------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TriangleMesh<class_TriangleMesh>` | :ref:`generate_triangle_mesh<class_SpriteBase3D_method_generate_triangle_mesh>`\ (\ ) |const|                                                                |
> +-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                 | :ref:`get_draw_flag<class_SpriteBase3D_method_get_draw_flag>`\ (\ flag\: :ref:`DrawFlags<enum_SpriteBase3D_DrawFlags>`\ ) |const|                            |
> +-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`               | :ref:`get_item_rect<class_SpriteBase3D_method_get_item_rect>`\ (\ ) |const|                                                                                  |
> +-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                  | :ref:`set_draw_flag<class_SpriteBase3D_method_set_draw_flag>`\ (\ flag\: :ref:`DrawFlags<enum_SpriteBase3D_DrawFlags>`, enabled\: :ref:`bool<class_bool>`\ ) |
> +-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **DrawFlags**: [🔗<enum_SpriteBase3D_DrawFlags>]



[DrawFlags<enum_SpriteBase3D_DrawFlags>] **FLAG_TRANSPARENT** = `0`

If set, the texture's transparency and the opacity are used to make those parts of the sprite invisible.



[DrawFlags<enum_SpriteBase3D_DrawFlags>] **FLAG_SHADED** = `1`

If set, lights in the environment affect the sprite.



[DrawFlags<enum_SpriteBase3D_DrawFlags>] **FLAG_DOUBLE_SIDED** = `2`

If set, texture can be seen from the back as well. If not, the texture is invisible when looking at it from behind.



[DrawFlags<enum_SpriteBase3D_DrawFlags>] **FLAG_DISABLE_DEPTH_TEST** = `3`

Disables the depth test, so this object is drawn on top of all others. However, objects drawn after it in the draw order may cover it.



[DrawFlags<enum_SpriteBase3D_DrawFlags>] **FLAG_FIXED_SIZE** = `4`

Label is scaled by depth so that it always appears the same size on screen.



[DrawFlags<enum_SpriteBase3D_DrawFlags>] **FLAG_MAX** = `5`

Represents the size of the [DrawFlags<enum_SpriteBase3D_DrawFlags>] enum.


----



enum **AlphaCutMode**: [🔗<enum_SpriteBase3D_AlphaCutMode>]



[AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>] **ALPHA_CUT_DISABLED** = `0`

This mode performs standard alpha blending. It can display translucent areas, but transparency sorting issues may be visible when multiple transparent materials are overlapping.



[AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>] **ALPHA_CUT_DISCARD** = `1`

This mode only allows fully transparent or fully opaque pixels. Harsh edges will be visible unless some form of screen-space antialiasing is enabled (see [ProjectSettings.rendering/anti_aliasing/quality/screen_space_aa<class_ProjectSettings_property_rendering/anti_aliasing/quality/screen_space_aa>]). On the bright side, this mode doesn't suffer from transparency sorting issues when multiple transparent materials are overlapping. This mode is also known as *alpha testing* or *1-bit transparency*.



[AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>] **ALPHA_CUT_OPAQUE_PREPASS** = `2`

This mode draws fully opaque pixels in the depth prepass. This is slower than [ALPHA_CUT_DISABLED<class_SpriteBase3D_constant_ALPHA_CUT_DISABLED>] or [ALPHA_CUT_DISCARD<class_SpriteBase3D_constant_ALPHA_CUT_DISCARD>], but it allows displaying translucent areas and smooth edges while using proper sorting.



[AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>] **ALPHA_CUT_HASH** = `3`

This mode draws cuts off all values below a spatially-deterministic threshold, the rest will remain opaque.


----


## Property Descriptions



[float<class_float>] **alpha_antialiasing_edge** = `0.0` [🔗<class_SpriteBase3D_property_alpha_antialiasing_edge>]


- |void| **set_alpha_antialiasing_edge**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_alpha_antialiasing_edge**\ (\ )

Threshold at which antialiasing will be applied on the alpha channel.


----



[AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>] **alpha_antialiasing_mode** = `0` [🔗<class_SpriteBase3D_property_alpha_antialiasing_mode>]


- |void| **set_alpha_antialiasing**\ (\ value\: [AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>]\ )
- [AlphaAntiAliasing<enum_BaseMaterial3D_AlphaAntiAliasing>] **get_alpha_antialiasing**\ (\ )

The type of alpha antialiasing to apply.


----



[AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>] **alpha_cut** = `0` [🔗<class_SpriteBase3D_property_alpha_cut>]


- |void| **set_alpha_cut_mode**\ (\ value\: [AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>]\ )
- [AlphaCutMode<enum_SpriteBase3D_AlphaCutMode>] **get_alpha_cut_mode**\ (\ )

The alpha cutting mode to use for the sprite.


----



[float<class_float>] **alpha_hash_scale** = `1.0` [🔗<class_SpriteBase3D_property_alpha_hash_scale>]


- |void| **set_alpha_hash_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_alpha_hash_scale**\ (\ )

The hashing scale for Alpha Hash. Recommended values between `0` and `2`.


----



[float<class_float>] **alpha_scissor_threshold** = `0.5` [🔗<class_SpriteBase3D_property_alpha_scissor_threshold>]


- |void| **set_alpha_scissor_threshold**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_alpha_scissor_threshold**\ (\ )

Threshold at which the alpha scissor will discard values.


----



[Axis<enum_Vector3_Axis>] **axis** = `2` [🔗<class_SpriteBase3D_property_axis>]


- |void| **set_axis**\ (\ value\: [Axis<enum_Vector3_Axis>]\ )
- [Axis<enum_Vector3_Axis>] **get_axis**\ (\ )

The direction in which the front of the texture faces.


----



[BillboardMode<enum_BaseMaterial3D_BillboardMode>] **billboard** = `0` [🔗<class_SpriteBase3D_property_billboard>]


- |void| **set_billboard_mode**\ (\ value\: [BillboardMode<enum_BaseMaterial3D_BillboardMode>]\ )
- [BillboardMode<enum_BaseMaterial3D_BillboardMode>] **get_billboard_mode**\ (\ )

The billboard mode to use for the sprite.

\ **Note:** When billboarding is enabled and the material also casts shadows, billboards will face **the** camera in the scene when rendering shadows. In scenes with multiple cameras, the intended shadow cannot be determined and this will result in undefined behavior. See [GitHub Pull Request #72638 ](https://github.com/godotengine/godot/pull/72638)_ for details.


----



[bool<class_bool>] **centered** = `true` [🔗<class_SpriteBase3D_property_centered>]


- |void| **set_centered**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_centered**\ (\ )

If `true`, texture will be centered.


----



[bool<class_bool>] **double_sided** = `true` [🔗<class_SpriteBase3D_property_double_sided>]


- |void| **set_draw_flag**\ (\ flag\: [DrawFlags<enum_SpriteBase3D_DrawFlags>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_draw_flag**\ (\ flag\: [DrawFlags<enum_SpriteBase3D_DrawFlags>]\ ) |const|

If `true`, texture can be seen from the back as well, if `false`, it is invisible when looking at it from behind.


----



[bool<class_bool>] **fixed_size** = `false` [🔗<class_SpriteBase3D_property_fixed_size>]


- |void| **set_draw_flag**\ (\ flag\: [DrawFlags<enum_SpriteBase3D_DrawFlags>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_draw_flag**\ (\ flag\: [DrawFlags<enum_SpriteBase3D_DrawFlags>]\ ) |const|

If `true`, the texture is rendered at the same size regardless of distance. The texture's size on screen is the same as if the camera was `1.0` units away from the texture's origin, regardless of the actual distance from the camera. The [Camera3D<class_Camera3D>]'s field of view (or [Camera3D.size<class_Camera3D_property_size>] when in orthogonal/frustum mode) still affects the size the sprite is drawn at.


----



[bool<class_bool>] **flip_h** = `false` [🔗<class_SpriteBase3D_property_flip_h>]


- |void| **set_flip_h**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_flipped_h**\ (\ )

If `true`, texture is flipped horizontally.


----



[bool<class_bool>] **flip_v** = `false` [🔗<class_SpriteBase3D_property_flip_v>]


- |void| **set_flip_v**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_flipped_v**\ (\ )

If `true`, texture is flipped vertically.


----



[Color<class_Color>] **modulate** = `Color(1, 1, 1, 1)` [🔗<class_SpriteBase3D_property_modulate>]


- |void| **set_modulate**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_modulate**\ (\ )

A color value used to *multiply* the texture's colors. Can be used for mood-coloring or to simulate the color of ambient light.

\ **Note:** Unlike [CanvasItem.modulate<class_CanvasItem_property_modulate>] for 2D, colors with values above `1.0` (overbright) are not supported.

\ **Note:** If a [GeometryInstance3D.material_override<class_GeometryInstance3D_property_material_override>] is defined on the **SpriteBase3D**, the material override must be configured to take vertex colors into account for albedo. Otherwise, the color defined in [modulate<class_SpriteBase3D_property_modulate>] will be ignored. For a [BaseMaterial3D<class_BaseMaterial3D>], [BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>] must be `true`. For a [ShaderMaterial<class_ShaderMaterial>], `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function.


----



[bool<class_bool>] **no_depth_test** = `false` [🔗<class_SpriteBase3D_property_no_depth_test>]


- |void| **set_draw_flag**\ (\ flag\: [DrawFlags<enum_SpriteBase3D_DrawFlags>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_draw_flag**\ (\ flag\: [DrawFlags<enum_SpriteBase3D_DrawFlags>]\ ) |const|

If `true`, depth testing is disabled and the object will be drawn in render order.


----



[Vector2<class_Vector2>] **offset** = `Vector2(0, 0)` [🔗<class_SpriteBase3D_property_offset>]


- |void| **set_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_offset**\ (\ )

The texture's drawing offset.

\ **Note:** When you increase [offset<class_SpriteBase3D_property_offset>].y in Sprite3D, the sprite moves upward in world space (i.e., +Y is up).


----



[float<class_float>] **pixel_size** = `0.01` [🔗<class_SpriteBase3D_property_pixel_size>]


- |void| **set_pixel_size**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_pixel_size**\ (\ )

The size of one pixel's width on the sprite to scale it in 3D.


----



[int<class_int>] **render_priority** = `0` [🔗<class_SpriteBase3D_property_render_priority>]


- |void| **set_render_priority**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_render_priority**\ (\ )

Sets the render priority for the sprite. Higher priority objects will be sorted in front of lower priority objects.

\ **Note:** This only applies if [alpha_cut<class_SpriteBase3D_property_alpha_cut>] is set to [ALPHA_CUT_DISABLED<class_SpriteBase3D_constant_ALPHA_CUT_DISABLED>] (default value).

\ **Note:** This only applies to sorting of transparent objects. This will not impact how transparent objects are sorted relative to opaque objects. This is because opaque objects are not sorted, while transparent objects are sorted from back to front (subject to priority).


----



[bool<class_bool>] **shaded** = `false` [🔗<class_SpriteBase3D_property_shaded>]


- |void| **set_draw_flag**\ (\ flag\: [DrawFlags<enum_SpriteBase3D_DrawFlags>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_draw_flag**\ (\ flag\: [DrawFlags<enum_SpriteBase3D_DrawFlags>]\ ) |const|

If `true`, the [Light3D<class_Light3D>] in the [Environment<class_Environment>] has effects on the sprite.


----



[TextureFilter<enum_BaseMaterial3D_TextureFilter>] **texture_filter** = `3` [🔗<class_SpriteBase3D_property_texture_filter>]


- |void| **set_texture_filter**\ (\ value\: [TextureFilter<enum_BaseMaterial3D_TextureFilter>]\ )
- [TextureFilter<enum_BaseMaterial3D_TextureFilter>] **get_texture_filter**\ (\ )

Filter flags for the texture.

\ **Note:** Linear filtering may cause artifacts around the edges, which are especially noticeable on opaque textures. To prevent this, use textures with transparent or identical colors around the edges.


----



[bool<class_bool>] **transparent** = `true` [🔗<class_SpriteBase3D_property_transparent>]


- |void| **set_draw_flag**\ (\ flag\: [DrawFlags<enum_SpriteBase3D_DrawFlags>], enabled\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_draw_flag**\ (\ flag\: [DrawFlags<enum_SpriteBase3D_DrawFlags>]\ ) |const|

If `true`, the texture's transparency and the opacity are used to make those parts of the sprite invisible.


----


## Method Descriptions



[TriangleMesh<class_TriangleMesh>] **generate_triangle_mesh**\ (\ ) |const| [🔗<class_SpriteBase3D_method_generate_triangle_mesh>]

Returns a [TriangleMesh<class_TriangleMesh>] with the sprite's vertices following its current configuration (such as its [axis<class_SpriteBase3D_property_axis>] and [pixel_size<class_SpriteBase3D_property_pixel_size>]).


----



[bool<class_bool>] **get_draw_flag**\ (\ flag\: [DrawFlags<enum_SpriteBase3D_DrawFlags>]\ ) |const| [🔗<class_SpriteBase3D_method_get_draw_flag>]

Returns the value of the specified flag.


----



[Rect2<class_Rect2>] **get_item_rect**\ (\ ) |const| [🔗<class_SpriteBase3D_method_get_item_rect>]

Returns the rectangle representing this sprite.


----



|void| **set_draw_flag**\ (\ flag\: [DrawFlags<enum_SpriteBase3D_DrawFlags>], enabled\: [bool<class_bool>]\ ) [🔗<class_SpriteBase3D_method_set_draw_flag>]

If `true`, the specified flag will be enabled.

