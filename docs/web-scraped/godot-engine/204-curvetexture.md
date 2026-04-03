# CurveTexture

# CurveTexture

Inherits:Texture2D<Texture<Resource<RefCounted<Object
A 1D texture where pixel brightness corresponds to points on a curve.

## Description

A 1D texture where pixel brightness corresponds to points on a unitCurveresource, either in grayscale or in red. This visual representation simplifies the task of saving curves as image files.
If you need to store up to 3 curves within a single texture, useCurveXYZTextureinstead. See alsoGradientTexture1DandGradientTexture2D.

## Properties

| Curve | curve |  |
|---|---|---|
| bool | resource_local_to_scene | false(overridesResource) |
| TextureMode | texture_mode | 0 |
| int | width | 256 |

Curve
curve
bool
resource_local_to_scene
false(overridesResource)
TextureMode
texture_mode
width

## Enumerations

enumTextureMode:🔗
TextureModeTEXTURE_MODE_RGB=0
Store the curve equally across the red, green and blue channels. This uses more video memory, but is more compatible with shaders that only read the green and blue values.
TextureModeTEXTURE_MODE_RED=1
Store the curve only in the red channel. This saves video memory, but some custom shaders may not be able to work with this.

## Property Descriptions

Curvecurve🔗

- voidset_curve(value:Curve)
voidset_curve(value:Curve)
- Curveget_curve()
Curveget_curve()
TheCurvethat is rendered onto the texture. Should be a unitCurve.
TextureModetexture_mode=0🔗
- voidset_texture_mode(value:TextureMode)
voidset_texture_mode(value:TextureMode)
- TextureModeget_texture_mode()
TextureModeget_texture_mode()
The format the texture should be generated with. When passing a CurveTexture as an input to aShader, this may need to be adjusted.
intwidth=256🔗
- voidset_width(value:int)
voidset_width(value:int)
- intget_width()
intget_width()
The width of the texture (in pixels). Higher values make it possible to represent high-frequency data better (such as sudden direction changes), at the cost of increased generation time and memory usage.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
