# BaseMaterial3D in English

# BaseMaterial3D

Inherits:Material<Resource<RefCounted<Object
Inherited By:ORMMaterial3D,StandardMaterial3D
Abstract base class for defining the 3D rendering properties of meshes.

## Description

This class serves as a default material with a wide variety of rendering features and properties without the need to write shader code. See the tutorial below for details.

## Tutorials

- Standard Material 3D and ORM Material 3D
Standard Material 3D and ORM Material 3D

## Properties

| Color | albedo_color | Color(1,1,1,1) |
|---|---|---|
| Texture2D | albedo_texture |  |
| bool | albedo_texture_force_srgb | false |
| bool | albedo_texture_msdf | false |
| float | alpha_antialiasing_edge |  |
| AlphaAntiAliasing | alpha_antialiasing_mode |  |
| float | alpha_hash_scale |  |
| float | alpha_scissor_threshold |  |
| float | anisotropy | 0.0 |
| bool | anisotropy_enabled | false |
| Texture2D | anisotropy_flowmap |  |
| bool | ao_enabled | false |
| float | ao_light_affect | 0.0 |
| bool | ao_on_uv2 | false |
| Texture2D | ao_texture |  |
| TextureChannel | ao_texture_channel | 0 |
| Color | backlight | Color(0,0,0,1) |
| bool | backlight_enabled | false |
| Texture2D | backlight_texture |  |
| bool | bent_normal_enabled | false |
| Texture2D | bent_normal_texture |  |
| bool | billboard_keep_scale | false |
| BillboardMode | billboard_mode | 0 |
| BlendMode | blend_mode | 0 |
| float | clearcoat | 1.0 |
| bool | clearcoat_enabled | false |
| float | clearcoat_roughness | 0.5 |
| Texture2D | clearcoat_texture |  |
| CullMode | cull_mode | 0 |
| DepthDrawMode | depth_draw_mode | 0 |
| DepthTest | depth_test | 0 |
| Texture2D | detail_albedo |  |
| BlendMode | detail_blend_mode | 0 |
| bool | detail_enabled | false |
| Texture2D | detail_mask |  |
| Texture2D | detail_normal |  |
| DetailUV | detail_uv_layer | 0 |
| DiffuseMode | diffuse_mode | 0 |
| bool | disable_ambient_light | false |
| bool | disable_fog | false |
| bool | disable_receive_shadows | false |
| bool | disable_specular_occlusion | false |
| float | distance_fade_max_distance | 10.0 |
| float | distance_fade_min_distance | 0.0 |
| DistanceFadeMode | distance_fade_mode | 0 |
| Color | emission | Color(0,0,0,1) |
| bool | emission_enabled | false |
| float | emission_energy_multiplier | 1.0 |
| float | emission_intensity |  |
| bool | emission_on_uv2 | false |
| EmissionOperator | emission_operator | 0 |
| Texture2D | emission_texture |  |
| bool | fixed_size | false |
| float | fov_override | 75.0 |
| bool | grow | false |
| float | grow_amount | 0.0 |
| bool | heightmap_deep_parallax | false |
| bool | heightmap_enabled | false |
| bool | heightmap_flip_binormal | false |
| bool | heightmap_flip_tangent | false |
| bool | heightmap_flip_texture | false |
| int | heightmap_max_layers |  |
| int | heightmap_min_layers |  |
| float | heightmap_scale | 5.0 |
| Texture2D | heightmap_texture |  |
| float | metallic | 0.0 |
| float | metallic_specular | 0.5 |
| Texture2D | metallic_texture |  |
| TextureChannel | metallic_texture_channel | 0 |
| float | msdf_outline_size | 0.0 |
| float | msdf_pixel_range | 4.0 |
| bool | no_depth_test | false |
| bool | normal_enabled | false |
| float | normal_scale | 1.0 |
| Texture2D | normal_texture |  |
| Texture2D | orm_texture |  |
| int | particles_anim_h_frames |  |
| bool | particles_anim_loop |  |
| int | particles_anim_v_frames |  |
| float | point_size | 1.0 |
| float | proximity_fade_distance | 1.0 |
| bool | proximity_fade_enabled | false |
| bool | refraction_enabled | false |
| float | refraction_scale | 0.05 |
| Texture2D | refraction_texture |  |
| TextureChannel | refraction_texture_channel | 0 |
| float | rim | 1.0 |
| bool | rim_enabled | false |
| Texture2D | rim_texture |  |
| float | rim_tint | 0.5 |
| float | roughness | 1.0 |
| Texture2D | roughness_texture |  |
| TextureChannel | roughness_texture_channel | 0 |
| ShadingMode | shading_mode | 1 |
| bool | shadow_to_opacity | false |
| SpecularMode | specular_mode | 0 |
| Color | stencil_color | Color(0,0,0,1) |
| StencilCompare | stencil_compare | 0 |
| int | stencil_flags | 0 |
| StencilMode | stencil_mode | 0 |
| float | stencil_outline_thickness | 0.01 |
| int | stencil_reference | 1 |
| bool | subsurf_scatter_enabled | false |
| bool | subsurf_scatter_skin_mode | false |
| float | subsurf_scatter_strength | 0.0 |
| Texture2D | subsurf_scatter_texture |  |
| float | subsurf_scatter_transmittance_boost | 0.0 |
| Color | subsurf_scatter_transmittance_color | Color(1,1,1,1) |
| float | subsurf_scatter_transmittance_depth | 0.1 |
| bool | subsurf_scatter_transmittance_enabled | false |
| Texture2D | subsurf_scatter_transmittance_texture |  |
| TextureFilter | texture_filter | 3 |
| bool | texture_repeat | true |
| Transparency | transparency | 0 |
| bool | use_fov_override | false |
| bool | use_particle_trails | false |
| bool | use_point_size | false |
| bool | use_z_clip_scale | false |
| Vector3 | uv1_offset | Vector3(0,0,0) |
| Vector3 | uv1_scale | Vector3(1,1,1) |
| bool | uv1_triplanar | false |
| float | uv1_triplanar_sharpness | 1.0 |
| bool | uv1_world_triplanar | false |
| Vector3 | uv2_offset | Vector3(0,0,0) |
| Vector3 | uv2_scale | Vector3(1,1,1) |
| bool | uv2_triplanar | false |
| float | uv2_triplanar_sharpness | 1.0 |
| bool | uv2_world_triplanar | false |
| bool | vertex_color_is_srgb | false |
| bool | vertex_color_use_as_albedo | false |
| float | z_clip_scale | 1.0 |

Color
albedo_color
Color(1,1,1,1)
Texture2D
albedo_texture
bool
albedo_texture_force_srgb
false
bool
albedo_texture_msdf
false
float
alpha_antialiasing_edge
AlphaAntiAliasing
alpha_antialiasing_mode
float
alpha_hash_scale
float
alpha_scissor_threshold
float
anisotropy
bool
anisotropy_enabled
false
Texture2D
anisotropy_flowmap
bool
ao_enabled
false
float
ao_light_affect
bool
ao_on_uv2
false
Texture2D
ao_texture
TextureChannel
ao_texture_channel
Color
backlight
Color(0,0,0,1)
bool
backlight_enabled
false
Texture2D
backlight_texture
bool
bent_normal_enabled
false
Texture2D
bent_normal_texture
bool
billboard_keep_scale
false
BillboardMode
billboard_mode
BlendMode
blend_mode
float
clearcoat
bool
clearcoat_enabled
false
float
clearcoat_roughness
Texture2D
clearcoat_texture
CullMode
cull_mode
DepthDrawMode
depth_draw_mode
DepthTest
depth_test
Texture2D
detail_albedo
BlendMode
detail_blend_mode
bool
detail_enabled
false
Texture2D
detail_mask
Texture2D
detail_normal
DetailUV
detail_uv_layer
DiffuseMode
diffuse_mode
bool
disable_ambient_light
false
bool
disable_fog
false
bool
disable_receive_shadows
false
bool
disable_specular_occlusion
false
float
distance_fade_max_distance
10.0
float
distance_fade_min_distance
DistanceFadeMode
distance_fade_mode
Color
emission
Color(0,0,0,1)
bool
emission_enabled
false
float
emission_energy_multiplier
float
emission_intensity
bool
emission_on_uv2
false
EmissionOperator
emission_operator
Texture2D
emission_texture
bool
fixed_size
false
float
fov_override
75.0
bool
grow
false
float
grow_amount
bool
heightmap_deep_parallax
false
bool
heightmap_enabled
false
bool
heightmap_flip_binormal
false
bool
heightmap_flip_tangent
false
bool
heightmap_flip_texture
false
heightmap_max_layers
heightmap_min_layers
float
heightmap_scale
Texture2D
heightmap_texture
float
metallic
float
metallic_specular
Texture2D
metallic_texture
TextureChannel
metallic_texture_channel
float
msdf_outline_size
float
msdf_pixel_range
bool
no_depth_test
false
bool
normal_enabled
false
float
normal_scale
Texture2D
normal_texture
Texture2D
orm_texture
particles_anim_h_frames
bool
particles_anim_loop
particles_anim_v_frames
float
point_size
float
proximity_fade_distance
bool
proximity_fade_enabled
false
bool
refraction_enabled
false
float
refraction_scale
0.05
Texture2D
refraction_texture
TextureChannel
refraction_texture_channel
float
bool
rim_enabled
false
Texture2D
rim_texture
float
rim_tint
float
roughness
Texture2D
roughness_texture
TextureChannel
roughness_texture_channel
ShadingMode
shading_mode
bool
shadow_to_opacity
false
SpecularMode
specular_mode
Color
stencil_color
Color(0,0,0,1)
StencilCompare
stencil_compare
stencil_flags
StencilMode
stencil_mode
float
stencil_outline_thickness
0.01
stencil_reference
bool
subsurf_scatter_enabled
false
bool
subsurf_scatter_skin_mode
false
float
subsurf_scatter_strength
Texture2D
subsurf_scatter_texture
float
subsurf_scatter_transmittance_boost
Color
subsurf_scatter_transmittance_color
Color(1,1,1,1)
float
subsurf_scatter_transmittance_depth
bool
subsurf_scatter_transmittance_enabled
false
Texture2D
subsurf_scatter_transmittance_texture
TextureFilter
texture_filter
bool
texture_repeat
true
Transparency
transparency
bool
use_fov_override
false
bool
use_particle_trails
false
bool
use_point_size
false
bool
use_z_clip_scale
false
Vector3
uv1_offset
Vector3(0,0,0)
Vector3
uv1_scale
Vector3(1,1,1)
bool
uv1_triplanar
false
float
uv1_triplanar_sharpness
bool
uv1_world_triplanar
false
Vector3
uv2_offset
Vector3(0,0,0)
Vector3
uv2_scale
Vector3(1,1,1)
bool
uv2_triplanar
false
float
uv2_triplanar_sharpness
bool
uv2_world_triplanar
false
bool
vertex_color_is_srgb
false
bool
vertex_color_use_as_albedo
false
float
z_clip_scale

