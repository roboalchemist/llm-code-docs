:github_url: hide



# ArrayMesh

**Inherits:** [Mesh<class_Mesh>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

[Mesh<class_Mesh>] type that provides utility for constructing a surface from arrays.


## Description

The **ArrayMesh** is used to construct a [Mesh<class_Mesh>] by specifying the attributes as arrays.

The most basic example is the creation of a single triangle:


> **TABS**
>

    var vertices = PackedVector3Array()
    vertices.push_back(Vector3(0, 1, 0))
    vertices.push_back(Vector3(1, 0, 0))
    vertices.push_back(Vector3(0, 0, 1))

    # Initialize the ArrayMesh.
    var arr_mesh = ArrayMesh.new()
    var arrays = []
    arrays.resize(Mesh.ARRAY_MAX)
    arrays[Mesh.ARRAY_VERTEX] = vertices

    # Create the Mesh.
    arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays)
    var m = MeshInstance3D.new()
    m.mesh = arr_mesh


    Vector3[] vertices =
    [
        new Vector3(0, 1, 0),
        new Vector3(1, 0, 0),
        new Vector3(0, 0, 1),
    ];

    // Initialize the ArrayMesh.
    var arrMesh = new ArrayMesh();
    Godot.Collections.Array arrays = [];
    arrays.Resize((int)Mesh.ArrayType.Max);
    arrays[(int)Mesh.ArrayType.Vertex] = vertices;

    // Create the Mesh.
    arrMesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, arrays);
    var m = new MeshInstance3D();
    m.Mesh = arrMesh;



The [MeshInstance3D<class_MeshInstance3D>] is ready to be added to the [SceneTree<class_SceneTree>] to be shown.

See also [ImmediateMesh<class_ImmediateMesh>], [MeshDataTool<class_MeshDataTool>] and [SurfaceTool<class_SurfaceTool>] for procedural geometry generation.

