:github_url: hide

> **META**
	:keywords: omni, spot



# PointLight2D

**Inherits:** [Light2D<class_Light2D>] **<** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Positional 2D light source.


## Description

Casts light in a 2D environment. This light's shape is defined by a (usually grayscale) texture.


## Tutorials

- [../tutorials/2d/2d_lights_and_shadows](2D lights and shadows .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+-----------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`         | :ref:`height<class_PointLight2D_property_height>`               | ``0.0``           |
> +-----------------------------------+-----------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>`     | :ref:`offset<class_PointLight2D_property_offset>`               | ``Vector2(0, 0)`` |
> +-----------------------------------+-----------------------------------------------------------------+-------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`texture<class_PointLight2D_property_texture>`             |                   |
> +-----------------------------------+-----------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`         | :ref:`texture_scale<class_PointLight2D_property_texture_scale>` | ``1.0``           |
> +-----------------------------------+-----------------------------------------------------------------+-------------------+
>

----


## Property Descriptions



[float<class_float>] **height** = `0.0` [🔗<class_PointLight2D_property_height>]


- |void| **set_height**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_height**\ (\ )

The height of the light. Used with 2D normal mapping. The units are in pixels, e.g. if the height is 100, then it will illuminate an object 100 pixels away at a 45° angle to the plane.


----



[Vector2<class_Vector2>] **offset** = `Vector2(0, 0)` [🔗<class_PointLight2D_property_offset>]


- |void| **set_texture_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_texture_offset**\ (\ )

The offset of the light's [texture<class_PointLight2D_property_texture>].


----



[Texture2D<class_Texture2D>] **texture** [🔗<class_PointLight2D_property_texture>]


- |void| **set_texture**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture**\ (\ )

[Texture2D<class_Texture2D>] used for the light's appearance.


----



[float<class_float>] **texture_scale** = `1.0` [🔗<class_PointLight2D_property_texture_scale>]


- |void| **set_texture_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_texture_scale**\ (\ )

The [texture<class_PointLight2D_property_texture>]'s scale factor.

