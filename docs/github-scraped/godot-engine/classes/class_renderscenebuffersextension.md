:github_url: hide



# RenderSceneBuffersExtension

**Inherits:** [RenderSceneBuffers<class_RenderSceneBuffers>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

This class allows for a RenderSceneBuffer implementation to be made in GDExtension.


## Description

This class allows for a RenderSceneBuffer implementation to be made in GDExtension.


## Methods

> **TABLE**
> :widths: auto
>
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_configure<class_RenderSceneBuffersExtension_private_method__configure>`\ (\ config\: :ref:`RenderSceneBuffersConfiguration<class_RenderSceneBuffersConfiguration>`\ ) |virtual|          |
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_set_anisotropic_filtering_level<class_RenderSceneBuffersExtension_private_method__set_anisotropic_filtering_level>`\ (\ anisotropic_filtering_level\: :ref:`int<class_int>`\ ) |virtual| |
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_set_fsr_sharpness<class_RenderSceneBuffersExtension_private_method__set_fsr_sharpness>`\ (\ fsr_sharpness\: :ref:`float<class_float>`\ ) |virtual|                                       |
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_set_texture_mipmap_bias<class_RenderSceneBuffersExtension_private_method__set_texture_mipmap_bias>`\ (\ texture_mipmap_bias\: :ref:`float<class_float>`\ ) |virtual|                     |
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_set_use_debanding<class_RenderSceneBuffersExtension_private_method__set_use_debanding>`\ (\ use_debanding\: :ref:`bool<class_bool>`\ ) |virtual|                                         |
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **_configure**\ (\ config\: [RenderSceneBuffersConfiguration<class_RenderSceneBuffersConfiguration>]\ ) |virtual| [🔗<class_RenderSceneBuffersExtension_private_method__configure>]

Implement this in GDExtension to handle the (re)sizing of a viewport.


----



|void| **_set_anisotropic_filtering_level**\ (\ anisotropic_filtering_level\: [int<class_int>]\ ) |virtual| [🔗<class_RenderSceneBuffersExtension_private_method__set_anisotropic_filtering_level>]

Implement this in GDExtension to change the anisotropic filtering level.


----



|void| **_set_fsr_sharpness**\ (\ fsr_sharpness\: [float<class_float>]\ ) |virtual| [🔗<class_RenderSceneBuffersExtension_private_method__set_fsr_sharpness>]

Implement this in GDExtension to record a new FSR sharpness value.


----



|void| **_set_texture_mipmap_bias**\ (\ texture_mipmap_bias\: [float<class_float>]\ ) |virtual| [🔗<class_RenderSceneBuffersExtension_private_method__set_texture_mipmap_bias>]

Implement this in GDExtension to change the texture mipmap bias.


----



|void| **_set_use_debanding**\ (\ use_debanding\: [bool<class_bool>]\ ) |virtual| [🔗<class_RenderSceneBuffersExtension_private_method__set_use_debanding>]

Implement this in GDExtension to react to the debanding flag changing.

