# FogMaterial

# FogMaterial

Inherits:Material<Resource<RefCounted<Object
A material that controls how volumetric fog is rendered, to be assigned to aFogVolume.

## Description

AMaterialresource that can be used byFogVolumes to draw volumetric effects.
If you need more advanced effects, use a customfog shader.

## Properties

| Color | albedo | Color(1,1,1,1) |
|---|---|---|
| float | density | 1.0 |
| Texture3D | density_texture |  |
| float | edge_fade | 0.1 |
| Color | emission | Color(0,0,0,1) |
| float | height_falloff | 0.0 |

Color
albedo
Color(1,1,1,1)
float
density
Texture3D
density_texture
float
edge_fade
Color
emission
Color(0,0,0,1)
float
height_falloff

## Property Descriptions

Coloralbedo=Color(1,1,1,1)🔗

- voidset_albedo(value:Color)
voidset_albedo(value:Color)
- Colorget_albedo()
Colorget_albedo()
The single-scatteringColorof theFogVolume. Internally,albedois converted into single-scattering, which is additively blended with otherFogVolumes and theEnvironment.volumetric_fog_albedo.
floatdensity=1.0🔗
- voidset_density(value:float)
voidset_density(value:float)
- floatget_density()
floatget_density()
The density of theFogVolume. Denser objects are more opaque, but may suffer from under-sampling artifacts that look like stripes. Negative values can be used to subtract fog from otherFogVolumes or global volumetric fog.
Note:Due to limited precision,densityvalues between-0.001and0.001(exclusive) act like0.0. This does not apply toEnvironment.volumetric_fog_density.
Texture3Ddensity_texture🔗
- voidset_density_texture(value:Texture3D)
voidset_density_texture(value:Texture3D)
- Texture3Dget_density_texture()
Texture3Dget_density_texture()
The 3D texture that is used to scale thedensityof theFogVolume. This can be used to vary fog density within theFogVolumewith any kind of static pattern. For animated effects, consider using a customfog shader.
floatedge_fade=0.1🔗
- voidset_edge_fade(value:float)
voidset_edge_fade(value:float)
- floatget_edge_fade()
floatget_edge_fade()
The hardness of the edges of theFogVolume. A higher value will result in softer edges, while a lower value will result in harder edges.
Coloremission=Color(0,0,0,1)🔗
- voidset_emission(value:Color)
voidset_emission(value:Color)
- Colorget_emission()
Colorget_emission()
TheColorof the light emitted by theFogVolume. Emitted light will not cast light or shadows on other objects, but can be useful for modulating theColorof theFogVolumeindependently from light sources.
floatheight_falloff=0.0🔗
- voidset_height_falloff(value:float)
voidset_height_falloff(value:float)
- floatget_height_falloff()
floatget_height_falloff()
The rate by which the height-based fog decreases in density as height increases in world space. A high falloff will result in a sharp transition, while a low falloff will result in a smoother transition. A value of0.0results in uniform-density fog. The height threshold is determined by the height of the associatedFogVolume.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
