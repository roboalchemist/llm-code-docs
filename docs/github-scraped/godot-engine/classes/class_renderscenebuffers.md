:github_url: hide



# RenderSceneBuffers

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [RenderSceneBuffersExtension<class_RenderSceneBuffersExtension>], [RenderSceneBuffersRD<class_RenderSceneBuffersRD>]

Abstract scene buffers object, created for each viewport for which 3D rendering is done.


## Description

Abstract scene buffers object, created for each viewport for which 3D rendering is done. It manages any additional buffers used during rendering and will discard buffers when the viewport is resized. See also [RenderSceneBuffersRD<class_RenderSceneBuffersRD>].

\ **Note:** This is an internal rendering server object. Do not instantiate this class from a script.


## Methods

> **TABLE**
> :widths: auto
>
> +--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`configure<class_RenderSceneBuffers_method_configure>`\ (\ config\: :ref:`RenderSceneBuffersConfiguration<class_RenderSceneBuffersConfiguration>`\ ) |
> +--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **configure**\ (\ config\: [RenderSceneBuffersConfiguration<class_RenderSceneBuffersConfiguration>]\ ) [🔗<class_RenderSceneBuffers_method_configure>]

This method is called by the rendering server when the associated viewport's configuration is changed. It will discard the old buffers and recreate the internal buffers used.

