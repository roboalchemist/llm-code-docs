:github_url: hide



# ImageTexture3D

**Inherits:** [Texture3D<class_Texture3D>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Texture with 3 dimensions.


## Description

**ImageTexture3D** is a 3-dimensional [ImageTexture<class_ImageTexture>] that has a width, height, and depth. See also [ImageTextureLayered<class_ImageTextureLayered>].

3D textures are typically used to store density maps for [FogMaterial<class_FogMaterial>], color correction LUTs for [Environment<class_Environment>], vector fields for [GPUParticlesAttractorVectorField3D<class_GPUParticlesAttractorVectorField3D>] and collision maps for [GPUParticlesCollisionSDF3D<class_GPUParticlesCollisionSDF3D>]. 3D textures can also be used in custom shaders.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`create<class_ImageTexture3D_method_create>`\ (\ format\: :ref:`Format<enum_Image_Format>`, width\: :ref:`int<class_int>`, height\: :ref:`int<class_int>`, depth\: :ref:`int<class_int>`, use_mipmaps\: :ref:`bool<class_bool>`, data\: :ref:`Array<class_Array>`\[:ref:`Image<class_Image>`\]\ ) |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`update<class_ImageTexture3D_method_update>`\ (\ data\: :ref:`Array<class_Array>`\[:ref:`Image<class_Image>`\]\ )                                                                                                                                                                                 |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Error<enum_@GlobalScope_Error>] **create**\ (\ format\: [Format<enum_Image_Format>], width\: [int<class_int>], height\: [int<class_int>], depth\: [int<class_int>], use_mipmaps\: [bool<class_bool>], data\: [Array<class_Array>]\[[Image<class_Image>]\]\ ) [🔗<class_ImageTexture3D_method_create>]

Creates the **ImageTexture3D** with specified `format`, `width`, `height`, and `depth`. If `use_mipmaps` is `true`, generates mipmaps for the **ImageTexture3D**.


----



|void| **update**\ (\ data\: [Array<class_Array>]\[[Image<class_Image>]\]\ ) [🔗<class_ImageTexture3D_method_update>]

Replaces the texture's existing data with the layers specified in `data`. The size of `data` must match the parameters that were used for [create()<class_ImageTexture3D_method_create>]. In other words, the texture cannot be resized or have its format changed by calling [update()<class_ImageTexture3D_method_update>].

