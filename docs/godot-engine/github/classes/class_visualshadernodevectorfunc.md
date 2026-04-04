:github_url: hide



# VisualShaderNodeVectorFunc

**Inherits:** [VisualShaderNodeVectorBase<class_VisualShaderNodeVectorBase>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A vector function to be used within the visual shader graph.


## Description

A visual shader node able to perform different functions using vectors.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------+---------------------------------------------------------------------+-------+
> | :ref:`Function<enum_VisualShaderNodeVectorFunc_Function>` | :ref:`function<class_VisualShaderNodeVectorFunc_property_function>` | ``0`` |
> +-----------------------------------------------------------+---------------------------------------------------------------------+-------+
>

----


## Enumerations



enum **Function**: [🔗<enum_VisualShaderNodeVectorFunc_Function>]



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_NORMALIZE** = `0`

Normalizes the vector so that it has a length of `1` but points in the same direction.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_SATURATE** = `1`

Clamps the value between `0.0` and `1.0`.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_NEGATE** = `2`

Returns the opposite value of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_RECIPROCAL** = `3`

Returns `1/vector`.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_ABS** = `4`

Returns the absolute value of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_ACOS** = `5`

Returns the arc-cosine of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_ACOSH** = `6`

Returns the inverse hyperbolic cosine of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_ASIN** = `7`

Returns the arc-sine of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_ASINH** = `8`

Returns the inverse hyperbolic sine of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_ATAN** = `9`

Returns the arc-tangent of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_ATANH** = `10`

Returns the inverse hyperbolic tangent of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_CEIL** = `11`

Finds the nearest integer that is greater than or equal to the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_COS** = `12`

Returns the cosine of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_COSH** = `13`

Returns the hyperbolic cosine of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_DEGREES** = `14`

Converts a quantity in radians to degrees.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_EXP** = `15`

Base-e Exponential.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_EXP2** = `16`

Base-2 Exponential.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_FLOOR** = `17`

Finds the nearest integer less than or equal to the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_FRACT** = `18`

Computes the fractional part of the argument.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_INVERSE_SQRT** = `19`

Returns the inverse of the square root of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_LOG** = `20`

Natural logarithm.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_LOG2** = `21`

Base-2 logarithm.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_RADIANS** = `22`

Converts a quantity in degrees to radians.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_ROUND** = `23`

Finds the nearest integer to the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_ROUNDEVEN** = `24`

Finds the nearest even integer to the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_SIGN** = `25`

Extracts the sign of the parameter, i.e. returns `-1` if the parameter is negative, `1` if it's positive and `0` otherwise.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_SIN** = `26`

Returns the sine of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_SINH** = `27`

Returns the hyperbolic sine of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_SQRT** = `28`

Returns the square root of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_TAN** = `29`

Returns the tangent of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_TANH** = `30`

Returns the hyperbolic tangent of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_TRUNC** = `31`

Returns a value equal to the nearest integer to the parameter whose absolute value is not larger than the absolute value of the parameter.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_ONEMINUS** = `32`

Returns `1.0 - vector`.



[Function<enum_VisualShaderNodeVectorFunc_Function>] **FUNC_MAX** = `33`

Represents the size of the [Function<enum_VisualShaderNodeVectorFunc_Function>] enum.


----


## Property Descriptions



[Function<enum_VisualShaderNodeVectorFunc_Function>] **function** = `0` [🔗<class_VisualShaderNodeVectorFunc_property_function>]


- |void| **set_function**\ (\ value\: [Function<enum_VisualShaderNodeVectorFunc_Function>]\ )
- [Function<enum_VisualShaderNodeVectorFunc_Function>] **get_function**\ (\ )

The function to be performed.

