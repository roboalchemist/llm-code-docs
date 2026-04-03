# CSGSphere3D

# CSGSphere3D
Inherits:CSGPrimitive3D<CSGShape3D<GeometryInstance3D<VisualInstance3D<Node3D<Node<Object
A CSG Sphere shape.

## Description
This node allows you to create a sphere for use with the CSG system.
Note:CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating aMeshInstance3Dwith aPrimitiveMesh. Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

## Tutorials
- Prototyping levels with CSG
Prototyping levels with CSG

## Properties

| Material | material |  |
|---|---|---|
| int | radial_segments | 12 |
| float | radius | 0.5 |
| int | rings | 6 |
| bool | smooth_faces | true |

Material
material
radial_segments
float
radius
rings
bool
smooth_faces
true

## Property Descriptions
Materialmaterial🔗
- voidset_material(value:Material)
voidset_material(value:Material)
- Materialget_material()
Materialget_material()
The material used to render the sphere.
intradial_segments=12🔗
- voidset_radial_segments(value:int)
voidset_radial_segments(value:int)
- intget_radial_segments()
intget_radial_segments()
Number of vertical slices for the sphere.
floatradius=0.5🔗
- voidset_radius(value:float)
voidset_radius(value:float)
- floatget_radius()
floatget_radius()
Radius of the sphere.
intrings=6🔗
- voidset_rings(value:int)
voidset_rings(value:int)
- intget_rings()
intget_rings()
Number of horizontal slices for the sphere.
boolsmooth_faces=true🔗
- voidset_smooth_faces(value:bool)
voidset_smooth_faces(value:bool)
- boolget_smooth_faces()
boolget_smooth_faces()
Iftruethe normals of the sphere are set to give a smooth effect making the sphere seem rounded. Iffalsethe sphere will have a flat shaded look.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.