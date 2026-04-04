:github_url: hide

> **META**
	:keywords: point



# OmniLight3D

**Inherits:** [Light3D<class_Light3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Omnidirectional light, such as a light bulb or a candle.


## Description

An Omnidirectional light is a type of [Light3D<class_Light3D>] that emits light in all directions. The light is attenuated by distance and this attenuation can be configured by changing its energy, radius, and attenuation parameters.

\ **Note:** When using the Mobile rendering method, only 8 omni lights can be displayed on each mesh resource. Attempting to display more than 8 omni lights on a single mesh resource will result in omni lights flickering in and out as the camera moves. When using the Compatibility rendering method, only 8 omni lights can be displayed on each mesh resource by default, but this can be increased by adjusting [ProjectSettings.rendering/limits/opengl/max_lights_per_object<class_ProjectSettings_property_rendering/limits/opengl/max_lights_per_object>].

\ **Note:** When using the Mobile or Compatibility rendering methods, omni lights will only correctly affect meshes whose visibility AABB intersects with the light's AABB. If using a shader to deform the mesh in a way that makes it go outside its AABB, [GeometryInstance3D.extra_cull_margin<class_GeometryInstance3D_property_extra_cull_margin>] must be increased on the mesh. Otherwise, the light may not be visible on the mesh.


## Tutorials

- [../tutorials/3d/lights_and_shadows](3D lights and shadows .md)

- [../tutorials/3d/global_illumination/faking_global_illumination](Faking global illumination .md)


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                      | light_specular                                                       | ``0.5`` (overrides :ref:`Light3D<class_Light3D_property_light_specular>`)     |
> +------------------------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                      | :ref:`omni_attenuation<class_OmniLight3D_property_omni_attenuation>` | ``1.0``                                                                       |
> +------------------------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                      | :ref:`omni_range<class_OmniLight3D_property_omni_range>`             | ``5.0``                                                                       |
> +------------------------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`ShadowMode<enum_OmniLight3D_ShadowMode>` | :ref:`omni_shadow_mode<class_OmniLight3D_property_omni_shadow_mode>` | ``1``                                                                         |
> +------------------------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                      | shadow_normal_bias                                                   | ``1.0`` (overrides :ref:`Light3D<class_Light3D_property_shadow_normal_bias>`) |
> +------------------------------------------------+----------------------------------------------------------------------+-------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ShadowMode**: [🔗<enum_OmniLight3D_ShadowMode>]



[ShadowMode<enum_OmniLight3D_ShadowMode>] **SHADOW_DUAL_PARABOLOID** = `0`

Shadows are rendered to a dual-paraboloid texture. Faster than [SHADOW_CUBE<class_OmniLight3D_constant_SHADOW_CUBE>], but lower-quality.



[ShadowMode<enum_OmniLight3D_ShadowMode>] **SHADOW_CUBE** = `1`

Shadows are rendered to a cubemap. Slower than [SHADOW_DUAL_PARABOLOID<class_OmniLight3D_constant_SHADOW_DUAL_PARABOLOID>], but higher-quality.


----


## Property Descriptions



[float<class_float>] **omni_attenuation** = `1.0` [🔗<class_OmniLight3D_property_omni_attenuation>]


- |void| **set_param**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ )

Controls the distance attenuation function for omnilights.

A value of `0.0` will maintain a constant brightness through most of the range, but smoothly attenuate the light at the edge of the range. Use a value of `2.0` for physically accurate lights as it results in the proper inverse square attenutation.

\ **Note:** Setting attenuation to `2.0` or higher may result in distant objects receiving minimal light, even within range. For example, with a range of `4096`, an object at `100` units is attenuated by a factor of `0.0001`. With a default brightness of `1`, the light would not be visible at that distance.

\ **Note:** Using negative or values higher than `10.0` may lead to unexpected results.


----



[float<class_float>] **omni_range** = `5.0` [🔗<class_OmniLight3D_property_omni_range>]


- |void| **set_param**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ )

The light's radius. Note that the effectively lit area may appear to be smaller depending on the [omni_attenuation<class_OmniLight3D_property_omni_attenuation>] in use. No matter the [omni_attenuation<class_OmniLight3D_property_omni_attenuation>] in use, the light will never reach anything outside this radius.

\ **Note:** [omni_range<class_OmniLight3D_property_omni_range>] is not affected by [Node3D.scale<class_Node3D_property_scale>] (the light's scale or its parent's scale).


----



[ShadowMode<enum_OmniLight3D_ShadowMode>] **omni_shadow_mode** = `1` [🔗<class_OmniLight3D_property_omni_shadow_mode>]


- |void| **set_shadow_mode**\ (\ value\: [ShadowMode<enum_OmniLight3D_ShadowMode>]\ )
- [ShadowMode<enum_OmniLight3D_ShadowMode>] **get_shadow_mode**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

