# VisualShaderNodeUIntFunc in English

# VisualShaderNodeUIntFunc
Inherits:VisualShaderNode<Resource<RefCounted<Object
An unsigned scalar integer function to be used within the visual shader graph.

## Description
Accept an unsigned integer scalar (x) to the input port and transform it according tofunction.

## Properties

| Function | function | 0 |

Function
function

## Enumerations
enumFunction:🔗
FunctionFUNC_NEGATE=0
Negates thexusing-(x).
FunctionFUNC_BITWISE_NOT=1
Returns the result of bitwiseNOToperation on the integer. Translates to~ain the Godot Shader Language.
FunctionFUNC_MAX=2
Represents the size of theFunctionenum.

## Property Descriptions
Functionfunction=0🔗
- voidset_function(value:Function)
voidset_function(value:Function)
- Functionget_function()
Functionget_function()
A function to be applied to the scalar.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.