:github_url: hide



# GridContainer

**Inherits:** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A container that arranges its child controls in a grid layout.


## Description

**GridContainer** arranges its child controls in a grid layout. The number of columns is specified by the [columns<class_GridContainer_property_columns>] property, whereas the number of rows depends on how many are needed for the child controls. The number of rows and columns is preserved for every size of the container.

\ **Note:** **GridContainer** only works with child nodes inheriting from [Control<class_Control>]. It won't rearrange child nodes inheriting from [Node2D<class_Node2D>].


## Tutorials

- [../tutorials/ui/gui_containers](Using Containers .md)

- [Operating System Testing Demo ](https://godotengine.org/asset-library/asset/2789)_


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`columns<class_GridContainer_property_columns>` | ``1`` |
> +-----------------------+------------------------------------------------------+-------+
>

## Theme Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+----------------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`h_separation<class_GridContainer_theme_constant_h_separation>` | ``4`` |
> +-----------------------+----------------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`v_separation<class_GridContainer_theme_constant_v_separation>` | ``4`` |
> +-----------------------+----------------------------------------------------------------------+-------+
>

----


## Property Descriptions



[int<class_int>] **columns** = `1` [🔗<class_GridContainer_property_columns>]


- |void| **set_columns**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_columns**\ (\ )

The number of columns in the **GridContainer**. If modified, **GridContainer** reorders its Control-derived children to accommodate the new layout.


----


## Theme Property Descriptions



[int<class_int>] **h_separation** = `4` [🔗<class_GridContainer_theme_constant_h_separation>]

The horizontal separation of child nodes.


----



[int<class_int>] **v_separation** = `4` [🔗<class_GridContainer_theme_constant_v_separation>]

The vertical separation of child nodes.

