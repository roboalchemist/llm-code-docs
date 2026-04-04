:github_url: hide



# RenderDataExtension

**Inherits:** [RenderData<class_RenderData>] **<** [Object<class_Object>]

This class allows for a RenderData implementation to be made in GDExtension.


## Description

This class allows for a RenderData implementation to be made in GDExtension.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                               | :ref:`_get_camera_attributes<class_RenderDataExtension_private_method__get_camera_attributes>`\ (\ ) |virtual| |const|       |
> +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                               | :ref:`_get_environment<class_RenderDataExtension_private_method__get_environment>`\ (\ ) |virtual| |const|                   |
> +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RenderSceneBuffers<class_RenderSceneBuffers>` | :ref:`_get_render_scene_buffers<class_RenderDataExtension_private_method__get_render_scene_buffers>`\ (\ ) |virtual| |const| |
> +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RenderSceneData<class_RenderSceneData>`       | :ref:`_get_render_scene_data<class_RenderDataExtension_private_method__get_render_scene_data>`\ (\ ) |virtual| |const|       |
> +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[RID<class_RID>] **_get_camera_attributes**\ (\ ) |virtual| |const| [🔗<class_RenderDataExtension_private_method__get_camera_attributes>]

Implement this in GDExtension to return the [RID<class_RID>] for the implementation's camera attributes object.


----



[RID<class_RID>] **_get_environment**\ (\ ) |virtual| |const| [🔗<class_RenderDataExtension_private_method__get_environment>]

Implement this in GDExtension to return the [RID<class_RID>] of the implementation's environment object.


----



[RenderSceneBuffers<class_RenderSceneBuffers>] **_get_render_scene_buffers**\ (\ ) |virtual| |const| [🔗<class_RenderDataExtension_private_method__get_render_scene_buffers>]

Implement this in GDExtension to return the implementation's [RenderSceneBuffers<class_RenderSceneBuffers>] object.


----



[RenderSceneData<class_RenderSceneData>] **_get_render_scene_data**\ (\ ) |virtual| |const| [🔗<class_RenderDataExtension_private_method__get_render_scene_data>]

Implement this in GDExtension to return the implementation's [RenderSceneDataExtension<class_RenderSceneDataExtension>] object.

