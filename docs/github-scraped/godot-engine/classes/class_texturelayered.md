:github_url: hide



# TextureLayered

**Inherits:** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [CompressedTextureLayered<class_CompressedTextureLayered>], [ImageTextureLayered<class_ImageTextureLayered>], [PlaceholderTextureLayered<class_PlaceholderTextureLayered>], [TextureLayeredRD<class_TextureLayeredRD>]

Base class for texture types which contain the data of multiple [Image<class_Image>]\ s. Each image is of the same size and format.


## Description

Base class for [ImageTextureLayered<class_ImageTextureLayered>] and [CompressedTextureLayered<class_CompressedTextureLayered>]. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also [Texture3D<class_Texture3D>].

Data is set on a per-layer basis. For [Texture2DArray<class_Texture2DArray>]\ s, the layer specifies the array layer.

All images need to have the same width, height and number of mipmap levels.

A **TextureLayered** can be loaded with [ResourceLoader.load()<class_ResourceLoader_method_load>].

Internally, Godot maps these files to their respective counterparts in the target rendering driver (Vulkan, OpenGL3).


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Format<enum_Image_Format>`                    | :ref:`_get_format<class_TextureLayered_private_method__get_format>`\ (\ ) |virtual| |required| |const|                                              |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`_get_height<class_TextureLayered_private_method__get_height>`\ (\ ) |virtual| |required| |const|                                              |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Image<class_Image>`                           | :ref:`_get_layer_data<class_TextureLayered_private_method__get_layer_data>`\ (\ layer_index\: :ref:`int<class_int>`\ ) |virtual| |required| |const| |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`_get_layered_type<class_TextureLayered_private_method__get_layered_type>`\ (\ ) |virtual| |required| |const|                                  |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`_get_layers<class_TextureLayered_private_method__get_layers>`\ (\ ) |virtual| |required| |const|                                              |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`_get_width<class_TextureLayered_private_method__get_width>`\ (\ ) |virtual| |required| |const|                                                |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`_has_mipmaps<class_TextureLayered_private_method__has_mipmaps>`\ (\ ) |virtual| |required| |const|                                            |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Format<enum_Image_Format>`                    | :ref:`get_format<class_TextureLayered_method_get_format>`\ (\ ) |const|                                                                             |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_height<class_TextureLayered_method_get_height>`\ (\ ) |const|                                                                             |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Image<class_Image>`                           | :ref:`get_layer_data<class_TextureLayered_method_get_layer_data>`\ (\ layer\: :ref:`int<class_int>`\ ) |const|                                      |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`LayeredType<enum_TextureLayered_LayeredType>` | :ref:`get_layered_type<class_TextureLayered_method_get_layered_type>`\ (\ ) |const|                                                                 |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_layers<class_TextureLayered_method_get_layers>`\ (\ ) |const|                                                                             |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_width<class_TextureLayered_method_get_width>`\ (\ ) |const|                                                                               |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`has_mipmaps<class_TextureLayered_method_has_mipmaps>`\ (\ ) |const|                                                                           |
> +-----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **LayeredType**: [🔗<enum_TextureLayered_LayeredType>]



[LayeredType<enum_TextureLayered_LayeredType>] **LAYERED_TYPE_2D_ARRAY** = `0`

Texture is a generic [Texture2DArray<class_Texture2DArray>].



[LayeredType<enum_TextureLayered_LayeredType>] **LAYERED_TYPE_CUBEMAP** = `1`

Texture is a [Cubemap<class_Cubemap>], with each side in its own layer (6 in total).



[LayeredType<enum_TextureLayered_LayeredType>] **LAYERED_TYPE_CUBEMAP_ARRAY** = `2`

Texture is a [CubemapArray<class_CubemapArray>], with each cubemap being made of 6 layers.


----


## Method Descriptions



[Format<enum_Image_Format>] **_get_format**\ (\ ) |virtual| |required| |const| [🔗<class_TextureLayered_private_method__get_format>]

Called when the **TextureLayered**'s format is queried.


----



[int<class_int>] **_get_height**\ (\ ) |virtual| |required| |const| [🔗<class_TextureLayered_private_method__get_height>]

Called when the **TextureLayered**'s height is queried.


----



[Image<class_Image>] **_get_layer_data**\ (\ layer_index\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_TextureLayered_private_method__get_layer_data>]

Called when the data for a layer in the **TextureLayered** is queried.


----



[int<class_int>] **_get_layered_type**\ (\ ) |virtual| |required| |const| [🔗<class_TextureLayered_private_method__get_layered_type>]

Called when the layers' type in the **TextureLayered** is queried.


----



[int<class_int>] **_get_layers**\ (\ ) |virtual| |required| |const| [🔗<class_TextureLayered_private_method__get_layers>]

Called when the number of layers in the **TextureLayered** is queried.


----



[int<class_int>] **_get_width**\ (\ ) |virtual| |required| |const| [🔗<class_TextureLayered_private_method__get_width>]

Called when the **TextureLayered**'s width queried.


----



[bool<class_bool>] **_has_mipmaps**\ (\ ) |virtual| |required| |const| [🔗<class_TextureLayered_private_method__has_mipmaps>]

Called when the presence of mipmaps in the **TextureLayered** is queried.


----



[Format<enum_Image_Format>] **get_format**\ (\ ) |const| [🔗<class_TextureLayered_method_get_format>]

Returns the current format being used by this texture.


----



[int<class_int>] **get_height**\ (\ ) |const| [🔗<class_TextureLayered_method_get_height>]

Returns the height of the texture in pixels. Height is typically represented by the Y axis.


----



[Image<class_Image>] **get_layer_data**\ (\ layer\: [int<class_int>]\ ) |const| [🔗<class_TextureLayered_method_get_layer_data>]

Returns an [Image<class_Image>] resource with the data from specified `layer`.


----



[LayeredType<enum_TextureLayered_LayeredType>] **get_layered_type**\ (\ ) |const| [🔗<class_TextureLayered_method_get_layered_type>]

Returns the **TextureLayered**'s type. The type determines how the data is accessed, with cubemaps having special types.


----



[int<class_int>] **get_layers**\ (\ ) |const| [🔗<class_TextureLayered_method_get_layers>]

Returns the number of referenced [Image<class_Image>]\ s.


----



[int<class_int>] **get_width**\ (\ ) |const| [🔗<class_TextureLayered_method_get_width>]

Returns the width of the texture in pixels. Width is typically represented by the X axis.


----



[bool<class_bool>] **has_mipmaps**\ (\ ) |const| [🔗<class_TextureLayered_method_has_mipmaps>]

Returns `true` if the layers have generated mipmaps.

