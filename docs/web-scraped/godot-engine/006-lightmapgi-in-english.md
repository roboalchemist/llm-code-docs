# LightmapGI in English

# LightmapGI

Inherits:VisualInstance3D<Node3D<Node<Object
Computes and stores baked lightmaps for fast global illumination.

## Description

TheLightmapGInode is used to compute and store baked lightmaps. Lightmaps are used to provide high-quality indirect lighting with very little light leaking.LightmapGIcan also provide rough reflections using spherical harmonics ifdirectionalis enabled. Dynamic objects can receive indirect lighting thanks tolight probes, which can be automatically placed by settinggenerate_probes_subdivto a value other thanGENERATE_PROBES_DISABLED. Additional lightmap probes can also be added by creatingLightmapProbenodes. The downside is that lightmaps are fully static and cannot be baked in an exported project. Baking aLightmapGInode is also slower compared toVoxelGI.
Procedural generation:Lightmap baking functionality is only available in the editor. This meansLightmapGIis not suited to procedurally generated or user-built levels. For procedurally generated or user-built levels, useVoxelGIor SDFGI instead (seeEnvironment.sdfgi_enabled).
Performance:LightmapGIprovides the best possible run-time performance for global illumination. It is suitable for low-end hardware including integrated graphics and mobile devices.
Note:Due to how lightmaps work, most properties only have a visible effect once lightmaps are baked again.
Note:Lightmap baking onCSGShape3Ds andPrimitiveMeshes is not supported, as these cannot store UV2 data required for baking.
Note:If no custom lightmappers are installed,LightmapGIcan only be baked from devices that support the Forward+ or Mobile renderers.
Note:TheLightmapGInode only bakes light data for child nodes of its parent. Nodes further up the hierarchy of the scene will not be baked.

## Tutorials

- Using Lightmap global illumination
Using Lightmap global illumination

## Properties

| float | bias | 0.0005 |
|---|---|---|
| float | bounce_indirect_energy | 1.0 |
| int | bounces | 3 |
| CameraAttributes | camera_attributes |  |
| int | denoiser_range | 10 |
| float | denoiser_strength | 0.1 |
| bool | directional | false |
| Color | environment_custom_color | Color(1,1,1,1) |
| float | environment_custom_energy | 1.0 |
| Sky | environment_custom_sky |  |
| EnvironmentMode | environment_mode | 1 |
| GenerateProbes | generate_probes_subdiv | 2 |
| bool | interior | false |
| LightmapGIData | light_data |  |
| int | max_texture_size | 16384 |
| BakeQuality | quality | 1 |
| ShadowmaskMode | shadowmask_mode | 0 |
| bool | supersampling | false |
| float | supersampling_factor | 2.0 |
| float | texel_scale | 1.0 |
| bool | use_denoiser | true |
| bool | use_texture_for_bounces | true |

float
bias
0.0005
float
bounce_indirect_energy
bounces
CameraAttributes
camera_attributes
denoiser_range
float
denoiser_strength
bool
directional
false
Color
environment_custom_color
Color(1,1,1,1)
float
environment_custom_energy
environment_custom_sky
EnvironmentMode
environment_mode
GenerateProbes
generate_probes_subdiv
bool
interior
false
LightmapGIData
light_data
max_texture_size
16384
BakeQuality
quality
ShadowmaskMode
shadowmask_mode
bool
supersampling
false
float
supersampling_factor
float
texel_scale
bool
use_denoiser
true
bool
use_texture_for_bounces
true

## Enumerations

