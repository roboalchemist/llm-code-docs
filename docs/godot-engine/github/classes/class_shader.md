:github_url: hide



# Shader

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [VisualShader<class_VisualShader>]

A shader implemented in the Godot shading language.


## Description

A custom shader program implemented in the Godot shading language, saved with the `.gdshader` extension.

This class is used by a [ShaderMaterial<class_ShaderMaterial>] and allows you to write your own custom behavior for rendering visual items or updating particle information. For a detailed explanation and usage, please see the tutorials linked below.


## Tutorials

- [../tutorials/shaders/index](Shaders documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+-----------------------------------------+--------+
> | :ref:`String<class_String>` | :ref:`code<class_Shader_property_code>` | ``""`` |
> +-----------------------------+-----------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture<class_Texture>` | :ref:`get_default_texture_parameter<class_Shader_method_get_default_texture_parameter>`\ (\ name\: :ref:`StringName<class_StringName>`, index\: :ref:`int<class_int>` = 0\ ) |const|                                  |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Mode<enum_Shader_Mode>` | :ref:`get_mode<class_Shader_method_get_mode>`\ (\ ) |const|                                                                                                                                                           |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`     | :ref:`get_shader_uniform_list<class_Shader_method_get_shader_uniform_list>`\ (\ get_groups\: :ref:`bool<class_bool>` = false\ )                                                                                       |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`inspect_native_shader_code<class_Shader_method_inspect_native_shader_code>`\ (\ )                                                                                                                               |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_default_texture_parameter<class_Shader_method_set_default_texture_parameter>`\ (\ name\: :ref:`StringName<class_StringName>`, texture\: :ref:`Texture<class_Texture>`, index\: :ref:`int<class_int>` = 0\ ) |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Mode**: [🔗<enum_Shader_Mode>]



[Mode<enum_Shader_Mode>] **MODE_SPATIAL** = `0`

Mode used to draw all 3D objects.



[Mode<enum_Shader_Mode>] **MODE_CANVAS_ITEM** = `1`

Mode used to draw all 2D objects.



[Mode<enum_Shader_Mode>] **MODE_PARTICLES** = `2`

Mode used to calculate particle information on a per-particle basis. Not used for drawing.



[Mode<enum_Shader_Mode>] **MODE_SKY** = `3`

Mode used for drawing skies. Only works with shaders attached to [Sky<class_Sky>] objects.



[Mode<enum_Shader_Mode>] **MODE_FOG** = `4`

Mode used for setting the color and density of volumetric fog effect.


----


## Property Descriptions



[String<class_String>] **code** = `""` [🔗<class_Shader_property_code>]


- |void| **set_code**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_code**\ (\ )

Returns the shader's code as the user has written it, not the full generated code used internally.


----


## Method Descriptions



[Texture<class_Texture>] **get_default_texture_parameter**\ (\ name\: [StringName<class_StringName>], index\: [int<class_int>] = 0\ ) |const| [🔗<class_Shader_method_get_default_texture_parameter>]

Returns the texture that is set as default for the specified parameter.

\ **Note:** `name` must match the name of the uniform in the code exactly.

\ **Note:** If the sampler array is used use `index` to access the specified texture.


----



[Mode<enum_Shader_Mode>] **get_mode**\ (\ ) |const| [🔗<class_Shader_method_get_mode>]

Returns the shader mode for the shader.


----



[Array<class_Array>] **get_shader_uniform_list**\ (\ get_groups\: [bool<class_bool>] = false\ ) [🔗<class_Shader_method_get_shader_uniform_list>]

Returns the list of shader uniforms that can be assigned to a [ShaderMaterial<class_ShaderMaterial>], for use with [ShaderMaterial.set_shader_parameter()<class_ShaderMaterial_method_set_shader_parameter>] and [ShaderMaterial.get_shader_parameter()<class_ShaderMaterial_method_get_shader_parameter>]. The parameters returned are contained in dictionaries in a similar format to the ones returned by [Object.get_property_list()<class_Object_method_get_property_list>].

If argument `get_groups` is `true`, parameter grouping hints are also included in the list.


----



|void| **inspect_native_shader_code**\ (\ ) [🔗<class_Shader_method_inspect_native_shader_code>]

Only available when running in the editor. Opens a popup that visualizes the generated shader code, including all variants and internal shader code. See also [Material.inspect_native_shader_code()<class_Material_method_inspect_native_shader_code>].


----



|void| **set_default_texture_parameter**\ (\ name\: [StringName<class_StringName>], texture\: [Texture<class_Texture>], index\: [int<class_int>] = 0\ ) [🔗<class_Shader_method_set_default_texture_parameter>]

Sets the default texture to be used with a texture uniform. The default is used if a texture is not set in the [ShaderMaterial<class_ShaderMaterial>].

\ **Note:** `name` must match the name of the uniform in the code exactly.

\ **Note:** If the sampler array is used use `index` to access the specified texture.

