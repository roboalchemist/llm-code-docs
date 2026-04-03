# VisualInstance3D in English

# VisualInstance3D
Inherits:Node3D<Node<Object
Inherited By:Decal,FogVolume,GeometryInstance3D,GPUParticlesAttractor3D,GPUParticlesCollision3D,Light3D,LightmapGI,OccluderInstance3D,OpenXRVisibilityMask,ReflectionProbe,RootMotionView,VisibleOnScreenNotifier3D,VoxelGI
Parent of all visual 3D nodes.

## Description
TheVisualInstance3Dis used to connect a resource to a visual representation. All visual 3D nodes inherit from theVisualInstance3D. In general, you should not access theVisualInstance3Dproperties directly as they are accessed and managed by the nodes that inherit fromVisualInstance3D.VisualInstance3Dis the node representation of theRenderingServerinstance.

## Properties

| int | layers | 1 |
|---|---|---|
| float | sorting_offset | 0.0 |
| bool | sorting_use_aabb_center |  |

layers
float
sorting_offset
bool
sorting_use_aabb_center

## Methods

| AABB | _get_aabb()virtualconst |
|---|---|
| AABB | get_aabb()const |
| RID | get_base()const |
| RID | get_instance()const |
| bool | get_layer_mask_value(layer_number:int)const |
| void | set_base(base:RID) |
| void | set_layer_mask_value(layer_number:int, value:bool) |

AABB
_get_aabb()virtualconst
AABB
get_aabb()const
get_base()const
get_instance()const
bool
get_layer_mask_value(layer_number:int)const
void
set_base(base:RID)
void
set_layer_mask_value(layer_number:int, value:bool)

## Property Descriptions
intlayers=1🔗
- voidset_layer_mask(value:int)
voidset_layer_mask(value:int)
- intget_layer_mask()
intget_layer_mask()
The render layer(s) thisVisualInstance3Dis drawn on.
This object will only be visible forCamera3Ds whose cull mask includes any of the render layers thisVisualInstance3Dis set to.
ForLight3Ds, this can be used to control whichVisualInstance3Ds are affected by a specific light. ForGPUParticles3D, this can be used to control which particles are effected by a specific attractor. ForDecals, this can be used to control whichVisualInstance3Ds are affected by a specific decal.
To adjustlayersmore easily using a script, useget_layer_mask_value()andset_layer_mask_value().
Note:VoxelGI, SDFGI andLightmapGIwill always take all layers into account to determine what contributes to global illumination. If this is an issue, setGeometryInstance3D.gi_modetoGeometryInstance3D.GI_MODE_DISABLEDfor meshes andLight3D.light_bake_modetoLight3D.BAKE_DISABLEDfor lights to exclude them from global illumination.
floatsorting_offset=0.0🔗
- voidset_sorting_offset(value:float)
voidset_sorting_offset(value:float)
- floatget_sorting_offset()
floatget_sorting_offset()
The amount by which the depth of thisVisualInstance3Dwill be adjusted when sorting by depth. Uses the same units as the engine (which are typically meters). Adjusting it to a higher value will make theVisualInstance3Dreliably draw on top of otherVisualInstance3Ds that are otherwise positioned at the same spot. To ensure it always draws on top of other objects around it (not positioned at the same spot), set the value to be greater than the distance between thisVisualInstance3Dand the other nearbyVisualInstance3Ds.
boolsorting_use_aabb_center🔗
- voidset_sorting_use_aabb_center(value:bool)
voidset_sorting_use_aabb_center(value:bool)
- boolis_sorting_use_aabb_center()
boolis_sorting_use_aabb_center()
Iftrue, the object is sorted based on theAABBcenter. The object will be sorted based on the global position otherwise.
TheAABBcenter based sorting is generally more accurate for 3D models. The position based sorting instead allows to better control the drawing order when working withGPUParticles3DandCPUParticles3D.

## Method Descriptions
AABB_get_aabb()virtualconst🔗
There is currently no description for this method. Please help us bycontributing one!
AABBget_aabb()const🔗
Returns theAABB(also known as the bounding box) for thisVisualInstance3D.
RIDget_base()const🔗
Returns the RID of the resource associated with thisVisualInstance3D. For example, if the Node is aMeshInstance3D, this will return the RID of the associatedMesh.
RIDget_instance()const🔗
Returns the RID of this instance. This RID is the same as the RID returned byRenderingServer.instance_create(). This RID is needed if you want to callRenderingServerfunctions directly on thisVisualInstance3D.
boolget_layer_mask_value(layer_number:int)const🔗
Returns whether or not the specified layer of thelayersis enabled, given alayer_numberbetween 1 and 20.
voidset_base(base:RID)🔗
Sets the resource that is instantiated by thisVisualInstance3D, which changes how the engine handles theVisualInstance3Dunder the hood. Equivalent toRenderingServer.instance_set_base().
voidset_layer_mask_value(layer_number:int, value:bool)🔗
Based onvalue, enables or disables the specified layer in thelayers, given alayer_numberbetween 1 and 20.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.