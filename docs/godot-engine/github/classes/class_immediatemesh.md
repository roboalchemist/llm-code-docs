:github_url: hide



# ImmediateMesh

**Inherits:** [Mesh<class_Mesh>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Mesh optimized for creating geometry manually.


## Description

A mesh type optimized for creating geometry manually, similar to OpenGL 1.x immediate mode.

Here's a sample on how to generate a triangular face:


> **TABS**
>

    var mesh = ImmediateMesh.new()
    mesh.surface_begin(Mesh.PRIMITIVE_TRIANGLES)
    mesh.surface_add_vertex(Vector3.LEFT)
    mesh.surface_add_vertex(Vector3.FORWARD)
    mesh.surface_add_vertex(Vector3.ZERO)
    mesh.surface_end()


    var mesh = new ImmediateMesh();
    mesh.SurfaceBegin(Mesh.PrimitiveType.Triangles);
    mesh.SurfaceAddVertex(Vector3.Left);
    mesh.SurfaceAddVertex(Vector3.Forward);
    mesh.SurfaceAddVertex(Vector3.Zero);
    mesh.SurfaceEnd();



\ **Note:** Generating complex geometries with **ImmediateMesh** is highly inefficient. Instead, it is designed to generate simple geometry that changes often.


## Tutorials

- [../tutorials/3d/procedural_geometry/immediatemesh](Using ImmediateMesh .md)


## Methods

> **TABLE**
> :widths: auto
>
> +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`clear_surfaces<class_ImmediateMesh_method_clear_surfaces>`\ (\ )                                                                                                             |
> +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`surface_add_vertex<class_ImmediateMesh_method_surface_add_vertex>`\ (\ vertex\: :ref:`Vector3<class_Vector3>`\ )                                                             |
> +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`surface_add_vertex_2d<class_ImmediateMesh_method_surface_add_vertex_2d>`\ (\ vertex\: :ref:`Vector2<class_Vector2>`\ )                                                       |
> +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`surface_begin<class_ImmediateMesh_method_surface_begin>`\ (\ primitive\: :ref:`PrimitiveType<enum_Mesh_PrimitiveType>`, material\: :ref:`Material<class_Material>` = null\ ) |
> +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`surface_end<class_ImmediateMesh_method_surface_end>`\ (\ )                                                                                                                   |
> +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`surface_set_color<class_ImmediateMesh_method_surface_set_color>`\ (\ color\: :ref:`Color<class_Color>`\ )                                                                    |
> +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`surface_set_normal<class_ImmediateMesh_method_surface_set_normal>`\ (\ normal\: :ref:`Vector3<class_Vector3>`\ )                                                             |
> +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`surface_set_tangent<class_ImmediateMesh_method_surface_set_tangent>`\ (\ tangent\: :ref:`Plane<class_Plane>`\ )                                                              |
> +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`surface_set_uv<class_ImmediateMesh_method_surface_set_uv>`\ (\ uv\: :ref:`Vector2<class_Vector2>`\ )                                                                         |
> +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`surface_set_uv2<class_ImmediateMesh_method_surface_set_uv2>`\ (\ uv2\: :ref:`Vector2<class_Vector2>`\ )                                                                      |
> +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **clear_surfaces**\ (\ ) [🔗<class_ImmediateMesh_method_clear_surfaces>]

Clear all surfaces.


----



|void| **surface_add_vertex**\ (\ vertex\: [Vector3<class_Vector3>]\ ) [🔗<class_ImmediateMesh_method_surface_add_vertex>]

Add a 3D vertex using the current attributes previously set.


----



|void| **surface_add_vertex_2d**\ (\ vertex\: [Vector2<class_Vector2>]\ ) [🔗<class_ImmediateMesh_method_surface_add_vertex_2d>]

Add a 2D vertex using the current attributes previously set.


----



|void| **surface_begin**\ (\ primitive\: [PrimitiveType<enum_Mesh_PrimitiveType>], material\: [Material<class_Material>] = null\ ) [🔗<class_ImmediateMesh_method_surface_begin>]

Begin a new surface.


----



|void| **surface_end**\ (\ ) [🔗<class_ImmediateMesh_method_surface_end>]

End and commit current surface. Note that surface being created will not be visible until this function is called.


----



|void| **surface_set_color**\ (\ color\: [Color<class_Color>]\ ) [🔗<class_ImmediateMesh_method_surface_set_color>]

Set the color attribute that will be pushed with the next vertex.


----



|void| **surface_set_normal**\ (\ normal\: [Vector3<class_Vector3>]\ ) [🔗<class_ImmediateMesh_method_surface_set_normal>]

Set the normal attribute that will be pushed with the next vertex.


----



|void| **surface_set_tangent**\ (\ tangent\: [Plane<class_Plane>]\ ) [🔗<class_ImmediateMesh_method_surface_set_tangent>]

Set the tangent attribute that will be pushed with the next vertex.

\ **Note:** Even though `tangent` is a [Plane<class_Plane>], it does not directly represent the tangent plane. Its [Plane.x<class_Plane_property_x>], [Plane.y<class_Plane_property_y>], and [Plane.z<class_Plane_property_z>] represent the tangent vector and [Plane.d<class_Plane_property_d>] should be either `-1` or `1`. See also [Mesh.ARRAY_TANGENT<class_Mesh_constant_ARRAY_TANGENT>].


----



|void| **surface_set_uv**\ (\ uv\: [Vector2<class_Vector2>]\ ) [🔗<class_ImmediateMesh_method_surface_set_uv>]

Set the UV attribute that will be pushed with the next vertex.


----



|void| **surface_set_uv2**\ (\ uv2\: [Vector2<class_Vector2>]\ ) [🔗<class_ImmediateMesh_method_surface_set_uv2>]

Set the UV2 attribute that will be pushed with the next vertex.

