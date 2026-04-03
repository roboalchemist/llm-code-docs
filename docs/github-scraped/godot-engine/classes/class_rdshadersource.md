:github_url: hide



# RDShaderSource

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Shader source code (used by [RenderingDevice<class_RenderingDevice>]).


## Description

Shader source code in text form.

See also [RDShaderFile<class_RDShaderFile>]. **RDShaderSource** is only meant to be used with the [RenderingDevice<class_RenderingDevice>] API. It should not be confused with Godot's own [Shader<class_Shader>] resource, which is what Godot's various nodes use for high-level shader programming.


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------+
> | :ref:`ShaderLanguage<enum_RenderingDevice_ShaderLanguage>` | :ref:`language<class_RDShaderSource_property_language>`                                           | ``0``  |
> +------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------+
> | :ref:`String<class_String>`                                | :ref:`source_compute<class_RDShaderSource_property_source_compute>`                               | ``""`` |
> +------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------+
> | :ref:`String<class_String>`                                | :ref:`source_fragment<class_RDShaderSource_property_source_fragment>`                             | ``""`` |
> +------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------+
> | :ref:`String<class_String>`                                | :ref:`source_tesselation_control<class_RDShaderSource_property_source_tesselation_control>`       | ``""`` |
> +------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------+
> | :ref:`String<class_String>`                                | :ref:`source_tesselation_evaluation<class_RDShaderSource_property_source_tesselation_evaluation>` | ``""`` |
> +------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------+
> | :ref:`String<class_String>`                                | :ref:`source_vertex<class_RDShaderSource_property_source_vertex>`                                 | ``""`` |
> +------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`get_stage_source<class_RDShaderSource_method_get_stage_source>`\ (\ stage\: :ref:`ShaderStage<enum_RenderingDevice_ShaderStage>`\ ) |const|                               |
> +-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`set_stage_source<class_RDShaderSource_method_set_stage_source>`\ (\ stage\: :ref:`ShaderStage<enum_RenderingDevice_ShaderStage>`, source\: :ref:`String<class_String>`\ ) |
> +-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[ShaderLanguage<enum_RenderingDevice_ShaderLanguage>] **language** = `0` [🔗<class_RDShaderSource_property_language>]


- |void| **set_language**\ (\ value\: [ShaderLanguage<enum_RenderingDevice_ShaderLanguage>]\ )
- [ShaderLanguage<enum_RenderingDevice_ShaderLanguage>] **get_language**\ (\ )

The language the shader is written in.


----



[String<class_String>] **source_compute** = `""` [🔗<class_RDShaderSource_property_source_compute>]


- |void| **set_stage_source**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], source\: [String<class_String>]\ )
- [String<class_String>] **get_stage_source**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

Source code for the shader's compute stage.


----



[String<class_String>] **source_fragment** = `""` [🔗<class_RDShaderSource_property_source_fragment>]


- |void| **set_stage_source**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], source\: [String<class_String>]\ )
- [String<class_String>] **get_stage_source**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

Source code for the shader's fragment stage.


----



[String<class_String>] **source_tesselation_control** = `""` [🔗<class_RDShaderSource_property_source_tesselation_control>]


- |void| **set_stage_source**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], source\: [String<class_String>]\ )
- [String<class_String>] **get_stage_source**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

Source code for the shader's tessellation control stage.


----



[String<class_String>] **source_tesselation_evaluation** = `""` [🔗<class_RDShaderSource_property_source_tesselation_evaluation>]


- |void| **set_stage_source**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], source\: [String<class_String>]\ )
- [String<class_String>] **get_stage_source**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

Source code for the shader's tessellation evaluation stage.


----



[String<class_String>] **source_vertex** = `""` [🔗<class_RDShaderSource_property_source_vertex>]


- |void| **set_stage_source**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], source\: [String<class_String>]\ )
- [String<class_String>] **get_stage_source**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

Source code for the shader's vertex stage.


----


## Method Descriptions



[String<class_String>] **get_stage_source**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const| [🔗<class_RDShaderSource_method_get_stage_source>]

Returns source code for the specified shader `stage`. Equivalent to getting one of [source_compute<class_RDShaderSource_property_source_compute>], [source_fragment<class_RDShaderSource_property_source_fragment>], [source_tesselation_control<class_RDShaderSource_property_source_tesselation_control>], [source_tesselation_evaluation<class_RDShaderSource_property_source_tesselation_evaluation>] or [source_vertex<class_RDShaderSource_property_source_vertex>].


----



|void| **set_stage_source**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], source\: [String<class_String>]\ ) [🔗<class_RDShaderSource_method_set_stage_source>]

Sets `source` code for the specified shader `stage`. Equivalent to setting one of [source_compute<class_RDShaderSource_property_source_compute>], [source_fragment<class_RDShaderSource_property_source_fragment>], [source_tesselation_control<class_RDShaderSource_property_source_tesselation_control>], [source_tesselation_evaluation<class_RDShaderSource_property_source_tesselation_evaluation>] or [source_vertex<class_RDShaderSource_property_source_vertex>].

\ **Note:** If you set the compute shader source code using this method directly, remember to remove the Godot-specific hint `#[compute]`.

