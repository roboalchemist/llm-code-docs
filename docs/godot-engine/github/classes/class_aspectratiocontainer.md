:github_url: hide



# AspectRatioContainer

**Inherits:** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A container that preserves the proportions of its child controls.


## Description

A container type that arranges its child controls in a way that preserves their proportions automatically when the container is resized. Useful when a container has a dynamic size and the child nodes must adjust their sizes accordingly without losing their aspect ratios.


## Tutorials

- [../tutorials/ui/gui_containers](Using Containers .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------+---------------------------------------------------------------------------------------+---------+
> | :ref:`AlignmentMode<enum_AspectRatioContainer_AlignmentMode>` | :ref:`alignment_horizontal<class_AspectRatioContainer_property_alignment_horizontal>` | ``1``   |
> +---------------------------------------------------------------+---------------------------------------------------------------------------------------+---------+
> | :ref:`AlignmentMode<enum_AspectRatioContainer_AlignmentMode>` | :ref:`alignment_vertical<class_AspectRatioContainer_property_alignment_vertical>`     | ``1``   |
> +---------------------------------------------------------------+---------------------------------------------------------------------------------------+---------+
> | :ref:`float<class_float>`                                     | :ref:`ratio<class_AspectRatioContainer_property_ratio>`                               | ``1.0`` |
> +---------------------------------------------------------------+---------------------------------------------------------------------------------------+---------+
> | :ref:`StretchMode<enum_AspectRatioContainer_StretchMode>`     | :ref:`stretch_mode<class_AspectRatioContainer_property_stretch_mode>`                 | ``2``   |
> +---------------------------------------------------------------+---------------------------------------------------------------------------------------+---------+
>

----


## Enumerations



enum **StretchMode**: [🔗<enum_AspectRatioContainer_StretchMode>]



[StretchMode<enum_AspectRatioContainer_StretchMode>] **STRETCH_WIDTH_CONTROLS_HEIGHT** = `0`

The height of child controls is automatically adjusted based on the width of the container.



[StretchMode<enum_AspectRatioContainer_StretchMode>] **STRETCH_HEIGHT_CONTROLS_WIDTH** = `1`

The width of child controls is automatically adjusted based on the height of the container.



[StretchMode<enum_AspectRatioContainer_StretchMode>] **STRETCH_FIT** = `2`

The bounding rectangle of child controls is automatically adjusted to fit inside the container while keeping the aspect ratio.



[StretchMode<enum_AspectRatioContainer_StretchMode>] **STRETCH_COVER** = `3`

The width and height of child controls is automatically adjusted to make their bounding rectangle cover the entire area of the container while keeping the aspect ratio.

When the bounding rectangle of child controls exceed the container's size and [Control.clip_contents<class_Control_property_clip_contents>] is enabled, this allows to show only the container's area restricted by its own bounding rectangle.


----



enum **AlignmentMode**: [🔗<enum_AspectRatioContainer_AlignmentMode>]



[AlignmentMode<enum_AspectRatioContainer_AlignmentMode>] **ALIGNMENT_BEGIN** = `0`

Aligns child controls with the beginning (left or top) of the container.



[AlignmentMode<enum_AspectRatioContainer_AlignmentMode>] **ALIGNMENT_CENTER** = `1`

Aligns child controls with the center of the container.



[AlignmentMode<enum_AspectRatioContainer_AlignmentMode>] **ALIGNMENT_END** = `2`

Aligns child controls with the end (right or bottom) of the container.


----


## Property Descriptions



[AlignmentMode<enum_AspectRatioContainer_AlignmentMode>] **alignment_horizontal** = `1` [🔗<class_AspectRatioContainer_property_alignment_horizontal>]


- |void| **set_alignment_horizontal**\ (\ value\: [AlignmentMode<enum_AspectRatioContainer_AlignmentMode>]\ )
- [AlignmentMode<enum_AspectRatioContainer_AlignmentMode>] **get_alignment_horizontal**\ (\ )

Specifies the horizontal relative position of child controls.


----



[AlignmentMode<enum_AspectRatioContainer_AlignmentMode>] **alignment_vertical** = `1` [🔗<class_AspectRatioContainer_property_alignment_vertical>]


- |void| **set_alignment_vertical**\ (\ value\: [AlignmentMode<enum_AspectRatioContainer_AlignmentMode>]\ )
- [AlignmentMode<enum_AspectRatioContainer_AlignmentMode>] **get_alignment_vertical**\ (\ )

Specifies the vertical relative position of child controls.


----



[float<class_float>] **ratio** = `1.0` [🔗<class_AspectRatioContainer_property_ratio>]


- |void| **set_ratio**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_ratio**\ (\ )

The aspect ratio to enforce on child controls. This is the width divided by the height. The ratio depends on the [stretch_mode<class_AspectRatioContainer_property_stretch_mode>].


----



[StretchMode<enum_AspectRatioContainer_StretchMode>] **stretch_mode** = `2` [🔗<class_AspectRatioContainer_property_stretch_mode>]


- |void| **set_stretch_mode**\ (\ value\: [StretchMode<enum_AspectRatioContainer_StretchMode>]\ )
- [StretchMode<enum_AspectRatioContainer_StretchMode>] **get_stretch_mode**\ (\ )

The stretch mode used to align child controls.

