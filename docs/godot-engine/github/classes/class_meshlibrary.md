:github_url: hide



# MeshLibrary

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Library of meshes.


## Description

A library of meshes. Contains a list of [Mesh<class_Mesh>] resources, each with a name and ID. Each item can also include collision and navigation shapes. This resource is used in [GridMap<class_GridMap>].


## Tutorials

- [3D Kinematic Character Demo ](https://godotengine.org/asset-library/asset/2739)_

- [3D Platformer Demo ](https://godotengine.org/asset-library/asset/2748)_


## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`clear<class_MeshLibrary_method_clear>`\ (\ )                                                                                                                                                                      |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`create_item<class_MeshLibrary_method_create_item>`\ (\ id\: :ref:`int<class_int>`\ )                                                                                                                              |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                  | :ref:`find_item_by_name<class_MeshLibrary_method_find_item_by_name>`\ (\ name\: :ref:`String<class_String>`\ ) |const|                                                                                                  |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`                        | :ref:`get_item_list<class_MeshLibrary_method_get_item_list>`\ (\ ) |const|                                                                                                                                              |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Mesh<class_Mesh>`                                                | :ref:`get_item_mesh<class_MeshLibrary_method_get_item_mesh>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                                                                                  |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ShadowCastingSetting<enum_RenderingServer_ShadowCastingSetting>` | :ref:`get_item_mesh_cast_shadow<class_MeshLibrary_method_get_item_mesh_cast_shadow>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                                                          |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                                  | :ref:`get_item_mesh_transform<class_MeshLibrary_method_get_item_mesh_transform>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                                                              |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                            | :ref:`get_item_name<class_MeshLibrary_method_get_item_name>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                                                                                  |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                  | :ref:`get_item_navigation_layers<class_MeshLibrary_method_get_item_navigation_layers>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                                                        |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`NavigationMesh<class_NavigationMesh>`                            | :ref:`get_item_navigation_mesh<class_MeshLibrary_method_get_item_navigation_mesh>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                                                            |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                                  | :ref:`get_item_navigation_mesh_transform<class_MeshLibrary_method_get_item_navigation_mesh_transform>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                                        |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>`                                      | :ref:`get_item_preview<class_MeshLibrary_method_get_item_preview>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                                                                            |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                                              | :ref:`get_item_shapes<class_MeshLibrary_method_get_item_shapes>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                                                                              |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                  | :ref:`get_last_unused_item_id<class_MeshLibrary_method_get_last_unused_item_id>`\ (\ ) |const|                                                                                                                          |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`remove_item<class_MeshLibrary_method_remove_item>`\ (\ id\: :ref:`int<class_int>`\ )                                                                                                                              |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_item_mesh<class_MeshLibrary_method_set_item_mesh>`\ (\ id\: :ref:`int<class_int>`, mesh\: :ref:`Mesh<class_Mesh>`\ )                                                                                          |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_item_mesh_cast_shadow<class_MeshLibrary_method_set_item_mesh_cast_shadow>`\ (\ id\: :ref:`int<class_int>`, shadow_casting_setting\: :ref:`ShadowCastingSetting<enum_RenderingServer_ShadowCastingSetting>`\ ) |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_item_mesh_transform<class_MeshLibrary_method_set_item_mesh_transform>`\ (\ id\: :ref:`int<class_int>`, mesh_transform\: :ref:`Transform3D<class_Transform3D>`\ )                                              |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_item_name<class_MeshLibrary_method_set_item_name>`\ (\ id\: :ref:`int<class_int>`, name\: :ref:`String<class_String>`\ )                                                                                      |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_item_navigation_layers<class_MeshLibrary_method_set_item_navigation_layers>`\ (\ id\: :ref:`int<class_int>`, navigation_layers\: :ref:`int<class_int>`\ )                                                     |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_item_navigation_mesh<class_MeshLibrary_method_set_item_navigation_mesh>`\ (\ id\: :ref:`int<class_int>`, navigation_mesh\: :ref:`NavigationMesh<class_NavigationMesh>`\ )                                     |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_item_navigation_mesh_transform<class_MeshLibrary_method_set_item_navigation_mesh_transform>`\ (\ id\: :ref:`int<class_int>`, navigation_mesh\: :ref:`Transform3D<class_Transform3D>`\ )                       |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_item_preview<class_MeshLibrary_method_set_item_preview>`\ (\ id\: :ref:`int<class_int>`, texture\: :ref:`Texture2D<class_Texture2D>`\ )                                                                       |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_item_shapes<class_MeshLibrary_method_set_item_shapes>`\ (\ id\: :ref:`int<class_int>`, shapes\: :ref:`Array<class_Array>`\ )                                                                                  |
> +------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **clear**\ (\ ) [🔗<class_MeshLibrary_method_clear>]

Clears the library.


----



|void| **create_item**\ (\ id\: [int<class_int>]\ ) [🔗<class_MeshLibrary_method_create_item>]

Creates a new item in the library with the given ID.

You can get an unused ID from [get_last_unused_item_id()<class_MeshLibrary_method_get_last_unused_item_id>].


----



[int<class_int>] **find_item_by_name**\ (\ name\: [String<class_String>]\ ) |const| [🔗<class_MeshLibrary_method_find_item_by_name>]

Returns the first item with the given name, or `-1` if no item is found.


----



[PackedInt32Array<class_PackedInt32Array>] **get_item_list**\ (\ ) |const| [🔗<class_MeshLibrary_method_get_item_list>]

Returns the list of item IDs in use.


----



[Mesh<class_Mesh>] **get_item_mesh**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_MeshLibrary_method_get_item_mesh>]

Returns the item's mesh.


----



[ShadowCastingSetting<enum_RenderingServer_ShadowCastingSetting>] **get_item_mesh_cast_shadow**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_MeshLibrary_method_get_item_mesh_cast_shadow>]

