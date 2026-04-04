:github_url: hide



# GradientTexture1D

**Inherits:** [Texture2D<class_Texture2D>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 1D texture that uses colors obtained from a [Gradient<class_Gradient>].


## Description

A 1D texture that obtains colors from a [Gradient<class_Gradient>] to fill the texture data. The texture is filled by sampling the gradient for each pixel. Therefore, the texture does not necessarily represent an exact copy of the gradient, as it may miss some colors if there are not enough pixels. See also [GradientTexture2D<class_GradientTexture2D>], [CurveTexture<class_CurveTexture>] and [CurveXYZTexture<class_CurveXYZTexture>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Gradient<class_Gradient>` | :ref:`gradient<class_GradientTexture1D_property_gradient>` |                                                                                        |
> +---------------------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | resource_local_to_scene                                    | ``false`` (overrides :ref:`Resource<class_Resource_property_resource_local_to_scene>`) |
> +---------------------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`use_hdr<class_GradientTexture1D_property_use_hdr>`   | ``false``                                                                              |
> +---------------------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`width<class_GradientTexture1D_property_width>`       | ``256``                                                                                |
> +---------------------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Gradient<class_Gradient>] **gradient** [🔗<class_GradientTexture1D_property_gradient>]


- |void| **set_gradient**\ (\ value\: [Gradient<class_Gradient>]\ )
- [Gradient<class_Gradient>] **get_gradient**\ (\ )

The [Gradient<class_Gradient>] used to fill the texture.


----



[bool<class_bool>] **use_hdr** = `false` [🔗<class_GradientTexture1D_property_use_hdr>]


- |void| **set_use_hdr**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_hdr**\ (\ )

If `true`, the generated texture will support high dynamic range ([Image.FORMAT_RGBAF<class_Image_constant_FORMAT_RGBAF>] format). This allows for glow effects to work if [Environment.glow_enabled<class_Environment_property_glow_enabled>] is `true`. If `false`, the generated texture will use low dynamic range; overbright colors will be clamped ([Image.FORMAT_RGBA8<class_Image_constant_FORMAT_RGBA8>] format).


----



[int<class_int>] **width** = `256` [🔗<class_GradientTexture1D_property_width>]


- |void| **set_width**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_width**\ (\ )

The number of color samples that will be obtained from the [Gradient<class_Gradient>].

