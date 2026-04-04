:github_url: hide



# VisualShaderNodeParticleEmitter

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [VisualShaderNodeParticleBoxEmitter<class_VisualShaderNodeParticleBoxEmitter>], [VisualShaderNodeParticleMeshEmitter<class_VisualShaderNodeParticleMeshEmitter>], [VisualShaderNodeParticleRingEmitter<class_VisualShaderNodeParticleRingEmitter>], [VisualShaderNodeParticleSphereEmitter<class_VisualShaderNodeParticleSphereEmitter>]

A base class for particle emitters.


## Description

Particle emitter nodes can be used in "start" step of particle shaders and they define the starting position of the particles. Connect them to the Position output port.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>` | :ref:`mode_2d<class_VisualShaderNodeParticleEmitter_property_mode_2d>` | ``false`` |
> +-------------------------+------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[bool<class_bool>] **mode_2d** = `false` [🔗<class_VisualShaderNodeParticleEmitter_property_mode_2d>]


- |void| **set_mode_2d**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_mode_2d**\ (\ )

If `true`, the result of this emitter is projected to 2D space. By default it is `false` and meant for use in 3D space.

