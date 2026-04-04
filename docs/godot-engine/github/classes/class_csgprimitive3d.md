:github_url: hide



# CSGPrimitive3D

**Inherits:** [CSGShape3D<class_CSGShape3D>] **<** [GeometryInstance3D<class_GeometryInstance3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [CSGBox3D<class_CSGBox3D>], [CSGCylinder3D<class_CSGCylinder3D>], [CSGMesh3D<class_CSGMesh3D>], [CSGPolygon3D<class_CSGPolygon3D>], [CSGSphere3D<class_CSGSphere3D>], [CSGTorus3D<class_CSGTorus3D>]

Base class for CSG primitives.


## Description

Parent class for various CSG primitives. It contains code and functionality that is common between them. It cannot be used directly. Instead use one of the various classes that inherit from it.

\ **Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D<class_MeshInstance3D>] with a [PrimitiveMesh<class_PrimitiveMesh>]. Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.


## Tutorials

- [../tutorials/3d/csg_tools](Prototyping levels with CSG .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+-------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>` | :ref:`flip_faces<class_CSGPrimitive3D_property_flip_faces>` | ``false`` |
> +-------------------------+-------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[bool<class_bool>] **flip_faces** = `false` [🔗<class_CSGPrimitive3D_property_flip_faces>]


- |void| **set_flip_faces**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flip_faces**\ (\ )

If set, the order of the vertices in each triangle are reversed resulting in the backside of the mesh being drawn.

