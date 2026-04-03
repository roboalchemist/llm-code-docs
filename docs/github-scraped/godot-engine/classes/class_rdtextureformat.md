:github_url: hide



# RDTextureFormat

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Texture format (used by [RenderingDevice<class_RenderingDevice>]).


## Description

This object is used by [RenderingDevice<class_RenderingDevice>].


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                                        | :ref:`array_layers<class_RDTextureFormat_property_array_layers>`           | ``1``     |
> +------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                                        | :ref:`depth<class_RDTextureFormat_property_depth>`                         | ``1``     |
> +------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------+
> | :ref:`DataFormat<enum_RenderingDevice_DataFormat>`                           | :ref:`format<class_RDTextureFormat_property_format>`                       | ``8``     |
> +------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                                        | :ref:`height<class_RDTextureFormat_property_height>`                       | ``1``     |
> +------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                      | :ref:`is_discardable<class_RDTextureFormat_property_is_discardable>`       | ``false`` |
> +------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                      | :ref:`is_resolve_buffer<class_RDTextureFormat_property_is_resolve_buffer>` | ``false`` |
> +------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                                        | :ref:`mipmaps<class_RDTextureFormat_property_mipmaps>`                     | ``1``     |
> +------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------+
> | :ref:`TextureSamples<enum_RenderingDevice_TextureSamples>`                   | :ref:`samples<class_RDTextureFormat_property_samples>`                     | ``0``     |
> +------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------+
> | :ref:`TextureType<enum_RenderingDevice_TextureType>`                         | :ref:`texture_type<class_RDTextureFormat_property_texture_type>`           | ``1``     |
> +------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------+
> | |bitfield|\[:ref:`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`\] | :ref:`usage_bits<class_RDTextureFormat_property_usage_bits>`               | ``0``     |
> +------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                                        | :ref:`width<class_RDTextureFormat_property_width>`                         | ``1``     |
> +------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`add_shareable_format<class_RDTextureFormat_method_add_shareable_format>`\ (\ format\: :ref:`DataFormat<enum_RenderingDevice_DataFormat>`\ )       |
> +--------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`remove_shareable_format<class_RDTextureFormat_method_remove_shareable_format>`\ (\ format\: :ref:`DataFormat<enum_RenderingDevice_DataFormat>`\ ) |
> +--------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[int<class_int>] **array_layers** = `1` [🔗<class_RDTextureFormat_property_array_layers>]


- |void| **set_array_layers**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_array_layers**\ (\ )

The number of layers in the texture. Only relevant for 2D texture arrays.


----



[int<class_int>] **depth** = `1` [🔗<class_RDTextureFormat_property_depth>]


- |void| **set_depth**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_depth**\ (\ )

The texture's depth (in pixels). This is always `1` for 2D textures.


----



[DataFormat<enum_RenderingDevice_DataFormat>] **format** = `8` [🔗<class_RDTextureFormat_property_format>]


- |void| **set_format**\ (\ value\: [DataFormat<enum_RenderingDevice_DataFormat>]\ )
- [DataFormat<enum_RenderingDevice_DataFormat>] **get_format**\ (\ )

The texture's pixel data format.


----



[int<class_int>] **height** = `1` [🔗<class_RDTextureFormat_property_height>]


- |void| **set_height**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_height**\ (\ )

The texture's height (in pixels).


----



[bool<class_bool>] **is_discardable** = `false` [🔗<class_RDTextureFormat_property_is_discardable>]


- |void| **set_is_discardable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_is_discardable**\ (\ )

If a texture is discardable, its contents do not need to be preserved between frames. This flag is only relevant when the texture is used as target in a draw list.

This information is used by [RenderingDevice<class_RenderingDevice>] to figure out if a texture's contents can be discarded, eliminating unnecessary writes to memory and boosting performance.


----



[bool<class_bool>] **is_resolve_buffer** = `false` [🔗<class_RDTextureFormat_property_is_resolve_buffer>]


- |void| **set_is_resolve_buffer**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_is_resolve_buffer**\ (\ )

The texture will be used as the destination of a resolve operation.


----



[int<class_int>] **mipmaps** = `1` [🔗<class_RDTextureFormat_property_mipmaps>]


- |void| **set_mipmaps**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_mipmaps**\ (\ )

The number of mipmaps available in the texture.


----



[TextureSamples<enum_RenderingDevice_TextureSamples>] **samples** = `0` [🔗<class_RDTextureFormat_property_samples>]


- |void| **set_samples**\ (\ value\: [TextureSamples<enum_RenderingDevice_TextureSamples>]\ )
- [TextureSamples<enum_RenderingDevice_TextureSamples>] **get_samples**\ (\ )

The number of samples used when sampling the texture.


----



[TextureType<enum_RenderingDevice_TextureType>] **texture_type** = `1` [🔗<class_RDTextureFormat_property_texture_type>]


- |void| **set_texture_type**\ (\ value\: [TextureType<enum_RenderingDevice_TextureType>]\ )
- [TextureType<enum_RenderingDevice_TextureType>] **get_texture_type**\ (\ )

The texture type.


----



|bitfield|\[[TextureUsageBits<enum_RenderingDevice_TextureUsageBits>]\] **usage_bits** = `0` [🔗<class_RDTextureFormat_property_usage_bits>]


- |void| **set_usage_bits**\ (\ value\: |bitfield|\[[TextureUsageBits<enum_RenderingDevice_TextureUsageBits>]\]\ )
- |bitfield|\[[TextureUsageBits<enum_RenderingDevice_TextureUsageBits>]\] **get_usage_bits**\ (\ )

The texture's usage bits, which determine what can be done using the texture.


----



[int<class_int>] **width** = `1` [🔗<class_RDTextureFormat_property_width>]


- |void| **set_width**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_width**\ (\ )

The texture's width (in pixels).


----


## Method Descriptions



|void| **add_shareable_format**\ (\ format\: [DataFormat<enum_RenderingDevice_DataFormat>]\ ) [🔗<class_RDTextureFormat_method_add_shareable_format>]

Adds `format` as a valid format for the corresponding [RDTextureView<class_RDTextureView>]'s [RDTextureView.format_override<class_RDTextureView_property_format_override>] property. If any format is added as shareable, then the main [format<class_RDTextureFormat_property_format>] must also be added.


----



|void| **remove_shareable_format**\ (\ format\: [DataFormat<enum_RenderingDevice_DataFormat>]\ ) [🔗<class_RDTextureFormat_method_remove_shareable_format>]

Removes `format` from the list of valid formats that the corresponding [RDTextureView<class_RDTextureView>]'s [RDTextureView.format_override<class_RDTextureView_property_format_override>] property can be set to.

