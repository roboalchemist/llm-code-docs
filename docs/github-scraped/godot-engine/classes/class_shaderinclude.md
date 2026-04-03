:github_url: hide



# ShaderInclude

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A snippet of shader code to be included in a [Shader<class_Shader>] with `#include`.


## Description

A shader include file, saved with the `.gdshaderinc` extension. This class allows you to define a custom shader snippet that can be included in a [Shader<class_Shader>] by using the preprocessor directive `#include`, followed by the file path (e.g. `#include "res://shader_lib.gdshaderinc"`). The snippet doesn't have to be a valid shader on its own.


## Tutorials

- [../tutorials/shaders/shader_reference/shader_preprocessor](Shader preprocessor .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+------------------------------------------------+--------+
> | :ref:`String<class_String>` | :ref:`code<class_ShaderInclude_property_code>` | ``""`` |
> +-----------------------------+------------------------------------------------+--------+
>

----


## Property Descriptions



[String<class_String>] **code** = `""` [🔗<class_ShaderInclude_property_code>]


- |void| **set_code**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_code**\ (\ )

Returns the code of the shader include file. The returned text is what the user has written, not the full generated code used internally.

