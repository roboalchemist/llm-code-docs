:github_url: hide



# VisualShaderNodeIs

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A boolean comparison operator to be used within the visual shader graph.


## Description

Returns the boolean result of the comparison between `INF` or `NaN` and a scalar parameter.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+-------------------------------------------------------------+-------+
> | :ref:`Function<enum_VisualShaderNodeIs_Function>` | :ref:`function<class_VisualShaderNodeIs_property_function>` | ``0`` |
> +---------------------------------------------------+-------------------------------------------------------------+-------+
>

----


## Enumerations



enum **Function**: [🔗<enum_VisualShaderNodeIs_Function>]



[Function<enum_VisualShaderNodeIs_Function>] **FUNC_IS_INF** = `0`

Comparison with `INF` (Infinity).



[Function<enum_VisualShaderNodeIs_Function>] **FUNC_IS_NAN** = `1`

Comparison with `NaN` (Not a Number; indicates invalid numeric results, such as division by zero).



[Function<enum_VisualShaderNodeIs_Function>] **FUNC_MAX** = `2`

Represents the size of the [Function<enum_VisualShaderNodeIs_Function>] enum.


----


## Property Descriptions



[Function<enum_VisualShaderNodeIs_Function>] **function** = `0` [🔗<class_VisualShaderNodeIs_property_function>]


- |void| **set_function**\ (\ value\: [Function<enum_VisualShaderNodeIs_Function>]\ )
- [Function<enum_VisualShaderNodeIs_Function>] **get_function**\ (\ )

The comparison function.

