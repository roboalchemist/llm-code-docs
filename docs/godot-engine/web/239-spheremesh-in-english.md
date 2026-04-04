# SphereMesh in English

# SphereMesh

Inherits:PrimitiveMesh<Mesh<Resource<RefCounted<Object
Class representing a sphericalPrimitiveMesh.

## Description

Class representing a sphericalPrimitiveMesh.

## Properties

| float | height | 1.0 |
|---|---|---|
| bool | is_hemisphere | false |
| int | radial_segments | 64 |
| float | radius | 0.5 |
| int | rings | 32 |

float
height
bool
is_hemisphere
false
radial_segments
float
radius
rings

## Property Descriptions

floatheight=1.0🔗

- voidset_height(value:float)
voidset_height(value:float)
- floatget_height()
floatget_height()
Full height of the sphere.
boolis_hemisphere=false🔗
- voidset_is_hemisphere(value:bool)
voidset_is_hemisphere(value:bool)
- boolget_is_hemisphere()
boolget_is_hemisphere()
Iftrue, a hemisphere is created rather than a full sphere.
Note:To get a regular hemisphere, the height and radius of the sphere must be equal.
intradial_segments=64🔗
- voidset_radial_segments(value:int)
voidset_radial_segments(value:int)
- intget_radial_segments()
intget_radial_segments()
Number of radial segments on the sphere.
floatradius=0.5🔗
- voidset_radius(value:float)
voidset_radius(value:float)
- floatget_radius()
floatget_radius()
Radius of sphere.
intrings=32🔗
- voidset_rings(value:int)
voidset_rings(value:int)
- intget_rings()
intget_rings()
Number of segments along the height of the sphere.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
