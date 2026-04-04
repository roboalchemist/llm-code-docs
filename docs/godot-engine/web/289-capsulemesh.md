# CapsuleMesh

# CapsuleMesh
Inherits:PrimitiveMesh<Mesh<Resource<RefCounted<Object
Class representing a capsule-shapedPrimitiveMesh.

## Description
Class representing a capsule-shapedPrimitiveMesh.

## Properties

| float | height | 2.0 |
|---|---|---|
| int | radial_segments | 64 |
| float | radius | 0.5 |
| int | rings | 8 |

float
height
radial_segments
float
radius
rings

## Property Descriptions
floatheight=2.0🔗
- voidset_height(value:float)
voidset_height(value:float)
- floatget_height()
floatget_height()
Total height of the capsule mesh (including the hemispherical ends).
Note:Theheightof a capsule must be at least twice itsradius. Otherwise, the capsule becomes a circle. If theheightis less than twice theradius, the properties adjust to a valid value.
intradial_segments=64🔗
- voidset_radial_segments(value:int)
voidset_radial_segments(value:int)
- intget_radial_segments()
intget_radial_segments()
Number of radial segments on the capsule mesh.
floatradius=0.5🔗
- voidset_radius(value:float)
voidset_radius(value:float)
- floatget_radius()
floatget_radius()
Radius of the capsule mesh.
Note:Theradiusof a capsule cannot be greater than half of itsheight. Otherwise, the capsule becomes a circle. If theradiusis greater than half of theheight, the properties adjust to a valid value.
intrings=8🔗
- voidset_rings(value:int)
voidset_rings(value:int)
- intget_rings()
intget_rings()
Number of rings along the height of the capsule.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.