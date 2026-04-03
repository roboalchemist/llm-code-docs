:github_url: hide



# VisualShaderNodeParticleRandomness

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Visual shader node for randomizing particle values.


## Description

Randomness node will output pseudo-random values of the given type based on the specified minimum and maximum values.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------+---------------------------------------------------------------------------+-------+
> | :ref:`OpType<enum_VisualShaderNodeParticleRandomness_OpType>` | :ref:`op_type<class_VisualShaderNodeParticleRandomness_property_op_type>` | ``0`` |
> +---------------------------------------------------------------+---------------------------------------------------------------------------+-------+
>

----


## Enumerations



enum **OpType**: [🔗<enum_VisualShaderNodeParticleRandomness_OpType>]



[OpType<enum_VisualShaderNodeParticleRandomness_OpType>] **OP_TYPE_SCALAR** = `0`

A floating-point scalar.



[OpType<enum_VisualShaderNodeParticleRandomness_OpType>] **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.



[OpType<enum_VisualShaderNodeParticleRandomness_OpType>] **OP_TYPE_VECTOR_3D** = `2`

A 3D vector type.



[OpType<enum_VisualShaderNodeParticleRandomness_OpType>] **OP_TYPE_VECTOR_4D** = `3`

A 4D vector type.



[OpType<enum_VisualShaderNodeParticleRandomness_OpType>] **OP_TYPE_MAX** = `4`

Represents the size of the [OpType<enum_VisualShaderNodeParticleRandomness_OpType>] enum.


----


## Property Descriptions



[OpType<enum_VisualShaderNodeParticleRandomness_OpType>] **op_type** = `0` [🔗<class_VisualShaderNodeParticleRandomness_property_op_type>]


- |void| **set_op_type**\ (\ value\: [OpType<enum_VisualShaderNodeParticleRandomness_OpType>]\ )
- [OpType<enum_VisualShaderNodeParticleRandomness_OpType>] **get_op_type**\ (\ )

A type of operands and returned value.

