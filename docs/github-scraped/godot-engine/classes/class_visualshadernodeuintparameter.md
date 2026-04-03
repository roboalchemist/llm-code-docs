:github_url: hide



# VisualShaderNodeUIntParameter

**Inherits:** [VisualShaderNodeParameter<class_VisualShaderNodeParameter>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A visual shader node for shader parameter (uniform) of type unsigned [int<class_int>].


## Description

A [VisualShaderNodeParameter<class_VisualShaderNodeParameter>] of type unsigned [int<class_int>]. Offers additional customization for range of accepted values.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`   | :ref:`default_value<class_VisualShaderNodeUIntParameter_property_default_value>`                 | ``0``     |
> +-------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>` | :ref:`default_value_enabled<class_VisualShaderNodeUIntParameter_property_default_value_enabled>` | ``false`` |
> +-------------------------+--------------------------------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[int<class_int>] **default_value** = `0` [🔗<class_VisualShaderNodeUIntParameter_property_default_value>]


- |void| **set_default_value**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_default_value**\ (\ )

Default value of this parameter, which will be used if not set externally. [default_value_enabled<class_VisualShaderNodeUIntParameter_property_default_value_enabled>] must be enabled; defaults to `0` otherwise.


----



[bool<class_bool>] **default_value_enabled** = `false` [🔗<class_VisualShaderNodeUIntParameter_property_default_value_enabled>]


- |void| **set_default_value_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_default_value_enabled**\ (\ )

If `true`, the node will have a custom default value.

