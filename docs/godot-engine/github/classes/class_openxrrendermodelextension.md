:github_url: hide



# OpenXRRenderModelExtension

**Inherits:** [OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>] **<** [Object<class_Object>]

This class implements the OpenXR Render Model Extension.


## Description

This class implements the OpenXR Render Model Extension, if enabled it will maintain a list of active render models and provides an interface to the render model data.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`is_active<class_OpenXRRenderModelExtension_method_is_active>`\ (\ ) |const|                                                                                                                                        |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                     | :ref:`render_model_create<class_OpenXRRenderModelExtension_method_render_model_create>`\ (\ render_model_id\: :ref:`int<class_int>`\ )                                                                                   |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`render_model_destroy<class_OpenXRRenderModelExtension_method_render_model_destroy>`\ (\ render_model\: :ref:`RID<class_RID>`\ )                                                                                    |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`RID<class_RID>`\]        | :ref:`render_model_get_all<class_OpenXRRenderModelExtension_method_render_model_get_all>`\ (\ )                                                                                                                          |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                     | :ref:`render_model_get_animatable_node_count<class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_count>`\ (\ render_model\: :ref:`RID<class_RID>`\ ) |const|                                        |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                               | :ref:`render_model_get_animatable_node_name<class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_name>`\ (\ render_model\: :ref:`RID<class_RID>`, index\: :ref:`int<class_int>`\ ) |const|           |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                     | :ref:`render_model_get_animatable_node_transform<class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_transform>`\ (\ render_model\: :ref:`RID<class_RID>`, index\: :ref:`int<class_int>`\ ) |const| |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TrackingConfidence<enum_XRPose_TrackingConfidence>` | :ref:`render_model_get_confidence<class_OpenXRRenderModelExtension_method_render_model_get_confidence>`\ (\ render_model\: :ref:`RID<class_RID>`\ ) |const|                                                              |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                     | :ref:`render_model_get_root_transform<class_OpenXRRenderModelExtension_method_render_model_get_root_transform>`\ (\ render_model\: :ref:`RID<class_RID>`\ ) |const|                                                      |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`         | :ref:`render_model_get_subaction_paths<class_OpenXRRenderModelExtension_method_render_model_get_subaction_paths>`\ (\ render_model\: :ref:`RID<class_RID>`\ )                                                            |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                               | :ref:`render_model_get_top_level_path<class_OpenXRRenderModelExtension_method_render_model_get_top_level_path>`\ (\ render_model\: :ref:`RID<class_RID>`\ ) |const|                                                      |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`render_model_is_animatable_node_visible<class_OpenXRRenderModelExtension_method_render_model_is_animatable_node_visible>`\ (\ render_model\: :ref:`RID<class_RID>`, index\: :ref:`int<class_int>`\ ) |const|       |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Node3D<class_Node3D>`                               | :ref:`render_model_new_scene_instance<class_OpenXRRenderModelExtension_method_render_model_new_scene_instance>`\ (\ render_model\: :ref:`RID<class_RID>`\ ) |const|                                                      |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**render_model_added**\ (\ render_model\: [RID<class_RID>]\ ) [🔗<class_OpenXRRenderModelExtension_signal_render_model_added>]

Emitted when a new render model is added.


----



**render_model_removed**\ (\ render_model\: [RID<class_RID>]\ ) [🔗<class_OpenXRRenderModelExtension_signal_render_model_removed>]

Emitted when a render model is removed.


----



**render_model_top_level_path_changed**\ (\ render_model\: [RID<class_RID>]\ ) [🔗<class_OpenXRRenderModelExtension_signal_render_model_top_level_path_changed>]

Emitted when the top level path associated with a render model changed.


----


## Method Descriptions



[bool<class_bool>] **is_active**\ (\ ) |const| [🔗<class_OpenXRRenderModelExtension_method_is_active>]

Returns `true` if OpenXR's render model extension is supported and enabled.

\ **Note:** This only returns a valid value after OpenXR has been initialized.


----



[RID<class_RID>] **render_model_create**\ (\ render_model_id\: [int<class_int>]\ ) [🔗<class_OpenXRRenderModelExtension_method_render_model_create>]

Creates a render model object within OpenXR using a render model id.

\ **Note:** This function is exposed for dependent OpenXR extensions that provide render model ids to be used with the render model extension.


----



|void| **render_model_destroy**\ (\ render_model\: [RID<class_RID>]\ ) [🔗<class_OpenXRRenderModelExtension_method_render_model_destroy>]

Destroys a render model object within OpenXR that was previously created with [render_model_create()<class_OpenXRRenderModelExtension_method_render_model_create>].

\ **Note:** This function is exposed for dependent OpenXR extensions that provide render model ids to be used with the render model extension.


----



[Array<class_Array>]\[[RID<class_RID>]\] **render_model_get_all**\ (\ ) [🔗<class_OpenXRRenderModelExtension_method_render_model_get_all>]

Returns an array of all currently active render models registered with this extension.


----



[int<class_int>] **render_model_get_animatable_node_count**\ (\ render_model\: [RID<class_RID>]\ ) |const| [🔗<class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_count>]

Returns the number of animatable nodes this render model has.


----



[String<class_String>] **render_model_get_animatable_node_name**\ (\ render_model\: [RID<class_RID>], index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_name>]

Returns the name of the given animatable node.


----



[Transform3D<class_Transform3D>] **render_model_get_animatable_node_transform**\ (\ render_model\: [RID<class_RID>], index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_transform>]

Returns the current local transform for an animatable node. This is updated every frame.


----



[TrackingConfidence<enum_XRPose_TrackingConfidence>] **render_model_get_confidence**\ (\ render_model\: [RID<class_RID>]\ ) |const| [🔗<class_OpenXRRenderModelExtension_method_render_model_get_confidence>]

Returns the tracking confidence of the tracking data for the render model.


----



[Transform3D<class_Transform3D>] **render_model_get_root_transform**\ (\ render_model\: [RID<class_RID>]\ ) |const| [🔗<class_OpenXRRenderModelExtension_method_render_model_get_root_transform>]

Returns the root transform of a render model. This is the tracked position relative to our [XROrigin3D<class_XROrigin3D>] node.


----



[PackedStringArray<class_PackedStringArray>] **render_model_get_subaction_paths**\ (\ render_model\: [RID<class_RID>]\ ) [🔗<class_OpenXRRenderModelExtension_method_render_model_get_subaction_paths>]

Returns a list of active subaction paths for this `render_model`.

\ **Note:** If different devices are bound to your actions than available in suggested interaction bindings, this information shows paths related to the interaction bindings being mimicked by that device.


----



[String<class_String>] **render_model_get_top_level_path**\ (\ render_model\: [RID<class_RID>]\ ) |const| [🔗<class_OpenXRRenderModelExtension_method_render_model_get_top_level_path>]

Returns the top level path associated with this `render_model`. If provided this identifies whether the render model is associated with the player's hands or other body part.


----



[bool<class_bool>] **render_model_is_animatable_node_visible**\ (\ render_model\: [RID<class_RID>], index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRRenderModelExtension_method_render_model_is_animatable_node_visible>]

Returns `true` if this animatable node should be visible.


----



[Node3D<class_Node3D>] **render_model_new_scene_instance**\ (\ render_model\: [RID<class_RID>]\ ) |const| [🔗<class_OpenXRRenderModelExtension_method_render_model_new_scene_instance>]

Returns an instance of a subscene that contains all [MeshInstance3D<class_MeshInstance3D>] nodes that allow you to visualize the render model.

