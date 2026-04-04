:github_url: hide



# RenderSceneBuffersConfiguration

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Configuration object used to setup a [RenderSceneBuffers<class_RenderSceneBuffers>] object.


## Description

This configuration object is created and populated by the render engine on a viewport change and used to (re)configure a [RenderSceneBuffers<class_RenderSceneBuffers>] object.


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+--------------------+
> | :ref:`ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>` | :ref:`anisotropic_filtering_level<class_RenderSceneBuffersConfiguration_property_anisotropic_filtering_level>` | ``2``              |
> +----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+--------------------+
> | :ref:`float<class_float>`                                                              | :ref:`fsr_sharpness<class_RenderSceneBuffersConfiguration_property_fsr_sharpness>`                             | ``0.0``            |
> +----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+--------------------+
> | :ref:`Vector2i<class_Vector2i>`                                                        | :ref:`internal_size<class_RenderSceneBuffersConfiguration_property_internal_size>`                             | ``Vector2i(0, 0)`` |
> +----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+--------------------+
> | :ref:`ViewportMSAA<enum_RenderingServer_ViewportMSAA>`                                 | :ref:`msaa_3d<class_RenderSceneBuffersConfiguration_property_msaa_3d>`                                         | ``0``              |
> +----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+--------------------+
> | :ref:`RID<class_RID>`                                                                  | :ref:`render_target<class_RenderSceneBuffersConfiguration_property_render_target>`                             | ``RID()``          |
> +----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+--------------------+
> | :ref:`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`               | :ref:`scaling_3d_mode<class_RenderSceneBuffersConfiguration_property_scaling_3d_mode>`                         | ``255``            |
> +----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+--------------------+
> | :ref:`ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>`               | :ref:`screen_space_aa<class_RenderSceneBuffersConfiguration_property_screen_space_aa>`                         | ``0``              |
> +----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+--------------------+
> | :ref:`Vector2i<class_Vector2i>`                                                        | :ref:`target_size<class_RenderSceneBuffersConfiguration_property_target_size>`                                 | ``Vector2i(0, 0)`` |
> +----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+--------------------+
> | :ref:`float<class_float>`                                                              | :ref:`texture_mipmap_bias<class_RenderSceneBuffersConfiguration_property_texture_mipmap_bias>`                 | ``0.0``            |
> +----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+--------------------+
> | :ref:`int<class_int>`                                                                  | :ref:`view_count<class_RenderSceneBuffersConfiguration_property_view_count>`                                   | ``1``              |
> +----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+--------------------+
>

----


## Property Descriptions



[ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>] **anisotropic_filtering_level** = `2` [🔗<class_RenderSceneBuffersConfiguration_property_anisotropic_filtering_level>]


- |void| **set_anisotropic_filtering_level**\ (\ value\: [ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>]\ )
- [ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>] **get_anisotropic_filtering_level**\ (\ )

Level of the anisotropic filter.


----



[float<class_float>] **fsr_sharpness** = `0.0` [🔗<class_RenderSceneBuffersConfiguration_property_fsr_sharpness>]


- |void| **set_fsr_sharpness**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_fsr_sharpness**\ (\ )

FSR Sharpness applicable if FSR upscaling is used.


----



[Vector2i<class_Vector2i>] **internal_size** = `Vector2i(0, 0)` [🔗<class_RenderSceneBuffersConfiguration_property_internal_size>]


- |void| **set_internal_size**\ (\ value\: [Vector2i<class_Vector2i>]\ )
- [Vector2i<class_Vector2i>] **get_internal_size**\ (\ )

The size of the 3D render buffer used for rendering.


----



[ViewportMSAA<enum_RenderingServer_ViewportMSAA>] **msaa_3d** = `0` [🔗<class_RenderSceneBuffersConfiguration_property_msaa_3d>]


- |void| **set_msaa_3d**\ (\ value\: [ViewportMSAA<enum_RenderingServer_ViewportMSAA>]\ )
- [ViewportMSAA<enum_RenderingServer_ViewportMSAA>] **get_msaa_3d**\ (\ )

The MSAA mode we're using for 3D rendering.


----



[RID<class_RID>] **render_target** = `RID()` [🔗<class_RenderSceneBuffersConfiguration_property_render_target>]


- |void| **set_render_target**\ (\ value\: [RID<class_RID>]\ )
- [RID<class_RID>] **get_render_target**\ (\ )

The render target associated with these buffer.


----



[ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>] **scaling_3d_mode** = `255` [🔗<class_RenderSceneBuffersConfiguration_property_scaling_3d_mode>]


- |void| **set_scaling_3d_mode**\ (\ value\: [ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>]\ )
- [ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>] **get_scaling_3d_mode**\ (\ )

The requested scaling mode with which we upscale/downscale if [internal_size<class_RenderSceneBuffersConfiguration_property_internal_size>] and [target_size<class_RenderSceneBuffersConfiguration_property_target_size>] are not equal.


----



[ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>] **screen_space_aa** = `0` [🔗<class_RenderSceneBuffersConfiguration_property_screen_space_aa>]


- |void| **set_screen_space_aa**\ (\ value\: [ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>]\ )
- [ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>] **get_screen_space_aa**\ (\ )

The requested screen space AA applied in post processing.


----



[Vector2i<class_Vector2i>] **target_size** = `Vector2i(0, 0)` [🔗<class_RenderSceneBuffersConfiguration_property_target_size>]


- |void| **set_target_size**\ (\ value\: [Vector2i<class_Vector2i>]\ )
- [Vector2i<class_Vector2i>] **get_target_size**\ (\ )

The target (upscale) size if scaling is used.


----



[float<class_float>] **texture_mipmap_bias** = `0.0` [🔗<class_RenderSceneBuffersConfiguration_property_texture_mipmap_bias>]


- |void| **set_texture_mipmap_bias**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_texture_mipmap_bias**\ (\ )

Bias applied to mipmaps.


----



[int<class_int>] **view_count** = `1` [🔗<class_RenderSceneBuffersConfiguration_property_view_count>]


- |void| **set_view_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_view_count**\ (\ )

The number of views we're rendering.

