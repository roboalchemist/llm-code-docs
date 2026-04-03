# ReflectionProbe in English

# ReflectionProbe
Inherits:VisualInstance3D<Node3D<Node<Object
Captures its surroundings to create fast, accurate reflections from a given point.

## Description
Captures its surroundings as a cubemap, and stores versions of it with increasing levels of blur to simulate different material roughnesses.
TheReflectionProbeis used to create high-quality reflections at a low performance cost (whenupdate_modeisUPDATE_ONCE).ReflectionProbes can be blended together and with the rest of the scene smoothly.ReflectionProbes can also be combined withVoxelGI, SDFGI (Environment.sdfgi_enabled) and screen-space reflections (Environment.ssr_enabled) to get more accurate reflections in specific areas.ReflectionProbes render all objects within theircull_mask, so updating them can be quite expensive. It is best to update them once with the important static objects and then leave them as-is.
Note:UnlikeVoxelGIand SDFGI,ReflectionProbes only source their environment from aWorldEnvironmentnode. If you specify anEnvironmentresource within aCamera3Dnode, it will be ignored by theReflectionProbe. This can lead to incorrect lighting within theReflectionProbe.
Note:When using the Mobile rendering method, only8reflection probes can be displayed on each mesh resource, while the Compatibility rendering method only supports up to2reflection probes on each mesh. Attempting to display more than8reflection probes on a single mesh resource using the Mobile renderer will result in reflection probes flickering in and out as the camera moves, while the Compatibility renderer will not render any additional probes if more than2reflection probes are being used.
Note:When using the Mobile rendering method, reflection probes will only correctly affect meshes whose visibility AABB intersects with the reflection probe's AABB. If using a shader to deform the mesh in a way that makes it go outside its AABB,GeometryInstance3D.extra_cull_marginmust be increased on the mesh. Otherwise, the reflection probe may not be visible on the mesh.

## Tutorials
- Reflection probes
Reflection probes

## Properties

| Color | ambient_color | Color(0,0,0,1) |
|---|---|---|
| float | ambient_color_energy | 1.0 |
| AmbientMode | ambient_mode | 1 |
| float | blend_distance | 1.0 |
| bool | box_projection | false |
| int | cull_mask | 1048575 |
| bool | enable_shadows | false |
| float | intensity | 1.0 |
| bool | interior | false |
| float | max_distance | 0.0 |
| float | mesh_lod_threshold | 1.0 |
| Vector3 | origin_offset | Vector3(0,0,0) |
| int | reflection_mask | 1048575 |
| Vector3 | size | Vector3(20,20,20) |
| UpdateMode | update_mode | 0 |

Color
ambient_color
Color(0,0,0,1)
float
ambient_color_energy
AmbientMode
ambient_mode
float
blend_distance
bool
box_projection
false
cull_mask
1048575
bool
enable_shadows
false
float
intensity
bool
interior
false
float
max_distance
float
mesh_lod_threshold
Vector3
origin_offset
Vector3(0,0,0)
reflection_mask
1048575
Vector3
size
Vector3(20,20,20)
UpdateMode
update_mode

## Enumerations
enumUpdateMode:🔗
UpdateModeUPDATE_ONCE=0
Update the probe once on the next frame (recommended for most objects). The corresponding radiance map will be generated over the following six frames. This takes more time to update thanUPDATE_ALWAYS, but it has a lower performance cost and can result in higher-quality reflections. The ReflectionProbe is updated when its transform changes, but not when nearby geometry changes. You can force aReflectionProbeupdate by moving theReflectionProbeslightly in any direction.
UpdateModeUPDATE_ALWAYS=1
Update the probe every frame. This provides better results for fast-moving dynamic objects (such as cars). However, it has a significant performance cost. Due to the cost, it's recommended to only use one ReflectionProbe withUPDATE_ALWAYSat most per scene. For all other use cases, useUPDATE_ONCE.
enumAmbientMode:🔗
AmbientModeAMBIENT_DISABLED=0
Do not apply any ambient lighting inside theReflectionProbe's box defined by itssize.
AmbientModeAMBIENT_ENVIRONMENT=1
Apply automatically-sourced environment lighting inside theReflectionProbe's box defined by itssize.
AmbientModeAMBIENT_COLOR=2
Apply custom ambient lighting inside theReflectionProbe's box defined by itssize. Seeambient_colorandambient_color_energy.

