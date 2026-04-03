:github_url: hide



# VisualShaderNodeVectorBase

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [VisualShaderNodeFaceForward<class_VisualShaderNodeFaceForward>], [VisualShaderNodeVectorCompose<class_VisualShaderNodeVectorCompose>], [VisualShaderNodeVectorDecompose<class_VisualShaderNodeVectorDecompose>], [VisualShaderNodeVectorDistance<class_VisualShaderNodeVectorDistance>], [VisualShaderNodeVectorFunc<class_VisualShaderNodeVectorFunc>], [VisualShaderNodeVectorLen<class_VisualShaderNodeVectorLen>], [VisualShaderNodeVectorOp<class_VisualShaderNodeVectorOp>], [VisualShaderNodeVectorRefract<class_VisualShaderNodeVectorRefract>]

A base type for the nodes that perform vector operations within the visual shader graph.


## Description

This is an abstract class. See the derived types for descriptions of the possible operations.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------+-------------------------------------------------------------------+-------+
> | :ref:`OpType<enum_VisualShaderNodeVectorBase_OpType>` | :ref:`op_type<class_VisualShaderNodeVectorBase_property_op_type>` | ``1`` |
> +-------------------------------------------------------+-------------------------------------------------------------------+-------+
>

----


## Enumerations



enum **OpType**: [🔗<enum_VisualShaderNodeVectorBase_OpType>]



[OpType<enum_VisualShaderNodeVectorBase_OpType>] **OP_TYPE_VECTOR_2D** = `0`

A 2D vector type.



[OpType<enum_VisualShaderNodeVectorBase_OpType>] **OP_TYPE_VECTOR_3D** = `1`

A 3D vector type.



[OpType<enum_VisualShaderNodeVectorBase_OpType>] **OP_TYPE_VECTOR_4D** = `2`

A 4D vector type.



[OpType<enum_VisualShaderNodeVectorBase_OpType>] **OP_TYPE_MAX** = `3`

Represents the size of the [OpType<enum_VisualShaderNodeVectorBase_OpType>] enum.


----


## Property Descriptions



[OpType<enum_VisualShaderNodeVectorBase_OpType>] **op_type** = `1` [🔗<class_VisualShaderNodeVectorBase_property_op_type>]


- |void| **set_op_type**\ (\ value\: [OpType<enum_VisualShaderNodeVectorBase_OpType>]\ )
- [OpType<enum_VisualShaderNodeVectorBase_OpType>] **get_op_type**\ (\ )

A vector type that this operation is performed on.

