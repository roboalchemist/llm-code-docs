:github_url: hide



# CameraAttributesPhysical

**Inherits:** [CameraAttributes<class_CameraAttributes>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Physically-based camera settings.


## Description

**CameraAttributesPhysical** is used to set rendering settings based on a physically-based camera's settings. It is responsible for exposure, auto-exposure, and depth of field.

When used in a [WorldEnvironment<class_WorldEnvironment>] it provides default settings for exposure, auto-exposure, and depth of field that will be used by all cameras without their own [CameraAttributes<class_CameraAttributes>], including the editor camera. When used in a [Camera3D<class_Camera3D>] it will override any [CameraAttributes<class_CameraAttributes>] set in the [WorldEnvironment<class_WorldEnvironment>] and will override the [Camera3D<class_Camera3D>]\ s [Camera3D.far<class_Camera3D_property_far>], [Camera3D.near<class_Camera3D_property_near>], [Camera3D.fov<class_Camera3D_property_fov>], and [Camera3D.keep_aspect<class_Camera3D_property_keep_aspect>] properties. When used in [VoxelGI<class_VoxelGI>] or [LightmapGI<class_LightmapGI>], only the exposure settings will be used.

The default settings are intended for use in an outdoor environment, tips for settings for use in an indoor environment can be found in each setting's documentation.

\ **Note:** Depth of field blur is only supported in the Forward+ and Mobile rendering methods, not Compatibility.


## Tutorials

- [../tutorials/3d/physical_light_and_camera_units](Physical light and camera units .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-------------------------------------------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`auto_exposure_max_exposure_value<class_CameraAttributesPhysical_property_auto_exposure_max_exposure_value>` | ``10.0``   |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`auto_exposure_min_exposure_value<class_CameraAttributesPhysical_property_auto_exposure_min_exposure_value>` | ``-8.0``   |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`exposure_aperture<class_CameraAttributesPhysical_property_exposure_aperture>`                               | ``16.0``   |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`exposure_shutter_speed<class_CameraAttributesPhysical_property_exposure_shutter_speed>`                     | ``100.0``  |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`frustum_far<class_CameraAttributesPhysical_property_frustum_far>`                                           | ``4000.0`` |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`frustum_focal_length<class_CameraAttributesPhysical_property_frustum_focal_length>`                         | ``35.0``   |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`frustum_focus_distance<class_CameraAttributesPhysical_property_frustum_focus_distance>`                     | ``10.0``   |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`frustum_near<class_CameraAttributesPhysical_property_frustum_near>`                                         | ``0.05``   |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------+------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_fov<class_CameraAttributesPhysical_method_get_fov>`\ (\ ) |const| |
> +---------------------------+-----------------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **auto_exposure_max_exposure_value** = `10.0` [🔗<class_CameraAttributesPhysical_property_auto_exposure_max_exposure_value>]


- |void| **set_auto_exposure_max_exposure_value**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_auto_exposure_max_exposure_value**\ (\ )

The maximum luminance (in EV100) used when calculating auto exposure. When calculating scene average luminance, color values will be clamped to at least this value. This limits the auto-exposure from exposing below a certain brightness, resulting in a cut off point where the scene will remain bright.


----



[float<class_float>] **auto_exposure_min_exposure_value** = `-8.0` [🔗<class_CameraAttributesPhysical_property_auto_exposure_min_exposure_value>]


- |void| **set_auto_exposure_min_exposure_value**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_auto_exposure_min_exposure_value**\ (\ )

The minimum luminance (in EV100) used when calculating auto exposure. When calculating scene average luminance, color values will be clamped to at least this value. This limits the auto-exposure from exposing above a certain brightness, resulting in a cut off point where the scene will remain dark.


----



[float<class_float>] **exposure_aperture** = `16.0` [🔗<class_CameraAttributesPhysical_property_exposure_aperture>]


- |void| **set_aperture**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_aperture**\ (\ )

Size of the aperture of the camera, measured in f-stops. An f-stop is a unitless ratio between the focal length of the camera and the diameter of the aperture. A high aperture setting will result in a smaller aperture which leads to a dimmer image and sharper focus. A low aperture results in a wide aperture which lets in more light resulting in a brighter, less-focused image. Default is appropriate for outdoors at daytime (i.e. for use with a default [DirectionalLight3D<class_DirectionalLight3D>]), for indoor lighting, a value between 2 and 4 is more appropriate.

Only available when [ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>] is enabled.


----



[float<class_float>] **exposure_shutter_speed** = `100.0` [🔗<class_CameraAttributesPhysical_property_exposure_shutter_speed>]


- |void| **set_shutter_speed**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_shutter_speed**\ (\ )

Time for shutter to open and close, evaluated as `1 / shutter_speed` seconds. A higher value will allow less light (leading to a darker image), while a lower value will allow more light (leading to a brighter image).

Only available when [ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>] is enabled.


----



[float<class_float>] **frustum_far** = `4000.0` [🔗<class_CameraAttributesPhysical_property_frustum_far>]


- |void| **set_far**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_far**\ (\ )

Override value for [Camera3D.far<class_Camera3D_property_far>]. Used internally when calculating depth of field. When attached to a [Camera3D<class_Camera3D>] as its [Camera3D.attributes<class_Camera3D_property_attributes>], it will override the [Camera3D.far<class_Camera3D_property_far>] property.


----



[float<class_float>] **frustum_focal_length** = `35.0` [🔗<class_CameraAttributesPhysical_property_frustum_focal_length>]


- |void| **set_focal_length**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_focal_length**\ (\ )

Distance between camera lens and camera aperture, measured in millimeters. Controls field of view and depth of field. A larger focal length will result in a smaller field of view and a narrower depth of field meaning fewer objects will be in focus. A smaller focal length will result in a wider field of view and a larger depth of field meaning more objects will be in focus. When attached to a [Camera3D<class_Camera3D>] as its [Camera3D.attributes<class_Camera3D_property_attributes>], it will override the [Camera3D.fov<class_Camera3D_property_fov>] property and the [Camera3D.keep_aspect<class_Camera3D_property_keep_aspect>] property.


----



[float<class_float>] **frustum_focus_distance** = `10.0` [🔗<class_CameraAttributesPhysical_property_frustum_focus_distance>]


- |void| **set_focus_distance**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_focus_distance**\ (\ )

Distance from camera of object that will be in focus, measured in meters. Internally this will be clamped to be at least 1 millimeter larger than [frustum_focal_length<class_CameraAttributesPhysical_property_frustum_focal_length>].


----



[float<class_float>] **frustum_near** = `0.05` [🔗<class_CameraAttributesPhysical_property_frustum_near>]


- |void| **set_near**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_near**\ (\ )

Override value for [Camera3D.near<class_Camera3D_property_near>]. Used internally when calculating depth of field. When attached to a [Camera3D<class_Camera3D>] as its [Camera3D.attributes<class_Camera3D_property_attributes>], it will override the [Camera3D.near<class_Camera3D_property_near>] property.


----


## Method Descriptions



[float<class_float>] **get_fov**\ (\ ) |const| [🔗<class_CameraAttributesPhysical_method_get_fov>]

Returns the vertical field of view that corresponds to the [frustum_focal_length<class_CameraAttributesPhysical_property_frustum_focal_length>]. This value is calculated internally whenever [frustum_focal_length<class_CameraAttributesPhysical_property_frustum_focal_length>] is changed.

