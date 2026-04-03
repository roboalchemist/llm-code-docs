:github_url: hide



# LightmapGI

**Inherits:** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Computes and stores baked lightmaps for fast global illumination.


## Description

The **LightmapGI** node is used to compute and store baked lightmaps. Lightmaps are used to provide high-quality indirect lighting with very little light leaking. **LightmapGI** can also provide rough reflections using spherical harmonics if [directional<class_LightmapGI_property_directional>] is enabled. Dynamic objects can receive indirect lighting thanks to *light probes*, which can be automatically placed by setting [generate_probes_subdiv<class_LightmapGI_property_generate_probes_subdiv>] to a value other than [GENERATE_PROBES_DISABLED<class_LightmapGI_constant_GENERATE_PROBES_DISABLED>]. Additional lightmap probes can also be added by creating [LightmapProbe<class_LightmapProbe>] nodes. The downside is that lightmaps are fully static and cannot be baked in an exported project. Baking a **LightmapGI** node is also slower compared to [VoxelGI<class_VoxelGI>].

\ **Procedural generation:** Lightmap baking functionality is only available in the editor. This means **LightmapGI** is not suited to procedurally generated or user-built levels. For procedurally generated or user-built levels, use [VoxelGI<class_VoxelGI>] or SDFGI instead (see [Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>]).

\ **Performance:** **LightmapGI** provides the best possible run-time performance for global illumination. It is suitable for low-end hardware including integrated graphics and mobile devices.

\ **Note:** Due to how lightmaps work, most properties only have a visible effect once lightmaps are baked again.

\ **Note:** Lightmap baking on [CSGShape3D<class_CSGShape3D>]\ s and [PrimitiveMesh<class_PrimitiveMesh>]\ es is not supported, as these cannot store UV2 data required for baking.

\ **Note:** If no custom lightmappers are installed, **LightmapGI** can only be baked from devices that support the Forward+ or Mobile renderers.

\ **Note:** The **LightmapGI** node only bakes light data for child nodes of its parent. Nodes further up the hierarchy of the scene will not be baked.


## Tutorials

