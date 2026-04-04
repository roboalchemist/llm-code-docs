:github_url: hide



# OpenXRExtensionWrapper

**Inherits:** [Object<class_Object>]

**Inherited By:** [OpenXRAndroidThreadSettingsExtension<class_OpenXRAndroidThreadSettingsExtension>], [OpenXRExtensionWrapperExtension<class_OpenXRExtensionWrapperExtension>], [OpenXRFrameSynthesisExtension<class_OpenXRFrameSynthesisExtension>], [OpenXRFutureExtension<class_OpenXRFutureExtension>], [OpenXRRenderModelExtension<class_OpenXRRenderModelExtension>], [OpenXRSpatialAnchorCapability<class_OpenXRSpatialAnchorCapability>], [OpenXRSpatialEntityExtension<class_OpenXRSpatialEntityExtension>], [OpenXRSpatialMarkerTrackingCapability<class_OpenXRSpatialMarkerTrackingCapability>], [OpenXRSpatialPlaneTrackingCapability<class_OpenXRSpatialPlaneTrackingCapability>]

Allows implementing OpenXR extensions with GDExtension.


## Description

**OpenXRExtensionWrapper** allows implementing OpenXR extensions with GDExtension. The extension should be registered with [register_extension_wrapper()<class_OpenXRExtensionWrapper_method_register_extension_wrapper>].

When [OpenXRInterface<class_OpenXRInterface>] is initialized as the primary interface and any [Viewport<class_Viewport>] has [Viewport.use_xr<class_Viewport_property_use_xr>] set to `true`, OpenXR will become involved in Godot's rendering process. If [ProjectSettings.rendering/driver/threads/thread_model<class_ProjectSettings_property_rendering/driver/threads/thread_model>] is set to "Separate", Godot's renderer will run on its own thread, and special care must be taken in all **OpenXRExtensionWrapper**\ s in order to prevent crashes or unexpected behavior. Some virtual methods will be called on the render thread, and any data they access should not be directly written to on the main thread. This is to prevent two potential issues:

1. Changes intended for the next frame, taking effect on the current frame. When using the "Separate" thread model, the main thread will immediately start working on the next frame while the render thread may still be rendering the current frame. If the main thread changes anything used by the render thread directly, the change could end up being used one frame earlier than intended.

2. Reading and writing to the same data at the same time from different threads can lead to the render thread using data in an invalid state.

In most cases, the solution is to use [RenderingServer.call_on_render_thread()<class_RenderingServer_method_call_on_render_thread>] to schedule [Callable<class_Callable>]\ s to write to any data used on the render thread. When using the "Separate" thread model, these [Callable<class_Callable>]\ s will run after the renderer finishes the current frame and before it starts rendering the next frame. When not using this mode, they'll run immediately, so it's recommended to always use [RenderingServer.call_on_render_thread()<class_RenderingServer_method_call_on_render_thread>] in these cases, which will allow your code to do the right thing regardless of the thread model.

Any virtual methods that run on the render thread will be noted below.


## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_get_composition_layer<class_OpenXRExtensionWrapper_private_method__get_composition_layer>`\ (\ index\: :ref:`int<class_int>`\ ) |virtual|                                                                                                                                        |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_get_composition_layer_count<class_OpenXRExtensionWrapper_private_method__get_composition_layer_count>`\ (\ ) |virtual|                                                                                                                                                           |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_get_composition_layer_order<class_OpenXRExtensionWrapper_private_method__get_composition_layer_order>`\ (\ index\: :ref:`int<class_int>`\ ) |virtual|                                                                                                                            |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`_get_requested_extensions<class_OpenXRExtensionWrapper_private_method__get_requested_extensions>`\ (\ xr_version\: :ref:`int<class_int>`\ ) |virtual|                                                                                                                             |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                | :ref:`_get_suggested_tracker_names<class_OpenXRExtensionWrapper_private_method__get_suggested_tracker_names>`\ (\ ) |virtual|                                                                                                                                                           |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`_get_viewport_composition_layer_extension_properties<class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_properties>`\ (\ ) |virtual|                                                                                                           |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`_get_viewport_composition_layer_extension_property_defaults<class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_property_defaults>`\ (\ ) |virtual|                                                                                             |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_before_instance_created<class_OpenXRExtensionWrapper_private_method__on_before_instance_created>`\ (\ ) |virtual|                                                                                                                                                             |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_on_event_polled<class_OpenXRExtensionWrapper_private_method__on_event_polled>`\ (\ event\: ``const void*``\ ) |virtual|                                                                                                                                                          |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_instance_created<class_OpenXRExtensionWrapper_private_method__on_instance_created>`\ (\ instance\: :ref:`int<class_int>`\ ) |virtual|                                                                                                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_instance_destroyed<class_OpenXRExtensionWrapper_private_method__on_instance_destroyed>`\ (\ ) |virtual|                                                                                                                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_main_swapchains_created<class_OpenXRExtensionWrapper_private_method__on_main_swapchains_created>`\ (\ ) |virtual|                                                                                                                                                             |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_post_draw_viewport<class_OpenXRExtensionWrapper_private_method__on_post_draw_viewport>`\ (\ viewport\: :ref:`RID<class_RID>`\ ) |virtual|                                                                                                                                     |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_pre_draw_viewport<class_OpenXRExtensionWrapper_private_method__on_pre_draw_viewport>`\ (\ viewport\: :ref:`RID<class_RID>`\ ) |virtual|                                                                                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_pre_render<class_OpenXRExtensionWrapper_private_method__on_pre_render>`\ (\ ) |virtual|                                                                                                                                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_process<class_OpenXRExtensionWrapper_private_method__on_process>`\ (\ ) |virtual|                                                                                                                                                                                             |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_register_metadata<class_OpenXRExtensionWrapper_private_method__on_register_metadata>`\ (\ ) |virtual|                                                                                                                                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_session_created<class_OpenXRExtensionWrapper_private_method__on_session_created>`\ (\ session\: :ref:`int<class_int>`\ ) |virtual|                                                                                                                                            |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_session_destroyed<class_OpenXRExtensionWrapper_private_method__on_session_destroyed>`\ (\ ) |virtual|                                                                                                                                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_state_exiting<class_OpenXRExtensionWrapper_private_method__on_state_exiting>`\ (\ ) |virtual|                                                                                                                                                                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_state_focused<class_OpenXRExtensionWrapper_private_method__on_state_focused>`\ (\ ) |virtual|                                                                                                                                                                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_state_idle<class_OpenXRExtensionWrapper_private_method__on_state_idle>`\ (\ ) |virtual|                                                                                                                                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_state_loss_pending<class_OpenXRExtensionWrapper_private_method__on_state_loss_pending>`\ (\ ) |virtual|                                                                                                                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_state_ready<class_OpenXRExtensionWrapper_private_method__on_state_ready>`\ (\ ) |virtual|                                                                                                                                                                                     |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_state_stopping<class_OpenXRExtensionWrapper_private_method__on_state_stopping>`\ (\ ) |virtual|                                                                                                                                                                               |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_state_synchronized<class_OpenXRExtensionWrapper_private_method__on_state_synchronized>`\ (\ ) |virtual|                                                                                                                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_state_visible<class_OpenXRExtensionWrapper_private_method__on_state_visible>`\ (\ ) |virtual|                                                                                                                                                                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_sync_actions<class_OpenXRExtensionWrapper_private_method__on_sync_actions>`\ (\ ) |virtual|                                                                                                                                                                                   |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_on_viewport_composition_layer_destroyed<class_OpenXRExtensionWrapper_private_method__on_viewport_composition_layer_destroyed>`\ (\ layer\: ``const void*``\ ) |virtual|                                                                                                          |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_prepare_view_configuration<class_OpenXRExtensionWrapper_private_method__prepare_view_configuration>`\ (\ view_count\: :ref:`int<class_int>`\ ) |virtual|                                                                                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`_print_view_configuration_info<class_OpenXRExtensionWrapper_private_method__print_view_configuration_info>`\ (\ view\: :ref:`int<class_int>`\ ) |virtual| |const|                                                                                                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_set_android_surface_swapchain_create_info_and_get_next_pointer<class_OpenXRExtensionWrapper_private_method__set_android_surface_swapchain_create_info_and_get_next_pointer>`\ (\ property_values\: :ref:`Dictionary<class_Dictionary>`, next_pointer\: ``void*``\ ) |virtual|    |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_set_frame_end_info_and_get_next_pointer<class_OpenXRExtensionWrapper_private_method__set_frame_end_info_and_get_next_pointer>`\ (\ next_pointer\: ``void*``\ ) |virtual|                                                                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_set_frame_wait_info_and_get_next_pointer<class_OpenXRExtensionWrapper_private_method__set_frame_wait_info_and_get_next_pointer>`\ (\ next_pointer\: ``void*``\ ) |virtual|                                                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_set_hand_joint_locations_and_get_next_pointer<class_OpenXRExtensionWrapper_private_method__set_hand_joint_locations_and_get_next_pointer>`\ (\ hand_index\: :ref:`int<class_int>`, next_pointer\: ``void*``\ ) |virtual|                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_set_instance_create_info_and_get_next_pointer<class_OpenXRExtensionWrapper_private_method__set_instance_create_info_and_get_next_pointer>`\ (\ xr_version\: :ref:`int<class_int>`, next_pointer\: ``void*``\ ) |virtual|                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_set_projection_views_and_get_next_pointer<class_OpenXRExtensionWrapper_private_method__set_projection_views_and_get_next_pointer>`\ (\ view_index\: :ref:`int<class_int>`, next_pointer\: ``void*``\ ) |virtual|                                                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_set_reference_space_create_info_and_get_next_pointer<class_OpenXRExtensionWrapper_private_method__set_reference_space_create_info_and_get_next_pointer>`\ (\ reference_space_type\: :ref:`int<class_int>`, next_pointer\: ``void*``\ ) |virtual|                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_set_session_create_and_get_next_pointer<class_OpenXRExtensionWrapper_private_method__set_session_create_and_get_next_pointer>`\ (\ next_pointer\: ``void*``\ ) |virtual|                                                                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_set_swapchain_create_info_and_get_next_pointer<class_OpenXRExtensionWrapper_private_method__set_swapchain_create_info_and_get_next_pointer>`\ (\ next_pointer\: ``void*``\ ) |virtual|                                                                                           |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_set_system_properties_and_get_next_pointer<class_OpenXRExtensionWrapper_private_method__set_system_properties_and_get_next_pointer>`\ (\ next_pointer\: ``void*``\ ) |virtual|                                                                                                   |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_set_view_configuration_and_get_next_pointer<class_OpenXRExtensionWrapper_private_method__set_view_configuration_and_get_next_pointer>`\ (\ view\: :ref:`int<class_int>`, next_pointer\: ``void*``\ ) |virtual|                                                                   |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_set_view_locate_info_and_get_next_pointer<class_OpenXRExtensionWrapper_private_method__set_view_locate_info_and_get_next_pointer>`\ (\ next_pointer\: ``void*``\ ) |virtual|                                                                                                     |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_set_viewport_composition_layer_and_get_next_pointer<class_OpenXRExtensionWrapper_private_method__set_viewport_composition_layer_and_get_next_pointer>`\ (\ layer\: ``const void*``, property_values\: :ref:`Dictionary<class_Dictionary>`, next_pointer\: ``void*``\ ) |virtual| |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`OpenXRAPIExtension<class_OpenXRAPIExtension>`              | :ref:`get_openxr_api<class_OpenXRExtensionWrapper_method_get_openxr_api>`\ (\ )                                                                                                                                                                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`register_extension_wrapper<class_OpenXRExtensionWrapper_method_register_extension_wrapper>`\ (\ )                                                                                                                                                                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **_get_composition_layer**\ (\ index\: [int<class_int>]\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__get_composition_layer>]

