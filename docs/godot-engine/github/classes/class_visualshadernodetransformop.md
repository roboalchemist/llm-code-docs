:github_url: hide



# VisualShaderNodeTransformOp

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A [Transform3D<class_Transform3D>] operator to be used within the visual shader graph.


## Description

Applies [operator<class_VisualShaderNodeTransformOp_property_operator>] to two transform (4×4 matrices) inputs.


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------+----------------------------------------------------------------------+-------+
> | :ref:`Operator<enum_VisualShaderNodeTransformOp_Operator>` | :ref:`operator<class_VisualShaderNodeTransformOp_property_operator>` | ``0`` |
> +------------------------------------------------------------+----------------------------------------------------------------------+-------+
>

----


## Enumerations



enum **Operator**: [🔗<enum_VisualShaderNodeTransformOp_Operator>]



[Operator<enum_VisualShaderNodeTransformOp_Operator>] **OP_AxB** = `0`

Multiplies transform `a` by the transform `b`.



[Operator<enum_VisualShaderNodeTransformOp_Operator>] **OP_BxA** = `1`

Multiplies transform `b` by the transform `a`.



[Operator<enum_VisualShaderNodeTransformOp_Operator>] **OP_AxB_COMP** = `2`

Performs a component-wise multiplication of transform `a` by the transform `b`.



[Operator<enum_VisualShaderNodeTransformOp_Operator>] **OP_BxA_COMP** = `3`

Performs a component-wise multiplication of transform `b` by the transform `a`.



[Operator<enum_VisualShaderNodeTransformOp_Operator>] **OP_ADD** = `4`

Adds two transforms.



[Operator<enum_VisualShaderNodeTransformOp_Operator>] **OP_A_MINUS_B** = `5`

Subtracts the transform `a` from the transform `b`.



[Operator<enum_VisualShaderNodeTransformOp_Operator>] **OP_B_MINUS_A** = `6`

Subtracts the transform `b` from the transform `a`.



[Operator<enum_VisualShaderNodeTransformOp_Operator>] **OP_A_DIV_B** = `7`

Divides the transform `a` by the transform `b`.



[Operator<enum_VisualShaderNodeTransformOp_Operator>] **OP_B_DIV_A** = `8`

Divides the transform `b` by the transform `a`.



[Operator<enum_VisualShaderNodeTransformOp_Operator>] **OP_MAX** = `9`

Represents the size of the [Operator<enum_VisualShaderNodeTransformOp_Operator>] enum.


----


## Property Descriptions



[Operator<enum_VisualShaderNodeTransformOp_Operator>] **operator** = `0` [🔗<class_VisualShaderNodeTransformOp_property_operator>]


- |void| **set_operator**\ (\ value\: [Operator<enum_VisualShaderNodeTransformOp_Operator>]\ )
- [Operator<enum_VisualShaderNodeTransformOp_Operator>] **get_operator**\ (\ )

The type of the operation to be performed on the transforms.

