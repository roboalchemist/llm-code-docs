# OpenXRCompositionLayerEquirect in English

# OpenXRCompositionLayerEquirect
Experimental:This class may be changed or removed in future versions.
Inherits:OpenXRCompositionLayer<Node3D<Node<Object
An OpenXR composition layer that is rendered as an internal slice of a sphere.

## Description
An OpenXR composition layer that allows rendering aSubViewporton an internal slice of a sphere.

## Properties

| float | central_horizontal_angle | 1.5707964 |
|---|---|---|
| int | fallback_segments | 10 |
| float | lower_vertical_angle | 0.7853982 |
| float | radius | 1.0 |
| float | upper_vertical_angle | 0.7853982 |

float
central_horizontal_angle
1.5707964
fallback_segments
float
lower_vertical_angle
0.7853982
float
radius
float
upper_vertical_angle
0.7853982

## Property Descriptions
floatcentral_horizontal_angle=1.5707964🔗
- voidset_central_horizontal_angle(value:float)
voidset_central_horizontal_angle(value:float)
- floatget_central_horizontal_angle()
floatget_central_horizontal_angle()
The central horizontal angle of the sphere. Used to set the width.
intfallback_segments=10🔗
- voidset_fallback_segments(value:int)
voidset_fallback_segments(value:int)
- intget_fallback_segments()
intget_fallback_segments()
The number of segments to use in the fallback mesh.
floatlower_vertical_angle=0.7853982🔗
- voidset_lower_vertical_angle(value:float)
voidset_lower_vertical_angle(value:float)
- floatget_lower_vertical_angle()
floatget_lower_vertical_angle()
The lower vertical angle of the sphere. Used (together withupper_vertical_angle) to set the height.
floatradius=1.0🔗
- voidset_radius(value:float)
voidset_radius(value:float)
- floatget_radius()
floatget_radius()
The radius of the sphere.
floatupper_vertical_angle=0.7853982🔗
- voidset_upper_vertical_angle(value:float)
voidset_upper_vertical_angle(value:float)
- floatget_upper_vertical_angle()
floatget_upper_vertical_angle()
The upper vertical angle of the sphere. Used (together withlower_vertical_angle) to set the height.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.