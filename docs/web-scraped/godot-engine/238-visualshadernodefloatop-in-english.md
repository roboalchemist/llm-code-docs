# VisualShaderNodeFloatOp in English

# VisualShaderNodeFloatOp

Inherits:VisualShaderNode<Resource<RefCounted<Object
A floating-point scalar operator to be used within the visual shader graph.

## Description

Appliesoperatorto two floating-point inputs:aandb.

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
Calculates the remainder of two numbers. Translates tomod(a,b)in the Godot Shader Language.
OperatorOP_POW=5
Raises theato the power ofb. Translates topow(a,b)in the Godot Shader Language.
OperatorOP_MAX=6
Returns the greater of two numbers. Translates tomax(a,b)in the Godot Shader Language.
OperatorOP_MIN=7
Returns the lesser of two numbers. Translates tomin(a,b)in the Godot Shader Language.
OperatorOP_ATAN2=8
Returns the arc-tangent of the parameters. Translates toatan(a,b)in the Godot Shader Language.
OperatorOP_STEP=9
Generates a step function by comparingb(x) toa(edge). Returns 0.0 ifxis smaller thanedgeand otherwise 1.0. Translates tostep(a,b)in the Godot Shader Language.
OperatorOP_ENUM_SIZE=10
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
