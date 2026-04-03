:github_url: hide



# VisualShaderNodeColorConstant

**Inherits:** [VisualShaderNodeConstant<class_VisualShaderNodeConstant>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A [Color<class_Color>] constant to be used within the visual shader graph.


## Description

Has two output ports representing RGB and alpha channels of [Color<class_Color>].

Translated to `vec3 rgb` and `float alpha` in the shader language.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>` | :ref:`constant<class_VisualShaderNodeColorConstant_property_constant>` | ``Color(1, 1, 1, 1)`` |
> +---------------------------+------------------------------------------------------------------------+-----------------------+
>

----


## Property Descriptions



[Color<class_Color>] **constant** = `Color(1, 1, 1, 1)` [🔗<class_VisualShaderNodeColorConstant_property_constant>]


- |void| **set_constant**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_constant**\ (\ )

A [Color<class_Color>] constant which represents a state of this node.

