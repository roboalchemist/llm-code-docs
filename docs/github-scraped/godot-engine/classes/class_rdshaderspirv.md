:github_url: hide



# RDShaderSPIRV

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

SPIR-V intermediate representation as part of an [RDShaderFile<class_RDShaderFile>] (used by [RenderingDevice<class_RenderingDevice>]).


## Description

**RDShaderSPIRV** represents an [RDShaderFile<class_RDShaderFile>]'s [SPIR-V ](https://www.khronos.org/spir/)_ code for various shader stages, as well as possible compilation error messages. SPIR-V is a low-level intermediate shader representation. This intermediate representation is not used directly by GPUs for rendering, but it can be compiled into binary shaders that GPUs can understand. Unlike compiled shaders, SPIR-V is portable across GPU models and driver versions.

This object is used by [RenderingDevice<class_RenderingDevice>].


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>` | :ref:`bytecode_compute<class_RDShaderSPIRV_property_bytecode_compute>`                                         | ``PackedByteArray()`` |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>` | :ref:`bytecode_fragment<class_RDShaderSPIRV_property_bytecode_fragment>`                                       | ``PackedByteArray()`` |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>` | :ref:`bytecode_tesselation_control<class_RDShaderSPIRV_property_bytecode_tesselation_control>`                 | ``PackedByteArray()`` |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>` | :ref:`bytecode_tesselation_evaluation<class_RDShaderSPIRV_property_bytecode_tesselation_evaluation>`           | ``PackedByteArray()`` |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>` | :ref:`bytecode_vertex<class_RDShaderSPIRV_property_bytecode_vertex>`                                           | ``PackedByteArray()`` |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`String<class_String>`                   | :ref:`compile_error_compute<class_RDShaderSPIRV_property_compile_error_compute>`                               | ``""``                |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`String<class_String>`                   | :ref:`compile_error_fragment<class_RDShaderSPIRV_property_compile_error_fragment>`                             | ``""``                |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`String<class_String>`                   | :ref:`compile_error_tesselation_control<class_RDShaderSPIRV_property_compile_error_tesselation_control>`       | ``""``                |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`String<class_String>`                   | :ref:`compile_error_tesselation_evaluation<class_RDShaderSPIRV_property_compile_error_tesselation_evaluation>` | ``""``                |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------+-----------------------+
> | :ref:`String<class_String>`                   | :ref:`compile_error_vertex<class_RDShaderSPIRV_property_compile_error_vertex>`                                 | ``""``                |
> +-----------------------------------------------+----------------------------------------------------------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>` | :ref:`get_stage_bytecode<class_RDShaderSPIRV_method_get_stage_bytecode>`\ (\ stage\: :ref:`ShaderStage<enum_RenderingDevice_ShaderStage>`\ ) |const|                                                   |
> +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                   | :ref:`get_stage_compile_error<class_RDShaderSPIRV_method_get_stage_compile_error>`\ (\ stage\: :ref:`ShaderStage<enum_RenderingDevice_ShaderStage>`\ ) |const|                                         |
> +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                        | :ref:`set_stage_bytecode<class_RDShaderSPIRV_method_set_stage_bytecode>`\ (\ stage\: :ref:`ShaderStage<enum_RenderingDevice_ShaderStage>`, bytecode\: :ref:`PackedByteArray<class_PackedByteArray>`\ ) |
> +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                        | :ref:`set_stage_compile_error<class_RDShaderSPIRV_method_set_stage_compile_error>`\ (\ stage\: :ref:`ShaderStage<enum_RenderingDevice_ShaderStage>`, compile_error\: :ref:`String<class_String>`\ )    |
> +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[PackedByteArray<class_PackedByteArray>] **bytecode_compute** = `PackedByteArray()` [🔗<class_RDShaderSPIRV_property_bytecode_compute>]


- |void| **set_stage_bytecode**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], bytecode\: [PackedByteArray<class_PackedByteArray>]\ )
- [PackedByteArray<class_PackedByteArray>] **get_stage_bytecode**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

The SPIR-V bytecode for the compute shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray<class_PackedByteArray>] for more details.


----



[PackedByteArray<class_PackedByteArray>] **bytecode_fragment** = `PackedByteArray()` [🔗<class_RDShaderSPIRV_property_bytecode_fragment>]


- |void| **set_stage_bytecode**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], bytecode\: [PackedByteArray<class_PackedByteArray>]\ )
- [PackedByteArray<class_PackedByteArray>] **get_stage_bytecode**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

The SPIR-V bytecode for the fragment shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray<class_PackedByteArray>] for more details.


----



[PackedByteArray<class_PackedByteArray>] **bytecode_tesselation_control** = `PackedByteArray()` [🔗<class_RDShaderSPIRV_property_bytecode_tesselation_control>]


- |void| **set_stage_bytecode**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], bytecode\: [PackedByteArray<class_PackedByteArray>]\ )
- [PackedByteArray<class_PackedByteArray>] **get_stage_bytecode**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

The SPIR-V bytecode for the tessellation control shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray<class_PackedByteArray>] for more details.


----



[PackedByteArray<class_PackedByteArray>] **bytecode_tesselation_evaluation** = `PackedByteArray()` [🔗<class_RDShaderSPIRV_property_bytecode_tesselation_evaluation>]


- |void| **set_stage_bytecode**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], bytecode\: [PackedByteArray<class_PackedByteArray>]\ )
- [PackedByteArray<class_PackedByteArray>] **get_stage_bytecode**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

