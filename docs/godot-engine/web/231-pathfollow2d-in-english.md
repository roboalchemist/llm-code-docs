# PathFollow2D in English

# PathFollow2D

Inherits:Node2D<CanvasItem<Node<Object
Point sampler for aPath2D.

## Description

This node takes its parentPath2D, and returns the coordinates of a point within it, given a distance from the first vertex.
It is useful for making other nodes follow a path, without coding the movement pattern. For that, the nodes must be children of this node. The descendant nodes will then move accordingly when setting theprogressin this node.

## Properties

| bool | cubic_interp | true |
|---|---|---|
| float | h_offset | 0.0 |
| bool | loop | true |
| float | progress | 0.0 |
| float | progress_ratio | 0.0 |
| bool | rotates | true |
| float | v_offset | 0.0 |

bool
cubic_interp
true
float
h_offset
bool
loop
true
float
progress
float
progress_ratio
bool
rotates
true
float
v_offset

## Property Descriptions

boolcubic_interp=true🔗

- voidset_cubic_interpolation(value:bool)
voidset_cubic_interpolation(value:bool)
- boolget_cubic_interpolation()
boolget_cubic_interpolation()
Iftrue, the position between two cached points is interpolated cubically, and linearly otherwise.
The points along theCurve2Dof thePath2Dare precomputed before use, for faster calculations. The point at the requested offset is then calculated interpolating between two adjacent cached points. This may present a problem if the curve makes sharp turns, as the cached points may not follow the curve closely enough.
There are two answers to this problem: either increase the number of cached points and increase memory consumption, or make a cubic interpolation between two points at the cost of (slightly) slower calculations.
floath_offset=0.0🔗
- voidset_h_offset(value:float)
voidset_h_offset(value:float)
- floatget_h_offset()
floatget_h_offset()
The node's offset along the curve.
boolloop=true🔗
- voidset_loop(value:bool)
voidset_loop(value:bool)
- boolhas_loop()
boolhas_loop()
Iftrue, any offset outside the path's length will wrap around, instead of stopping at the ends. Use it for cyclic paths.
floatprogress=0.0🔗
- voidset_progress(value:float)
voidset_progress(value:float)
- floatget_progress()
floatget_progress()
The distance along the path, in pixels. Changing this value sets this node's position to a point within the path.
floatprogress_ratio=0.0🔗
- voidset_progress_ratio(value:float)
voidset_progress_ratio(value:float)
- floatget_progress_ratio()
floatget_progress_ratio()
The distance along the path as a number in the range 0.0 (for the first vertex) to 1.0 (for the last). This is just another way of expressing the progress within the path, as the offset supplied is multiplied internally by the path's length.
It can be set or get only if thePathFollow2Dis the child of aPath2Dwhich is part of the scene tree, and that thisPath2Dhas aCurve2Dwith a non-zero length. Otherwise, trying to set this field will print an error, and getting this field will return0.0.
boolrotates=true🔗
- voidset_rotates(value:bool)
voidset_rotates(value:bool)
- boolis_rotating()
boolis_rotating()
Iftrue, this node rotates to follow the path, with the +X direction facing forward on the path.
floatv_offset=0.0🔗
- voidset_v_offset(value:float)
voidset_v_offset(value:float)
- floatget_v_offset()
floatget_v_offset()
The node's offset perpendicular to the curve.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
