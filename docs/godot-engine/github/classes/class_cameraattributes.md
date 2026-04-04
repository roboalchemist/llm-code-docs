:github_url: hide



# CameraAttributes

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [CameraAttributesPhysical<class_CameraAttributesPhysical>], [CameraAttributesPractical<class_CameraAttributesPractical>]

Parent class for camera settings.


## Description

Controls camera-specific attributes such as depth of field and exposure override.

When used in a [WorldEnvironment<class_WorldEnvironment>] it provides default settings for exposure, auto-exposure, and depth of field that will be used by all cameras without their own **CameraAttributes**, including the editor camera. When used in a [Camera3D<class_Camera3D>] it will override any **CameraAttributes** set in the [WorldEnvironment<class_WorldEnvironment>]. When used in [VoxelGI<class_VoxelGI>] or [LightmapGI<class_LightmapGI>], only the exposure settings will be used.

See also [Environment<class_Environment>] for general 3D environment settings.

This is a pure virtual class that is inherited by [CameraAttributesPhysical<class_CameraAttributesPhysical>] and [CameraAttributesPractical<class_CameraAttributesPractical>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`auto_exposure_enabled<class_CameraAttributes_property_auto_exposure_enabled>` | ``false`` |
> +---------------------------+-------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`auto_exposure_scale<class_CameraAttributes_property_auto_exposure_scale>`     | ``0.4``   |
> +---------------------------+-------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`auto_exposure_speed<class_CameraAttributes_property_auto_exposure_speed>`     | ``0.5``   |
> +---------------------------+-------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`exposure_multiplier<class_CameraAttributes_property_exposure_multiplier>`     | ``1.0``   |
> +---------------------------+-------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`exposure_sensitivity<class_CameraAttributes_property_exposure_sensitivity>`   | ``100.0`` |
> +---------------------------+-------------------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[bool<class_bool>] **auto_exposure_enabled** = `false` [🔗<class_CameraAttributes_property_auto_exposure_enabled>]


- |void| **set_auto_exposure_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_auto_exposure_enabled**\ (\ )

If `true`, enables the tonemapping auto exposure mode of the scene renderer. If `true`, the renderer will automatically determine the exposure setting to adapt to the scene's illumination and the observed light.


----



[float<class_float>] **auto_exposure_scale** = `0.4` [🔗<class_CameraAttributes_property_auto_exposure_scale>]


- |void| **set_auto_exposure_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_auto_exposure_scale**\ (\ )

The scale of the auto exposure effect. Affects the intensity of auto exposure.


----



[float<class_float>] **auto_exposure_speed** = `0.5` [🔗<class_CameraAttributes_property_auto_exposure_speed>]


- |void| **set_auto_exposure_speed**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_auto_exposure_speed**\ (\ )

The speed of the auto exposure effect. Affects the time needed for the camera to perform auto exposure.


----



[float<class_float>] **exposure_multiplier** = `1.0` [🔗<class_CameraAttributes_property_exposure_multiplier>]


- |void| **set_exposure_multiplier**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_exposure_multiplier**\ (\ )

Multiplier for the exposure amount. A higher value results in a brighter image.


----



[float<class_float>] **exposure_sensitivity** = `100.0` [🔗<class_CameraAttributes_property_exposure_sensitivity>]


- |void| **set_exposure_sensitivity**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_exposure_sensitivity**\ (\ )

Sensitivity of camera sensors, measured in ISO. A higher sensitivity results in a brighter image.

If [auto_exposure_enabled<class_CameraAttributes_property_auto_exposure_enabled>] is `true`, this can be used as a method of exposure compensation, doubling the value will increase the exposure value (measured in EV100) by 1 stop.

\ **Note:** Only available when [ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>] is enabled.

