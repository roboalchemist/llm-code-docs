:github_url: hide



# ResourceImporterBMFont

**Inherits:** [ResourceImporter<class_ResourceImporter>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Imports a bitmap font in the BMFont (`.fnt`) format.


## Description

The BMFont format is a format created by the [BMFont ](https://www.angelcode.com/products/bmfont/)_ program. Many BMFont-compatible programs also exist, like [BMGlyph ](https://www.bmglyph.com/)_.

Compared to [ResourceImporterImageFont<class_ResourceImporterImageFont>], **ResourceImporterBMFont** supports bitmap fonts with varying glyph widths/heights.

See also [ResourceImporterDynamicFont<class_ResourceImporterDynamicFont>].


## Tutorials

- [Bitmap fonts - Using fonts ](../tutorials/ui/gui_using_fonts.html#bitmap-fonts)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-------------------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>`   | :ref:`compress<class_ResourceImporterBMFont_property_compress>`         | ``true`` |
> +---------------------------+-------------------------------------------------------------------------+----------+
> | :ref:`Array<class_Array>` | :ref:`fallbacks<class_ResourceImporterBMFont_property_fallbacks>`       | ``[]``   |
> +---------------------------+-------------------------------------------------------------------------+----------+
> | :ref:`int<class_int>`     | :ref:`scaling_mode<class_ResourceImporterBMFont_property_scaling_mode>` | ``2``    |
> +---------------------------+-------------------------------------------------------------------------+----------+
>

----


## Property Descriptions



[bool<class_bool>] **compress** = `true` [🔗<class_ResourceImporterBMFont_property_compress>]

If `true`, uses lossless compression for the resulting font.


----



[Array<class_Array>] **fallbacks** = `[]` [🔗<class_ResourceImporterBMFont_property_fallbacks>]

List of font fallbacks to use if a glyph isn't found in this bitmap font. Fonts at the beginning of the array are attempted first.


----



[int<class_int>] **scaling_mode** = `2` [🔗<class_ResourceImporterBMFont_property_scaling_mode>]

Font scaling mode.

