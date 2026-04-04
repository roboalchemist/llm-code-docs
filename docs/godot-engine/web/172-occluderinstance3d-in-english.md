# OccluderInstance3D in English

# OccluderInstance3D

Inherits:VisualInstance3D<Node3D<Node<Object
Provides occlusion culling for 3D nodes, which improves performance in closed areas.

## Description

Occlusion culling can improve rendering performance in closed/semi-open areas by hiding geometry that is occluded by other objects.
The occlusion culling system is mostly static.OccluderInstance3Ds can be moved or hidden at run-time, but doing so will trigger a background recomputation that can take several frames. It is recommended to only moveOccluderInstance3Ds sporadically (e.g. for procedural generation purposes), rather than doing so every frame.
The occlusion culling system works by rendering the occluders on the CPU in parallel usingEmbree, drawing the result to a low-resolution buffer then using this to cull 3D nodes individually. In the 3D editor, you can preview the occlusion culling buffer by choosingPerspective > Display Advanced... > Occlusion Culling Bufferin the top-left corner of the 3D viewport. The occlusion culling buffer quality can be adjusted in the Project Settings.
Baking:Select anOccluderInstance3Dnode, then use theBake Occludersbutton at the top of the 3D editor. Only opaque materials will be taken into account; transparent materials (alpha-blended or alpha-tested) will be ignored by the occluder generation.
Note:Occlusion culling is only effective ifProjectSettings.rendering/occlusion_culling/use_occlusion_cullingistrue. Enabling occlusion culling has a cost on the CPU. Only enable occlusion culling if you actually plan to use it. Large open scenes with few or no objects blocking the view will generally not benefit much from occlusion culling. Large open scenes generally benefit more from mesh LOD and visibility ranges (GeometryInstance3D.visibility_range_beginandGeometryInstance3D.visibility_range_end) compared to occlusion culling.
Note:Due to memory constraints, occlusion culling is not supported by default in Web export templates. It can be enabled by compiling custom Web export templates withmodule_raycast_enabled=yes.

## Tutorials

- Occlusion culling
Occlusion culling

## Properties

| int | bake_mask | 4294967295 |
|---|---|---|
| float | bake_simplification_distance | 0.1 |
| Occluder3D | occluder |  |

bake_mask
4294967295
float
bake_simplification_distance
Occluder3D
occluder

## Methods

| bool | get_bake_mask_value(layer_number:int)const |
|---|---|
| void | set_bake_mask_value(layer_number:int, value:bool) |

bool
get_bake_mask_value(layer_number:int)const
void
set_bake_mask_value(layer_number:int, value:bool)

## Property Descriptions

intbake_mask=4294967295🔗

- voidset_bake_mask(value:int)
voidset_bake_mask(value:int)
- intget_bake_mask()
intget_bake_mask()
The visual layers to account for when baking for occluders. OnlyMeshInstance3Ds whoseVisualInstance3D.layersmatch with thisbake_maskwill be included in the generated occluder mesh. By default, all objects withopaquematerials are taken into account for the occluder baking.
To improve performance and avoid artifacts, it is recommended to exclude dynamic objects, small objects and fixtures from the baking process by moving them to a separate visual layer and excluding this layer inbake_mask.
floatbake_simplification_distance=0.1🔗
- voidset_bake_simplification_distance(value:float)
voidset_bake_simplification_distance(value:float)
- floatget_bake_simplification_distance()
floatget_bake_simplification_distance()
The simplification distance to use for simplifying the generated occluder polygon (in 3D units). Higher values result in a less detailed occluder mesh, which improves performance but reduces culling accuracy.
The occluder geometry is rendered on the CPU, so it is important to keep its geometry as simple as possible. Since the buffer is rendered at a low resolution, less detailed occluder meshes generally still work well. The default value is fairly aggressive, so you may have to decrease it if you run into false negatives (objects being occluded even though they are visible by the camera). A value of0.01will act conservatively, and will keep geometryperceptuallyunaffected in the occlusion culling buffer. Depending on the scene, a value of0.01may still simplify the mesh noticeably compared to disabling simplification entirely.
Setting this to0.0disables simplification entirely, but vertices in the exact same position will still be merged. The mesh will also be re-indexed to reduce both the number of vertices and indices.
Note:This uses themeshoptimizerlibrary under the hood, similar to LOD generation.
Occluder3Doccluder🔗
- voidset_occluder(value:Occluder3D)
voidset_occluder(value:Occluder3D)
- Occluder3Dget_occluder()
Occluder3Dget_occluder()
The occluder resource for thisOccluderInstance3D. You can generate an occluder resource by selecting anOccluderInstance3Dnode then using theBake Occludersbutton at the top of the editor.
You can also draw your own 2D occluder polygon by adding a newPolygonOccluder3Dresource to theoccluderproperty in the Inspector.
Alternatively, you can select a primitive occluder to use:QuadOccluder3D,BoxOccluder3DorSphereOccluder3D.

## Method Descriptions

boolget_bake_mask_value(layer_number:int)const🔗
Returns whether or not the specified layer of thebake_maskis enabled, given alayer_numberbetween 1 and 32.
voidset_bake_mask_value(layer_number:int, value:bool)🔗
Based onvalue, enables or disables the specified layer in thebake_mask, given alayer_numberbetween 1 and 32.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
