# VisualShaderNodeFloatFunc in English

# VisualShaderNodeFloatFunc

Inherits:VisualShaderNode<Resource<RefCounted<Object
A scalar floating-point function to be used within the visual shader graph.

## Description

Accept a floating-point scalar (x) to the input port and transform it according tofunction.

## Properties

| Function | function | 13 |

Function
function

## Enumerations

enumFunction:🔗
FunctionFUNC_SIN=0
Returns the sine of the parameter. Translates tosin(x)in the Godot Shader Language.
FunctionFUNC_COS=1
Returns the cosine of the parameter. Translates tocos(x)in the Godot Shader Language.
FunctionFUNC_TAN=2
Returns the tangent of the parameter. Translates totan(x)in the Godot Shader Language.
FunctionFUNC_ASIN=3
Returns the arc-sine of the parameter. Translates toasin(x)in the Godot Shader Language.
FunctionFUNC_ACOS=4
Returns the arc-cosine of the parameter. Translates toacos(x)in the Godot Shader Language.
FunctionFUNC_ATAN=5
Returns the arc-tangent of the parameter. Translates toatan(x)in the Godot Shader Language.
FunctionFUNC_SINH=6
Returns the hyperbolic sine of the parameter. Translates tosinh(x)in the Godot Shader Language.
FunctionFUNC_COSH=7
Returns the hyperbolic cosine of the parameter. Translates tocosh(x)in the Godot Shader Language.
FunctionFUNC_TANH=8
Returns the hyperbolic tangent of the parameter. Translates totanh(x)in the Godot Shader Language.
FunctionFUNC_LOG=9
Returns the natural logarithm of the parameter. Translates tolog(x)in the Godot Shader Language.
FunctionFUNC_EXP=10
Returns the natural exponentiation of the parameter. Translates toexp(x)in the Godot Shader Language.
FunctionFUNC_SQRT=11
Returns the square root of the parameter. Translates tosqrt(x)in the Godot Shader Language.
FunctionFUNC_ABS=12
Returns the absolute value of the parameter. Translates toabs(x)in the Godot Shader Language.
FunctionFUNC_SIGN=13
Extracts the sign of the parameter. Translates tosign(x)in the Godot Shader Language.
FunctionFUNC_FLOOR=14
Finds the nearest integer less than or equal to the parameter. Translates tofloor(x)in the Godot Shader Language.
FunctionFUNC_ROUND=15
Finds the nearest integer to the parameter. Translates toround(x)in the Godot Shader Language.
FunctionFUNC_CEIL=16
Finds the nearest integer that is greater than or equal to the parameter. Translates toceil(x)in the Godot Shader Language.
FunctionFUNC_FRACT=17
Computes the fractional part of the argument. Translates tofract(x)in the Godot Shader Language.
FunctionFUNC_SATURATE=18
Clamps the value between0.0and1.0usingmin(max(x,0.0),1.0).
FunctionFUNC_NEGATE=19
Negates thexusing-(x).
FunctionFUNC_ACOSH=20
Returns the arc-hyperbolic-cosine of the parameter. Translates toacosh(x)in the Godot Shader Language.
FunctionFUNC_ASINH=21
Returns the arc-hyperbolic-sine of the parameter. Translates toasinh(x)in the Godot Shader Language.
FunctionFUNC_ATANH=22
Returns the arc-hyperbolic-tangent of the parameter. Translates toatanh(x)in the Godot Shader Language.
FunctionFUNC_DEGREES=23
Convert a quantity in radians to degrees. Translates todegrees(x)in the Godot Shader Language.
FunctionFUNC_EXP2=24
Returns 2 raised by the power of the parameter. Translates toexp2(x)in the Godot Shader Language.
FunctionFUNC_INVERSE_SQRT=25
Returns the inverse of the square root of the parameter. Translates toinversesqrt(x)in the Godot Shader Language.
FunctionFUNC_LOG2=26
Returns the base 2 logarithm of the parameter. Translates tolog2(x)in the Godot Shader Language.
FunctionFUNC_RADIANS=27
Convert a quantity in degrees to radians. Translates toradians(x)in the Godot Shader Language.
FunctionFUNC_RECIPROCAL=28
Finds reciprocal value of dividing 1 byx(i.e.1/x).
FunctionFUNC_ROUNDEVEN=29
Finds the nearest even integer to the parameter. Translates toroundEven(x)in the Godot Shader Language.
FunctionFUNC_TRUNC=30
Returns a value equal to the nearest integer toxwhose absolute value is not larger than the absolute value ofx. Translates totrunc(x)in the Godot Shader Language.
FunctionFUNC_ONEMINUS=31
Subtracts scalarxfrom 1 (i.e.1-x).
FunctionFUNC_MAX=32
Represents the size of theFunctionenum.

## Property Descriptions

Functionfunction=13🔗

- voidset_function(value:Function)
voidset_function(value:Function)
- Functionget_function()
Functionget_function()
A function to be applied to the scalar.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