enumBakeQuality:🔗
BakeQualityBAKE_QUALITY_LOW=0
Low bake quality (fastest bake times). The quality of this preset can be adjusted by changingProjectSettings.rendering/lightmapping/bake_quality/low_quality_ray_countandProjectSettings.rendering/lightmapping/bake_quality/low_quality_probe_ray_count.
BakeQualityBAKE_QUALITY_MEDIUM=1
Medium bake quality (fast bake times). The quality of this preset can be adjusted by changingProjectSettings.rendering/lightmapping/bake_quality/medium_quality_ray_countandProjectSettings.rendering/lightmapping/bake_quality/medium_quality_probe_ray_count.
BakeQualityBAKE_QUALITY_HIGH=2
High bake quality (slow bake times). The quality of this preset can be adjusted by changingProjectSettings.rendering/lightmapping/bake_quality/high_quality_ray_countandProjectSettings.rendering/lightmapping/bake_quality/high_quality_probe_ray_count.
BakeQualityBAKE_QUALITY_ULTRA=3
Highest bake quality (slowest bake times). The quality of this preset can be adjusted by changingProjectSettings.rendering/lightmapping/bake_quality/ultra_quality_ray_countandProjectSettings.rendering/lightmapping/bake_quality/ultra_quality_probe_ray_count.
enumGenerateProbes:🔗
GenerateProbesGENERATE_PROBES_DISABLED=0
Don't generate lightmap probes for lighting dynamic objects.
GenerateProbesGENERATE_PROBES_SUBDIV_4=1
Lowest level of subdivision (fastest bake times, smallest file sizes).
GenerateProbesGENERATE_PROBES_SUBDIV_8=2
Low level of subdivision (fast bake times, small file sizes).
GenerateProbesGENERATE_PROBES_SUBDIV_16=3
High level of subdivision (slow bake times, large file sizes).
GenerateProbesGENERATE_PROBES_SUBDIV_32=4
Highest level of subdivision (slowest bake times, largest file sizes).
enumBakeError:🔗
BakeErrorBAKE_ERROR_OK=0
Lightmap baking was successful.
BakeErrorBAKE_ERROR_NO_SCENE_ROOT=1
Lightmap baking failed because the root node for the edited scene could not be accessed.
BakeErrorBAKE_ERROR_FOREIGN_DATA=2
Lightmap baking failed as the lightmap data resource is embedded in a foreign resource.
BakeErrorBAKE_ERROR_NO_LIGHTMAPPER=3
Lightmap baking failed as there is no lightmapper available in this Godot build.
BakeErrorBAKE_ERROR_NO_SAVE_PATH=4
Lightmap baking failed as theLightmapGIDatasave path isn't configured in the resource.
BakeErrorBAKE_ERROR_NO_MESHES=5
Lightmap baking failed as there are no meshes whoseGeometryInstance3D.gi_modeisGeometryInstance3D.GI_MODE_STATICand with valid UV2 mapping in the current scene. You may need to select 3D scenes in the Import dock and change their global illumination mode accordingly.
BakeErrorBAKE_ERROR_MESHES_INVALID=6
Lightmap baking failed as the lightmapper failed to analyze some of the meshes marked as static for baking.
BakeErrorBAKE_ERROR_CANT_CREATE_IMAGE=7
Lightmap baking failed as the resulting image couldn't be saved or imported by Godot after it was saved.
BakeErrorBAKE_ERROR_USER_ABORTED=8
The user aborted the lightmap baking operation (typically by clicking theCancelbutton in the progress dialog).
BakeErrorBAKE_ERROR_TEXTURE_SIZE_TOO_SMALL=9
Lightmap baking failed as the maximum texture size is too small to fit some of the meshes marked for baking.
BakeErrorBAKE_ERROR_LIGHTMAP_TOO_SMALL=10
Lightmap baking failed as the lightmap is too small.
BakeErrorBAKE_ERROR_ATLAS_TOO_SMALL=11
Lightmap baking failed as the lightmap was unable to fit into an atlas.
enumEnvironmentMode:🔗
EnvironmentModeENVIRONMENT_MODE_DISABLED=0
Ignore environment lighting when baking lightmaps.
EnvironmentModeENVIRONMENT_MODE_SCENE=1
Use the scene's environment lighting when baking lightmaps.
Note:If baking lightmaps in a scene with noWorldEnvironmentnode, this will act likeENVIRONMENT_MODE_DISABLED. The editor's preview sky and sun isnottaken into account byLightmapGIwhen baking lightmaps.
EnvironmentModeENVIRONMENT_MODE_CUSTOM_SKY=2
Useenvironment_custom_skyas a source of environment lighting when baking lightmaps.
EnvironmentModeENVIRONMENT_MODE_CUSTOM_COLOR=3
Useenvironment_custom_colormultiplied byenvironment_custom_energyas a constant source of environment lighting when baking lightmaps.

## Property Descriptions

floatbias=0.0005🔗

