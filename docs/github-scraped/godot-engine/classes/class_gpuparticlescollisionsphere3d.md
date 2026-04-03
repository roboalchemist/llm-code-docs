:github_url: hide



# GPUParticlesCollisionSphere3D

**Inherits:** [GPUParticlesCollision3D<class_GPUParticlesCollision3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A sphere-shaped 3D particle collision shape affecting [GPUParticles3D<class_GPUParticles3D>] nodes.


## Description

A sphere-shaped 3D particle collision shape affecting [GPUParticles3D<class_GPUParticles3D>] nodes.

Particle collision shapes work in real-time and can be moved, rotated and scaled during gameplay. Unlike attractors, non-uniform scaling of collision shapes is *not* supported.

\ **Note:** [ParticleProcessMaterial.collision_mode<class_ParticleProcessMaterial_property_collision_mode>] must be [ParticleProcessMaterial.COLLISION_RIGID<class_ParticleProcessMaterial_constant_COLLISION_RIGID>] or [ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT<class_ParticleProcessMaterial_constant_COLLISION_HIDE_ON_CONTACT>] on the [GPUParticles3D<class_GPUParticles3D>]'s process material for collision to work.

\ **Note:** Particle collision only affects [GPUParticles3D<class_GPUParticles3D>], not [CPUParticles3D<class_CPUParticles3D>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+--------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`radius<class_GPUParticlesCollisionSphere3D_property_radius>` | ``1.0`` |
> +---------------------------+--------------------------------------------------------------------+---------+
>

----


## Property Descriptions



[float<class_float>] **radius** = `1.0` [🔗<class_GPUParticlesCollisionSphere3D_property_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

The collision sphere's radius in 3D units.

