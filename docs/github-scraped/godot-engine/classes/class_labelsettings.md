:github_url: hide



# LabelSettings

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Provides common settings to customize the text in a [Label<class_Label>].


## Description

**LabelSettings** is a resource that provides common settings to customize the text in a [Label<class_Label>]. It will take priority over the properties defined in [Control.theme<class_Control_property_theme>]. The resource can be shared between multiple labels and changed on the fly, so it's convenient and flexible way to setup text style.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`Font<class_Font>`       | :ref:`font<class_LabelSettings_property_font>`                                   |                       |
> +-------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`     | :ref:`font_color<class_LabelSettings_property_font_color>`                       | ``Color(1, 1, 1, 1)`` |
> +-------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`         | :ref:`font_size<class_LabelSettings_property_font_size>`                         | ``16``                |
> +-------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`     | :ref:`line_spacing<class_LabelSettings_property_line_spacing>`                   | ``3.0``               |
> +-------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`     | :ref:`outline_color<class_LabelSettings_property_outline_color>`                 | ``Color(1, 1, 1, 1)`` |
> +-------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`         | :ref:`outline_size<class_LabelSettings_property_outline_size>`                   | ``0``                 |
> +-------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`     | :ref:`paragraph_spacing<class_LabelSettings_property_paragraph_spacing>`         | ``0.0``               |
> +-------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`     | :ref:`shadow_color<class_LabelSettings_property_shadow_color>`                   | ``Color(0, 0, 0, 0)`` |
> +-------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`shadow_offset<class_LabelSettings_property_shadow_offset>`                 | ``Vector2(1, 1)``     |
> +-------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`         | :ref:`shadow_size<class_LabelSettings_property_shadow_size>`                     | ``1``                 |
> +-------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`         | :ref:`stacked_outline_count<class_LabelSettings_property_stacked_outline_count>` | ``0``                 |
> +-------------------------------+----------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`         | :ref:`stacked_shadow_count<class_LabelSettings_property_stacked_shadow_count>`   | ``0``                 |
> +-------------------------------+----------------------------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`add_stacked_outline<class_LabelSettings_method_add_stacked_outline>`\ (\ index\: :ref:`int<class_int>` = -1\ )                                                  |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`add_stacked_shadow<class_LabelSettings_method_add_stacked_shadow>`\ (\ index\: :ref:`int<class_int>` = -1\ )                                                    |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>`     | :ref:`get_stacked_outline_color<class_LabelSettings_method_get_stacked_outline_color>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                   |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_stacked_outline_size<class_LabelSettings_method_get_stacked_outline_size>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                     |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>`     | :ref:`get_stacked_shadow_color<class_LabelSettings_method_get_stacked_shadow_color>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                     |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_stacked_shadow_offset<class_LabelSettings_method_get_stacked_shadow_offset>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                   |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_stacked_shadow_outline_size<class_LabelSettings_method_get_stacked_shadow_outline_size>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                       |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`move_stacked_outline<class_LabelSettings_method_move_stacked_outline>`\ (\ from_index\: :ref:`int<class_int>`, to_position\: :ref:`int<class_int>`\ )           |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`move_stacked_shadow<class_LabelSettings_method_move_stacked_shadow>`\ (\ from_index\: :ref:`int<class_int>`, to_position\: :ref:`int<class_int>`\ )             |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`remove_stacked_outline<class_LabelSettings_method_remove_stacked_outline>`\ (\ index\: :ref:`int<class_int>`\ )                                                 |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`remove_stacked_shadow<class_LabelSettings_method_remove_stacked_shadow>`\ (\ index\: :ref:`int<class_int>`\ )                                                   |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_stacked_outline_color<class_LabelSettings_method_set_stacked_outline_color>`\ (\ index\: :ref:`int<class_int>`, color\: :ref:`Color<class_Color>`\ )        |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_stacked_outline_size<class_LabelSettings_method_set_stacked_outline_size>`\ (\ index\: :ref:`int<class_int>`, size\: :ref:`int<class_int>`\ )               |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_stacked_shadow_color<class_LabelSettings_method_set_stacked_shadow_color>`\ (\ index\: :ref:`int<class_int>`, color\: :ref:`Color<class_Color>`\ )          |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_stacked_shadow_offset<class_LabelSettings_method_set_stacked_shadow_offset>`\ (\ index\: :ref:`int<class_int>`, offset\: :ref:`Vector2<class_Vector2>`\ )   |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_stacked_shadow_outline_size<class_LabelSettings_method_set_stacked_shadow_outline_size>`\ (\ index\: :ref:`int<class_int>`, size\: :ref:`int<class_int>`\ ) |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Font<class_Font>] **font** [🔗<class_LabelSettings_property_font>]


- |void| **set_font**\ (\ value\: [Font<class_Font>]\ )
- [Font<class_Font>] **get_font**\ (\ )

[Font<class_Font>] used for the text.


----



[Color<class_Color>] **font_color** = `Color(1, 1, 1, 1)` [🔗<class_LabelSettings_property_font_color>]


- |void| **set_font_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_font_color**\ (\ )

Color of the text.


----



[int<class_int>] **font_size** = `16` [🔗<class_LabelSettings_property_font_size>]


- |void| **set_font_size**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_font_size**\ (\ )

Size of the text.


----



[float<class_float>] **line_spacing** = `3.0` [🔗<class_LabelSettings_property_line_spacing>]


- |void| **set_line_spacing**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_line_spacing**\ (\ )

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.


----



[Color<class_Color>] **outline_color** = `Color(1, 1, 1, 1)` [🔗<class_LabelSettings_property_outline_color>]


- |void| **set_outline_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_outline_color**\ (\ )

The color of the outline.


----



[int<class_int>] **outline_size** = `0` [🔗<class_LabelSettings_property_outline_size>]


- |void| **set_outline_size**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_outline_size**\ (\ )

Text outline size.


----



[float<class_float>] **paragraph_spacing** = `0.0` [🔗<class_LabelSettings_property_paragraph_spacing>]


- |void| **set_paragraph_spacing**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_paragraph_spacing**\ (\ )

Vertical space between paragraphs. Added on top of [line_spacing<class_LabelSettings_property_line_spacing>].


----



[Color<class_Color>] **shadow_color** = `Color(0, 0, 0, 0)` [🔗<class_LabelSettings_property_shadow_color>]


- |void| **set_shadow_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_shadow_color**\ (\ )

Color of the shadow effect. If alpha is `0`, no shadow will be drawn.


----



[Vector2<class_Vector2>] **shadow_offset** = `Vector2(1, 1)` [🔗<class_LabelSettings_property_shadow_offset>]


- |void| **set_shadow_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_shadow_offset**\ (\ )

Offset of the shadow effect, in pixels.


----



[int<class_int>] **shadow_size** = `1` [🔗<class_LabelSettings_property_shadow_size>]


- |void| **set_shadow_size**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_shadow_size**\ (\ )

Size of the shadow effect.


----



[int<class_int>] **stacked_outline_count** = `0` [🔗<class_LabelSettings_property_stacked_outline_count>]


- |void| **set_stacked_outline_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_stacked_outline_count**\ (\ )

The number of stacked outlines.


----



[int<class_int>] **stacked_shadow_count** = `0` [🔗<class_LabelSettings_property_stacked_shadow_count>]


- |void| **set_stacked_shadow_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_stacked_shadow_count**\ (\ )

The number of stacked shadows.


----


## Method Descriptions



|void| **add_stacked_outline**\ (\ index\: [int<class_int>] = -1\ ) [🔗<class_LabelSettings_method_add_stacked_outline>]

Adds a new stacked outline to the label at the given `index`. If `index` is `-1`, the new stacked outline will be added at the end of the list.


----



|void| **add_stacked_shadow**\ (\ index\: [int<class_int>] = -1\ ) [🔗<class_LabelSettings_method_add_stacked_shadow>]

Adds a new stacked shadow to the label at the given `index`. If `index` is `-1`, the new stacked shadow will be added at the end of the list.


----



[Color<class_Color>] **get_stacked_outline_color**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_LabelSettings_method_get_stacked_outline_color>]

Returns the color of the stacked outline at `index`.


----



[int<class_int>] **get_stacked_outline_size**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_LabelSettings_method_get_stacked_outline_size>]

Returns the size of the stacked outline at `index`.


----



[Color<class_Color>] **get_stacked_shadow_color**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_LabelSettings_method_get_stacked_shadow_color>]

Returns the color of the stacked shadow at `index`.


----



[Vector2<class_Vector2>] **get_stacked_shadow_offset**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_LabelSettings_method_get_stacked_shadow_offset>]

Returns the offset of the stacked shadow at `index`.


----



[int<class_int>] **get_stacked_shadow_outline_size**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_LabelSettings_method_get_stacked_shadow_outline_size>]

Returns the outline size of the stacked shadow at `index`.


----



|void| **move_stacked_outline**\ (\ from_index\: [int<class_int>], to_position\: [int<class_int>]\ ) [🔗<class_LabelSettings_method_move_stacked_outline>]

Moves the stacked outline at index `from_index` to the given position `to_position` in the array.


----



|void| **move_stacked_shadow**\ (\ from_index\: [int<class_int>], to_position\: [int<class_int>]\ ) [🔗<class_LabelSettings_method_move_stacked_shadow>]

Moves the stacked shadow at index `from_index` to the given position `to_position` in the array.


----



|void| **remove_stacked_outline**\ (\ index\: [int<class_int>]\ ) [🔗<class_LabelSettings_method_remove_stacked_outline>]

Removes the stacked outline at index `index`.


----



|void| **remove_stacked_shadow**\ (\ index\: [int<class_int>]\ ) [🔗<class_LabelSettings_method_remove_stacked_shadow>]

Removes the stacked shadow at index `index`.


----



|void| **set_stacked_outline_color**\ (\ index\: [int<class_int>], color\: [Color<class_Color>]\ ) [🔗<class_LabelSettings_method_set_stacked_outline_color>]

Sets the color of the stacked outline identified by the given `index` to `color`.


----



|void| **set_stacked_outline_size**\ (\ index\: [int<class_int>], size\: [int<class_int>]\ ) [🔗<class_LabelSettings_method_set_stacked_outline_size>]

Sets the size of the stacked outline identified by the given `index` to `size`.


----



|void| **set_stacked_shadow_color**\ (\ index\: [int<class_int>], color\: [Color<class_Color>]\ ) [🔗<class_LabelSettings_method_set_stacked_shadow_color>]

Sets the color of the stacked shadow identified by the given `index` to `color`.


----



|void| **set_stacked_shadow_offset**\ (\ index\: [int<class_int>], offset\: [Vector2<class_Vector2>]\ ) [🔗<class_LabelSettings_method_set_stacked_shadow_offset>]

Sets the offset of the stacked shadow identified by the given `index` to `offset`.


----



|void| **set_stacked_shadow_outline_size**\ (\ index\: [int<class_int>], size\: [int<class_int>]\ ) [🔗<class_LabelSettings_method_set_stacked_shadow_outline_size>]

Sets the outline size of the stacked shadow identified by the given `index` to `size`.

