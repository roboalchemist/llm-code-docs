:github_url: hide

> **META**
	:keywords: padding



# MarginContainer

**Inherits:** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [EditorDock<class_EditorDock>]

A container that keeps a margin around its child controls.


## Description

**MarginContainer** adds an adjustable margin on each side of its child controls. The margins are added around all children, not around each individual one. To control the **MarginContainer**'s margins, use the `margin_*` theme properties listed below.

\ **Note:** The margin sizes are theme overrides, not normal properties. This is an example of how to change them in code:


> **TABS**
>

    # This code sample assumes the current script is extending MarginContainer.
    var margin_value = 100
    add_theme_constant_override("margin_top", margin_value)
    add_theme_constant_override("margin_left", margin_value)
    add_theme_constant_override("margin_bottom", margin_value)
    add_theme_constant_override("margin_right", margin_value)


    // This code sample assumes the current script is extending MarginContainer.
    int marginValue = 100;
    AddThemeConstantOverride("margin_top", marginValue);
    AddThemeConstantOverride("margin_left", marginValue);
    AddThemeConstantOverride("margin_bottom", marginValue);
    AddThemeConstantOverride("margin_right", marginValue);




## Tutorials

- [../tutorials/ui/gui_containers](Using Containers .md)


## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+--------------------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`margin_bottom<class_MarginContainer_theme_constant_margin_bottom>` | ``0`` |
> +-----------------------+--------------------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`margin_left<class_MarginContainer_theme_constant_margin_left>`     | ``0`` |
> +-----------------------+--------------------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`margin_right<class_MarginContainer_theme_constant_margin_right>`   | ``0`` |
> +-----------------------+--------------------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`margin_top<class_MarginContainer_theme_constant_margin_top>`       | ``0`` |
> +-----------------------+--------------------------------------------------------------------------+-------+
>

----


## Theme Property Descriptions



[int<class_int>] **margin_bottom** = `0` [🔗<class_MarginContainer_theme_constant_margin_bottom>]

Offsets towards the inside direct children of the container by this amount of pixels from the bottom.


----



[int<class_int>] **margin_left** = `0` [🔗<class_MarginContainer_theme_constant_margin_left>]

Offsets towards the inside direct children of the container by this amount of pixels from the left.


----



[int<class_int>] **margin_right** = `0` [🔗<class_MarginContainer_theme_constant_margin_right>]

Offsets towards the inside direct children of the container by this amount of pixels from the right.


----



[int<class_int>] **margin_top** = `0` [🔗<class_MarginContainer_theme_constant_margin_top>]

Offsets towards the inside direct children of the container by this amount of pixels from the top.