Returns a pointer to an `XrCompositionLayerBaseHeader` struct to provide the given composition layer.

This will only be called if the extension previously registered itself with [OpenXRAPIExtension.register_composition_layer_provider()<class_OpenXRAPIExtension_method_register_composition_layer_provider>].

\ **Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time [_on_pre_render()<class_OpenXRExtensionWrapper_private_method__on_pre_render>] runs.


----



[int<class_int>] **_get_composition_layer_count**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__get_composition_layer_count>]

Returns the number of composition layers this extension wrapper provides via [_get_composition_layer()<class_OpenXRExtensionWrapper_private_method__get_composition_layer>].

This will only be called if the extension previously registered itself with [OpenXRAPIExtension.register_composition_layer_provider()<class_OpenXRAPIExtension_method_register_composition_layer_provider>].

\ **Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time [_on_pre_render()<class_OpenXRExtensionWrapper_private_method__on_pre_render>] runs.


----



[int<class_int>] **_get_composition_layer_order**\ (\ index\: [int<class_int>]\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__get_composition_layer_order>]

Returns an integer that will be used to sort the given composition layer provided via [_get_composition_layer()<class_OpenXRExtensionWrapper_private_method__get_composition_layer>]. Lower numbers will move the layer to the front of the list, and higher numbers to the end. The default projection layer has an order of `0`, so layers provided by this method should probably be above or below (but not exactly) `0`.

