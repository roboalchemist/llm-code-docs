:github_url: hide



# MeshDataTool

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Helper tool to access and edit [Mesh<class_Mesh>] data.


## Description

MeshDataTool provides access to individual vertices in a [Mesh<class_Mesh>]. It allows users to read and edit vertex data of meshes. It also creates an array of faces and edges.

To use MeshDataTool, load a mesh with [create_from_surface()<class_MeshDataTool_method_create_from_surface>]. When you are finished editing the data commit the data to a mesh with [commit_to_surface()<class_MeshDataTool_method_commit_to_surface>].

Below is an example of how MeshDataTool may be used.


> **TABS**
>

    var mesh = ArrayMesh.new()
    mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, BoxMesh.new().get_mesh_arrays())
    var mdt = MeshDataTool.new()
    mdt.create_from_surface(mesh, 0)
    for i in range(mdt.get_vertex_count()):
        var vertex = mdt.get_vertex(i)
        # In this example we extend the mesh by one unit, which results in separated faces as it is flat shaded.
        vertex += mdt.get_vertex_normal(i)
        # Save your change.
        mdt.set_vertex(i, vertex)
    mesh.clear_surfaces()
    mdt.commit_to_surface(mesh)
    var mi = MeshInstance.new()
    mi.mesh = mesh
    add_child(mi)


    var mesh = new ArrayMesh();
    mesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, new BoxMesh().GetMeshArrays());
    var mdt = new MeshDataTool();
    mdt.CreateFromSurface(mesh, 0);
    for (var i = 0; i < mdt.GetVertexCount(); i++)
    {
        Vector3 vertex = mdt.GetVertex(i);
        // In this example we extend the mesh by one unit, which results in separated faces as it is flat shaded.
        vertex += mdt.GetVertexNormal(i);
        // Save your change.
        mdt.SetVertex(i, vertex);
    }
    mesh.ClearSurfaces();
    mdt.CommitToSurface(mesh);
    var mi = new MeshInstance();
    mi.Mesh = mesh;
    AddChild(mi);



See also [ArrayMesh<class_ArrayMesh>], [ImmediateMesh<class_ImmediateMesh>] and [SurfaceTool<class_SurfaceTool>] for procedural geometry generation.

