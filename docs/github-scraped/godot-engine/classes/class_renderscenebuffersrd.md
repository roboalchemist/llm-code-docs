:github_url: hide



# RenderSceneBuffersRD

**Inherits:** [RenderSceneBuffers<class_RenderSceneBuffers>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Render scene buffer implementation for the RenderingDevice based renderers.


## Description

This object manages all 3D rendering buffers for the rendering device based renderers. An instance of this object is created for every viewport that has 3D rendering enabled. See also [RenderSceneBuffers<class_RenderSceneBuffers>].

All buffers are organized in **contexts**. The default context is called **render_buffers** and can contain amongst others the color buffer, depth buffer, velocity buffers, VRS density map and MSAA variants of these buffers.

Buffers are only guaranteed to exist during rendering of the viewport.

\ **Note:** This is an internal rendering server object. Do not instantiate this class from a script.


## Methods

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                   | :ref:`clear_context<class_RenderSceneBuffersRD_method_clear_context>`\ (\ context\: :ref:`StringName<class_StringName>`\ )                                                                                                                                                                                                                                                                                                                                                                                                                     |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                    | :ref:`create_texture<class_RenderSceneBuffersRD_method_create_texture>`\ (\ context\: :ref:`StringName<class_StringName>`, name\: :ref:`StringName<class_StringName>`, data_format\: :ref:`DataFormat<enum_RenderingDevice_DataFormat>`, usage_bits\: :ref:`int<class_int>`, texture_samples\: :ref:`TextureSamples<enum_RenderingDevice_TextureSamples>`, size\: :ref:`Vector2i<class_Vector2i>`, layers\: :ref:`int<class_int>`, mipmaps\: :ref:`int<class_int>`, unique\: :ref:`bool<class_bool>`, discardable\: :ref:`bool<class_bool>`\ ) |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                    | :ref:`create_texture_from_format<class_RenderSceneBuffersRD_method_create_texture_from_format>`\ (\ context\: :ref:`StringName<class_StringName>`, name\: :ref:`StringName<class_StringName>`, format\: :ref:`RDTextureFormat<class_RDTextureFormat>`, view\: :ref:`RDTextureView<class_RDTextureView>`, unique\: :ref:`bool<class_bool>`\ )                                                                                                                                                                                                   |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                    | :ref:`create_texture_view<class_RenderSceneBuffersRD_method_create_texture_view>`\ (\ context\: :ref:`StringName<class_StringName>`, name\: :ref:`StringName<class_StringName>`, view_name\: :ref:`StringName<class_StringName>`, view\: :ref:`RDTextureView<class_RDTextureView>`\ )                                                                                                                                                                                                                                                          |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                    | :ref:`get_color_layer<class_RenderSceneBuffersRD_method_get_color_layer>`\ (\ layer\: :ref:`int<class_int>`, msaa\: :ref:`bool<class_bool>` = false\ )                                                                                                                                                                                                                                                                                                                                                                                         |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                    | :ref:`get_color_texture<class_RenderSceneBuffersRD_method_get_color_texture>`\ (\ msaa\: :ref:`bool<class_bool>` = false\ )                                                                                                                                                                                                                                                                                                                                                                                                                    |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                    | :ref:`get_depth_layer<class_RenderSceneBuffersRD_method_get_depth_layer>`\ (\ layer\: :ref:`int<class_int>`, msaa\: :ref:`bool<class_bool>` = false\ )                                                                                                                                                                                                                                                                                                                                                                                         |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                    | :ref:`get_depth_texture<class_RenderSceneBuffersRD_method_get_depth_texture>`\ (\ msaa\: :ref:`bool<class_bool>` = false\ )                                                                                                                                                                                                                                                                                                                                                                                                                    |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                                | :ref:`get_fsr_sharpness<class_RenderSceneBuffersRD_method_get_fsr_sharpness>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>`                                          | :ref:`get_internal_size<class_RenderSceneBuffersRD_method_get_internal_size>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ViewportMSAA<enum_RenderingServer_ViewportMSAA>`                   | :ref:`get_msaa_3d<class_RenderSceneBuffersRD_method_get_msaa_3d>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                    | :ref:`get_render_target<class_RenderSceneBuffersRD_method_get_render_target>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>` | :ref:`get_scaling_3d_mode<class_RenderSceneBuffersRD_method_get_scaling_3d_mode>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>` | :ref:`get_screen_space_aa<class_RenderSceneBuffersRD_method_get_screen_space_aa>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>`                                          | :ref:`get_target_size<class_RenderSceneBuffersRD_method_get_target_size>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                    | :ref:`get_texture<class_RenderSceneBuffersRD_method_get_texture>`\ (\ context\: :ref:`StringName<class_StringName>`, name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                     |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RDTextureFormat<class_RDTextureFormat>`                            | :ref:`get_texture_format<class_RenderSceneBuffersRD_method_get_texture_format>`\ (\ context\: :ref:`StringName<class_StringName>`, name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                       |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TextureSamples<enum_RenderingDevice_TextureSamples>`               | :ref:`get_texture_samples<class_RenderSceneBuffersRD_method_get_texture_samples>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                    | :ref:`get_texture_slice<class_RenderSceneBuffersRD_method_get_texture_slice>`\ (\ context\: :ref:`StringName<class_StringName>`, name\: :ref:`StringName<class_StringName>`, layer\: :ref:`int<class_int>`, mipmap\: :ref:`int<class_int>`, layers\: :ref:`int<class_int>`, mipmaps\: :ref:`int<class_int>`\ )                                                                                                                                                                                                                                 |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>`                                          | :ref:`get_texture_slice_size<class_RenderSceneBuffersRD_method_get_texture_slice_size>`\ (\ context\: :ref:`StringName<class_StringName>`, name\: :ref:`StringName<class_StringName>`, mipmap\: :ref:`int<class_int>`\ )                                                                                                                                                                                                                                                                                                                       |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                    | :ref:`get_texture_slice_view<class_RenderSceneBuffersRD_method_get_texture_slice_view>`\ (\ context\: :ref:`StringName<class_StringName>`, name\: :ref:`StringName<class_StringName>`, layer\: :ref:`int<class_int>`, mipmap\: :ref:`int<class_int>`, layers\: :ref:`int<class_int>`, mipmaps\: :ref:`int<class_int>`, view\: :ref:`RDTextureView<class_RDTextureView>`\ )                                                                                                                                                                     |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                  | :ref:`get_use_debanding<class_RenderSceneBuffersRD_method_get_use_debanding>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                  | :ref:`get_use_taa<class_RenderSceneBuffersRD_method_get_use_taa>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                    | :ref:`get_velocity_layer<class_RenderSceneBuffersRD_method_get_velocity_layer>`\ (\ layer\: :ref:`int<class_int>`, msaa\: :ref:`bool<class_bool>` = false\ )                                                                                                                                                                                                                                                                                                                                                                                   |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                    | :ref:`get_velocity_texture<class_RenderSceneBuffersRD_method_get_velocity_texture>`\ (\ msaa\: :ref:`bool<class_bool>` = false\ )                                                                                                                                                                                                                                                                                                                                                                                                              |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                    | :ref:`get_view_count<class_RenderSceneBuffersRD_method_get_view_count>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                  | :ref:`has_texture<class_RenderSceneBuffersRD_method_has_texture>`\ (\ context\: :ref:`StringName<class_StringName>`, name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                     |
> +--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **clear_context**\ (\ context\: [StringName<class_StringName>]\ ) [🔗<class_RenderSceneBuffersRD_method_clear_context>]

Frees all buffers related to this context.


----



[RID<class_RID>] **create_texture**\ (\ context\: [StringName<class_StringName>], name\: [StringName<class_StringName>], data_format\: [DataFormat<enum_RenderingDevice_DataFormat>], usage_bits\: [int<class_int>], texture_samples\: [TextureSamples<enum_RenderingDevice_TextureSamples>], size\: [Vector2i<class_Vector2i>], layers\: [int<class_int>], mipmaps\: [int<class_int>], unique\: [bool<class_bool>], discardable\: [bool<class_bool>]\ ) [🔗<class_RenderSceneBuffersRD_method_create_texture>]

Create a new texture with the given definition and cache this under the given name. Will return the existing texture if it already exists.


----



[RID<class_RID>] **create_texture_from_format**\ (\ context\: [StringName<class_StringName>], name\: [StringName<class_StringName>], format\: [RDTextureFormat<class_RDTextureFormat>], view\: [RDTextureView<class_RDTextureView>], unique\: [bool<class_bool>]\ ) [🔗<class_RenderSceneBuffersRD_method_create_texture_from_format>]

Create a new texture using the given format and view and cache this under the given name. Will return the existing texture if it already exists.


----



[RID<class_RID>] **create_texture_view**\ (\ context\: [StringName<class_StringName>], name\: [StringName<class_StringName>], view_name\: [StringName<class_StringName>], view\: [RDTextureView<class_RDTextureView>]\ ) [🔗<class_RenderSceneBuffersRD_method_create_texture_view>]

Create a new texture view for an existing texture and cache this under the given `view_name`. Will return the existing texture view if it already exists. Will error if the source texture doesn't exist.


----



[RID<class_RID>] **get_color_layer**\ (\ layer\: [int<class_int>], msaa\: [bool<class_bool>] = false\ ) [🔗<class_RenderSceneBuffersRD_method_get_color_layer>]

Returns the specified layer from the color texture we are rendering 3D content to.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.


----



[RID<class_RID>] **get_color_texture**\ (\ msaa\: [bool<class_bool>] = false\ ) [🔗<class_RenderSceneBuffersRD_method_get_color_texture>]

Returns the color texture we are rendering 3D content to. If multiview is used this will be a texture array with all views.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.


----



[RID<class_RID>] **get_depth_layer**\ (\ layer\: [int<class_int>], msaa\: [bool<class_bool>] = false\ ) [🔗<class_RenderSceneBuffersRD_method_get_depth_layer>]

Returns the specified layer from the depth texture we are rendering 3D content to.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.


----



[RID<class_RID>] **get_depth_texture**\ (\ msaa\: [bool<class_bool>] = false\ ) [🔗<class_RenderSceneBuffersRD_method_get_depth_texture>]

Returns the depth texture we are rendering 3D content to. If multiview is used this will be a texture array with all views.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.


----



[float<class_float>] **get_fsr_sharpness**\ (\ ) |const| [🔗<class_RenderSceneBuffersRD_method_get_fsr_sharpness>]

Returns the FSR sharpness value used while rendering the 3D content (if [get_scaling_3d_mode()<class_RenderSceneBuffersRD_method_get_scaling_3d_mode>] is an FSR mode).


----



[Vector2i<class_Vector2i>] **get_internal_size**\ (\ ) |const| [🔗<class_RenderSceneBuffersRD_method_get_internal_size>]

Returns the internal size of the render buffer (size before upscaling) with which textures are created by default.


----



[ViewportMSAA<enum_RenderingServer_ViewportMSAA>] **get_msaa_3d**\ (\ ) |const| [🔗<class_RenderSceneBuffersRD_method_get_msaa_3d>]

Returns the applied 3D MSAA mode for this viewport.


----



[RID<class_RID>] **get_render_target**\ (\ ) |const| [🔗<class_RenderSceneBuffersRD_method_get_render_target>]

Returns the render target associated with this buffers object.


----



[ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>] **get_scaling_3d_mode**\ (\ ) |const| [🔗<class_RenderSceneBuffersRD_method_get_scaling_3d_mode>]

Returns the scaling mode used for upscaling.


----



[ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>] **get_screen_space_aa**\ (\ ) |const| [🔗<class_RenderSceneBuffersRD_method_get_screen_space_aa>]

Returns the screen-space antialiasing method applied.


----



[Vector2i<class_Vector2i>] **get_target_size**\ (\ ) |const| [🔗<class_RenderSceneBuffersRD_method_get_target_size>]

Returns the target size of the render buffer (size after upscaling).


----



[RID<class_RID>] **get_texture**\ (\ context\: [StringName<class_StringName>], name\: [StringName<class_StringName>]\ ) |const| [🔗<class_RenderSceneBuffersRD_method_get_texture>]

Returns a cached texture with this name.


----



[RDTextureFormat<class_RDTextureFormat>] **get_texture_format**\ (\ context\: [StringName<class_StringName>], name\: [StringName<class_StringName>]\ ) |const| [🔗<class_RenderSceneBuffersRD_method_get_texture_format>]

Returns the texture format information with which a cached texture was created.


----



[TextureSamples<enum_RenderingDevice_TextureSamples>] **get_texture_samples**\ (\ ) |const| [🔗<class_RenderSceneBuffersRD_method_get_texture_samples>]

Returns the number of MSAA samples used.


----



[RID<class_RID>] **get_texture_slice**\ (\ context\: [StringName<class_StringName>], name\: [StringName<class_StringName>], layer\: [int<class_int>], mipmap\: [int<class_int>], layers\: [int<class_int>], mipmaps\: [int<class_int>]\ ) [🔗<class_RenderSceneBuffersRD_method_get_texture_slice>]

Returns a specific slice (layer or mipmap) for a cached texture.


----



[Vector2i<class_Vector2i>] **get_texture_slice_size**\ (\ context\: [StringName<class_StringName>], name\: [StringName<class_StringName>], mipmap\: [int<class_int>]\ ) [🔗<class_RenderSceneBuffersRD_method_get_texture_slice_size>]

Returns the texture size of a given slice of a cached texture.


----



[RID<class_RID>] **get_texture_slice_view**\ (\ context\: [StringName<class_StringName>], name\: [StringName<class_StringName>], layer\: [int<class_int>], mipmap\: [int<class_int>], layers\: [int<class_int>], mipmaps\: [int<class_int>], view\: [RDTextureView<class_RDTextureView>]\ ) [🔗<class_RenderSceneBuffersRD_method_get_texture_slice_view>]

Returns a specific view of a slice (layer or mipmap) for a cached texture.


----



[bool<class_bool>] **get_use_debanding**\ (\ ) |const| [🔗<class_RenderSceneBuffersRD_method_get_use_debanding>]

Returns `true` if debanding is enabled.


----



[bool<class_bool>] **get_use_taa**\ (\ ) |const| [🔗<class_RenderSceneBuffersRD_method_get_use_taa>]

Returns `true` if TAA is enabled.


----



[RID<class_RID>] **get_velocity_layer**\ (\ layer\: [int<class_int>], msaa\: [bool<class_bool>] = false\ ) [🔗<class_RenderSceneBuffersRD_method_get_velocity_layer>]

Returns the specified layer from the velocity texture we are rendering 3D content to.


----



[RID<class_RID>] **get_velocity_texture**\ (\ msaa\: [bool<class_bool>] = false\ ) [🔗<class_RenderSceneBuffersRD_method_get_velocity_texture>]

Returns the velocity texture we are rendering 3D content to. If multiview is used this will be a texture array with all views.

If `msaa` is **true** and MSAA is enabled, this returns the MSAA variant of the buffer.


----



[int<class_int>] **get_view_count**\ (\ ) |const| [🔗<class_RenderSceneBuffersRD_method_get_view_count>]

Returns the view count for the associated viewport.


----



[bool<class_bool>] **has_texture**\ (\ context\: [StringName<class_StringName>], name\: [StringName<class_StringName>]\ ) |const| [🔗<class_RenderSceneBuffersRD_method_has_texture>]

Returns `true` if a cached texture exists for this name.