## Methods

| bool | get_feature(feature:Feature)const |
|---|---|
| bool | get_flag(flag:Flags)const |
| Texture2D | get_texture(param:TextureParam)const |
| void | set_feature(feature:Feature, enable:bool) |
| void | set_flag(flag:Flags, enable:bool) |
| void | set_texture(param:TextureParam, texture:Texture2D) |

bool
get_feature(feature:Feature)const
bool
get_flag(flag:Flags)const
Texture2D
get_texture(param:TextureParam)const
void
set_feature(feature:Feature, enable:bool)
void
set_flag(flag:Flags, enable:bool)
void
set_texture(param:TextureParam, texture:Texture2D)

## Enumerations

enumTextureParam:🔗
TextureParamTEXTURE_ALBEDO=0
Texture specifying per-pixel color.
TextureParamTEXTURE_METALLIC=1
Texture specifying per-pixel metallic value.
TextureParamTEXTURE_ROUGHNESS=2
Texture specifying per-pixel roughness value.
TextureParamTEXTURE_EMISSION=3
Texture specifying per-pixel emission color.
TextureParamTEXTURE_NORMAL=4
Texture specifying per-pixel normal vector.
TextureParamTEXTURE_BENT_NORMAL=18
Texture specifying per-pixel bent normal vector.
TextureParamTEXTURE_RIM=5
Texture specifying per-pixel rim value.
TextureParamTEXTURE_CLEARCOAT=6
Texture specifying per-pixel clearcoat value.
TextureParamTEXTURE_FLOWMAP=7
Texture specifying per-pixel flowmap direction for use withanisotropy.
TextureParamTEXTURE_AMBIENT_OCCLUSION=8
Texture specifying per-pixel ambient occlusion value.
TextureParamTEXTURE_HEIGHTMAP=9
Texture specifying per-pixel height.
TextureParamTEXTURE_SUBSURFACE_SCATTERING=10
Texture specifying per-pixel subsurface scattering.
TextureParamTEXTURE_SUBSURFACE_TRANSMITTANCE=11
Texture specifying per-pixel transmittance for subsurface scattering.
TextureParamTEXTURE_BACKLIGHT=12
Texture specifying per-pixel backlight color.
TextureParamTEXTURE_REFRACTION=13
Texture specifying per-pixel refraction strength.
TextureParamTEXTURE_DETAIL_MASK=14
Texture specifying per-pixel detail mask blending value.
TextureParamTEXTURE_DETAIL_ALBEDO=15
Texture specifying per-pixel detail color.
TextureParamTEXTURE_DETAIL_NORMAL=16
Texture specifying per-pixel detail normal.
TextureParamTEXTURE_ORM=17
Texture holding ambient occlusion, roughness, and metallic.
TextureParamTEXTURE_MAX=19
Represents the size of theTextureParamenum.
enumTextureFilter:🔗
TextureFilterTEXTURE_FILTER_NEAREST=0
The texture filter reads from the nearest pixel only. This makes the texture look pixelated from up close, and grainy from a distance (due to mipmaps not being sampled).
TextureFilterTEXTURE_FILTER_LINEAR=1
The texture filter blends between the nearest 4 pixels. This makes the texture look smooth from up close, and grainy from a distance (due to mipmaps not being sampled).
TextureFilterTEXTURE_FILTER_NEAREST_WITH_MIPMAPS=2
The texture filter reads from the nearest pixel and blends between the nearest 2 mipmaps (or uses the nearest mipmap ifProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filteristrue). This makes the texture look pixelated from up close, and smooth from a distance.
TextureFilterTEXTURE_FILTER_LINEAR_WITH_MIPMAPS=3
The texture filter blends between the nearest 4 pixels and between the nearest 2 mipmaps (or uses the nearest mipmap ifProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filteristrue). This makes the texture look smooth from up close, and smooth from a distance.
TextureFilterTEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC=4
The texture filter reads from the nearest pixel and blends between 2 mipmaps (or uses the nearest mipmap ifProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filteristrue) based on the angle between the surface and the camera view. This makes the texture look pixelated from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjustingProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.
TextureFilterTEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC=5
The texture filter blends between the nearest 4 pixels and blends between 2 mipmaps (or uses the nearest mipmap ifProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filteristrue) based on the angle between the surface and the camera view. This makes the texture look smooth from up close, and smooth from a distance. Anisotropic filtering improves texture quality on surfaces that are almost in line with the camera, but is slightly slower. The anisotropic filtering level can be changed by adjustingProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level.
TextureFilterTEXTURE_FILTER_MAX=6
Represents the size of theTextureFilterenum.
enumDetailUV:🔗
DetailUVDETAIL_UV_1=0
UseUVwith the detail texture.
DetailUVDETAIL_UV_2=1
UseUV2with the detail texture.
enumTransparency:🔗
TransparencyTRANSPARENCY_DISABLED=0
The material will not use transparency. This is the fastest to render.
TransparencyTRANSPARENCY_ALPHA=1
The material will use the texture's alpha values for transparency. This is the slowest to render, and disables shadow casting.
TransparencyTRANSPARENCY_ALPHA_SCISSOR=2
The material will cut off all values below a threshold, the rest will remain opaque. The opaque portions will be rendered in the depth prepass. This is faster to render than alpha blending, but slower than opaque rendering. This also supports casting shadows.
TransparencyTRANSPARENCY_ALPHA_HASH=3
The material will cut off all values below a spatially-deterministic threshold, the rest will remain opaque. This is faster to render than alpha blending, but slower than opaque rendering. This also supports casting shadows. Alpha hashing is suited for hair rendering.
TransparencyTRANSPARENCY_ALPHA_DEPTH_PRE_PASS=4
The material will use the texture's alpha value for transparency, but will discard fragments with an alpha of less than 0.99 during the depth prepass and fragments with an alpha less than 0.1 during the shadow pass. This also supports casting shadows.
TransparencyTRANSPARENCY_MAX=5
Represents the size of theTransparencyenum.
enumShadingMode:🔗
ShadingModeSHADING_MODE_UNSHADED=0
The object will not receive shadows. This is the fastest to render, but it disables all interactions with lights.
ShadingModeSHADING_MODE_PER_PIXEL=1
The object will be shaded per pixel. Useful for realistic shading effects.
ShadingModeSHADING_MODE_PER_VERTEX=2
The object will be shaded per vertex. Useful when you want cheaper shaders and do not care about visual quality.
ShadingModeSHADING_MODE_MAX=3
Represents the size of theShadingModeenum.
enumFeature:🔗
FeatureFEATURE_EMISSION=0
Constant for settingemission_enabled.
FeatureFEATURE_NORMAL_MAPPING=1
Constant for settingnormal_enabled.
FeatureFEATURE_RIM=2
Constant for settingrim_enabled.
FeatureFEATURE_CLEARCOAT=3
Constant for settingclearcoat_enabled.
FeatureFEATURE_ANISOTROPY=4
Constant for settinganisotropy_enabled.
FeatureFEATURE_AMBIENT_OCCLUSION=5
Constant for settingao_enabled.
FeatureFEATURE_HEIGHT_MAPPING=6
Constant for settingheightmap_enabled.
FeatureFEATURE_SUBSURFACE_SCATTERING=7
Constant for settingsubsurf_scatter_enabled.
FeatureFEATURE_SUBSURFACE_TRANSMITTANCE=8
Constant for settingsubsurf_scatter_transmittance_enabled.
FeatureFEATURE_BACKLIGHT=9
Constant for settingbacklight_enabled.
FeatureFEATURE_REFRACTION=10
Constant for settingrefraction_enabled.
FeatureFEATURE_DETAIL=11
Constant for settingdetail_enabled.
FeatureFEATURE_BENT_NORMAL_MAPPING=12
Constant for settingbent_normal_enabled.
FeatureFEATURE_MAX=13
Represents the size of theFeatureenum.
enumBlendMode:🔗
BlendModeBLEND_MODE_MIX=0
Default blend mode. The color of the object is blended over the background based on the object's alpha value.
BlendModeBLEND_MODE_ADD=1
The color of the object is added to the background.
BlendModeBLEND_MODE_SUB=2
The color of the object is subtracted from the background.
BlendModeBLEND_MODE_MUL=3
The color of the object is multiplied by the background.
BlendModeBLEND_MODE_PREMULT_ALPHA=4
The color of the object is added to the background and the alpha channel is used to mask out the background. This is effectively a hybrid of the blend mix and add modes, useful for effects like fire where you want the flame to add but the smoke to mix. By default, this works with unshaded materials using premultiplied textures. For shaded materials, use thePREMUL_ALPHA_FACTORbuilt-in so that lighting can be modulated as well.
enumAlphaAntiAliasing:🔗
AlphaAntiAliasingALPHA_ANTIALIASING_OFF=0
Disables Alpha AntiAliasing for the material.
AlphaAntiAliasingALPHA_ANTIALIASING_ALPHA_TO_COVERAGE=1
Enables AlphaToCoverage. Alpha values in the material are passed to the AntiAliasing sample mask.
AlphaAntiAliasingALPHA_ANTIALIASING_ALPHA_TO_COVERAGE_AND_TO_ONE=2
Enables AlphaToCoverage and forces all non-zero alpha values to1. Alpha values in the material are passed to the AntiAliasing sample mask.
enumDepthDrawMode:🔗
DepthDrawModeDEPTH_DRAW_OPAQUE_ONLY=0
Default depth draw mode. Depth is drawn only for opaque objects during the opaque prepass (if any) and during the opaque pass.
DepthDrawModeDEPTH_DRAW_ALWAYS=1
Objects will write to depth during the opaque and the transparent passes. Transparent objects that are close to the camera may obscure other transparent objects behind them.
Note:This does not influence whether transparent objects are included in the depth prepass or not. For that, seeTransparency.
DepthDrawModeDEPTH_DRAW_DISABLED=2
Objects will not write their depth to the depth buffer, even during the depth prepass (if enabled).
enumDepthTest:🔗
DepthTestDEPTH_TEST_DEFAULT=0
Depth test will discard the pixel if it is behind other pixels.
DepthTestDEPTH_TEST_INVERTED=1
Depth test will discard the pixel if it is in front of other pixels. Useful for stencil effects.
enumCullMode:🔗
CullModeCULL_BACK=0
Default cull mode. The back of the object is culled when not visible. Back face triangles will be culled when facing the camera. This results in only the front side of triangles being drawn. For closed-surface meshes, this means that only the exterior of the mesh will be visible.
CullModeCULL_FRONT=1
Front face triangles will be culled when facing the camera. This results in only the back side of triangles being drawn. For closed-surface meshes, this means that the interior of the mesh will be drawn instead of the exterior.
CullModeCULL_DISABLED=2
No face culling is performed; both the front face and back face will be visible.
enumFlags:🔗
FlagsFLAG_DISABLE_DEPTH_TEST=0
Disables the depth test, so this object is drawn on top of all others drawn before it. This puts the object in the transparent draw pass where it is sorted based on distance to camera. Objects drawn after it in the draw order may cover it. This also disables writing to depth.
FlagsFLAG_ALBEDO_FROM_VERTEX_COLOR=1
SetALBEDOto the per-vertex color specified in the mesh.
FlagsFLAG_SRGB_VERTEX_COLOR=2
Vertex colors are considered to be stored in nonlinear sRGB encoding and are converted to linear encoding during rendering. See alsovertex_color_is_srgb.
Note:Only effective when using the Forward+ and Mobile rendering methods.
FlagsFLAG_USE_POINT_SIZE=3
Uses point size to alter the size of primitive points. Also changes the albedo texture lookup to usePOINT_COORDinstead ofUV.
FlagsFLAG_FIXED_SIZE=4
Object is scaled by depth so that it always appears the same size on screen.
FlagsFLAG_BILLBOARD_KEEP_SCALE=5
Shader will keep the scale set for the mesh. Otherwise the scale is lost when billboarding. Only applies whenbillboard_modeisBILLBOARD_ENABLED.
FlagsFLAG_UV1_USE_TRIPLANAR=6
Use triplanar texture lookup for all texture lookups that would normally useUV.
FlagsFLAG_UV2_USE_TRIPLANAR=7
Use triplanar texture lookup for all texture lookups that would normally useUV2.
FlagsFLAG_UV1_USE_WORLD_TRIPLANAR=8
Use triplanar texture lookup for all texture lookups that would normally useUV.
FlagsFLAG_UV2_USE_WORLD_TRIPLANAR=9
Use triplanar texture lookup for all texture lookups that would normally useUV2.
FlagsFLAG_AO_ON_UV2=10
UseUV2coordinates to look up from theao_texture.
FlagsFLAG_EMISSION_ON_UV2=11
UseUV2coordinates to look up from theemission_texture.
FlagsFLAG_ALBEDO_TEXTURE_FORCE_SRGB=12
Forces the shader to convert albedo from nonlinear sRGB encoding to linear encoding. See alsoalbedo_texture_force_srgb.
FlagsFLAG_DONT_RECEIVE_SHADOWS=13
Disables receiving shadows from other objects.
FlagsFLAG_DISABLE_AMBIENT_LIGHT=14
Disables receiving ambient light.
FlagsFLAG_USE_SHADOW_TO_OPACITY=15
Enables the shadow to opacity feature.
FlagsFLAG_USE_TEXTURE_REPEAT=16
Enables the texture to repeat when UV coordinates are outside the 0-1 range. If using one of the linear filtering modes, this can result in artifacts at the edges of a texture when the sampler filters across the edges of the texture.
FlagsFLAG_INVERT_HEIGHTMAP=17
Invert values read from a depth texture to convert them to height values (heightmap).
FlagsFLAG_SUBSURFACE_MODE_SKIN=18
Enables the skin mode for subsurface scattering which is used to improve the look of subsurface scattering when used for human skin.
FlagsFLAG_PARTICLE_TRAILS_MODE=19
Enables parts of the shader required forGPUParticles3Dtrails to function. This also requires using a mesh with appropriate skinning, such asRibbonTrailMeshorTubeTrailMesh. Enabling this feature outside of materials used inGPUParticles3Dmeshes will break material rendering.
FlagsFLAG_ALBEDO_TEXTURE_MSDF=20
Enables multichannel signed distance field rendering shader.
FlagsFLAG_DISABLE_FOG=21
Disables receiving depth-based or volumetric fog.
FlagsFLAG_DISABLE_SPECULAR_OCCLUSION=22
Disables specular occlusion.
FlagsFLAG_USE_Z_CLIP_SCALE=23
Enables usingz_clip_scale.
FlagsFLAG_USE_FOV_OVERRIDE=24
Enables usingfov_override.
FlagsFLAG_MAX=25
Represents the size of theFlagsenum.
enumDiffuseMode:🔗
DiffuseModeDIFFUSE_BURLEY=0
Default diffuse scattering algorithm.
DiffuseModeDIFFUSE_LAMBERT=1
Diffuse scattering ignores roughness.
DiffuseModeDIFFUSE_LAMBERT_WRAP=2
Extends Lambert to cover more than 90 degrees when roughness increases.
DiffuseModeDIFFUSE_TOON=3
Uses a hard cut for lighting, with smoothing affected by roughness.
enumSpecularMode:🔗
SpecularModeSPECULAR_SCHLICK_GGX=0
Default specular blob.
Note:Forward+ uses multiscattering for more accurate reflections, although the impact of multiscattering is more noticeable on rough metallic surfaces than on smooth, non-metallic surfaces.
Note:Mobile and Compatibility don't perform multiscattering for performance reasons. Instead, they perform single scattering, which means rough metallic surfaces may look slightly darker than intended.
SpecularModeSPECULAR_TOON=1
Toon blob which changes size based on roughness.
SpecularModeSPECULAR_DISABLED=2
No specular blob. This is slightly faster to render than other specular modes.
enumBillboardMode:🔗
BillboardModeBILLBOARD_DISABLED=0
Billboard mode is disabled.
BillboardModeBILLBOARD_ENABLED=1
The object's Z axis will always face the camera.
BillboardModeBILLBOARD_FIXED_Y=2
The object's X axis will always face the camera.
BillboardModeBILLBOARD_PARTICLES=3
Used for particle systems when assigned toGPUParticles3DandCPUParticles3Dnodes (flipbook animation). Enablesparticles_anim_*properties.
TheParticleProcessMaterial.anim_speed_minorCPUParticles3D.anim_speed_minshould also be set to a value bigger than zero for the animation to play.
enumTextureChannel:🔗
TextureChannelTEXTURE_CHANNEL_RED=0
Used to read from the red channel of a texture.
TextureChannelTEXTURE_CHANNEL_GREEN=1
Used to read from the green channel of a texture.
TextureChannelTEXTURE_CHANNEL_BLUE=2
Used to read from the blue channel of a texture.
TextureChannelTEXTURE_CHANNEL_ALPHA=3
Used to read from the alpha channel of a texture.
TextureChannelTEXTURE_CHANNEL_GRAYSCALE=4
Used to read from the linear (non-perceptual) average of the red, green and blue channels of a texture.
enumEmissionOperator:🔗
EmissionOperatorEMISSION_OP_ADD=0
Adds the emission color to the color from the emission texture.
EmissionOperatorEMISSION_OP_MULTIPLY=1
Multiplies the emission color by the color from the emission texture.
enumDistanceFadeMode:🔗
DistanceFadeModeDISTANCE_FADE_DISABLED=0
Do not use distance fade.
DistanceFadeModeDISTANCE_FADE_PIXEL_ALPHA=1
Smoothly fades the object out based on each pixel's distance from the camera using the alpha channel.
DistanceFadeModeDISTANCE_FADE_PIXEL_DITHER=2
Smoothly fades the object out based on each pixel's distance from the camera using a dithering approach. Dithering discards pixels based on a set pattern to smoothly fade without enabling transparency. On certain hardware, this can be faster thanDISTANCE_FADE_PIXEL_ALPHA.
DistanceFadeModeDISTANCE_FADE_OBJECT_DITHER=3
Smoothly fades the object out based on the object's distance from the camera using a dithering approach. Dithering discards pixels based on a set pattern to smoothly fade without enabling transparency. On certain hardware, this can be faster thanDISTANCE_FADE_PIXEL_ALPHAandDISTANCE_FADE_PIXEL_DITHER.
enumStencilMode:🔗
StencilModeSTENCIL_MODE_DISABLED=0
Disables stencil operations.
StencilModeSTENCIL_MODE_OUTLINE=1
Stencil preset which applies an outline to the object.
Note:Requires aMaterial.next_passmaterial which will be automatically applied. Any manual changes made toMaterial.next_passwill be lost when the stencil properties are modified or the scene is reloaded. To safely apply aMaterial.next_passmaterial on a material that uses stencil presets, useGeometryInstance3D.material_overlayinstead.
StencilModeSTENCIL_MODE_XRAY=2
Stencil preset which shows a silhouette of the object behind walls.
Note:Requires aMaterial.next_passmaterial which will be automatically applied. Any manual changes made toMaterial.next_passwill be lost when the stencil properties are modified or the scene is reloaded. To safely apply aMaterial.next_passmaterial on a material that uses stencil presets, useGeometryInstance3D.material_overlayinstead.
StencilModeSTENCIL_MODE_CUSTOM=3
Enables stencil operations without a preset.
enumStencilFlags:🔗
StencilFlagsSTENCIL_FLAG_READ=1
The material will only be rendered where it passes a stencil comparison with existing stencil buffer values.
StencilFlagsSTENCIL_FLAG_WRITE=2
The material will write the reference value to the stencil buffer where it passes the depth test.
StencilFlagsSTENCIL_FLAG_WRITE_DEPTH_FAIL=4
The material will write the reference value to the stencil buffer where it fails the depth test.
enumStencilCompare:🔗
StencilCompareSTENCIL_COMPARE_ALWAYS=0
Always passes the stencil test.
StencilCompareSTENCIL_COMPARE_LESS=1
Passes the stencil test when the reference value is less than the existing stencil value.
StencilCompareSTENCIL_COMPARE_EQUAL=2
Passes the stencil test when the reference value is equal to the existing stencil value.
StencilCompareSTENCIL_COMPARE_LESS_OR_EQUAL=3
Passes the stencil test when the reference value is less than or equal to the existing stencil value.
StencilCompareSTENCIL_COMPARE_GREATER=4
Passes the stencil test when the reference value is greater than the existing stencil value.
StencilCompareSTENCIL_COMPARE_NOT_EQUAL=5
Passes the stencil test when the reference value is not equal to the existing stencil value.
StencilCompareSTENCIL_COMPARE_GREATER_OR_EQUAL=6
Passes the stencil test when the reference value is greater than or equal to the existing stencil value.