\ **Note:** Godot uses clockwise [winding order ](https://learnopengl.com/Advanced-OpenGL/Face-culling)_ for front faces of triangle primitive modes.


## Tutorials

- [../tutorials/3d/procedural_geometry/meshdatatool](Using the MeshDataTool .md)


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`clear<class_MeshDataTool_method_clear>`\ (\ )                                                                                                                       |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`               | :ref:`commit_to_surface<class_MeshDataTool_method_commit_to_surface>`\ (\ mesh\: :ref:`ArrayMesh<class_ArrayMesh>`, compression_flags\: :ref:`int<class_int>` = 0\ )      |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`               | :ref:`create_from_surface<class_MeshDataTool_method_create_from_surface>`\ (\ mesh\: :ref:`ArrayMesh<class_ArrayMesh>`, surface\: :ref:`int<class_int>`\ )                |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_edge_count<class_MeshDataTool_method_get_edge_count>`\ (\ ) |const|                                                                                             |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`     | :ref:`get_edge_faces<class_MeshDataTool_method_get_edge_faces>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                       | :ref:`get_edge_meta<class_MeshDataTool_method_get_edge_meta>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                  |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_edge_vertex<class_MeshDataTool_method_get_edge_vertex>`\ (\ idx\: :ref:`int<class_int>`, vertex\: :ref:`int<class_int>`\ ) |const|                              |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_face_count<class_MeshDataTool_method_get_face_count>`\ (\ ) |const|                                                                                             |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_face_edge<class_MeshDataTool_method_get_face_edge>`\ (\ idx\: :ref:`int<class_int>`, edge\: :ref:`int<class_int>`\ ) |const|                                    |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                       | :ref:`get_face_meta<class_MeshDataTool_method_get_face_meta>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                  |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                       | :ref:`get_face_normal<class_MeshDataTool_method_get_face_normal>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                              |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_face_vertex<class_MeshDataTool_method_get_face_vertex>`\ (\ idx\: :ref:`int<class_int>`, vertex\: :ref:`int<class_int>`\ ) |const|                              |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_format<class_MeshDataTool_method_get_format>`\ (\ ) |const|                                                                                                     |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Material<class_Material>`                     | :ref:`get_material<class_MeshDataTool_method_get_material>`\ (\ ) |const|                                                                                                 |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                       | :ref:`get_vertex<class_MeshDataTool_method_get_vertex>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                        |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`     | :ref:`get_vertex_bones<class_MeshDataTool_method_get_vertex_bones>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                            |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>`                           | :ref:`get_vertex_color<class_MeshDataTool_method_get_vertex_color>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                            |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_vertex_count<class_MeshDataTool_method_get_vertex_count>`\ (\ ) |const|                                                                                         |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`     | :ref:`get_vertex_edges<class_MeshDataTool_method_get_vertex_edges>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                            |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`     | :ref:`get_vertex_faces<class_MeshDataTool_method_get_vertex_faces>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                            |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                       | :ref:`get_vertex_meta<class_MeshDataTool_method_get_vertex_meta>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                              |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                       | :ref:`get_vertex_normal<class_MeshDataTool_method_get_vertex_normal>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                          |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Plane<class_Plane>`                           | :ref:`get_vertex_tangent<class_MeshDataTool_method_get_vertex_tangent>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                        |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                       | :ref:`get_vertex_uv<class_MeshDataTool_method_get_vertex_uv>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                  |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                       | :ref:`get_vertex_uv2<class_MeshDataTool_method_get_vertex_uv2>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedFloat32Array<class_PackedFloat32Array>` | :ref:`get_vertex_weights<class_MeshDataTool_method_get_vertex_weights>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                        |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_edge_meta<class_MeshDataTool_method_set_edge_meta>`\ (\ idx\: :ref:`int<class_int>`, meta\: :ref:`Variant<class_Variant>`\ )                                    |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_face_meta<class_MeshDataTool_method_set_face_meta>`\ (\ idx\: :ref:`int<class_int>`, meta\: :ref:`Variant<class_Variant>`\ )                                    |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_material<class_MeshDataTool_method_set_material>`\ (\ material\: :ref:`Material<class_Material>`\ )                                                             |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_vertex<class_MeshDataTool_method_set_vertex>`\ (\ idx\: :ref:`int<class_int>`, vertex\: :ref:`Vector3<class_Vector3>`\ )                                        |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_vertex_bones<class_MeshDataTool_method_set_vertex_bones>`\ (\ idx\: :ref:`int<class_int>`, bones\: :ref:`PackedInt32Array<class_PackedInt32Array>`\ )           |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_vertex_color<class_MeshDataTool_method_set_vertex_color>`\ (\ idx\: :ref:`int<class_int>`, color\: :ref:`Color<class_Color>`\ )                                 |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_vertex_meta<class_MeshDataTool_method_set_vertex_meta>`\ (\ idx\: :ref:`int<class_int>`, meta\: :ref:`Variant<class_Variant>`\ )                                |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_vertex_normal<class_MeshDataTool_method_set_vertex_normal>`\ (\ idx\: :ref:`int<class_int>`, normal\: :ref:`Vector3<class_Vector3>`\ )                          |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_vertex_tangent<class_MeshDataTool_method_set_vertex_tangent>`\ (\ idx\: :ref:`int<class_int>`, tangent\: :ref:`Plane<class_Plane>`\ )                           |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_vertex_uv<class_MeshDataTool_method_set_vertex_uv>`\ (\ idx\: :ref:`int<class_int>`, uv\: :ref:`Vector2<class_Vector2>`\ )                                      |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_vertex_uv2<class_MeshDataTool_method_set_vertex_uv2>`\ (\ idx\: :ref:`int<class_int>`, uv2\: :ref:`Vector2<class_Vector2>`\ )                                   |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_vertex_weights<class_MeshDataTool_method_set_vertex_weights>`\ (\ idx\: :ref:`int<class_int>`, weights\: :ref:`PackedFloat32Array<class_PackedFloat32Array>`\ ) |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **clear**\ (\ ) [🔗<class_MeshDataTool_method_clear>]

Clears all data currently in MeshDataTool.


----



[Error<enum_@GlobalScope_Error>] **commit_to_surface**\ (\ mesh\: [ArrayMesh<class_ArrayMesh>], compression_flags\: [int<class_int>] = 0\ ) [🔗<class_MeshDataTool_method_commit_to_surface>]

Adds a new surface to specified [Mesh<class_Mesh>] with edited data.


----



[Error<enum_@GlobalScope_Error>] **create_from_surface**\ (\ mesh\: [ArrayMesh<class_ArrayMesh>], surface\: [int<class_int>]\ ) [🔗<class_MeshDataTool_method_create_from_surface>]

Uses specified surface of given [Mesh<class_Mesh>] to populate data for MeshDataTool.

Requires [Mesh<class_Mesh>] with primitive type [Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>].


----



[int<class_int>] **get_edge_count**\ (\ ) |const| [🔗<class_MeshDataTool_method_get_edge_count>]

Returns the number of edges in this [Mesh<class_Mesh>].


----



[PackedInt32Array<class_PackedInt32Array>] **get_edge_faces**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_edge_faces>]

