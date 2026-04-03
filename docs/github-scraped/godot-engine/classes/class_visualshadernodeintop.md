:github_url: hide



# VisualShaderNodeIntOp

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

An integer scalar operator to be used within the visual shader graph.


## Description

Applies [operator<class_VisualShaderNodeIntOp_property_operator>] to two integer inputs: `a` and `b`.


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------+----------------------------------------------------------------+-------+
> | :ref:`Operator<enum_VisualShaderNodeIntOp_Operator>` | :ref:`operator<class_VisualShaderNodeIntOp_property_operator>` | ``0`` |
> +------------------------------------------------------+----------------------------------------------------------------+-------+
>

----


## Enumerations



enum **Operator**: [🔗<enum_VisualShaderNodeIntOp_Operator>]



[Operator<enum_VisualShaderNodeIntOp_Operator>] **OP_ADD** = `0`

Sums two numbers using `a + b`.



[Operator<enum_VisualShaderNodeIntOp_Operator>] **OP_SUB** = `1`

Subtracts two numbers using `a - b`.



[Operator<enum_VisualShaderNodeIntOp_Operator>] **OP_MUL** = `2`

Multiplies two numbers using `a * b`.



[Operator<enum_VisualShaderNodeIntOp_Operator>] **OP_DIV** = `3`

Divides two numbers using `a / b`.



[Operator<enum_VisualShaderNodeIntOp_Operator>] **OP_MOD** = `4`

Calculates the remainder of two numbers using `a % b`.



[Operator<enum_VisualShaderNodeIntOp_Operator>] **OP_MAX** = `5`

Returns the greater of two numbers. Translates to `max(a, b)` in the Godot Shader Language.



[Operator<enum_VisualShaderNodeIntOp_Operator>] **OP_MIN** = `6`

Returns the lesser of two numbers. Translates to `max(a, b)` in the Godot Shader Language.



[Operator<enum_VisualShaderNodeIntOp_Operator>] **OP_BITWISE_AND** = `7`

Returns the result of bitwise `AND` operation on the integer. Translates to `a & b` in the Godot Shader Language.



[Operator<enum_VisualShaderNodeIntOp_Operator>] **OP_BITWISE_OR** = `8`

Returns the result of bitwise `OR` operation for two integers. Translates to `a | b` in the Godot Shader Language.



[Operator<enum_VisualShaderNodeIntOp_Operator>] **OP_BITWISE_XOR** = `9`

Returns the result of bitwise `XOR` operation for two integers. Translates to `a ^ b` in the Godot Shader Language.



[Operator<enum_VisualShaderNodeIntOp_Operator>] **OP_BITWISE_LEFT_SHIFT** = `10`

Returns the result of bitwise left shift operation on the integer. Translates to `a << b` in the Godot Shader Language.



[Operator<enum_VisualShaderNodeIntOp_Operator>] **OP_BITWISE_RIGHT_SHIFT** = `11`

Returns the result of bitwise right shift operation on the integer. Translates to `a >> b` in the Godot Shader Language.



[Operator<enum_VisualShaderNodeIntOp_Operator>] **OP_ENUM_SIZE** = `12`

Represents the size of the [Operator<enum_VisualShaderNodeIntOp_Operator>] enum.


----


## Property Descriptions



[Operator<enum_VisualShaderNodeIntOp_Operator>] **operator** = `0` [🔗<class_VisualShaderNodeIntOp_property_operator>]


- |void| **set_operator**\ (\ value\: [Operator<enum_VisualShaderNodeIntOp_Operator>]\ )
- [Operator<enum_VisualShaderNodeIntOp_Operator>] **get_operator**\ (\ )

An operator to be applied to the inputs.

