:github_url: hide



# PrismMesh

**Inherits:** [PrimitiveMesh<class_PrimitiveMesh>] **<** [Mesh<class_Mesh>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Class representing a prism-shaped [PrimitiveMesh<class_PrimitiveMesh>].


## Description

Class representing a prism-shaped [PrimitiveMesh<class_PrimitiveMesh>].


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+--------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`     | :ref:`left_to_right<class_PrismMesh_property_left_to_right>`       | ``0.5``              |
> +-------------------------------+--------------------------------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`size<class_PrismMesh_property_size>`                         | ``Vector3(1, 1, 1)`` |
> +-------------------------------+--------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`         | :ref:`subdivide_depth<class_PrismMesh_property_subdivide_depth>`   | ``0``                |
> +-------------------------------+--------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`         | :ref:`subdivide_height<class_PrismMesh_property_subdivide_height>` | ``0``                |
> +-------------------------------+--------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`         | :ref:`subdivide_width<class_PrismMesh_property_subdivide_width>`   | ``0``                |
> +-------------------------------+--------------------------------------------------------------------+----------------------+
>

----


## Property Descriptions



[float<class_float>] **left_to_right** = `0.5` [🔗<class_PrismMesh_property_left_to_right>]


- |void| **set_left_to_right**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_left_to_right**\ (\ )

Displacement of the upper edge along the X axis. 0.0 positions edge straight above the bottom-left edge.


----



[Vector3<class_Vector3>] **size** = `Vector3(1, 1, 1)` [🔗<class_PrismMesh_property_size>]


- |void| **set_size**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_size**\ (\ )

Size of the prism.


----



[int<class_int>] **subdivide_depth** = `0` [🔗<class_PrismMesh_property_subdivide_depth>]


- |void| **set_subdivide_depth**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_subdivide_depth**\ (\ )

Number of added edge loops along the Z axis.


----



[int<class_int>] **subdivide_height** = `0` [🔗<class_PrismMesh_property_subdivide_height>]


- |void| **set_subdivide_height**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_subdivide_height**\ (\ )

Number of added edge loops along the Y axis.


----



[int<class_int>] **subdivide_width** = `0` [🔗<class_PrismMesh_property_subdivide_width>]


- |void| **set_subdivide_width**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_subdivide_width**\ (\ )

Number of added edge loops along the X axis.

