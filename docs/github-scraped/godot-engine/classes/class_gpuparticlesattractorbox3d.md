:github_url: hide



# GPUParticlesAttractorBox3D

**Inherits:** [GPUParticlesAttractor3D<class_GPUParticlesAttractor3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A box-shaped attractor that influences particles from [GPUParticles3D<class_GPUParticles3D>] nodes.


## Description

A box-shaped attractor that influences particles from [GPUParticles3D<class_GPUParticles3D>] nodes. Can be used to attract particles towards its origin, or to push them away from its origin.

Particle attractors work in real-time and can be moved, rotated and scaled during gameplay. Unlike collision shapes, non-uniform scaling of attractors is also supported.

\ **Note:** Particle attractors only affect [GPUParticles3D<class_GPUParticles3D>], not [CPUParticles3D<class_CPUParticles3D>].


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+-------------------------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`size<class_GPUParticlesAttractorBox3D_property_size>` | ``Vector3(2, 2, 2)`` |
> +-------------------------------+-------------------------------------------------------------+----------------------+
>

----


## Property Descriptions



[Vector3<class_Vector3>] **size** = `Vector3(2, 2, 2)` [🔗<class_GPUParticlesAttractorBox3D_property_size>]


- |void| **set_size**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_size**\ (\ )

The attractor box's size in 3D units.

