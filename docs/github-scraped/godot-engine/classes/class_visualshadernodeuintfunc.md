:github_url: hide



# VisualShaderNodeUIntFunc

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

An unsigned scalar integer function to be used within the visual shader graph.


## Description

Accept an unsigned integer scalar (`x`) to the input port and transform it according to [function<class_VisualShaderNodeUIntFunc_property_function>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------+-------------------------------------------------------------------+-------+
> | :ref:`Function<enum_VisualShaderNodeUIntFunc_Function>` | :ref:`function<class_VisualShaderNodeUIntFunc_property_function>` | ``0`` |
> +---------------------------------------------------------+-------------------------------------------------------------------+-------+
>

----


## Enumerations



enum **Function**: [🔗<enum_VisualShaderNodeUIntFunc_Function>]



[Function<enum_VisualShaderNodeUIntFunc_Function>] **FUNC_NEGATE** = `0`

Negates the `x` using `-(x)`.



[Function<enum_VisualShaderNodeUIntFunc_Function>] **FUNC_BITWISE_NOT** = `1`

Returns the result of bitwise `NOT` operation on the integer. Translates to `~a` in the Godot Shader Language.



[Function<enum_VisualShaderNodeUIntFunc_Function>] **FUNC_MAX** = `2`

Represents the size of the [Function<enum_VisualShaderNodeUIntFunc_Function>] enum.


----


## Property Descriptions



[Function<enum_VisualShaderNodeUIntFunc_Function>] **function** = `0` [🔗<class_VisualShaderNodeUIntFunc_property_function>]


- |void| **set_function**\ (\ value\: [Function<enum_VisualShaderNodeUIntFunc_Function>]\ )
- [Function<enum_VisualShaderNodeUIntFunc_Function>] **get_function**\ (\ )

A function to be applied to the scalar.