This will only be called if the extension previously registered itself with [OpenXRAPIExtension.register_composition_layer_provider()<class_OpenXRAPIExtension_method_register_composition_layer_provider>].

\ **Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time [_on_pre_render()<class_OpenXRExtensionWrapper_private_method__on_pre_render>] runs.


----



[Dictionary<class_Dictionary>] **_get_requested_extensions**\ (\ xr_version\: [int<class_int>]\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__get_requested_extensions>]

Returns a [Dictionary<class_Dictionary>] of OpenXR extensions related to this extension. `xr_version` specifies the OpenXR version we're instantiating. This will be zero if the editor requests this list to flag supported features. The [Dictionary<class_Dictionary>] should contain the name of the extension, mapped to a `bool *` cast to an integer:

- If the `bool *` is a `nullptr` this extension is mandatory.

- If the `bool *` points to a boolean, the boolean will be updated to `true` if the extension is enabled.


----



[PackedStringArray<class_PackedStringArray>] **_get_suggested_tracker_names**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__get_suggested_tracker_names>]

Returns a [PackedStringArray<class_PackedStringArray>] of positional tracker names that are used within the extension wrapper.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **_get_viewport_composition_layer_extension_properties**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_properties>]

Gets an array of [Dictionary<class_Dictionary>]\ s that represent properties, just like [Object._get_property_list()<class_Object_private_method__get_property_list>], that will be added to [OpenXRCompositionLayer<class_OpenXRCompositionLayer>] nodes.

\ **Note:** This virtual method will be called on the render thread.


----



[Dictionary<class_Dictionary>] **_get_viewport_composition_layer_extension_property_defaults**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_property_defaults>]

Gets a [Dictionary<class_Dictionary>] containing the default values for the properties returned by [_get_viewport_composition_layer_extension_properties()<class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_properties>].


----



|void| **_on_before_instance_created**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_before_instance_created>]

Called before the OpenXR instance is created.

\ **Note:** This virtual method will be called on the main thread, however, it will be called *before* OpenXR becomes involved in rendering, so it is safe to write to data that will be used by the render thread.


----



