:github_url: hide



# CSGBox3D

**Inherits:** [CSGPrimitive3D<class_CSGPrimitive3D>] **<** [CSGShape3D<class_CSGShape3D>] **<** [GeometryInstance3D<class_GeometryInstance3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A CSG Box shape.


## Description

This node allows you to create a box for use with the CSG system.

\ **Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D<class_MeshInstance3D>] with a [PrimitiveMesh<class_PrimitiveMesh>]. Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.


## Tutorials

- [../tutorials/3d/csg_tools](Prototyping levels with CSG .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+---------------------------------------------------+----------------------+
> | :ref:`Material<class_Material>` | :ref:`material<class_CSGBox3D_property_material>` |                      |
> +---------------------------------+---------------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>`   | :ref:`size<class_CSGBox3D_property_size>`         | ``Vector3(1, 1, 1)`` |
> +---------------------------------+---------------------------------------------------+----------------------+
>

----


## Property Descriptions



[Material<class_Material>] **material** [🔗<class_CSGBox3D_property_material>]


- |void| **set_material**\ (\ value\: [Material<class_Material>]\ )
- [Material<class_Material>] **get_material**\ (\ )

The material used to render the box.


----



[Vector3<class_Vector3>] **size** = `Vector3(1, 1, 1)` [🔗<class_CSGBox3D_property_size>]


- |void| **set_size**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_size**\ (\ )

The box's width, height and depth.