\ **Note:** Godot uses clockwise [winding order ](https://learnopengl.com/Advanced-OpenGL/Face-culling)_ for front faces of triangle primitive modes.


## Tutorials

- [../tutorials/3d/procedural_geometry/arraymesh](Procedural geometry using the ArrayMesh .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+--------------------------------------------------------------------+----------------------------+
> | :ref:`BlendShapeMode<enum_Mesh_BlendShapeMode>` | :ref:`blend_shape_mode<class_ArrayMesh_property_blend_shape_mode>` | ``1``                      |
> +-------------------------------------------------+--------------------------------------------------------------------+----------------------------+
> | :ref:`AABB<class_AABB>`                         | :ref:`custom_aabb<class_ArrayMesh_property_custom_aabb>`           | ``AABB(0, 0, 0, 0, 0, 0)`` |
> +-------------------------------------------------+--------------------------------------------------------------------+----------------------------+
> | :ref:`ArrayMesh<class_ArrayMesh>`               | :ref:`shadow_mesh<class_ArrayMesh_property_shadow_mesh>`           |                            |
> +-------------------------------------------------+--------------------------------------------------------------------+----------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                  | :ref:`add_blend_shape<class_ArrayMesh_method_add_blend_shape>`\ (\ name\: :ref:`StringName<class_StringName>`\ )                                                                                                                                                                                                                                                                      |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                  | :ref:`add_surface_from_arrays<class_ArrayMesh_method_add_surface_from_arrays>`\ (\ primitive\: :ref:`PrimitiveType<enum_Mesh_PrimitiveType>`, arrays\: :ref:`Array<class_Array>`, blend_shapes\: :ref:`Array<class_Array>`\[:ref:`Array<class_Array>`\] = [], lods\: :ref:`Dictionary<class_Dictionary>` = {}, flags\: |bitfield|\[:ref:`ArrayFormat<enum_Mesh_ArrayFormat>`\] = 0\ ) |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                  | :ref:`clear_blend_shapes<class_ArrayMesh_method_clear_blend_shapes>`\ (\ )                                                                                                                                                                                                                                                                                                            |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                  | :ref:`clear_surfaces<class_ArrayMesh_method_clear_surfaces>`\ (\ )                                                                                                                                                                                                                                                                                                                    |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                   | :ref:`get_blend_shape_count<class_ArrayMesh_method_get_blend_shape_count>`\ (\ ) |const|                                                                                                                                                                                                                                                                                              |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                     | :ref:`get_blend_shape_name<class_ArrayMesh_method_get_blend_shape_name>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                 |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                   | :ref:`lightmap_unwrap<class_ArrayMesh_method_lightmap_unwrap>`\ (\ transform\: :ref:`Transform3D<class_Transform3D>`, texel_size\: :ref:`float<class_float>`\ )                                                                                                                                                                                                                       |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                  | :ref:`regen_normal_maps<class_ArrayMesh_method_regen_normal_maps>`\ (\ )                                                                                                                                                                                                                                                                                                              |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                  | :ref:`set_blend_shape_name<class_ArrayMesh_method_set_blend_shape_name>`\ (\ index\: :ref:`int<class_int>`, name\: :ref:`StringName<class_StringName>`\ )                                                                                                                                                                                                                             |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                   | :ref:`surface_find_by_name<class_ArrayMesh_method_surface_find_by_name>`\ (\ name\: :ref:`String<class_String>`\ ) |const|                                                                                                                                                                                                                                                            |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                   | :ref:`surface_get_array_index_len<class_ArrayMesh_method_surface_get_array_index_len>`\ (\ surf_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                   | :ref:`surface_get_array_len<class_ArrayMesh_method_surface_get_array_len>`\ (\ surf_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                            |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |bitfield|\[:ref:`ArrayFormat<enum_Mesh_ArrayFormat>`\] | :ref:`surface_get_format<class_ArrayMesh_method_surface_get_format>`\ (\ surf_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                  |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                             | :ref:`surface_get_name<class_ArrayMesh_method_surface_get_name>`\ (\ surf_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                      |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PrimitiveType<enum_Mesh_PrimitiveType>`           | :ref:`surface_get_primitive_type<class_ArrayMesh_method_surface_get_primitive_type>`\ (\ surf_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                  |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                  | :ref:`surface_remove<class_ArrayMesh_method_surface_remove>`\ (\ surf_idx\: :ref:`int<class_int>`\ )                                                                                                                                                                                                                                                                                  |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                  | :ref:`surface_set_name<class_ArrayMesh_method_surface_set_name>`\ (\ surf_idx\: :ref:`int<class_int>`, name\: :ref:`String<class_String>`\ )                                                                                                                                                                                                                                          |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                  | :ref:`surface_update_attribute_region<class_ArrayMesh_method_surface_update_attribute_region>`\ (\ surf_idx\: :ref:`int<class_int>`, offset\: :ref:`int<class_int>`, data\: :ref:`PackedByteArray<class_PackedByteArray>`\ )                                                                                                                                                          |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                  | :ref:`surface_update_skin_region<class_ArrayMesh_method_surface_update_skin_region>`\ (\ surf_idx\: :ref:`int<class_int>`, offset\: :ref:`int<class_int>`, data\: :ref:`PackedByteArray<class_PackedByteArray>`\ )                                                                                                                                                                    |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                  | :ref:`surface_update_vertex_region<class_ArrayMesh_method_surface_update_vertex_region>`\ (\ surf_idx\: :ref:`int<class_int>`, offset\: :ref:`int<class_int>`, data\: :ref:`PackedByteArray<class_PackedByteArray>`\ )                                                                                                                                                                |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[BlendShapeMode<enum_Mesh_BlendShapeMode>] **blend_shape_mode** = `1` [🔗<class_ArrayMesh_property_blend_shape_mode>]


- |void| **set_blend_shape_mode**\ (\ value\: [BlendShapeMode<enum_Mesh_BlendShapeMode>]\ )
- [BlendShapeMode<enum_Mesh_BlendShapeMode>] **get_blend_shape_mode**\ (\ )

The blend shape mode.


----



[AABB<class_AABB>] **custom_aabb** = `AABB(0, 0, 0, 0, 0, 0)` [🔗<class_ArrayMesh_property_custom_aabb>]


- |void| **set_custom_aabb**\ (\ value\: [AABB<class_AABB>]\ )
- [AABB<class_AABB>] **get_custom_aabb**\ (\ )

Overrides the [AABB<class_AABB>] with one defined by user for use with frustum culling. Especially useful to avoid unexpected culling when using a shader to offset vertices.


----



[ArrayMesh<class_ArrayMesh>] **shadow_mesh** [🔗<class_ArrayMesh_property_shadow_mesh>]


- |void| **set_shadow_mesh**\ (\ value\: [ArrayMesh<class_ArrayMesh>]\ )
- [ArrayMesh<class_ArrayMesh>] **get_shadow_mesh**\ (\ )

An optional mesh which can be used for rendering shadows and the depth prepass. Can be used to increase performance by supplying a mesh with fused vertices and only vertex position data (without normals, UVs, colors, etc.).

\ **Note:** This mesh must have exactly the same vertex positions as the source mesh (including the source mesh's LODs, if present). If vertex positions differ, then the mesh will not draw correctly.


----


## Method Descriptions



|void| **add_blend_shape**\ (\ name\: [StringName<class_StringName>]\ ) [🔗<class_ArrayMesh_method_add_blend_shape>]

Adds name for a blend shape that will be added with [add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>]. Must be called before surface is added.


----



|void| **add_surface_from_arrays**\ (\ primitive\: [PrimitiveType<enum_Mesh_PrimitiveType>], arrays\: [Array<class_Array>], blend_shapes\: [Array<class_Array>]\[[Array<class_Array>]\] = [], lods\: [Dictionary<class_Dictionary>] = {}, flags\: |bitfield|\[[ArrayFormat<enum_Mesh_ArrayFormat>]\] = 0\ ) [🔗<class_ArrayMesh_method_add_surface_from_arrays>]

Creates a new surface. [Mesh.get_surface_count()<class_Mesh_method_get_surface_count>] will become the `surf_idx` for this new surface.

Surfaces are created to be rendered using a `primitive`, which may be any of the values defined in [PrimitiveType<enum_Mesh_PrimitiveType>].

The `arrays` argument is an array of arrays. Each of the [Mesh.ARRAY_MAX<class_Mesh_constant_ARRAY_MAX>] elements contains an array with some of the mesh data for this surface as described by the corresponding member of [ArrayType<enum_Mesh_ArrayType>] or `null` if it is not used by the surface. For example, `arrays[0]` is the array of vertices. That first vertex sub-array is always required; the others are optional. Adding an index array puts this surface into "index mode" where the vertex and other arrays become the sources of data and the index array defines the vertex order. All sub-arrays must have the same length as the vertex array (or be an exact multiple of the vertex array's length, when multiple elements of a sub-array correspond to a single vertex) or be empty, except for [Mesh.ARRAY_INDEX<class_Mesh_constant_ARRAY_INDEX>] if it is used.

The `blend_shapes` argument is an array of vertex data for each blend shape. Each element is an array of the same structure as `arrays`, but [Mesh.ARRAY_VERTEX<class_Mesh_constant_ARRAY_VERTEX>], [Mesh.ARRAY_NORMAL<class_Mesh_constant_ARRAY_NORMAL>], and [Mesh.ARRAY_TANGENT<class_Mesh_constant_ARRAY_TANGENT>] are set if and only if they are set in `arrays` and all other entries are `null`.

The `lods` argument is a dictionary with [float<class_float>] keys and [PackedInt32Array<class_PackedInt32Array>] values. Each entry in the dictionary represents an LOD level of the surface, where the value is the [Mesh.ARRAY_INDEX<class_Mesh_constant_ARRAY_INDEX>] array to use for the LOD level and the key is roughly proportional to the distance at which the LOD stats being used. I.e., increasing the key of an LOD also increases the distance that the objects has to be from the camera before the LOD is used.

The `flags` argument is the bitwise OR of, as required: One value of [ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] left shifted by `ARRAY_FORMAT_CUSTOMn_SHIFT` for each custom channel in use, [Mesh.ARRAY_FLAG_USE_DYNAMIC_UPDATE<class_Mesh_constant_ARRAY_FLAG_USE_DYNAMIC_UPDATE>], [Mesh.ARRAY_FLAG_USE_8_BONE_WEIGHTS<class_Mesh_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS>], or [Mesh.ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY<class_Mesh_constant_ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY>].

\ **Note:** When using indices, it is recommended to only use points, lines, or triangles.


----



|void| **clear_blend_shapes**\ (\ ) [🔗<class_ArrayMesh_method_clear_blend_shapes>]

Removes all blend shapes from this **ArrayMesh**.


----



|void| **clear_surfaces**\ (\ ) [🔗<class_ArrayMesh_method_clear_surfaces>]

Removes all surfaces from this **ArrayMesh**.


----



[int<class_int>] **get_blend_shape_count**\ (\ ) |const| [🔗<class_ArrayMesh_method_get_blend_shape_count>]

Returns the number of blend shapes that the **ArrayMesh** holds.


----



[StringName<class_StringName>] **get_blend_shape_name**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_ArrayMesh_method_get_blend_shape_name>]

Returns the name of the blend shape at this index.


----



[Error<enum_@GlobalScope_Error>] **lightmap_unwrap**\ (\ transform\: [Transform3D<class_Transform3D>], texel_size\: [float<class_float>]\ ) [🔗<class_ArrayMesh_method_lightmap_unwrap>]

Performs a UV unwrap on the **ArrayMesh** to prepare the mesh for lightmapping.


----



|void| **regen_normal_maps**\ (\ ) [🔗<class_ArrayMesh_method_regen_normal_maps>]

Regenerates tangents for each of the **ArrayMesh**'s surfaces.


----



|void| **set_blend_shape_name**\ (\ index\: [int<class_int>], name\: [StringName<class_StringName>]\ ) [🔗<class_ArrayMesh_method_set_blend_shape_name>]

Sets the name of the blend shape at this index.


----



[int<class_int>] **surface_find_by_name**\ (\ name\: [String<class_String>]\ ) |const| [🔗<class_ArrayMesh_method_surface_find_by_name>]

Returns the index of the first surface with this name held within this **ArrayMesh**. If none are found, -1 is returned.


----



[int<class_int>] **surface_get_array_index_len**\ (\ surf_idx\: [int<class_int>]\ ) |const| [🔗<class_ArrayMesh_method_surface_get_array_index_len>]

Returns the length in indices of the index array in the requested surface (see [add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>]).


----



[int<class_int>] **surface_get_array_len**\ (\ surf_idx\: [int<class_int>]\ ) |const| [🔗<class_ArrayMesh_method_surface_get_array_len>]

Returns the length in vertices of the vertex array in the requested surface (see [add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>]).


----



|bitfield|\[[ArrayFormat<enum_Mesh_ArrayFormat>]\] **surface_get_format**\ (\ surf_idx\: [int<class_int>]\ ) |const| [🔗<class_ArrayMesh_method_surface_get_format>]

Returns the format mask of the requested surface (see [add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>]).


----



[String<class_String>] **surface_get_name**\ (\ surf_idx\: [int<class_int>]\ ) |const| [🔗<class_ArrayMesh_method_surface_get_name>]

Gets the name assigned to this surface.


----



[PrimitiveType<enum_Mesh_PrimitiveType>] **surface_get_primitive_type**\ (\ surf_idx\: [int<class_int>]\ ) |const| [🔗<class_ArrayMesh_method_surface_get_primitive_type>]

Returns the primitive type of the requested surface (see [add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>]).


----



|void| **surface_remove**\ (\ surf_idx\: [int<class_int>]\ ) [🔗<class_ArrayMesh_method_surface_remove>]

Removes the surface at the given index from the Mesh, shifting surfaces with higher index down by one.


----



|void| **surface_set_name**\ (\ surf_idx\: [int<class_int>], name\: [String<class_String>]\ ) [🔗<class_ArrayMesh_method_surface_set_name>]

Sets a name for a given surface.


----



|void| **surface_update_attribute_region**\ (\ surf_idx\: [int<class_int>], offset\: [int<class_int>], data\: [PackedByteArray<class_PackedByteArray>]\ ) [🔗<class_ArrayMesh_method_surface_update_attribute_region>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **surface_update_skin_region**\ (\ surf_idx\: [int<class_int>], offset\: [int<class_int>], data\: [PackedByteArray<class_PackedByteArray>]\ ) [🔗<class_ArrayMesh_method_surface_update_skin_region>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **surface_update_vertex_region**\ (\ surf_idx\: [int<class_int>], offset\: [int<class_int>], data\: [PackedByteArray<class_PackedByteArray>]\ ) [🔗<class_ArrayMesh_method_surface_update_vertex_region>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

