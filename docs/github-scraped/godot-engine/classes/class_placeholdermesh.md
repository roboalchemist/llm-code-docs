:github_url: hide



# PlaceholderMesh

**Inherits:** [Mesh<class_Mesh>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Placeholder class for a mesh.


## Description

This class is used when loading a project that uses a [Mesh<class_Mesh>] subclass in 2 conditions:

- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.

- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+--------------------------------------------------+----------------------------+
> | :ref:`AABB<class_AABB>` | :ref:`aabb<class_PlaceholderMesh_property_aabb>` | ``AABB(0, 0, 0, 0, 0, 0)`` |
> +-------------------------+--------------------------------------------------+----------------------------+
>

----


## Property Descriptions



[AABB<class_AABB>] **aabb** = `AABB(0, 0, 0, 0, 0, 0)` [🔗<class_PlaceholderMesh_property_aabb>]


- |void| **set_aabb**\ (\ value\: [AABB<class_AABB>]\ )
- [AABB<class_AABB>] **get_aabb**\ (\ )

The smallest [AABB<class_AABB>] enclosing this mesh in local space.

