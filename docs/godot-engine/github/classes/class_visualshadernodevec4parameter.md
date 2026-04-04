:github_url: hide



# VisualShaderNodeVec4Parameter

**Inherits:** [VisualShaderNodeParameter<class_VisualShaderNodeParameter>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 4D vector parameter to be used within the visual shader graph.


## Description

Translated to `uniform vec4` in the shader language.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`Vector4<class_Vector4>` | :ref:`default_value<class_VisualShaderNodeVec4Parameter_property_default_value>`                 | ``Vector4(0, 0, 0, 0)`` |
> +-------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
> | :ref:`bool<class_bool>`       | :ref:`default_value_enabled<class_VisualShaderNodeVec4Parameter_property_default_value_enabled>` | ``false``               |
> +-------------------------------+--------------------------------------------------------------------------------------------------+-------------------------+
>

----


## Property Descriptions



[Vector4<class_Vector4>] **default_value** = `Vector4(0, 0, 0, 0)` [🔗<class_VisualShaderNodeVec4Parameter_property_default_value>]


- |void| **set_default_value**\ (\ value\: [Vector4<class_Vector4>]\ )
- [Vector4<class_Vector4>] **get_default_value**\ (\ )

A default value to be assigned within the shader.


----



[bool<class_bool>] **default_value_enabled** = `false` [🔗<class_VisualShaderNodeVec4Parameter_property_default_value_enabled>]


- |void| **set_default_value_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_default_value_enabled**\ (\ )

Enables usage of the [default_value<class_VisualShaderNodeVec4Parameter_property_default_value>].

