:github_url: hide



# GPUParticlesAttractor3D

**Inherits:** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [GPUParticlesAttractorBox3D<class_GPUParticlesAttractorBox3D>], [GPUParticlesAttractorSphere3D<class_GPUParticlesAttractorSphere3D>], [GPUParticlesAttractorVectorField3D<class_GPUParticlesAttractorVectorField3D>]

Abstract base class for 3D particle attractors.


## Description

Particle attractors can be used to attract particles towards the attractor's origin, or to push them away from the attractor's origin.

Particle attractors work in real-time and can be moved, rotated and scaled during gameplay. Unlike collision shapes, non-uniform scaling of attractors is also supported.

Attractors can be temporarily disabled by hiding them, or by setting their [strength<class_GPUParticlesAttractor3D_property_strength>] to `0.0`.

\ **Note:** Particle attractors only affect [GPUParticles3D<class_GPUParticles3D>], not [CPUParticles3D<class_CPUParticles3D>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+------------------------------------------------------------------------------+----------------+
> | :ref:`float<class_float>` | :ref:`attenuation<class_GPUParticlesAttractor3D_property_attenuation>`       | ``1.0``        |
> +---------------------------+------------------------------------------------------------------------------+----------------+
> | :ref:`int<class_int>`     | :ref:`cull_mask<class_GPUParticlesAttractor3D_property_cull_mask>`           | ``4294967295`` |
> +---------------------------+------------------------------------------------------------------------------+----------------+
> | :ref:`float<class_float>` | :ref:`directionality<class_GPUParticlesAttractor3D_property_directionality>` | ``0.0``        |
> +---------------------------+------------------------------------------------------------------------------+----------------+
> | :ref:`float<class_float>` | :ref:`strength<class_GPUParticlesAttractor3D_property_strength>`             | ``1.0``        |
> +---------------------------+------------------------------------------------------------------------------+----------------+
>

----


## Property Descriptions



[float<class_float>] **attenuation** = `1.0` [🔗<class_GPUParticlesAttractor3D_property_attenuation>]


- |void| **set_attenuation**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_attenuation**\ (\ )

The particle attractor's attenuation. Higher values result in more gradual pushing of particles as they come closer to the attractor's origin. Zero or negative values will cause particles to be pushed very fast as soon as the touch the attractor's edges.


----



[int<class_int>] **cull_mask** = `4294967295` [🔗<class_GPUParticlesAttractor3D_property_cull_mask>]


- |void| **set_cull_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_cull_mask**\ (\ )

The particle rendering layers ([VisualInstance3D.layers<class_VisualInstance3D_property_layers>]) that will be affected by the attractor. By default, all particles are affected by an attractor.

After configuring particle nodes accordingly, specific layers can be unchecked to prevent certain particles from being affected by attractors. For example, this can be used if you're using an attractor as part of a spell effect but don't want the attractor to affect unrelated weather particles at the same position.

Particle attraction can also be disabled on a per-process material basis by setting [ParticleProcessMaterial.attractor_interaction_enabled<class_ParticleProcessMaterial_property_attractor_interaction_enabled>] on the [GPUParticles3D<class_GPUParticles3D>] node.


----



[float<class_float>] **directionality** = `0.0` [🔗<class_GPUParticlesAttractor3D_property_directionality>]


- |void| **set_directionality**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_directionality**\ (\ )

Adjusts how directional the attractor is. At `0.0`, the attractor is not directional at all: it will attract particles towards its center. At `1.0`, the attractor is fully directional: particles will always be pushed towards local -Z (or +Z if [strength<class_GPUParticlesAttractor3D_property_strength>] is negative).

\ **Note:** If [directionality<class_GPUParticlesAttractor3D_property_directionality>] is greater than `0.0`, the direction in which particles are pushed can be changed by rotating the **GPUParticlesAttractor3D** node.


----



[float<class_float>] **strength** = `1.0` [🔗<class_GPUParticlesAttractor3D_property_strength>]


- |void| **set_strength**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_strength**\ (\ )

Adjusts the strength of the attractor. If [strength<class_GPUParticlesAttractor3D_property_strength>] is negative, particles will be pushed in the opposite direction. Particles will be pushed *away* from the attractor's origin if [directionality<class_GPUParticlesAttractor3D_property_directionality>] is `0.0`, or towards local +Z if [directionality<class_GPUParticlesAttractor3D_property_directionality>] is greater than `0.0`.