The SPIR-V bytecode for the tessellation evaluation shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray<class_PackedByteArray>] for more details.


----



[PackedByteArray<class_PackedByteArray>] **bytecode_vertex** = `PackedByteArray()` [🔗<class_RDShaderSPIRV_property_bytecode_vertex>]


- |void| **set_stage_bytecode**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], bytecode\: [PackedByteArray<class_PackedByteArray>]\ )
- [PackedByteArray<class_PackedByteArray>] **get_stage_bytecode**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

The SPIR-V bytecode for the vertex shader stage.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray<class_PackedByteArray>] for more details.


----



[String<class_String>] **compile_error_compute** = `""` [🔗<class_RDShaderSPIRV_property_compile_error_compute>]


- |void| **set_stage_compile_error**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], compile_error\: [String<class_String>]\ )
- [String<class_String>] **get_stage_compile_error**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

The compilation error message for the compute shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.


----



[String<class_String>] **compile_error_fragment** = `""` [🔗<class_RDShaderSPIRV_property_compile_error_fragment>]


- |void| **set_stage_compile_error**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], compile_error\: [String<class_String>]\ )
- [String<class_String>] **get_stage_compile_error**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

The compilation error message for the fragment shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.


----



[String<class_String>] **compile_error_tesselation_control** = `""` [🔗<class_RDShaderSPIRV_property_compile_error_tesselation_control>]


- |void| **set_stage_compile_error**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], compile_error\: [String<class_String>]\ )
- [String<class_String>] **get_stage_compile_error**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

The compilation error message for the tessellation control shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.


----



[String<class_String>] **compile_error_tesselation_evaluation** = `""` [🔗<class_RDShaderSPIRV_property_compile_error_tesselation_evaluation>]


- |void| **set_stage_compile_error**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], compile_error\: [String<class_String>]\ )
- [String<class_String>] **get_stage_compile_error**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

The compilation error message for the tessellation evaluation shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.


----



[String<class_String>] **compile_error_vertex** = `""` [🔗<class_RDShaderSPIRV_property_compile_error_vertex>]


- |void| **set_stage_compile_error**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], compile_error\: [String<class_String>]\ )
- [String<class_String>] **get_stage_compile_error**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const|

The compilation error message for the vertex shader stage (set by the SPIR-V compiler and Godot). If empty, shader compilation was successful.


----


## Method Descriptions



[PackedByteArray<class_PackedByteArray>] **get_stage_bytecode**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const| [🔗<class_RDShaderSPIRV_method_get_stage_bytecode>]

Equivalent to getting one of [bytecode_compute<class_RDShaderSPIRV_property_bytecode_compute>], [bytecode_fragment<class_RDShaderSPIRV_property_bytecode_fragment>], [bytecode_tesselation_control<class_RDShaderSPIRV_property_bytecode_tesselation_control>], [bytecode_tesselation_evaluation<class_RDShaderSPIRV_property_bytecode_tesselation_evaluation>], [bytecode_vertex<class_RDShaderSPIRV_property_bytecode_vertex>].


----



[String<class_String>] **get_stage_compile_error**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>]\ ) |const| [🔗<class_RDShaderSPIRV_method_get_stage_compile_error>]

Returns the compilation error message for the given shader `stage`. Equivalent to getting one of [compile_error_compute<class_RDShaderSPIRV_property_compile_error_compute>], [compile_error_fragment<class_RDShaderSPIRV_property_compile_error_fragment>], [compile_error_tesselation_control<class_RDShaderSPIRV_property_compile_error_tesselation_control>], [compile_error_tesselation_evaluation<class_RDShaderSPIRV_property_compile_error_tesselation_evaluation>], [compile_error_vertex<class_RDShaderSPIRV_property_compile_error_vertex>].


----



|void| **set_stage_bytecode**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], bytecode\: [PackedByteArray<class_PackedByteArray>]\ ) [🔗<class_RDShaderSPIRV_method_set_stage_bytecode>]

Sets the SPIR-V `bytecode` for the given shader `stage`. Equivalent to setting one of [bytecode_compute<class_RDShaderSPIRV_property_bytecode_compute>], [bytecode_fragment<class_RDShaderSPIRV_property_bytecode_fragment>], [bytecode_tesselation_control<class_RDShaderSPIRV_property_bytecode_tesselation_control>], [bytecode_tesselation_evaluation<class_RDShaderSPIRV_property_bytecode_tesselation_evaluation>], [bytecode_vertex<class_RDShaderSPIRV_property_bytecode_vertex>].


----



|void| **set_stage_compile_error**\ (\ stage\: [ShaderStage<enum_RenderingDevice_ShaderStage>], compile_error\: [String<class_String>]\ ) [🔗<class_RDShaderSPIRV_method_set_stage_compile_error>]

Sets the compilation error message for the given shader `stage` to `compile_error`. Equivalent to setting one of [compile_error_compute<class_RDShaderSPIRV_property_compile_error_compute>], [compile_error_fragment<class_RDShaderSPIRV_property_compile_error_fragment>], [compile_error_tesselation_control<class_RDShaderSPIRV_property_compile_error_tesselation_control>], [compile_error_tesselation_evaluation<class_RDShaderSPIRV_property_compile_error_tesselation_evaluation>], [compile_error_vertex<class_RDShaderSPIRV_property_compile_error_vertex>].

