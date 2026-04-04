:github_url: hide



# VisualShaderNodeFloatFunc

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A scalar floating-point function to be used within the visual shader graph.


## Description

Accept a floating-point scalar (`x`) to the input port and transform it according to [function<class_VisualShaderNodeFloatFunc_property_function>].


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------+--------------------------------------------------------------------+--------+
> | :ref:`Function<enum_VisualShaderNodeFloatFunc_Function>` | :ref:`function<class_VisualShaderNodeFloatFunc_property_function>` | ``13`` |
> +----------------------------------------------------------+--------------------------------------------------------------------+--------+
>

----


## Enumerations



enum **Function**: [🔗<enum_VisualShaderNodeFloatFunc_Function>]



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_SIN** = `0`

Returns the sine of the parameter. Translates to `sin(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_COS** = `1`

Returns the cosine of the parameter. Translates to `cos(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_TAN** = `2`

Returns the tangent of the parameter. Translates to `tan(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_ASIN** = `3`

Returns the arc-sine of the parameter. Translates to `asin(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_ACOS** = `4`

Returns the arc-cosine of the parameter. Translates to `acos(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_ATAN** = `5`

Returns the arc-tangent of the parameter. Translates to `atan(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_SINH** = `6`

Returns the hyperbolic sine of the parameter. Translates to `sinh(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_COSH** = `7`

Returns the hyperbolic cosine of the parameter. Translates to `cosh(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_TANH** = `8`

Returns the hyperbolic tangent of the parameter. Translates to `tanh(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_LOG** = `9`

Returns the natural logarithm of the parameter. Translates to `log(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_EXP** = `10`

Returns the natural exponentiation of the parameter. Translates to `exp(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_SQRT** = `11`

Returns the square root of the parameter. Translates to `sqrt(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_ABS** = `12`

Returns the absolute value of the parameter. Translates to `abs(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_SIGN** = `13`

Extracts the sign of the parameter. Translates to `sign(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_FLOOR** = `14`

Finds the nearest integer less than or equal to the parameter. Translates to `floor(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_ROUND** = `15`

Finds the nearest integer to the parameter. Translates to `round(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_CEIL** = `16`

Finds the nearest integer that is greater than or equal to the parameter. Translates to `ceil(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_FRACT** = `17`

Computes the fractional part of the argument. Translates to `fract(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_SATURATE** = `18`

Clamps the value between `0.0` and `1.0` using `min(max(x, 0.0), 1.0)`.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_NEGATE** = `19`

Negates the `x` using `-(x)`.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_ACOSH** = `20`

Returns the arc-hyperbolic-cosine of the parameter. Translates to `acosh(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_ASINH** = `21`

Returns the arc-hyperbolic-sine of the parameter. Translates to `asinh(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_ATANH** = `22`

Returns the arc-hyperbolic-tangent of the parameter. Translates to `atanh(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_DEGREES** = `23`

Convert a quantity in radians to degrees. Translates to `degrees(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_EXP2** = `24`

Returns 2 raised by the power of the parameter. Translates to `exp2(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_INVERSE_SQRT** = `25`

Returns the inverse of the square root of the parameter. Translates to `inversesqrt(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_LOG2** = `26`

Returns the base 2 logarithm of the parameter. Translates to `log2(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_RADIANS** = `27`

Convert a quantity in degrees to radians. Translates to `radians(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_RECIPROCAL** = `28`

Finds reciprocal value of dividing 1 by `x` (i.e. `1 / x`).



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_ROUNDEVEN** = `29`

Finds the nearest even integer to the parameter. Translates to `roundEven(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_TRUNC** = `30`

Returns a value equal to the nearest integer to `x` whose absolute value is not larger than the absolute value of `x`. Translates to `trunc(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_ONEMINUS** = `31`

Subtracts scalar `x` from 1 (i.e. `1 - x`).



[Function<enum_VisualShaderNodeFloatFunc_Function>] **FUNC_MAX** = `32`

Represents the size of the [Function<enum_VisualShaderNodeFloatFunc_Function>] enum.


----


## Property Descriptions



[Function<enum_VisualShaderNodeFloatFunc_Function>] **function** = `13` [🔗<class_VisualShaderNodeFloatFunc_property_function>]


- |void| **set_function**\ (\ value\: [Function<enum_VisualShaderNodeFloatFunc_Function>]\ )
- [Function<enum_VisualShaderNodeFloatFunc_Function>] **get_function**\ (\ )

A function to be applied to the scalar.

