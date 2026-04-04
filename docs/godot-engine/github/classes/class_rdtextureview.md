:github_url: hide



# RDTextureView

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Texture view (used by [RenderingDevice<class_RenderingDevice>]).


## Description

This object is used by [RenderingDevice<class_RenderingDevice>].


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------+----------------------------------------------------------------------+---------+
> | :ref:`DataFormat<enum_RenderingDevice_DataFormat>`         | :ref:`format_override<class_RDTextureView_property_format_override>` | ``232`` |
> +------------------------------------------------------------+----------------------------------------------------------------------+---------+
> | :ref:`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>` | :ref:`swizzle_a<class_RDTextureView_property_swizzle_a>`             | ``6``   |
> +------------------------------------------------------------+----------------------------------------------------------------------+---------+
> | :ref:`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>` | :ref:`swizzle_b<class_RDTextureView_property_swizzle_b>`             | ``5``   |
> +------------------------------------------------------------+----------------------------------------------------------------------+---------+
> | :ref:`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>` | :ref:`swizzle_g<class_RDTextureView_property_swizzle_g>`             | ``4``   |
> +------------------------------------------------------------+----------------------------------------------------------------------+---------+
> | :ref:`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>` | :ref:`swizzle_r<class_RDTextureView_property_swizzle_r>`             | ``3``   |
> +------------------------------------------------------------+----------------------------------------------------------------------+---------+
>

----


## Property Descriptions



[DataFormat<enum_RenderingDevice_DataFormat>] **format_override** = `232` [🔗<class_RDTextureView_property_format_override>]


- |void| **set_format_override**\ (\ value\: [DataFormat<enum_RenderingDevice_DataFormat>]\ )
- [DataFormat<enum_RenderingDevice_DataFormat>] **get_format_override**\ (\ )

Optional override for the data format to return sampled values in. The corresponding [RDTextureFormat<class_RDTextureFormat>] must have had this added as a shareable format. The default value of [RenderingDevice.DATA_FORMAT_MAX<class_RenderingDevice_constant_DATA_FORMAT_MAX>] does not override the format.


----



[TextureSwizzle<enum_RenderingDevice_TextureSwizzle>] **swizzle_a** = `6` [🔗<class_RDTextureView_property_swizzle_a>]


- |void| **set_swizzle_a**\ (\ value\: [TextureSwizzle<enum_RenderingDevice_TextureSwizzle>]\ )
- [TextureSwizzle<enum_RenderingDevice_TextureSwizzle>] **get_swizzle_a**\ (\ )

The channel to sample when sampling the alpha channel.


----



[TextureSwizzle<enum_RenderingDevice_TextureSwizzle>] **swizzle_b** = `5` [🔗<class_RDTextureView_property_swizzle_b>]


- |void| **set_swizzle_b**\ (\ value\: [TextureSwizzle<enum_RenderingDevice_TextureSwizzle>]\ )
- [TextureSwizzle<enum_RenderingDevice_TextureSwizzle>] **get_swizzle_b**\ (\ )

The channel to sample when sampling the blue color channel.


----



[TextureSwizzle<enum_RenderingDevice_TextureSwizzle>] **swizzle_g** = `4` [🔗<class_RDTextureView_property_swizzle_g>]


- |void| **set_swizzle_g**\ (\ value\: [TextureSwizzle<enum_RenderingDevice_TextureSwizzle>]\ )
- [TextureSwizzle<enum_RenderingDevice_TextureSwizzle>] **get_swizzle_g**\ (\ )

The channel to sample when sampling the green color channel.


----



[TextureSwizzle<enum_RenderingDevice_TextureSwizzle>] **swizzle_r** = `3` [🔗<class_RDTextureView_property_swizzle_r>]


- |void| **set_swizzle_r**\ (\ value\: [TextureSwizzle<enum_RenderingDevice_TextureSwizzle>]\ )
- [TextureSwizzle<enum_RenderingDevice_TextureSwizzle>] **get_swizzle_r**\ (\ )

The channel to sample when sampling the red color channel.

