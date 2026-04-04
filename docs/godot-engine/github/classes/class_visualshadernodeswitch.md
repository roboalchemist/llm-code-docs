:github_url: hide



# VisualShaderNodeSwitch

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A selector function for use within the visual shader graph.


## Description

Returns an associated value of the [op_type<class_VisualShaderNodeSwitch_property_op_type>] type if the provided boolean value is `true` or `false`.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+---------------------------------------------------------------+-------+
> | :ref:`OpType<enum_VisualShaderNodeSwitch_OpType>` | :ref:`op_type<class_VisualShaderNodeSwitch_property_op_type>` | ``0`` |
> +---------------------------------------------------+---------------------------------------------------------------+-------+
>

----


## Enumerations



enum **OpType**: [🔗<enum_VisualShaderNodeSwitch_OpType>]



[OpType<enum_VisualShaderNodeSwitch_OpType>] **OP_TYPE_FLOAT** = `0`

A floating-point scalar.



[OpType<enum_VisualShaderNodeSwitch_OpType>] **OP_TYPE_INT** = `1`

An integer scalar.



[OpType<enum_VisualShaderNodeSwitch_OpType>] **OP_TYPE_UINT** = `2`

An unsigned integer scalar.



[OpType<enum_VisualShaderNodeSwitch_OpType>] **OP_TYPE_VECTOR_2D** = `3`

A 2D vector type.



[OpType<enum_VisualShaderNodeSwitch_OpType>] **OP_TYPE_VECTOR_3D** = `4`

A 3D vector type.



[OpType<enum_VisualShaderNodeSwitch_OpType>] **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.



[OpType<enum_VisualShaderNodeSwitch_OpType>] **OP_TYPE_BOOLEAN** = `6`

A boolean type.



[OpType<enum_VisualShaderNodeSwitch_OpType>] **OP_TYPE_TRANSFORM** = `7`

A transform type.



[OpType<enum_VisualShaderNodeSwitch_OpType>] **OP_TYPE_MAX** = `8`

Represents the size of the [OpType<enum_VisualShaderNodeSwitch_OpType>] enum.


----


## Property Descriptions



[OpType<enum_VisualShaderNodeSwitch_OpType>] **op_type** = `0` [🔗<class_VisualShaderNodeSwitch_property_op_type>]


- |void| **set_op_type**\ (\ value\: [OpType<enum_VisualShaderNodeSwitch_OpType>]\ )
- [OpType<enum_VisualShaderNodeSwitch_OpType>] **get_op_type**\ (\ )

A type of operands and returned value.

