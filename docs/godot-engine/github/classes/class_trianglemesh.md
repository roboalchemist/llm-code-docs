:github_url: hide



# TriangleMesh

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Triangle geometry for efficient, physicsless intersection queries.


## Description

Creates a bounding volume hierarchy (BVH) tree structure around triangle geometry.

The triangle BVH tree can be used for efficient intersection queries without involving a physics engine.

For example, this can be used in editor tools to select objects with complex shapes based on the mouse cursor position.

\ **Performance:** Creating the BVH tree for complex geometry is a slow process and best done in a background thread.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`create_from_faces<class_TriangleMesh_method_create_from_faces>`\ (\ faces\: :ref:`PackedVector3Array<class_PackedVector3Array>`\ )                        |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>` | :ref:`get_faces<class_TriangleMesh_method_get_faces>`\ (\ ) |const|                                                                                             |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                 | :ref:`intersect_ray<class_TriangleMesh_method_intersect_ray>`\ (\ begin\: :ref:`Vector3<class_Vector3>`, dir\: :ref:`Vector3<class_Vector3>`\ ) |const|         |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                 | :ref:`intersect_segment<class_TriangleMesh_method_intersect_segment>`\ (\ begin\: :ref:`Vector3<class_Vector3>`, end\: :ref:`Vector3<class_Vector3>`\ ) |const| |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[bool<class_bool>] **create_from_faces**\ (\ faces\: [PackedVector3Array<class_PackedVector3Array>]\ ) [🔗<class_TriangleMesh_method_create_from_faces>]

Creates the BVH tree from an array of faces. Each 3 vertices of the input `faces` array represent one triangle (face).

Returns `true` if the tree is successfully built, `false` otherwise.


----



[PackedVector3Array<class_PackedVector3Array>] **get_faces**\ (\ ) |const| [🔗<class_TriangleMesh_method_get_faces>]

Returns a copy of the geometry faces. Each 3 vertices of the array represent one triangle (face).


----



[Dictionary<class_Dictionary>] **intersect_ray**\ (\ begin\: [Vector3<class_Vector3>], dir\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_TriangleMesh_method_intersect_ray>]

Tests for intersection with a ray starting at `begin` and facing `dir` and extending toward infinity.

If an intersection with a triangle happens, returns a [Dictionary<class_Dictionary>] with the following fields:

\ `position`: The position on the intersected triangle.

\ `normal`: The normal of the intersected triangle.

\ `face_index`: The index of the intersected triangle.

Returns an empty [Dictionary<class_Dictionary>] if no intersection happens.

See also [intersect_segment()<class_TriangleMesh_method_intersect_segment>], which is similar but uses a finite-length segment.


----



[Dictionary<class_Dictionary>] **intersect_segment**\ (\ begin\: [Vector3<class_Vector3>], end\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_TriangleMesh_method_intersect_segment>]

Tests for intersection with a segment going from `begin` to `end`.

If an intersection with a triangle happens returns a [Dictionary<class_Dictionary>] with the following fields:

\ `position`: The position on the intersected triangle.

\ `normal`: The normal of the intersected triangle.

\ `face_index`: The index of the intersected triangle.

Returns an empty [Dictionary<class_Dictionary>] if no intersection happens.

See also [intersect_ray()<class_TriangleMesh_method_intersect_ray>], which is similar but uses an infinite-length ray.

