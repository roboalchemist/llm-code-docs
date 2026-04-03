:github_url: hide



# CurveXYZTexture

**Inherits:** [Texture2D<class_Texture2D>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 1D texture where the red, green, and blue color channels correspond to points on 3 curves.


## Description

A 1D texture where the red, green, and blue color channels correspond to points on 3 unit [Curve<class_Curve>] resources. Compared to using separate [CurveTexture<class_CurveTexture>]\ s, this further simplifies the task of saving curves as image files.

If you only need to store one curve within a single texture, use [CurveTexture<class_CurveTexture>] instead. See also [GradientTexture1D<class_GradientTexture1D>] and [GradientTexture2D<class_GradientTexture2D>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Curve<class_Curve>` | :ref:`curve_x<class_CurveXYZTexture_property_curve_x>` |                                                                                        |
> +---------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Curve<class_Curve>` | :ref:`curve_y<class_CurveXYZTexture_property_curve_y>` |                                                                                        |
> +---------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Curve<class_Curve>` | :ref:`curve_z<class_CurveXYZTexture_property_curve_z>` |                                                                                        |
> +---------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | resource_local_to_scene                                | ``false`` (overrides :ref:`Resource<class_Resource_property_resource_local_to_scene>`) |
> +---------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`     | :ref:`width<class_CurveXYZTexture_property_width>`     | ``256``                                                                                |
> +---------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Curve<class_Curve>] **curve_x** [🔗<class_CurveXYZTexture_property_curve_x>]


- |void| **set_curve_x**\ (\ value\: [Curve<class_Curve>]\ )
- [Curve<class_Curve>] **get_curve_x**\ (\ )

The [Curve<class_Curve>] that is rendered onto the texture's red channel. Should be a unit [Curve<class_Curve>].


----



[Curve<class_Curve>] **curve_y** [🔗<class_CurveXYZTexture_property_curve_y>]


- |void| **set_curve_y**\ (\ value\: [Curve<class_Curve>]\ )
- [Curve<class_Curve>] **get_curve_y**\ (\ )

The [Curve<class_Curve>] that is rendered onto the texture's green channel. Should be a unit [Curve<class_Curve>].


----



[Curve<class_Curve>] **curve_z** [🔗<class_CurveXYZTexture_property_curve_z>]


- |void| **set_curve_z**\ (\ value\: [Curve<class_Curve>]\ )
- [Curve<class_Curve>] **get_curve_z**\ (\ )

The [Curve<class_Curve>] that is rendered onto the texture's blue channel. Should be a unit [Curve<class_Curve>].


----



[int<class_int>] **width** = `256` [🔗<class_CurveXYZTexture_property_width>]


- |void| **set_width**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_width**\ (\ )

The width of the texture (in pixels). Higher values make it possible to represent high-frequency data better (such as sudden direction changes), at the cost of increased generation time and memory usage.