[bool<class_bool>] **_on_event_polled**\ (\ event\: `const void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_event_polled>]

Called when there is an OpenXR event to process. When implementing, return `true` if the event was handled, return `false` otherwise.


----



|void| **_on_instance_created**\ (\ instance\: [int<class_int>]\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_instance_created>]

Called right after the OpenXR instance is created.

\ **Note:** This virtual method will be called on the main thread, however, it will be called *before* OpenXR becomes involved in rendering, so it is safe to write to data that will be used by the render thread.


----



|void| **_on_instance_destroyed**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_instance_destroyed>]

Called right before the OpenXR instance is destroyed.

\ **Note:** This virtual method will be called on the main thread, however, it will be called *after* OpenXR is done being involved in rendering, so it is safe to write to data that was used by the render thread.


----



|void| **_on_main_swapchains_created**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_main_swapchains_created>]

Called right after the main swapchains are (re)created.

\ **Note:** This virtual method will be called on the render thread.


----



|void| **_on_post_draw_viewport**\ (\ viewport\: [RID<class_RID>]\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_post_draw_viewport>]

Called right after the given viewport is rendered.

\ **Note:** The draw commands might only be queued at this point, not executed.

\ **Note:** This virtual method will be called on the render thread.


----



|void| **_on_pre_draw_viewport**\ (\ viewport\: [RID<class_RID>]\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_pre_draw_viewport>]

Called right before the given viewport is rendered.

\ **Note:** This virtual method will be called on the render thread.


----



|void| **_on_pre_render**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_pre_render>]

Called right before the XR viewports begin their rendering step.

\ **Note:** This virtual method will be called on the render thread.


----



|void| **_on_process**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_process>]

Called as part of the OpenXR process handling. This happens right before general and physics processing steps of the main loop. During this step controller data is queried and made available to game logic.


----



|void| **_on_register_metadata**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_register_metadata>]

Allows extensions to register additional controller metadata. This function is called even when the OpenXR API is not constructed as the metadata needs to be available to the editor.

Extensions should also provide metadata regardless of whether they are supported on the host system. The controller data is used to setup action maps for users who may have access to the relevant hardware.


----



|void| **_on_session_created**\ (\ session\: [int<class_int>]\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_session_created>]

Called right after the OpenXR session is created.

\ **Note:** This virtual method will be called on the main thread, however, it will be called *before* OpenXR becomes involved in rendering, so it is safe to write to data that will be used by the render thread.


----



|void| **_on_session_destroyed**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_session_destroyed>]

Called right before the OpenXR session is destroyed.

\ **Note:** This virtual method will be called on the main thread, however, it will be called *after* OpenXR is done being involved in rendering, so it is safe to write to data that was used by the render thread.


----



|void| **_on_state_exiting**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_state_exiting>]

Called when the OpenXR session state is changed to exiting.


----



|void| **_on_state_focused**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_state_focused>]

Called when the OpenXR session state is changed to focused. This state is the active state when the game runs.


----



|void| **_on_state_idle**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_state_idle>]

Called when the OpenXR session state is changed to idle.


----



|void| **_on_state_loss_pending**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_state_loss_pending>]

Called when the OpenXR session state is changed to loss pending.


----



|void| **_on_state_ready**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_state_ready>]

Called when the OpenXR session state is changed to ready. This means OpenXR is ready to set up the session.


----



|void| **_on_state_stopping**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_state_stopping>]

Called when the OpenXR session state is changed to stopping.


----



|void| **_on_state_synchronized**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_state_synchronized>]

Called when the OpenXR session state is changed to synchronized. OpenXR also returns to this state when the application loses focus.


----



|void| **_on_state_visible**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_state_visible>]

Called when the OpenXR session state is changed to visible. This means OpenXR is now ready to receive frames.


----



|void| **_on_sync_actions**\ (\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_sync_actions>]

Called when OpenXR has performed its action sync.


----



|void| **_on_viewport_composition_layer_destroyed**\ (\ layer\: `const void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__on_viewport_composition_layer_destroyed>]

Called when a composition layer created via [OpenXRCompositionLayer<class_OpenXRCompositionLayer>] is destroyed.

\ `layer` is a pointer to an `XrCompositionLayerBaseHeader` struct.


----



|void| **_prepare_view_configuration**\ (\ view_count\: [int<class_int>]\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__prepare_view_configuration>]

Called before [_set_view_configuration_and_get_next_pointer()<class_OpenXRExtensionWrapper_private_method__set_view_configuration_and_get_next_pointer>] to allow the extension to reserve data for the given number of views.


----



|void| **_print_view_configuration_info**\ (\ view\: [int<class_int>]\ ) |virtual| |const| [🔗<class_OpenXRExtensionWrapper_private_method__print_view_configuration_info>]

Called to allow an extension to print additional information about its view configuration, if applicable. This will only be called if verbose output is enabled.


----



[int<class_int>] **_set_android_surface_swapchain_create_info_and_get_next_pointer**\ (\ property_values\: [Dictionary<class_Dictionary>], next_pointer\: `void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__set_android_surface_swapchain_create_info_and_get_next_pointer>]

Add additional data structures to Android surface swapchains created by [OpenXRCompositionLayer<class_OpenXRCompositionLayer>].

\ `property_values` contains the values of the properties returned by [_get_viewport_composition_layer_extension_properties()<class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_properties>].

\ **Note:** This virtual method will be called on the render thread.


----



[int<class_int>] **_set_frame_end_info_and_get_next_pointer**\ (\ next_pointer\: `void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__set_frame_end_info_and_get_next_pointer>]

Add additional data structures to `XrFrameEndInfo`.

This will only be called if the extension previously registered itself with [OpenXRAPIExtension.register_frame_info_extension()<class_OpenXRAPIExtension_method_register_frame_info_extension>].

\ **Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time [_on_pre_render()<class_OpenXRExtensionWrapper_private_method__on_pre_render>] runs.


----



