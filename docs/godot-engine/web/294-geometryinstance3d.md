# GeometryInstance3D

# GeometryInstance3D
Inherits:VisualInstance3D<Node3D<Node<Object
Inherited By:CPUParticles3D,CSGShape3D,GPUParticles3D,Label3D,MeshInstance3D,MultiMeshInstance3D,SpriteBase3D
Base node for geometry-based visual instances.

## Description
Base node for geometry-based visual instances. Shares some common functionality like visibility and custom materials.

## Tutorials
- Visibility ranges (HLOD)
Visibility ranges (HLOD)

## Properties

| ShadowCastingSetting | cast_shadow | 1 |
|---|---|---|
| AABB | custom_aabb | AABB(0,0,0,0,0,0) |
| float | extra_cull_margin | 0.0 |
| LightmapScale | gi_lightmap_scale | 0 |
| float | gi_lightmap_texel_scale | 1.0 |
| GIMode | gi_mode | 1 |
| bool | ignore_occlusion_culling | false |
| float | lod_bias | 1.0 |
| Material | material_overlay |  |
| Material | material_override |  |
| float | transparency | 0.0 |
| float | visibility_range_begin | 0.0 |
| float | visibility_range_begin_margin | 0.0 |
| float | visibility_range_end | 0.0 |
| float | visibility_range_end_margin | 0.0 |
| VisibilityRangeFadeMode | visibility_range_fade_mode | 0 |

ShadowCastingSetting
cast_shadow
AABB
custom_aabb
AABB(0,0,0,0,0,0)
float
extra_cull_margin
LightmapScale
gi_lightmap_scale
float
gi_lightmap_texel_scale
GIMode
gi_mode
bool
ignore_occlusion_culling
false
float
lod_bias
Material
material_overlay
Material
material_override
float
transparency
float
visibility_range_begin
float
visibility_range_begin_margin
float
visibility_range_end
float
visibility_range_end_margin
VisibilityRangeFadeMode
visibility_range_fade_mode

## Methods

| Variant | get_instance_shader_parameter(name:StringName)const |
|---|---|
| void | set_instance_shader_parameter(name:StringName, value:Variant) |

Variant
get_instance_shader_parameter(name:StringName)const
void
set_instance_shader_parameter(name:StringName, value:Variant)

