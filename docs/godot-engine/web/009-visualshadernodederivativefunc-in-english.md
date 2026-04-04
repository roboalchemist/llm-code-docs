# VisualShaderNodeDerivativeFunc in English

# VisualShaderNodeDerivativeFunc

Inherits:VisualShaderNode<Resource<RefCounted<Object
Calculates a derivative within the visual shader graph.

## Description

This node is only available inFragmentandLightvisual shaders.

## Properties

| Function | function | 0 |
|---|---|---|
| OpType | op_type | 0 |
| Precision | precision | 0 |

Function
function
OpType
op_type
Precision
precision

## Enumerations

enumOpType:🔗
OpTypeOP_TYPE_SCALAR=0
A floating-point scalar.
OpTypeOP_TYPE_VECTOR_2D=1
A 2D vector type.
OpTypeOP_TYPE_VECTOR_3D=2
A 3D vector type.
OpTypeOP_TYPE_VECTOR_4D=3
A 4D vector type.
OpTypeOP_TYPE_MAX=4
Represents the size of theOpTypeenum.
enumFunction:🔗
FunctionFUNC_SUM=0
Sum of absolute derivative inxandy.
FunctionFUNC_X=1
Derivative inxusing local differencing.
FunctionFUNC_Y=2
Derivative inyusing local differencing.
FunctionFUNC_MAX=3
Represents the size of theFunctionenum.
enumPrecision:🔗
PrecisionPRECISION_NONE=0
No precision is specified, the GPU driver is allowed to use whatever level of precision it chooses. This is the default option and is equivalent to usingdFdx()ordFdy()in text shaders.
PrecisionPRECISION_COARSE=1
The derivative will be calculated using the current fragment's neighbors (which may not include the current fragment). This tends to be faster than usingPRECISION_FINE, but may not be suitable when more precision is needed. This is equivalent to usingdFdxCoarse()ordFdyCoarse()in text shaders.
PrecisionPRECISION_FINE=2
The derivative will be calculated using the current fragment and its immediate neighbors. This tends to be slower than usingPRECISION_COARSE, but may be necessary when more precision is needed. This is equivalent to usingdFdxFine()ordFdyFine()in text shaders.
PrecisionPRECISION_MAX=3
Represents the size of thePrecisionenum.

## Property Descriptions

Functionfunction=0🔗

- voidset_function(value:Function)
voidset_function(value:Function)
- Functionget_function()
Functionget_function()
A derivative function type.
OpTypeop_type=0🔗
- voidset_op_type(value:OpType)
voidset_op_type(value:OpType)
- OpTypeget_op_type()
OpTypeget_op_type()
A type of operands and returned value.
Precisionprecision=0🔗
- voidset_precision(value:Precision)
voidset_precision(value:Precision)
- Precisionget_precision()
Precisionget_precision()
Sets the level of precision to use for the derivative function. When using the Compatibility renderer, this setting has no effect.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
