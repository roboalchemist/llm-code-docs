# GPUParticlesCollisionSDF3D in English

# GPUParticlesCollisionSDF3D
Inherits:GPUParticlesCollision3D<VisualInstance3D<Node3D<Node<Object
A baked signed distance field 3D particle collision shape affectingGPUParticles3Dnodes.

## Description
A baked signed distance field 3D particle collision shape affectingGPUParticles3Dnodes.
Signed distance fields (SDF) allow for efficiently representing approximate collision shapes for convex and concave objects of any shape. This is more flexible thanGPUParticlesCollisionHeightField3D, but it requires a baking step.
Baking:The signed distance field texture can be baked by selecting theGPUParticlesCollisionSDF3Dnode in the editor, then clickingBake SDFat the top of the 3D viewport. AnyvisibleMeshInstance3Ds within thesizewill be taken into account for baking, regardless of theirGeometryInstance3D.gi_mode.
Note:Baking aGPUParticlesCollisionSDF3D'stextureis only possible within the editor, as there is no bake method exposed for use in exported projects. However, it's still possible to load pre-bakedTexture3Ds into itstextureproperty in an exported project.
Note:ParticleProcessMaterial.collision_modemust beParticleProcessMaterial.COLLISION_RIGIDorParticleProcessMaterial.COLLISION_HIDE_ON_CONTACTon theGPUParticles3D's process material for collision to work.
Note:Particle collision only affectsGPUParticles3D, notCPUParticles3D.

## Properties

| int | bake_mask | 4294967295 |
|---|---|---|
| Resolution | resolution | 2 |
| Vector3 | size | Vector3(2,2,2) |
| Texture3D | texture |  |
| float | thickness | 1.0 |

bake_mask
4294967295
Resolution
resolution
Vector3
size
Vector3(2,2,2)
Texture3D
texture
float
thickness

## Methods

| bool | get_bake_mask_value(layer_number:int)const |
|---|---|
| void | set_bake_mask_value(layer_number:int, value:bool) |

bool
get_bake_mask_value(layer_number:int)const
void
set_bake_mask_value(layer_number:int, value:bool)

## Enumerations
enumResolution:🔗
ResolutionRESOLUTION_16=0
Bake a 16×16×16 signed distance field. This is the fastest option, but also the least precise.
ResolutionRESOLUTION_32=1
Bake a 32×32×32 signed distance field.
ResolutionRESOLUTION_64=2
Bake a 64×64×64 signed distance field.
ResolutionRESOLUTION_128=3
Bake a 128×128×128 signed distance field.
ResolutionRESOLUTION_256=4
Bake a 256×256×256 signed distance field.
ResolutionRESOLUTION_512=5
Bake a 512×512×512 signed distance field. This is the slowest option, but also the most precise.
ResolutionRESOLUTION_MAX=6
Represents the size of theResolutionenum.

## Property Descriptions
intbake_mask=4294967295🔗
- voidset_bake_mask(value:int)
voidset_bake_mask(value:int)
- intget_bake_mask()
intget_bake_mask()
The visual layers to account for when baking the particle collision SDF. OnlyMeshInstance3Ds whoseVisualInstance3D.layersmatch with thisbake_maskwill be included in the generated particle collision SDF. By default, all objects are taken into account for the particle collision SDF baking.
Resolutionresolution=2🔗
- voidset_resolution(value:Resolution)
voidset_resolution(value:Resolution)
- Resolutionget_resolution()
Resolutionget_resolution()
The bake resolution to use for the signed distance fieldtexture. The texture must be baked again for changes to theresolutionproperty to be effective. Higher resolutions have a greater performance cost and take more time to bake. Higher resolutions also result in larger baked textures, leading to increased VRAM and storage space requirements. To improve performance and reduce bake times, use the lowest resolution possible for the object you're representing the collision of.
Vector3size=Vector3(2,2,2)🔗
- voidset_size(value:Vector3)
voidset_size(value:Vector3)
- Vector3get_size()
Vector3get_size()
The collision SDF's size in 3D units. To improve SDF quality, thesizeshould be set as small as possible while covering the parts of the scene you need.
Texture3Dtexture🔗
- voidset_texture(value:Texture3D)
voidset_texture(value:Texture3D)
- Texture3Dget_texture()
Texture3Dget_texture()
The 3D texture representing the signed distance field.
floatthickness=1.0🔗
- voidset_thickness(value:float)
voidset_thickness(value:float)
- floatget_thickness()
floatget_thickness()
The collision shape's thickness. Unlike other particle colliders,GPUParticlesCollisionSDF3Dis actually hollow on the inside.thicknesscan be increased to prevent particles from tunneling through the collision shape at high speeds, or when theGPUParticlesCollisionSDF3Dis moved.

## Method Descriptions
boolget_bake_mask_value(layer_number:int)const🔗
Returns whether or not the specified layer of thebake_maskis enabled, given alayer_numberbetween 1 and 32.
voidset_bake_mask_value(layer_number:int, value:bool)🔗
Based onvalue, enables or disables the specified layer in thebake_mask, given alayer_numberbetween 1 and 32.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.