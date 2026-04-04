:github_url: hide



# RDShaderFile

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Compiled shader file in SPIR-V form (used by [RenderingDevice<class_RenderingDevice>]). Not to be confused with Godot's own [Shader<class_Shader>].


## Description

Compiled shader file in SPIR-V form.

See also [RDShaderSource<class_RDShaderSource>]. **RDShaderFile** is only meant to be used with the [RenderingDevice<class_RenderingDevice>] API. It should not be confused with Godot's own [Shader<class_Shader>] resource, which is what Godot's various nodes use for high-level shader programming.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+-----------------------------------------------------------+--------+
> | :ref:`String<class_String>` | :ref:`base_error<class_RDShaderFile_property_base_error>` | ``""`` |
> +-----------------------------+-----------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RDShaderSPIRV<class_RDShaderSPIRV>`                        | :ref:`get_spirv<class_RDShaderFile_method_get_spirv>`\ (\ version\: :ref:`StringName<class_StringName>` = &""\ ) |const|                                                     |
> +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`StringName<class_StringName>`\] | :ref:`get_version_list<class_RDShaderFile_method_get_version_list>`\ (\ ) |const|                                                                                            |
> +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_bytecode<class_RDShaderFile_method_set_bytecode>`\ (\ bytecode\: :ref:`RDShaderSPIRV<class_RDShaderSPIRV>`, version\: :ref:`StringName<class_StringName>` = &""\ ) |
> +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[String<class_String>] **base_error** = `""` [🔗<class_RDShaderFile_property_base_error>]


- |void| **set_base_error**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_base_error**\ (\ )

The base compilation error message, which indicates errors not related to a specific shader stage if non-empty. If empty, shader compilation is not necessarily successful (check [RDShaderSPIRV<class_RDShaderSPIRV>]'s error message members).


----


## Method Descriptions



[RDShaderSPIRV<class_RDShaderSPIRV>] **get_spirv**\ (\ version\: [StringName<class_StringName>] = &""\ ) |const| [🔗<class_RDShaderFile_method_get_spirv>]

Returns the SPIR-V intermediate representation for the specified shader `version`.


----



[Array<class_Array>]\[[StringName<class_StringName>]\] **get_version_list**\ (\ ) |const| [🔗<class_RDShaderFile_method_get_version_list>]

Returns the list of compiled versions for this shader.


----



|void| **set_bytecode**\ (\ bytecode\: [RDShaderSPIRV<class_RDShaderSPIRV>], version\: [StringName<class_StringName>] = &""\ ) [🔗<class_RDShaderFile_method_set_bytecode>]

Sets the SPIR-V `bytecode` that will be compiled for the specified `version`.

