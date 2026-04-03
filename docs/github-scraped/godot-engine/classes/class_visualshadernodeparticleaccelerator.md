:github_url: hide



# VisualShaderNodeParticleAccelerator

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A visual shader node that accelerates particles.


## Description

Particle accelerator can be used in "process" step of particle shader. It will accelerate the particles. Connect it to the Velocity output port.


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------+----------------------------------------------------------------------+-------+
> | :ref:`Mode<enum_VisualShaderNodeParticleAccelerator_Mode>` | :ref:`mode<class_VisualShaderNodeParticleAccelerator_property_mode>` | ``0`` |
> +------------------------------------------------------------+----------------------------------------------------------------------+-------+
>

----


## Enumerations



enum **Mode**: [🔗<enum_VisualShaderNodeParticleAccelerator_Mode>]



[Mode<enum_VisualShaderNodeParticleAccelerator_Mode>] **MODE_LINEAR** = `0`

The particles will be accelerated based on their velocity.



[Mode<enum_VisualShaderNodeParticleAccelerator_Mode>] **MODE_RADIAL** = `1`

The particles will be accelerated towards or away from the center.



[Mode<enum_VisualShaderNodeParticleAccelerator_Mode>] **MODE_TANGENTIAL** = `2`

The particles will be accelerated tangentially to the radius vector from center to their position.



[Mode<enum_VisualShaderNodeParticleAccelerator_Mode>] **MODE_MAX** = `3`

Represents the size of the [Mode<enum_VisualShaderNodeParticleAccelerator_Mode>] enum.


----


## Property Descriptions



[Mode<enum_VisualShaderNodeParticleAccelerator_Mode>] **mode** = `0` [🔗<class_VisualShaderNodeParticleAccelerator_property_mode>]


- |void| **set_mode**\ (\ value\: [Mode<enum_VisualShaderNodeParticleAccelerator_Mode>]\ )
- [Mode<enum_VisualShaderNodeParticleAccelerator_Mode>] **get_mode**\ (\ )

Defines in what manner the particles will be accelerated.

