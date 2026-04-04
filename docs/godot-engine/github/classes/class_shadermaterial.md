:github_url: hide



# ShaderMaterial

**Inherits:** [Material<class_Material>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A material defined by a custom [Shader<class_Shader>] program and the values of its shader parameters.


## Description

A material that uses a custom [Shader<class_Shader>] program to render visual items (canvas items, meshes, skies, fog), or to process particles. Compared to other materials, **ShaderMaterial** gives deeper control over the generated shader code. For more information, see the shaders documentation index below.

Multiple **ShaderMaterial**\ s can use the same shader and configure different values for the shader uniforms.

\ **Note:** For performance reasons, the [Resource.changed<class_Resource_signal_changed>] signal is only emitted when the [Resource.resource_name<class_Resource_property_resource_name>] changes. Only in editor, it is also emitted for [shader<class_ShaderMaterial_property_shader>] changes.


## Tutorials

- [../tutorials/shaders/index](Shaders documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+-----------------------------------------------------+
> | :ref:`Shader<class_Shader>` | :ref:`shader<class_ShaderMaterial_property_shader>` |
> +-----------------------------+-----------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`get_shader_parameter<class_ShaderMaterial_method_get_shader_parameter>`\ (\ param\: :ref:`StringName<class_StringName>`\ ) |const|                                |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_shader_parameter<class_ShaderMaterial_method_set_shader_parameter>`\ (\ param\: :ref:`StringName<class_StringName>`, value\: :ref:`Variant<class_Variant>`\ ) |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Shader<class_Shader>] **shader** [🔗<class_ShaderMaterial_property_shader>]


- |void| **set_shader**\ (\ value\: [Shader<class_Shader>]\ )
- [Shader<class_Shader>] **get_shader**\ (\ )

The [Shader<class_Shader>] program used to render this material.


----


## Method Descriptions



[Variant<class_Variant>] **get_shader_parameter**\ (\ param\: [StringName<class_StringName>]\ ) |const| [🔗<class_ShaderMaterial_method_get_shader_parameter>]

Returns the current value set for this material of a uniform in the shader.


----



|void| **set_shader_parameter**\ (\ param\: [StringName<class_StringName>], value\: [Variant<class_Variant>]\ ) [🔗<class_ShaderMaterial_method_set_shader_parameter>]

Changes the value set for this material of a uniform in the shader.

\ **Note:** `param` is case-sensitive and must match the name of the uniform in the code exactly (not the capitalized name in the inspector).

\ **Note:** Changes to the shader uniform will be effective on all instances using this **ShaderMaterial**. To prevent this, use per-instance uniforms with [CanvasItem.set_instance_shader_parameter()<class_CanvasItem_method_set_instance_shader_parameter>], [GeometryInstance3D.set_instance_shader_parameter()<class_GeometryInstance3D_method_set_instance_shader_parameter>] or duplicate the **ShaderMaterial** resource using [Resource.duplicate()<class_Resource_method_duplicate>]. Per-instance uniforms allow for better shader reuse and are therefore faster, so they should be preferred over duplicating the **ShaderMaterial** when possible.

