# Gradient in English

# Gradient
Inherits:Resource<RefCounted<Object
A color transition.

## Description
This resource describes a color transition by defining a set of colored points and how to interpolate between them.
See alsoCurvewhich supports more complex easing methods, but does not support colors.

## Properties

| PackedColorArray | colors | PackedColorArray(0,0,0,1,1,1,1,1) |
|---|---|---|
| ColorSpace | interpolation_color_space | 0 |
| InterpolationMode | interpolation_mode | 0 |
| PackedFloat32Array | offsets | PackedFloat32Array(0,1) |

PackedColorArray
colors
PackedColorArray(0,0,0,1,1,1,1,1)
ColorSpace
interpolation_color_space
InterpolationMode
interpolation_mode
PackedFloat32Array
offsets
PackedFloat32Array(0,1)

## Methods

| void | add_point(offset:float, color:Color) |
|---|---|
| Color | get_color(point:int) |
| float | get_offset(point:int) |
| int | get_point_count()const |
| void | remove_point(point:int) |
| void | reverse() |
| Color | sample(offset:float) |
| void | set_color(point:int, color:Color) |
| void | set_offset(point:int, offset:float) |

void
add_point(offset:float, color:Color)
Color
get_color(point:int)
float
get_offset(point:int)
get_point_count()const
void
remove_point(point:int)
void
reverse()
Color
sample(offset:float)
void
set_color(point:int, color:Color)
void
set_offset(point:int, offset:float)

## Enumerations
enumInterpolationMode:🔗
InterpolationModeGRADIENT_INTERPOLATE_LINEAR=0
Linear interpolation.
InterpolationModeGRADIENT_INTERPOLATE_CONSTANT=1
Constant interpolation, color changes abruptly at each point and stays uniform between. This might cause visible aliasing when used for a gradient texture in some cases.
InterpolationModeGRADIENT_INTERPOLATE_CUBIC=2
Cubic interpolation.
enumColorSpace:🔗
ColorSpaceGRADIENT_COLOR_SPACE_SRGB=0
sRGB color space.
ColorSpaceGRADIENT_COLOR_SPACE_LINEAR_SRGB=1
Linear sRGB color space.
ColorSpaceGRADIENT_COLOR_SPACE_OKLAB=2
Oklabcolor space. This color space provides a smooth and uniform-looking transition between colors.

## Property Descriptions
PackedColorArraycolors=PackedColorArray(0,0,0,1,1,1,1,1)🔗
- voidset_colors(value:PackedColorArray)
voidset_colors(value:PackedColorArray)
- PackedColorArrayget_colors()
PackedColorArrayget_colors()
Gradient's colors as aPackedColorArray.
Note:Setting this property updates all colors at once. To update any color individually useset_color().
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedColorArrayfor more details.
ColorSpaceinterpolation_color_space=0🔗
- voidset_interpolation_color_space(value:ColorSpace)
voidset_interpolation_color_space(value:ColorSpace)
- ColorSpaceget_interpolation_color_space()
ColorSpaceget_interpolation_color_space()
The color space used to interpolate between points of the gradient. It does not affect the returned colors, which will always use nonlinear sRGB encoding.
Note:This setting has no effect wheninterpolation_modeis set toGRADIENT_INTERPOLATE_CONSTANT.
InterpolationModeinterpolation_mode=0🔗
- voidset_interpolation_mode(value:InterpolationMode)
voidset_interpolation_mode(value:InterpolationMode)
- InterpolationModeget_interpolation_mode()
InterpolationModeget_interpolation_mode()
The algorithm used to interpolate between points of the gradient.
PackedFloat32Arrayoffsets=PackedFloat32Array(0,1)🔗
- voidset_offsets(value:PackedFloat32Array)
voidset_offsets(value:PackedFloat32Array)
- PackedFloat32Arrayget_offsets()
PackedFloat32Arrayget_offsets()
Gradient's offsets as aPackedFloat32Array.
Note:Setting this property updates all offsets at once. To update any offset individually useset_offset().
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedFloat32Arrayfor more details.

## Method Descriptions
voidadd_point(offset:float, color:Color)🔗
Adds the specified color to the gradient, with the specified offset.
Colorget_color(point:int)🔗
Returns the color of the gradient color at indexpoint.
floatget_offset(point:int)🔗
Returns the offset of the gradient color at indexpoint.
intget_point_count()const🔗
Returns the number of colors in the gradient.
voidremove_point(point:int)🔗
Removes the color at indexpoint.
voidreverse()🔗
Reverses/mirrors the gradient.
Note:This method mirrors all points around the middle of the gradient, which may produce unexpected results wheninterpolation_modeis set toGRADIENT_INTERPOLATE_CONSTANT.
Colorsample(offset:float)🔗
Returns the interpolated color specified byoffset.offsetshould be between0.0and1.0(inclusive). Using a value lower than0.0will return the same color as0.0, and using a value higher than1.0will return the same color as1.0. If your input value is not within this range, consider using@GlobalScope.remap()on the input value with output values set to0.0and1.0.
voidset_color(point:int, color:Color)🔗
Sets the color of the gradient color at indexpoint.
voidset_offset(point:int, offset:float)🔗
Sets the offset for the gradient color at indexpoint.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.