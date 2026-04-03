# MultiMesh in English

# MultiMesh
Inherits:Resource<RefCounted<Object
Provides high-performance drawing of a mesh multiple times using GPU instancing.

## Description
MultiMesh provides low-level mesh instancing. Drawing thousands ofMeshInstance3Dnodes can be slow, since each object is submitted to the GPU then drawn individually.
MultiMesh is much faster as it can draw thousands of instances with a single draw call, resulting in less API overhead.
As a drawback, if the instances are too far away from each other, performance may be reduced as every single instance will always render (they are spatially indexed as one, for the whole object).
Since instances may have any behavior, the AABB used for visibility must be provided by the user.
Note:A MultiMesh is a single object, therefore the same maximum lights per object restriction applies. This means, that once the maximum lights are consumed by one or more instances, the rest of the MultiMesh instances willnotreceive any lighting.
Note:Blend Shapes will be ignored if used in a MultiMesh.

## Tutorials
- Using MultiMeshInstance
Using MultiMeshInstance
- Optimization using MultiMeshes
Optimization using MultiMeshes
- Animating thousands of fish with MultiMeshInstance
Animating thousands of fish with MultiMeshInstance

## Properties

| PackedFloat32Array | buffer | PackedFloat32Array() |
|---|---|---|
| PackedColorArray | color_array |  |
| AABB | custom_aabb | AABB(0,0,0,0,0,0) |
| PackedColorArray | custom_data_array |  |
| int | instance_count | 0 |
| Mesh | mesh |  |
| PhysicsInterpolationQuality | physics_interpolation_quality | 0 |
| PackedVector2Array | transform_2d_array |  |
| PackedVector3Array | transform_array |  |
| TransformFormat | transform_format | 0 |
| bool | use_colors | false |
| bool | use_custom_data | false |
| int | visible_instance_count | -1 |

PackedFloat32Array
buffer
PackedFloat32Array()
PackedColorArray
color_array
AABB
custom_aabb
AABB(0,0,0,0,0,0)
PackedColorArray
custom_data_array
instance_count
Mesh
mesh
PhysicsInterpolationQuality
physics_interpolation_quality
PackedVector2Array
transform_2d_array
PackedVector3Array
transform_array
TransformFormat
transform_format
bool
use_colors
false
bool
use_custom_data
false
visible_instance_count

## Methods

| AABB | get_aabb()const |
|---|---|
| Color | get_instance_color(instance:int)const |
| Color | get_instance_custom_data(instance:int)const |
| Transform3D | get_instance_transform(instance:int)const |
| Transform2D | get_instance_transform_2d(instance:int)const |
| void | reset_instance_physics_interpolation(instance:int) |
| void | reset_instances_physics_interpolation() |
| void | set_buffer_interpolated(buffer_curr:PackedFloat32Array, buffer_prev:PackedFloat32Array) |
| void | set_instance_color(instance:int, color:Color) |
| void | set_instance_custom_data(instance:int, custom_data:Color) |
| void | set_instance_transform(instance:int, transform:Transform3D) |
| void | set_instance_transform_2d(instance:int, transform:Transform2D) |

AABB
get_aabb()const
Color
get_instance_color(instance:int)const
Color
get_instance_custom_data(instance:int)const
Transform3D
get_instance_transform(instance:int)const
Transform2D
get_instance_transform_2d(instance:int)const
void
reset_instance_physics_interpolation(instance:int)
void
reset_instances_physics_interpolation()
void
set_buffer_interpolated(buffer_curr:PackedFloat32Array, buffer_prev:PackedFloat32Array)
void
set_instance_color(instance:int, color:Color)
void
set_instance_custom_data(instance:int, custom_data:Color)
void
set_instance_transform(instance:int, transform:Transform3D)
void
set_instance_transform_2d(instance:int, transform:Transform2D)

