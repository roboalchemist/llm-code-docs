:github_url: hide



# VisualShaderNodeVec3Parameter

**Inherits:** [VisualShaderNodeParameter<class_VisualShaderNodeParameter>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A [Vector3<class_Vector3>] parameter to be used within the visual shader graph.


## Description

Translated to `uniform vec3` in the shader language.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+--------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`default_value<class_VisualShaderNodeVec3Parameter_property_default_value>`                 | ``Vector3(0, 0, 0)`` |
> +-------------------------------+--------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`bool<class_bool>`       | :ref:`default_value_enabled<class_VisualShaderNodeVec3Parameter_property_default_value_enabled>` | ``false``            |
> +-------------------------------+--------------------------------------------------------------------------------------------------+----------------------+
>

----


## Property Descriptions



[Vector3<class_Vector3>] **default_value** = `Vector3(0, 0, 0)` [🔗<class_VisualShaderNodeVec3Parameter_property_default_value>]


- |void| **set_default_value**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_default_value**\ (\ )

A default value to be assigned within the shader.


----



[bool<class_bool>] **default_value_enabled** = `false` [🔗<class_VisualShaderNodeVec3Parameter_property_default_value_enabled>]


- |void| **set_default_value_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_default_value_enabled**\ (\ )

Enables usage of the [default_value<class_VisualShaderNodeVec3Parameter_property_default_value>].

