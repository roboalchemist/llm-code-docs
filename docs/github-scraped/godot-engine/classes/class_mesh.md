:github_url: hide



# Mesh

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [ArrayMesh<class_ArrayMesh>], [ImmediateMesh<class_ImmediateMesh>], [PlaceholderMesh<class_PlaceholderMesh>], [PrimitiveMesh<class_PrimitiveMesh>]

A [Resource<class_Resource>] that contains vertex array-based geometry.


## Description

Mesh is a type of [Resource<class_Resource>] that contains vertex array-based geometry, divided in *surfaces*. Each surface contains a completely separate array and a material used to draw it. Design wise, a mesh with multiple surfaces is preferred to a single surface, because objects created in 3D editing software commonly contain multiple materials. The maximum number of surfaces per mesh is [RenderingServer.MAX_MESH_SURFACES<class_RenderingServer_constant_MAX_MESH_SURFACES>].


## Tutorials

- [3D Material Testers Demo ](https://godotengine.org/asset-library/asset/2742)_

- [3D Kinematic Character Demo ](https://godotengine.org/asset-library/asset/2739)_

- [3D Platformer Demo ](https://godotengine.org/asset-library/asset/2748)_

- [Third Person Shooter (TPS) Demo ](https://godotengine.org/asset-library/asset/2710)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+-------------------------------------------------------------------+--------------------+
> | :ref:`Vector2i<class_Vector2i>` | :ref:`lightmap_size_hint<class_Mesh_property_lightmap_size_hint>` | ``Vector2i(0, 0)`` |
> +---------------------------------+-------------------------------------------------------------------+--------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>`                                   | :ref:`_get_aabb<class_Mesh_private_method__get_aabb>`\ (\ ) |virtual| |required| |const|                                                                                            |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                     | :ref:`_get_blend_shape_count<class_Mesh_private_method__get_blend_shape_count>`\ (\ ) |virtual| |required| |const|                                                                  |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                       | :ref:`_get_blend_shape_name<class_Mesh_private_method__get_blend_shape_name>`\ (\ index\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                                     |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                     | :ref:`_get_surface_count<class_Mesh_private_method__get_surface_count>`\ (\ ) |virtual| |required| |const|                                                                          |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`_set_blend_shape_name<class_Mesh_private_method__set_blend_shape_name>`\ (\ index\: :ref:`int<class_int>`, name\: :ref:`StringName<class_StringName>`\ ) |virtual| |required| |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                     | :ref:`_surface_get_array_index_len<class_Mesh_private_method__surface_get_array_index_len>`\ (\ index\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                       |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                     | :ref:`_surface_get_array_len<class_Mesh_private_method__surface_get_array_len>`\ (\ index\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                                   |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                                 | :ref:`_surface_get_arrays<class_Mesh_private_method__surface_get_arrays>`\ (\ index\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                                         |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Array<class_Array>`\]    | :ref:`_surface_get_blend_shape_arrays<class_Mesh_private_method__surface_get_blend_shape_arrays>`\ (\ index\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                 |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                     | :ref:`_surface_get_format<class_Mesh_private_method__surface_get_format>`\ (\ index\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                                         |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                       | :ref:`_surface_get_lods<class_Mesh_private_method__surface_get_lods>`\ (\ index\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                                             |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Material<class_Material>`                           | :ref:`_surface_get_material<class_Mesh_private_method__surface_get_material>`\ (\ index\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                                     |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                     | :ref:`_surface_get_primitive_type<class_Mesh_private_method__surface_get_primitive_type>`\ (\ index\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                         |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`_surface_set_material<class_Mesh_private_method__surface_set_material>`\ (\ index\: :ref:`int<class_int>`, material\: :ref:`Material<class_Material>`\ ) |virtual| |required| |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ConvexPolygonShape3D<class_ConvexPolygonShape3D>`   | :ref:`create_convex_shape<class_Mesh_method_create_convex_shape>`\ (\ clean\: :ref:`bool<class_bool>` = true, simplify\: :ref:`bool<class_bool>` = false\ ) |const|                 |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Mesh<class_Mesh>`                                   | :ref:`create_outline<class_Mesh_method_create_outline>`\ (\ margin\: :ref:`float<class_float>`\ ) |const|                                                                           |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Resource<class_Resource>`                           | :ref:`create_placeholder<class_Mesh_method_create_placeholder>`\ (\ ) |const|                                                                                                       |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ConcavePolygonShape3D<class_ConcavePolygonShape3D>` | :ref:`create_trimesh_shape<class_Mesh_method_create_trimesh_shape>`\ (\ ) |const|                                                                                                   |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TriangleMesh<class_TriangleMesh>`                   | :ref:`generate_triangle_mesh<class_Mesh_method_generate_triangle_mesh>`\ (\ ) |const|                                                                                               |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>`                                   | :ref:`get_aabb<class_Mesh_method_get_aabb>`\ (\ ) |const|                                                                                                                           |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>`       | :ref:`get_faces<class_Mesh_method_get_faces>`\ (\ ) |const|                                                                                                                         |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                     | :ref:`get_surface_count<class_Mesh_method_get_surface_count>`\ (\ ) |const|                                                                                                         |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                                 | :ref:`surface_get_arrays<class_Mesh_method_surface_get_arrays>`\ (\ surf_idx\: :ref:`int<class_int>`\ ) |const|                                                                     |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Array<class_Array>`\]    | :ref:`surface_get_blend_shape_arrays<class_Mesh_method_surface_get_blend_shape_arrays>`\ (\ surf_idx\: :ref:`int<class_int>`\ ) |const|                                             |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Material<class_Material>`                           | :ref:`surface_get_material<class_Mesh_method_surface_get_material>`\ (\ surf_idx\: :ref:`int<class_int>`\ ) |const|                                                                 |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`surface_set_material<class_Mesh_method_surface_set_material>`\ (\ surf_idx\: :ref:`int<class_int>`, material\: :ref:`Material<class_Material>`\ )                             |
> +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **PrimitiveType**: [🔗<enum_Mesh_PrimitiveType>]



[PrimitiveType<enum_Mesh_PrimitiveType>] **PRIMITIVE_POINTS** = `0`

Render array as points (one vertex equals one point).



[PrimitiveType<enum_Mesh_PrimitiveType>] **PRIMITIVE_LINES** = `1`

Render array as lines (every two vertices a line is created).



[PrimitiveType<enum_Mesh_PrimitiveType>] **PRIMITIVE_LINE_STRIP** = `2`

Render array as line strip.



[PrimitiveType<enum_Mesh_PrimitiveType>] **PRIMITIVE_TRIANGLES** = `3`

Render array as triangles (every three vertices a triangle is created).



[PrimitiveType<enum_Mesh_PrimitiveType>] **PRIMITIVE_TRIANGLE_STRIP** = `4`

Render array as triangle strips.


----



enum **ArrayType**: [🔗<enum_Mesh_ArrayType>]



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_VERTEX** = `0`

[PackedVector3Array<class_PackedVector3Array>], [PackedVector2Array<class_PackedVector2Array>], or [Array<class_Array>] of vertex positions.



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_NORMAL** = `1`

[PackedVector3Array<class_PackedVector3Array>] of vertex normals.

\ **Note:** The array has to consist of normal vectors, otherwise they will be normalized by the engine, potentially causing visual discrepancies.



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_TANGENT** = `2`

[PackedFloat32Array<class_PackedFloat32Array>] of vertex tangents. Each element in groups of 4 floats, first 3 floats determine the tangent, and the last the binormal direction as -1 or 1.



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_COLOR** = `3`

[PackedColorArray<class_PackedColorArray>] of vertex colors.



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_TEX_UV** = `4`

[PackedVector2Array<class_PackedVector2Array>] for UV coordinates.



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_TEX_UV2** = `5`

[PackedVector2Array<class_PackedVector2Array>] for second UV coordinates.



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_CUSTOM0** = `6`

Contains custom color channel 0. [PackedByteArray<class_PackedByteArray>] if `(format >> Mesh.ARRAY_FORMAT_CUSTOM0_SHIFT) & Mesh.ARRAY_FORMAT_CUSTOM_MASK` is [ARRAY_CUSTOM_RGBA8_UNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_UNORM>], [ARRAY_CUSTOM_RGBA8_SNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_SNORM>], [ARRAY_CUSTOM_RG_HALF<class_Mesh_constant_ARRAY_CUSTOM_RG_HALF>], or [ARRAY_CUSTOM_RGBA_HALF<class_Mesh_constant_ARRAY_CUSTOM_RGBA_HALF>]. [PackedFloat32Array<class_PackedFloat32Array>] otherwise.



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_CUSTOM1** = `7`

Contains custom color channel 1. [PackedByteArray<class_PackedByteArray>] if `(format >> Mesh.ARRAY_FORMAT_CUSTOM1_SHIFT) & Mesh.ARRAY_FORMAT_CUSTOM_MASK` is [ARRAY_CUSTOM_RGBA8_UNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_UNORM>], [ARRAY_CUSTOM_RGBA8_SNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_SNORM>], [ARRAY_CUSTOM_RG_HALF<class_Mesh_constant_ARRAY_CUSTOM_RG_HALF>], or [ARRAY_CUSTOM_RGBA_HALF<class_Mesh_constant_ARRAY_CUSTOM_RGBA_HALF>]. [PackedFloat32Array<class_PackedFloat32Array>] otherwise.



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_CUSTOM2** = `8`

Contains custom color channel 2. [PackedByteArray<class_PackedByteArray>] if `(format >> Mesh.ARRAY_FORMAT_CUSTOM2_SHIFT) & Mesh.ARRAY_FORMAT_CUSTOM_MASK` is [ARRAY_CUSTOM_RGBA8_UNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_UNORM>], [ARRAY_CUSTOM_RGBA8_SNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_SNORM>], [ARRAY_CUSTOM_RG_HALF<class_Mesh_constant_ARRAY_CUSTOM_RG_HALF>], or [ARRAY_CUSTOM_RGBA_HALF<class_Mesh_constant_ARRAY_CUSTOM_RGBA_HALF>]. [PackedFloat32Array<class_PackedFloat32Array>] otherwise.



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_CUSTOM3** = `9`

Contains custom color channel 3. [PackedByteArray<class_PackedByteArray>] if `(format >> Mesh.ARRAY_FORMAT_CUSTOM3_SHIFT) & Mesh.ARRAY_FORMAT_CUSTOM_MASK` is [ARRAY_CUSTOM_RGBA8_UNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_UNORM>], [ARRAY_CUSTOM_RGBA8_SNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_SNORM>], [ARRAY_CUSTOM_RG_HALF<class_Mesh_constant_ARRAY_CUSTOM_RG_HALF>], or [ARRAY_CUSTOM_RGBA_HALF<class_Mesh_constant_ARRAY_CUSTOM_RGBA_HALF>]. [PackedFloat32Array<class_PackedFloat32Array>] otherwise.



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_BONES** = `10`

[PackedFloat32Array<class_PackedFloat32Array>] or [PackedInt32Array<class_PackedInt32Array>] of bone indices. Contains either 4 or 8 numbers per vertex depending on the presence of the [ARRAY_FLAG_USE_8_BONE_WEIGHTS<class_Mesh_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS>] flag.



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_WEIGHTS** = `11`

[PackedFloat32Array<class_PackedFloat32Array>] or [PackedFloat64Array<class_PackedFloat64Array>] of bone weights in the range `0.0` to `1.0` (inclusive). Contains either 4 or 8 numbers per vertex depending on the presence of the [ARRAY_FLAG_USE_8_BONE_WEIGHTS<class_Mesh_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS>] flag.



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_INDEX** = `12`

[PackedInt32Array<class_PackedInt32Array>] of integers used as indices referencing vertices, colors, normals, tangents, and textures. All of those arrays must have the same number of elements as the vertex array. No index can be beyond the vertex array size. When this index array is present, it puts the function into "index mode," where the index selects the *i*'th vertex, normal, tangent, color, UV, etc. This means if you want to have different normals or colors along an edge, you have to duplicate the vertices.

For triangles, the index array is interpreted as triples, referring to the vertices of each triangle. For lines, the index array is in pairs indicating the start and end of each line.



[ArrayType<enum_Mesh_ArrayType>] **ARRAY_MAX** = `13`

Represents the size of the [ArrayType<enum_Mesh_ArrayType>] enum.


----



enum **ArrayCustomFormat**: [🔗<enum_Mesh_ArrayCustomFormat>]



[ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] **ARRAY_CUSTOM_RGBA8_UNORM** = `0`

Indicates this custom channel contains unsigned normalized byte colors from 0 to 1, encoded as [PackedByteArray<class_PackedByteArray>].



[ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] **ARRAY_CUSTOM_RGBA8_SNORM** = `1`

Indicates this custom channel contains signed normalized byte colors from -1 to 1, encoded as [PackedByteArray<class_PackedByteArray>].



[ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] **ARRAY_CUSTOM_RG_HALF** = `2`

Indicates this custom channel contains half precision float colors, encoded as [PackedByteArray<class_PackedByteArray>]. Only red and green channels are used.



[ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] **ARRAY_CUSTOM_RGBA_HALF** = `3`

Indicates this custom channel contains half precision float colors, encoded as [PackedByteArray<class_PackedByteArray>].



[ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] **ARRAY_CUSTOM_R_FLOAT** = `4`

Indicates this custom channel contains full float colors, in a [PackedFloat32Array<class_PackedFloat32Array>]. Only the red channel is used.



[ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] **ARRAY_CUSTOM_RG_FLOAT** = `5`

Indicates this custom channel contains full float colors, in a [PackedFloat32Array<class_PackedFloat32Array>]. Only red and green channels are used.



[ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] **ARRAY_CUSTOM_RGB_FLOAT** = `6`

Indicates this custom channel contains full float colors, in a [PackedFloat32Array<class_PackedFloat32Array>]. Only red, green and blue channels are used.



[ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] **ARRAY_CUSTOM_RGBA_FLOAT** = `7`

Indicates this custom channel contains full float colors, in a [PackedFloat32Array<class_PackedFloat32Array>].



[ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] **ARRAY_CUSTOM_MAX** = `8`

Represents the size of the [ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] enum.


----



flags **ArrayFormat**: [🔗<enum_Mesh_ArrayFormat>]



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_VERTEX** = `1`

Mesh array contains vertices. All meshes require a vertex array so this should always be present.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_NORMAL** = `2`

Mesh array contains normals.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_TANGENT** = `4`

Mesh array contains tangents.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_COLOR** = `8`

Mesh array contains colors.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_TEX_UV** = `16`

Mesh array contains UVs.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_TEX_UV2** = `32`

Mesh array contains second UV.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_CUSTOM0** = `64`

Mesh array contains custom channel index 0.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_CUSTOM1** = `128`

Mesh array contains custom channel index 1.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_CUSTOM2** = `256`

Mesh array contains custom channel index 2.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_CUSTOM3** = `512`

Mesh array contains custom channel index 3.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_BONES** = `1024`

Mesh array contains bones.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_WEIGHTS** = `2048`

Mesh array contains bone weights.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_INDEX** = `4096`

Mesh array uses indices.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_BLEND_SHAPE_MASK** = `7`

Mask of mesh channels permitted in blend shapes.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_CUSTOM_BASE** = `13`

Shift of first custom channel.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_CUSTOM_BITS** = `3`

Number of format bits per custom channel. See [ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>].



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_CUSTOM0_SHIFT** = `13`

Amount to shift [ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] for custom channel index 0.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_CUSTOM1_SHIFT** = `16`

Amount to shift [ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] for custom channel index 1.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_CUSTOM2_SHIFT** = `19`

Amount to shift [ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] for custom channel index 2.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_CUSTOM3_SHIFT** = `22`

Amount to shift [ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>] for custom channel index 3.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FORMAT_CUSTOM_MASK** = `7`

Mask of custom format bits per custom channel. Must be shifted by one of the SHIFT constants. See [ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>].



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_COMPRESS_FLAGS_BASE** = `25`

Shift of first compress flag. Compress flags should be passed to [ArrayMesh.add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>] and [SurfaceTool.commit()<class_SurfaceTool_method_commit>].



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FLAG_USE_2D_VERTICES** = `33554432`

Flag used to mark that the array contains 2D vertices.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FLAG_USE_DYNAMIC_UPDATE** = `67108864`

Flag used to mark that the mesh data will use `GL_DYNAMIC_DRAW` on GLES. Unused on Vulkan.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FLAG_USE_8_BONE_WEIGHTS** = `134217728`

Flag used to mark that the mesh contains up to 8 bone influences per vertex. This flag indicates that [ARRAY_BONES<class_Mesh_constant_ARRAY_BONES>] and [ARRAY_WEIGHTS<class_Mesh_constant_ARRAY_WEIGHTS>] elements will have double length.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY** = `268435456`

Flag used to mark that the mesh intentionally contains no vertex array.



[ArrayFormat<enum_Mesh_ArrayFormat>] **ARRAY_FLAG_COMPRESS_ATTRIBUTES** = `536870912`

Flag used to mark that a mesh is using compressed attributes (vertices, normals, tangents, UVs). When this form of compression is enabled, vertex positions will be packed into an RGBA16UNORM attribute and scaled in the vertex shader. The normal and tangent will be packed into an RG16UNORM representing an axis, and a 16-bit float stored in the A-channel of the vertex. UVs will use 16-bit normalized floats instead of full 32-bit signed floats. When using this compression mode you must use either vertices, normals, and tangents or only vertices. You cannot use normals without tangents. Importers will automatically enable this compression if they can.


----



enum **BlendShapeMode**: [🔗<enum_Mesh_BlendShapeMode>]



[BlendShapeMode<enum_Mesh_BlendShapeMode>] **BLEND_SHAPE_MODE_NORMALIZED** = `0`

Blend shapes are normalized.



[BlendShapeMode<enum_Mesh_BlendShapeMode>] **BLEND_SHAPE_MODE_RELATIVE** = `1`

Blend shapes are relative to base weight.


----


## Property Descriptions



[Vector2i<class_Vector2i>] **lightmap_size_hint** = `Vector2i(0, 0)` [🔗<class_Mesh_property_lightmap_size_hint>]


- |void| **set_lightmap_size_hint**\ (\ value\: [Vector2i<class_Vector2i>]\ )
- [Vector2i<class_Vector2i>] **get_lightmap_size_hint**\ (\ )

Sets a hint to be used for lightmap resolution.


----


## Method Descriptions



[AABB<class_AABB>] **_get_aabb**\ (\ ) |virtual| |required| |const| [🔗<class_Mesh_private_method__get_aabb>]

Virtual method to override the [AABB<class_AABB>] for a custom class extending **Mesh**.


----



[int<class_int>] **_get_blend_shape_count**\ (\ ) |virtual| |required| |const| [🔗<class_Mesh_private_method__get_blend_shape_count>]

Virtual method to override the number of blend shapes for a custom class extending **Mesh**.


----



[StringName<class_StringName>] **_get_blend_shape_name**\ (\ index\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_Mesh_private_method__get_blend_shape_name>]

Virtual method to override the retrieval of blend shape names for a custom class extending **Mesh**.


----



[int<class_int>] **_get_surface_count**\ (\ ) |virtual| |required| |const| [🔗<class_Mesh_private_method__get_surface_count>]

Virtual method to override the surface count for a custom class extending **Mesh**.


----



|void| **_set_blend_shape_name**\ (\ index\: [int<class_int>], name\: [StringName<class_StringName>]\ ) |virtual| |required| [🔗<class_Mesh_private_method__set_blend_shape_name>]

Virtual method to override the names of blend shapes for a custom class extending **Mesh**.


----



[int<class_int>] **_surface_get_array_index_len**\ (\ index\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_Mesh_private_method__surface_get_array_index_len>]

Virtual method to override the surface array index length for a custom class extending **Mesh**.


----



[int<class_int>] **_surface_get_array_len**\ (\ index\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_Mesh_private_method__surface_get_array_len>]

Virtual method to override the surface array length for a custom class extending **Mesh**.


----



[Array<class_Array>] **_surface_get_arrays**\ (\ index\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_Mesh_private_method__surface_get_arrays>]

Virtual method to override the surface arrays for a custom class extending **Mesh**.


----



[Array<class_Array>]\[[Array<class_Array>]\] **_surface_get_blend_shape_arrays**\ (\ index\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_Mesh_private_method__surface_get_blend_shape_arrays>]

Virtual method to override the blend shape arrays for a custom class extending **Mesh**.


----



[int<class_int>] **_surface_get_format**\ (\ index\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_Mesh_private_method__surface_get_format>]

Virtual method to override the surface format for a custom class extending **Mesh**.


----



[Dictionary<class_Dictionary>] **_surface_get_lods**\ (\ index\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_Mesh_private_method__surface_get_lods>]

Virtual method to override the surface LODs for a custom class extending **Mesh**.


----



[Material<class_Material>] **_surface_get_material**\ (\ index\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_Mesh_private_method__surface_get_material>]

Virtual method to override the surface material for a custom class extending **Mesh**.


----



[int<class_int>] **_surface_get_primitive_type**\ (\ index\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_Mesh_private_method__surface_get_primitive_type>]

Virtual method to override the surface primitive type for a custom class extending **Mesh**.


----



|void| **_surface_set_material**\ (\ index\: [int<class_int>], material\: [Material<class_Material>]\ ) |virtual| |required| [🔗<class_Mesh_private_method__surface_set_material>]

Virtual method to override the setting of a `material` at the given `index` for a custom class extending **Mesh**.


----



[ConvexPolygonShape3D<class_ConvexPolygonShape3D>] **create_convex_shape**\ (\ clean\: [bool<class_bool>] = true, simplify\: [bool<class_bool>] = false\ ) |const| [🔗<class_Mesh_method_create_convex_shape>]

Calculate a [ConvexPolygonShape3D<class_ConvexPolygonShape3D>] from the mesh.

If `clean` is `true` (default), duplicate and interior vertices are removed automatically. You can set it to `false` to make the process faster if not needed.

If `simplify` is `true`, the geometry can be further simplified to reduce the number of vertices. Disabled by default.


----



[Mesh<class_Mesh>] **create_outline**\ (\ margin\: [float<class_float>]\ ) |const| [🔗<class_Mesh_method_create_outline>]

Calculate an outline mesh at a defined offset (margin) from the original mesh.

\ **Note:** This method typically returns the vertices in reverse order (e.g. clockwise to counterclockwise).


----



[Resource<class_Resource>] **create_placeholder**\ (\ ) |const| [🔗<class_Mesh_method_create_placeholder>]

Creates a placeholder version of this resource ([PlaceholderMesh<class_PlaceholderMesh>]).


----



[ConcavePolygonShape3D<class_ConcavePolygonShape3D>] **create_trimesh_shape**\ (\ ) |const| [🔗<class_Mesh_method_create_trimesh_shape>]

Calculate a [ConcavePolygonShape3D<class_ConcavePolygonShape3D>] from the mesh.


----



[TriangleMesh<class_TriangleMesh>] **generate_triangle_mesh**\ (\ ) |const| [🔗<class_Mesh_method_generate_triangle_mesh>]

Generate a [TriangleMesh<class_TriangleMesh>] from the mesh. Considers only surfaces using one of these primitive types: [PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>], [PRIMITIVE_TRIANGLE_STRIP<class_Mesh_constant_PRIMITIVE_TRIANGLE_STRIP>].


----



[AABB<class_AABB>] **get_aabb**\ (\ ) |const| [🔗<class_Mesh_method_get_aabb>]

Returns the smallest [AABB<class_AABB>] enclosing this mesh in local space. Not affected by `custom_aabb`.

\ **Note:** This is only implemented for [ArrayMesh<class_ArrayMesh>] and [PrimitiveMesh<class_PrimitiveMesh>].


----



[PackedVector3Array<class_PackedVector3Array>] **get_faces**\ (\ ) |const| [🔗<class_Mesh_method_get_faces>]

Returns all the vertices that make up the faces of the mesh. Each three vertices represent one triangle.


----



[int<class_int>] **get_surface_count**\ (\ ) |const| [🔗<class_Mesh_method_get_surface_count>]

Returns the number of surfaces that the **Mesh** holds. This is equivalent to [MeshInstance3D.get_surface_override_material_count()<class_MeshInstance3D_method_get_surface_override_material_count>].


----



[Array<class_Array>] **surface_get_arrays**\ (\ surf_idx\: [int<class_int>]\ ) |const| [🔗<class_Mesh_method_surface_get_arrays>]

Returns the arrays for the vertices, normals, UVs, etc. that make up the requested surface (see [ArrayMesh.add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>]).


----



[Array<class_Array>]\[[Array<class_Array>]\] **surface_get_blend_shape_arrays**\ (\ surf_idx\: [int<class_int>]\ ) |const| [🔗<class_Mesh_method_surface_get_blend_shape_arrays>]

Returns the blend shape arrays for the requested surface.


----



[Material<class_Material>] **surface_get_material**\ (\ surf_idx\: [int<class_int>]\ ) |const| [🔗<class_Mesh_method_surface_get_material>]

Returns a [Material<class_Material>] in a given surface. Surface is rendered using this material.

\ **Note:** This returns the material within the **Mesh** resource, not the [Material<class_Material>] associated to the [MeshInstance3D<class_MeshInstance3D>]'s Surface Material Override properties. To get the [Material<class_Material>] associated to the [MeshInstance3D<class_MeshInstance3D>]'s Surface Material Override properties, use [MeshInstance3D.get_surface_override_material()<class_MeshInstance3D_method_get_surface_override_material>] instead.


----



|void| **surface_set_material**\ (\ surf_idx\: [int<class_int>], material\: [Material<class_Material>]\ ) [🔗<class_Mesh_method_surface_set_material>]

Sets a [Material<class_Material>] for a given surface. Surface will be rendered using this material.

\ **Note:** This assigns the material within the **Mesh** resource, not the [Material<class_Material>] associated to the [MeshInstance3D<class_MeshInstance3D>]'s Surface Material Override properties. To set the [Material<class_Material>] associated to the [MeshInstance3D<class_MeshInstance3D>]'s Surface Material Override properties, use [MeshInstance3D.set_surface_override_material()<class_MeshInstance3D_method_set_surface_override_material>] instead.

