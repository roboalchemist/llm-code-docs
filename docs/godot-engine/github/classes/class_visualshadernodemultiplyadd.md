:github_url: hide



# VisualShaderNodeMultiplyAdd

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Performs a fused multiply-add operation within the visual shader graph.


## Description

Uses three operands to compute `(a * b + c)` expression.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------+--------------------------------------------------------------------+-------+
> | :ref:`OpType<enum_VisualShaderNodeMultiplyAdd_OpType>` | :ref:`op_type<class_VisualShaderNodeMultiplyAdd_property_op_type>` | ``0`` |
> +--------------------------------------------------------+--------------------------------------------------------------------+-------+
>

----


## Enumerations



enum **OpType**: [🔗<enum_VisualShaderNodeMultiplyAdd_OpType>]



[OpType<enum_VisualShaderNodeMultiplyAdd_OpType>] **OP_TYPE_SCALAR** = `0`

A floating-point scalar type.



[OpType<enum_VisualShaderNodeMultiplyAdd_OpType>] **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.



[OpType<enum_VisualShaderNodeMultiplyAdd_OpType>] **OP_TYPE_VECTOR_3D** = `2`

A 3D vector type.



[OpType<enum_VisualShaderNodeMultiplyAdd_OpType>] **OP_TYPE_VECTOR_4D** = `3`

A 4D vector type.



[OpType<enum_VisualShaderNodeMultiplyAdd_OpType>] **OP_TYPE_MAX** = `4`

Represents the size of the [OpType<enum_VisualShaderNodeMultiplyAdd_OpType>] enum.


----


## Property Descriptions



[OpType<enum_VisualShaderNodeMultiplyAdd_OpType>] **op_type** = `0` [🔗<class_VisualShaderNodeMultiplyAdd_property_op_type>]


- |void| **set_op_type**\ (\ value\: [OpType<enum_VisualShaderNodeMultiplyAdd_OpType>]\ )
- [OpType<enum_VisualShaderNodeMultiplyAdd_OpType>] **get_op_type**\ (\ )

A type of operands and returned value.

