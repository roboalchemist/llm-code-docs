:github_url: hide



# RenderSceneData

**Inherits:** [Object<class_Object>]

**Inherited By:** [RenderSceneDataExtension<class_RenderSceneDataExtension>], [RenderSceneDataRD<class_RenderSceneDataRD>]

Abstract render data object, holds scene data related to rendering a single frame of a viewport.


## Description

Abstract scene data object, exists for the duration of rendering a single viewport. See also [RenderSceneDataRD<class_RenderSceneDataRD>], [RenderData<class_RenderData>], and [RenderDataRD<class_RenderDataRD>].

\ **Note:** This is an internal rendering server object. Do not instantiate this class from a script.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Projection<class_Projection>`   | :ref:`get_cam_projection<class_RenderSceneData_method_get_cam_projection>`\ (\ ) |const|                                 |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`get_cam_transform<class_RenderSceneData_method_get_cam_transform>`\ (\ ) |const|                                   |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                 | :ref:`get_uniform_buffer<class_RenderSceneData_method_get_uniform_buffer>`\ (\ ) |const|                                 |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_view_count<class_RenderSceneData_method_get_view_count>`\ (\ ) |const|                                         |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`         | :ref:`get_view_eye_offset<class_RenderSceneData_method_get_view_eye_offset>`\ (\ view\: :ref:`int<class_int>`\ ) |const| |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Projection<class_Projection>`   | :ref:`get_view_projection<class_RenderSceneData_method_get_view_projection>`\ (\ view\: :ref:`int<class_int>`\ ) |const| |
> +---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Projection<class_Projection>] **get_cam_projection**\ (\ ) |const| [🔗<class_RenderSceneData_method_get_cam_projection>]

Returns the camera projection used to render this frame.

\ **Note:** If more than one view is rendered, this will return a combined projection.


----



[Transform3D<class_Transform3D>] **get_cam_transform**\ (\ ) |const| [🔗<class_RenderSceneData_method_get_cam_transform>]

Returns the camera transform used to render this frame.

\ **Note:** If more than one view is rendered, this will return a centered transform.


----



[RID<class_RID>] **get_uniform_buffer**\ (\ ) |const| [🔗<class_RenderSceneData_method_get_uniform_buffer>]

Return the [RID<class_RID>] of the uniform buffer containing the scene data as a UBO.


----



[int<class_int>] **get_view_count**\ (\ ) |const| [🔗<class_RenderSceneData_method_get_view_count>]

Returns the number of views being rendered.


----



[Vector3<class_Vector3>] **get_view_eye_offset**\ (\ view\: [int<class_int>]\ ) |const| [🔗<class_RenderSceneData_method_get_view_eye_offset>]

Returns the eye offset per view used to render this frame. This is the offset between our camera transform and the eye transform.


----



[Projection<class_Projection>] **get_view_projection**\ (\ view\: [int<class_int>]\ ) |const| [🔗<class_RenderSceneData_method_get_view_projection>]

Returns the view projection per view used to render this frame.

\ **Note:** If a single view is rendered, this returns the camera projection. If more than one view is rendered, this will return a projection for the given view including the eye offset.

