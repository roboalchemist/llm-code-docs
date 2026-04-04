# GPUParticlesAttractor3D

# GPUParticlesAttractor3D
Inherits:VisualInstance3D<Node3D<Node<Object
Inherited By:GPUParticlesAttractorBox3D,GPUParticlesAttractorSphere3D,GPUParticlesAttractorVectorField3D
Abstract base class for 3D particle attractors.

## Description
Particle attractors can be used to attract particles towards the attractor's origin, or to push them away from the attractor's origin.
Particle attractors work in real-time and can be moved, rotated and scaled during gameplay. Unlike collision shapes, non-uniform scaling of attractors is also supported.
Attractors can be temporarily disabled by hiding them, or by setting theirstrengthto0.0.
Note:Particle attractors only affectGPUParticles3D, notCPUParticles3D.

## Properties

| float | attenuation | 1.0 |
|---|---|---|
| int | cull_mask | 4294967295 |
| float | directionality | 0.0 |
| float | strength | 1.0 |

float
attenuation
cull_mask
4294967295
float
directionality
float
strength

## Property Descriptions
floatattenuation=1.0🔗
- voidset_attenuation(value:float)
voidset_attenuation(value:float)
- floatget_attenuation()
floatget_attenuation()
The particle attractor's attenuation. Higher values result in more gradual pushing of particles as they come closer to the attractor's origin. Zero or negative values will cause particles to be pushed very fast as soon as the touch the attractor's edges.
intcull_mask=4294967295🔗
- voidset_cull_mask(value:int)
voidset_cull_mask(value:int)
- intget_cull_mask()
intget_cull_mask()
The particle rendering layers (VisualInstance3D.layers) that will be affected by the attractor. By default, all particles are affected by an attractor.
After configuring particle nodes accordingly, specific layers can be unchecked to prevent certain particles from being affected by attractors. For example, this can be used if you're using an attractor as part of a spell effect but don't want the attractor to affect unrelated weather particles at the same position.
Particle attraction can also be disabled on a per-process material basis by settingParticleProcessMaterial.attractor_interaction_enabledon theGPUParticles3Dnode.
floatdirectionality=0.0🔗
- voidset_directionality(value:float)
voidset_directionality(value:float)
- floatget_directionality()
floatget_directionality()
Adjusts how directional the attractor is. At0.0, the attractor is not directional at all: it will attract particles towards its center. At1.0, the attractor is fully directional: particles will always be pushed towards local -Z (or +Z ifstrengthis negative).
Note:Ifdirectionalityis greater than0.0, the direction in which particles are pushed can be changed by rotating theGPUParticlesAttractor3Dnode.
floatstrength=1.0🔗
- voidset_strength(value:float)
voidset_strength(value:float)
- floatget_strength()
floatget_strength()
Adjusts the strength of the attractor. Ifstrengthis negative, particles will be pushed in the opposite direction. Particles will be pushedawayfrom the attractor's origin ifdirectionalityis0.0, or towards local +Z ifdirectionalityis greater than0.0.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.