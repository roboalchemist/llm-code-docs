:github_url: hide



# BoxContainer

**Inherits:** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [HBoxContainer<class_HBoxContainer>], [VBoxContainer<class_VBoxContainer>]

A container that arranges its child controls horizontally or vertically.


## Description

A container that arranges its child controls horizontally or vertically, rearranging them automatically when their minimum size changes.


## Tutorials

- [../tutorials/ui/gui_containers](Using Containers .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------+---------------------------------------------------------+-----------+
> | :ref:`AlignmentMode<enum_BoxContainer_AlignmentMode>` | :ref:`alignment<class_BoxContainer_property_alignment>` | ``0``     |
> +-------------------------------------------------------+---------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                               | :ref:`vertical<class_BoxContainer_property_vertical>`   | ``false`` |
> +-------------------------------------------------------+---------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+------------------------------------------------------------------------------------------------+
> | :ref:`Control<class_Control>` | :ref:`add_spacer<class_BoxContainer_method_add_spacer>`\ (\ begin\: :ref:`bool<class_bool>`\ ) |
> +-------------------------------+------------------------------------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+-----------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`separation<class_BoxContainer_theme_constant_separation>` | ``4`` |
> +-----------------------+-----------------------------------------------------------------+-------+
>

----


## Enumerations



enum **AlignmentMode**: [🔗<enum_BoxContainer_AlignmentMode>]



[AlignmentMode<enum_BoxContainer_AlignmentMode>] **ALIGNMENT_BEGIN** = `0`

The child controls will be arranged at the beginning of the container, i.e. top if orientation is vertical, left if orientation is horizontal (right for RTL layout).



[AlignmentMode<enum_BoxContainer_AlignmentMode>] **ALIGNMENT_CENTER** = `1`

The child controls will be centered in the container.



[AlignmentMode<enum_BoxContainer_AlignmentMode>] **ALIGNMENT_END** = `2`

The child controls will be arranged at the end of the container, i.e. bottom if orientation is vertical, right if orientation is horizontal (left for RTL layout).


----


## Property Descriptions



[AlignmentMode<enum_BoxContainer_AlignmentMode>] **alignment** = `0` [🔗<class_BoxContainer_property_alignment>]


- |void| **set_alignment**\ (\ value\: [AlignmentMode<enum_BoxContainer_AlignmentMode>]\ )
- [AlignmentMode<enum_BoxContainer_AlignmentMode>] **get_alignment**\ (\ )

The alignment of the container's children (must be one of [ALIGNMENT_BEGIN<class_BoxContainer_constant_ALIGNMENT_BEGIN>], [ALIGNMENT_CENTER<class_BoxContainer_constant_ALIGNMENT_CENTER>], or [ALIGNMENT_END<class_BoxContainer_constant_ALIGNMENT_END>]).


----



[bool<class_bool>] **vertical** = `false` [🔗<class_BoxContainer_property_vertical>]


- |void| **set_vertical**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_vertical**\ (\ )

If `true`, the **BoxContainer** will arrange its children vertically, rather than horizontally.

Can't be changed when using [HBoxContainer<class_HBoxContainer>] and [VBoxContainer<class_VBoxContainer>].


----


## Method Descriptions



[Control<class_Control>] **add_spacer**\ (\ begin\: [bool<class_bool>]\ ) [🔗<class_BoxContainer_method_add_spacer>]

Adds a [Control<class_Control>] node to the box as a spacer. If `begin` is `true`, it will insert the [Control<class_Control>] node in front of all other children.


----


## Theme Property Descriptions



[int<class_int>] **separation** = `4` [🔗<class_BoxContainer_theme_constant_separation>]

The space between the **BoxContainer**'s elements, in pixels.

