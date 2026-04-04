:github_url: hide



# CSGCylinder3D

**Inherits:** [CSGPrimitive3D<class_CSGPrimitive3D>] **<** [CSGShape3D<class_CSGShape3D>] **<** [GeometryInstance3D<class_GeometryInstance3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A CSG Cylinder shape.


## Description

This node allows you to create a cylinder (or cone) for use with the CSG system.

\ **Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D<class_MeshInstance3D>] with a [PrimitiveMesh<class_PrimitiveMesh>]. Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.


## Tutorials

- [../tutorials/3d/csg_tools](Prototyping levels with CSG .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+----------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`         | :ref:`cone<class_CSGCylinder3D_property_cone>`                 | ``false`` |
> +---------------------------------+----------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`       | :ref:`height<class_CSGCylinder3D_property_height>`             | ``2.0``   |
> +---------------------------------+----------------------------------------------------------------+-----------+
> | :ref:`Material<class_Material>` | :ref:`material<class_CSGCylinder3D_property_material>`         |           |
> +---------------------------------+----------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`       | :ref:`radius<class_CSGCylinder3D_property_radius>`             | ``0.5``   |
> +---------------------------------+----------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`           | :ref:`sides<class_CSGCylinder3D_property_sides>`               | ``8``     |
> +---------------------------------+----------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`         | :ref:`smooth_faces<class_CSGCylinder3D_property_smooth_faces>` | ``true``  |
> +---------------------------------+----------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[bool<class_bool>] **cone** = `false` [🔗<class_CSGCylinder3D_property_cone>]


- |void| **set_cone**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_cone**\ (\ )

If `true` a cone is created, the [radius<class_CSGCylinder3D_property_radius>] will only apply to one side.


----



[float<class_float>] **height** = `2.0` [🔗<class_CSGCylinder3D_property_height>]


- |void| **set_height**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_height**\ (\ )

The height of the cylinder.


----



[Material<class_Material>] **material** [🔗<class_CSGCylinder3D_property_material>]


- |void| **set_material**\ (\ value\: [Material<class_Material>]\ )
- [Material<class_Material>] **get_material**\ (\ )

The material used to render the cylinder.


----



[float<class_float>] **radius** = `0.5` [🔗<class_CSGCylinder3D_property_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

The radius of the cylinder.


----



[int<class_int>] **sides** = `8` [🔗<class_CSGCylinder3D_property_sides>]


- |void| **set_sides**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_sides**\ (\ )

The number of sides of the cylinder, the higher this number the more detail there will be in the cylinder.


----



[bool<class_bool>] **smooth_faces** = `true` [🔗<class_CSGCylinder3D_property_smooth_faces>]


- |void| **set_smooth_faces**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_smooth_faces**\ (\ )

If `true` the normals of the cylinder are set to give a smooth effect making the cylinder seem rounded. If `false` the cylinder will have a flat shaded look.

