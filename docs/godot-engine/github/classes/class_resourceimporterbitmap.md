:github_url: hide



# ResourceImporterBitMap

**Inherits:** [ResourceImporter<class_ResourceImporter>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Imports a [BitMap<class_BitMap>] resource (2D array of boolean values).


## Description

[BitMap<class_BitMap>] resources are typically used as click masks in [TextureButton<class_TextureButton>] and [TouchScreenButton<class_TouchScreenButton>].


## Tutorials

- [../tutorials/assets_pipeline/importing_images](Importing images .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------------------+---------+
> | :ref:`int<class_int>`     | :ref:`create_from<class_ResourceImporterBitMap_property_create_from>` | ``0``   |
> +---------------------------+-----------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`threshold<class_ResourceImporterBitMap_property_threshold>`     | ``0.5`` |
> +---------------------------+-----------------------------------------------------------------------+---------+
>

----


## Property Descriptions



[int<class_int>] **create_from** = `0` [🔗<class_ResourceImporterBitMap_property_create_from>]

The data source to use for generating the bitmap.

\ **Black & White:** Pixels whose HSV value is greater than the [threshold<class_ResourceImporterBitMap_property_threshold>] will be considered as "enabled" (bit is `true`). If the pixel is lower than or equal to the threshold, it will be considered as "disabled" (bit is `false`).

\ **Alpha:** Pixels whose alpha value is greater than the [threshold<class_ResourceImporterBitMap_property_threshold>] will be considered as "enabled" (bit is `true`). If the pixel is lower than or equal to the threshold, it will be considered as "disabled" (bit is `false`).


----



[float<class_float>] **threshold** = `0.5` [🔗<class_ResourceImporterBitMap_property_threshold>]

The threshold to use to determine which bits should be considered enabled or disabled. See also [create_from<class_ResourceImporterBitMap_property_create_from>].

