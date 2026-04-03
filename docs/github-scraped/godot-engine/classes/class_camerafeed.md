:github_url: hide



# CameraFeed

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A camera feed gives you access to a single physical camera attached to your device.


## Description

A camera feed gives you access to a single physical camera attached to your device. When enabled, Godot will start capturing frames from the camera which can then be used. See also [CameraServer<class_CameraServer>].

\ **Note:** Many cameras will return YCbCr images which are split into two textures and need to be combined in a shader. Godot does this automatically for you if you set the environment to show the camera image in the background.

\ **Note:** This class is currently only implemented on Linux, Android, macOS, and iOS. On other platforms no **CameraFeed**\ s will be available. To get a **CameraFeed** on iOS, the camera plugin from [godot-ios-plugins ](https://github.com/godotengine/godot-ios-plugins)_ is required.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------+-----------------------------------------------------------------+------------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`feed_is_active<class_CameraFeed_property_feed_is_active>` | ``false``                          |
> +---------------------------------------+-----------------------------------------------------------------+------------------------------------+
> | :ref:`Transform2D<class_Transform2D>` | :ref:`feed_transform<class_CameraFeed_property_feed_transform>` | ``Transform2D(1, 0, 0, -1, 0, 1)`` |
> +---------------------------------------+-----------------------------------------------------------------+------------------------------------+
> | :ref:`Array<class_Array>`             | :ref:`formats<class_CameraFeed_property_formats>`               | ``[]``                             |
> +---------------------------------------+-----------------------------------------------------------------+------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`_activate_feed<class_CameraFeed_private_method__activate_feed>`\ (\ ) |virtual|                                                                |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`_deactivate_feed<class_CameraFeed_private_method__deactivate_feed>`\ (\ ) |virtual|                                                            |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`FeedDataType<enum_CameraFeed_FeedDataType>` | :ref:`get_datatype<class_CameraFeed_method_get_datatype>`\ (\ ) |const|                                                                              |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`get_id<class_CameraFeed_method_get_id>`\ (\ ) |const|                                                                                          |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                       | :ref:`get_name<class_CameraFeed_method_get_name>`\ (\ ) |const|                                                                                      |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`FeedPosition<enum_CameraFeed_FeedPosition>` | :ref:`get_position<class_CameraFeed_method_get_position>`\ (\ ) |const|                                                                              |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`get_texture_tex_id<class_CameraFeed_method_get_texture_tex_id>`\ (\ feed_image_type\: :ref:`FeedImage<enum_CameraServer_FeedImage>`\ )         |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_external<class_CameraFeed_method_set_external>`\ (\ width\: :ref:`int<class_int>`, height\: :ref:`int<class_int>`\ )                       |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`set_format<class_CameraFeed_method_set_format>`\ (\ index\: :ref:`int<class_int>`, parameters\: :ref:`Dictionary<class_Dictionary>`\ )         |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_name<class_CameraFeed_method_set_name>`\ (\ name\: :ref:`String<class_String>`\ )                                                          |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_position<class_CameraFeed_method_set_position>`\ (\ position\: :ref:`FeedPosition<enum_CameraFeed_FeedPosition>`\ )                        |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_rgb_image<class_CameraFeed_method_set_rgb_image>`\ (\ rgb_image\: :ref:`Image<class_Image>`\ )                                             |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_ycbcr_image<class_CameraFeed_method_set_ycbcr_image>`\ (\ ycbcr_image\: :ref:`Image<class_Image>`\ )                                       |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_ycbcr_images<class_CameraFeed_method_set_ycbcr_images>`\ (\ y_image\: :ref:`Image<class_Image>`, cbcr_image\: :ref:`Image<class_Image>`\ ) |
> +---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**format_changed**\ (\ ) [🔗<class_CameraFeed_signal_format_changed>]

Emitted when the format has changed.


----



**frame_changed**\ (\ ) [🔗<class_CameraFeed_signal_frame_changed>]

Emitted when a new frame is available.


----


## Enumerations



enum **FeedDataType**: [🔗<enum_CameraFeed_FeedDataType>]



[FeedDataType<enum_CameraFeed_FeedDataType>] **FEED_NOIMAGE** = `0`

No image set for the feed.



[FeedDataType<enum_CameraFeed_FeedDataType>] **FEED_RGB** = `1`

Feed supplies RGB images.



[FeedDataType<enum_CameraFeed_FeedDataType>] **FEED_YCBCR** = `2`

Feed supplies YCbCr images that need to be converted to RGB.



[FeedDataType<enum_CameraFeed_FeedDataType>] **FEED_YCBCR_SEP** = `3`

Feed supplies separate Y and CbCr images that need to be combined and converted to RGB.



[FeedDataType<enum_CameraFeed_FeedDataType>] **FEED_EXTERNAL** = `4`

Feed supplies external image.


----



enum **FeedPosition**: [🔗<enum_CameraFeed_FeedPosition>]



[FeedPosition<enum_CameraFeed_FeedPosition>] **FEED_UNSPECIFIED** = `0`

Unspecified position.



[FeedPosition<enum_CameraFeed_FeedPosition>] **FEED_FRONT** = `1`

Camera is mounted at the front of the device.



[FeedPosition<enum_CameraFeed_FeedPosition>] **FEED_BACK** = `2`

Camera is mounted at the back of the device.


----


## Property Descriptions



[bool<class_bool>] **feed_is_active** = `false` [🔗<class_CameraFeed_property_feed_is_active>]


- |void| **set_active**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_active**\ (\ )

If `true`, the feed is active.


----



[Transform2D<class_Transform2D>] **feed_transform** = `Transform2D(1, 0, 0, -1, 0, 1)` [🔗<class_CameraFeed_property_feed_transform>]


- |void| **set_transform**\ (\ value\: [Transform2D<class_Transform2D>]\ )
- [Transform2D<class_Transform2D>] **get_transform**\ (\ )

The transform applied to the camera's image.


----



[Array<class_Array>] **formats** = `[]` [🔗<class_CameraFeed_property_formats>]


- [Array<class_Array>] **get_formats**\ (\ )

Formats supported by the feed. Each entry is a [Dictionary<class_Dictionary>] describing format parameters.


----


## Method Descriptions



[bool<class_bool>] **_activate_feed**\ (\ ) |virtual| [🔗<class_CameraFeed_private_method__activate_feed>]

Called when the camera feed is activated.


----



|void| **_deactivate_feed**\ (\ ) |virtual| [🔗<class_CameraFeed_private_method__deactivate_feed>]

Called when the camera feed is deactivated.


----



[FeedDataType<enum_CameraFeed_FeedDataType>] **get_datatype**\ (\ ) |const| [🔗<class_CameraFeed_method_get_datatype>]

Returns feed image data type.


----



[int<class_int>] **get_id**\ (\ ) |const| [🔗<class_CameraFeed_method_get_id>]

Returns the unique ID for this feed.


----



[String<class_String>] **get_name**\ (\ ) |const| [🔗<class_CameraFeed_method_get_name>]

Returns the camera's name.


----



[FeedPosition<enum_CameraFeed_FeedPosition>] **get_position**\ (\ ) |const| [🔗<class_CameraFeed_method_get_position>]

Returns the position of camera on the device.


----



[int<class_int>] **get_texture_tex_id**\ (\ feed_image_type\: [FeedImage<enum_CameraServer_FeedImage>]\ ) [🔗<class_CameraFeed_method_get_texture_tex_id>]

Returns the texture backend ID (usable by some external libraries that need a handle to a texture to write data).


----



|void| **set_external**\ (\ width\: [int<class_int>], height\: [int<class_int>]\ ) [🔗<class_CameraFeed_method_set_external>]

Sets the feed as external feed provided by another library.


----



[bool<class_bool>] **set_format**\ (\ index\: [int<class_int>], parameters\: [Dictionary<class_Dictionary>]\ ) [🔗<class_CameraFeed_method_set_format>]

Sets the feed format parameters for the given `index` in the [formats<class_CameraFeed_property_formats>] array. Returns `true` on success. By default, the YUYV encoded stream is transformed to [FEED_RGB<class_CameraFeed_constant_FEED_RGB>]. The YUYV encoded stream output format can be changed by setting `parameters`'s `output` entry to one of the following:

- `"separate"` will result in [FEED_YCBCR_SEP<class_CameraFeed_constant_FEED_YCBCR_SEP>];

- `"grayscale"` will result in desaturated [FEED_RGB<class_CameraFeed_constant_FEED_RGB>];

- `"copy"` will result in [FEED_YCBCR<class_CameraFeed_constant_FEED_YCBCR>].


----



|void| **set_name**\ (\ name\: [String<class_String>]\ ) [🔗<class_CameraFeed_method_set_name>]

Sets the camera's name.


----



|void| **set_position**\ (\ position\: [FeedPosition<enum_CameraFeed_FeedPosition>]\ ) [🔗<class_CameraFeed_method_set_position>]

Sets the position of this camera.


----



|void| **set_rgb_image**\ (\ rgb_image\: [Image<class_Image>]\ ) [🔗<class_CameraFeed_method_set_rgb_image>]

Sets RGB image for this feed.


----



|void| **set_ycbcr_image**\ (\ ycbcr_image\: [Image<class_Image>]\ ) [🔗<class_CameraFeed_method_set_ycbcr_image>]

Sets YCbCr image for this feed.


----



|void| **set_ycbcr_images**\ (\ y_image\: [Image<class_Image>], cbcr_image\: [Image<class_Image>]\ ) [🔗<class_CameraFeed_method_set_ycbcr_images>]

Sets Y and CbCr images for this feed.

