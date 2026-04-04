:github_url: hide



# VisualShaderNodeColorParameter

**Inherits:** [VisualShaderNodeParameter<class_VisualShaderNodeParameter>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A [Color<class_Color>] parameter to be used within the visual shader graph.


## Description

Translated to `uniform vec4` in the shader language.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>` | :ref:`default_value<class_VisualShaderNodeColorParameter_property_default_value>`                 | ``Color(1, 1, 1, 1)`` |
> +---------------------------+---------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`   | :ref:`default_value_enabled<class_VisualShaderNodeColorParameter_property_default_value_enabled>` | ``false``             |
> +---------------------------+---------------------------------------------------------------------------------------------------+-----------------------+
>

----


## Property Descriptions



[Color<class_Color>] **default_value** = `Color(1, 1, 1, 1)` [🔗<class_VisualShaderNodeColorParameter_property_default_value>]


- |void| **set_default_value**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_default_value**\ (\ )

A default value to be assigned within the shader.


----



[bool<class_bool>] **default_value_enabled** = `false` [🔗<class_VisualShaderNodeColorParameter_property_default_value_enabled>]


- |void| **set_default_value_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_default_value_enabled**\ (\ )

Enables usage of the [default_value<class_VisualShaderNodeColorParameter_property_default_value>].

