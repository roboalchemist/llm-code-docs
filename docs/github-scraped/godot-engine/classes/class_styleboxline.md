:github_url: hide



# StyleBoxLine

**Inherits:** [StyleBox<class_StyleBox>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A [StyleBox<class_StyleBox>] that displays a single line of a given color and thickness.


## Description

A [StyleBox<class_StyleBox>] that displays a single line of a given color and thickness. The line can be either horizontal or vertical. Useful for separators.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>` | :ref:`color<class_StyleBoxLine_property_color>`           | ``Color(0, 0, 0, 1)`` |
> +---------------------------+-----------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>` | :ref:`grow_begin<class_StyleBoxLine_property_grow_begin>` | ``1.0``               |
> +---------------------------+-----------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>` | :ref:`grow_end<class_StyleBoxLine_property_grow_end>`     | ``1.0``               |
> +---------------------------+-----------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`     | :ref:`thickness<class_StyleBoxLine_property_thickness>`   | ``1``                 |
> +---------------------------+-----------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`   | :ref:`vertical<class_StyleBoxLine_property_vertical>`     | ``false``             |
> +---------------------------+-----------------------------------------------------------+-----------------------+
>

----


## Property Descriptions



[Color<class_Color>] **color** = `Color(0, 0, 0, 1)` [🔗<class_StyleBoxLine_property_color>]


- |void| **set_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_color**\ (\ )

The line's color.


----



[float<class_float>] **grow_begin** = `1.0` [🔗<class_StyleBoxLine_property_grow_begin>]


- |void| **set_grow_begin**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_grow_begin**\ (\ )

The number of pixels the line will extend before the **StyleBoxLine**'s bounds. If set to a negative value, the line will begin inside the **StyleBoxLine**'s bounds.


----



[float<class_float>] **grow_end** = `1.0` [🔗<class_StyleBoxLine_property_grow_end>]


- |void| **set_grow_end**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_grow_end**\ (\ )

The number of pixels the line will extend past the **StyleBoxLine**'s bounds. If set to a negative value, the line will end inside the **StyleBoxLine**'s bounds.


----



[int<class_int>] **thickness** = `1` [🔗<class_StyleBoxLine_property_thickness>]


- |void| **set_thickness**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_thickness**\ (\ )

The line's thickness in pixels.


----



[bool<class_bool>] **vertical** = `false` [🔗<class_StyleBoxLine_property_vertical>]


- |void| **set_vertical**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_vertical**\ (\ )

If `true`, the line will be vertical. If `false`, the line will be horizontal.

