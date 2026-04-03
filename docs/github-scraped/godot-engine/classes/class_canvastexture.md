:github_url: hide



# CanvasTexture

**Inherits:** [Texture2D<class_Texture2D>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Texture with optional normal and specular maps for use in 2D rendering.


## Description

**CanvasTexture** is an alternative to [ImageTexture<class_ImageTexture>] for 2D rendering. It allows using normal maps and specular maps in any node that inherits from [CanvasItem<class_CanvasItem>]. **CanvasTexture** also allows overriding the texture's filter and repeat mode independently of the node's properties (or the project settings).

\ **Note:** **CanvasTexture** cannot be used in 3D. It will not display correctly when applied to any [VisualInstance3D<class_VisualInstance3D>], such as [Sprite3D<class_Sprite3D>] or [Decal<class_Decal>]. For physically-based materials in 3D, use [BaseMaterial3D<class_BaseMaterial3D>] instead.


## Tutorials

- [../tutorials/2d/2d_lights_and_shadows](2D Lights and Shadows .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>`                   | :ref:`diffuse_texture<class_CanvasTexture_property_diffuse_texture>`       |                                                                                        |
> +-----------------------------------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>`                   | :ref:`normal_texture<class_CanvasTexture_property_normal_texture>`         |                                                                                        |
> +-----------------------------------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | resource_local_to_scene                                                    | ``false`` (overrides :ref:`Resource<class_Resource_property_resource_local_to_scene>`) |
> +-----------------------------------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>`                           | :ref:`specular_color<class_CanvasTexture_property_specular_color>`         | ``Color(1, 1, 1, 1)``                                                                  |
> +-----------------------------------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                           | :ref:`specular_shininess<class_CanvasTexture_property_specular_shininess>` | ``1.0``                                                                                |
> +-----------------------------------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>`                   | :ref:`specular_texture<class_CanvasTexture_property_specular_texture>`     |                                                                                        |
> +-----------------------------------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`TextureFilter<enum_CanvasItem_TextureFilter>` | :ref:`texture_filter<class_CanvasTexture_property_texture_filter>`         | ``0``                                                                                  |
> +-----------------------------------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`TextureRepeat<enum_CanvasItem_TextureRepeat>` | :ref:`texture_repeat<class_CanvasTexture_property_texture_repeat>`         | ``0``                                                                                  |
> +-----------------------------------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Texture2D<class_Texture2D>] **diffuse_texture** [🔗<class_CanvasTexture_property_diffuse_texture>]


- |void| **set_diffuse_texture**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_diffuse_texture**\ (\ )

The diffuse (color) texture to use. This is the main texture you want to set in most cases.


----



[Texture2D<class_Texture2D>] **normal_texture** [🔗<class_CanvasTexture_property_normal_texture>]


- |void| **set_normal_texture**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_normal_texture**\ (\ )

The normal map texture to use. Only has a visible effect if [Light2D<class_Light2D>]\ s are affecting this **CanvasTexture**.

\ **Note:** Godot expects the normal map to use X+, Y+, and Z+ coordinates. See [this page ](http://wiki.polycount.com/wiki/Normal_Map_Technical_Details#Common_Swizzle_Coordinates)_ for a comparison of normal map coordinates expected by popular engines.


----



[Color<class_Color>] **specular_color** = `Color(1, 1, 1, 1)` [🔗<class_CanvasTexture_property_specular_color>]


- |void| **set_specular_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_specular_color**\ (\ )

The multiplier for specular reflection colors. The [Light2D<class_Light2D>]'s color is also taken into account when determining the reflection color. Only has a visible effect if [Light2D<class_Light2D>]\ s are affecting this **CanvasTexture**.


----



[float<class_float>] **specular_shininess** = `1.0` [🔗<class_CanvasTexture_property_specular_shininess>]


- |void| **set_specular_shininess**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_specular_shininess**\ (\ )

The specular exponent for [Light2D<class_Light2D>] specular reflections. Higher values result in a more glossy/"wet" look, with reflections becoming more localized and less visible overall. The default value of `1.0` disables specular reflections entirely. Only has a visible effect if [Light2D<class_Light2D>]\ s are affecting this **CanvasTexture**.


----



[Texture2D<class_Texture2D>] **specular_texture** [🔗<class_CanvasTexture_property_specular_texture>]


- |void| **set_specular_texture**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_specular_texture**\ (\ )

The specular map to use for [Light2D<class_Light2D>] specular reflections. This should be a grayscale or colored texture, with brighter areas resulting in a higher [specular_shininess<class_CanvasTexture_property_specular_shininess>] value. Using a colored [specular_texture<class_CanvasTexture_property_specular_texture>] allows controlling specular shininess on a per-channel basis. Only has a visible effect if [Light2D<class_Light2D>]\ s are affecting this **CanvasTexture**.


----



[TextureFilter<enum_CanvasItem_TextureFilter>] **texture_filter** = `0` [🔗<class_CanvasTexture_property_texture_filter>]


- |void| **set_texture_filter**\ (\ value\: [TextureFilter<enum_CanvasItem_TextureFilter>]\ )
- [TextureFilter<enum_CanvasItem_TextureFilter>] **get_texture_filter**\ (\ )

The texture filtering mode to use when drawing this **CanvasTexture**.


----



[TextureRepeat<enum_CanvasItem_TextureRepeat>] **texture_repeat** = `0` [🔗<class_CanvasTexture_property_texture_repeat>]


- |void| **set_texture_repeat**\ (\ value\: [TextureRepeat<enum_CanvasItem_TextureRepeat>]\ )
- [TextureRepeat<enum_CanvasItem_TextureRepeat>] **get_texture_repeat**\ (\ )

The texture repeat mode to use when drawing this **CanvasTexture**.

