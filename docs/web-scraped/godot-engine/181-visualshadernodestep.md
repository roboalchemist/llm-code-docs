# VisualShaderNodeStep

# VisualShaderNodeStep
Inherits:VisualShaderNode<Resource<RefCounted<Object
Calculates a Step function within the visual shader graph.

## Description
Translates tostep(edge,x)in the shader language.
Returns0.0ifxis smaller thanedgeand1.0otherwise.

## Properties

| OpType | op_type | 0 |

OpType
op_type

## Enumerations
enumOpType:🔗
OpTypeOP_TYPE_SCALAR=0
A floating-point scalar type.
OpTypeOP_TYPE_VECTOR_2D=1
A 2D vector type.
OpTypeOP_TYPE_VECTOR_2D_SCALAR=2
Thexport uses a 2D vector type, while theedgeport uses a floating-point scalar type.
OpTypeOP_TYPE_VECTOR_3D=3
A 3D vector type.
OpTypeOP_TYPE_VECTOR_3D_SCALAR=4
Thexport uses a 3D vector type, while theedgeport uses a floating-point scalar type.
OpTypeOP_TYPE_VECTOR_4D=5
A 4D vector type.
OpTypeOP_TYPE_VECTOR_4D_SCALAR=6
Theaandbports use a 4D vector type. Theweightport uses a scalar type.
OpTypeOP_TYPE_MAX=7
Represents the size of theOpTypeenum.

## Property Descriptions
OpTypeop_type=0🔗
- voidset_op_type(value:OpType)
voidset_op_type(value:OpType)
- OpTypeget_op_type()
OpTypeget_op_type()
A type of operands and returned value.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.