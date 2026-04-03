# VisualShaderNodeTexture

# VisualShaderNodeTexture
Inherits:VisualShaderNode<Resource<RefCounted<Object
Performs a 2D texture lookup within the visual shader graph.

## Description
Performs a lookup operation on the provided texture, with support for multiple texture sources to choose from.

## Properties

| Source | source | 0 |
|---|---|---|
| Texture2D | texture |  |
| TextureType | texture_type | 0 |

Source
source
Texture2D
texture
TextureType
texture_type

## Enumerations
enumSource:🔗
SourceSOURCE_TEXTURE=0
Use the texture given as an argument for this function.
SourceSOURCE_SCREEN=1
Use the current viewport's texture as the source.
SourceSOURCE_2D_TEXTURE=2
Use the texture from this shader's texture built-in (e.g. a texture of aSprite2D).
SourceSOURCE_2D_NORMAL=3
Use the texture from this shader's normal map built-in.
SourceSOURCE_DEPTH=4
Use the depth texture captured during the depth prepass. Only available when the depth prepass is used (i.e. in spatial shaders and in the forward_plus or gl_compatibility renderers).
SourceSOURCE_PORT=5
Use the texture provided in the input port for this function.
SourceSOURCE_3D_NORMAL=6
Use the normal buffer captured during the depth prepass. Only available when the normal-roughness buffer is available (i.e. in spatial shaders and in the forward_plus renderer).
SourceSOURCE_ROUGHNESS=7
Use the roughness buffer captured during the depth prepass. Only available when the normal-roughness buffer is available (i.e. in spatial shaders and in the forward_plus renderer).
SourceSOURCE_MAX=8
Represents the size of theSourceenum.
enumTextureType:🔗
TextureTypeTYPE_DATA=0
No hints are added to the uniform declaration.
TextureTypeTYPE_COLOR=1
Addssource_coloras hint to the uniform declaration for proper conversion from nonlinear sRGB encoding to linear encoding.
TextureTypeTYPE_NORMAL_MAP=2
Addshint_normalas hint to the uniform declaration, which internally converts the texture for proper usage as normal map.
TextureTypeTYPE_MAX=3
Represents the size of theTextureTypeenum.

## Property Descriptions
Sourcesource=0🔗
- voidset_source(value:Source)
voidset_source(value:Source)
- Sourceget_source()
Sourceget_source()
Determines the source for the lookup.
Texture2Dtexture🔗
- voidset_texture(value:Texture2D)
voidset_texture(value:Texture2D)
- Texture2Dget_texture()
Texture2Dget_texture()
The source texture, if needed for the selectedsource.
TextureTypetexture_type=0🔗
- voidset_texture_type(value:TextureType)
voidset_texture_type(value:TextureType)
- TextureTypeget_texture_type()
TextureTypeget_texture_type()
Specifies the type of the texture ifsourceis set toSOURCE_TEXTURE.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.