:github_url: hide



# VisualShaderNodeParameterRef

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A reference to an existing [VisualShaderNodeParameter<class_VisualShaderNodeParameter>].


## Description

Creating a reference to a [VisualShaderNodeParameter<class_VisualShaderNodeParameter>] allows you to reuse this parameter in different shaders or shader stages easily.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+-----------------------------------------------------------------------------------+--------------+
> | :ref:`String<class_String>` | :ref:`parameter_name<class_VisualShaderNodeParameterRef_property_parameter_name>` | ``"[None]"`` |
> +-----------------------------+-----------------------------------------------------------------------------------+--------------+
>

----


## Property Descriptions



[String<class_String>] **parameter_name** = `"[None]"` [🔗<class_VisualShaderNodeParameterRef_property_parameter_name>]


- |void| **set_parameter_name**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_parameter_name**\ (\ )

The name of the parameter which this reference points to.

