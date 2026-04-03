# ShaderInclude in English

# ShaderInclude
Inherits:Resource<RefCounted<Object
A snippet of shader code to be included in aShaderwith#include.

## Description
A shader include file, saved with the.gdshaderincextension. This class allows you to define a custom shader snippet that can be included in aShaderby using the preprocessor directive#include, followed by the file path (e.g.#include"res://shader_lib.gdshaderinc"). The snippet doesn't have to be a valid shader on its own.

## Tutorials
- Shader preprocessor
Shader preprocessor

## Properties

| String | code | "" |

String
code

## Property Descriptions
Stringcode=""🔗
- voidset_code(value:String)
voidset_code(value:String)
- Stringget_code()
Stringget_code()
Returns the code of the shader include file. The returned text is what the user has written, not the full generated code used internally.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.