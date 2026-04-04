:github_url: hide



# NavigationMeshSourceGeometryData3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Container for parsed source geometry data used in navigation mesh baking.


## Description

Container for parsed source geometry data used in navigation mesh baking.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`add_faces<class_NavigationMeshSourceGeometryData3D_method_add_faces>`\ (\ faces\: :ref:`PackedVector3Array<class_PackedVector3Array>`, xform\: :ref:`Transform3D<class_Transform3D>`\ )                                                                                                 |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`add_mesh<class_NavigationMeshSourceGeometryData3D_method_add_mesh>`\ (\ mesh\: :ref:`Mesh<class_Mesh>`, xform\: :ref:`Transform3D<class_Transform3D>`\ )                                                                                                                                |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`add_mesh_array<class_NavigationMeshSourceGeometryData3D_method_add_mesh_array>`\ (\ mesh_array\: :ref:`Array<class_Array>`, xform\: :ref:`Transform3D<class_Transform3D>`\ )                                                                                                            |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`add_projected_obstruction<class_NavigationMeshSourceGeometryData3D_method_add_projected_obstruction>`\ (\ vertices\: :ref:`PackedVector3Array<class_PackedVector3Array>`, elevation\: :ref:`float<class_float>`, height\: :ref:`float<class_float>`, carve\: :ref:`bool<class_bool>`\ ) |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`append_arrays<class_NavigationMeshSourceGeometryData3D_method_append_arrays>`\ (\ vertices\: :ref:`PackedFloat32Array<class_PackedFloat32Array>`, indices\: :ref:`PackedInt32Array<class_PackedInt32Array>`\ )                                                                          |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`clear<class_NavigationMeshSourceGeometryData3D_method_clear>`\ (\ )                                                                                                                                                                                                                     |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`clear_projected_obstructions<class_NavigationMeshSourceGeometryData3D_method_clear_projected_obstructions>`\ (\ )                                                                                                                                                                       |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>`                             | :ref:`get_bounds<class_NavigationMeshSourceGeometryData3D_method_get_bounds>`\ (\ )                                                                                                                                                                                                           |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`     | :ref:`get_indices<class_NavigationMeshSourceGeometryData3D_method_get_indices>`\ (\ ) |const|                                                                                                                                                                                                 |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                           | :ref:`get_projected_obstructions<class_NavigationMeshSourceGeometryData3D_method_get_projected_obstructions>`\ (\ ) |const|                                                                                                                                                                   |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedFloat32Array<class_PackedFloat32Array>` | :ref:`get_vertices<class_NavigationMeshSourceGeometryData3D_method_get_vertices>`\ (\ ) |const|                                                                                                                                                                                               |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`has_data<class_NavigationMeshSourceGeometryData3D_method_has_data>`\ (\ )                                                                                                                                                                                                               |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`merge<class_NavigationMeshSourceGeometryData3D_method_merge>`\ (\ other_geometry\: :ref:`NavigationMeshSourceGeometryData3D<class_NavigationMeshSourceGeometryData3D>`\ )                                                                                                               |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_indices<class_NavigationMeshSourceGeometryData3D_method_set_indices>`\ (\ indices\: :ref:`PackedInt32Array<class_PackedInt32Array>`\ )                                                                                                                                              |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_projected_obstructions<class_NavigationMeshSourceGeometryData3D_method_set_projected_obstructions>`\ (\ projected_obstructions\: :ref:`Array<class_Array>`\ )                                                                                                                       |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_vertices<class_NavigationMeshSourceGeometryData3D_method_set_vertices>`\ (\ vertices\: :ref:`PackedFloat32Array<class_PackedFloat32Array>`\ )                                                                                                                                       |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **add_faces**\ (\ faces\: [PackedVector3Array<class_PackedVector3Array>], xform\: [Transform3D<class_Transform3D>]\ ) [🔗<class_NavigationMeshSourceGeometryData3D_method_add_faces>]

Adds an array of vertex positions to the geometry data for navigation mesh baking to form triangulated faces. For each face the array must have three vertex positions in clockwise winding order. Since [NavigationMesh<class_NavigationMesh>] resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.


----



|void| **add_mesh**\ (\ mesh\: [Mesh<class_Mesh>], xform\: [Transform3D<class_Transform3D>]\ ) [🔗<class_NavigationMeshSourceGeometryData3D_method_add_mesh>]

Adds the geometry data of a [Mesh<class_Mesh>] resource to the navigation mesh baking data. The mesh must have valid triangulated mesh data to be considered. Since [NavigationMesh<class_NavigationMesh>] resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.


----



|void| **add_mesh_array**\ (\ mesh_array\: [Array<class_Array>], xform\: [Transform3D<class_Transform3D>]\ ) [🔗<class_NavigationMeshSourceGeometryData3D_method_add_mesh_array>]