Returns the item's shadow casting mode.


----



[Transform3D<class_Transform3D>] **get_item_mesh_transform**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_MeshLibrary_method_get_item_mesh_transform>]

Returns the transform applied to the item's mesh.


----



[String<class_String>] **get_item_name**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_MeshLibrary_method_get_item_name>]

Returns the item's name.


----



[int<class_int>] **get_item_navigation_layers**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_MeshLibrary_method_get_item_navigation_layers>]

Returns the item's navigation layers bitmask.


----



[NavigationMesh<class_NavigationMesh>] **get_item_navigation_mesh**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_MeshLibrary_method_get_item_navigation_mesh>]

Returns the item's navigation mesh.


----



[Transform3D<class_Transform3D>] **get_item_navigation_mesh_transform**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_MeshLibrary_method_get_item_navigation_mesh_transform>]

Returns the transform applied to the item's navigation mesh.


----



[Texture2D<class_Texture2D>] **get_item_preview**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_MeshLibrary_method_get_item_preview>]

When running in the editor, returns a generated item preview (a 3D rendering in isometric perspective). When used in a running project, returns the manually-defined item preview which can be set using [set_item_preview()<class_MeshLibrary_method_set_item_preview>]. Returns an empty [Texture2D<class_Texture2D>] if no preview was manually set in a running project.


----



[Array<class_Array>] **get_item_shapes**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_MeshLibrary_method_get_item_shapes>]

Returns an item's collision shapes.

The array consists of each [Shape3D<class_Shape3D>] followed by its [Transform3D<class_Transform3D>].


----



[int<class_int>] **get_last_unused_item_id**\ (\ ) |const| [🔗<class_MeshLibrary_method_get_last_unused_item_id>]

Gets an unused ID for a new item.


----



|void| **remove_item**\ (\ id\: [int<class_int>]\ ) [🔗<class_MeshLibrary_method_remove_item>]

Removes the item.


----



|void| **set_item_mesh**\ (\ id\: [int<class_int>], mesh\: [Mesh<class_Mesh>]\ ) [🔗<class_MeshLibrary_method_set_item_mesh>]

Sets the item's mesh.


----



|void| **set_item_mesh_cast_shadow**\ (\ id\: [int<class_int>], shadow_casting_setting\: [ShadowCastingSetting<enum_RenderingServer_ShadowCastingSetting>]\ ) [🔗<class_MeshLibrary_method_set_item_mesh_cast_shadow>]

Sets the item's shadow casting mode to `shadow_casting_setting`.


----



|void| **set_item_mesh_transform**\ (\ id\: [int<class_int>], mesh_transform\: [Transform3D<class_Transform3D>]\ ) [🔗<class_MeshLibrary_method_set_item_mesh_transform>]

Sets the transform to apply to the item's mesh.


----



|void| **set_item_name**\ (\ id\: [int<class_int>], name\: [String<class_String>]\ ) [🔗<class_MeshLibrary_method_set_item_name>]

Sets the item's name.

This name is shown in the editor. It can also be used to look up the item later using [find_item_by_name()<class_MeshLibrary_method_find_item_by_name>].


----



|void| **set_item_navigation_layers**\ (\ id\: [int<class_int>], navigation_layers\: [int<class_int>]\ ) [🔗<class_MeshLibrary_method_set_item_navigation_layers>]

Sets the item's navigation layers bitmask.


----



|void| **set_item_navigation_mesh**\ (\ id\: [int<class_int>], navigation_mesh\: [NavigationMesh<class_NavigationMesh>]\ ) [🔗<class_MeshLibrary_method_set_item_navigation_mesh>]

Sets the item's navigation mesh.


----



|void| **set_item_navigation_mesh_transform**\ (\ id\: [int<class_int>], navigation_mesh\: [Transform3D<class_Transform3D>]\ ) [🔗<class_MeshLibrary_method_set_item_navigation_mesh_transform>]

Sets the transform to apply to the item's navigation mesh.


----



|void| **set_item_preview**\ (\ id\: [int<class_int>], texture\: [Texture2D<class_Texture2D>]\ ) [🔗<class_MeshLibrary_method_set_item_preview>]

Sets a texture to use as the item's preview icon in the editor.


----



|void| **set_item_shapes**\ (\ id\: [int<class_int>], shapes\: [Array<class_Array>]\ ) [🔗<class_MeshLibrary_method_set_item_shapes>]

Sets an item's collision shapes.

The array should consist of [Shape3D<class_Shape3D>] objects, each followed by a [Transform3D<class_Transform3D>] that will be applied to it. For shapes that should not have a transform, use [Transform3D.IDENTITY<class_Transform3D_constant_IDENTITY>].

