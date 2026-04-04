:github_url: hide



# RenderSceneDataExtension

**Inherits:** [RenderSceneData<class_RenderSceneData>] **<** [Object<class_Object>]

This class allows for a RenderSceneData implementation to be made in GDExtension.


## Description

This class allows for a RenderSceneData implementation to be made in GDExtension.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Projection<class_Projection>`   | :ref:`_get_cam_projection<class_RenderSceneDataExtension_private_method__get_cam_projection>`\ (\ ) |virtual| |const|                                 |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`_get_cam_transform<class_RenderSceneDataExtension_private_method__get_cam_transform>`\ (\ ) |virtual| |const|                                   |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                 | :ref:`_get_uniform_buffer<class_RenderSceneDataExtension_private_method__get_uniform_buffer>`\ (\ ) |virtual| |const|                                 |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`_get_view_count<class_RenderSceneDataExtension_private_method__get_view_count>`\ (\ ) |virtual| |const|                                         |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`         | :ref:`_get_view_eye_offset<class_RenderSceneDataExtension_private_method__get_view_eye_offset>`\ (\ view\: :ref:`int<class_int>`\ ) |virtual| |const| |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Projection<class_Projection>`   | :ref:`_get_view_projection<class_RenderSceneDataExtension_private_method__get_view_projection>`\ (\ view\: :ref:`int<class_int>`\ ) |virtual| |const| |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Projection<class_Projection>] **_get_cam_projection**\ (\ ) |virtual| |const| [🔗<class_RenderSceneDataExtension_private_method__get_cam_projection>]

Implement this in GDExtension to return the camera [Projection<class_Projection>].


----



[Transform3D<class_Transform3D>] **_get_cam_transform**\ (\ ) |virtual| |const| [🔗<class_RenderSceneDataExtension_private_method__get_cam_transform>]

Implement this in GDExtension to return the camera [Transform3D<class_Transform3D>].


----



[RID<class_RID>] **_get_uniform_buffer**\ (\ ) |virtual| |const| [🔗<class_RenderSceneDataExtension_private_method__get_uniform_buffer>]

Implement this in GDExtension to return the [RID<class_RID>] of the uniform buffer containing the scene data as a UBO.


----



[int<class_int>] **_get_view_count**\ (\ ) |virtual| |const| [🔗<class_RenderSceneDataExtension_private_method__get_view_count>]

Implement this in GDExtension to return the view count.


----



[Vector3<class_Vector3>] **_get_view_eye_offset**\ (\ view\: [int<class_int>]\ ) |virtual| |const| [🔗<class_RenderSceneDataExtension_private_method__get_view_eye_offset>]

Implement this in GDExtension to return the eye offset for the given `view`.


----



[Projection<class_Projection>] **_get_view_projection**\ (\ view\: [int<class_int>]\ ) |virtual| |const| [🔗<class_RenderSceneDataExtension_private_method__get_view_projection>]

Implement this in GDExtension to return the view [Projection<class_Projection>] for the given `view`.