Returns array of faces that touch given edge.


----



[Variant<class_Variant>] **get_edge_meta**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_edge_meta>]

Returns meta information assigned to given edge.


----



[int<class_int>] **get_edge_vertex**\ (\ idx\: [int<class_int>], vertex\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_edge_vertex>]

Returns the index of the specified `vertex` connected to the edge at index `idx`.

\ `vertex` can only be `0` or `1`, as edges are composed of two vertices.


----



[int<class_int>] **get_face_count**\ (\ ) |const| [🔗<class_MeshDataTool_method_get_face_count>]

Returns the number of faces in this [Mesh<class_Mesh>].


----



[int<class_int>] **get_face_edge**\ (\ idx\: [int<class_int>], edge\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_face_edge>]

Returns the edge associated with the face at index `idx`.

\ `edge` argument must be either `0`, `1`, or `2` because a face only has three edges.


----



[Variant<class_Variant>] **get_face_meta**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_face_meta>]

Returns the metadata associated with the given face.


----



[Vector3<class_Vector3>] **get_face_normal**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_face_normal>]

Calculates and returns the face normal of the given face.


----



[int<class_int>] **get_face_vertex**\ (\ idx\: [int<class_int>], vertex\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_face_vertex>]

Returns the specified vertex index of the given face.

\ `vertex` must be either `0`, `1`, or `2` because faces contain three vertices.


> **TABS**
>

    var index = mesh_data_tool.get_face_vertex(0, 1) # Gets the index of the second vertex of the first face.
    var position = mesh_data_tool.get_vertex(index)
    var normal = mesh_data_tool.get_vertex_normal(index)


    int index = meshDataTool.GetFaceVertex(0, 1); // Gets the index of the second vertex of the first face.
    Vector3 position = meshDataTool.GetVertex(index);
    Vector3 normal = meshDataTool.GetVertexNormal(index);




----



[int<class_int>] **get_format**\ (\ ) |const| [🔗<class_MeshDataTool_method_get_format>]

Returns the [Mesh<class_Mesh>]'s format as a combination of the [ArrayFormat<enum_Mesh_ArrayFormat>] flags. For example, a mesh containing both vertices and normals would return a format of `3` because [Mesh.ARRAY_FORMAT_VERTEX<class_Mesh_constant_ARRAY_FORMAT_VERTEX>] is `1` and [Mesh.ARRAY_FORMAT_NORMAL<class_Mesh_constant_ARRAY_FORMAT_NORMAL>] is `2`.


----



[Material<class_Material>] **get_material**\ (\ ) |const| [🔗<class_MeshDataTool_method_get_material>]

Returns the material assigned to the [Mesh<class_Mesh>].


----



[Vector3<class_Vector3>] **get_vertex**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_vertex>]

Returns the position of the given vertex.


----



[PackedInt32Array<class_PackedInt32Array>] **get_vertex_bones**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_vertex_bones>]

Returns the bones of the given vertex.


----



[Color<class_Color>] **get_vertex_color**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_vertex_color>]

Returns the color of the given vertex.


----



[int<class_int>] **get_vertex_count**\ (\ ) |const| [🔗<class_MeshDataTool_method_get_vertex_count>]

Returns the total number of vertices in [Mesh<class_Mesh>].


----



[PackedInt32Array<class_PackedInt32Array>] **get_vertex_edges**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_vertex_edges>]

Returns an array of edges that share the given vertex.


----



