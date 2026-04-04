# VisualShaderNodeUVFunc in English

# VisualShaderNodeUVFunc

Inherits:VisualShaderNode<Resource<RefCounted<Object
Contains functions to modify texture coordinates (uv) to be used within the visual shader graph.

## Description

UV functions are similar toVector2functions, but the input port of this node uses the shader's UV value by default.

## Properties

| Function | function | 0 |

Function
function

## Enumerations

enumFunction:🔗
FunctionFUNC_PANNING=0
Translatesuvby usingscaleandoffsetvalues using the following formula:uv=uv+offset*scale.uvport is connected toUVbuilt-in by default.
FunctionFUNC_SCALING=1
Scalesuvby usingscaleandpivotvalues using the following formula:uv=(uv-pivot)*scale+pivot.uvport is connected toUVbuilt-in by default.
FunctionFUNC_MAX=2
Represents the size of theFunctionenum.

## Property Descriptions

Functionfunction=0🔗

- voidset_function(value:Function)
voidset_function(value:Function)
- Functionget_function()
Functionget_function()
A function to be applied to the texture coordinates.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
