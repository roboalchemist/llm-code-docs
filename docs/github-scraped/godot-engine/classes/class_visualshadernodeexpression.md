:github_url: hide



# VisualShaderNodeExpression

**Inherits:** [VisualShaderNodeGroupBase<class_VisualShaderNodeGroupBase>] **<** [VisualShaderNodeResizableBase<class_VisualShaderNodeResizableBase>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [VisualShaderNodeGlobalExpression<class_VisualShaderNodeGlobalExpression>]

A custom visual shader graph expression written in Godot Shading Language.


## Description

Custom Godot Shading Language expression, with a custom number of input and output ports.

The provided code is directly injected into the graph's matching shader function (`vertex`, `fragment`, or `light`), so it cannot be used to declare functions, varyings, uniforms, or global constants. See [VisualShaderNodeGlobalExpression<class_VisualShaderNodeGlobalExpression>] for such global definitions.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+-------------------------------------------------------------------------+--------+
> | :ref:`String<class_String>` | :ref:`expression<class_VisualShaderNodeExpression_property_expression>` | ``""`` |
> +-----------------------------+-------------------------------------------------------------------------+--------+
>

----


## Property Descriptions



[String<class_String>] **expression** = `""` [🔗<class_VisualShaderNodeExpression_property_expression>]


- |void| **set_expression**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_expression**\ (\ )

An expression in Godot Shading Language, which will be injected at the start of the graph's matching shader function (`vertex`, `fragment`, or `light`), and thus cannot be used to declare functions, varyings, uniforms, or global constants.

