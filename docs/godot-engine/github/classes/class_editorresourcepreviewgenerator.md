:github_url: hide



# EditorResourcePreviewGenerator

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Custom generator of previews.


## Description

Custom code to generate previews. Check [EditorSettings.filesystem/file_dialog/thumbnail_size<class_EditorSettings_property_filesystem/file_dialog/thumbnail_size>] to find a proper size to generate previews at.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`_can_generate_small_preview<class_EditorResourcePreviewGenerator_private_method__can_generate_small_preview>`\ (\ ) |virtual| |const|                                                                                                             |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`_generate<class_EditorResourcePreviewGenerator_private_method__generate>`\ (\ resource\: :ref:`Resource<class_Resource>`, size\: :ref:`Vector2i<class_Vector2i>`, metadata\: :ref:`Dictionary<class_Dictionary>`\ ) |virtual| |required| |const|  |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`_generate_from_path<class_EditorResourcePreviewGenerator_private_method__generate_from_path>`\ (\ path\: :ref:`String<class_String>`, size\: :ref:`Vector2i<class_Vector2i>`, metadata\: :ref:`Dictionary<class_Dictionary>`\ ) |virtual| |const| |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`_generate_small_preview_automatically<class_EditorResourcePreviewGenerator_private_method__generate_small_preview_automatically>`\ (\ ) |virtual| |const|                                                                                         |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`_handles<class_EditorResourcePreviewGenerator_private_method__handles>`\ (\ type\: :ref:`String<class_String>`\ ) |virtual| |required| |const|                                                                                                    |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`request_draw_and_wait<class_EditorResourcePreviewGenerator_method_request_draw_and_wait>`\ (\ viewport\: :ref:`RID<class_RID>`\ ) |const|                                                                                                         |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[bool<class_bool>] **_can_generate_small_preview**\ (\ ) |virtual| |const| [🔗<class_EditorResourcePreviewGenerator_private_method__can_generate_small_preview>]

If this function returns `true`, the generator will call [_generate()<class_EditorResourcePreviewGenerator_private_method__generate>] or [_generate_from_path()<class_EditorResourcePreviewGenerator_private_method__generate_from_path>] for small previews as well.

By default, it returns `false`.


----



[Texture2D<class_Texture2D>] **_generate**\ (\ resource\: [Resource<class_Resource>], size\: [Vector2i<class_Vector2i>], metadata\: [Dictionary<class_Dictionary>]\ ) |virtual| |required| |const| [🔗<class_EditorResourcePreviewGenerator_private_method__generate>]

Generate a preview from a given resource with the specified size. This must always be implemented.

Returning `null` is an OK way to fail and let another generator take care.

Care must be taken because this function is always called from a thread (not the main thread).

\ `metadata` dictionary can be modified to store file-specific metadata that can be used in [EditorResourceTooltipPlugin._make_tooltip_for_path()<class_EditorResourceTooltipPlugin_private_method__make_tooltip_for_path>] (like image size, sample length etc.).


----



[Texture2D<class_Texture2D>] **_generate_from_path**\ (\ path\: [String<class_String>], size\: [Vector2i<class_Vector2i>], metadata\: [Dictionary<class_Dictionary>]\ ) |virtual| |const| [🔗<class_EditorResourcePreviewGenerator_private_method__generate_from_path>]

Generate a preview directly from a path with the specified size. Implementing this is optional, as default code will load and call [_generate()<class_EditorResourcePreviewGenerator_private_method__generate>].

Returning `null` is an OK way to fail and let another generator take care.

Care must be taken because this function is always called from a thread (not the main thread).

\ `metadata` dictionary can be modified to store file-specific metadata that can be used in [EditorResourceTooltipPlugin._make_tooltip_for_path()<class_EditorResourceTooltipPlugin_private_method__make_tooltip_for_path>] (like image size, sample length etc.).


----



[bool<class_bool>] **_generate_small_preview_automatically**\ (\ ) |virtual| |const| [🔗<class_EditorResourcePreviewGenerator_private_method__generate_small_preview_automatically>]

If this function returns `true`, the generator will automatically generate the small previews from the normal preview texture generated by the methods [_generate()<class_EditorResourcePreviewGenerator_private_method__generate>] or [_generate_from_path()<class_EditorResourcePreviewGenerator_private_method__generate_from_path>].

By default, it returns `false`.


----



[bool<class_bool>] **_handles**\ (\ type\: [String<class_String>]\ ) |virtual| |required| |const| [🔗<class_EditorResourcePreviewGenerator_private_method__handles>]

Returns `true` if your generator supports the resource of type `type`.


----



|void| **request_draw_and_wait**\ (\ viewport\: [RID<class_RID>]\ ) |const| [🔗<class_EditorResourcePreviewGenerator_method_request_draw_and_wait>]

Call from within [_generate()<class_EditorResourcePreviewGenerator_private_method__generate>] to request the rendering server draw to the `viewport`.

