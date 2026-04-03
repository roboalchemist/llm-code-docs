:github_url: hide



# PlaneMesh

**Inherits:** [PrimitiveMesh<class_PrimitiveMesh>] **<** [Mesh<class_Mesh>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [QuadMesh<class_QuadMesh>]

Class representing a planar [PrimitiveMesh<class_PrimitiveMesh>].


## Description

Class representing a planar [PrimitiveMesh<class_PrimitiveMesh>]. This flat mesh does not have a thickness. By default, this mesh is aligned on the X and Z axes; this default rotation isn't suited for use with billboarded materials. For billboarded materials, change [orientation<class_PlaneMesh_property_orientation>] to [FACE_Z<class_PlaneMesh_constant_FACE_Z>].

\ **Note:** When using a large textured **PlaneMesh** (e.g. as a floor), you may stumble upon UV jittering issues depending on the camera angle. To solve this, increase [subdivide_depth<class_PlaneMesh_property_subdivide_depth>] and [subdivide_width<class_PlaneMesh_property_subdivide_width>] until you no longer notice UV jittering.


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------+------------------------------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>`                  | :ref:`center_offset<class_PlaneMesh_property_center_offset>`     | ``Vector3(0, 0, 0)`` |
> +------------------------------------------------+------------------------------------------------------------------+----------------------+
> | :ref:`Orientation<enum_PlaneMesh_Orientation>` | :ref:`orientation<class_PlaneMesh_property_orientation>`         | ``1``                |
> +------------------------------------------------+------------------------------------------------------------------+----------------------+
> | :ref:`Vector2<class_Vector2>`                  | :ref:`size<class_PlaneMesh_property_size>`                       | ``Vector2(2, 2)``    |
> +------------------------------------------------+------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`                          | :ref:`subdivide_depth<class_PlaneMesh_property_subdivide_depth>` | ``0``                |
> +------------------------------------------------+------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`                          | :ref:`subdivide_width<class_PlaneMesh_property_subdivide_width>` | ``0``                |
> +------------------------------------------------+------------------------------------------------------------------+----------------------+
>

----


## Enumerations



enum **Orientation**: [🔗<enum_PlaneMesh_Orientation>]



[Orientation<enum_PlaneMesh_Orientation>] **FACE_X** = `0`

**PlaneMesh** will face the positive X-axis.



[Orientation<enum_PlaneMesh_Orientation>] **FACE_Y** = `1`

**PlaneMesh** will face the positive Y-axis. This matches the behavior of the **PlaneMesh** in Godot 3.x.



[Orientation<enum_PlaneMesh_Orientation>] **FACE_Z** = `2`

**PlaneMesh** will face the positive Z-axis. This matches the behavior of the QuadMesh in Godot 3.x.


----


## Property Descriptions



[Vector3<class_Vector3>] **center_offset** = `Vector3(0, 0, 0)` [🔗<class_PlaneMesh_property_center_offset>]


- |void| **set_center_offset**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_center_offset**\ (\ )

Offset of the generated plane. Useful for particles.


----



[Orientation<enum_PlaneMesh_Orientation>] **orientation** = `1` [🔗<class_PlaneMesh_property_orientation>]


- |void| **set_orientation**\ (\ value\: [Orientation<enum_PlaneMesh_Orientation>]\ )
- [Orientation<enum_PlaneMesh_Orientation>] **get_orientation**\ (\ )

Direction that the **PlaneMesh** is facing.


----



[Vector2<class_Vector2>] **size** = `Vector2(2, 2)` [🔗<class_PlaneMesh_property_size>]


- |void| **set_size**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_size**\ (\ )

Size of the generated plane.


----



[int<class_int>] **subdivide_depth** = `0` [🔗<class_PlaneMesh_property_subdivide_depth>]


- |void| **set_subdivide_depth**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_subdivide_depth**\ (\ )

Number of subdivision along the Z axis.


----



[int<class_int>] **subdivide_width** = `0` [🔗<class_PlaneMesh_property_subdivide_width>]


- |void| **set_subdivide_width**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_subdivide_width**\ (\ )

Number of subdivision along the X axis.

