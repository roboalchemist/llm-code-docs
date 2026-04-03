:github_url: hide



# XRVRS

**Inherits:** [Object<class_Object>]

Helper class for XR interfaces that generates VRS images.


## Description

This class is used by various XR interfaces to generate VRS textures that can be used to speed up rendering.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+------------------------------------------------------------------+------------------------+
> | :ref:`float<class_float>`   | :ref:`vrs_min_radius<class_XRVRS_property_vrs_min_radius>`       | ``20.0``               |
> +-----------------------------+------------------------------------------------------------------+------------------------+
> | :ref:`Rect2i<class_Rect2i>` | :ref:`vrs_render_region<class_XRVRS_property_vrs_render_region>` | ``Rect2i(0, 0, 0, 0)`` |
> +-----------------------------+------------------------------------------------------------------+------------------------+
> | :ref:`float<class_float>`   | :ref:`vrs_strength<class_XRVRS_property_vrs_strength>`           | ``1.0``                |
> +-----------------------------+------------------------------------------------------------------+------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>` | :ref:`make_vrs_texture<class_XRVRS_method_make_vrs_texture>`\ (\ target_size\: :ref:`Vector2<class_Vector2>`, eye_foci\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ ) |
> +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **vrs_min_radius** = `20.0` [🔗<class_XRVRS_property_vrs_min_radius>]


- |void| **set_vrs_min_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_vrs_min_radius**\ (\ )

The minimum radius around the focal point where full quality is guaranteed if VRS is used as a percentage of screen size.


----



[Rect2i<class_Rect2i>] **vrs_render_region** = `Rect2i(0, 0, 0, 0)` [🔗<class_XRVRS_property_vrs_render_region>]


- |void| **set_vrs_render_region**\ (\ value\: [Rect2i<class_Rect2i>]\ )
- [Rect2i<class_Rect2i>] **get_vrs_render_region**\ (\ )

The render region that the VRS texture will be scaled to when generated.


----



[float<class_float>] **vrs_strength** = `1.0` [🔗<class_XRVRS_property_vrs_strength>]


- |void| **set_vrs_strength**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_vrs_strength**\ (\ )

The strength used to calculate the VRS density map. The greater this value, the more noticeable VRS is.


----


## Method Descriptions



[RID<class_RID>] **make_vrs_texture**\ (\ target_size\: [Vector2<class_Vector2>], eye_foci\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_XRVRS_method_make_vrs_texture>]

Generates the VRS texture based on a render `target_size` adjusted by our VRS tile size. For each eyes focal point passed in `eye_foci` a layer is created. Focal point should be in NDC.

The result will be cached, requesting a VRS texture with unchanged parameters and settings will return the cached RID.

