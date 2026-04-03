:github_url: hide



# VisualShaderNodeParameter

**Inherits:** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [VisualShaderNodeBooleanParameter<class_VisualShaderNodeBooleanParameter>], [VisualShaderNodeColorParameter<class_VisualShaderNodeColorParameter>], [VisualShaderNodeFloatParameter<class_VisualShaderNodeFloatParameter>], [VisualShaderNodeIntParameter<class_VisualShaderNodeIntParameter>], [VisualShaderNodeTextureParameter<class_VisualShaderNodeTextureParameter>], [VisualShaderNodeTransformParameter<class_VisualShaderNodeTransformParameter>], [VisualShaderNodeUIntParameter<class_VisualShaderNodeUIntParameter>], [VisualShaderNodeVec2Parameter<class_VisualShaderNodeVec2Parameter>], [VisualShaderNodeVec3Parameter<class_VisualShaderNodeVec3Parameter>], [VisualShaderNodeVec4Parameter<class_VisualShaderNodeVec4Parameter>]

A base type for the parameters within the visual shader graph.


## Description

A parameter represents a variable in the shader which is set externally, i.e. from the [ShaderMaterial<class_ShaderMaterial>]. Parameters are exposed as properties in the [ShaderMaterial<class_ShaderMaterial>] and can be assigned from the Inspector or from a script.


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------+--------------------------------------------------------------------------------+--------+
> | :ref:`int<class_int>`                                      | :ref:`instance_index<class_VisualShaderNodeParameter_property_instance_index>` | ``0``  |
> +------------------------------------------------------------+--------------------------------------------------------------------------------+--------+
> | :ref:`String<class_String>`                                | :ref:`parameter_name<class_VisualShaderNodeParameter_property_parameter_name>` | ``""`` |
> +------------------------------------------------------------+--------------------------------------------------------------------------------+--------+
> | :ref:`Qualifier<enum_VisualShaderNodeParameter_Qualifier>` | :ref:`qualifier<class_VisualShaderNodeParameter_property_qualifier>`           | ``0``  |
> +------------------------------------------------------------+--------------------------------------------------------------------------------+--------+
>

----


## Enumerations



enum **Qualifier**: [🔗<enum_VisualShaderNodeParameter_Qualifier>]



[Qualifier<enum_VisualShaderNodeParameter_Qualifier>] **QUAL_NONE** = `0`

The parameter will be tied to the [ShaderMaterial<class_ShaderMaterial>] using this shader.



[Qualifier<enum_VisualShaderNodeParameter_Qualifier>] **QUAL_GLOBAL** = `1`

The parameter will use a global value, defined in Project Settings.



[Qualifier<enum_VisualShaderNodeParameter_Qualifier>] **QUAL_INSTANCE** = `2`

The parameter will be tied to the node with attached [ShaderMaterial<class_ShaderMaterial>] using this shader.



[Qualifier<enum_VisualShaderNodeParameter_Qualifier>] **QUAL_INSTANCE_INDEX** = `3`

The parameter will be tied to the node with attached [ShaderMaterial<class_ShaderMaterial>] using this shader. Enables setting a [instance_index<class_VisualShaderNodeParameter_property_instance_index>] property.



[Qualifier<enum_VisualShaderNodeParameter_Qualifier>] **QUAL_MAX** = `4`

Represents the size of the [Qualifier<enum_VisualShaderNodeParameter_Qualifier>] enum.


----


## Property Descriptions



[int<class_int>] **instance_index** = `0` [🔗<class_VisualShaderNodeParameter_property_instance_index>]


- |void| **set_instance_index**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_instance_index**\ (\ )

The index within 0-15 range, which is used to avoid clashes when shader used on multiple materials.


----



[String<class_String>] **parameter_name** = `""` [🔗<class_VisualShaderNodeParameter_property_parameter_name>]


- |void| **set_parameter_name**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_parameter_name**\ (\ )

Name of the parameter, by which it can be accessed through the [ShaderMaterial<class_ShaderMaterial>] properties.


----



[Qualifier<enum_VisualShaderNodeParameter_Qualifier>] **qualifier** = `0` [🔗<class_VisualShaderNodeParameter_property_qualifier>]


- |void| **set_qualifier**\ (\ value\: [Qualifier<enum_VisualShaderNodeParameter_Qualifier>]\ )
- [Qualifier<enum_VisualShaderNodeParameter_Qualifier>] **get_qualifier**\ (\ )

Defines the scope of the parameter.

