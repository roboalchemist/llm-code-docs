:github_url: hide



# VisualShaderNodeBooleanParameter

**Inherits:** [VisualShaderNodeParameter<class_VisualShaderNodeParameter>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A boolean parameter to be used within the visual shader graph.


## Description

Translated to `uniform bool` in the shader language.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+-----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>` | :ref:`default_value<class_VisualShaderNodeBooleanParameter_property_default_value>`                 | ``false`` |
> +-------------------------+-----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>` | :ref:`default_value_enabled<class_VisualShaderNodeBooleanParameter_property_default_value_enabled>` | ``false`` |
> +-------------------------+-----------------------------------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[bool<class_bool>] **default_value** = `false` [🔗<class_VisualShaderNodeBooleanParameter_property_default_value>]


- |void| **set_default_value**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_default_value**\ (\ )

A default value to be assigned within the shader.


----



[bool<class_bool>] **default_value_enabled** = `false` [🔗<class_VisualShaderNodeBooleanParameter_property_default_value_enabled>]


- |void| **set_default_value_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_default_value_enabled**\ (\ )

Enables usage of the [default_value<class_VisualShaderNodeBooleanParameter_property_default_value>].

