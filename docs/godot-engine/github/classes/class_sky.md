:github_url: hide



# Sky

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Defines a 3D environment's background by using a [Material<class_Material>].


## Description

The **Sky** class uses a [Material<class_Material>] to render a 3D environment's background and the light it emits by updating the reflection/radiance cubemaps.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------+--------------------------------------------------------+-------+
> | :ref:`ProcessMode<enum_Sky_ProcessMode>`   | :ref:`process_mode<class_Sky_property_process_mode>`   | ``0`` |
> +--------------------------------------------+--------------------------------------------------------+-------+
> | :ref:`RadianceSize<enum_Sky_RadianceSize>` | :ref:`radiance_size<class_Sky_property_radiance_size>` | ``3`` |
> +--------------------------------------------+--------------------------------------------------------+-------+
> | :ref:`Material<class_Material>`            | :ref:`sky_material<class_Sky_property_sky_material>`   |       |
> +--------------------------------------------+--------------------------------------------------------+-------+
>

----


## Enumerations



enum **RadianceSize**: [🔗<enum_Sky_RadianceSize>]



[RadianceSize<enum_Sky_RadianceSize>] **RADIANCE_SIZE_32** = `0`

Radiance texture size is 32×32 pixels.



[RadianceSize<enum_Sky_RadianceSize>] **RADIANCE_SIZE_64** = `1`

Radiance texture size is 64×64 pixels.



[RadianceSize<enum_Sky_RadianceSize>] **RADIANCE_SIZE_128** = `2`

Radiance texture size is 128×128 pixels.



[RadianceSize<enum_Sky_RadianceSize>] **RADIANCE_SIZE_256** = `3`

Radiance texture size is 256×256 pixels.



[RadianceSize<enum_Sky_RadianceSize>] **RADIANCE_SIZE_512** = `4`

Radiance texture size is 512×512 pixels.



[RadianceSize<enum_Sky_RadianceSize>] **RADIANCE_SIZE_1024** = `5`

Radiance texture size is 1024×1024 pixels.



[RadianceSize<enum_Sky_RadianceSize>] **RADIANCE_SIZE_2048** = `6`

Radiance texture size is 2048×2048 pixels.



[RadianceSize<enum_Sky_RadianceSize>] **RADIANCE_SIZE_MAX** = `7`

Represents the size of the [RadianceSize<enum_Sky_RadianceSize>] enum.


----



enum **ProcessMode**: [🔗<enum_Sky_ProcessMode>]



[ProcessMode<enum_Sky_ProcessMode>] **PROCESS_MODE_AUTOMATIC** = `0`

Automatically selects the appropriate process mode based on your sky shader. If your shader uses `TIME` or `POSITION`, this will use [PROCESS_MODE_REALTIME<class_Sky_constant_PROCESS_MODE_REALTIME>]. If your shader uses any of the `LIGHT_*` variables or any custom uniforms, this uses [PROCESS_MODE_INCREMENTAL<class_Sky_constant_PROCESS_MODE_INCREMENTAL>]. Otherwise, this defaults to [PROCESS_MODE_QUALITY<class_Sky_constant_PROCESS_MODE_QUALITY>].



[ProcessMode<enum_Sky_ProcessMode>] **PROCESS_MODE_QUALITY** = `1`

Uses high quality importance sampling to process the radiance map. In general, this results in much higher quality than [PROCESS_MODE_REALTIME<class_Sky_constant_PROCESS_MODE_REALTIME>] but takes much longer to generate. This should not be used if you plan on changing the sky at runtime. If you are finding that the reflection is not blurry enough and is showing sparkles or fireflies, try increasing [ProjectSettings.rendering/reflections/sky_reflections/ggx_samples<class_ProjectSettings_property_rendering/reflections/sky_reflections/ggx_samples>].



[ProcessMode<enum_Sky_ProcessMode>] **PROCESS_MODE_INCREMENTAL** = `2`

Uses the same high quality importance sampling to process the radiance map as [PROCESS_MODE_QUALITY<class_Sky_constant_PROCESS_MODE_QUALITY>], but updates over several frames. The number of frames is determined by [ProjectSettings.rendering/reflections/sky_reflections/roughness_layers<class_ProjectSettings_property_rendering/reflections/sky_reflections/roughness_layers>]. Use this when you need highest quality radiance maps, but have a sky that updates slowly.



[ProcessMode<enum_Sky_ProcessMode>] **PROCESS_MODE_REALTIME** = `3`

Uses the fast filtering algorithm to process the radiance map. In general this results in lower quality, but substantially faster run times. If you need better quality, but still need to update the sky every frame, consider turning on [ProjectSettings.rendering/reflections/sky_reflections/fast_filter_high_quality<class_ProjectSettings_property_rendering/reflections/sky_reflections/fast_filter_high_quality>].

\ **Note:** The fast filtering algorithm is limited to 256×256 cubemaps, so [radiance_size<class_Sky_property_radiance_size>] must be set to [RADIANCE_SIZE_256<class_Sky_constant_RADIANCE_SIZE_256>]. Otherwise, a warning is printed and the overridden radiance size is ignored.


----


## Property Descriptions



[ProcessMode<enum_Sky_ProcessMode>] **process_mode** = `0` [🔗<class_Sky_property_process_mode>]


- |void| **set_process_mode**\ (\ value\: [ProcessMode<enum_Sky_ProcessMode>]\ )
- [ProcessMode<enum_Sky_ProcessMode>] **get_process_mode**\ (\ )

The method for generating the radiance map from the sky. The radiance map is a cubemap with increasingly blurry versions of the sky corresponding to different levels of roughness. Radiance maps can be expensive to calculate.


----



[RadianceSize<enum_Sky_RadianceSize>] **radiance_size** = `3` [🔗<class_Sky_property_radiance_size>]


- |void| **set_radiance_size**\ (\ value\: [RadianceSize<enum_Sky_RadianceSize>]\ )
- [RadianceSize<enum_Sky_RadianceSize>] **get_radiance_size**\ (\ )

The **Sky**'s radiance map size. The higher the radiance map size, the more detailed the lighting from the **Sky** will be.

\ **Note:** Some hardware will have trouble with higher radiance sizes, especially [RADIANCE_SIZE_512<class_Sky_constant_RADIANCE_SIZE_512>] and above. Only use such high values on high-end hardware.


----



[Material<class_Material>] **sky_material** [🔗<class_Sky_property_sky_material>]


- |void| **set_material**\ (\ value\: [Material<class_Material>]\ )
- [Material<class_Material>] **get_material**\ (\ )

[Material<class_Material>] used to draw the background. Can be [PanoramaSkyMaterial<class_PanoramaSkyMaterial>], [ProceduralSkyMaterial<class_ProceduralSkyMaterial>], [PhysicalSkyMaterial<class_PhysicalSkyMaterial>], or even a [ShaderMaterial<class_ShaderMaterial>] if you want to use your own custom shader.