- [../tutorials/3d/global_illumination/using_lightmap_gi](Using Lightmap global illumination .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                 | :ref:`bias<class_LightmapGI_property_bias>`                                           | ``0.0005``            |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                 | :ref:`bounce_indirect_energy<class_LightmapGI_property_bounce_indirect_energy>`       | ``1.0``               |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                                     | :ref:`bounces<class_LightmapGI_property_bounces>`                                     | ``3``                 |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`CameraAttributes<class_CameraAttributes>`           | :ref:`camera_attributes<class_LightmapGI_property_camera_attributes>`                 |                       |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                                     | :ref:`denoiser_range<class_LightmapGI_property_denoiser_range>`                       | ``10``                |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                 | :ref:`denoiser_strength<class_LightmapGI_property_denoiser_strength>`                 | ``0.1``               |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`directional<class_LightmapGI_property_directional>`                             | ``false``             |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`                                 | :ref:`environment_custom_color<class_LightmapGI_property_environment_custom_color>`   | ``Color(1, 1, 1, 1)`` |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                 | :ref:`environment_custom_energy<class_LightmapGI_property_environment_custom_energy>` | ``1.0``               |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Sky<class_Sky>`                                     | :ref:`environment_custom_sky<class_LightmapGI_property_environment_custom_sky>`       |                       |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`EnvironmentMode<enum_LightmapGI_EnvironmentMode>`   | :ref:`environment_mode<class_LightmapGI_property_environment_mode>`                   | ``1``                 |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`GenerateProbes<enum_LightmapGI_GenerateProbes>`     | :ref:`generate_probes_subdiv<class_LightmapGI_property_generate_probes_subdiv>`       | ``2``                 |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`interior<class_LightmapGI_property_interior>`                                   | ``false``             |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`LightmapGIData<class_LightmapGIData>`               | :ref:`light_data<class_LightmapGI_property_light_data>`                               |                       |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                                     | :ref:`max_texture_size<class_LightmapGI_property_max_texture_size>`                   | ``16384``             |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`BakeQuality<enum_LightmapGI_BakeQuality>`           | :ref:`quality<class_LightmapGI_property_quality>`                                     | ``1``                 |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`ShadowmaskMode<enum_LightmapGIData_ShadowmaskMode>` | :ref:`shadowmask_mode<class_LightmapGI_property_shadowmask_mode>`                     | ``0``                 |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`supersampling<class_LightmapGI_property_supersampling>`                         | ``false``             |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                 | :ref:`supersampling_factor<class_LightmapGI_property_supersampling_factor>`           | ``2.0``               |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                                 | :ref:`texel_scale<class_LightmapGI_property_texel_scale>`                             | ``1.0``               |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`use_denoiser<class_LightmapGI_property_use_denoiser>`                           | ``true``              |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`use_texture_for_bounces<class_LightmapGI_property_use_texture_for_bounces>`     | ``true``              |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
>

----


## Enumerations



enum **BakeQuality**: [🔗<enum_LightmapGI_BakeQuality>]



[BakeQuality<enum_LightmapGI_BakeQuality>] **BAKE_QUALITY_LOW** = `0`

Low bake quality (fastest bake times). The quality of this preset can be adjusted by changing [ProjectSettings.rendering/lightmapping/bake_quality/low_quality_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/low_quality_ray_count>] and [ProjectSettings.rendering/lightmapping/bake_quality/low_quality_probe_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/low_quality_probe_ray_count>].



[BakeQuality<enum_LightmapGI_BakeQuality>] **BAKE_QUALITY_MEDIUM** = `1`

Medium bake quality (fast bake times). The quality of this preset can be adjusted by changing [ProjectSettings.rendering/lightmapping/bake_quality/medium_quality_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/medium_quality_ray_count>] and [ProjectSettings.rendering/lightmapping/bake_quality/medium_quality_probe_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/medium_quality_probe_ray_count>].



[BakeQuality<enum_LightmapGI_BakeQuality>] **BAKE_QUALITY_HIGH** = `2`

High bake quality (slow bake times). The quality of this preset can be adjusted by changing [ProjectSettings.rendering/lightmapping/bake_quality/high_quality_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/high_quality_ray_count>] and [ProjectSettings.rendering/lightmapping/bake_quality/high_quality_probe_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/high_quality_probe_ray_count>].



[BakeQuality<enum_LightmapGI_BakeQuality>] **BAKE_QUALITY_ULTRA** = `3`

Highest bake quality (slowest bake times). The quality of this preset can be adjusted by changing [ProjectSettings.rendering/lightmapping/bake_quality/ultra_quality_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/ultra_quality_ray_count>] and [ProjectSettings.rendering/lightmapping/bake_quality/ultra_quality_probe_ray_count<class_ProjectSettings_property_rendering/lightmapping/bake_quality/ultra_quality_probe_ray_count>].


----



enum **GenerateProbes**: [🔗<enum_LightmapGI_GenerateProbes>]



[GenerateProbes<enum_LightmapGI_GenerateProbes>] **GENERATE_PROBES_DISABLED** = `0`

Don't generate lightmap probes for lighting dynamic objects.



[GenerateProbes<enum_LightmapGI_GenerateProbes>] **GENERATE_PROBES_SUBDIV_4** = `1`

Lowest level of subdivision (fastest bake times, smallest file sizes).



[GenerateProbes<enum_LightmapGI_GenerateProbes>] **GENERATE_PROBES_SUBDIV_8** = `2`

Low level of subdivision (fast bake times, small file sizes).



[GenerateProbes<enum_LightmapGI_GenerateProbes>] **GENERATE_PROBES_SUBDIV_16** = `3`

High level of subdivision (slow bake times, large file sizes).



[GenerateProbes<enum_LightmapGI_GenerateProbes>] **GENERATE_PROBES_SUBDIV_32** = `4`

Highest level of subdivision (slowest bake times, largest file sizes).


----



enum **BakeError**: [🔗<enum_LightmapGI_BakeError>]



[BakeError<enum_LightmapGI_BakeError>] **BAKE_ERROR_OK** = `0`

Lightmap baking was successful.



[BakeError<enum_LightmapGI_BakeError>] **BAKE_ERROR_NO_SCENE_ROOT** = `1`

Lightmap baking failed because the root node for the edited scene could not be accessed.



[BakeError<enum_LightmapGI_BakeError>] **BAKE_ERROR_FOREIGN_DATA** = `2`

Lightmap baking failed as the lightmap data resource is embedded in a foreign resource.



[BakeError<enum_LightmapGI_BakeError>] **BAKE_ERROR_NO_LIGHTMAPPER** = `3`

Lightmap baking failed as there is no lightmapper available in this Godot build.



[BakeError<enum_LightmapGI_BakeError>] **BAKE_ERROR_NO_SAVE_PATH** = `4`

Lightmap baking failed as the [LightmapGIData<class_LightmapGIData>] save path isn't configured in the resource.



[BakeError<enum_LightmapGI_BakeError>] **BAKE_ERROR_NO_MESHES** = `5`

Lightmap baking failed as there are no meshes whose [GeometryInstance3D.gi_mode<class_GeometryInstance3D_property_gi_mode>] is [GeometryInstance3D.GI_MODE_STATIC<class_GeometryInstance3D_constant_GI_MODE_STATIC>] and with valid UV2 mapping in the current scene. You may need to select 3D scenes in the Import dock and change their global illumination mode accordingly.



[BakeError<enum_LightmapGI_BakeError>] **BAKE_ERROR_MESHES_INVALID** = `6`

Lightmap baking failed as the lightmapper failed to analyze some of the meshes marked as static for baking.



[BakeError<enum_LightmapGI_BakeError>] **BAKE_ERROR_CANT_CREATE_IMAGE** = `7`

Lightmap baking failed as the resulting image couldn't be saved or imported by Godot after it was saved.



[BakeError<enum_LightmapGI_BakeError>] **BAKE_ERROR_USER_ABORTED** = `8`

The user aborted the lightmap baking operation (typically by clicking the **Cancel** button in the progress dialog).



[BakeError<enum_LightmapGI_BakeError>] **BAKE_ERROR_TEXTURE_SIZE_TOO_SMALL** = `9`

Lightmap baking failed as the maximum texture size is too small to fit some of the meshes marked for baking.



[BakeError<enum_LightmapGI_BakeError>] **BAKE_ERROR_LIGHTMAP_TOO_SMALL** = `10`

Lightmap baking failed as the lightmap is too small.



[BakeError<enum_LightmapGI_BakeError>] **BAKE_ERROR_ATLAS_TOO_SMALL** = `11`

Lightmap baking failed as the lightmap was unable to fit into an atlas.


----



enum **EnvironmentMode**: [🔗<enum_LightmapGI_EnvironmentMode>]



[EnvironmentMode<enum_LightmapGI_EnvironmentMode>] **ENVIRONMENT_MODE_DISABLED** = `0`

Ignore environment lighting when baking lightmaps.



[EnvironmentMode<enum_LightmapGI_EnvironmentMode>] **ENVIRONMENT_MODE_SCENE** = `1`

Use the scene's environment lighting when baking lightmaps.

\ **Note:** If baking lightmaps in a scene with no [WorldEnvironment<class_WorldEnvironment>] node, this will act like [ENVIRONMENT_MODE_DISABLED<class_LightmapGI_constant_ENVIRONMENT_MODE_DISABLED>]. The editor's preview sky and sun is *not* taken into account by **LightmapGI** when baking lightmaps.



[EnvironmentMode<enum_LightmapGI_EnvironmentMode>] **ENVIRONMENT_MODE_CUSTOM_SKY** = `2`

Use [environment_custom_sky<class_LightmapGI_property_environment_custom_sky>] as a source of environment lighting when baking lightmaps.



[EnvironmentMode<enum_LightmapGI_EnvironmentMode>] **ENVIRONMENT_MODE_CUSTOM_COLOR** = `3`

Use [environment_custom_color<class_LightmapGI_property_environment_custom_color>] multiplied by [environment_custom_energy<class_LightmapGI_property_environment_custom_energy>] as a constant source of environment lighting when baking lightmaps.


----


## Property Descriptions



[float<class_float>] **bias** = `0.0005` [🔗<class_LightmapGI_property_bias>]


- |void| **set_bias**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_bias**\ (\ )

The bias to use when computing shadows. Increasing [bias<class_LightmapGI_property_bias>] can fix shadow acne on the resulting baked lightmap, but can introduce peter-panning (shadows not connecting to their casters). Real-time [Light3D<class_Light3D>] shadows are not affected by this [bias<class_LightmapGI_property_bias>] property.


----



[float<class_float>] **bounce_indirect_energy** = `1.0` [🔗<class_LightmapGI_property_bounce_indirect_energy>]


- |void| **set_bounce_indirect_energy**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_bounce_indirect_energy**\ (\ )

The energy multiplier for each bounce. Higher values will make indirect lighting brighter. A value of `1.0` represents physically accurate behavior, but higher values can be used to make indirect lighting propagate more visibly when using a low number of bounces. This can be used to speed up bake times by lowering the number of [bounces<class_LightmapGI_property_bounces>] then increasing [bounce_indirect_energy<class_LightmapGI_property_bounce_indirect_energy>].

\ **Note:** [bounce_indirect_energy<class_LightmapGI_property_bounce_indirect_energy>] only has an effect if [bounces<class_LightmapGI_property_bounces>] is set to a value greater than or equal to `1`.


----



[int<class_int>] **bounces** = `3` [🔗<class_LightmapGI_property_bounces>]


- |void| **set_bounces**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_bounces**\ (\ )

Number of light bounces that are taken into account during baking. Higher values result in brighter, more realistic lighting, at the cost of longer bake times. If set to `0`, only environment lighting, direct light and emissive lighting is baked.


----



[CameraAttributes<class_CameraAttributes>] **camera_attributes** [🔗<class_LightmapGI_property_camera_attributes>]


- |void| **set_camera_attributes**\ (\ value\: [CameraAttributes<class_CameraAttributes>]\ )
- [CameraAttributes<class_CameraAttributes>] **get_camera_attributes**\ (\ )

The [CameraAttributes<class_CameraAttributes>] resource that specifies exposure levels to bake at. Auto-exposure and non exposure properties will be ignored. Exposure settings should be used to reduce the dynamic range present when baking. If exposure is too high, the **LightmapGI** will have banding artifacts or may have over-exposure artifacts.


----



[int<class_int>] **denoiser_range** = `10` [🔗<class_LightmapGI_property_denoiser_range>]


- |void| **set_denoiser_range**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_denoiser_range**\ (\ )

The distance in pixels from which the denoiser samples. Lower values preserve more details, but may give blotchy results if the lightmap quality is not high enough. Only effective if [use_denoiser<class_LightmapGI_property_use_denoiser>] is `true` and [ProjectSettings.rendering/lightmapping/denoising/denoiser<class_ProjectSettings_property_rendering/lightmapping/denoising/denoiser>] is set to JNLM.


----



[float<class_float>] **denoiser_strength** = `0.1` [🔗<class_LightmapGI_property_denoiser_strength>]


- |void| **set_denoiser_strength**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_denoiser_strength**\ (\ )

The strength of denoising step applied to the generated lightmaps. Only effective if [use_denoiser<class_LightmapGI_property_use_denoiser>] is `true` and [ProjectSettings.rendering/lightmapping/denoising/denoiser<class_ProjectSettings_property_rendering/lightmapping/denoising/denoiser>] is set to JNLM.


----



[bool<class_bool>] **directional** = `false` [🔗<class_LightmapGI_property_directional>]


- |void| **set_directional**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_directional**\ (\ )

If `true`, bakes lightmaps to contain directional information as spherical harmonics. This results in more realistic lighting appearance, especially with normal mapped materials and for lights that have their direct light baked ([Light3D.light_bake_mode<class_Light3D_property_light_bake_mode>] set to [Light3D.BAKE_STATIC<class_Light3D_constant_BAKE_STATIC>] and with [Light3D.editor_only<class_Light3D_property_editor_only>] set to `false`). The directional information is also used to provide rough reflections for static and dynamic objects. This has a small run-time performance cost as the shader has to perform more work to interpret the direction information from the lightmap. Directional lightmaps also take longer to bake and result in larger file sizes.

\ **Note:** The property's name has no relationship with [DirectionalLight3D<class_DirectionalLight3D>]. [directional<class_LightmapGI_property_directional>] works with all light types.


----



[Color<class_Color>] **environment_custom_color** = `Color(1, 1, 1, 1)` [🔗<class_LightmapGI_property_environment_custom_color>]


- |void| **set_environment_custom_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_environment_custom_color**\ (\ )

The color to use for environment lighting. Only effective if [environment_mode<class_LightmapGI_property_environment_mode>] is [ENVIRONMENT_MODE_CUSTOM_COLOR<class_LightmapGI_constant_ENVIRONMENT_MODE_CUSTOM_COLOR>].


----



[float<class_float>] **environment_custom_energy** = `1.0` [🔗<class_LightmapGI_property_environment_custom_energy>]


- |void| **set_environment_custom_energy**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_environment_custom_energy**\ (\ )

The color multiplier to use for environment lighting. Only effective if [environment_mode<class_LightmapGI_property_environment_mode>] is [ENVIRONMENT_MODE_CUSTOM_COLOR<class_LightmapGI_constant_ENVIRONMENT_MODE_CUSTOM_COLOR>].


----



[Sky<class_Sky>] **environment_custom_sky** [🔗<class_LightmapGI_property_environment_custom_sky>]


- |void| **set_environment_custom_sky**\ (\ value\: [Sky<class_Sky>]\ )
- [Sky<class_Sky>] **get_environment_custom_sky**\ (\ )

The sky to use as a source of environment lighting. Only effective if [environment_mode<class_LightmapGI_property_environment_mode>] is [ENVIRONMENT_MODE_CUSTOM_SKY<class_LightmapGI_constant_ENVIRONMENT_MODE_CUSTOM_SKY>].


----



[EnvironmentMode<enum_LightmapGI_EnvironmentMode>] **environment_mode** = `1` [🔗<class_LightmapGI_property_environment_mode>]


- |void| **set_environment_mode**\ (\ value\: [EnvironmentMode<enum_LightmapGI_EnvironmentMode>]\ )
- [EnvironmentMode<enum_LightmapGI_EnvironmentMode>] **get_environment_mode**\ (\ )

The environment mode to use when baking lightmaps.


----



[GenerateProbes<enum_LightmapGI_GenerateProbes>] **generate_probes_subdiv** = `2` [🔗<class_LightmapGI_property_generate_probes_subdiv>]


- |void| **set_generate_probes**\ (\ value\: [GenerateProbes<enum_LightmapGI_GenerateProbes>]\ )
- [GenerateProbes<enum_LightmapGI_GenerateProbes>] **get_generate_probes**\ (\ )

The level of subdivision to use when automatically generating [LightmapProbe<class_LightmapProbe>]\ s for dynamic object lighting. Higher values result in more accurate indirect lighting on dynamic objects, at the cost of longer bake times and larger file sizes.

\ **Note:** Automatically generated [LightmapProbe<class_LightmapProbe>]\ s are not visible as nodes in the Scene tree dock, and cannot be modified this way after they are generated.

\ **Note:** Regardless of [generate_probes_subdiv<class_LightmapGI_property_generate_probes_subdiv>], direct lighting on dynamic objects is always applied using [Light3D<class_Light3D>] nodes in real-time.


----



[bool<class_bool>] **interior** = `false` [🔗<class_LightmapGI_property_interior>]


- |void| **set_interior**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_interior**\ (\ )

If `true`, ignore environment lighting when baking lightmaps.


----



[LightmapGIData<class_LightmapGIData>] **light_data** [🔗<class_LightmapGI_property_light_data>]


- |void| **set_light_data**\ (\ value\: [LightmapGIData<class_LightmapGIData>]\ )
- [LightmapGIData<class_LightmapGIData>] **get_light_data**\ (\ )

The [LightmapGIData<class_LightmapGIData>] associated to this **LightmapGI** node. This resource is automatically created after baking, and is not meant to be created manually.


----



[int<class_int>] **max_texture_size** = `16384` [🔗<class_LightmapGI_property_max_texture_size>]


- |void| **set_max_texture_size**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_max_texture_size**\ (\ )

The maximum texture size for the generated texture atlas. Higher values will result in fewer slices being generated, but may not work on all hardware as a result of hardware limitations on texture sizes. Leave [max_texture_size<class_LightmapGI_property_max_texture_size>] at its default value of `16384` if unsure.


----



[BakeQuality<enum_LightmapGI_BakeQuality>] **quality** = `1` [🔗<class_LightmapGI_property_quality>]


- |void| **set_bake_quality**\ (\ value\: [BakeQuality<enum_LightmapGI_BakeQuality>]\ )
- [BakeQuality<enum_LightmapGI_BakeQuality>] **get_bake_quality**\ (\ )

The quality preset to use when baking lightmaps. This affects bake times, but output file sizes remain mostly identical across quality levels.

To further speed up bake times, decrease [bounces<class_LightmapGI_property_bounces>], disable [use_denoiser<class_LightmapGI_property_use_denoiser>] and/or decrease [texel_scale<class_LightmapGI_property_texel_scale>].

To further increase quality, enable [supersampling<class_LightmapGI_property_supersampling>] and/or increase [texel_scale<class_LightmapGI_property_texel_scale>].


----



[ShadowmaskMode<enum_LightmapGIData_ShadowmaskMode>] **shadowmask_mode** = `0` [🔗<class_LightmapGI_property_shadowmask_mode>]


- |void| **set_shadowmask_mode**\ (\ value\: [ShadowmaskMode<enum_LightmapGIData_ShadowmaskMode>]\ )
- [ShadowmaskMode<enum_LightmapGIData_ShadowmaskMode>] **get_shadowmask_mode**\ (\ )

**Experimental:** This property may be changed or removed in future versions.

The shadowmasking policy to use for directional shadows on static objects that are baked with this **LightmapGI** instance.

Shadowmasking allows [DirectionalLight3D<class_DirectionalLight3D>] nodes to cast shadows even outside the range defined by their [DirectionalLight3D.directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>] property. This is done by baking a texture that contains a shadowmap for the directional light, then using this texture according to the current shadowmask mode.

\ **Note:** The shadowmask texture is only created if [shadowmask_mode<class_LightmapGI_property_shadowmask_mode>] is not [LightmapGIData.SHADOWMASK_MODE_NONE<class_LightmapGIData_constant_SHADOWMASK_MODE_NONE>]. To see a difference, you need to bake lightmaps again after switching from [LightmapGIData.SHADOWMASK_MODE_NONE<class_LightmapGIData_constant_SHADOWMASK_MODE_NONE>] to any other mode.


----



[bool<class_bool>] **supersampling** = `false` [🔗<class_LightmapGI_property_supersampling>]


- |void| **set_supersampling_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_supersampling_enabled**\ (\ )

If `true`, lightmaps are baked with the texel scale multiplied with [supersampling_factor<class_LightmapGI_property_supersampling_factor>] and downsampled before saving the lightmap (so the effective texel density is identical to having supersampling disabled).

Supersampling provides increased lightmap quality with less noise, smoother shadows and better shadowing of small-scale features in objects. However, it may result in significantly increased bake times and memory usage while baking lightmaps. Padding is automatically adjusted to avoid increasing light leaking.


----



[float<class_float>] **supersampling_factor** = `2.0` [🔗<class_LightmapGI_property_supersampling_factor>]


- |void| **set_supersampling_factor**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_supersampling_factor**\ (\ )

The factor by which the texel density is multiplied for supersampling. For best results, use an integer value. While fractional values are allowed, they can result in increased light leaking and a blurry lightmap.

Higher values may result in better quality, but also increase bake times and memory usage while baking.

See [supersampling<class_LightmapGI_property_supersampling>] for more information.


----



[float<class_float>] **texel_scale** = `1.0` [🔗<class_LightmapGI_property_texel_scale>]


- |void| **set_texel_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_texel_scale**\ (\ )

Scales the lightmap texel density of all meshes for the current bake. This is a multiplier that builds upon the existing lightmap texel size defined in each imported 3D scene, along with the per-mesh density multiplier (which is designed to be used when the same mesh is used at different scales). Lower values will result in faster bake times.

For example, doubling [texel_scale<class_LightmapGI_property_texel_scale>] doubles the lightmap texture resolution for all objects *on each axis*, so it will *quadruple* the texel count.


----



[bool<class_bool>] **use_denoiser** = `true` [🔗<class_LightmapGI_property_use_denoiser>]


- |void| **set_use_denoiser**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_denoiser**\ (\ )

If `true`, uses a GPU-based denoising algorithm on the generated lightmap. This eliminates most noise within the generated lightmap at the cost of longer bake times. File sizes are generally not impacted significantly by the use of a denoiser, although lossless compression may do a better job at compressing a denoised image.


----



[bool<class_bool>] **use_texture_for_bounces** = `true` [🔗<class_LightmapGI_property_use_texture_for_bounces>]


- |void| **set_use_texture_for_bounces**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_texture_for_bounces**\ (\ )

If `true`, a texture with the lighting information will be generated to speed up the generation of indirect lighting at the cost of some accuracy. The geometry might exhibit extra light leak artifacts when using low resolution lightmaps or UVs that stretch the lightmap significantly across surfaces. Leave [use_texture_for_bounces<class_LightmapGI_property_use_texture_for_bounces>] at its default value of `true` if unsure.

\ **Note:** [use_texture_for_bounces<class_LightmapGI_property_use_texture_for_bounces>] only has an effect if [bounces<class_LightmapGI_property_bounces>] is set to a value greater than or equal to `1`.