## Property Descriptions

Coloralbedo_color=Color(1,1,1,1)🔗

- voidset_albedo(value:Color)
voidset_albedo(value:Color)
- Colorget_albedo()
Colorget_albedo()
The material's base color.
Note:Ifdetail_enabledistrueand adetail_albedotexture is specified,albedo_colorwillnotmodulate the detail texture. This can be used to color partial areas of a material by not specifying an albedo texture and using a transparentdetail_albedotexture instead.
Texture2Dalbedo_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture to multiply byalbedo_color. Used for basic texturing of objects.
If the texture appears unexpectedly too dark or too bright, checkalbedo_texture_force_srgb.
boolalbedo_texture_force_srgb=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, forces a conversion of thealbedo_texturefrom nonlinear sRGB encoding to linear encoding. See alsovertex_color_is_srgb.
This should only be enabled when needed (typically when using aViewportTextureasalbedo_texture). Ifalbedo_texture_force_srgbistruewhen it shouldn't be, the texture will appear to be too dark. Ifalbedo_texture_force_srgbisfalsewhen it shouldn't be, the texture will appear to be too bright.
boolalbedo_texture_msdf=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Enables multichannel signed distance field rendering shader. Usemsdf_pixel_rangeandmsdf_outline_sizeto configure MSDF parameters.
floatalpha_antialiasing_edge🔗
- voidset_alpha_antialiasing_edge(value:float)
voidset_alpha_antialiasing_edge(value:float)
- floatget_alpha_antialiasing_edge()
floatget_alpha_antialiasing_edge()
Threshold at which antialiasing will be applied on the alpha channel.
AlphaAntiAliasingalpha_antialiasing_mode🔗
- voidset_alpha_antialiasing(value:AlphaAntiAliasing)
voidset_alpha_antialiasing(value:AlphaAntiAliasing)
- AlphaAntiAliasingget_alpha_antialiasing()
AlphaAntiAliasingget_alpha_antialiasing()
The type of alpha antialiasing to apply.
floatalpha_hash_scale🔗
- voidset_alpha_hash_scale(value:float)
voidset_alpha_hash_scale(value:float)
- floatget_alpha_hash_scale()
floatget_alpha_hash_scale()
The hashing scale for Alpha Hash. Recommended values between0and2.
floatalpha_scissor_threshold🔗
- voidset_alpha_scissor_threshold(value:float)
voidset_alpha_scissor_threshold(value:float)
- floatget_alpha_scissor_threshold()
floatget_alpha_scissor_threshold()
Threshold at which the alpha scissor will discard values. Higher values will result in more pixels being discarded. If the material becomes too opaque at a distance, try increasingalpha_scissor_threshold. If the material disappears at a distance, try decreasingalpha_scissor_threshold.
floatanisotropy=0.0🔗
- voidset_anisotropy(value:float)
voidset_anisotropy(value:float)
- floatget_anisotropy()
floatget_anisotropy()
The strength of the anisotropy effect. This is multiplied byanisotropy_flowmap's alpha channel if a texture is defined there and the texture contains an alpha channel.
boolanisotropy_enabled=false🔗
- voidset_feature(feature:Feature, enable:bool)
voidset_feature(feature:Feature, enable:bool)
- boolget_feature(feature:Feature)const
boolget_feature(feature:Feature)const
Iftrue, anisotropy is enabled. Anisotropy changes the shape of the specular blob and aligns it to tangent space. This is useful for brushed aluminum and hair reflections.
Note:Mesh tangents are needed for anisotropy to work. If the mesh does not contain tangents, the anisotropy effect will appear broken.
Note:Material anisotropy should not to be confused with anisotropic texture filtering, which can be enabled by settingtexture_filtertoTEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC.
Texture2Danisotropy_flowmap🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture that offsets the tangent map for anisotropy calculations and optionally controls the anisotropy effect (if an alpha channel is present). The flowmap texture is expected to be a derivative map, with the red channel representing distortion on the X axis and green channel representing distortion on the Y axis. Values below 0.5 will result in negative distortion, whereas values above 0.5 will result in positive distortion.
If present, the texture's alpha channel will be used to multiply the strength of theanisotropyeffect. Fully opaque pixels will keep the anisotropy effect's original strength while fully transparent pixels will disable the anisotropy effect entirely. The flowmap texture's blue channel is ignored.
boolao_enabled=false🔗
- voidset_feature(feature:Feature, enable:bool)
voidset_feature(feature:Feature, enable:bool)
- boolget_feature(feature:Feature)const
boolget_feature(feature:Feature)const
Iftrue, ambient occlusion is enabled. Ambient occlusion darkens areas based on theao_texture.
floatao_light_affect=0.0🔗
- voidset_ao_light_affect(value:float)
voidset_ao_light_affect(value:float)
- floatget_ao_light_affect()
floatget_ao_light_affect()
Amount that ambient occlusion affects lighting from lights. If0, ambient occlusion only affects ambient light. If1, ambient occlusion affects lights just as much as it affects ambient light. This can be used to impact the strength of the ambient occlusion effect, but typically looks unrealistic.
boolao_on_uv2=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, useUV2coordinates to look up from theao_texture.
Texture2Dao_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture that defines the amount of ambient occlusion for a given point on the object.
TextureChannelao_texture_channel=0🔗
- voidset_ao_texture_channel(value:TextureChannel)
voidset_ao_texture_channel(value:TextureChannel)
- TextureChannelget_ao_texture_channel()
TextureChannelget_ao_texture_channel()
Specifies the channel of theao_texturein which the ambient occlusion information is stored. This is useful when you store the information for multiple effects in a single texture. For example if you stored metallic in the red channel, roughness in the blue, and ambient occlusion in the green you could reduce the number of textures you use.
Colorbacklight=Color(0,0,0,1)🔗
- voidset_backlight(value:Color)
voidset_backlight(value:Color)
- Colorget_backlight()
Colorget_backlight()
The color used by the backlight effect. Represents the light passing through an object.
boolbacklight_enabled=false🔗
- voidset_feature(feature:Feature, enable:bool)
voidset_feature(feature:Feature, enable:bool)
- boolget_feature(feature:Feature)const
boolget_feature(feature:Feature)const
Iftrue, the backlight effect is enabled. See alsosubsurf_scatter_transmittance_enabled.
Texture2Dbacklight_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture used to control the backlight effect per-pixel. Added tobacklight.
boolbent_normal_enabled=false🔗
- voidset_feature(feature:Feature, enable:bool)
voidset_feature(feature:Feature, enable:bool)
- boolget_feature(feature:Feature)const
boolget_feature(feature:Feature)const
Iftrue, the bent normal map is enabled. This allows for more accurate indirect lighting and specular occlusion.
Texture2Dbent_normal_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture that specifies the average direction of incoming ambient light at a given pixel. Thebent_normal_textureonly uses the red and green channels; the blue and alpha channels are ignored. The normal read frombent_normal_textureis oriented around the surface normal provided by theMesh.
Note:A bent normal map is different from a regular normal map. When baking a bent normal map make sure to usea cosine distributionfor the bent normal map to work correctly.
Note:The mesh must have both normals and tangents defined in its vertex data. Otherwise, the shading produced by the bent normal map will not look correct. If creating geometry withSurfaceTool, you can useSurfaceTool.generate_normals()andSurfaceTool.generate_tangents()to automatically generate normals and tangents respectively.
Note:Godot expects the bent normal map to use X+, Y+, and Z+ coordinates. Seethis pagefor a comparison of normal map coordinates expected by popular engines.
boolbillboard_keep_scale=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, the shader will keep the scale set for the mesh. Otherwise, the scale is lost when billboarding. Only applies whenbillboard_modeis notBILLBOARD_DISABLED.
BillboardModebillboard_mode=0🔗
- voidset_billboard_mode(value:BillboardMode)
voidset_billboard_mode(value:BillboardMode)
- BillboardModeget_billboard_mode()
BillboardModeget_billboard_mode()
Controls how the object faces the camera.
Note:Billboard mode is not suitable for VR because the left-right vector of the camera is not horizontal when the screen is attached to your head instead of on the table. SeeGitHub issue #41567for details.
BlendModeblend_mode=0🔗
- voidset_blend_mode(value:BlendMode)
voidset_blend_mode(value:BlendMode)
- BlendModeget_blend_mode()
BlendModeget_blend_mode()
The material's blend mode.
Note:Values other thanMixforce the object into the transparent pipeline.
floatclearcoat=1.0🔗
- voidset_clearcoat(value:float)
voidset_clearcoat(value:float)
- floatget_clearcoat()
floatget_clearcoat()
Sets the strength of the clearcoat effect. Setting to0looks the same as disabling the clearcoat effect.
boolclearcoat_enabled=false🔗
- voidset_feature(feature:Feature, enable:bool)
voidset_feature(feature:Feature, enable:bool)
- boolget_feature(feature:Feature)const
boolget_feature(feature:Feature)const
Iftrue, clearcoat rendering is enabled. Adds a secondary transparent pass to the lighting calculation resulting in an added specular blob. This makes materials appear as if they have a clear layer on them that can be either glossy or rough.
Note:Clearcoat rendering is not visible if the material'sshading_modeisSHADING_MODE_UNSHADED.
floatclearcoat_roughness=0.5🔗
- voidset_clearcoat_roughness(value:float)
voidset_clearcoat_roughness(value:float)
- floatget_clearcoat_roughness()
floatget_clearcoat_roughness()
Sets the roughness of the clearcoat pass. A higher value results in a rougher clearcoat while a lower value results in a smoother clearcoat.
Texture2Dclearcoat_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture that defines the strength of the clearcoat effect and the glossiness of the clearcoat. Strength is specified in the red channel while glossiness is specified in the green channel.
CullModecull_mode=0🔗
- voidset_cull_mode(value:CullMode)
voidset_cull_mode(value:CullMode)
- CullModeget_cull_mode()
CullModeget_cull_mode()
Determines which side of the triangle to cull depending on whether the triangle faces towards or away from the camera.
DepthDrawModedepth_draw_mode=0🔗
- voidset_depth_draw_mode(value:DepthDrawMode)
voidset_depth_draw_mode(value:DepthDrawMode)
- DepthDrawModeget_depth_draw_mode()
DepthDrawModeget_depth_draw_mode()
Determines when depth rendering takes place. See alsotransparency.
DepthTestdepth_test=0🔗
- voidset_depth_test(value:DepthTest)
voidset_depth_test(value:DepthTest)
- DepthTestget_depth_test()
DepthTestget_depth_test()
Experimental:May be affected by future rendering pipeline changes.
Determines which comparison operator is used when testing depth.
Note:Changingdepth_testto a non-default value only has a visible effect when used on a transparent material, or a material that hasdepth_draw_modeset toDEPTH_DRAW_DISABLED.
Texture2Ddetail_albedo🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture that specifies the color of the detail overlay.detail_albedo's alpha channel is used as a mask, even when the material is opaque. To use a dedicated texture as a mask, seedetail_mask.
Note:detail_albedoisnotmodulated byalbedo_color.
BlendModedetail_blend_mode=0🔗
- voidset_detail_blend_mode(value:BlendMode)
voidset_detail_blend_mode(value:BlendMode)
- BlendModeget_detail_blend_mode()
BlendModeget_detail_blend_mode()
Specifies how thedetail_albedoshould blend with the currentALBEDO.
booldetail_enabled=false🔗
- voidset_feature(feature:Feature, enable:bool)
voidset_feature(feature:Feature, enable:bool)
- boolget_feature(feature:Feature)const
boolget_feature(feature:Feature)const
Iftrue, enables the detail overlay. Detail is a second texture that gets mixed over the surface of the object based ondetail_maskanddetail_albedo's alpha channel. This can be used to add variation to objects, or to blend between two different albedo/normal textures.
Texture2Ddetail_mask🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture used to specify how the detail textures get blended with the base textures.detail_maskcan be used together withdetail_albedo's alpha channel (if any).
Texture2Ddetail_normal🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture that specifies the per-pixel normal of the detail overlay. Thedetail_normaltexture only uses the red and green channels; the blue and alpha channels are ignored. The normal read fromdetail_normalis oriented around the surface normal provided by theMesh.
Note:Godot expects the normal map to use X+, Y+, and Z+ coordinates. Seethis pagefor a comparison of normal map coordinates expected by popular engines.
DetailUVdetail_uv_layer=0🔗
- voidset_detail_uv(value:DetailUV)
voidset_detail_uv(value:DetailUV)
- DetailUVget_detail_uv()
DetailUVget_detail_uv()
Specifies whether to useUVorUV2for the detail layer.
DiffuseModediffuse_mode=0🔗
- voidset_diffuse_mode(value:DiffuseMode)
voidset_diffuse_mode(value:DiffuseMode)
- DiffuseModeget_diffuse_mode()
DiffuseModeget_diffuse_mode()
The algorithm used for diffuse light scattering.
booldisable_ambient_light=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, the object receives no ambient light.
booldisable_fog=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, the object will not be affected by fog (neither volumetric nor depth fog). This is useful for unshaded or transparent materials (e.g. particles), which without this setting will be affected even if fully transparent.
booldisable_receive_shadows=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, the object receives no shadow that would otherwise be cast onto it.
booldisable_specular_occlusion=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, disables specular occlusion even ifProjectSettings.rendering/reflections/specular_occlusion/enabledisfalse.
floatdistance_fade_max_distance=10.0🔗
- voidset_distance_fade_max_distance(value:float)
voidset_distance_fade_max_distance(value:float)
- floatget_distance_fade_max_distance()
floatget_distance_fade_max_distance()
Distance at which the object appears fully opaque.
Note:Ifdistance_fade_max_distanceis less thandistance_fade_min_distance, the behavior will be reversed. The object will start to fade away atdistance_fade_max_distanceand will fully disappear once it reachesdistance_fade_min_distance.
floatdistance_fade_min_distance=0.0🔗
- voidset_distance_fade_min_distance(value:float)
voidset_distance_fade_min_distance(value:float)
- floatget_distance_fade_min_distance()
floatget_distance_fade_min_distance()
Distance at which the object starts to become visible. If the object is less than this distance away, it will be invisible.
Note:Ifdistance_fade_min_distanceis greater thandistance_fade_max_distance, the behavior will be reversed. The object will start to fade away atdistance_fade_max_distanceand will fully disappear once it reachesdistance_fade_min_distance.
DistanceFadeModedistance_fade_mode=0🔗
- voidset_distance_fade(value:DistanceFadeMode)
voidset_distance_fade(value:DistanceFadeMode)
- DistanceFadeModeget_distance_fade()
DistanceFadeModeget_distance_fade()
Specifies which type of fade to use. Can be any of theDistanceFadeModes.
Coloremission=Color(0,0,0,1)🔗
- voidset_emission(value:Color)
voidset_emission(value:Color)
- Colorget_emission()
Colorget_emission()
The emitted light's color. Seeemission_enabled.
boolemission_enabled=false🔗
- voidset_feature(feature:Feature, enable:bool)
voidset_feature(feature:Feature, enable:bool)
- boolget_feature(feature:Feature)const
boolget_feature(feature:Feature)const
Iftrue, the body emits light. Emitting light makes the object appear brighter. The object can also cast light on other objects if aVoxelGI, SDFGI, orLightmapGIis used and this object is used in baked lighting.
floatemission_energy_multiplier=1.0🔗
- voidset_emission_energy_multiplier(value:float)
voidset_emission_energy_multiplier(value:float)
- floatget_emission_energy_multiplier()
floatget_emission_energy_multiplier()
Multiplier for emitted light. Seeemission_enabled.
floatemission_intensity🔗
- voidset_emission_intensity(value:float)
voidset_emission_intensity(value:float)
- floatget_emission_intensity()
floatget_emission_intensity()
Luminance of emitted light, measured in nits (candela per square meter). Only available whenProjectSettings.rendering/lights_and_shadows/use_physical_light_unitsis enabled. The default is roughly equivalent to an indoor lightbulb.
boolemission_on_uv2=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
UseUV2to read from theemission_texture.
EmissionOperatoremission_operator=0🔗
- voidset_emission_operator(value:EmissionOperator)
voidset_emission_operator(value:EmissionOperator)
- EmissionOperatorget_emission_operator()
EmissionOperatorget_emission_operator()
Sets howemissioninteracts withemission_texture. Can either add or multiply.
Texture2Demission_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture that specifies how much surface emits light at a given point.
boolfixed_size=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, the object is rendered at the same size regardless of distance. The object's size on screen is the same as if the camera was1.0units away from the object's origin, regardless of the actual distance from the camera. TheCamera3D's field of view (orCamera3D.sizewhen in orthogonal/frustum mode) still affects the size the object is drawn at.
floatfov_override=75.0🔗
- voidset_fov_override(value:float)
voidset_fov_override(value:float)
- floatget_fov_override()
floatget_fov_override()
Overrides theCamera3D's field of view angle (in degrees).
Note:This behaves as if the field of view is set on aCamera3DwithCamera3D.keep_aspectset toCamera3D.KEEP_HEIGHT. Additionally, it may not look correct on a non-perspective camera where the field of view setting is ignored.
boolgrow=false🔗
- voidset_grow_enabled(value:bool)
voidset_grow_enabled(value:bool)
- boolis_grow_enabled()
boolis_grow_enabled()
Iftrue, enables the vertex grow setting. This can be used to create mesh-based outlines using a second material pass and itscull_modeset toCULL_FRONT. See alsogrow_amount.
Note:Vertex growth cannot create new vertices, which means that visible gaps may occur in sharp corners. This can be alleviated by designing the mesh to use smooth normals exclusively usingface weighted normalsin the 3D authoring software. In this case, grow will be able to join every outline together, just like in the original mesh.
floatgrow_amount=0.0🔗
- voidset_grow(value:float)
voidset_grow(value:float)
- floatget_grow()
floatget_grow()
Grows object vertices in the direction of their normals. Only effective ifgrowistrue.
boolheightmap_deep_parallax=false🔗
- voidset_heightmap_deep_parallax(value:bool)
voidset_heightmap_deep_parallax(value:bool)
- boolis_heightmap_deep_parallax_enabled()
boolis_heightmap_deep_parallax_enabled()
Iftrue, uses parallax occlusion mapping to represent depth in the material instead of simple offset mapping (seeheightmap_enabled). This results in a more convincing depth effect, but is much more expensive on the GPU. Only enable this on materials where it makes a significant visual difference.
boolheightmap_enabled=false🔗
- voidset_feature(feature:Feature, enable:bool)
voidset_feature(feature:Feature, enable:bool)
- boolget_feature(feature:Feature)const
boolget_feature(feature:Feature)const
Iftrue, height mapping is enabled (also called "parallax mapping" or "depth mapping"). See alsonormal_enabled. Height mapping is a demanding feature on the GPU, so it should only be used on materials where it makes a significant visual difference.
Note:Height mapping is not supported if triplanar mapping is used on the same material. The value ofheightmap_enabledwill be ignored ifuv1_triplanaris enabled.
boolheightmap_flip_binormal=false🔗
- voidset_heightmap_deep_parallax_flip_binormal(value:bool)
voidset_heightmap_deep_parallax_flip_binormal(value:bool)
- boolget_heightmap_deep_parallax_flip_binormal()
boolget_heightmap_deep_parallax_flip_binormal()
Iftrue, flips the mesh's binormal vectors when interpreting the height map. If the heightmap effect looks strange when the camera moves (even with a reasonableheightmap_scale), try setting this totrue.
boolheightmap_flip_tangent=false🔗
- voidset_heightmap_deep_parallax_flip_tangent(value:bool)
voidset_heightmap_deep_parallax_flip_tangent(value:bool)
- boolget_heightmap_deep_parallax_flip_tangent()
boolget_heightmap_deep_parallax_flip_tangent()
Iftrue, flips the mesh's tangent vectors when interpreting the height map. If the heightmap effect looks strange when the camera moves (even with a reasonableheightmap_scale), try setting this totrue.
boolheightmap_flip_texture=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, interprets the height map texture as a depth map, with brighter values appearing to be "lower" in altitude compared to darker values.
This can be enabled for compatibility with some materials authored for Godot 3.x. This is not necessary if the Invert import option was used to invert the depth map in Godot 3.x, in which caseheightmap_flip_textureshould remainfalse.
intheightmap_max_layers🔗
- voidset_heightmap_deep_parallax_max_layers(value:int)
voidset_heightmap_deep_parallax_max_layers(value:int)
- intget_heightmap_deep_parallax_max_layers()
intget_heightmap_deep_parallax_max_layers()
The number of layers to use for parallax occlusion mapping when the camera is up close to the material. Higher values result in a more convincing depth effect, especially in materials that have steep height changes. Higher values have a significant cost on the GPU, so it should only be increased on materials where it makes a significant visual difference.
Note:Only effective ifheightmap_deep_parallaxistrue.
intheightmap_min_layers🔗
- voidset_heightmap_deep_parallax_min_layers(value:int)
voidset_heightmap_deep_parallax_min_layers(value:int)
- intget_heightmap_deep_parallax_min_layers()
intget_heightmap_deep_parallax_min_layers()
The number of layers to use for parallax occlusion mapping when the camera is far away from the material. Higher values result in a more convincing depth effect, especially in materials that have steep height changes. Higher values have a significant cost on the GPU, so it should only be increased on materials where it makes a significant visual difference.
Note:Only effective ifheightmap_deep_parallaxistrue.
floatheightmap_scale=5.0🔗
- voidset_heightmap_scale(value:float)
voidset_heightmap_scale(value:float)
- floatget_heightmap_scale()
floatget_heightmap_scale()
The heightmap scale to use for the parallax effect (seeheightmap_enabled). The default value is tuned so that the highest point (value = 255) appears to be 5 cm higher than the lowest point (value = 0). Higher values result in a deeper appearance, but may result in artifacts appearing when looking at the material from oblique angles, especially when the camera moves. Negative values can be used to invert the parallax effect, but this is different from inverting the texture usingheightmap_flip_textureas the material will also appear to be "closer" to the camera. In most cases,heightmap_scaleshould be kept to a positive value.
Note:If the height map effect looks strange regardless of this value, try adjustingheightmap_flip_binormalandheightmap_flip_tangent. See alsoheightmap_texturefor recommendations on authoring heightmap textures, as the way the heightmap texture is authored affects howheightmap_scalebehaves.
Texture2Dheightmap_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
The texture to use as a height map. See alsoheightmap_enabled.
For best results, the texture should be normalized (withheightmap_scalereduced to compensate). InGIMP, this can be done usingColors > Auto > Equalize. If the texture only uses a small part of its available range, the parallax effect may look strange, especially when the camera moves.
Note:To reduce memory usage and improve loading times, you may be able to use a lower-resolution heightmap texture as most heightmaps are only comprised of low-frequency data.
floatmetallic=0.0🔗
- voidset_metallic(value:float)
voidset_metallic(value:float)
- floatget_metallic()
floatget_metallic()
A high value makes the material appear more like a metal. Non-metals use their albedo as the diffuse color and add diffuse to the specular reflection. With non-metals, the reflection appears on top of the albedo color. Metals use their albedo as a multiplier to the specular reflection and set the diffuse color to black resulting in a tinted reflection. Materials work better when fully metal or fully non-metal, values between0and1should only be used for blending between metal and non-metal sections. To alter the amount of reflection useroughness.
floatmetallic_specular=0.5🔗
- voidset_specular(value:float)
voidset_specular(value:float)
- floatget_specular()
floatget_specular()
Adjusts the strength of specular reflections. Specular reflections are composed of scene reflections and the specular lobe which is the bright spot that is reflected from light sources. When set to0.0, no specular reflections will be visible. This differs from theSPECULAR_DISABLEDSpecularModeasSPECULAR_DISABLEDonly applies to the specular lobe from the light source.
Note:Unlikemetallic, this is not energy-conserving, so it should be left at0.5in most cases. See alsoroughness.
Texture2Dmetallic_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture used to specify metallic for an object. This is multiplied bymetallic.
TextureChannelmetallic_texture_channel=0🔗
- voidset_metallic_texture_channel(value:TextureChannel)
voidset_metallic_texture_channel(value:TextureChannel)
- TextureChannelget_metallic_texture_channel()
TextureChannelget_metallic_texture_channel()
Specifies the channel of themetallic_texturein which the metallic information is stored. This is useful when you store the information for multiple effects in a single texture. For example if you stored metallic in the red channel, roughness in the blue, and ambient occlusion in the green you could reduce the number of textures you use.
floatmsdf_outline_size=0.0🔗
- voidset_msdf_outline_size(value:float)
voidset_msdf_outline_size(value:float)
- floatget_msdf_outline_size()
floatget_msdf_outline_size()
The width of the shape outline.
floatmsdf_pixel_range=4.0🔗
- voidset_msdf_pixel_range(value:float)
voidset_msdf_pixel_range(value:float)
- floatget_msdf_pixel_range()
floatget_msdf_pixel_range()
The width of the range around the shape between the minimum and maximum representable signed distance.
boolno_depth_test=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, depth testing is disabled and the object will be drawn in render order.
boolnormal_enabled=false🔗
- voidset_feature(feature:Feature, enable:bool)
voidset_feature(feature:Feature, enable:bool)
- boolget_feature(feature:Feature)const
boolget_feature(feature:Feature)const
Iftrue, normal mapping is enabled. This has a slight performance cost, especially on mobile GPUs.
floatnormal_scale=1.0🔗
- voidset_normal_scale(value:float)
voidset_normal_scale(value:float)
- floatget_normal_scale()
floatget_normal_scale()
The strength of the normal map's effect.
Texture2Dnormal_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture used to specify the normal at a given pixel. Thenormal_textureonly uses the red and green channels; the blue and alpha channels are ignored. The normal read fromnormal_textureis oriented around the surface normal provided by theMesh.
Note:The mesh must have both normals and tangents defined in its vertex data. Otherwise, the normal map won't render correctly and will only appear to darken the whole surface. If creating geometry withSurfaceTool, you can useSurfaceTool.generate_normals()andSurfaceTool.generate_tangents()to automatically generate normals and tangents respectively.
Note:Godot expects the normal map to use X+, Y+, and Z+ coordinates. Seethis pagefor a comparison of normal map coordinates expected by popular engines.
Note:Ifdetail_enabledistrue, thedetail_albedotexture is drawnbelowthenormal_texture. To display a normal mapabovethedetail_albedotexture, usedetail_normalinstead.
Texture2Dorm_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
The Occlusion/Roughness/Metallic texture to use. This is a more efficient replacement ofao_texture,roughness_textureandmetallic_textureinORMMaterial3D. Ambient occlusion is stored in the red channel. Roughness map is stored in the green channel. Metallic map is stored in the blue channel. The alpha channel is ignored.
intparticles_anim_h_frames🔗
- voidset_particles_anim_h_frames(value:int)
voidset_particles_anim_h_frames(value:int)
- intget_particles_anim_h_frames()
intget_particles_anim_h_frames()
The number of horizontal frames in the particle sprite sheet. Only enabled when usingBILLBOARD_PARTICLES. Seebillboard_mode.
boolparticles_anim_loop🔗
- voidset_particles_anim_loop(value:bool)
voidset_particles_anim_loop(value:bool)
- boolget_particles_anim_loop()
boolget_particles_anim_loop()
Iftrue, particle animations are looped. Only enabled when usingBILLBOARD_PARTICLES. Seebillboard_mode.
intparticles_anim_v_frames🔗
- voidset_particles_anim_v_frames(value:int)
voidset_particles_anim_v_frames(value:int)
- intget_particles_anim_v_frames()
intget_particles_anim_v_frames()
The number of vertical frames in the particle sprite sheet. Only enabled when usingBILLBOARD_PARTICLES. Seebillboard_mode.
floatpoint_size=1.0🔗
- voidset_point_size(value:float)
voidset_point_size(value:float)
- floatget_point_size()
floatget_point_size()
The point size in pixels. Seeuse_point_size.
floatproximity_fade_distance=1.0🔗
- voidset_proximity_fade_distance(value:float)
voidset_proximity_fade_distance(value:float)
- floatget_proximity_fade_distance()
floatget_proximity_fade_distance()
Distance over which the fade effect takes place. The larger the distance the longer it takes for an object to fade.
boolproximity_fade_enabled=false🔗
- voidset_proximity_fade_enabled(value:bool)
voidset_proximity_fade_enabled(value:bool)
- boolis_proximity_fade_enabled()
boolis_proximity_fade_enabled()
Iftrue, the proximity fade effect is enabled. The proximity fade effect fades out each pixel based on its distance to another object.
boolrefraction_enabled=false🔗
- voidset_feature(feature:Feature, enable:bool)
voidset_feature(feature:Feature, enable:bool)
- boolget_feature(feature:Feature)const
boolget_feature(feature:Feature)const
Iftrue, the refraction effect is enabled. Distorts transparency based on light from behind the object.
Note:Refraction is implemented using the screen texture. Only opaque materials will appear in the refraction, since transparent materials do not appear in the screen texture.
floatrefraction_scale=0.05🔗
- voidset_refraction(value:float)
voidset_refraction(value:float)
- floatget_refraction()
floatget_refraction()
The strength of the refraction effect.
Texture2Drefraction_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture that controls the strength of the refraction per-pixel. Multiplied byrefraction_scale.
TextureChannelrefraction_texture_channel=0🔗
- voidset_refraction_texture_channel(value:TextureChannel)
voidset_refraction_texture_channel(value:TextureChannel)
- TextureChannelget_refraction_texture_channel()
TextureChannelget_refraction_texture_channel()
Specifies the channel of therefraction_texturein which the refraction information is stored. This is useful when you store the information for multiple effects in a single texture. For example if you stored refraction in the red channel, roughness in the blue, and ambient occlusion in the green you could reduce the number of textures you use.
floatrim=1.0🔗
- voidset_rim(value:float)
voidset_rim(value:float)
- floatget_rim()
floatget_rim()
Sets the strength of the rim lighting effect.
boolrim_enabled=false🔗
- voidset_feature(feature:Feature, enable:bool)
voidset_feature(feature:Feature, enable:bool)
- boolget_feature(feature:Feature)const
boolget_feature(feature:Feature)const
Iftrue, rim effect is enabled. Rim lighting increases the brightness at glancing angles on an object.
Note:Rim lighting is not visible if the material'sshading_modeisSHADING_MODE_UNSHADED.
Texture2Drim_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture used to set the strength of the rim lighting effect per-pixel. Multiplied byrim.
floatrim_tint=0.5🔗
- voidset_rim_tint(value:float)
voidset_rim_tint(value:float)
- floatget_rim_tint()
floatget_rim_tint()
The amount of to blend light and albedo color when rendering rim effect. If0the light color is used, while1means albedo color is used. An intermediate value generally works best.
floatroughness=1.0🔗
- voidset_roughness(value:float)
voidset_roughness(value:float)
- floatget_roughness()
floatget_roughness()
Surface reflection. A value of0represents a perfect mirror while a value of1completely blurs the reflection. See alsometallic.
Texture2Droughness_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture used to control the roughness per-pixel. Multiplied byroughness.
TextureChannelroughness_texture_channel=0🔗
- voidset_roughness_texture_channel(value:TextureChannel)
voidset_roughness_texture_channel(value:TextureChannel)
- TextureChannelget_roughness_texture_channel()
TextureChannelget_roughness_texture_channel()
Specifies the channel of theroughness_texturein which the roughness information is stored. This is useful when you store the information for multiple effects in a single texture. For example if you stored metallic in the red channel, roughness in the blue, and ambient occlusion in the green you could reduce the number of textures you use.
ShadingModeshading_mode=1🔗
- voidset_shading_mode(value:ShadingMode)
voidset_shading_mode(value:ShadingMode)
- ShadingModeget_shading_mode()
ShadingModeget_shading_mode()
Sets whether the shading takes place, per-pixel, per-vertex or unshaded. Per-vertex lighting is faster, making it the best choice for mobile applications, however it looks considerably worse than per-pixel. Unshaded rendering is the fastest, but disables all interactions with lights.
boolshadow_to_opacity=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, enables the "shadow to opacity" render mode where lighting modifies the alpha so shadowed areas are opaque and non-shadowed areas are transparent. Useful for overlaying shadows onto a camera feed in AR.
SpecularModespecular_mode=0🔗
- voidset_specular_mode(value:SpecularMode)
voidset_specular_mode(value:SpecularMode)
- SpecularModeget_specular_mode()
SpecularModeget_specular_mode()
The method for rendering the specular blob.
Note:specular_modeonly applies to the specular blob. It does not affect specular reflections from the sky, screen-space reflections,VoxelGI, SDFGI orReflectionProbes. To disable reflections from these sources as well, setmetallic_specularto0.0instead.
Colorstencil_color=Color(0,0,0,1)🔗
- voidset_stencil_effect_color(value:Color)
voidset_stencil_effect_color(value:Color)
- Colorget_stencil_effect_color()
Colorget_stencil_effect_color()
Experimental:May be affected by future rendering pipeline changes.
The primary color of the stencil effect.
StencilComparestencil_compare=0🔗
- voidset_stencil_compare(value:StencilCompare)
voidset_stencil_compare(value:StencilCompare)
- StencilCompareget_stencil_compare()
StencilCompareget_stencil_compare()
Experimental:May be affected by future rendering pipeline changes.
The comparison operator to use for stencil masking operations.
intstencil_flags=0🔗
- voidset_stencil_flags(value:int)
voidset_stencil_flags(value:int)
- intget_stencil_flags()
intget_stencil_flags()
Experimental:May be affected by future rendering pipeline changes.
The flags dictating how the stencil operation behaves.
StencilModestencil_mode=0🔗
- voidset_stencil_mode(value:StencilMode)
voidset_stencil_mode(value:StencilMode)
- StencilModeget_stencil_mode()
StencilModeget_stencil_mode()
Experimental:May be affected by future rendering pipeline changes.
The stencil effect mode.
floatstencil_outline_thickness=0.01🔗
- voidset_stencil_effect_outline_thickness(value:float)
voidset_stencil_effect_outline_thickness(value:float)
- floatget_stencil_effect_outline_thickness()
floatget_stencil_effect_outline_thickness()
Experimental:May be affected by future rendering pipeline changes.
The outline thickness forSTENCIL_MODE_OUTLINE.
intstencil_reference=1🔗
- voidset_stencil_reference(value:int)
voidset_stencil_reference(value:int)
- intget_stencil_reference()
intget_stencil_reference()
Experimental:May be affected by future rendering pipeline changes.
The stencil reference value (0-255). Typically a power of 2.
boolsubsurf_scatter_enabled=false🔗
- voidset_feature(feature:Feature, enable:bool)
voidset_feature(feature:Feature, enable:bool)
- boolget_feature(feature:Feature)const
boolget_feature(feature:Feature)const
Iftrue, subsurface scattering is enabled. Emulates light that penetrates an object's surface, is scattered, and then emerges. Subsurface scattering quality is controlled byProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_quality.
Note:Subsurface scattering is not supported on viewports that have a transparent background (whereViewport.transparent_bgistrue).
boolsubsurf_scatter_skin_mode=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, subsurface scattering will use a special mode optimized for the color and density of human skin, such as boosting the intensity of the red channel in subsurface scattering.
floatsubsurf_scatter_strength=0.0🔗
- voidset_subsurface_scattering_strength(value:float)
voidset_subsurface_scattering_strength(value:float)
- floatget_subsurface_scattering_strength()
floatget_subsurface_scattering_strength()
The strength of the subsurface scattering effect. The depth of the effect is also controlled byProjectSettings.rendering/environment/subsurface_scattering/subsurface_scattering_scale, which is set globally.
Texture2Dsubsurf_scatter_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
Texture used to control the subsurface scattering strength. Stored in the red texture channel. Multiplied bysubsurf_scatter_strength.
floatsubsurf_scatter_transmittance_boost=0.0🔗
- voidset_transmittance_boost(value:float)
voidset_transmittance_boost(value:float)
- floatget_transmittance_boost()
floatget_transmittance_boost()
The intensity of the subsurface scattering transmittance effect.
Colorsubsurf_scatter_transmittance_color=Color(1,1,1,1)🔗
- voidset_transmittance_color(value:Color)
voidset_transmittance_color(value:Color)
- Colorget_transmittance_color()
Colorget_transmittance_color()
The color to multiply the subsurface scattering transmittance effect with. Ignored ifsubsurf_scatter_skin_modeistrue.
floatsubsurf_scatter_transmittance_depth=0.1🔗
- voidset_transmittance_depth(value:float)
voidset_transmittance_depth(value:float)
- floatget_transmittance_depth()
floatget_transmittance_depth()
The depth of the subsurface scattering transmittance effect.
boolsubsurf_scatter_transmittance_enabled=false🔗
- voidset_feature(feature:Feature, enable:bool)
voidset_feature(feature:Feature, enable:bool)
- boolget_feature(feature:Feature)const
boolget_feature(feature:Feature)const
Iftrue, enables subsurface scattering transmittance. Only effective ifsubsurf_scatter_enabledistrue. See alsobacklight_enabled.
Texture2Dsubsurf_scatter_transmittance_texture🔗
- voidset_texture(param:TextureParam, texture:Texture2D)
voidset_texture(param:TextureParam, texture:Texture2D)
- Texture2Dget_texture(param:TextureParam)const
Texture2Dget_texture(param:TextureParam)const
The texture to use for multiplying the intensity of the subsurface scattering transmittance intensity. See alsosubsurf_scatter_texture. Ignored ifsubsurf_scatter_skin_modeistrue.
TextureFiltertexture_filter=3🔗
- voidset_texture_filter(value:TextureFilter)
voidset_texture_filter(value:TextureFilter)
- TextureFilterget_texture_filter()
TextureFilterget_texture_filter()
Filter flags for the texture.
Note:heightmap_textureis always sampled with linear filtering, even if nearest-neighbor filtering is selected here. This is to ensure the heightmap effect looks as intended. If you need sharper height transitions between pixels, resize the heightmap texture in an image editor with nearest-neighbor filtering.
booltexture_repeat=true🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, the texture repeats when exceeding the texture's size. SeeFLAG_USE_TEXTURE_REPEAT.
Transparencytransparency=0🔗
- voidset_transparency(value:Transparency)
voidset_transparency(value:Transparency)
- Transparencyget_transparency()
Transparencyget_transparency()
The material's transparency mode. Some transparency modes will disable shadow casting. Any transparency mode other thanTRANSPARENCY_DISABLEDhas a greater performance impact compared to opaque rendering. See alsoblend_mode.
booluse_fov_override=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrueusefov_overrideto override theCamera3D's field of view angle.
booluse_particle_trails=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, enables parts of the shader required forGPUParticles3Dtrails to function. This also requires using a mesh with appropriate skinning, such asRibbonTrailMeshorTubeTrailMesh. Enabling this feature outside of materials used inGPUParticles3Dmeshes will break material rendering.
booluse_point_size=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, render point size can be changed.
Note:This is only effective for objects whose geometry is point-based rather than triangle-based. See alsopoint_size.
booluse_z_clip_scale=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrueusez_clip_scaleto scale the object being rendered towards the camera to avoid clipping into things like walls.
Vector3uv1_offset=Vector3(0,0,0)🔗
- voidset_uv1_offset(value:Vector3)
voidset_uv1_offset(value:Vector3)
- Vector3get_uv1_offset()
Vector3get_uv1_offset()
How much to offset theUVcoordinates. This amount will be added toUVin the vertex function. This can be used to offset a texture. The Z component is used whenuv1_triplanaris enabled, but it is not used anywhere else.
Vector3uv1_scale=Vector3(1,1,1)🔗
- voidset_uv1_scale(value:Vector3)
voidset_uv1_scale(value:Vector3)
- Vector3get_uv1_scale()
Vector3get_uv1_scale()
How much to scale theUVcoordinates. This is multiplied byUVin the vertex function. The Z component is used whenuv1_triplanaris enabled, but it is not used anywhere else.
booluv1_triplanar=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, instead of usingUVtextures will use a triplanar texture lookup to determine how to apply textures. Triplanar uses the orientation of the object's surface to blend between texture coordinates. It reads from the source texture 3 times, once for each axis and then blends between the results based on how closely the pixel aligns with each axis. This is often used for natural features to get a realistic blend of materials. Because triplanar texturing requires many more texture reads per-pixel it is much slower than normal UV texturing. Additionally, because it is blending the texture between the three axes, it is unsuitable when you are trying to achieve crisp texturing.
floatuv1_triplanar_sharpness=1.0🔗
- voidset_uv1_triplanar_blend_sharpness(value:float)
voidset_uv1_triplanar_blend_sharpness(value:float)
- floatget_uv1_triplanar_blend_sharpness()
floatget_uv1_triplanar_blend_sharpness()
A lower number blends the texture more softly while a higher number blends the texture more sharply.
Note:uv1_triplanar_sharpnessis clamped between0.0and150.0(inclusive) as values outside that range can look broken depending on the mesh.
booluv1_world_triplanar=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, triplanar mapping forUVis calculated in world space rather than object local space. See alsouv1_triplanar.
Vector3uv2_offset=Vector3(0,0,0)🔗
- voidset_uv2_offset(value:Vector3)
voidset_uv2_offset(value:Vector3)
- Vector3get_uv2_offset()
Vector3get_uv2_offset()
How much to offset theUV2coordinates. This amount will be added toUV2in the vertex function. This can be used to offset a texture. The Z component is used whenuv2_triplanaris enabled, but it is not used anywhere else.
Vector3uv2_scale=Vector3(1,1,1)🔗
- voidset_uv2_scale(value:Vector3)
voidset_uv2_scale(value:Vector3)
- Vector3get_uv2_scale()
Vector3get_uv2_scale()
How much to scale theUV2coordinates. This is multiplied byUV2in the vertex function. The Z component is used whenuv2_triplanaris enabled, but it is not used anywhere else.
booluv2_triplanar=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, instead of usingUV2textures will use a triplanar texture lookup to determine how to apply textures. Triplanar uses the orientation of the object's surface to blend between texture coordinates. It reads from the source texture 3 times, once for each axis and then blends between the results based on how closely the pixel aligns with each axis. This is often used for natural features to get a realistic blend of materials. Because triplanar texturing requires many more texture reads per-pixel it is much slower than normal UV texturing. Additionally, because it is blending the texture between the three axes, it is unsuitable when you are trying to achieve crisp texturing.
floatuv2_triplanar_sharpness=1.0🔗
- voidset_uv2_triplanar_blend_sharpness(value:float)
voidset_uv2_triplanar_blend_sharpness(value:float)
- floatget_uv2_triplanar_blend_sharpness()
floatget_uv2_triplanar_blend_sharpness()
A lower number blends the texture more softly while a higher number blends the texture more sharply.
Note:uv2_triplanar_sharpnessis clamped between0.0and150.0(inclusive) as values outside that range can look broken depending on the mesh.
booluv2_world_triplanar=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, triplanar mapping forUV2is calculated in world space rather than object local space. See alsouv2_triplanar.
boolvertex_color_is_srgb=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, vertex colors are considered to be stored in nonlinear sRGB encoding and are converted to linear encoding during rendering. Iffalse, vertex colors are considered to be stored in linear encoding and are rendered as-is. See alsoalbedo_texture_force_srgb.
Note:Only effective when using the Forward+ and Mobile rendering methods, not Compatibility.
boolvertex_color_use_as_albedo=false🔗
- voidset_flag(flag:Flags, enable:bool)
voidset_flag(flag:Flags, enable:bool)
- boolget_flag(flag:Flags)const
boolget_flag(flag:Flags)const
Iftrue, the vertex color is used as albedo color.
floatz_clip_scale=1.0🔗
- voidset_z_clip_scale(value:float)
voidset_z_clip_scale(value:float)
- floatget_z_clip_scale()
floatget_z_clip_scale()
Scales the object being rendered towards the camera to avoid clipping into things like walls. This is intended to be used for objects that are fixed with respect to the camera like player arms, tools, etc. Lighting and shadows will continue to work correctly when this setting is adjusted, but screen-space effects like SSAO and SSR may break with lower scales. Therefore, try to keep this setting as close to1.0as possible.

## Method Descriptions

boolget_feature(feature:Feature)const🔗
Returnstrueif the specifiedfeatureis enabled.
boolget_flag(flag:Flags)const🔗
Returnstrueif the specifiedflagis enabled.
Texture2Dget_texture(param:TextureParam)const🔗
Returns theTexture2Dassociated with the specified textureparam.
voidset_feature(feature:Feature, enable:bool)🔗
Ifenableistrue, enables the specifiedfeature. Many features that are available inBaseMaterial3Dneed to be enabled before use. This way, the cost for using the feature is only incurred when specified. Features can also be enabled by setting their corresponding property totrue.
voidset_flag(flag:Flags, enable:bool)🔗
Ifenableistrue, enables the specifiedflag. Flags are optional behavior that can be turned on and off. Only one flag can be enabled at a time with this function, the flag enumerators cannot be bit-masked together to enable or disable multiple flags at once. Flags can also be enabled by setting their corresponding property totrue.
voidset_texture(param:TextureParam, texture:Texture2D)🔗
Sets the texture for the slot specified byparam.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
