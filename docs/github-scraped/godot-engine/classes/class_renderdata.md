:github_url: hide



# RenderData

**Inherits:** [Object<class_Object>]

**Inherited By:** [RenderDataExtension<class_RenderDataExtension>], [RenderDataRD<class_RenderDataRD>]

Abstract render data object, holds frame data related to rendering a single frame of a viewport.


## Description

Abstract render data object, exists for the duration of rendering a single viewport. See also [RenderDataRD<class_RenderDataRD>], [RenderSceneData<class_RenderSceneData>], and [RenderSceneDataRD<class_RenderSceneDataRD>].

\ **Note:** This is an internal rendering server object. Do not instantiate this class from a script.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                               | :ref:`get_camera_attributes<class_RenderData_method_get_camera_attributes>`\ (\ ) |const|       |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                               | :ref:`get_environment<class_RenderData_method_get_environment>`\ (\ ) |const|                   |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`RenderSceneBuffers<class_RenderSceneBuffers>` | :ref:`get_render_scene_buffers<class_RenderData_method_get_render_scene_buffers>`\ (\ ) |const| |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`RenderSceneData<class_RenderSceneData>`       | :ref:`get_render_scene_data<class_RenderData_method_get_render_scene_data>`\ (\ ) |const|       |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[RID<class_RID>] **get_camera_attributes**\ (\ ) |const| [🔗<class_RenderData_method_get_camera_attributes>]

Returns the [RID<class_RID>] of the camera attributes object in the [RenderingServer<class_RenderingServer>] being used to render this viewport.


----



[RID<class_RID>] **get_environment**\ (\ ) |const| [🔗<class_RenderData_method_get_environment>]

Returns the [RID<class_RID>] of the environment object in the [RenderingServer<class_RenderingServer>] being used to render this viewport.


----



[RenderSceneBuffers<class_RenderSceneBuffers>] **get_render_scene_buffers**\ (\ ) |const| [🔗<class_RenderData_method_get_render_scene_buffers>]

Returns the [RenderSceneBuffers<class_RenderSceneBuffers>] object managing the scene buffers for rendering this viewport.


----



[RenderSceneData<class_RenderSceneData>] **get_render_scene_data**\ (\ ) |const| [🔗<class_RenderData_method_get_render_scene_data>]

Returns the [RenderSceneData<class_RenderSceneData>] object managing this frames scene data.

