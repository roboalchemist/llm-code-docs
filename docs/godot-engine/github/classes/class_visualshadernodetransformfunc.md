:github_url: hide



# VisualShaderNodeTransformFunc

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Computes a [Transform3D<class_Transform3D>] function within the visual shader graph.


## Description

Computes an inverse or transpose function on the provided [Transform3D<class_Transform3D>].


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------+------------------------------------------------------------------------+-------+
> | :ref:`Function<enum_VisualShaderNodeTransformFunc_Function>` | :ref:`function<class_VisualShaderNodeTransformFunc_property_function>` | ``0`` |
> +--------------------------------------------------------------+------------------------------------------------------------------------+-------+
>

----


## Enumerations



enum **Function**: [🔗<enum_VisualShaderNodeTransformFunc_Function>]



[Function<enum_VisualShaderNodeTransformFunc_Function>] **FUNC_INVERSE** = `0`

Perform the inverse operation on the [Transform3D<class_Transform3D>] matrix.



[Function<enum_VisualShaderNodeTransformFunc_Function>] **FUNC_TRANSPOSE** = `1`

Perform the transpose operation on the [Transform3D<class_Transform3D>] matrix.



[Function<enum_VisualShaderNodeTransformFunc_Function>] **FUNC_MAX** = `2`

Represents the size of the [Function<enum_VisualShaderNodeTransformFunc_Function>] enum.


----


## Property Descriptions



[Function<enum_VisualShaderNodeTransformFunc_Function>] **function** = `0` [🔗<class_VisualShaderNodeTransformFunc_property_function>]


- |void| **set_function**\ (\ value\: [Function<enum_VisualShaderNodeTransformFunc_Function>]\ )
- [Function<enum_VisualShaderNodeTransformFunc_Function>] **get_function**\ (\ )

The function to be computed.

