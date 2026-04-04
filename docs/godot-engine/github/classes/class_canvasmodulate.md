:github_url: hide

> **META**
	:keywords: color



# CanvasModulate

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A node that applies a color tint to a canvas.


## Description

**CanvasModulate** applies a color tint to all nodes on a canvas. Only one can be used to tint a canvas, but [CanvasLayer<class_CanvasLayer>]\ s can be used to render things independently.


## Tutorials

- [../tutorials/2d/2d_lights_and_shadows](2D lights and shadows .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>` | :ref:`color<class_CanvasModulate_property_color>` | ``Color(1, 1, 1, 1)`` |
> +---------------------------+---------------------------------------------------+-----------------------+
>

----


## Property Descriptions



[Color<class_Color>] **color** = `Color(1, 1, 1, 1)` [🔗<class_CanvasModulate_property_color>]


- |void| **set_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_color**\ (\ )

The tint color to apply.

