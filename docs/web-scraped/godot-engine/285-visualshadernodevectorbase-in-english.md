# VisualShaderNodeVectorBase in English

# VisualShaderNodeVectorBase
Inherits:VisualShaderNode<Resource<RefCounted<Object
Inherited By:VisualShaderNodeFaceForward,VisualShaderNodeVectorCompose,VisualShaderNodeVectorDecompose,VisualShaderNodeVectorDistance,VisualShaderNodeVectorFunc,VisualShaderNodeVectorLen,VisualShaderNodeVectorOp,VisualShaderNodeVectorRefract
A base type for the nodes that perform vector operations within the visual shader graph.

## Description
This is an abstract class. See the derived types for descriptions of the possible operations.

## Properties

| OpType | op_type | 1 |

OpType
op_type

## Enumerations
enumOpType:🔗
OpTypeOP_TYPE_VECTOR_2D=0
A 2D vector type.
OpTypeOP_TYPE_VECTOR_3D=1
A 3D vector type.
OpTypeOP_TYPE_VECTOR_4D=2
A 4D vector type.
OpTypeOP_TYPE_MAX=3
Represents the size of theOpTypeenum.

## Property Descriptions
OpTypeop_type=1🔗
- voidset_op_type(value:OpType)
voidset_op_type(value:OpType)
- OpTypeget_op_type()
OpTypeget_op_type()
A vector type that this operation is performed on.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.