## Enumerations
enumShadowCastingSetting:🔗
ShadowCastingSettingSHADOW_CASTING_SETTING_OFF=0
Will not cast any shadows. Use this to improve performance for small geometry that is unlikely to cast noticeable shadows (such as debris).
ShadowCastingSettingSHADOW_CASTING_SETTING_ON=1
Will cast shadows from all visible faces in the GeometryInstance3D.
Will take culling into account, so faces not being rendered will not be taken into account when shadow casting.
ShadowCastingSettingSHADOW_CASTING_SETTING_DOUBLE_SIDED=2
Will cast shadows from all visible faces in the GeometryInstance3D.
Will not take culling into account, so all faces will be taken into account when shadow casting.
ShadowCastingSettingSHADOW_CASTING_SETTING_SHADOWS_ONLY=3
Will only show the shadows casted from this object.
In other words, the actual mesh will not be visible, only the shadows casted from the mesh will be.
enumGIMode:🔗
GIModeGI_MODE_DISABLED=0
Disabled global illumination mode. Use for dynamic objects that do not contribute to global illumination (such as characters). When usingVoxelGIand SDFGI, the geometry willreceiveindirect lighting and reflections but the geometry will not be considered in GI baking.
GIModeGI_MODE_STATIC=1
Baked global illumination mode. Use for static objects that contribute to global illumination (such as level geometry). This GI mode is effective when usingVoxelGI, SDFGI andLightmapGI.
GIModeGI_MODE_DYNAMIC=2
Dynamic global illumination mode. Use for dynamic objects that contribute to global illumination. This GI mode is only effective when usingVoxelGI, but it has a higher performance impact thanGI_MODE_STATIC. When using other GI methods, this will act the same asGI_MODE_DISABLED. When usingLightmapGI, the object will receive indirect lighting using lightmap probes instead of using the baked lightmap texture.
enumLightmapScale:🔗
LightmapScaleLIGHTMAP_SCALE_1X=0
Deprecated:Usegi_lightmap_texel_scaleinstead.
The standard texel density for lightmapping withLightmapGI.
LightmapScaleLIGHTMAP_SCALE_2X=1
Deprecated:Usegi_lightmap_texel_scaleinstead.
Multiplies texel density by 2× for lightmapping withLightmapGI. To ensure consistency in texel density, use this when scaling a mesh by a factor between 1.5 and 3.0.
LightmapScaleLIGHTMAP_SCALE_4X=2
Deprecated:Usegi_lightmap_texel_scaleinstead.
Multiplies texel density by 4× for lightmapping withLightmapGI. To ensure consistency in texel density, use this when scaling a mesh by a factor between 3.0 and 6.0.
LightmapScaleLIGHTMAP_SCALE_8X=3
Deprecated:Usegi_lightmap_texel_scaleinstead.
Multiplies texel density by 8× for lightmapping withLightmapGI. To ensure consistency in texel density, use this when scaling a mesh by a factor greater than 6.0.
LightmapScaleLIGHTMAP_SCALE_MAX=4
Deprecated:Usegi_lightmap_texel_scaleinstead.
Represents the size of theLightmapScaleenum.
enumVisibilityRangeFadeMode:🔗
VisibilityRangeFadeModeVISIBILITY_RANGE_FADE_DISABLED=0
Will not fade itself nor its visibility dependencies, hysteresis will be used instead. This is the fastest approach to manual LOD, but it can result in noticeable LOD transitions depending on how the LOD meshes are authored. Seevisibility_range_beginandNode3D.visibility_parentfor more information.
VisibilityRangeFadeModeVISIBILITY_RANGE_FADE_SELF=1
Will fade-out itself when reaching the limits of its own visibility range. This is slower thanVISIBILITY_RANGE_FADE_DISABLED, but it can provide smoother transitions. The fading range is determined byvisibility_range_begin_marginandvisibility_range_end_margin.
Note:Only supported when using the Forward+ rendering method. When using the Mobile or Compatibility rendering method, this mode acts likeVISIBILITY_RANGE_FADE_DISABLEDbut with hysteresis disabled.
VisibilityRangeFadeModeVISIBILITY_RANGE_FADE_DEPENDENCIES=2
Will fade-in its visibility dependencies (seeNode3D.visibility_parent) when reaching the limits of its own visibility range. This is slower thanVISIBILITY_RANGE_FADE_DISABLED, but it can provide smoother transitions. The fading range is determined byvisibility_range_begin_marginandvisibility_range_end_margin.
Note:Only supported when using the Forward+ rendering method. When using the Mobile or Compatibility rendering method, this mode acts likeVISIBILITY_RANGE_FADE_DISABLEDbut with hysteresis disabled.

