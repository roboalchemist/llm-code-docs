:github_url: hide



# CameraAttributesPractical

**Inherits:** [CameraAttributes<class_CameraAttributes>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Camera settings in an easy to use format.


## Description

Controls camera-specific attributes such as auto-exposure, depth of field, and exposure override.

When used in a [WorldEnvironment<class_WorldEnvironment>] it provides default settings for exposure, auto-exposure, and depth of field that will be used by all cameras without their own [CameraAttributes<class_CameraAttributes>], including the editor camera. When used in a [Camera3D<class_Camera3D>] it will override any [CameraAttributes<class_CameraAttributes>] set in the [WorldEnvironment<class_WorldEnvironment>]. When used in [VoxelGI<class_VoxelGI>] or [LightmapGI<class_LightmapGI>], only the exposure settings will be used.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+--------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`auto_exposure_max_sensitivity<class_CameraAttributesPractical_property_auto_exposure_max_sensitivity>` | ``800.0`` |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`auto_exposure_min_sensitivity<class_CameraAttributesPractical_property_auto_exposure_min_sensitivity>` | ``0.0``   |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`dof_blur_amount<class_CameraAttributesPractical_property_dof_blur_amount>`                             | ``0.1``   |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`dof_blur_far_distance<class_CameraAttributesPractical_property_dof_blur_far_distance>`                 | ``10.0``  |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`dof_blur_far_enabled<class_CameraAttributesPractical_property_dof_blur_far_enabled>`                   | ``false`` |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`dof_blur_far_transition<class_CameraAttributesPractical_property_dof_blur_far_transition>`             | ``5.0``   |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`dof_blur_near_distance<class_CameraAttributesPractical_property_dof_blur_near_distance>`               | ``2.0``   |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`dof_blur_near_enabled<class_CameraAttributesPractical_property_dof_blur_near_enabled>`                 | ``false`` |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`dof_blur_near_transition<class_CameraAttributesPractical_property_dof_blur_near_transition>`           | ``1.0``   |
> +---------------------------+--------------------------------------------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[float<class_float>] **auto_exposure_max_sensitivity** = `800.0` [🔗<class_CameraAttributesPractical_property_auto_exposure_max_sensitivity>]


- |void| **set_auto_exposure_max_sensitivity**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_auto_exposure_max_sensitivity**\ (\ )

The maximum sensitivity (in ISO) used when calculating auto exposure. When calculating scene average luminance, color values will be clamped to at least this value. This limits the auto-exposure from exposing below a certain brightness, resulting in a cut off point where the scene will remain bright.


----



[float<class_float>] **auto_exposure_min_sensitivity** = `0.0` [🔗<class_CameraAttributesPractical_property_auto_exposure_min_sensitivity>]


- |void| **set_auto_exposure_min_sensitivity**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_auto_exposure_min_sensitivity**\ (\ )

The minimum sensitivity (in ISO) used when calculating auto exposure. When calculating scene average luminance, color values will be clamped to at least this value. This limits the auto-exposure from exposing above a certain brightness, resulting in a cut off point where the scene will remain dark.


----



[float<class_float>] **dof_blur_amount** = `0.1` [🔗<class_CameraAttributesPractical_property_dof_blur_amount>]


- |void| **set_dof_blur_amount**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_dof_blur_amount**\ (\ )

Sets the maximum amount of blur. When using physically-based blur amounts, will instead act as a multiplier. High values lead to an increased amount of blurriness, but can be much more expensive to calculate. It is best to keep this as low as possible for a given art style.


----



[float<class_float>] **dof_blur_far_distance** = `10.0` [🔗<class_CameraAttributesPractical_property_dof_blur_far_distance>]


- |void| **set_dof_blur_far_distance**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_dof_blur_far_distance**\ (\ )

Objects further from the [Camera3D<class_Camera3D>] by this amount will be blurred by the depth of field effect. Measured in meters.


----



[bool<class_bool>] **dof_blur_far_enabled** = `false` [🔗<class_CameraAttributesPractical_property_dof_blur_far_enabled>]


- |void| **set_dof_blur_far_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_dof_blur_far_enabled**\ (\ )

Enables depth of field blur for objects further than [dof_blur_far_distance<class_CameraAttributesPractical_property_dof_blur_far_distance>]. Strength of blur is controlled by [dof_blur_amount<class_CameraAttributesPractical_property_dof_blur_amount>] and modulated by [dof_blur_far_transition<class_CameraAttributesPractical_property_dof_blur_far_transition>].

\ **Note:** Depth of field blur is only supported in the Forward+ and Mobile rendering methods, not Compatibility.

\ **Note:** Depth of field blur is not supported on viewports that have a transparent background (where [Viewport.transparent_bg<class_Viewport_property_transparent_bg>] is `true`).


----



[float<class_float>] **dof_blur_far_transition** = `5.0` [🔗<class_CameraAttributesPractical_property_dof_blur_far_transition>]


- |void| **set_dof_blur_far_transition**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_dof_blur_far_transition**\ (\ )

When positive, distance over which (starting from [dof_blur_far_distance<class_CameraAttributesPractical_property_dof_blur_far_distance>]) blur effect will scale from 0 to [dof_blur_amount<class_CameraAttributesPractical_property_dof_blur_amount>]. When negative, uses physically-based scaling so depth of field effect will scale from 0 at [dof_blur_far_distance<class_CameraAttributesPractical_property_dof_blur_far_distance>] and will increase in a physically accurate way as objects get further from the [Camera3D<class_Camera3D>].


----



[float<class_float>] **dof_blur_near_distance** = `2.0` [🔗<class_CameraAttributesPractical_property_dof_blur_near_distance>]


- |void| **set_dof_blur_near_distance**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_dof_blur_near_distance**\ (\ )

Objects closer from the [Camera3D<class_Camera3D>] by this amount will be blurred by the depth of field effect. Measured in meters.


----



[bool<class_bool>] **dof_blur_near_enabled** = `false` [🔗<class_CameraAttributesPractical_property_dof_blur_near_enabled>]


- |void| **set_dof_blur_near_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_dof_blur_near_enabled**\ (\ )

Enables depth of field blur for objects closer than [dof_blur_near_distance<class_CameraAttributesPractical_property_dof_blur_near_distance>]. Strength of blur is controlled by [dof_blur_amount<class_CameraAttributesPractical_property_dof_blur_amount>] and modulated by [dof_blur_near_transition<class_CameraAttributesPractical_property_dof_blur_near_transition>].

\ **Note:** Depth of field blur is only supported in the Forward+ and Mobile rendering methods, not Compatibility.

\ **Note:** Depth of field blur is not supported on viewports that have a transparent background (where [Viewport.transparent_bg<class_Viewport_property_transparent_bg>] is `true`).


----



[float<class_float>] **dof_blur_near_transition** = `1.0` [🔗<class_CameraAttributesPractical_property_dof_blur_near_transition>]


- |void| **set_dof_blur_near_transition**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_dof_blur_near_transition**\ (\ )

When positive, distance over which blur effect will scale from 0 to [dof_blur_amount<class_CameraAttributesPractical_property_dof_blur_amount>], ending at [dof_blur_near_distance<class_CameraAttributesPractical_property_dof_blur_near_distance>]. When negative, uses physically-based scaling so depth of field effect will scale from 0 at [dof_blur_near_distance<class_CameraAttributesPractical_property_dof_blur_near_distance>] and will increase in a physically accurate way as objects get closer to the [Camera3D<class_Camera3D>].

