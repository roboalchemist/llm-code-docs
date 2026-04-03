:github_url: hide



# PlaceholderTexture3D

**Inherits:** [Texture3D<class_Texture3D>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Placeholder class for a 3-dimensional texture.


## Description

This class is used when loading a project that uses a [Texture3D<class_Texture3D>] subclass in 2 conditions:

- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.

- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

\ **Note:** This is not intended to be used as an actual texture for rendering. It is not guaranteed to work like one in shaders or materials (for example when calculating UV).


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+-------------------------------------------------------+-----------------------+
> | :ref:`Vector3i<class_Vector3i>` | :ref:`size<class_PlaceholderTexture3D_property_size>` | ``Vector3i(1, 1, 1)`` |
> +---------------------------------+-------------------------------------------------------+-----------------------+
>

----


## Property Descriptions



[Vector3i<class_Vector3i>] **size** = `Vector3i(1, 1, 1)` [🔗<class_PlaceholderTexture3D_property_size>]


- |void| **set_size**\ (\ value\: [Vector3i<class_Vector3i>]\ )
- [Vector3i<class_Vector3i>] **get_size**\ (\ )

The texture's size (in pixels).

