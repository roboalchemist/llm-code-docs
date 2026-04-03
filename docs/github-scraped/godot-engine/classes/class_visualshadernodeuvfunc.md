:github_url: hide



# VisualShaderNodeUVFunc

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Contains functions to modify texture coordinates (`uv`) to be used within the visual shader graph.


## Description

UV functions are similar to [Vector2<class_Vector2>] functions, but the input port of this node uses the shader's UV value by default.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------+-----------------------------------------------------------------+-------+
> | :ref:`Function<enum_VisualShaderNodeUVFunc_Function>` | :ref:`function<class_VisualShaderNodeUVFunc_property_function>` | ``0`` |
> +-------------------------------------------------------+-----------------------------------------------------------------+-------+
>

----


## Enumerations



enum **Function**: [🔗<enum_VisualShaderNodeUVFunc_Function>]



[Function<enum_VisualShaderNodeUVFunc_Function>] **FUNC_PANNING** = `0`

Translates `uv` by using `scale` and `offset` values using the following formula: `uv = uv + offset * scale`. `uv` port is connected to `UV` built-in by default.



[Function<enum_VisualShaderNodeUVFunc_Function>] **FUNC_SCALING** = `1`

Scales `uv` by using `scale` and `pivot` values using the following formula: `uv = (uv - pivot) * scale + pivot`. `uv` port is connected to `UV` built-in by default.



[Function<enum_VisualShaderNodeUVFunc_Function>] **FUNC_MAX** = `2`

Represents the size of the [Function<enum_VisualShaderNodeUVFunc_Function>] enum.


----


## Property Descriptions



[Function<enum_VisualShaderNodeUVFunc_Function>] **function** = `0` [🔗<class_VisualShaderNodeUVFunc_property_function>]


- |void| **set_function**\ (\ value\: [Function<enum_VisualShaderNodeUVFunc_Function>]\ )
- [Function<enum_VisualShaderNodeUVFunc_Function>] **get_function**\ (\ )

A function to be applied to the texture coordinates.

