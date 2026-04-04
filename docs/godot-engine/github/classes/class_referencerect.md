:github_url: hide



# ReferenceRect

**Inherits:** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A rectangular box for designing UIs.


## Description

A rectangular box that displays only a colored border around its rectangle (see [Control.get_rect()<class_Control_method_get_rect>]). It can be used to visualize the extents of a [Control<class_Control>] node, for testing purposes.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>` | :ref:`border_color<class_ReferenceRect_property_border_color>` | ``Color(1, 0, 0, 1)`` |
> +---------------------------+----------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>` | :ref:`border_width<class_ReferenceRect_property_border_width>` | ``1.0``               |
> +---------------------------+----------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`   | :ref:`editor_only<class_ReferenceRect_property_editor_only>`   | ``true``              |
> +---------------------------+----------------------------------------------------------------+-----------------------+
>

----


## Property Descriptions



[Color<class_Color>] **border_color** = `Color(1, 0, 0, 1)` [🔗<class_ReferenceRect_property_border_color>]


- |void| **set_border_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_border_color**\ (\ )

Sets the border color of the **ReferenceRect**.


----



[float<class_float>] **border_width** = `1.0` [🔗<class_ReferenceRect_property_border_width>]


- |void| **set_border_width**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_border_width**\ (\ )

Sets the border width of the **ReferenceRect**. The border grows both inwards and outwards with respect to the rectangle box.


----



[bool<class_bool>] **editor_only** = `true` [🔗<class_ReferenceRect_property_editor_only>]


- |void| **set_editor_only**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_editor_only**\ (\ )

If `true`, the **ReferenceRect** will only be visible while in editor. Otherwise, **ReferenceRect** will be visible in the running project.

