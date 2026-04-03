:github_url: hide



# PhysicsServer3DRenderingServerHandler

**Inherits:** [Object<class_Object>]

A class used to provide [PhysicsServer3DExtension._soft_body_update_rendering_server()<class_PhysicsServer3DExtension_private_method__soft_body_update_rendering_server>] with a rendering handler for soft bodies.


## Methods

> **TABLE**
> :widths: auto
>
> +--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_set_aabb<class_PhysicsServer3DRenderingServerHandler_private_method__set_aabb>`\ (\ aabb\: :ref:`AABB<class_AABB>`\ ) |virtual| |required|                                                |
> +--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_set_normal<class_PhysicsServer3DRenderingServerHandler_private_method__set_normal>`\ (\ vertex_id\: :ref:`int<class_int>`, normal\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required| |
> +--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_set_vertex<class_PhysicsServer3DRenderingServerHandler_private_method__set_vertex>`\ (\ vertex_id\: :ref:`int<class_int>`, vertex\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required| |
> +--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`set_aabb<class_PhysicsServer3DRenderingServerHandler_method_set_aabb>`\ (\ aabb\: :ref:`AABB<class_AABB>`\ )                                                                               |
> +--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`set_normal<class_PhysicsServer3DRenderingServerHandler_method_set_normal>`\ (\ vertex_id\: :ref:`int<class_int>`, normal\: :ref:`Vector3<class_Vector3>`\ )                                |
> +--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`set_vertex<class_PhysicsServer3DRenderingServerHandler_method_set_vertex>`\ (\ vertex_id\: :ref:`int<class_int>`, vertex\: :ref:`Vector3<class_Vector3>`\ )                                |
> +--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **_set_aabb**\ (\ aabb\: [AABB<class_AABB>]\ ) |virtual| |required| [🔗<class_PhysicsServer3DRenderingServerHandler_private_method__set_aabb>]

Called by the [PhysicsServer3D<class_PhysicsServer3D>] to set the bounding box for the [SoftBody3D<class_SoftBody3D>].


----



|void| **_set_normal**\ (\ vertex_id\: [int<class_int>], normal\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsServer3DRenderingServerHandler_private_method__set_normal>]

Called by the [PhysicsServer3D<class_PhysicsServer3D>] to set the normal for the [SoftBody3D<class_SoftBody3D>] vertex at the index specified by `vertex_id`.

\ **Note:** The `normal` parameter used to be of type `const void*` prior to Godot 4.2.


----



|void| **_set_vertex**\ (\ vertex_id\: [int<class_int>], vertex\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsServer3DRenderingServerHandler_private_method__set_vertex>]

Called by the [PhysicsServer3D<class_PhysicsServer3D>] to set the position for the [SoftBody3D<class_SoftBody3D>] vertex at the index specified by `vertex_id`.

\ **Note:** The `vertex` parameter used to be of type `const void*` prior to Godot 4.2.


----



|void| **set_aabb**\ (\ aabb\: [AABB<class_AABB>]\ ) [🔗<class_PhysicsServer3DRenderingServerHandler_method_set_aabb>]

Sets the bounding box for the [SoftBody3D<class_SoftBody3D>].


----



|void| **set_normal**\ (\ vertex_id\: [int<class_int>], normal\: [Vector3<class_Vector3>]\ ) [🔗<class_PhysicsServer3DRenderingServerHandler_method_set_normal>]

Sets the normal for the [SoftBody3D<class_SoftBody3D>] vertex at the index specified by `vertex_id`.


----



|void| **set_vertex**\ (\ vertex_id\: [int<class_int>], vertex\: [Vector3<class_Vector3>]\ ) [🔗<class_PhysicsServer3DRenderingServerHandler_method_set_vertex>]

Sets the position for the [SoftBody3D<class_SoftBody3D>] vertex at the index specified by `vertex_id`.

