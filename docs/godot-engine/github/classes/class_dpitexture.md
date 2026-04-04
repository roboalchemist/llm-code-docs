:github_url: hide



# DPITexture

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Texture2D<class_Texture2D>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

An automatically scalable [Texture2D<class_Texture2D>] based on an SVG image.


## Description

An automatically scalable [Texture2D<class_Texture2D>] based on an SVG image. **DPITexture**\ s are used to automatically re-rasterize icons and other texture based UI theme elements to match viewport scale and font oversampling. See also [ProjectSettings.display/window/stretch/mode<class_ProjectSettings_property_display/window/stretch/mode>] ("canvas_items" mode) and [Viewport.oversampling_override<class_Viewport_property_oversampling_override>].


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------+---------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`base_scale<class_DPITexture_property_base_scale>` | ``1.0``                                                                                |
> +-------------------------------------+---------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>` | :ref:`color_map<class_DPITexture_property_color_map>`   | ``{}``                                                                                 |
> +-------------------------------------+---------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | resource_local_to_scene                                 | ``false`` (overrides :ref:`Resource<class_Resource_property_resource_local_to_scene>`) |
> +-------------------------------------+---------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`saturation<class_DPITexture_property_saturation>` | ``1.0``                                                                                |
> +-------------------------------------+---------------------------------------------------------+----------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`DPITexture<class_DPITexture>` | :ref:`create_from_string<class_DPITexture_method_create_from_string>`\ (\ source\: :ref:`String<class_String>`, scale\: :ref:`float<class_float>` = 1.0, saturation\: :ref:`float<class_float>` = 1.0, color_map\: :ref:`Dictionary<class_Dictionary>` = {}\ ) |static| |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`               | :ref:`get_scaled_rid<class_DPITexture_method_get_scaled_rid>`\ (\ ) |const|                                                                                                                                                                                             |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`         | :ref:`get_source<class_DPITexture_method_get_source>`\ (\ ) |const|                                                                                                                                                                                                     |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`set_size_override<class_DPITexture_method_set_size_override>`\ (\ size\: :ref:`Vector2i<class_Vector2i>`\ )                                                                                                                                                       |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`set_source<class_DPITexture_method_set_source>`\ (\ source\: :ref:`String<class_String>`\ )                                                                                                                                                                       |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **base_scale** = `1.0` [🔗<class_DPITexture_property_base_scale>]


- |void| **set_base_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_base_scale**\ (\ )

Texture scale. `1.0` is the original SVG size. Higher values result in a larger image.


----



[Dictionary<class_Dictionary>] **color_map** = `{}` [🔗<class_DPITexture_property_color_map>]


- |void| **set_color_map**\ (\ value\: [Dictionary<class_Dictionary>]\ )
- [Dictionary<class_Dictionary>] **get_color_map**\ (\ )

If set, remaps texture colors according to [Color<class_Color>]-[Color<class_Color>] map.


----



[float<class_float>] **saturation** = `1.0` [🔗<class_DPITexture_property_saturation>]


- |void| **set_saturation**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_saturation**\ (\ )

Overrides texture saturation.


----


## Method Descriptions



[DPITexture<class_DPITexture>] **create_from_string**\ (\ source\: [String<class_String>], scale\: [float<class_float>] = 1.0, saturation\: [float<class_float>] = 1.0, color_map\: [Dictionary<class_Dictionary>] = {}\ ) |static| [🔗<class_DPITexture_method_create_from_string>]

Creates a new **DPITexture** and initializes it by allocating and setting the SVG data to `source`.


----



[RID<class_RID>] **get_scaled_rid**\ (\ ) |const| [🔗<class_DPITexture_method_get_scaled_rid>]

Returns the [RID<class_RID>] of the texture rasterized to match the oversampling of the currently drawn canvas item.


----



[String<class_String>] **get_source**\ (\ ) |const| [🔗<class_DPITexture_method_get_source>]

Returns this SVG texture's source code.


----



|void| **set_size_override**\ (\ size\: [Vector2i<class_Vector2i>]\ ) [🔗<class_DPITexture_method_set_size_override>]

Resizes the texture to the specified dimensions.


----



|void| **set_source**\ (\ source\: [String<class_String>]\ ) [🔗<class_DPITexture_method_set_source>]

Sets this SVG texture's source code.

