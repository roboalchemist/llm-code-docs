:github_url: hide



# Texture2DArray

**Inherits:** [ImageTextureLayered<class_ImageTextureLayered>] **<** [TextureLayered<class_TextureLayered>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A single texture resource which consists of multiple, separate images. Each image has the same dimensions and number of mipmap levels.


## Description

A Texture2DArray is different from a Texture3D: The Texture2DArray does not support trilinear interpolation between the [Image<class_Image>]\ s, i.e. no blending. See also [Cubemap<class_Cubemap>] and [CubemapArray<class_CubemapArray>], which are texture arrays with specialized cubemap functions.

A Texture2DArray is also different from an [AtlasTexture<class_AtlasTexture>]: In a Texture2DArray, all images are treated separately. In an atlas, the regions (i.e. the single images) can be of different sizes. Furthermore, you usually need to add a padding around the regions, to prevent accidental UV mapping to more than one region. The same goes for mipmapping: Mipmap chains are handled separately for each layer. In an atlas, the slicing has to be done manually in the fragment shader.

To create such a texture file yourself, reimport your image files using the Godot Editor import presets. To create a Texture2DArray from code, use [ImageTextureLayered.create_from_images()<class_ImageTextureLayered_method_create_from_images>] on an instance of the Texture2DArray class.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------+-----------------------------------------------------------------------------------------+
> | :ref:`Resource<class_Resource>` | :ref:`create_placeholder<class_Texture2DArray_method_create_placeholder>`\ (\ ) |const| |
> +---------------------------------+-----------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Resource<class_Resource>] **create_placeholder**\ (\ ) |const| [🔗<class_Texture2DArray_method_create_placeholder>]

Creates a placeholder version of this resource ([PlaceholderTexture2DArray<class_PlaceholderTexture2DArray>]).