## Enumerations
enumTransformFormat:🔗
TransformFormatTRANSFORM_2D=0
Use this when using 2D transforms.
TransformFormatTRANSFORM_3D=1
Use this when using 3D transforms.
enumPhysicsInterpolationQuality:🔗
PhysicsInterpolationQualityINTERP_QUALITY_FAST=0
Always interpolate using Basis lerping, which can produce warping artifacts in some situations.
PhysicsInterpolationQualityINTERP_QUALITY_HIGH=1
Attempt to interpolate using Basis slerping (spherical linear interpolation) where possible, otherwise fall back to lerping.

## Property Descriptions
PackedFloat32Arraybuffer=PackedFloat32Array()🔗
- voidset_buffer(value:PackedFloat32Array)
voidset_buffer(value:PackedFloat32Array)
- PackedFloat32Arrayget_buffer()
PackedFloat32Arrayget_buffer()
There is currently no description for this property. Please help us bycontributing one!
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedFloat32Arrayfor more details.
PackedColorArraycolor_array🔗
Deprecated:Accessing this property is very slow. Useset_instance_color()andget_instance_color()instead.
Array containing eachColorused by all instances of this mesh.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedColorArrayfor more details.
AABBcustom_aabb=AABB(0,0,0,0,0,0)🔗
- voidset_custom_aabb(value:AABB)
voidset_custom_aabb(value:AABB)
- AABBget_custom_aabb()
AABBget_custom_aabb()
Custom AABB for this MultiMesh resource. Setting this manually prevents costly runtime AABB recalculations.
PackedColorArraycustom_data_array🔗
Deprecated:Accessing this property is very slow. Useset_instance_custom_data()andget_instance_custom_data()instead.
Array containing each custom data value used by all instances of this mesh, as aPackedColorArray.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedColorArrayfor more details.
intinstance_count=0🔗
- voidset_instance_count(value:int)
voidset_instance_count(value:int)
- intget_instance_count()
intget_instance_count()
Number of instances that will get drawn. This clears and (re)sizes the buffers. Setting data format or flags afterwards will have no effect.
By default, all instances are drawn but you can limit this withvisible_instance_count.
Meshmesh🔗
- voidset_mesh(value:Mesh)
voidset_mesh(value:Mesh)
- Meshget_mesh()
Meshget_mesh()
Meshresource to be instanced.
The looks of the individual instances can be modified usingset_instance_color()andset_instance_custom_data().
PhysicsInterpolationQualityphysics_interpolation_quality=0🔗
- voidset_physics_interpolation_quality(value:PhysicsInterpolationQuality)
voidset_physics_interpolation_quality(value:PhysicsInterpolationQuality)
- PhysicsInterpolationQualityget_physics_interpolation_quality()
PhysicsInterpolationQualityget_physics_interpolation_quality()
Choose whether to use an interpolation method that favors speed or quality.
When using low physics tick rates (typically below 20) or high rates of object rotation, you may get better results from the high quality setting.
Note:Fast quality does not equate to low quality. Except in the special cases mentioned above, the quality should be comparable to high quality.
PackedVector2Arraytransform_2d_array🔗
Deprecated:Accessing this property is very slow. Useset_instance_transform_2d()andget_instance_transform_2d()instead.
Array containing eachTransform2Dvalue used by all instances of this mesh, as aPackedVector2Array. Each transform is divided into 3Vector2values corresponding to the transforms'x,y, andorigin.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedVector2Arrayfor more details.
PackedVector3Arraytransform_array🔗
Deprecated:Accessing this property is very slow. Useset_instance_transform()andget_instance_transform()instead.
Array containing eachTransform3Dvalue used by all instances of this mesh, as aPackedVector3Array. Each transform is divided into 4Vector3values corresponding to the transforms'x,y,z, andorigin.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedVector3Arrayfor more details.
TransformFormattransform_format=0🔗
- voidset_transform_format(value:TransformFormat)
voidset_transform_format(value:TransformFormat)
- TransformFormatget_transform_format()
TransformFormatget_transform_format()
Format of transform used to transform mesh, either 2D or 3D.
booluse_colors=false🔗
- voidset_use_colors(value:bool)
voidset_use_colors(value:bool)
- boolis_using_colors()
boolis_using_colors()
Iftrue, theMultiMeshwill use color data (seeset_instance_color()). Can only be set wheninstance_countis0or less. This means that you need to call this method before setting the instance count, or temporarily reset it to0.
booluse_custom_data=false🔗
- voidset_use_custom_data(value:bool)
voidset_use_custom_data(value:bool)
- boolis_using_custom_data()
boolis_using_custom_data()
Iftrue, theMultiMeshwill use custom data (seeset_instance_custom_data()). Can only be set wheninstance_countis0or less. This means that you need to call this method before setting the instance count, or temporarily reset it to0.
intvisible_instance_count=-1🔗
- voidset_visible_instance_count(value:int)
voidset_visible_instance_count(value:int)
- intget_visible_instance_count()
intget_visible_instance_count()
Limits the number of instances drawn, -1 draws all instances. Changing this does not change the sizes of the buffers.

