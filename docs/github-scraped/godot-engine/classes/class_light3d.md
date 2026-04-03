:github_url: hide



# Light3D

**Inherits:** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [DirectionalLight3D<class_DirectionalLight3D>], [OmniLight3D<class_OmniLight3D>], [SpotLight3D<class_SpotLight3D>]

Provides a base class for different kinds of light nodes.


## Description

Light3D is the *abstract* base class for light nodes. As it can't be instantiated, it shouldn't be used directly. Other types of light nodes inherit from it. Light3D contains the common variables and parameters used for lighting.


## Tutorials

- [../tutorials/3d/lights_and_shadows](3D lights and shadows .md)

- [../tutorials/3d/global_illumination/faking_global_illumination](Faking global illumination .md)

- [Third Person Shooter (TPS) Demo ](https://godotengine.org/asset-library/asset/2710)_


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`distance_fade_begin<class_Light3D_property_distance_fade_begin>`                 | ``40.0``              |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                | :ref:`distance_fade_enabled<class_Light3D_property_distance_fade_enabled>`             | ``false``             |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`distance_fade_length<class_Light3D_property_distance_fade_length>`               | ``10.0``              |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`distance_fade_shadow<class_Light3D_property_distance_fade_shadow>`               | ``50.0``              |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                | :ref:`editor_only<class_Light3D_property_editor_only>`                                 | ``false``             |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`light_angular_distance<class_Light3D_property_light_angular_distance>`           | ``0.0``               |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`BakeMode<enum_Light3D_BakeMode>` | :ref:`light_bake_mode<class_Light3D_property_light_bake_mode>`                         | ``2``                 |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`              | :ref:`light_color<class_Light3D_property_light_color>`                                 | ``Color(1, 1, 1, 1)`` |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                  | :ref:`light_cull_mask<class_Light3D_property_light_cull_mask>`                         | ``4294967295``        |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`light_energy<class_Light3D_property_light_energy>`                               | ``1.0``               |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`light_indirect_energy<class_Light3D_property_light_indirect_energy>`             | ``1.0``               |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`light_intensity_lumens<class_Light3D_property_light_intensity_lumens>`           |                       |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`light_intensity_lux<class_Light3D_property_light_intensity_lux>`                 |                       |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                | :ref:`light_negative<class_Light3D_property_light_negative>`                           | ``false``             |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Texture2D<class_Texture2D>`      | :ref:`light_projector<class_Light3D_property_light_projector>`                         |                       |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`light_size<class_Light3D_property_light_size>`                                   | ``0.0``               |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`light_specular<class_Light3D_property_light_specular>`                           | ``1.0``               |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`light_temperature<class_Light3D_property_light_temperature>`                     |                       |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`light_volumetric_fog_energy<class_Light3D_property_light_volumetric_fog_energy>` | ``1.0``               |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`shadow_bias<class_Light3D_property_shadow_bias>`                                 | ``0.1``               |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`shadow_blur<class_Light3D_property_shadow_blur>`                                 | ``1.0``               |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                  | :ref:`shadow_caster_mask<class_Light3D_property_shadow_caster_mask>`                   | ``4294967295``        |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                | :ref:`shadow_enabled<class_Light3D_property_shadow_enabled>`                           | ``false``             |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`shadow_normal_bias<class_Light3D_property_shadow_normal_bias>`                   | ``2.0``               |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`shadow_opacity<class_Light3D_property_shadow_opacity>`                           | ``1.0``               |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                | :ref:`shadow_reverse_cull_face<class_Light3D_property_shadow_reverse_cull_face>`       | ``false``             |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`              | :ref:`shadow_transmittance_bias<class_Light3D_property_shadow_transmittance_bias>`     | ``0.05``              |
> +----------------------------------------+----------------------------------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>` | :ref:`get_correlated_color<class_Light3D_method_get_correlated_color>`\ (\ ) |const|                                                |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_param<class_Light3D_method_get_param>`\ (\ param\: :ref:`Param<enum_Light3D_Param>`\ ) |const|                            |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_param<class_Light3D_method_set_param>`\ (\ param\: :ref:`Param<enum_Light3D_Param>`, value\: :ref:`float<class_float>`\ ) |
> +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Param**: [🔗<enum_Light3D_Param>]



[Param<enum_Light3D_Param>] **PARAM_ENERGY** = `0`

Constant for accessing [light_energy<class_Light3D_property_light_energy>].



[Param<enum_Light3D_Param>] **PARAM_INDIRECT_ENERGY** = `1`

Constant for accessing [light_indirect_energy<class_Light3D_property_light_indirect_energy>].



[Param<enum_Light3D_Param>] **PARAM_VOLUMETRIC_FOG_ENERGY** = `2`

Constant for accessing [light_volumetric_fog_energy<class_Light3D_property_light_volumetric_fog_energy>].



[Param<enum_Light3D_Param>] **PARAM_SPECULAR** = `3`

Constant for accessing [light_specular<class_Light3D_property_light_specular>].



[Param<enum_Light3D_Param>] **PARAM_RANGE** = `4`

Constant for accessing [OmniLight3D.omni_range<class_OmniLight3D_property_omni_range>] or [SpotLight3D.spot_range<class_SpotLight3D_property_spot_range>].



[Param<enum_Light3D_Param>] **PARAM_SIZE** = `5`

Constant for accessing [light_size<class_Light3D_property_light_size>].



[Param<enum_Light3D_Param>] **PARAM_ATTENUATION** = `6`

Constant for accessing [OmniLight3D.omni_attenuation<class_OmniLight3D_property_omni_attenuation>] or [SpotLight3D.spot_attenuation<class_SpotLight3D_property_spot_attenuation>].



[Param<enum_Light3D_Param>] **PARAM_SPOT_ANGLE** = `7`

Constant for accessing [SpotLight3D.spot_angle<class_SpotLight3D_property_spot_angle>].



[Param<enum_Light3D_Param>] **PARAM_SPOT_ATTENUATION** = `8`

Constant for accessing [SpotLight3D.spot_angle_attenuation<class_SpotLight3D_property_spot_angle_attenuation>].



[Param<enum_Light3D_Param>] **PARAM_SHADOW_MAX_DISTANCE** = `9`

Constant for accessing [DirectionalLight3D.directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>].



[Param<enum_Light3D_Param>] **PARAM_SHADOW_SPLIT_1_OFFSET** = `10`

Constant for accessing [DirectionalLight3D.directional_shadow_split_1<class_DirectionalLight3D_property_directional_shadow_split_1>].



[Param<enum_Light3D_Param>] **PARAM_SHADOW_SPLIT_2_OFFSET** = `11`

Constant for accessing [DirectionalLight3D.directional_shadow_split_2<class_DirectionalLight3D_property_directional_shadow_split_2>].



[Param<enum_Light3D_Param>] **PARAM_SHADOW_SPLIT_3_OFFSET** = `12`

Constant for accessing [DirectionalLight3D.directional_shadow_split_3<class_DirectionalLight3D_property_directional_shadow_split_3>].



[Param<enum_Light3D_Param>] **PARAM_SHADOW_FADE_START** = `13`

Constant for accessing [DirectionalLight3D.directional_shadow_fade_start<class_DirectionalLight3D_property_directional_shadow_fade_start>].



[Param<enum_Light3D_Param>] **PARAM_SHADOW_NORMAL_BIAS** = `14`

Constant for accessing [shadow_normal_bias<class_Light3D_property_shadow_normal_bias>].



[Param<enum_Light3D_Param>] **PARAM_SHADOW_BIAS** = `15`

Constant for accessing [shadow_bias<class_Light3D_property_shadow_bias>].



[Param<enum_Light3D_Param>] **PARAM_SHADOW_PANCAKE_SIZE** = `16`

Constant for accessing [DirectionalLight3D.directional_shadow_pancake_size<class_DirectionalLight3D_property_directional_shadow_pancake_size>].



[Param<enum_Light3D_Param>] **PARAM_SHADOW_OPACITY** = `17`

Constant for accessing [shadow_opacity<class_Light3D_property_shadow_opacity>].



[Param<enum_Light3D_Param>] **PARAM_SHADOW_BLUR** = `18`

Constant for accessing [shadow_blur<class_Light3D_property_shadow_blur>].



[Param<enum_Light3D_Param>] **PARAM_TRANSMITTANCE_BIAS** = `19`

Constant for accessing [shadow_transmittance_bias<class_Light3D_property_shadow_transmittance_bias>].



[Param<enum_Light3D_Param>] **PARAM_INTENSITY** = `20`

Constant for accessing [light_intensity_lumens<class_Light3D_property_light_intensity_lumens>] and [light_intensity_lux<class_Light3D_property_light_intensity_lux>]. Only used when [ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>] is `true`.



[Param<enum_Light3D_Param>] **PARAM_MAX** = `21`

Represents the size of the [Param<enum_Light3D_Param>] enum.


----



enum **BakeMode**: [🔗<enum_Light3D_BakeMode>]



[BakeMode<enum_Light3D_BakeMode>] **BAKE_DISABLED** = `0`

Light is ignored when baking. This is the fastest mode, but the light will not be taken into account when baking global illumination. This mode should generally be used for dynamic lights that change quickly, as the effect of global illumination is less noticeable on those lights.

\ **Note:** Hiding a light does *not* affect baking [LightmapGI<class_LightmapGI>]. Hiding a light will still affect baking [VoxelGI<class_VoxelGI>] and SDFGI (see [Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>]).



[BakeMode<enum_Light3D_BakeMode>] **BAKE_STATIC** = `1`

Light is taken into account in static baking ([VoxelGI<class_VoxelGI>], [LightmapGI<class_LightmapGI>], SDFGI ([Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>])). The light can be moved around or modified, but its global illumination will not update in real-time. This is suitable for subtle changes (such as flickering torches), but generally not large changes such as toggling a light on and off.

\ **Note:** The light is not baked in [LightmapGI<class_LightmapGI>] if [editor_only<class_Light3D_property_editor_only>] is `true`.



[BakeMode<enum_Light3D_BakeMode>] **BAKE_DYNAMIC** = `2`

Light is taken into account in dynamic baking ([VoxelGI<class_VoxelGI>] and SDFGI ([Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>]) only). The light can be moved around or modified with global illumination updating in real-time. The light's global illumination appearance will be slightly different compared to [BAKE_STATIC<class_Light3D_constant_BAKE_STATIC>]. This has a greater performance cost compared to [BAKE_STATIC<class_Light3D_constant_BAKE_STATIC>]. When using SDFGI, the update speed of dynamic lights is affected by [ProjectSettings.rendering/global_illumination/sdfgi/frames_to_update_lights<class_ProjectSettings_property_rendering/global_illumination/sdfgi/frames_to_update_lights>].


----


## Property Descriptions



[float<class_float>] **distance_fade_begin** = `40.0` [🔗<class_Light3D_property_distance_fade_begin>]


- |void| **set_distance_fade_begin**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_distance_fade_begin**\ (\ )

The distance from the camera at which the light begins to fade away (in 3D units).

\ **Note:** Only effective for [OmniLight3D<class_OmniLight3D>] and [SpotLight3D<class_SpotLight3D>].


----



[bool<class_bool>] **distance_fade_enabled** = `false` [🔗<class_Light3D_property_distance_fade_enabled>]


- |void| **set_enable_distance_fade**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_distance_fade_enabled**\ (\ )

If `true`, the light will smoothly fade away when far from the active [Camera3D<class_Camera3D>] starting at [distance_fade_begin<class_Light3D_property_distance_fade_begin>]. This acts as a form of level of detail (LOD). The light will fade out over [distance_fade_begin<class_Light3D_property_distance_fade_begin>] + [distance_fade_length<class_Light3D_property_distance_fade_length>], after which it will be culled and not sent to the shader at all. Use this to reduce the number of active lights in a scene and thus improve performance.

\ **Note:** Only effective for [OmniLight3D<class_OmniLight3D>] and [SpotLight3D<class_SpotLight3D>].


----



[float<class_float>] **distance_fade_length** = `10.0` [🔗<class_Light3D_property_distance_fade_length>]


- |void| **set_distance_fade_length**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_distance_fade_length**\ (\ )

Distance over which the light and its shadow fades. The light's energy and shadow's opacity is progressively reduced over this distance and is completely invisible at the end.

\ **Note:** Only effective for [OmniLight3D<class_OmniLight3D>] and [SpotLight3D<class_SpotLight3D>].


----



[float<class_float>] **distance_fade_shadow** = `50.0` [🔗<class_Light3D_property_distance_fade_shadow>]


- |void| **set_distance_fade_shadow**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_distance_fade_shadow**\ (\ )

The distance from the camera at which the light's shadow cuts off (in 3D units). Set this to a value lower than [distance_fade_begin<class_Light3D_property_distance_fade_begin>] + [distance_fade_length<class_Light3D_property_distance_fade_length>] to further improve performance, as shadow rendering is often more expensive than light rendering itself.

\ **Note:** Only effective for [OmniLight3D<class_OmniLight3D>] and [SpotLight3D<class_SpotLight3D>], and only when [shadow_enabled<class_Light3D_property_shadow_enabled>] is `true`.


----



[bool<class_bool>] **editor_only** = `false` [🔗<class_Light3D_property_editor_only>]


- |void| **set_editor_only**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_editor_only**\ (\ )

If `true`, the light only appears in the editor and will not be visible at runtime. If `true`, the light will never be baked in [LightmapGI<class_LightmapGI>] regardless of its [light_bake_mode<class_Light3D_property_light_bake_mode>].


----



[float<class_float>] **light_angular_distance** = `0.0` [🔗<class_Light3D_property_light_angular_distance>]


- |void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const|

The light's angular size in degrees. Increasing this will make shadows softer at greater distances (also called percentage-closer soft shadows, or PCSS). Only available for [DirectionalLight3D<class_DirectionalLight3D>]\ s. For reference, the Sun from the Earth is approximately `0.5`. Increasing this value above `0.0` for lights with shadows enabled will have a noticeable performance cost due to PCSS.

\ **Note:** [light_angular_distance<class_Light3D_property_light_angular_distance>] is not affected by [Node3D.scale<class_Node3D_property_scale>] (the light's scale or its parent's scale).

\ **Note:** PCSS for directional lights is only supported in the Forward+ rendering method, not Mobile or Compatibility.


----



[BakeMode<enum_Light3D_BakeMode>] **light_bake_mode** = `2` [🔗<class_Light3D_property_light_bake_mode>]


- |void| **set_bake_mode**\ (\ value\: [BakeMode<enum_Light3D_BakeMode>]\ )
- [BakeMode<enum_Light3D_BakeMode>] **get_bake_mode**\ (\ )

The light's bake mode. This will affect the global illumination techniques that have an effect on the light's rendering.

\ **Note:** Meshes' global illumination mode will also affect the global illumination rendering. See [GeometryInstance3D.gi_mode<class_GeometryInstance3D_property_gi_mode>].


----



[Color<class_Color>] **light_color** = `Color(1, 1, 1, 1)` [🔗<class_Light3D_property_light_color>]


- |void| **set_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_color**\ (\ )

The light's color in nonlinear sRGB encoding. An *overbright* color can be used to achieve a result equivalent to increasing the light's [light_energy<class_Light3D_property_light_energy>].


----



[int<class_int>] **light_cull_mask** = `4294967295` [🔗<class_Light3D_property_light_cull_mask>]


- |void| **set_cull_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_cull_mask**\ (\ )

The light will affect objects in the selected layers.

\ **Note:** The light cull mask is ignored by [VoxelGI<class_VoxelGI>], SDFGI, [LightmapGI<class_LightmapGI>], and volumetric fog. These will always render lights in a way that ignores the cull mask. See also [VisualInstance3D.layers<class_VisualInstance3D_property_layers>].


----



[float<class_float>] **light_energy** = `1.0` [🔗<class_Light3D_property_light_energy>]


- |void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const|

The light's strength multiplier (this is not a physical unit). For [OmniLight3D<class_OmniLight3D>] and [SpotLight3D<class_SpotLight3D>], changing this value will only change the light color's intensity, not the light's radius.


----



[float<class_float>] **light_indirect_energy** = `1.0` [🔗<class_Light3D_property_light_indirect_energy>]


- |void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const|

Secondary multiplier used with indirect light (light bounces). Used with [VoxelGI<class_VoxelGI>] and SDFGI (see [Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>]).

\ **Note:** This property is ignored if [light_energy<class_Light3D_property_light_energy>] is equal to `0.0`, as the light won't be present at all in the GI shader.


----



[float<class_float>] **light_intensity_lumens** [🔗<class_Light3D_property_light_intensity_lumens>]


- |void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const|

Used by positional lights ([OmniLight3D<class_OmniLight3D>] and [SpotLight3D<class_SpotLight3D>]) when [ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>] is `true`. Sets the intensity of the light source measured in Lumens. Lumens are a measure of luminous flux, which is the total amount of visible light emitted by a light source per unit of time.

For [SpotLight3D<class_SpotLight3D>]\ s, we assume that the area outside the visible cone is surrounded by a perfect light absorbing material. Accordingly, the apparent brightness of the cone area does not change as the cone increases and decreases in size.

A typical household lightbulb can range from around 600 lumens to 1,200 lumens, a candle is about 13 lumens, while a streetlight can be approximately 60,000 lumens.


----



[float<class_float>] **light_intensity_lux** [🔗<class_Light3D_property_light_intensity_lux>]


- |void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const|

Used by [DirectionalLight3D<class_DirectionalLight3D>]\ s when [ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>] is `true`. Sets the intensity of the light source measured in Lux. Lux is a measure of luminous flux per unit area, it is equal to one lumen per square meter. Lux is the measure of how much light hits a surface at a given time.

On a clear sunny day a surface in direct sunlight may be approximately 100,000 lux, a typical room in a home may be approximately 50 lux, while the moonlit ground may be approximately 0.1 lux.


----



[bool<class_bool>] **light_negative** = `false` [🔗<class_Light3D_property_light_negative>]


- |void| **set_negative**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_negative**\ (\ )

If `true`, the light's effect is reversed, darkening areas and casting bright shadows.


----



[Texture2D<class_Texture2D>] **light_projector** [🔗<class_Light3D_property_light_projector>]


- |void| **set_projector**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_projector**\ (\ )

[Texture2D<class_Texture2D>] projected by light. [shadow_enabled<class_Light3D_property_shadow_enabled>] must be on for the projector to work. Light projectors make the light appear as if it is shining through a colored but transparent object, almost like light shining through stained-glass.

\ **Note:** Unlike [BaseMaterial3D<class_BaseMaterial3D>] whose filter mode can be adjusted on a per-material basis, the filter mode for light projector textures is set globally with [ProjectSettings.rendering/textures/light_projectors/filter<class_ProjectSettings_property_rendering/textures/light_projectors/filter>].

\ **Note:** Light projector textures are only supported in the Forward+ and Mobile rendering methods, not Compatibility.


----



[float<class_float>] **light_size** = `0.0` [🔗<class_Light3D_property_light_size>]


- |void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const|

The size of the light in Godot units. Only available for [OmniLight3D<class_OmniLight3D>]\ s and [SpotLight3D<class_SpotLight3D>]\ s. Increasing this value will make the light fade out slower and shadows appear blurrier (also called percentage-closer soft shadows, or PCSS). This can be used to simulate area lights to an extent. Increasing this value above `0.0` for lights with shadows enabled will have a noticeable performance cost due to PCSS.

\ **Note:** [light_size<class_Light3D_property_light_size>] is not affected by [Node3D.scale<class_Node3D_property_scale>] (the light's scale or its parent's scale).

\ **Note:** PCSS for positional lights is only supported in the Forward+ and Mobile rendering methods, not Compatibility.


----



[float<class_float>] **light_specular** = `1.0` [🔗<class_Light3D_property_light_specular>]


- |void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const|

The intensity of the specular blob in objects affected by the light. At `0`, the light becomes a pure diffuse light. When not baking emission, this can be used to avoid unrealistic reflections when placing lights above an emissive surface.


----



[float<class_float>] **light_temperature** [🔗<class_Light3D_property_light_temperature>]


- |void| **set_temperature**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_temperature**\ (\ )

Sets the color temperature of the light source, measured in Kelvin. This is used to calculate a correlated color temperature which tints the [light_color<class_Light3D_property_light_color>].

The sun on a cloudy day is approximately 6500 Kelvin, on a clear day it is between 5500 to 6000 Kelvin, and on a clear day at sunrise or sunset it ranges to around 1850 Kelvin.


----



[float<class_float>] **light_volumetric_fog_energy** = `1.0` [🔗<class_Light3D_property_light_volumetric_fog_energy>]


- |void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const|

Secondary multiplier multiplied with [light_energy<class_Light3D_property_light_energy>] then used with the [Environment<class_Environment>]'s volumetric fog (if enabled). If set to `0.0`, computing volumetric fog will be skipped for this light, which can improve performance for large amounts of lights when volumetric fog is enabled.

\ **Note:** To prevent short-lived dynamic light effects from poorly interacting with volumetric fog, lights used in those effects should have [light_volumetric_fog_energy<class_Light3D_property_light_volumetric_fog_energy>] set to `0.0` unless [Environment.volumetric_fog_temporal_reprojection_enabled<class_Environment_property_volumetric_fog_temporal_reprojection_enabled>] is disabled (or unless the reprojection amount is significantly lowered).


----



[float<class_float>] **shadow_bias** = `0.1` [🔗<class_Light3D_property_shadow_bias>]


- |void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const|

Used to adjust shadow appearance. Too small a value results in self-shadowing ("shadow acne"), while too large a value causes shadows to separate from casters ("peter-panning"). Adjust as needed.


----



[float<class_float>] **shadow_blur** = `1.0` [🔗<class_Light3D_property_shadow_blur>]


- |void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const|

Blurs the edges of the shadow. Can be used to hide pixel artifacts in low-resolution shadow maps. A high value can impact performance, make shadows appear grainy and can cause other unwanted artifacts. Try to keep as near default as possible.


----



[int<class_int>] **shadow_caster_mask** = `4294967295` [🔗<class_Light3D_property_shadow_caster_mask>]


- |void| **set_shadow_caster_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_shadow_caster_mask**\ (\ )

The light will only cast shadows using objects in the selected layers.


----



[bool<class_bool>] **shadow_enabled** = `false` [🔗<class_Light3D_property_shadow_enabled>]


- |void| **set_shadow**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **has_shadow**\ (\ )

If `true`, the light will cast real-time shadows. This has a significant performance cost. Only enable shadow rendering when it makes a noticeable difference in the scene's appearance, and consider using [distance_fade_enabled<class_Light3D_property_distance_fade_enabled>] to hide the light when far away from the [Camera3D<class_Camera3D>].


----



[float<class_float>] **shadow_normal_bias** = `2.0` [🔗<class_Light3D_property_shadow_normal_bias>]


- |void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const|

Offsets the lookup into the shadow map by the object's normal. This can be used to reduce self-shadowing artifacts without using [shadow_bias<class_Light3D_property_shadow_bias>]. In practice, this value should be tweaked along with [shadow_bias<class_Light3D_property_shadow_bias>] to reduce artifacts as much as possible.


----



[float<class_float>] **shadow_opacity** = `1.0` [🔗<class_Light3D_property_shadow_opacity>]


- |void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const|

The opacity to use when rendering the light's shadow map. Values lower than `1.0` make the light appear through shadows. This can be used to fake global illumination at a low performance cost.


----



[bool<class_bool>] **shadow_reverse_cull_face** = `false` [🔗<class_Light3D_property_shadow_reverse_cull_face>]


- |void| **set_shadow_reverse_cull_face**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_shadow_reverse_cull_face**\ (\ )

If `true`, reverses the backface culling of the mesh. This can be useful when you have a flat mesh that has a light behind it. If you need to cast a shadow on both sides of the mesh, set the mesh to use double-sided shadows with [GeometryInstance3D.SHADOW_CASTING_SETTING_DOUBLE_SIDED<class_GeometryInstance3D_constant_SHADOW_CASTING_SETTING_DOUBLE_SIDED>].


----



[float<class_float>] **shadow_transmittance_bias** = `0.05` [🔗<class_Light3D_property_shadow_transmittance_bias>]


- |void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ )
- [float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const|

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----


## Method Descriptions



[Color<class_Color>] **get_correlated_color**\ (\ ) |const| [🔗<class_Light3D_method_get_correlated_color>]

Returns the [Color<class_Color>] of an idealized blackbody at the given [light_temperature<class_Light3D_property_light_temperature>]. This value is calculated internally based on the [light_temperature<class_Light3D_property_light_temperature>]. This [Color<class_Color>] is multiplied by [light_color<class_Light3D_property_light_color>] before being sent to the [RenderingServer<class_RenderingServer>].


----



[float<class_float>] **get_param**\ (\ param\: [Param<enum_Light3D_Param>]\ ) |const| [🔗<class_Light3D_method_get_param>]

Returns the value of the specified [Param<enum_Light3D_Param>] parameter.


----



|void| **set_param**\ (\ param\: [Param<enum_Light3D_Param>], value\: [float<class_float>]\ ) [🔗<class_Light3D_method_set_param>]

Sets the value of the specified [Param<enum_Light3D_Param>] parameter.