Adds an [Array<class_Array>] the size of [Mesh.ARRAY_MAX<class_Mesh_constant_ARRAY_MAX>] and with vertices at index [Mesh.ARRAY_VERTEX<class_Mesh_constant_ARRAY_VERTEX>] and indices at index [Mesh.ARRAY_INDEX<class_Mesh_constant_ARRAY_INDEX>] to the navigation mesh baking data. The array must have valid triangulated mesh data to be considered. Since [NavigationMesh<class_NavigationMesh>] resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.


----



|void| **add_projected_obstruction**\ (\ vertices\: [PackedVector3Array<class_PackedVector3Array>], elevation\: [float<class_float>], height\: [float<class_float>], carve\: [bool<class_bool>]\ ) [🔗<class_NavigationMeshSourceGeometryData3D_method_add_projected_obstruction>]

Adds a projected obstruction shape to the source geometry. The `vertices` are considered projected on an xz-axes plane, placed at the global y-axis `elevation` and extruded by `height`. If `carve` is `true` the carved shape will not be affected by additional offsets (e.g. agent radius) of the navigation mesh baking process.


----



|void| **append_arrays**\ (\ vertices\: [PackedFloat32Array<class_PackedFloat32Array>], indices\: [PackedInt32Array<class_PackedInt32Array>]\ ) [🔗<class_NavigationMeshSourceGeometryData3D_method_append_arrays>]

Appends arrays of `vertices` and `indices` at the end of the existing arrays. Adds the existing index as an offset to the appended indices.


----



|void| **clear**\ (\ ) [🔗<class_NavigationMeshSourceGeometryData3D_method_clear>]

Clears the internal data.


----



|void| **clear_projected_obstructions**\ (\ ) [🔗<class_NavigationMeshSourceGeometryData3D_method_clear_projected_obstructions>]

Clears all projected obstructions.


----



[AABB<class_AABB>] **get_bounds**\ (\ ) [🔗<class_NavigationMeshSourceGeometryData3D_method_get_bounds>]

Returns an axis-aligned bounding box that covers all the stored geometry data. The bounds are calculated when calling this function with the result cached until further geometry changes are made.


----



[PackedInt32Array<class_PackedInt32Array>] **get_indices**\ (\ ) |const| [🔗<class_NavigationMeshSourceGeometryData3D_method_get_indices>]

Returns the parsed source geometry data indices array.


----



[Array<class_Array>] **get_projected_obstructions**\ (\ ) |const| [🔗<class_NavigationMeshSourceGeometryData3D_method_get_projected_obstructions>]

Returns the projected obstructions as an [Array<class_Array>] of dictionaries. Each [Dictionary<class_Dictionary>] contains the following entries:

- `vertices` - A [PackedFloat32Array<class_PackedFloat32Array>] that defines the outline points of the projected shape.

- `elevation` - A [float<class_float>] that defines the projected shape placement on the y-axis.

- `height` - A [float<class_float>] that defines how much the projected shape is extruded along the y-axis.

- `carve` - A [bool<class_bool>] that defines how the obstacle affects the navigation mesh baking. If `true` the projected shape will not be affected by addition offsets, e.g. agent radius.


----



[PackedFloat32Array<class_PackedFloat32Array>] **get_vertices**\ (\ ) |const| [🔗<class_NavigationMeshSourceGeometryData3D_method_get_vertices>]

Returns the parsed source geometry data vertices array.


----



[bool<class_bool>] **has_data**\ (\ ) [🔗<class_NavigationMeshSourceGeometryData3D_method_has_data>]

Returns `true` when parsed source geometry data exists.


----



|void| **merge**\ (\ other_geometry\: [NavigationMeshSourceGeometryData3D<class_NavigationMeshSourceGeometryData3D>]\ ) [🔗<class_NavigationMeshSourceGeometryData3D_method_merge>]

Adds the geometry data of another **NavigationMeshSourceGeometryData3D** to the navigation mesh baking data.


----



|void| **set_indices**\ (\ indices\: [PackedInt32Array<class_PackedInt32Array>]\ ) [🔗<class_NavigationMeshSourceGeometryData3D_method_set_indices>]

Sets the parsed source geometry data indices. The indices need to be matched with appropriated vertices.

\ **Warning:** Inappropriate data can crash the baking process of the involved third-party libraries.


----



|void| **set_projected_obstructions**\ (\ projected_obstructions\: [Array<class_Array>]\ ) [🔗<class_NavigationMeshSourceGeometryData3D_method_set_projected_obstructions>]

Sets the projected obstructions with an Array of Dictionaries with the following key value pairs:


> **TABS**
>

    "vertices" : PackedFloat32Array
    "elevation" : float
    "height" : float
    "carve" : bool




----



|void| **set_vertices**\ (\ vertices\: [PackedFloat32Array<class_PackedFloat32Array>]\ ) [🔗<class_NavigationMeshSourceGeometryData3D_method_set_vertices>]

Sets the parsed source geometry data vertices. The vertices need to be matched with appropriated indices.

\ **Warning:** Inappropriate data can crash the baking process of the involved third-party libraries.

