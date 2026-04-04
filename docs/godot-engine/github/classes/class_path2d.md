:github_url: hide



# Path2D

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Contains a [Curve2D<class_Curve2D>] path for [PathFollow2D<class_PathFollow2D>] nodes to follow.


## Description

Can have [PathFollow2D<class_PathFollow2D>] child nodes moving along the [Curve2D<class_Curve2D>]. See [PathFollow2D<class_PathFollow2D>] for more information on usage.

\ **Note:** The path is considered as relative to the moved nodes (children of [PathFollow2D<class_PathFollow2D>]). As such, the curve should usually start with a zero vector (`(0, 0)`).


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+-------------------------------------------+
> | :ref:`Curve2D<class_Curve2D>` | :ref:`curve<class_Path2D_property_curve>` |
> +-------------------------------+-------------------------------------------+
>

----


## Property Descriptions



[Curve2D<class_Curve2D>] **curve** [🔗<class_Path2D_property_curve>]


- |void| **set_curve**\ (\ value\: [Curve2D<class_Curve2D>]\ )
- [Curve2D<class_Curve2D>] **get_curve**\ (\ )

A [Curve2D<class_Curve2D>] describing the path.

