# VisualShaderNodeUIntOp

# VisualShaderNodeUIntOp
Inherits:VisualShaderNode<Resource<RefCounted<Object
An unsigned integer scalar operator to be used within the visual shader graph.

## Description
Appliesoperatorto two unsigned integer inputs:aandb.

## Properties

| Operator | operator | 0 |

Operator
operator

## Enumerations
enumOperator:🔗
OperatorOP_ADD=0
Sums two numbers usinga+b.
OperatorOP_SUB=1
Subtracts two numbers usinga-b.
OperatorOP_MUL=2
Multiplies two numbers usinga*b.
OperatorOP_DIV=3
Divides two numbers usinga/b.
OperatorOP_MOD=4
Calculates the remainder of two numbers usinga%b.
OperatorOP_MAX=5
Returns the greater of two numbers. Translates tomax(a,b)in the Godot Shader Language.
OperatorOP_MIN=6
Returns the lesser of two numbers. Translates tomax(a,b)in the Godot Shader Language.
OperatorOP_BITWISE_AND=7
Returns the result of bitwiseANDoperation on the integer. Translates toa&bin the Godot Shader Language.
OperatorOP_BITWISE_OR=8
Returns the result of bitwiseORoperation for two integers. Translates toa|bin the Godot Shader Language.
OperatorOP_BITWISE_XOR=9
Returns the result of bitwiseXORoperation for two integers. Translates toa^bin the Godot Shader Language.
OperatorOP_BITWISE_LEFT_SHIFT=10
Returns the result of bitwise left shift operation on the integer. Translates toa<<bin the Godot Shader Language.
OperatorOP_BITWISE_RIGHT_SHIFT=11
Returns the result of bitwise right shift operation on the integer. Translates toa>>bin the Godot Shader Language.
OperatorOP_ENUM_SIZE=12
Represents the size of theOperatorenum.

## Property Descriptions
Operatoroperator=0🔗
- voidset_operator(value:Operator)
voidset_operator(value:Operator)
- Operatorget_operator()
Operatorget_operator()
An operator to be applied to the inputs.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.