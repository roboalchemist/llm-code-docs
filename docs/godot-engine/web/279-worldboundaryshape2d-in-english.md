# WorldBoundaryShape2D in English

# WorldBoundaryShape2D

Inherits:Shape2D<Resource<RefCounted<Object
A 2D world boundary (half-plane) shape used for physics collision.

## Description

A 2D world boundary shape, intended for use in physics.WorldBoundaryShape2Dworks like an infinite straight line that forces all physics bodies to stay above it. The line's normal determines which direction is considered as "above" and in the editor, the smaller line over it represents this direction. It can for example be used for endless flat floors.

## Properties

| float | distance | 0.0 |
|---|---|---|
| Vector2 | normal | Vector2(0,-1) |

float
distance
Vector2
normal
Vector2(0,-1)

## Property Descriptions

floatdistance=0.0🔗

- voidset_distance(value:float)
voidset_distance(value:float)
- floatget_distance()
floatget_distance()
The distance from the origin to the line, expressed in terms ofnormal(according to its direction and magnitude). Actual absolute distance from the origin to the line can be calculated asabs(distance)/normal.length().
In the scalar equation of the lineax+by=d, this isd, while the(a,b)coordinates are represented by thenormalproperty.
Vector2normal=Vector2(0,-1)🔗
- voidset_normal(value:Vector2)
voidset_normal(value:Vector2)
- Vector2get_normal()
Vector2get_normal()
The line's normal, typically a unit vector. Its direction indicates the non-colliding half-plane. Can be of any length but zero. Defaults toVector2.UP.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
