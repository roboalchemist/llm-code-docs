:github_url: hide



# BoxMesh

**Inherits:** [PrimitiveMesh<class_PrimitiveMesh>] **<** [Mesh<class_Mesh>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Generate an axis-aligned box [PrimitiveMesh<class_PrimitiveMesh>].


## Description

Generate an axis-aligned box [PrimitiveMesh<class_PrimitiveMesh>].

The box's UV layout is arranged in a 3×2 layout that allows texturing each face individually. To apply the same texture on all faces, change the material's UV property to `Vector3(3, 2, 1)`. This is equivalent to adding `UV *= vec2(3.0, 2.0)` in a vertex shader.

\ **Note:** When using a large textured **BoxMesh** (e.g. as a floor), you may stumble upon UV jittering issues depending on the camera angle. To solve this, increase [subdivide_depth<class_BoxMesh_property_subdivide_depth>], [subdivide_height<class_BoxMesh_property_subdivide_height>] and [subdivide_width<class_BoxMesh_property_subdivide_width>] until you no longer notice UV jittering.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+------------------------------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`size<class_BoxMesh_property_size>`                         | ``Vector3(1, 1, 1)`` |
> +-------------------------------+------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`         | :ref:`subdivide_depth<class_BoxMesh_property_subdivide_depth>`   | ``0``                |
> +-------------------------------+------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`         | :ref:`subdivide_height<class_BoxMesh_property_subdivide_height>` | ``0``                |
> +-------------------------------+------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`         | :ref:`subdivide_width<class_BoxMesh_property_subdivide_width>`   | ``0``                |
> +-------------------------------+------------------------------------------------------------------+----------------------+
>

----


## Property Descriptions



[Vector3<class_Vector3>] **size** = `Vector3(1, 1, 1)` [🔗<class_BoxMesh_property_size>]


- |void| **set_size**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_size**\ (\ )

The box's width, height and depth.


----



[int<class_int>] **subdivide_depth** = `0` [🔗<class_BoxMesh_property_subdivide_depth>]


- |void| **set_subdivide_depth**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_subdivide_depth**\ (\ )

Number of extra edge loops inserted along the Z axis.


----



[int<class_int>] **subdivide_height** = `0` [🔗<class_BoxMesh_property_subdivide_height>]


- |void| **set_subdivide_height**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_subdivide_height**\ (\ )

Number of extra edge loops inserted along the Y axis.


----



[int<class_int>] **subdivide_width** = `0` [🔗<class_BoxMesh_property_subdivide_width>]


- |void| **set_subdivide_width**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_subdivide_width**\ (\ )

Number of extra edge loops inserted along the X axis.

