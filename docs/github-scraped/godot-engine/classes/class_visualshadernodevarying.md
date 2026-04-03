:github_url: hide



# VisualShaderNodeVarying

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [VisualShaderNodeVaryingGetter<class_VisualShaderNodeVaryingGetter>], [VisualShaderNodeVaryingSetter<class_VisualShaderNodeVaryingSetter>]

A visual shader node that represents a "varying" shader value.


## Description

Varying values are shader variables that can be passed between shader functions, e.g. from Vertex shader to Fragment shader.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+--------------------------------------------------------------------------+--------------+
> | :ref:`String<class_String>`                       | :ref:`varying_name<class_VisualShaderNodeVarying_property_varying_name>` | ``"[None]"`` |
> +---------------------------------------------------+--------------------------------------------------------------------------+--------------+
> | :ref:`VaryingType<enum_VisualShader_VaryingType>` | :ref:`varying_type<class_VisualShaderNodeVarying_property_varying_type>` | ``0``        |
> +---------------------------------------------------+--------------------------------------------------------------------------+--------------+
>

----


## Property Descriptions



[String<class_String>] **varying_name** = `"[None]"` [🔗<class_VisualShaderNodeVarying_property_varying_name>]


- |void| **set_varying_name**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_varying_name**\ (\ )

Name of the variable. Must be unique.


----



[VaryingType<enum_VisualShader_VaryingType>] **varying_type** = `0` [🔗<class_VisualShaderNodeVarying_property_varying_type>]


- |void| **set_varying_type**\ (\ value\: [VaryingType<enum_VisualShader_VaryingType>]\ )
- [VaryingType<enum_VisualShader_VaryingType>] **get_varying_type**\ (\ )

Type of the variable. Determines where the variable can be accessed.

