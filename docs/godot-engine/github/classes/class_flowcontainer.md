:github_url: hide



# FlowContainer

**Inherits:** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [HFlowContainer<class_HFlowContainer>], [VFlowContainer<class_VFlowContainer>]

A container that arranges its child controls horizontally or vertically and wraps them around at the borders.


## Description

A container that arranges its child controls horizontally or vertically and wraps them around at the borders. This is similar to how text in a book wraps around when no more words can fit on a line.


## Tutorials

- [../tutorials/ui/gui_containers](Using Containers .md)


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`AlignmentMode<enum_FlowContainer_AlignmentMode>`                 | :ref:`alignment<class_FlowContainer_property_alignment>`                     | ``0``     |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>` | :ref:`last_wrap_alignment<class_FlowContainer_property_last_wrap_alignment>` | ``0``     |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                | :ref:`reverse_fill<class_FlowContainer_property_reverse_fill>`               | ``false`` |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                | :ref:`vertical<class_FlowContainer_property_vertical>`                       | ``false`` |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------+--------------------------------------------------------------------------------+
> | :ref:`int<class_int>` | :ref:`get_line_count<class_FlowContainer_method_get_line_count>`\ (\ ) |const| |
> +-----------------------+--------------------------------------------------------------------------------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+----------------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`h_separation<class_FlowContainer_theme_constant_h_separation>` | ``4`` |
> +-----------------------+----------------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`v_separation<class_FlowContainer_theme_constant_v_separation>` | ``4`` |
> +-----------------------+----------------------------------------------------------------------+-------+
>

----


## Enumerations



enum **AlignmentMode**: [🔗<enum_FlowContainer_AlignmentMode>]



[AlignmentMode<enum_FlowContainer_AlignmentMode>] **ALIGNMENT_BEGIN** = `0`

The child controls will be arranged at the beginning of the container, i.e. top if orientation is vertical, left if orientation is horizontal (right for RTL layout).



[AlignmentMode<enum_FlowContainer_AlignmentMode>] **ALIGNMENT_CENTER** = `1`

The child controls will be centered in the container.



[AlignmentMode<enum_FlowContainer_AlignmentMode>] **ALIGNMENT_END** = `2`

The child controls will be arranged at the end of the container, i.e. bottom if orientation is vertical, right if orientation is horizontal (left for RTL layout).


----



enum **LastWrapAlignmentMode**: [🔗<enum_FlowContainer_LastWrapAlignmentMode>]



[LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>] **LAST_WRAP_ALIGNMENT_INHERIT** = `0`

The last partially filled row or column will wrap aligned to the previous row or column in accordance with [alignment<class_FlowContainer_property_alignment>].



[LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>] **LAST_WRAP_ALIGNMENT_BEGIN** = `1`

The last partially filled row or column will wrap aligned to the beginning of the previous row or column.



[LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>] **LAST_WRAP_ALIGNMENT_CENTER** = `2`

The last partially filled row or column will wrap aligned to the center of the previous row or column.



[LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>] **LAST_WRAP_ALIGNMENT_END** = `3`

The last partially filled row or column will wrap aligned to the end of the previous row or column.


----


## Property Descriptions



[AlignmentMode<enum_FlowContainer_AlignmentMode>] **alignment** = `0` [🔗<class_FlowContainer_property_alignment>]


- |void| **set_alignment**\ (\ value\: [AlignmentMode<enum_FlowContainer_AlignmentMode>]\ )
- [AlignmentMode<enum_FlowContainer_AlignmentMode>] **get_alignment**\ (\ )

The alignment of the container's children (must be one of [ALIGNMENT_BEGIN<class_FlowContainer_constant_ALIGNMENT_BEGIN>], [ALIGNMENT_CENTER<class_FlowContainer_constant_ALIGNMENT_CENTER>], or [ALIGNMENT_END<class_FlowContainer_constant_ALIGNMENT_END>]).


----



[LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>] **last_wrap_alignment** = `0` [🔗<class_FlowContainer_property_last_wrap_alignment>]


- |void| **set_last_wrap_alignment**\ (\ value\: [LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>]\ )
- [LastWrapAlignmentMode<enum_FlowContainer_LastWrapAlignmentMode>] **get_last_wrap_alignment**\ (\ )

The wrap behavior of the last, partially filled row or column (must be one of [LAST_WRAP_ALIGNMENT_INHERIT<class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_INHERIT>], [LAST_WRAP_ALIGNMENT_BEGIN<class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_BEGIN>], [LAST_WRAP_ALIGNMENT_CENTER<class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_CENTER>], or [LAST_WRAP_ALIGNMENT_END<class_FlowContainer_constant_LAST_WRAP_ALIGNMENT_END>]).


----



[bool<class_bool>] **reverse_fill** = `false` [🔗<class_FlowContainer_property_reverse_fill>]


- |void| **set_reverse_fill**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_reverse_fill**\ (\ )

If `true`, reverses fill direction. Horizontal **FlowContainer**\ s will fill rows bottom to top, vertical **FlowContainer**\ s will fill columns right to left.

When using a vertical **FlowContainer** with a right to left [Control.layout_direction<class_Control_property_layout_direction>], columns will fill left to right instead.


----



[bool<class_bool>] **vertical** = `false` [🔗<class_FlowContainer_property_vertical>]


- |void| **set_vertical**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_vertical**\ (\ )

If `true`, the **FlowContainer** will arrange its children vertically, rather than horizontally.

Can't be changed when using [HFlowContainer<class_HFlowContainer>] and [VFlowContainer<class_VFlowContainer>].


----


## Method Descriptions



[int<class_int>] **get_line_count**\ (\ ) |const| [🔗<class_FlowContainer_method_get_line_count>]

Returns the current line count.


----


## Theme Property Descriptions



[int<class_int>] **h_separation** = `4` [🔗<class_FlowContainer_theme_constant_h_separation>]

The horizontal separation of child nodes.


----



[int<class_int>] **v_separation** = `4` [🔗<class_FlowContainer_theme_constant_v_separation>]

The vertical separation of child nodes.

