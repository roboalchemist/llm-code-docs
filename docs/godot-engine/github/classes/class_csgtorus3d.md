:github_url: hide



# CSGTorus3D

**Inherits:** [CSGPrimitive3D<class_CSGPrimitive3D>] **<** [CSGShape3D<class_CSGShape3D>] **<** [GeometryInstance3D<class_GeometryInstance3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A CSG Torus shape.


## Description

This node allows you to create a torus for use with the CSG system.

\ **Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D<class_MeshInstance3D>] with a [PrimitiveMesh<class_PrimitiveMesh>]. Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.


## Tutorials

- [../tutorials/3d/csg_tools](Prototyping levels with CSG .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+-------------------------------------------------------------+----------+
> | :ref:`float<class_float>`       | :ref:`inner_radius<class_CSGTorus3D_property_inner_radius>` | ``0.5``  |
> +---------------------------------+-------------------------------------------------------------+----------+
> | :ref:`Material<class_Material>` | :ref:`material<class_CSGTorus3D_property_material>`         |          |
> +---------------------------------+-------------------------------------------------------------+----------+
> | :ref:`float<class_float>`       | :ref:`outer_radius<class_CSGTorus3D_property_outer_radius>` | ``1.0``  |
> +---------------------------------+-------------------------------------------------------------+----------+
> | :ref:`int<class_int>`           | :ref:`ring_sides<class_CSGTorus3D_property_ring_sides>`     | ``6``    |
> +---------------------------------+-------------------------------------------------------------+----------+
> | :ref:`int<class_int>`           | :ref:`sides<class_CSGTorus3D_property_sides>`               | ``8``    |
> +---------------------------------+-------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>`         | :ref:`smooth_faces<class_CSGTorus3D_property_smooth_faces>` | ``true`` |
> +---------------------------------+-------------------------------------------------------------+----------+
>

----


## Property Descriptions



[float<class_float>] **inner_radius** = `0.5` [🔗<class_CSGTorus3D_property_inner_radius>]


- |void| **set_inner_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_inner_radius**\ (\ )

The inner radius of the torus.


----



[Material<class_Material>] **material** [🔗<class_CSGTorus3D_property_material>]


- |void| **set_material**\ (\ value\: [Material<class_Material>]\ )
- [Material<class_Material>] **get_material**\ (\ )

The material used to render the torus.


----



[float<class_float>] **outer_radius** = `1.0` [🔗<class_CSGTorus3D_property_outer_radius>]


- |void| **set_outer_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_outer_radius**\ (\ )

The outer radius of the torus.


----



[int<class_int>] **ring_sides** = `6` [🔗<class_CSGTorus3D_property_ring_sides>]


- |void| **set_ring_sides**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_ring_sides**\ (\ )

The number of edges each ring of the torus is constructed of.


----



[int<class_int>] **sides** = `8` [🔗<class_CSGTorus3D_property_sides>]


- |void| **set_sides**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_sides**\ (\ )

The number of slices the torus is constructed of.


----



[bool<class_bool>] **smooth_faces** = `true` [🔗<class_CSGTorus3D_property_smooth_faces>]


- |void| **set_smooth_faces**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_smooth_faces**\ (\ )

If `true` the normals of the torus are set to give a smooth effect making the torus seem rounded. If `false` the torus will have a flat shaded look.

