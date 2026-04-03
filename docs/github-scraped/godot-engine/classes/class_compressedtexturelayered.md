:github_url: hide



# CompressedTextureLayered

**Inherits:** [TextureLayered<class_TextureLayered>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [CompressedCubemap<class_CompressedCubemap>], [CompressedCubemapArray<class_CompressedCubemapArray>], [CompressedTexture2DArray<class_CompressedTexture2DArray>]

Base class for texture arrays that can optionally be compressed.


## Description

Base class for [CompressedTexture2DArray<class_CompressedTexture2DArray>] and [CompressedTexture3D<class_CompressedTexture3D>]. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also [TextureLayered<class_TextureLayered>].


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+---------------------------------------------------------------------+--------+
> | :ref:`String<class_String>` | :ref:`load_path<class_CompressedTextureLayered_property_load_path>` | ``""`` |
> +-----------------------------+---------------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+---------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`load<class_CompressedTextureLayered_method_load>`\ (\ path\: :ref:`String<class_String>`\ ) |
> +---------------------------------------+---------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[String<class_String>] **load_path** = `""` [🔗<class_CompressedTextureLayered_property_load_path>]


- [Error<enum_@GlobalScope_Error>] **load**\ (\ path\: [String<class_String>]\ )
- [String<class_String>] **get_load_path**\ (\ )

The path the texture should be loaded from.


----


## Method Descriptions



[Error<enum_@GlobalScope_Error>] **load**\ (\ path\: [String<class_String>]\ ) [🔗<class_CompressedTextureLayered_method_load>]

Loads the texture at `path`.

