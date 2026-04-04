:github_url: hide



# QuadMesh

**Inherits:** [PlaneMesh<class_PlaneMesh>] **<** [PrimitiveMesh<class_PrimitiveMesh>] **<** [Mesh<class_Mesh>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Class representing a square mesh facing the camera.


## Description

Class representing a square [PrimitiveMesh<class_PrimitiveMesh>]. This flat mesh does not have a thickness. By default, this mesh is aligned on the X and Y axes; this rotation is more suited for use with billboarded materials. A **QuadMesh** is equivalent to a [PlaneMesh<class_PlaneMesh>] except its default [PlaneMesh.orientation<class_PlaneMesh_property_orientation>] is [PlaneMesh.FACE_Z<class_PlaneMesh_constant_FACE_Z>].


## Tutorials

- [GUI in 3D Viewport Demo ](https://godotengine.org/asset-library/asset/2807)_

- [2D in 3D Viewport Demo ](https://godotengine.org/asset-library/asset/2803)_


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------+-------------+-------------------------------------------------------------------------------+
> | :ref:`Orientation<enum_PlaneMesh_Orientation>` | orientation | ``2`` (overrides :ref:`PlaneMesh<class_PlaneMesh_property_orientation>`)      |
> +------------------------------------------------+-------------+-------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                  | size        | ``Vector2(1, 1)`` (overrides :ref:`PlaneMesh<class_PlaneMesh_property_size>`) |
> +------------------------------------------------+-------------+-------------------------------------------------------------------------------+
>
