# Curve in English

# Curve

Inherits:Resource<RefCounted<Object
A mathematical curve.

## Description

This resource describes a mathematical curve by defining a set of points and tangents at each point. By default, it ranges between0and1on the X and Y axes, but these ranges can be changed.
Please note that many resources and nodes assume they are givenunit curves. A unit curve is a curve whose domain (the X axis) is between0and1. Some examples of unit curve usage areCPUParticles2D.angle_curveandLine2D.width_curve.

## Properties

| int | bake_resolution | 100 |
|---|---|---|
| float | max_domain | 1.0 |
| float | max_value | 1.0 |
| float | min_domain | 0.0 |
| float | min_value | 0.0 |
| int | point_count | 0 |

bake_resolution
float
max_domain
float
max_value
float
min_domain
float
min_value
point_count

## Methods

| int | add_point(position:Vector2, left_tangent:float= 0, right_tangent:float= 0, left_mode:TangentMode= 0, right_mode:TangentMode= 0) |
|---|---|
| void | bake() |
| void | clean_dupes() |
| void | clear_points() |
| float | get_domain_range()const |
| TangentMode | get_point_left_mode(index:int)const |
| float | get_point_left_tangent(index:int)const |
| Vector2 | get_point_position(index:int)const |
| TangentMode | get_point_right_mode(index:int)const |
| float | get_point_right_tangent(index:int)const |
| float | get_value_range()const |
| void | remove_point(index:int) |
| float | sample(offset:float)const |
| float | sample_baked(offset:float)const |
| void | set_point_left_mode(index:int, mode:TangentMode) |
| void | set_point_left_tangent(index:int, tangent:float) |
| int | set_point_offset(index:int, offset:float) |
| void | set_point_right_mode(index:int, mode:TangentMode) |
| void | set_point_right_tangent(index:int, tangent:float) |
| void | set_point_value(index:int, y:float) |

add_point(position:Vector2, left_tangent:float= 0, right_tangent:float= 0, left_mode:TangentMode= 0, right_mode:TangentMode= 0)
void
bake()
void
clean_dupes()
void
clear_points()
float
get_domain_range()const
TangentMode
get_point_left_mode(index:int)const
float
get_point_left_tangent(index:int)const
Vector2
get_point_position(index:int)const
TangentMode
get_point_right_mode(index:int)const
float
get_point_right_tangent(index:int)const
float
get_value_range()const
void
remove_point(index:int)
float
sample(offset:float)const
float
sample_baked(offset:float)const
void
set_point_left_mode(index:int, mode:TangentMode)
void
set_point_left_tangent(index:int, tangent:float)
set_point_offset(index:int, offset:float)
void
set_point_right_mode(index:int, mode:TangentMode)
void
set_point_right_tangent(index:int, tangent:float)
void
set_point_value(index:int, y:float)

## Signals

domain_changed()🔗
Emitted whenmax_domainormin_domainis changed.
range_changed()🔗
Emitted whenmax_valueormin_valueis changed.

## Enumerations

enumTangentMode:🔗
TangentModeTANGENT_FREE=0
The tangent on this side of the point is user-defined.
TangentModeTANGENT_LINEAR=1
The curve calculates the tangent on this side of the point as the slope halfway towards the adjacent point.
TangentModeTANGENT_MODE_COUNT=2
The total number of available tangent modes.

## Property Descriptions

intbake_resolution=100🔗

- voidset_bake_resolution(value:int)
voidset_bake_resolution(value:int)
- intget_bake_resolution()
intget_bake_resolution()
The number of points to include in the baked (i.e. cached) curve data.
floatmax_domain=1.0🔗
- voidset_max_domain(value:float)
voidset_max_domain(value:float)
- floatget_max_domain()
floatget_max_domain()
The maximum domain (x-coordinate) that points can have.
floatmax_value=1.0🔗
- voidset_max_value(value:float)
voidset_max_value(value:float)
- floatget_max_value()
floatget_max_value()
The maximum value (y-coordinate) that points can have. Tangents can cause higher values between points.
floatmin_domain=0.0🔗
- voidset_min_domain(value:float)
voidset_min_domain(value:float)
- floatget_min_domain()
floatget_min_domain()
The minimum domain (x-coordinate) that points can have.
floatmin_value=0.0🔗
- voidset_min_value(value:float)
voidset_min_value(value:float)
- floatget_min_value()
floatget_min_value()
The minimum value (y-coordinate) that points can have. Tangents can cause lower values between points.
intpoint_count=0🔗
- voidset_point_count(value:int)
voidset_point_count(value:int)
- intget_point_count()
intget_point_count()
The number of points describing the curve.

## Method Descriptions

intadd_point(position:Vector2, left_tangent:float= 0, right_tangent:float= 0, left_mode:TangentMode= 0, right_mode:TangentMode= 0)🔗
Adds a point to the curve. For each side, if the*_modeisTANGENT_LINEAR, the*_tangentangle (in degrees) uses the slope of the curve halfway to the adjacent point. Allows custom assignments to the*_tangentangle if*_modeis set toTANGENT_FREE.
voidbake()🔗
Recomputes the baked cache of points for the curve.
voidclean_dupes()🔗
Removes duplicate points, i.e. points that are less than 0.00001 units (engine epsilon value) away from their neighbor on the curve.
voidclear_points()🔗
Removes all points from the curve.
floatget_domain_range()const🔗
Returns the difference betweenmin_domainandmax_domain.
TangentModeget_point_left_mode(index:int)const🔗
Returns the leftTangentModefor the point atindex.
floatget_point_left_tangent(index:int)const🔗
Returns the left tangent angle (in degrees) for the point atindex.
Vector2get_point_position(index:int)const🔗
Returns the curve coordinates for the point atindex.
TangentModeget_point_right_mode(index:int)const🔗
Returns the rightTangentModefor the point atindex.
floatget_point_right_tangent(index:int)const🔗
Returns the right tangent angle (in degrees) for the point atindex.
floatget_value_range()const🔗
Returns the difference betweenmin_valueandmax_value.
voidremove_point(index:int)🔗
Removes the point atindexfrom the curve.
floatsample(offset:float)const🔗
Returns the Y value for the point that would exist at the X positionoffsetalong the curve.
floatsample_baked(offset:float)const🔗
Returns the Y value for the point that would exist at the X positionoffsetalong the curve using the baked cache. Bakes the curve's points if not already baked.
voidset_point_left_mode(index:int, mode:TangentMode)🔗
Sets the leftTangentModefor the point atindextomode.
voidset_point_left_tangent(index:int, tangent:float)🔗
Sets the left tangent angle for the point atindextotangent.
intset_point_offset(index:int, offset:float)🔗
Sets the offset from0.5.
voidset_point_right_mode(index:int, mode:TangentMode)🔗
Sets the rightTangentModefor the point atindextomode.
voidset_point_right_tangent(index:int, tangent:float)🔗
Sets the right tangent angle for the point atindextotangent.
voidset_point_value(index:int, y:float)🔗
Assigns the vertical positionyto the point atindex.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