- voidset_bias(value:float)
voidset_bias(value:float)
- floatget_bias()
floatget_bias()
The bias to use when computing shadows. Increasingbiascan fix shadow acne on the resulting baked lightmap, but can introduce peter-panning (shadows not connecting to their casters). Real-timeLight3Dshadows are not affected by thisbiasproperty.
floatbounce_indirect_energy=1.0🔗
- voidset_bounce_indirect_energy(value:float)
voidset_bounce_indirect_energy(value:float)
- floatget_bounce_indirect_energy()
floatget_bounce_indirect_energy()
The energy multiplier for each bounce. Higher values will make indirect lighting brighter. A value of1.0represents physically accurate behavior, but higher values can be used to make indirect lighting propagate more visibly when using a low number of bounces. This can be used to speed up bake times by lowering the number ofbouncesthen increasingbounce_indirect_energy.
Note:bounce_indirect_energyonly has an effect ifbouncesis set to a value greater than or equal to1.
intbounces=3🔗
- voidset_bounces(value:int)
voidset_bounces(value:int)
- intget_bounces()
intget_bounces()
Number of light bounces that are taken into account during baking. Higher values result in brighter, more realistic lighting, at the cost of longer bake times. If set to0, only environment lighting, direct light and emissive lighting is baked.
CameraAttributescamera_attributes🔗
- voidset_camera_attributes(value:CameraAttributes)
voidset_camera_attributes(value:CameraAttributes)
- CameraAttributesget_camera_attributes()
CameraAttributesget_camera_attributes()
TheCameraAttributesresource that specifies exposure levels to bake at. Auto-exposure and non exposure properties will be ignored. Exposure settings should be used to reduce the dynamic range present when baking. If exposure is too high, theLightmapGIwill have banding artifacts or may have over-exposure artifacts.
intdenoiser_range=10🔗
- voidset_denoiser_range(value:int)
voidset_denoiser_range(value:int)
- intget_denoiser_range()
intget_denoiser_range()
The distance in pixels from which the denoiser samples. Lower values preserve more details, but may give blotchy results if the lightmap quality is not high enough. Only effective ifuse_denoiseristrueandProjectSettings.rendering/lightmapping/denoising/denoiseris set to JNLM.
floatdenoiser_strength=0.1🔗
- voidset_denoiser_strength(value:float)
voidset_denoiser_strength(value:float)
- floatget_denoiser_strength()
floatget_denoiser_strength()
The strength of denoising step applied to the generated lightmaps. Only effective ifuse_denoiseristrueandProjectSettings.rendering/lightmapping/denoising/denoiseris set to JNLM.
booldirectional=false🔗
- voidset_directional(value:bool)
voidset_directional(value:bool)
- boolis_directional()
boolis_directional()
Iftrue, bakes lightmaps to contain directional information as spherical harmonics. This results in more realistic lighting appearance, especially with normal mapped materials and for lights that have their direct light baked (Light3D.light_bake_modeset toLight3D.BAKE_STATICand withLight3D.editor_onlyset tofalse). The directional information is also used to provide rough reflections for static and dynamic objects. This has a small run-time performance cost as the shader has to perform more work to interpret the direction information from the lightmap. Directional lightmaps also take longer to bake and result in larger file sizes.
Note:The property's name has no relationship withDirectionalLight3D.directionalworks with all light types.
Colorenvironment_custom_color=Color(1,1,1,1)🔗
- voidset_environment_custom_color(value:Color)
voidset_environment_custom_color(value:Color)
- Colorget_environment_custom_color()
Colorget_environment_custom_color()
The color to use for environment lighting. Only effective ifenvironment_modeisENVIRONMENT_MODE_CUSTOM_COLOR.
floatenvironment_custom_energy=1.0🔗
- voidset_environment_custom_energy(value:float)
voidset_environment_custom_energy(value:float)
- floatget_environment_custom_energy()
floatget_environment_custom_energy()
The color multiplier to use for environment lighting. Only effective ifenvironment_modeisENVIRONMENT_MODE_CUSTOM_COLOR.
Skyenvironment_custom_sky🔗
- voidset_environment_custom_sky(value:Sky)
voidset_environment_custom_sky(value:Sky)
- Skyget_environment_custom_sky()
Skyget_environment_custom_sky()
The sky to use as a source of environment lighting. Only effective ifenvironment_modeisENVIRONMENT_MODE_CUSTOM_SKY.
EnvironmentModeenvironment_mode=1🔗
- voidset_environment_mode(value:EnvironmentMode)
voidset_environment_mode(value:EnvironmentMode)
- EnvironmentModeget_environment_mode()
EnvironmentModeget_environment_mode()
The environment mode to use when baking lightmaps.
GenerateProbesgenerate_probes_subdiv=2🔗
- voidset_generate_probes(value:GenerateProbes)
voidset_generate_probes(value:GenerateProbes)
- GenerateProbesget_generate_probes()
GenerateProbesget_generate_probes()
The level of subdivision to use when automatically generatingLightmapProbes for dynamic object lighting. Higher values result in more accurate indirect lighting on dynamic objects, at the cost of longer bake times and larger file sizes.
Note:Automatically generatedLightmapProbes are not visible as nodes in the Scene tree dock, and cannot be modified this way after they are generated.
Note:Regardless ofgenerate_probes_subdiv, direct lighting on dynamic objects is always applied usingLight3Dnodes in real-time.
boolinterior=false🔗
- voidset_interior(value:bool)
voidset_interior(value:bool)
- boolis_interior()
boolis_interior()
Iftrue, ignore environment lighting when baking lightmaps.
LightmapGIDatalight_data🔗
- voidset_light_data(value:LightmapGIData)
voidset_light_data(value:LightmapGIData)
- LightmapGIDataget_light_data()
LightmapGIDataget_light_data()
TheLightmapGIDataassociated to thisLightmapGInode. This resource is automatically created after baking, and is not meant to be created manually.
intmax_texture_size=16384🔗
- voidset_max_texture_size(value:int)
voidset_max_texture_size(value:int)
- intget_max_texture_size()
intget_max_texture_size()
The maximum texture size for the generated texture atlas. Higher values will result in fewer slices being generated, but may not work on all hardware as a result of hardware limitations on texture sizes. Leavemax_texture_sizeat its default value of16384if unsure.
BakeQualityquality=1🔗
- voidset_bake_quality(value:BakeQuality)
voidset_bake_quality(value:BakeQuality)
- BakeQualityget_bake_quality()
BakeQualityget_bake_quality()
The quality preset to use when baking lightmaps. This affects bake times, but output file sizes remain mostly identical across quality levels.
To further speed up bake times, decreasebounces, disableuse_denoiserand/or decreasetexel_scale.
To further increase quality, enablesupersamplingand/or increasetexel_scale.
ShadowmaskModeshadowmask_mode=0🔗
- voidset_shadowmask_mode(value:ShadowmaskMode)
voidset_shadowmask_mode(value:ShadowmaskMode)
- ShadowmaskModeget_shadowmask_mode()
ShadowmaskModeget_shadowmask_mode()
Experimental:This property may be changed or removed in future versions.
The shadowmasking policy to use for directional shadows on static objects that are baked with thisLightmapGIinstance.
Shadowmasking allowsDirectionalLight3Dnodes to cast shadows even outside the range defined by theirDirectionalLight3D.directional_shadow_max_distanceproperty. This is done by baking a texture that contains a shadowmap for the directional light, then using this texture according to the current shadowmask mode.
Note:The shadowmask texture is only created ifshadowmask_modeis notLightmapGIData.SHADOWMASK_MODE_NONE. To see a difference, you need to bake lightmaps again after switching fromLightmapGIData.SHADOWMASK_MODE_NONEto any other mode.
boolsupersampling=false🔗
- voidset_supersampling_enabled(value:bool)
voidset_supersampling_enabled(value:bool)
- boolis_supersampling_enabled()
boolis_supersampling_enabled()
Iftrue, lightmaps are baked with the texel scale multiplied withsupersampling_factorand downsampled before saving the lightmap (so the effective texel density is identical to having supersampling disabled).
Supersampling provides increased lightmap quality with less noise, smoother shadows and better shadowing of small-scale features in objects. However, it may result in significantly increased bake times and memory usage while baking lightmaps. Padding is automatically adjusted to avoid increasing light leaking.
floatsupersampling_factor=2.0🔗
- voidset_supersampling_factor(value:float)
voidset_supersampling_factor(value:float)
- floatget_supersampling_factor()
floatget_supersampling_factor()
The factor by which the texel density is multiplied for supersampling. For best results, use an integer value. While fractional values are allowed, they can result in increased light leaking and a blurry lightmap.
Higher values may result in better quality, but also increase bake times and memory usage while baking.
Seesupersamplingfor more information.
floattexel_scale=1.0🔗
- voidset_texel_scale(value:float)
voidset_texel_scale(value:float)
- floatget_texel_scale()
floatget_texel_scale()
Scales the lightmap texel density of all meshes for the current bake. This is a multiplier that builds upon the existing lightmap texel size defined in each imported 3D scene, along with the per-mesh density multiplier (which is designed to be used when the same mesh is used at different scales). Lower values will result in faster bake times.
For example, doublingtexel_scaledoubles the lightmap texture resolution for all objectson each axis, so it willquadruplethe texel count.
booluse_denoiser=true🔗
- voidset_use_denoiser(value:bool)
voidset_use_denoiser(value:bool)
- boolis_using_denoiser()
boolis_using_denoiser()
Iftrue, uses a GPU-based denoising algorithm on the generated lightmap. This eliminates most noise within the generated lightmap at the cost of longer bake times. File sizes are generally not impacted significantly by the use of a denoiser, although lossless compression may do a better job at compressing a denoised image.
booluse_texture_for_bounces=true🔗
- voidset_use_texture_for_bounces(value:bool)
voidset_use_texture_for_bounces(value:bool)
- boolis_using_texture_for_bounces()
boolis_using_texture_for_bounces()
Iftrue, a texture with the lighting information will be generated to speed up the generation of indirect lighting at the cost of some accuracy. The geometry might exhibit extra light leak artifacts when using low resolution lightmaps or UVs that stretch the lightmap significantly across surfaces. Leaveuse_texture_for_bouncesat its default value oftrueif unsure.
Note:use_texture_for_bouncesonly has an effect ifbouncesis set to a value greater than or equal to1.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
