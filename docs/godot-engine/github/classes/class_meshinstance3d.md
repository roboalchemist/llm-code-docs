:github_url: hide



# MeshInstance3D

**Inherits:** [GeometryInstance3D<class_GeometryInstance3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [SoftBody3D<class_SoftBody3D>]

Node that instances meshes into a scenario.


## Description

MeshInstance3D is a node that takes a [Mesh<class_Mesh>] resource and adds it to the current scenario by creating an instance of it. This is the class most often used to render 3D geometry and can be used to instance a single [Mesh<class_Mesh>] in many places. This allows reusing geometry, which can save on resources. When a [Mesh<class_Mesh>] has to be instantiated more than thousands of times at close proximity, consider using a [MultiMesh<class_MultiMesh>] in a [MultiMeshInstance3D<class_MultiMeshInstance3D>] instead.


## Tutorials

- [3D Material Testers Demo ](https://godotengine.org/asset-library/asset/2742)_

- [3D Kinematic Character Demo ](https://godotengine.org/asset-library/asset/2739)_

- [3D Platformer Demo ](https://godotengine.org/asset-library/asset/2748)_

- [Third Person Shooter (TPS) Demo ](https://godotengine.org/asset-library/asset/2710)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+---------------------------------------------------------+------------------+
> | :ref:`Mesh<class_Mesh>`         | :ref:`mesh<class_MeshInstance3D_property_mesh>`         |                  |
> +---------------------------------+---------------------------------------------------------+------------------+
> | :ref:`NodePath<class_NodePath>` | :ref:`skeleton<class_MeshInstance3D_property_skeleton>` | ``NodePath("")`` |
> +---------------------------------+---------------------------------------------------------+------------------+
> | :ref:`Skin<class_Skin>`         | :ref:`skin<class_MeshInstance3D_property_skin>`         |                  |
> +---------------------------------+---------------------------------------------------------+------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ArrayMesh<class_ArrayMesh>`         | :ref:`bake_mesh_from_current_blend_shape_mix<class_MeshInstance3D_method_bake_mesh_from_current_blend_shape_mix>`\ (\ existing\: :ref:`ArrayMesh<class_ArrayMesh>` = null\ )                                   |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ArrayMesh<class_ArrayMesh>`         | :ref:`bake_mesh_from_current_skeleton_pose<class_MeshInstance3D_method_bake_mesh_from_current_skeleton_pose>`\ (\ existing\: :ref:`ArrayMesh<class_ArrayMesh>` = null\ )                                       |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`create_convex_collision<class_MeshInstance3D_method_create_convex_collision>`\ (\ clean\: :ref:`bool<class_bool>` = true, simplify\: :ref:`bool<class_bool>` = false\ )                                  |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`create_debug_tangents<class_MeshInstance3D_method_create_debug_tangents>`\ (\ )                                                                                                                          |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`create_multiple_convex_collisions<class_MeshInstance3D_method_create_multiple_convex_collisions>`\ (\ settings\: :ref:`MeshConvexDecompositionSettings<class_MeshConvexDecompositionSettings>` = null\ ) |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`create_trimesh_collision<class_MeshInstance3D_method_create_trimesh_collision>`\ (\ )                                                                                                                    |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                     | :ref:`find_blend_shape_by_name<class_MeshInstance3D_method_find_blend_shape_by_name>`\ (\ name\: :ref:`StringName<class_StringName>`\ )                                                                        |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Material<class_Material>`           | :ref:`get_active_material<class_MeshInstance3D_method_get_active_material>`\ (\ surface\: :ref:`int<class_int>`\ ) |const|                                                                                     |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                     | :ref:`get_blend_shape_count<class_MeshInstance3D_method_get_blend_shape_count>`\ (\ ) |const|                                                                                                                  |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                 | :ref:`get_blend_shape_value<class_MeshInstance3D_method_get_blend_shape_value>`\ (\ blend_shape_idx\: :ref:`int<class_int>`\ ) |const|                                                                         |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`SkinReference<class_SkinReference>` | :ref:`get_skin_reference<class_MeshInstance3D_method_get_skin_reference>`\ (\ ) |const|                                                                                                                        |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Material<class_Material>`           | :ref:`get_surface_override_material<class_MeshInstance3D_method_get_surface_override_material>`\ (\ surface\: :ref:`int<class_int>`\ ) |const|                                                                 |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                     | :ref:`get_surface_override_material_count<class_MeshInstance3D_method_get_surface_override_material_count>`\ (\ ) |const|                                                                                      |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`set_blend_shape_value<class_MeshInstance3D_method_set_blend_shape_value>`\ (\ blend_shape_idx\: :ref:`int<class_int>`, value\: :ref:`float<class_float>`\ )                                              |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`set_surface_override_material<class_MeshInstance3D_method_set_surface_override_material>`\ (\ surface\: :ref:`int<class_int>`, material\: :ref:`Material<class_Material>`\ )                             |
> +-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Mesh<class_Mesh>] **mesh** [🔗<class_MeshInstance3D_property_mesh>]


- |void| **set_mesh**\ (\ value\: [Mesh<class_Mesh>]\ )
- [Mesh<class_Mesh>] **get_mesh**\ (\ )

The [Mesh<class_Mesh>] resource for the instance.


----



[NodePath<class_NodePath>] **skeleton** = `NodePath("")` [🔗<class_MeshInstance3D_property_skeleton>]


- |void| **set_skeleton_path**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_skeleton_path**\ (\ )

[NodePath<class_NodePath>] to the [Skeleton3D<class_Skeleton3D>] associated with the instance.

\ **Note:** The default value of this property has changed in Godot 4.6. Enable [ProjectSettings.animation/compatibility/default_parent_skeleton_in_mesh_instance_3d<class_ProjectSettings_property_animation/compatibility/default_parent_skeleton_in_mesh_instance_3d>] if the old behavior is needed for compatibility.


----



[Skin<class_Skin>] **skin** [🔗<class_MeshInstance3D_property_skin>]


- |void| **set_skin**\ (\ value\: [Skin<class_Skin>]\ )
- [Skin<class_Skin>] **get_skin**\ (\ )

The [Skin<class_Skin>] to be used by this instance.


----


## Method Descriptions



[ArrayMesh<class_ArrayMesh>] **bake_mesh_from_current_blend_shape_mix**\ (\ existing\: [ArrayMesh<class_ArrayMesh>] = null\ ) [🔗<class_MeshInstance3D_method_bake_mesh_from_current_blend_shape_mix>]

Takes a snapshot from the current [ArrayMesh<class_ArrayMesh>] with all blend shapes applied according to their current weights and bakes it to the provided `existing` mesh. If no `existing` mesh is provided a new [ArrayMesh<class_ArrayMesh>] is created, baked and returned. Mesh surface materials are not copied.

\ **Performance:** [Mesh<class_Mesh>] data needs to be received from the GPU, stalling the [RenderingServer<class_RenderingServer>] in the process.


----



[ArrayMesh<class_ArrayMesh>] **bake_mesh_from_current_skeleton_pose**\ (\ existing\: [ArrayMesh<class_ArrayMesh>] = null\ ) [🔗<class_MeshInstance3D_method_bake_mesh_from_current_skeleton_pose>]

Takes a snapshot of the current animated skeleton pose of the skinned mesh and bakes it to the provided `existing` mesh. If no `existing` mesh is provided a new [ArrayMesh<class_ArrayMesh>] is created, baked, and returned. Requires a skeleton with a registered skin to work. Blendshapes are ignored. Mesh surface materials are not copied.

\ **Performance:** [Mesh<class_Mesh>] data needs to be retrieved from the GPU, stalling the [RenderingServer<class_RenderingServer>] in the process.


----



|void| **create_convex_collision**\ (\ clean\: [bool<class_bool>] = true, simplify\: [bool<class_bool>] = false\ ) [🔗<class_MeshInstance3D_method_create_convex_collision>]

This helper creates a [StaticBody3D<class_StaticBody3D>] child node with a [ConvexPolygonShape3D<class_ConvexPolygonShape3D>] collision shape calculated from the mesh geometry. It's mainly used for testing.

If `clean` is `true` (default), duplicate and interior vertices are removed automatically. You can set it to `false` to make the process faster if not needed.

If `simplify` is `true`, the geometry can be further simplified to reduce the number of vertices. Disabled by default.


----



|void| **create_debug_tangents**\ (\ ) [🔗<class_MeshInstance3D_method_create_debug_tangents>]

This helper creates a **MeshInstance3D** child node with gizmos at every vertex calculated from the mesh geometry. It's mainly used for testing.


----



|void| **create_multiple_convex_collisions**\ (\ settings\: [MeshConvexDecompositionSettings<class_MeshConvexDecompositionSettings>] = null\ ) [🔗<class_MeshInstance3D_method_create_multiple_convex_collisions>]

This helper creates a [StaticBody3D<class_StaticBody3D>] child node with multiple [ConvexPolygonShape3D<class_ConvexPolygonShape3D>] collision shapes calculated from the mesh geometry via convex decomposition. The convex decomposition operation can be controlled with parameters from the optional `settings`.


----



|void| **create_trimesh_collision**\ (\ ) [🔗<class_MeshInstance3D_method_create_trimesh_collision>]

This helper creates a [StaticBody3D<class_StaticBody3D>] child node with a [ConcavePolygonShape3D<class_ConcavePolygonShape3D>] collision shape calculated from the mesh geometry. It's mainly used for testing.


----



[int<class_int>] **find_blend_shape_by_name**\ (\ name\: [StringName<class_StringName>]\ ) [🔗<class_MeshInstance3D_method_find_blend_shape_by_name>]

Returns the index of the blend shape with the given `name`. Returns `-1` if no blend shape with this name exists, including when [mesh<class_MeshInstance3D_property_mesh>] is `null`.


----



[Material<class_Material>] **get_active_material**\ (\ surface\: [int<class_int>]\ ) |const| [🔗<class_MeshInstance3D_method_get_active_material>]

Returns the [Material<class_Material>] that will be used by the [Mesh<class_Mesh>] when drawing. This can return the [GeometryInstance3D.material_override<class_GeometryInstance3D_property_material_override>], the surface override [Material<class_Material>] defined in this **MeshInstance3D**, or the surface [Material<class_Material>] defined in the [mesh<class_MeshInstance3D_property_mesh>]. For example, if [GeometryInstance3D.material_override<class_GeometryInstance3D_property_material_override>] is used, all surfaces will return the override material.

Returns `null` if no material is active, including when [mesh<class_MeshInstance3D_property_mesh>] is `null`.


----



[int<class_int>] **get_blend_shape_count**\ (\ ) |const| [🔗<class_MeshInstance3D_method_get_blend_shape_count>]

Returns the number of blend shapes available. Produces an error if [mesh<class_MeshInstance3D_property_mesh>] is `null`.


----



[float<class_float>] **get_blend_shape_value**\ (\ blend_shape_idx\: [int<class_int>]\ ) |const| [🔗<class_MeshInstance3D_method_get_blend_shape_value>]

Returns the value of the blend shape at the given `blend_shape_idx`. Returns `0.0` and produces an error if [mesh<class_MeshInstance3D_property_mesh>] is `null` or doesn't have a blend shape at that index.


----



[SkinReference<class_SkinReference>] **get_skin_reference**\ (\ ) |const| [🔗<class_MeshInstance3D_method_get_skin_reference>]

Returns the internal [SkinReference<class_SkinReference>] containing the skeleton's [RID<class_RID>] attached to this RID. See also [Resource.get_rid()<class_Resource_method_get_rid>], [SkinReference.get_skeleton()<class_SkinReference_method_get_skeleton>], and [RenderingServer.instance_attach_skeleton()<class_RenderingServer_method_instance_attach_skeleton>].


----



[Material<class_Material>] **get_surface_override_material**\ (\ surface\: [int<class_int>]\ ) |const| [🔗<class_MeshInstance3D_method_get_surface_override_material>]

Returns the override [Material<class_Material>] for the specified `surface` of the [Mesh<class_Mesh>] resource. See also [get_surface_override_material_count()<class_MeshInstance3D_method_get_surface_override_material_count>].

\ **Note:** This returns the [Material<class_Material>] associated to the **MeshInstance3D**'s Surface Material Override properties, not the material within the [Mesh<class_Mesh>] resource. To get the material within the [Mesh<class_Mesh>] resource, use [Mesh.surface_get_material()<class_Mesh_method_surface_get_material>] instead.


----



[int<class_int>] **get_surface_override_material_count**\ (\ ) |const| [🔗<class_MeshInstance3D_method_get_surface_override_material_count>]

Returns the number of surface override materials. This is equivalent to [Mesh.get_surface_count()<class_Mesh_method_get_surface_count>]. See also [get_surface_override_material()<class_MeshInstance3D_method_get_surface_override_material>].


----



|void| **set_blend_shape_value**\ (\ blend_shape_idx\: [int<class_int>], value\: [float<class_float>]\ ) [🔗<class_MeshInstance3D_method_set_blend_shape_value>]

Sets the value of the blend shape at `blend_shape_idx` to `value`. Produces an error if [mesh<class_MeshInstance3D_property_mesh>] is `null` or doesn't have a blend shape at that index.


----



|void| **set_surface_override_material**\ (\ surface\: [int<class_int>], material\: [Material<class_Material>]\ ) [🔗<class_MeshInstance3D_method_set_surface_override_material>]

Sets the override `material` for the specified `surface` of the [Mesh<class_Mesh>] resource. This material is associated with this **MeshInstance3D** rather than with [mesh<class_MeshInstance3D_property_mesh>].

\ **Note:** This assigns the [Material<class_Material>] associated to the **MeshInstance3D**'s Surface Material Override properties, not the material within the [Mesh<class_Mesh>] resource. To set the material within the [Mesh<class_Mesh>] resource, use [Mesh.surface_set_material()<class_Mesh_method_surface_set_material>] instead.