## Property Descriptions
ShadowCastingSettingcast_shadow=1🔗
- voidset_cast_shadows_setting(value:ShadowCastingSetting)
voidset_cast_shadows_setting(value:ShadowCastingSetting)
- ShadowCastingSettingget_cast_shadows_setting()
ShadowCastingSettingget_cast_shadows_setting()
The mode used to cast shadows from this instance.
AABBcustom_aabb=AABB(0,0,0,0,0,0)🔗
- voidset_custom_aabb(value:AABB)
voidset_custom_aabb(value:AABB)
- AABBget_custom_aabb()
AABBget_custom_aabb()
Overrides the bounding box of this node with a custom one. This can be used to avoid the expensiveAABBrecalculation that happens when a skeleton is used with aMeshInstance3Dor to have precise control over theMeshInstance3D's bounding box. To use the default AABB, set value to anAABBwith all fields set to0.0. To avoid frustum culling, setcustom_aabbto a very large AABB that covers your entire game world such asAABB(-10000,-10000,-10000,20000,20000,20000). To disable all forms of culling (including occlusion culling), callRenderingServer.instance_set_ignore_culling()on theGeometryInstance3D'sRID.
floatextra_cull_margin=0.0🔗
- voidset_extra_cull_margin(value:float)
voidset_extra_cull_margin(value:float)
- floatget_extra_cull_margin()
floatget_extra_cull_margin()
The extra distance added to the GeometryInstance3D's bounding box (AABB) to increase its cull box.
LightmapScalegi_lightmap_scale=0🔗
- voidset_lightmap_scale(value:LightmapScale)
voidset_lightmap_scale(value:LightmapScale)
- LightmapScaleget_lightmap_scale()
LightmapScaleget_lightmap_scale()
Deprecated:Usegi_lightmap_texel_scaleinstead.
The texel density to use for lightmapping inLightmapGI.
floatgi_lightmap_texel_scale=1.0🔗
- voidset_lightmap_texel_scale(value:float)
voidset_lightmap_texel_scale(value:float)
- floatget_lightmap_texel_scale()
floatget_lightmap_texel_scale()
The texel density to use for lightmapping inLightmapGI. Greater scale values provide higher resolution in the lightmap, which can result in sharper shadows for lights that have both direct and indirect light baked. However, greater scale values will also increase the space taken by the mesh in the lightmap texture, which increases the memory, storage, and bake time requirements. When using a single mesh at different scales, consider adjusting this value to keep the lightmap texel density consistent across meshes.
For example, doublinggi_lightmap_texel_scaledoubles the lightmap texture resolution for this objecton each axis, so it willquadruplethe texel count.
GIModegi_mode=1🔗
- voidset_gi_mode(value:GIMode)
voidset_gi_mode(value:GIMode)
- GIModeget_gi_mode()
GIModeget_gi_mode()
The global illumination mode to use for the whole geometry. To avoid inconsistent results, use a mode that matches the purpose of the mesh during gameplay (static/dynamic).
Note:Lights' bake mode will also affect the global illumination rendering. SeeLight3D.light_bake_mode.
boolignore_occlusion_culling=false🔗
- voidset_ignore_occlusion_culling(value:bool)
voidset_ignore_occlusion_culling(value:bool)
- boolis_ignoring_occlusion_culling()
boolis_ignoring_occlusion_culling()
Iftrue, disables occlusion culling for this instance. Useful for gizmos that must be rendered even when occlusion culling is in use.
Note:ignore_occlusion_cullingdoes not affect frustum culling (which is what happens when an object is not visible given the camera's angle). To avoid frustum culling, setcustom_aabbto a very large AABB that covers your entire game world such asAABB(-10000,-10000,-10000,20000,20000,20000).
floatlod_bias=1.0🔗
- voidset_lod_bias(value:float)
voidset_lod_bias(value:float)
- floatget_lod_bias()
floatget_lod_bias()
Changes how quickly the mesh transitions to a lower level of detail. A value of 0 will force the mesh to its lowest level of detail, a value of 1 will use the default settings, and larger values will keep the mesh in a higher level of detail at farther distances.
Useful for testing level of detail transitions in the editor.
Materialmaterial_overlay🔗
- voidset_material_overlay(value:Material)
voidset_material_overlay(value:Material)
- Materialget_material_overlay()
Materialget_material_overlay()
The material overlay for the whole geometry.
If a material is assigned to this property, it will be rendered on top of any other active material for all the surfaces.
Materialmaterial_override🔗
- voidset_material_override(value:Material)
voidset_material_override(value:Material)
- Materialget_material_override()
Materialget_material_override()
The material override for the whole geometry.
If a material is assigned to this property, it will be used instead of any material set in any material slot of the mesh.
floattransparency=0.0🔗
- voidset_transparency(value:float)
voidset_transparency(value:float)
- floatget_transparency()
floatget_transparency()
The transparency applied to the whole geometry (as a multiplier of the materials' existing transparency).0.0is fully opaque, while1.0is fully transparent. Values greater than0.0(exclusive) will force the geometry's materials to go through the transparent pipeline, which is slower to render and can exhibit rendering issues due to incorrect transparency sorting. However, unlike using a transparent material, settingtransparencyto a value greater than0.0(exclusive) willnotdisable shadow rendering.
In spatial shaders,1.0-transparencyis set as the default value of theALPHAbuilt-in.
Note:transparencyis clamped between0.0and1.0, so this property cannot be used to make transparent materials more opaque than they originally are.
Note:Only supported when using the Forward+ rendering method. When using the Mobile or Compatibility rendering method,transparencyis ignored and is considered as always being0.0.
floatvisibility_range_begin=0.0🔗
- voidset_visibility_range_begin(value:float)
voidset_visibility_range_begin(value:float)
- floatget_visibility_range_begin()
floatget_visibility_range_begin()
Starting distance from which the GeometryInstance3D will be visible, takingvisibility_range_begin_margininto account as well. The default value of 0 is used to disable the range check.
floatvisibility_range_begin_margin=0.0🔗
- voidset_visibility_range_begin_margin(value:float)
voidset_visibility_range_begin_margin(value:float)
- floatget_visibility_range_begin_margin()
floatget_visibility_range_begin_margin()
Margin for thevisibility_range_beginthreshold. The GeometryInstance3D will only change its visibility state when it goes over or under thevisibility_range_beginthreshold by this amount.
Ifvisibility_range_fade_modeisVISIBILITY_RANGE_FADE_DISABLED, this acts as a hysteresis distance. Ifvisibility_range_fade_modeisVISIBILITY_RANGE_FADE_SELForVISIBILITY_RANGE_FADE_DEPENDENCIES, this acts as a fade transition distance and must be set to a value greater than0.0for the effect to be noticeable.
floatvisibility_range_end=0.0🔗
- voidset_visibility_range_end(value:float)
voidset_visibility_range_end(value:float)
- floatget_visibility_range_end()
floatget_visibility_range_end()
Distance from which the GeometryInstance3D will be hidden, takingvisibility_range_end_margininto account as well. The default value of 0 is used to disable the range check.
floatvisibility_range_end_margin=0.0🔗
- voidset_visibility_range_end_margin(value:float)
voidset_visibility_range_end_margin(value:float)
- floatget_visibility_range_end_margin()
floatget_visibility_range_end_margin()
Margin for thevisibility_range_endthreshold. The GeometryInstance3D will only change its visibility state when it goes over or under thevisibility_range_endthreshold by this amount.
Ifvisibility_range_fade_modeisVISIBILITY_RANGE_FADE_DISABLED, this acts as a hysteresis distance. Ifvisibility_range_fade_modeisVISIBILITY_RANGE_FADE_SELForVISIBILITY_RANGE_FADE_DEPENDENCIES, this acts as a fade transition distance and must be set to a value greater than0.0for the effect to be noticeable.
VisibilityRangeFadeModevisibility_range_fade_mode=0🔗
- voidset_visibility_range_fade_mode(value:VisibilityRangeFadeMode)
voidset_visibility_range_fade_mode(value:VisibilityRangeFadeMode)
- VisibilityRangeFadeModeget_visibility_range_fade_mode()
VisibilityRangeFadeModeget_visibility_range_fade_mode()
Controls which instances will be faded when approaching the limits of the visibility range.

## Method Descriptions
Variantget_instance_shader_parameter(name:StringName)const🔗
Get the value of a shader parameter as set on this instance.
voidset_instance_shader_parameter(name:StringName, value:Variant)🔗
Set the value of a shader uniform for this instance only (per-instance uniform). See alsoShaderMaterial.set_shader_parameter()to assign a uniform on all instances using the sameShaderMaterial.
Note:For a shader uniform to be assignable on a per-instance basis, itmustbe defined withinstanceuniform...rather thanuniform...in the shader code.
Note:nameis case-sensitive and must match the name of the uniform in the code exactly (not the capitalized name in the inspector).
Note:Per-instance shader uniforms are only available in Spatial and CanvasItem shaders, but not for Fog, Sky, or Particles shaders.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.