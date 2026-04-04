:github_url: hide



# PlaceholderTextureLayered

**Inherits:** [TextureLayered<class_TextureLayered>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [PlaceholderCubemap<class_PlaceholderCubemap>], [PlaceholderCubemapArray<class_PlaceholderCubemapArray>], [PlaceholderTexture2DArray<class_PlaceholderTexture2DArray>]

Placeholder class for a 2-dimensional texture array.


## Description

This class is used when loading a project that uses a [TextureLayered<class_TextureLayered>] subclass in 2 conditions:

- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.

- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

\ **Note:** This is not intended to be used as an actual texture for rendering. It is not guaranteed to work like one in shaders or materials (for example when calculating UV).


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+----------------------------------------------------------------+--------------------+
> | :ref:`int<class_int>`           | :ref:`layers<class_PlaceholderTextureLayered_property_layers>` | ``1``              |
> +---------------------------------+----------------------------------------------------------------+--------------------+
> | :ref:`Vector2i<class_Vector2i>` | :ref:`size<class_PlaceholderTextureLayered_property_size>`     | ``Vector2i(1, 1)`` |
> +---------------------------------+----------------------------------------------------------------+--------------------+
>

----


## Property Descriptions



[int<class_int>] **layers** = `1` [🔗<class_PlaceholderTextureLayered_property_layers>]


- |void| **set_layers**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_layers**\ (\ )

The number of layers in the texture array.


----



[Vector2i<class_Vector2i>] **size** = `Vector2i(1, 1)` [🔗<class_PlaceholderTextureLayered_property_size>]


- |void| **set_size**\ (\ value\: [Vector2i<class_Vector2i>]\ )
- [Vector2i<class_Vector2i>] **get_size**\ (\ )

The size of each texture layer (in pixels).