## Property Descriptions
Colorambient_color=Color(0,0,0,1)🔗
- voidset_ambient_color(value:Color)
voidset_ambient_color(value:Color)
- Colorget_ambient_color()
Colorget_ambient_color()
The custom ambient color to use within theReflectionProbe's box defined by itssize. Only effective ifambient_modeisAMBIENT_COLOR.
floatambient_color_energy=1.0🔗
- voidset_ambient_color_energy(value:float)
voidset_ambient_color_energy(value:float)
- floatget_ambient_color_energy()
floatget_ambient_color_energy()
The custom ambient color energy to use within theReflectionProbe's box defined by itssize. Only effective ifambient_modeisAMBIENT_COLOR.
AmbientModeambient_mode=1🔗
- voidset_ambient_mode(value:AmbientMode)
voidset_ambient_mode(value:AmbientMode)
- AmbientModeget_ambient_mode()
AmbientModeget_ambient_mode()
The ambient color to use within theReflectionProbe's box defined by itssize. The ambient color will smoothly blend with otherReflectionProbes and the rest of the scene (outside theReflectionProbe's box defined by itssize).
floatblend_distance=1.0🔗
- voidset_blend_distance(value:float)
voidset_blend_distance(value:float)
- floatget_blend_distance()
floatget_blend_distance()
Defines the distance in meters over which a probe blends into the scene.
boolbox_projection=false🔗
- voidset_enable_box_projection(value:bool)
voidset_enable_box_projection(value:bool)
- boolis_box_projection_enabled()
boolis_box_projection_enabled()
Iftrue, enables box projection. This makes reflections look more correct in rectangle-shaped rooms by offsetting the reflection center depending on the camera's location.
Note:To better fit rectangle-shaped rooms that are not aligned to the grid, you can rotate theReflectionProbenode.
intcull_mask=1048575🔗
- voidset_cull_mask(value:int)
voidset_cull_mask(value:int)
- intget_cull_mask()
intget_cull_mask()
Sets the cull mask which determines what objects are drawn by this probe. EveryVisualInstance3Dwith a layer included in this cull mask will be rendered by the probe. It is best to only include large objects which are likely to take up a lot of space in the reflection in order to save on rendering cost.
This can also be used to prevent an object from reflecting upon itself (for instance, aReflectionProbecentered on a vehicle).
boolenable_shadows=false🔗
- voidset_enable_shadows(value:bool)
voidset_enable_shadows(value:bool)
- boolare_shadows_enabled()
boolare_shadows_enabled()
Iftrue, computes shadows in the reflection probe. This makes the reflection probe slower to render; you may want to disable this if using theUPDATE_ALWAYSupdate_mode.
floatintensity=1.0🔗
- voidset_intensity(value:float)
voidset_intensity(value:float)
- floatget_intensity()
floatget_intensity()
Defines the reflection intensity. Intensity modulates the strength of the reflection.
boolinterior=false🔗
- voidset_as_interior(value:bool)
voidset_as_interior(value:bool)
- boolis_set_as_interior()
boolis_set_as_interior()
Iftrue, reflections will ignore sky contribution.
floatmax_distance=0.0🔗
- voidset_max_distance(value:float)
voidset_max_distance(value:float)
- floatget_max_distance()
floatget_max_distance()
The maximum distance away from theReflectionProbean object can be before it is culled. Decrease this to improve performance, especially when using theUPDATE_ALWAYSupdate_mode.
Note:The maximum reflection distance is always at least equal to the probe's extents. This means that decreasingmax_distancewill not always cull objects from reflections, especially if the reflection probe's box defined by itssizeis already large.
floatmesh_lod_threshold=1.0🔗
- voidset_mesh_lod_threshold(value:float)
voidset_mesh_lod_threshold(value:float)
- floatget_mesh_lod_threshold()
floatget_mesh_lod_threshold()
The automatic LOD bias to use for meshes rendered within theReflectionProbe(this is analog toViewport.mesh_lod_threshold). Higher values will use less detailed versions of meshes that have LOD variations generated. If set to0.0, automatic LOD is disabled. Increasemesh_lod_thresholdto improve performance at the cost of geometry detail, especially when using theUPDATE_ALWAYSupdate_mode.
Note:mesh_lod_thresholddoes not affectGeometryInstance3Dvisibility ranges (also known as "manual" LOD or hierarchical LOD).
Vector3origin_offset=Vector3(0,0,0)🔗
- voidset_origin_offset(value:Vector3)
voidset_origin_offset(value:Vector3)
- Vector3get_origin_offset()
Vector3get_origin_offset()
Sets the origin offset to be used when thisReflectionProbeis inbox_projectionmode. This can be set to a non-zero value to ensure a reflection fits a rectangle-shaped room, while reducing the number of objects that "get in the way" of the reflection.
intreflection_mask=1048575🔗
- voidset_reflection_mask(value:int)
voidset_reflection_mask(value:int)
- intget_reflection_mask()
intget_reflection_mask()
Sets the reflection mask which determines what objects have reflections applied from this probe. EveryVisualInstance3Dwith a layer included in this reflection mask will have reflections applied from this probe. See alsocull_mask, which can be used to exclude objects from appearing in the reflection while still making them affected by theReflectionProbe.
Vector3size=Vector3(20,20,20)🔗
- voidset_size(value:Vector3)
voidset_size(value:Vector3)
- Vector3get_size()
Vector3get_size()
The size of the reflection probe. The larger the size, the more space covered by the probe, which will lower the perceived resolution. It is best to keep the size only as large as you need it.
Note:To better fit areas that are not aligned to the grid, you can rotate theReflectionProbenode.
UpdateModeupdate_mode=0🔗
- voidset_update_mode(value:UpdateMode)
voidset_update_mode(value:UpdateMode)
- UpdateModeget_update_mode()
UpdateModeget_update_mode()
Sets how frequently theReflectionProbeis updated. Can beUPDATE_ONCEorUPDATE_ALWAYS.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.