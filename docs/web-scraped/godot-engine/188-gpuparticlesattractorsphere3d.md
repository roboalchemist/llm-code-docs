# GPUParticlesAttractorSphere3D

# GPUParticlesAttractorSphere3D

Inherits:GPUParticlesAttractor3D<VisualInstance3D<Node3D<Node<Object
A spheroid-shaped attractor that influences particles fromGPUParticles3Dnodes.

## Description

A spheroid-shaped attractor that influences particles fromGPUParticles3Dnodes. Can be used to attract particles towards its origin, or to push them away from its origin.
Particle attractors work in real-time and can be moved, rotated and scaled during gameplay. Unlike collision shapes, non-uniform scaling of attractors is also supported.
Note:Particle attractors only affectGPUParticles3D, notCPUParticles3D.

## Properties

| float | radius | 1.0 |

float
radius

## Property Descriptions

floatradius=1.0🔗

- voidset_radius(value:float)
voidset_radius(value:float)
- floatget_radius()
floatget_radius()
The attractor sphere's radius in 3D units.
Note:Stretched ellipses can be obtained by using non-uniform scaling on theGPUParticlesAttractorSphere3Dnode.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
