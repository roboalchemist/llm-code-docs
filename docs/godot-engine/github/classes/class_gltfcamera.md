:github_url: hide



# GLTFCamera

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a glTF camera.


## Description

Represents a camera as defined by the base glTF spec.


## Tutorials

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)

- [glTF camera detailed specification ](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-camera)_

- [glTF camera spec and example file ](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_015_SimpleCameras.md)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`depth_far<class_GLTFCamera_property_depth_far>`     | ``4000.0``    |
> +---------------------------+-----------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`depth_near<class_GLTFCamera_property_depth_near>`   | ``0.05``      |
> +---------------------------+-----------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`fov<class_GLTFCamera_property_fov>`                 | ``1.3089969`` |
> +---------------------------+-----------------------------------------------------------+---------------+
> | :ref:`bool<class_bool>`   | :ref:`perspective<class_GLTFCamera_property_perspective>` | ``true``      |
> +---------------------------+-----------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`size_mag<class_GLTFCamera_property_size_mag>`       | ``0.5``       |
> +---------------------------+-----------------------------------------------------------+---------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GLTFCamera<class_GLTFCamera>` | :ref:`from_dictionary<class_GLTFCamera_method_from_dictionary>`\ (\ dictionary\: :ref:`Dictionary<class_Dictionary>`\ ) |static| |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GLTFCamera<class_GLTFCamera>` | :ref:`from_node<class_GLTFCamera_method_from_node>`\ (\ camera_node\: :ref:`Camera3D<class_Camera3D>`\ ) |static|                |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>` | :ref:`to_dictionary<class_GLTFCamera_method_to_dictionary>`\ (\ ) |const|                                                        |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Camera3D<class_Camera3D>`     | :ref:`to_node<class_GLTFCamera_method_to_node>`\ (\ ) |const|                                                                    |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **depth_far** = `4000.0` [🔗<class_GLTFCamera_property_depth_far>]


- |void| **set_depth_far**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_depth_far**\ (\ )

The distance to the far culling boundary for this camera relative to its local Z axis, in meters. This maps to glTF's `zfar` property.


----



[float<class_float>] **depth_near** = `0.05` [🔗<class_GLTFCamera_property_depth_near>]


- |void| **set_depth_near**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_depth_near**\ (\ )

The distance to the near culling boundary for this camera relative to its local Z axis, in meters. This maps to glTF's `znear` property.


----



[float<class_float>] **fov** = `1.3089969` [🔗<class_GLTFCamera_property_fov>]


- |void| **set_fov**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_fov**\ (\ )

The FOV of the camera. This class and glTF define the camera FOV in radians, while Godot uses degrees. This maps to glTF's `yfov` property. This value is only used for perspective cameras, when [perspective<class_GLTFCamera_property_perspective>] is `true`.


----



[bool<class_bool>] **perspective** = `true` [🔗<class_GLTFCamera_property_perspective>]


- |void| **set_perspective**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_perspective**\ (\ )

If `true`, the camera is in perspective mode. Otherwise, the camera is in orthographic/orthogonal mode. This maps to glTF's camera `type` property. See [Camera3D.projection<class_Camera3D_property_projection>] and the glTF spec for more information.


----



[float<class_float>] **size_mag** = `0.5` [🔗<class_GLTFCamera_property_size_mag>]


- |void| **set_size_mag**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_size_mag**\ (\ )

The size of the camera. This class and glTF define the camera size magnitude as a radius in meters, while Godot defines it as a diameter in meters. This maps to glTF's `ymag` property. This value is only used for orthographic/orthogonal cameras, when [perspective<class_GLTFCamera_property_perspective>] is `false`.


----


## Method Descriptions



[GLTFCamera<class_GLTFCamera>] **from_dictionary**\ (\ dictionary\: [Dictionary<class_Dictionary>]\ ) |static| [🔗<class_GLTFCamera_method_from_dictionary>]

Creates a new GLTFCamera instance by parsing the given [Dictionary<class_Dictionary>].


----



[GLTFCamera<class_GLTFCamera>] **from_node**\ (\ camera_node\: [Camera3D<class_Camera3D>]\ ) |static| [🔗<class_GLTFCamera_method_from_node>]

Create a new GLTFCamera instance from the given Godot [Camera3D<class_Camera3D>] node.


----



[Dictionary<class_Dictionary>] **to_dictionary**\ (\ ) |const| [🔗<class_GLTFCamera_method_to_dictionary>]

Serializes this GLTFCamera instance into a [Dictionary<class_Dictionary>].


----



[Camera3D<class_Camera3D>] **to_node**\ (\ ) |const| [🔗<class_GLTFCamera_method_to_node>]

Converts this GLTFCamera instance into a Godot [Camera3D<class_Camera3D>] node.