## Method Descriptions
AABBget_aabb()const🔗
Returns the visibility axis-aligned bounding box in local space.
Colorget_instance_color(instance:int)const🔗
Gets a specific instance's color multiplier.
Colorget_instance_custom_data(instance:int)const🔗
Returns the custom data that has been set for a specific instance.
Transform3Dget_instance_transform(instance:int)const🔗
Returns theTransform3Dof a specific instance.
Transform2Dget_instance_transform_2d(instance:int)const🔗
Returns theTransform2Dof a specific instance.
voidreset_instance_physics_interpolation(instance:int)🔗
When usingphysics interpolation, this function allows you to prevent interpolation on an instance in the current physics tick.
This allows you to move instances instantaneously, and should usually be used when initially placing an instance such as a bullet to prevent graphical glitches.
voidreset_instances_physics_interpolation()🔗
When usingphysics interpolation, this function allows you to prevent interpolation for all instances in the current physics tick.
This allows you to move all instances instantaneously, and should usually be used when initially placing instances to prevent graphical glitches.
voidset_buffer_interpolated(buffer_curr:PackedFloat32Array, buffer_prev:PackedFloat32Array)🔗
An alternative to setting thebufferproperty, which can be used withphysics interpolation. This method takes two arrays, and can set the data for the current and previous tick in one go. The renderer will automatically interpolate the data at each frame.
This is useful for situations where the order of instances may change from physics tick to tick, such as particle systems.
When the order of instances is coherent, the simpler alternative of settingbuffercan still be used with interpolation.
voidset_instance_color(instance:int, color:Color)🔗
Sets the color of a specific instance bymultiplyingthe mesh's existing vertex colors. This allows for different color tinting per instance.
Note:Each component is stored in 32 bits in the Forward+ and Mobile rendering methods, but is packed into 16 bits in the Compatibility rendering method.
For the color to take effect, ensure thatuse_colorsistrueon theMultiMeshandBaseMaterial3D.vertex_color_use_as_albedoistrueon the material. If you intend to set an absolute color instead of tinting, make sure the material's albedo color is set to pure white (Color(1,1,1)).
voidset_instance_custom_data(instance:int, custom_data:Color)🔗
Sets custom data for a specific instance.custom_datais aColortype only to contain 4 floating-point numbers.
Note:Each number is stored in 32 bits in the Forward+ and Mobile rendering methods, but is packed into 16 bits in the Compatibility rendering method.
For the custom data to be used, ensure thatuse_custom_dataistrue.
This custom instance data has to be manually accessed in your custom shader usingINSTANCE_CUSTOM.
voidset_instance_transform(instance:int, transform:Transform3D)🔗
Sets theTransform3Dfor a specific instance.
voidset_instance_transform_2d(instance:int, transform:Transform2D)🔗
Sets theTransform2Dfor a specific instance.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.