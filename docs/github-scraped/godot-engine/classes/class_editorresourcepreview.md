:github_url: hide



# EditorResourcePreview

**Inherits:** [Node<class_Node>] **<** [Object<class_Object>]

A node used to generate previews of resources or files.


## Description

This node is used to generate previews for resources or files.

\ **Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_resource_previewer()<class_EditorInterface_method_get_resource_previewer>].


## Methods

> **TABLE**
> :widths: auto
>
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`add_preview_generator<class_EditorResourcePreview_method_add_preview_generator>`\ (\ generator\: :ref:`EditorResourcePreviewGenerator<class_EditorResourcePreviewGenerator>`\ )                                                                                                           |
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`check_for_invalidation<class_EditorResourcePreview_method_check_for_invalidation>`\ (\ path\: :ref:`String<class_String>`\ )                                                                                                                                                              |
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`queue_edited_resource_preview<class_EditorResourcePreview_method_queue_edited_resource_preview>`\ (\ resource\: :ref:`Resource<class_Resource>`, receiver\: :ref:`Object<class_Object>`, receiver_func\: :ref:`StringName<class_StringName>`, userdata\: :ref:`Variant<class_Variant>`\ ) |
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`queue_resource_preview<class_EditorResourcePreview_method_queue_resource_preview>`\ (\ path\: :ref:`String<class_String>`, receiver\: :ref:`Object<class_Object>`, receiver_func\: :ref:`StringName<class_StringName>`, userdata\: :ref:`Variant<class_Variant>`\ )                       |
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`remove_preview_generator<class_EditorResourcePreview_method_remove_preview_generator>`\ (\ generator\: :ref:`EditorResourcePreviewGenerator<class_EditorResourcePreviewGenerator>`\ )                                                                                                     |
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**preview_invalidated**\ (\ path\: [String<class_String>]\ ) [🔗<class_EditorResourcePreview_signal_preview_invalidated>]

Emitted if a preview was invalidated (changed). `path` corresponds to the path of the preview.


----


## Method Descriptions



|void| **add_preview_generator**\ (\ generator\: [EditorResourcePreviewGenerator<class_EditorResourcePreviewGenerator>]\ ) [🔗<class_EditorResourcePreview_method_add_preview_generator>]

Create an own, custom preview generator.


----



|void| **check_for_invalidation**\ (\ path\: [String<class_String>]\ ) [🔗<class_EditorResourcePreview_method_check_for_invalidation>]

Check if the resource changed, if so, it will be invalidated and the corresponding signal emitted.


----



|void| **queue_edited_resource_preview**\ (\ resource\: [Resource<class_Resource>], receiver\: [Object<class_Object>], receiver_func\: [StringName<class_StringName>], userdata\: [Variant<class_Variant>]\ ) [🔗<class_EditorResourcePreview_method_queue_edited_resource_preview>]

Queue the `resource` being edited for preview. Once the preview is ready, the `receiver`'s `receiver_func` will be called. The `receiver_func` must take the following four arguments: [String<class_String>] path, [Texture2D<class_Texture2D>] preview, [Texture2D<class_Texture2D>] thumbnail_preview, [Variant<class_Variant>] userdata. `userdata` can be anything, and will be returned when `receiver_func` is called.

\ **Note:** If it was not possible to create the preview the `receiver_func` will still be called, but the preview will be `null`.


----



|void| **queue_resource_preview**\ (\ path\: [String<class_String>], receiver\: [Object<class_Object>], receiver_func\: [StringName<class_StringName>], userdata\: [Variant<class_Variant>]\ ) [🔗<class_EditorResourcePreview_method_queue_resource_preview>]

Queue a resource file located at `path` for preview. Once the preview is ready, the `receiver`'s `receiver_func` will be called. The `receiver_func` must take the following four arguments: [String<class_String>] path, [Texture2D<class_Texture2D>] preview, [Texture2D<class_Texture2D>] thumbnail_preview, [Variant<class_Variant>] userdata. `userdata` can be anything, and will be returned when `receiver_func` is called.

\ **Note:** If it was not possible to create the preview the `receiver_func` will still be called, but the preview will be `null`.


----



|void| **remove_preview_generator**\ (\ generator\: [EditorResourcePreviewGenerator<class_EditorResourcePreviewGenerator>]\ ) [🔗<class_EditorResourcePreview_method_remove_preview_generator>]

Removes a custom preview generator.

