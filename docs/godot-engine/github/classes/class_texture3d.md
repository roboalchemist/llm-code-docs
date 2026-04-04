:github_url: hide



# Texture3D

**Inherits:** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [CompressedTexture3D<class_CompressedTexture3D>], [ImageTexture3D<class_ImageTexture3D>], [NoiseTexture3D<class_NoiseTexture3D>], [PlaceholderTexture3D<class_PlaceholderTexture3D>], [Texture3DRD<class_Texture3DRD>]

Base class for 3-dimensional textures.


## Description

Base class for [ImageTexture3D<class_ImageTexture3D>] and [CompressedTexture3D<class_CompressedTexture3D>]. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. **Texture3D** is the base class for all 3-dimensional texture types. See also [TextureLayered<class_TextureLayered>].

All images need to have the same width, height and number of mipmap levels.

To create such a texture file yourself, reimport your image files using the Godot Editor import presets.


## Methods

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Image<class_Image>`\] | :ref:`_get_data<class_Texture3D_private_method__get_data>`\ (\ ) |virtual| |required| |const|       |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                  | :ref:`_get_depth<class_Texture3D_private_method__get_depth>`\ (\ ) |virtual| |required| |const|     |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`Format<enum_Image_Format>`                       | :ref:`_get_format<class_Texture3D_private_method__get_format>`\ (\ ) |virtual| |required| |const|   |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                  | :ref:`_get_height<class_Texture3D_private_method__get_height>`\ (\ ) |virtual| |required| |const|   |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                  | :ref:`_get_width<class_Texture3D_private_method__get_width>`\ (\ ) |virtual| |required| |const|     |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                | :ref:`_has_mipmaps<class_Texture3D_private_method__has_mipmaps>`\ (\ ) |virtual| |required| |const| |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`Resource<class_Resource>`                        | :ref:`create_placeholder<class_Texture3D_method_create_placeholder>`\ (\ ) |const|                  |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Image<class_Image>`\] | :ref:`get_data<class_Texture3D_method_get_data>`\ (\ ) |const|                                      |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                  | :ref:`get_depth<class_Texture3D_method_get_depth>`\ (\ ) |const|                                    |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`Format<enum_Image_Format>`                       | :ref:`get_format<class_Texture3D_method_get_format>`\ (\ ) |const|                                  |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                  | :ref:`get_height<class_Texture3D_method_get_height>`\ (\ ) |const|                                  |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                  | :ref:`get_width<class_Texture3D_method_get_width>`\ (\ ) |const|                                    |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                | :ref:`has_mipmaps<class_Texture3D_method_has_mipmaps>`\ (\ ) |const|                                |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Array<class_Array>]\[[Image<class_Image>]\] **_get_data**\ (\ ) |virtual| |required| |const| [🔗<class_Texture3D_private_method__get_data>]

Called when the **Texture3D**'s data is queried.


----



[int<class_int>] **_get_depth**\ (\ ) |virtual| |required| |const| [🔗<class_Texture3D_private_method__get_depth>]

Called when the **Texture3D**'s depth is queried.


----



[Format<enum_Image_Format>] **_get_format**\ (\ ) |virtual| |required| |const| [🔗<class_Texture3D_private_method__get_format>]

Called when the **Texture3D**'s format is queried.


----



[int<class_int>] **_get_height**\ (\ ) |virtual| |required| |const| [🔗<class_Texture3D_private_method__get_height>]

Called when the **Texture3D**'s height is queried.


----



[int<class_int>] **_get_width**\ (\ ) |virtual| |required| |const| [🔗<class_Texture3D_private_method__get_width>]

Called when the **Texture3D**'s width is queried.


----



[bool<class_bool>] **_has_mipmaps**\ (\ ) |virtual| |required| |const| [🔗<class_Texture3D_private_method__has_mipmaps>]

Called when the presence of mipmaps in the **Texture3D** is queried.


----



[Resource<class_Resource>] **create_placeholder**\ (\ ) |const| [🔗<class_Texture3D_method_create_placeholder>]

Creates a placeholder version of this resource ([PlaceholderTexture3D<class_PlaceholderTexture3D>]).


----



[Array<class_Array>]\[[Image<class_Image>]\] **get_data**\ (\ ) |const| [🔗<class_Texture3D_method_get_data>]

Returns the **Texture3D**'s data as an array of [Image<class_Image>]\ s. Each [Image<class_Image>] represents a *slice* of the **Texture3D**, with different slices mapping to different depth (Z axis) levels.


----



[int<class_int>] **get_depth**\ (\ ) |const| [🔗<class_Texture3D_method_get_depth>]

Returns the **Texture3D**'s depth in pixels. Depth is typically represented by the Z axis (a dimension not present in [Texture2D<class_Texture2D>]).


----



[Format<enum_Image_Format>] **get_format**\ (\ ) |const| [🔗<class_Texture3D_method_get_format>]

Returns the current format being used by this texture.


----



[int<class_int>] **get_height**\ (\ ) |const| [🔗<class_Texture3D_method_get_height>]

Returns the **Texture3D**'s height in pixels. Width is typically represented by the Y axis.


----



[int<class_int>] **get_width**\ (\ ) |const| [🔗<class_Texture3D_method_get_width>]

Returns the **Texture3D**'s width in pixels. Width is typically represented by the X axis.


----



[bool<class_bool>] **has_mipmaps**\ (\ ) |const| [🔗<class_Texture3D_method_has_mipmaps>]

Returns `true` if the **Texture3D** has generated mipmaps.

