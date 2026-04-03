:github_url: hide



# VisualShaderNodeIntFunc

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A scalar integer function to be used within the visual shader graph.


## Description

Accept an integer scalar (`x`) to the input port and transform it according to [function<class_VisualShaderNodeIntFunc_property_function>].


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------+------------------------------------------------------------------+-------+
> | :ref:`Function<enum_VisualShaderNodeIntFunc_Function>` | :ref:`function<class_VisualShaderNodeIntFunc_property_function>` | ``2`` |
> +--------------------------------------------------------+------------------------------------------------------------------+-------+
>

----


## Enumerations



enum **Function**: [🔗<enum_VisualShaderNodeIntFunc_Function>]



[Function<enum_VisualShaderNodeIntFunc_Function>] **FUNC_ABS** = `0`

Returns the absolute value of the parameter. Translates to `abs(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeIntFunc_Function>] **FUNC_NEGATE** = `1`

Negates the `x` using `-(x)`.



[Function<enum_VisualShaderNodeIntFunc_Function>] **FUNC_SIGN** = `2`

Extracts the sign of the parameter. Translates to `sign(x)` in the Godot Shader Language.



[Function<enum_VisualShaderNodeIntFunc_Function>] **FUNC_BITWISE_NOT** = `3`

Returns the result of bitwise `NOT` operation on the integer. Translates to `~a` in the Godot Shader Language.



[Function<enum_VisualShaderNodeIntFunc_Function>] **FUNC_MAX** = `4`

Represents the size of the [Function<enum_VisualShaderNodeIntFunc_Function>] enum.


----


## Property Descriptions



[Function<enum_VisualShaderNodeIntFunc_Function>] **function** = `2` [🔗<class_VisualShaderNodeIntFunc_property_function>]


- |void| **set_function**\ (\ value\: [Function<enum_VisualShaderNodeIntFunc_Function>]\ )
- [Function<enum_VisualShaderNodeIntFunc_Function>] **get_function**\ (\ )

A function to be applied to the scalar.

