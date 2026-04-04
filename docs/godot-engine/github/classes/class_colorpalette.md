:github_url: hide



# ColorPalette

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A resource class for managing a palette of colors, which can be loaded and saved using [ColorPicker<class_ColorPicker>].


## Description

The **ColorPalette** resource is designed to store and manage a collection of colors. This resource is useful in scenarios where a predefined set of colors is required, such as for creating themes, designing user interfaces, or managing game assets. The built-in [ColorPicker<class_ColorPicker>] control can also make use of **ColorPalette** without additional code.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+---------------------------------------------------+------------------------+
> | :ref:`PackedColorArray<class_PackedColorArray>` | :ref:`colors<class_ColorPalette_property_colors>` | ``PackedColorArray()`` |
> +-------------------------------------------------+---------------------------------------------------+------------------------+
>

----


## Property Descriptions



[PackedColorArray<class_PackedColorArray>] **colors** = `PackedColorArray()` [🔗<class_ColorPalette_property_colors>]


- |void| **set_colors**\ (\ value\: [PackedColorArray<class_PackedColorArray>]\ )
- [PackedColorArray<class_PackedColorArray>] **get_colors**\ (\ )

A [PackedColorArray<class_PackedColorArray>] containing the colors in the palette.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedColorArray<class_PackedColorArray>] for more details.

