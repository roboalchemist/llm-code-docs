:github_url: hide



# VisualShaderNodeRemap

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A visual shader node for remap function.


## Description

Remap will transform the input range into output range, e.g. you can change a `0..1` value to `-2..2` etc. See [@GlobalScope.remap()<class_@GlobalScope_method_remap>] for more details.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------+--------------------------------------------------------------+-------+
> | :ref:`OpType<enum_VisualShaderNodeRemap_OpType>` | :ref:`op_type<class_VisualShaderNodeRemap_property_op_type>` | ``0`` |
> +--------------------------------------------------+--------------------------------------------------------------+-------+
>

----


## Enumerations



enum **OpType**: [🔗<enum_VisualShaderNodeRemap_OpType>]



[OpType<enum_VisualShaderNodeRemap_OpType>] **OP_TYPE_SCALAR** = `0`

A floating-point scalar type.



[OpType<enum_VisualShaderNodeRemap_OpType>] **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.



[OpType<enum_VisualShaderNodeRemap_OpType>] **OP_TYPE_VECTOR_2D_SCALAR** = `2`

The `value` port uses a 2D vector type, while the `input min`, `input max`, `output min`, and `output max` ports use a floating-point scalar type.



[OpType<enum_VisualShaderNodeRemap_OpType>] **OP_TYPE_VECTOR_3D** = `3`

A 3D vector type.



[OpType<enum_VisualShaderNodeRemap_OpType>] **OP_TYPE_VECTOR_3D_SCALAR** = `4`

The `value` port uses a 3D vector type, while the `input min`, `input max`, `output min`, and `output max` ports use a floating-point scalar type.



[OpType<enum_VisualShaderNodeRemap_OpType>] **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.



[OpType<enum_VisualShaderNodeRemap_OpType>] **OP_TYPE_VECTOR_4D_SCALAR** = `6`

The `value` port uses a 4D vector type, while the `input min`, `input max`, `output min`, and `output max` ports use a floating-point scalar type.



[OpType<enum_VisualShaderNodeRemap_OpType>] **OP_TYPE_MAX** = `7`

Represents the size of the [OpType<enum_VisualShaderNodeRemap_OpType>] enum.


----


## Property Descriptions



[OpType<enum_VisualShaderNodeRemap_OpType>] **op_type** = `0` [🔗<class_VisualShaderNodeRemap_property_op_type>]


- |void| **set_op_type**\ (\ value\: [OpType<enum_VisualShaderNodeRemap_OpType>]\ )
- [OpType<enum_VisualShaderNodeRemap_OpType>] **get_op_type**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

