:github_url: hide

> **META**
	:keywords: background, sky



# WorldEnvironment

**Inherits:** [Node<class_Node>] **<** [Object<class_Object>]

Default environment properties for the entire scene (post-processing effects, lighting and background settings).


## Description

The **WorldEnvironment** node is used to configure the default [Environment<class_Environment>] for the scene.

The parameters defined in the **WorldEnvironment** can be overridden by an [Environment<class_Environment>] node set on the current [Camera3D<class_Camera3D>]. Additionally, only one **WorldEnvironment** may be instantiated in a given scene at a time.

The **WorldEnvironment** allows the user to specify default lighting parameters (e.g. ambient lighting), various post-processing effects (e.g. SSAO, DOF, Tonemapping), and how to draw the background (e.g. solid color, skybox). Usually, these are added in order to improve the realism/color balance of the scene.


## Tutorials

- [../tutorials/3d/environment_and_post_processing](Environment and post-processing .md)

- [3D Material Testers Demo ](https://godotengine.org/asset-library/asset/2742)_

- [Third Person Shooter (TPS) Demo ](https://godotengine.org/asset-library/asset/2710)_


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+-----------------------------------------------------------------------------+
> | :ref:`CameraAttributes<class_CameraAttributes>` | :ref:`camera_attributes<class_WorldEnvironment_property_camera_attributes>` |
> +-------------------------------------------------+-----------------------------------------------------------------------------+
> | :ref:`Compositor<class_Compositor>`             | :ref:`compositor<class_WorldEnvironment_property_compositor>`               |
> +-------------------------------------------------+-----------------------------------------------------------------------------+
> | :ref:`Environment<class_Environment>`           | :ref:`environment<class_WorldEnvironment_property_environment>`             |
> +-------------------------------------------------+-----------------------------------------------------------------------------+
>

----


## Property Descriptions



[CameraAttributes<class_CameraAttributes>] **camera_attributes** [🔗<class_WorldEnvironment_property_camera_attributes>]


- |void| **set_camera_attributes**\ (\ value\: [CameraAttributes<class_CameraAttributes>]\ )
- [CameraAttributes<class_CameraAttributes>] **get_camera_attributes**\ (\ )

The default [CameraAttributes<class_CameraAttributes>] resource to use if none set on the [Camera3D<class_Camera3D>].


----



[Compositor<class_Compositor>] **compositor** [🔗<class_WorldEnvironment_property_compositor>]


- |void| **set_compositor**\ (\ value\: [Compositor<class_Compositor>]\ )
- [Compositor<class_Compositor>] **get_compositor**\ (\ )

The default [Compositor<class_Compositor>] resource to use if none set on the [Camera3D<class_Camera3D>].


----



[Environment<class_Environment>] **environment** [🔗<class_WorldEnvironment_property_environment>]


- |void| **set_environment**\ (\ value\: [Environment<class_Environment>]\ )
- [Environment<class_Environment>] **get_environment**\ (\ )

The [Environment<class_Environment>] resource used by this **WorldEnvironment**, defining the default properties.

