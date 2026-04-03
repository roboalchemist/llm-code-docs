:github_url: hide



# ExternalTexture

**Inherits:** [Texture2D<class_Texture2D>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Texture which displays the content of an external buffer.


## Description

Displays the content of an external buffer provided by the platform.

Requires the [OES_EGL_image_external ](https://registry.khronos.org/OpenGL/extensions/OES/OES_EGL_image_external.txt)_ extension (OpenGL) or [VK_ANDROID_external_memory_android_hardware_buffer ](https://registry.khronos.org/vulkan/specs/1.1-extensions/html/vkspec.html#VK_ANDROID_external_memory_android_hardware_buffer)_ extension (Vulkan).

\ **Note:** This is currently only supported in Android builds.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+--------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | resource_local_to_scene                          | ``false`` (overrides :ref:`Resource<class_Resource_property_resource_local_to_scene>`) |
> +-------------------------------+--------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`size<class_ExternalTexture_property_size>` | ``Vector2(256, 256)``                                                                  |
> +-------------------------------+--------------------------------------------------+----------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>` | :ref:`get_external_texture_id<class_ExternalTexture_method_get_external_texture_id>`\ (\ ) |const|                                   |
> +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                | :ref:`set_external_buffer_id<class_ExternalTexture_method_set_external_buffer_id>`\ (\ external_buffer_id\: :ref:`int<class_int>`\ ) |
> +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Vector2<class_Vector2>] **size** = `Vector2(256, 256)` [🔗<class_ExternalTexture_property_size>]


- |void| **set_size**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_size**\ (\ )

External texture size.


----


## Method Descriptions



[int<class_int>] **get_external_texture_id**\ (\ ) |const| [🔗<class_ExternalTexture_method_get_external_texture_id>]

Returns the external texture ID.

Depending on your use case, you may need to pass this to platform APIs, for example, when creating an `android.graphics.SurfaceTexture` on Android.


----



|void| **set_external_buffer_id**\ (\ external_buffer_id\: [int<class_int>]\ ) [🔗<class_ExternalTexture_method_set_external_buffer_id>]

Sets the external buffer ID.

Depending on your use case, you may need to call this with data received from a platform API, for example, `SurfaceTexture.getHardwareBuffer()` on Android.

