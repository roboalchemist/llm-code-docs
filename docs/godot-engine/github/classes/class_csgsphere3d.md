:github_url: hide



# CSGSphere3D

**Inherits:** [CSGPrimitive3D<class_CSGPrimitive3D>] **<** [CSGShape3D<class_CSGShape3D>] **<** [GeometryInstance3D<class_GeometryInstance3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A CSG Sphere shape.


## Description

This node allows you to create a sphere for use with the CSG system.

\ **Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D<class_MeshInstance3D>] with a [PrimitiveMesh<class_PrimitiveMesh>]. Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.


## Tutorials

- [../tutorials/3d/csg_tools](Prototyping levels with CSG .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+--------------------------------------------------------------------+----------+
> | :ref:`Material<class_Material>` | :ref:`material<class_CSGSphere3D_property_material>`               |          |
> +---------------------------------+--------------------------------------------------------------------+----------+
> | :ref:`int<class_int>`           | :ref:`radial_segments<class_CSGSphere3D_property_radial_segments>` | ``12``   |
> +---------------------------------+--------------------------------------------------------------------+----------+
> | :ref:`float<class_float>`       | :ref:`radius<class_CSGSphere3D_property_radius>`                   | ``0.5``  |
> +---------------------------------+--------------------------------------------------------------------+----------+
> | :ref:`int<class_int>`           | :ref:`rings<class_CSGSphere3D_property_rings>`                     | ``6``    |
> +---------------------------------+--------------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>`         | :ref:`smooth_faces<class_CSGSphere3D_property_smooth_faces>`       | ``true`` |
> +---------------------------------+--------------------------------------------------------------------+----------+
>

----


## Property Descriptions



[Material<class_Material>] **material** [🔗<class_CSGSphere3D_property_material>]


- |void| **set_material**\ (\ value\: [Material<class_Material>]\ )
- [Material<class_Material>] **get_material**\ (\ )

The material used to render the sphere.


----



[int<class_int>] **radial_segments** = `12` [🔗<class_CSGSphere3D_property_radial_segments>]


- |void| **set_radial_segments**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_radial_segments**\ (\ )

Number of vertical slices for the sphere.


----



[float<class_float>] **radius** = `0.5` [🔗<class_CSGSphere3D_property_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

Radius of the sphere.


----



[int<class_int>] **rings** = `6` [🔗<class_CSGSphere3D_property_rings>]


- |void| **set_rings**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_rings**\ (\ )

Number of horizontal slices for the sphere.


----



[bool<class_bool>] **smooth_faces** = `true` [🔗<class_CSGSphere3D_property_smooth_faces>]


- |void| **set_smooth_faces**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_smooth_faces**\ (\ )

If `true` the normals of the sphere are set to give a smooth effect making the sphere seem rounded. If `false` the sphere will have a flat shaded look.

