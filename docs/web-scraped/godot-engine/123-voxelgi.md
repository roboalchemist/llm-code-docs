# VoxelGI

# VoxelGI
Inherits:VisualInstance3D<Node3D<Node<Object
Real-time global illumination (GI) probe.

## Description
VoxelGIs are used to provide high-quality real-time indirect light and reflections to scenes. They precompute the effect of objects that emit light and the effect of static geometry to simulate the behavior of complex light in real-time.VoxelGIs need to be baked before having a visible effect. However, once baked, dynamic objects will receive light from them. Furthermore, lights can be fully dynamic or baked.
Note:VoxelGIis only supported in the Forward+ rendering method, not Mobile or Compatibility.
Procedural generation:VoxelGIcan be baked in an exported project, which makes it suitable for procedurally generated or user-built levels as long as all the geometry is generated in advance. For games where geometry is generated at any time during gameplay, SDFGI is more suitable (seeEnvironment.sdfgi_enabled).
Performance:VoxelGIis relatively demanding on the GPU and is not suited to low-end hardware such as integrated graphics (considerLightmapGIinstead). To improve performance, adjustProjectSettings.rendering/global_illumination/voxel_gi/qualityand enableProjectSettings.rendering/global_illumination/gi/use_half_resolutionin the Project Settings. To provide a fallback for low-end hardware, consider adding an option to disableVoxelGIin your project's options menus. AVoxelGInode can be disabled by hiding it.
Note:Meshes should have sufficiently thick walls to avoid light leaks (avoid one-sided walls). For interior levels, enclose your level geometry in a sufficiently large box and bridge the loops to close the mesh. To further prevent light leaks, you can also strategically place temporaryMeshInstance3Dnodes with theirGeometryInstance3D.gi_modeset toGeometryInstance3D.GI_MODE_STATIC. These temporary nodes can then be hidden after baking theVoxelGInode.

## Tutorials
- Using Voxel global illumination
Using Voxel global illumination
- Third Person Shooter (TPS) Demo
Third Person Shooter (TPS) Demo

## Properties

| CameraAttributes | camera_attributes |  |
|---|---|---|
| VoxelGIData | data |  |
| Vector3 | size | Vector3(20,20,20) |
| Subdiv | subdiv | 1 |

CameraAttributes
camera_attributes
VoxelGIData
data
Vector3
size
Vector3(20,20,20)
Subdiv
subdiv

## Methods

| void | bake(from_node:Node= null, create_visual_debug:bool= false) |
|---|---|
| void | debug_bake() |

void
bake(from_node:Node= null, create_visual_debug:bool= false)
void
debug_bake()

## Enumerations
enumSubdiv:🔗
SubdivSUBDIV_64=0
Use 64 subdivisions. This is the lowest quality setting, but the fastest. Use it if you can, but especially use it on lower-end hardware.
SubdivSUBDIV_128=1
Use 128 subdivisions. This is the default quality setting.
SubdivSUBDIV_256=2
Use 256 subdivisions.
SubdivSUBDIV_512=3
Use 512 subdivisions. This is the highest quality setting, but the slowest. On lower-end hardware, this could cause the GPU to stall.
SubdivSUBDIV_MAX=4
Represents the size of theSubdivenum.

## Property Descriptions
CameraAttributescamera_attributes🔗
- voidset_camera_attributes(value:CameraAttributes)
voidset_camera_attributes(value:CameraAttributes)
- CameraAttributesget_camera_attributes()
CameraAttributesget_camera_attributes()
TheCameraAttributesresource that specifies exposure levels to bake at. Auto-exposure and non exposure properties will be ignored. Exposure settings should be used to reduce the dynamic range present when baking. If exposure is too high, theVoxelGIwill have banding artifacts or may have over-exposure artifacts.
VoxelGIDatadata🔗
- voidset_probe_data(value:VoxelGIData)
voidset_probe_data(value:VoxelGIData)
- VoxelGIDataget_probe_data()
VoxelGIDataget_probe_data()
TheVoxelGIDataresource that holds the data for thisVoxelGI.
Vector3size=Vector3(20,20,20)🔗
- voidset_size(value:Vector3)
voidset_size(value:Vector3)
- Vector3get_size()
Vector3get_size()
The size of the area covered by theVoxelGI. This must be1.0or greater on each axis.
Note:If you make the size larger without increasing the number of subdivisions withsubdiv, the size of each cell will increase and result in less detailed lighting.
Subdivsubdiv=1🔗
- voidset_subdiv(value:Subdiv)
voidset_subdiv(value:Subdiv)
- Subdivget_subdiv()
Subdivget_subdiv()
Number of times to subdivide the grid that theVoxelGIoperates on. A higher number results in finer detail and thus higher visual quality, while lower numbers result in better performance.

## Method Descriptions
voidbake(from_node:Node= null, create_visual_debug:bool= false)🔗
Bakes the effect from allGeometryInstance3Ds marked withGeometryInstance3D.GI_MODE_STATICandLight3Ds marked with eitherLight3D.BAKE_STATICorLight3D.BAKE_DYNAMIC. Ifcreate_visual_debugistrue, after baking the light, this will generate aMultiMeshthat has a cube representing each solid cell with each cube colored to the cell's albedo color. This can be used to visualize theVoxelGI's data and debug any issues that may be occurring.
Note:bake()works from the editor and in exported projects. This makes it suitable for procedurally generated or user-built levels. Baking aVoxelGInode generally takes from 5 to 20 seconds in most scenes. Reducingsubdivcan speed up baking.
Note:GeometryInstance3Ds andLight3Ds must be fully ready beforebake()is called. If you are procedurally creating those and some meshes or lights are missing from your bakedVoxelGI, usecall_deferred("bake")instead of callingbake()directly.
voiddebug_bake()🔗
Callsbake()withcreate_visual_debugenabled.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.