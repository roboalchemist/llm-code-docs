# VisualShaderNodeVarying

# VisualShaderNodeVarying
Inherits:VisualShaderNode<Resource<RefCounted<Object
Inherited By:VisualShaderNodeVaryingGetter,VisualShaderNodeVaryingSetter
A visual shader node that represents a "varying" shader value.

## Description
Varying values are shader variables that can be passed between shader functions, e.g. from Vertex shader to Fragment shader.

## Properties

| String | varying_name | "[None]" |
|---|---|---|
| VaryingType | varying_type | 0 |

String
varying_name
"[None]"
VaryingType
varying_type

## Property Descriptions
Stringvarying_name="[None]"🔗
- voidset_varying_name(value:String)
voidset_varying_name(value:String)
- Stringget_varying_name()
Stringget_varying_name()
Name of the variable. Must be unique.
VaryingTypevarying_type=0🔗
- voidset_varying_type(value:VaryingType)
voidset_varying_type(value:VaryingType)
- VaryingTypeget_varying_type()
VaryingTypeget_varying_type()
Type of the variable. Determines where the variable can be accessed.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.