[PackedInt32Array<class_PackedInt32Array>] **get_vertex_faces**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_vertex_faces>]

Returns an array of faces that share the given vertex.


----



[Variant<class_Variant>] **get_vertex_meta**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_vertex_meta>]

Returns the metadata associated with the given vertex.


----



[Vector3<class_Vector3>] **get_vertex_normal**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_vertex_normal>]

Returns the normal of the given vertex.


----



[Plane<class_Plane>] **get_vertex_tangent**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_vertex_tangent>]

Returns the tangent of the given vertex.


----



[Vector2<class_Vector2>] **get_vertex_uv**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_vertex_uv>]

Returns the UV of the given vertex.


----



[Vector2<class_Vector2>] **get_vertex_uv2**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_vertex_uv2>]

Returns the UV2 of the given vertex.


----



[PackedFloat32Array<class_PackedFloat32Array>] **get_vertex_weights**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_MeshDataTool_method_get_vertex_weights>]

Returns bone weights of the given vertex.


----



|void| **set_edge_meta**\ (\ idx\: [int<class_int>], meta\: [Variant<class_Variant>]\ ) [🔗<class_MeshDataTool_method_set_edge_meta>]

Sets the metadata of the given edge.


----



|void| **set_face_meta**\ (\ idx\: [int<class_int>], meta\: [Variant<class_Variant>]\ ) [🔗<class_MeshDataTool_method_set_face_meta>]

Sets the metadata of the given face.


----



|void| **set_material**\ (\ material\: [Material<class_Material>]\ ) [🔗<class_MeshDataTool_method_set_material>]

Sets the material to be used by newly-constructed [Mesh<class_Mesh>].


----



|void| **set_vertex**\ (\ idx\: [int<class_int>], vertex\: [Vector3<class_Vector3>]\ ) [🔗<class_MeshDataTool_method_set_vertex>]

Sets the position of the given vertex.


----



|void| **set_vertex_bones**\ (\ idx\: [int<class_int>], bones\: [PackedInt32Array<class_PackedInt32Array>]\ ) [🔗<class_MeshDataTool_method_set_vertex_bones>]

Sets the bones of the given vertex.


----



|void| **set_vertex_color**\ (\ idx\: [int<class_int>], color\: [Color<class_Color>]\ ) [🔗<class_MeshDataTool_method_set_vertex_color>]

Sets the color of the given vertex.


----



|void| **set_vertex_meta**\ (\ idx\: [int<class_int>], meta\: [Variant<class_Variant>]\ ) [🔗<class_MeshDataTool_method_set_vertex_meta>]

Sets the metadata associated with the given vertex.


----



|void| **set_vertex_normal**\ (\ idx\: [int<class_int>], normal\: [Vector3<class_Vector3>]\ ) [🔗<class_MeshDataTool_method_set_vertex_normal>]

Sets the normal of the given vertex.


----



|void| **set_vertex_tangent**\ (\ idx\: [int<class_int>], tangent\: [Plane<class_Plane>]\ ) [🔗<class_MeshDataTool_method_set_vertex_tangent>]

Sets the tangent of the given vertex.

\ **Note:** Even though `tangent` is a [Plane<class_Plane>], it does not directly represent the tangent plane. Its [Plane.x<class_Plane_property_x>], [Plane.y<class_Plane_property_y>], and [Plane.z<class_Plane_property_z>] represent the tangent vector and [Plane.d<class_Plane_property_d>] should be either `-1` or `1`. See also [Mesh.ARRAY_TANGENT<class_Mesh_constant_ARRAY_TANGENT>].


----



|void| **set_vertex_uv**\ (\ idx\: [int<class_int>], uv\: [Vector2<class_Vector2>]\ ) [🔗<class_MeshDataTool_method_set_vertex_uv>]

Sets the UV of the given vertex.


----



|void| **set_vertex_uv2**\ (\ idx\: [int<class_int>], uv2\: [Vector2<class_Vector2>]\ ) [🔗<class_MeshDataTool_method_set_vertex_uv2>]

Sets the UV2 of the given vertex.


----



|void| **set_vertex_weights**\ (\ idx\: [int<class_int>], weights\: [PackedFloat32Array<class_PackedFloat32Array>]\ ) [🔗<class_MeshDataTool_method_set_vertex_weights>]

Sets the bone weights of the given vertex.

