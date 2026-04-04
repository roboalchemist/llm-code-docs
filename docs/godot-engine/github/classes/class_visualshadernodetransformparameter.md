:github_url: hide



# VisualShaderNodeTransformParameter

**Inherits:** [VisualShaderNodeParameter<class_VisualShaderNodeParameter>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A [Transform3D<class_Transform3D>] parameter for use within the visual shader graph.


## Description

Translated to `uniform mat4` in the shader language.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`default_value<class_VisualShaderNodeTransformParameter_property_default_value>`                 | ``Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`` |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`default_value_enabled<class_VisualShaderNodeTransformParameter_property_default_value_enabled>` | ``false``                                           |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
>

----


## Property Descriptions



[Transform3D<class_Transform3D>] **default_value** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` [🔗<class_VisualShaderNodeTransformParameter_property_default_value>]


- |void| **set_default_value**\ (\ value\: [Transform3D<class_Transform3D>]\ )
- [Transform3D<class_Transform3D>] **get_default_value**\ (\ )

A default value to be assigned within the shader.


----



[bool<class_bool>] **default_value_enabled** = `false` [🔗<class_VisualShaderNodeTransformParameter_property_default_value_enabled>]


- |void| **set_default_value_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_default_value_enabled**\ (\ )

Enables usage of the [default_value<class_VisualShaderNodeTransformParameter_property_default_value>].

