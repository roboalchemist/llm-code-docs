:github_url: hide



# ImageFormatLoaderExtension

**Inherits:** [ImageFormatLoader<class_ImageFormatLoader>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Base class for creating [ImageFormatLoader<class_ImageFormatLoader>] extensions (adding support for extra image formats).


## Description

The engine supports multiple image formats out of the box (PNG, SVG, JPEG, WebP to name a few), but you can choose to implement support for additional image formats by extending this class.

Be sure to respect the documented return types and values. You should create an instance of it, and call [add_format_loader()<class_ImageFormatLoaderExtension_method_add_format_loader>] to register that loader during the initialization phase.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`_get_recognized_extensions<class_ImageFormatLoaderExtension_private_method__get_recognized_extensions>`\ (\ ) |virtual| |const|                                                                                                                                                                 |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`             | :ref:`_load_image<class_ImageFormatLoaderExtension_private_method__load_image>`\ (\ image\: :ref:`Image<class_Image>`, fileaccess\: :ref:`FileAccess<class_FileAccess>`, flags\: |bitfield|\[:ref:`LoaderFlags<enum_ImageFormatLoader_LoaderFlags>`\], scale\: :ref:`float<class_float>`\ ) |virtual| |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`add_format_loader<class_ImageFormatLoaderExtension_method_add_format_loader>`\ (\ )                                                                                                                                                                                                             |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`remove_format_loader<class_ImageFormatLoaderExtension_method_remove_format_loader>`\ (\ )                                                                                                                                                                                                       |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[PackedStringArray<class_PackedStringArray>] **_get_recognized_extensions**\ (\ ) |virtual| |const| [🔗<class_ImageFormatLoaderExtension_private_method__get_recognized_extensions>]

Returns the list of file extensions for this image format. Files with the given extensions will be treated as image file and loaded using this class.


----



[Error<enum_@GlobalScope_Error>] **_load_image**\ (\ image\: [Image<class_Image>], fileaccess\: [FileAccess<class_FileAccess>], flags\: |bitfield|\[[LoaderFlags<enum_ImageFormatLoader_LoaderFlags>]\], scale\: [float<class_float>]\ ) |virtual| [🔗<class_ImageFormatLoaderExtension_private_method__load_image>]

Loads the content of `fileaccess` into the provided `image`.


----



|void| **add_format_loader**\ (\ ) [🔗<class_ImageFormatLoaderExtension_method_add_format_loader>]

Add this format loader to the engine, allowing it to recognize the file extensions returned by [_get_recognized_extensions()<class_ImageFormatLoaderExtension_private_method__get_recognized_extensions>].


----



|void| **remove_format_loader**\ (\ ) [🔗<class_ImageFormatLoaderExtension_method_remove_format_loader>]

Remove this format loader from the engine.

