:github_url: hide



# VisualShaderNodeVectorOp

**Inherits:** [VisualShaderNodeVectorBase<class_VisualShaderNodeVectorBase>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A vector operator to be used within the visual shader graph.


## Description

A visual shader node for use of vector operators. Operates on vector `a` and vector `b`.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------+-------------------------------------------------------------------+-------+
> | :ref:`Operator<enum_VisualShaderNodeVectorOp_Operator>` | :ref:`operator<class_VisualShaderNodeVectorOp_property_operator>` | ``0`` |
> +---------------------------------------------------------+-------------------------------------------------------------------+-------+
>

----


## Enumerations



enum **Operator**: [🔗<enum_VisualShaderNodeVectorOp_Operator>]



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **OP_ADD** = `0`

Adds two vectors.



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **OP_SUB** = `1`

Subtracts a vector from a vector.



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **OP_MUL** = `2`

Multiplies two vectors.



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **OP_DIV** = `3`

Divides vector by vector.



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **OP_MOD** = `4`

Returns the remainder of the two vectors.



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **OP_POW** = `5`

Returns the value of the first parameter raised to the power of the second, for each component of the vectors.



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **OP_MAX** = `6`

Returns the greater of two values, for each component of the vectors.



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **OP_MIN** = `7`

Returns the lesser of two values, for each component of the vectors.



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **OP_CROSS** = `8`

Calculates the cross product of two vectors.



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **OP_ATAN2** = `9`

Returns the arc-tangent of the parameters.



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **OP_REFLECT** = `10`

Returns the vector that points in the direction of reflection. `a` is incident vector and `b` is the normal vector.



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **OP_STEP** = `11`

Vector step operator. Returns `0.0` if `a` is smaller than `b` and `1.0` otherwise.



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **OP_ENUM_SIZE** = `12`

Represents the size of the [Operator<enum_VisualShaderNodeVectorOp_Operator>] enum.


----


## Property Descriptions



[Operator<enum_VisualShaderNodeVectorOp_Operator>] **operator** = `0` [🔗<class_VisualShaderNodeVectorOp_property_operator>]


- |void| **set_operator**\ (\ value\: [Operator<enum_VisualShaderNodeVectorOp_Operator>]\ )
- [Operator<enum_VisualShaderNodeVectorOp_Operator>] **get_operator**\ (\ )

The operator to be used.