[int<class_int>] **_set_frame_wait_info_and_get_next_pointer**\ (\ next_pointer\: `void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__set_frame_wait_info_and_get_next_pointer>]

Add additional data structures to `XrFrameWaitInfo`.

This will only be called if the extension previously registered itself with [OpenXRAPIExtension.register_frame_info_extension()<class_OpenXRAPIExtension_method_register_frame_info_extension>].

\ **Note:** This virtual method will be called on the render thread.


----



[int<class_int>] **_set_hand_joint_locations_and_get_next_pointer**\ (\ hand_index\: [int<class_int>], next_pointer\: `void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__set_hand_joint_locations_and_get_next_pointer>]

Add additional data structures when each hand tracker is created.


----



[int<class_int>] **_set_instance_create_info_and_get_next_pointer**\ (\ xr_version\: [int<class_int>], next_pointer\: `void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__set_instance_create_info_and_get_next_pointer>]

Add additional data structures when the OpenXR instance is created. `xr_version` specifies the OpenXR version we're instantiating.


----



[int<class_int>] **_set_projection_views_and_get_next_pointer**\ (\ view_index\: [int<class_int>], next_pointer\: `void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__set_projection_views_and_get_next_pointer>]

Add additional data structures to the projection view of the given `view_index`.

\ **Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time [_on_pre_render()<class_OpenXRExtensionWrapper_private_method__on_pre_render>] runs.


----



[int<class_int>] **_set_reference_space_create_info_and_get_next_pointer**\ (\ reference_space_type\: [int<class_int>], next_pointer\: `void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__set_reference_space_create_info_and_get_next_pointer>]

Add additional data structures to `XrReferenceSpaceCreateInfo`.


----



[int<class_int>] **_set_session_create_and_get_next_pointer**\ (\ next_pointer\: `void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__set_session_create_and_get_next_pointer>]

Add additional data structures when the OpenXR session is created.


----



[int<class_int>] **_set_swapchain_create_info_and_get_next_pointer**\ (\ next_pointer\: `void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__set_swapchain_create_info_and_get_next_pointer>]

Add additional data structures when creating OpenXR swapchains.


----



[int<class_int>] **_set_system_properties_and_get_next_pointer**\ (\ next_pointer\: `void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__set_system_properties_and_get_next_pointer>]

Add additional data structures when querying OpenXR system abilities.


----



[int<class_int>] **_set_view_configuration_and_get_next_pointer**\ (\ view\: [int<class_int>], next_pointer\: `void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__set_view_configuration_and_get_next_pointer>]

Add additional data structures when querying OpenXR view configuration.


----



[int<class_int>] **_set_view_locate_info_and_get_next_pointer**\ (\ next_pointer\: `void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__set_view_locate_info_and_get_next_pointer>]

Add additional data structures to `XrViewLocateInfo`.

This will only be called if the extension previously registered itself with [OpenXRAPIExtension.register_frame_info_extension()<class_OpenXRAPIExtension_method_register_frame_info_extension>].

\ **Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time [_on_pre_render()<class_OpenXRExtensionWrapper_private_method__on_pre_render>] runs.


----



[int<class_int>] **_set_viewport_composition_layer_and_get_next_pointer**\ (\ layer\: `const void*`, property_values\: [Dictionary<class_Dictionary>], next_pointer\: `void*`\ ) |virtual| [🔗<class_OpenXRExtensionWrapper_private_method__set_viewport_composition_layer_and_get_next_pointer>]

Add additional data structures to composition layers created by [OpenXRCompositionLayer<class_OpenXRCompositionLayer>].

\ `property_values` contains the values of the properties returned by [_get_viewport_composition_layer_extension_properties()<class_OpenXRExtensionWrapper_private_method__get_viewport_composition_layer_extension_properties>].

\ `layer` is a pointer to an `XrCompositionLayerBaseHeader` struct.

\ **Note:** This virtual method will be called on the render thread. Additionally, the data it returns will be used shortly after this method is called, so it needs to remain valid until the next time [_on_pre_render()<class_OpenXRExtensionWrapper_private_method__on_pre_render>] runs.


----



[OpenXRAPIExtension<class_OpenXRAPIExtension>] **get_openxr_api**\ (\ ) [🔗<class_OpenXRExtensionWrapper_method_get_openxr_api>]

Returns the created [OpenXRAPIExtension<class_OpenXRAPIExtension>], which can be used to access the OpenXR API.


----



|void| **register_extension_wrapper**\ (\ ) [🔗<class_OpenXRExtensionWrapper_method_register_extension_wrapper>]

Registers the extension. This should happen at core module initialization level.

\ **Note:** This cannot be called once OpenXR has been initialized.

