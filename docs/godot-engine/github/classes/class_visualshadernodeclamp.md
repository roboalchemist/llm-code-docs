:github_url: hide



# VisualShaderNodeClamp

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Clamps a value within the visual shader graph.


## Description

Constrains a value to lie between `min` and `max` values.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------+--------------------------------------------------------------+-------+
> | :ref:`OpType<enum_VisualShaderNodeClamp_OpType>` | :ref:`op_type<class_VisualShaderNodeClamp_property_op_type>` | ``0`` |
> +--------------------------------------------------+--------------------------------------------------------------+-------+
>

----


## Enumerations



enum **OpType**: [🔗<enum_VisualShaderNodeClamp_OpType>]



[OpType<enum_VisualShaderNodeClamp_OpType>] **OP_TYPE_FLOAT** = `0`

A floating-point scalar.



[OpType<enum_VisualShaderNodeClamp_OpType>] **OP_TYPE_INT** = `1`

An integer scalar.



[OpType<enum_VisualShaderNodeClamp_OpType>] **OP_TYPE_UINT** = `2`

An unsigned integer scalar.



[OpType<enum_VisualShaderNodeClamp_OpType>] **OP_TYPE_VECTOR_2D** = `3`

A 2D vector type.



[OpType<enum_VisualShaderNodeClamp_OpType>] **OP_TYPE_VECTOR_3D** = `4`

A 3D vector type.



[OpType<enum_VisualShaderNodeClamp_OpType>] **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.



[OpType<enum_VisualShaderNodeClamp_OpType>] **OP_TYPE_MAX** = `6`

Represents the size of the [OpType<enum_VisualShaderNodeClamp_OpType>] enum.


----


## Property Descriptions



[OpType<enum_VisualShaderNodeClamp_OpType>] **op_type** = `0` [🔗<class_VisualShaderNodeClamp_property_op_type>]


- |void| **set_op_type**\ (\ value\: [OpType<enum_VisualShaderNodeClamp_OpType>]\ )
- [OpType<enum_VisualShaderNodeClamp_OpType>] **get_op_type**\ (\ )

A type of operands and returned value.

