# Shader

# Shader

Inherits:Resource<RefCounted<Object
Inherited By:VisualShader
A shader implemented in the Godot shading language.

## Description

A custom shader program implemented in the Godot shading language, saved with the.gdshaderextension.
This class is used by aShaderMaterialand allows you to write your own custom behavior for rendering visual items or updating particle information. For a detailed explanation and usage, please see the tutorials linked below.

## Tutorials

- Shaders documentation index
Shaders documentation index

## Properties

| String | code | "" |

String
code

## Methods

| Texture | get_default_texture_parameter(name:StringName, index:int= 0)const |
|---|---|
| Mode | get_mode()const |
| Array | get_shader_uniform_list(get_groups:bool= false) |
| void | inspect_native_shader_code() |
| void | set_default_texture_parameter(name:StringName, texture:Texture, index:int= 0) |

Texture
get_default_texture_parameter(name:StringName, index:int= 0)const
Mode
get_mode()const
Array
get_shader_uniform_list(get_groups:bool= false)
void
inspect_native_shader_code()
void
set_default_texture_parameter(name:StringName, texture:Texture, index:int= 0)

## Enumerations

enumMode:🔗
ModeMODE_SPATIAL=0
Mode used to draw all 3D objects.
ModeMODE_CANVAS_ITEM=1
Mode used to draw all 2D objects.
ModeMODE_PARTICLES=2
Mode used to calculate particle information on a per-particle basis. Not used for drawing.
ModeMODE_SKY=3
Mode used for drawing skies. Only works with shaders attached toSkyobjects.
ModeMODE_FOG=4
Mode used for setting the color and density of volumetric fog effect.

## Property Descriptions

Stringcode=""🔗

- voidset_code(value:String)
voidset_code(value:String)
- Stringget_code()
Stringget_code()
Returns the shader's code as the user has written it, not the full generated code used internally.

## Method Descriptions

Textureget_default_texture_parameter(name:StringName, index:int= 0)const🔗
Returns the texture that is set as default for the specified parameter.
Note:namemust match the name of the uniform in the code exactly.
Note:If the sampler array is used useindexto access the specified texture.
Modeget_mode()const🔗
Returns the shader mode for the shader.
Arrayget_shader_uniform_list(get_groups:bool= false)🔗
Returns the list of shader uniforms that can be assigned to aShaderMaterial, for use withShaderMaterial.set_shader_parameter()andShaderMaterial.get_shader_parameter(). The parameters returned are contained in dictionaries in a similar format to the ones returned byObject.get_property_list().
If argumentget_groupsistrue, parameter grouping hints are also included in the list.
voidinspect_native_shader_code()🔗
Only available when running in the editor. Opens a popup that visualizes the generated shader code, including all variants and internal shader code. See alsoMaterial.inspect_native_shader_code().
voidset_default_texture_parameter(name:StringName, texture:Texture, index:int= 0)🔗
Sets the default texture to be used with a texture uniform. The default is used if a texture is not set in theShaderMaterial.
Note:namemust match the name of the uniform in the code exactly.
Note:If the sampler array is used useindexto access the specified texture.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
