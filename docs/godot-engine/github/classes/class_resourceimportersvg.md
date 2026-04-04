:github_url: hide



# ResourceImporterSVG

**Inherits:** [ResourceImporter<class_ResourceImporter>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Imports an SVG file as an automatically scalable texture for use in UI elements and 2D rendering.


## Description

This importer imports [DPITexture<class_DPITexture>] resources. See also [ResourceImporterTexture<class_ResourceImporterTexture>] and [ResourceImporterImage<class_ResourceImporterImage>].


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------+------------------------------------------------------------------+----------+
> | :ref:`float<class_float>`           | :ref:`base_scale<class_ResourceImporterSVG_property_base_scale>` | ``1.0``  |
> +-------------------------------------+------------------------------------------------------------------+----------+
> | :ref:`Dictionary<class_Dictionary>` | :ref:`color_map<class_ResourceImporterSVG_property_color_map>`   | ``{}``   |
> +-------------------------------------+------------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>`             | :ref:`compress<class_ResourceImporterSVG_property_compress>`     | ``true`` |
> +-------------------------------------+------------------------------------------------------------------+----------+
> | :ref:`float<class_float>`           | :ref:`saturation<class_ResourceImporterSVG_property_saturation>` | ``1.0``  |
> +-------------------------------------+------------------------------------------------------------------+----------+
>

----


## Property Descriptions



[float<class_float>] **base_scale** = `1.0` [🔗<class_ResourceImporterSVG_property_base_scale>]

Texture scale. `1.0` is the original SVG size. Higher values result in a larger image.


----



[Dictionary<class_Dictionary>] **color_map** = `{}` [🔗<class_ResourceImporterSVG_property_color_map>]

If set, remaps texture colors according to [Color<class_Color>]-[Color<class_Color>] map.


----



[bool<class_bool>] **compress** = `true` [🔗<class_ResourceImporterSVG_property_compress>]

If `true`, uses lossless compression for the SVG source.


----



[float<class_float>] **saturation** = `1.0` [🔗<class_ResourceImporterSVG_property_saturation>]

Overrides texture saturation.

