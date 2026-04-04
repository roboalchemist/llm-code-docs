# CSGPolygon3D

# CSGPolygon3D

Inherits:CSGPrimitive3D<CSGShape3D<GeometryInstance3D<VisualInstance3D<Node3D<Node<Object
Extrudes a 2D polygon shape to create a 3D mesh.

## Description

An array of 2D points is extruded to quickly and easily create a variety of 3D meshes. See alsoCSGMesh3Dfor using 3D meshes as CSG nodes.
Note:CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating aMeshInstance3Dwith aPrimitiveMesh. Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

## Tutorials

- Prototyping levels with CSG
Prototyping levels with CSG

## Properties

| float | depth | 1.0 |
|---|---|---|
| Material | material |  |
| Mode | mode | 0 |
| bool | path_continuous_u |  |
| float | path_interval |  |
| PathIntervalType | path_interval_type |  |
| bool | path_joined |  |
| bool | path_local |  |
| NodePath | path_node |  |
| PathRotation | path_rotation |  |
| bool | path_rotation_accurate |  |
| float | path_simplify_angle |  |
| float | path_u_distance |  |
| PackedVector2Array | polygon | PackedVector2Array(0,0,0,1,1,1,1,0) |
| bool | smooth_faces | false |
| float | spin_degrees |  |
| int | spin_sides |  |

float
depth
Material
material
Mode
mode
bool
path_continuous_u
float
path_interval
PathIntervalType
path_interval_type
bool
path_joined
bool
path_local
NodePath
path_node
PathRotation
path_rotation
bool
path_rotation_accurate
float
path_simplify_angle
float
path_u_distance
PackedVector2Array
polygon
PackedVector2Array(0,0,0,1,1,1,1,0)
bool
smooth_faces
false
float
spin_degrees
spin_sides

## Enumerations

enumMode:🔗
ModeMODE_DEPTH=0
Thepolygonshape is extruded along the negative Z axis.
ModeMODE_SPIN=1
Thepolygonshape is extruded by rotating it around the Y axis.
ModeMODE_PATH=2
Thepolygonshape is extruded along thePath3Dspecified inpath_node.
enumPathRotation:🔗
PathRotationPATH_ROTATION_POLYGON=0
Thepolygonshape is not rotated.
Note:Requires the path Z coordinates to continually decrease to ensure viable shapes.
PathRotationPATH_ROTATION_PATH=1
Thepolygonshape is rotated along the path, but it is not rotated around the path axis.
Note:Requires the path Z coordinates to continually decrease to ensure viable shapes.
PathRotationPATH_ROTATION_PATH_FOLLOW=2
Thepolygonshape follows the path and its rotations around the path axis.
enumPathIntervalType:🔗
PathIntervalTypePATH_INTERVAL_DISTANCE=0
Whenmodeis set toMODE_PATH,path_intervalwill determine the distance, in meters, each interval of the path will extrude.
PathIntervalTypePATH_INTERVAL_SUBDIVIDE=1
Whenmodeis set toMODE_PATH,path_intervalwill subdivide the polygons along the path.

## Property Descriptions

floatdepth=1.0🔗

- voidset_depth(value:float)
voidset_depth(value:float)
- floatget_depth()
floatget_depth()
WhenmodeisMODE_DEPTH, the depth of the extrusion.
Materialmaterial🔗
- voidset_material(value:Material)
voidset_material(value:Material)
- Materialget_material()
Materialget_material()
Material to use for the resulting mesh. The UV maps the top half of the material to the extruded shape (U along the length of the extrusions and V around the outline of thepolygon), the bottom-left quarter to the front end face, and the bottom-right quarter to the back end face.
Modemode=0🔗
- voidset_mode(value:Mode)
voidset_mode(value:Mode)
- Modeget_mode()
Modeget_mode()
Themodeused to extrude thepolygon.
boolpath_continuous_u🔗
- voidset_path_continuous_u(value:bool)
voidset_path_continuous_u(value:bool)
- boolis_path_continuous_u()
boolis_path_continuous_u()
WhenmodeisMODE_PATH, by default, the top half of thematerialis stretched along the entire length of the extruded shape. Iffalsethe top half of the material is repeated every step of the extrusion.
floatpath_interval🔗
- voidset_path_interval(value:float)
voidset_path_interval(value:float)
- floatget_path_interval()
floatget_path_interval()
WhenmodeisMODE_PATH, the path interval or ratio of path points to extrusions.
PathIntervalTypepath_interval_type🔗
- voidset_path_interval_type(value:PathIntervalType)
voidset_path_interval_type(value:PathIntervalType)
- PathIntervalTypeget_path_interval_type()
PathIntervalTypeget_path_interval_type()
WhenmodeisMODE_PATH, this will determine if the interval should be by distance (PATH_INTERVAL_DISTANCE) or subdivision fractions (PATH_INTERVAL_SUBDIVIDE).
boolpath_joined🔗
- voidset_path_joined(value:bool)
voidset_path_joined(value:bool)
- boolis_path_joined()
boolis_path_joined()
WhenmodeisMODE_PATH, iftruethe ends of the path are joined, by adding an extrusion between the last and first points of the path.
boolpath_local🔗
- voidset_path_local(value:bool)
voidset_path_local(value:bool)
- boolis_path_local()
boolis_path_local()
WhenmodeisMODE_PATH, iftruetheTransform3Dof theCSGPolygon3Dis used as the starting point for the extrusions, not theTransform3Dof thepath_node.
NodePathpath_node🔗
- voidset_path_node(value:NodePath)
voidset_path_node(value:NodePath)
- NodePathget_path_node()
NodePathget_path_node()
WhenmodeisMODE_PATH, the location of thePath3Dobject used to extrude thepolygon.
PathRotationpath_rotation🔗
- voidset_path_rotation(value:PathRotation)
voidset_path_rotation(value:PathRotation)
- PathRotationget_path_rotation()
PathRotationget_path_rotation()
WhenmodeisMODE_PATH, the path rotation method used to rotate thepolygonas it is extruded.
boolpath_rotation_accurate🔗
- voidset_path_rotation_accurate(value:bool)
voidset_path_rotation_accurate(value:bool)
- boolget_path_rotation_accurate()
boolget_path_rotation_accurate()
WhenmodeisMODE_PATH, iftruethe polygon will be rotated according to the proper tangent of the path at the sampled points. Iffalsean approximation is used, which decreases in accuracy as the number of subdivisions decreases.
floatpath_simplify_angle🔗
- voidset_path_simplify_angle(value:float)
voidset_path_simplify_angle(value:float)
- floatget_path_simplify_angle()
floatget_path_simplify_angle()
WhenmodeisMODE_PATH, extrusions that are less than this angle, will be merged together to reduce polygon count.
floatpath_u_distance🔗
- voidset_path_u_distance(value:float)
voidset_path_u_distance(value:float)
- floatget_path_u_distance()
floatget_path_u_distance()
WhenmodeisMODE_PATH, this is the distance along the path, in meters, the texture coordinates will tile. When set to 0, texture coordinates will match geometry exactly with no tiling.
PackedVector2Arraypolygon=PackedVector2Array(0,0,0,1,1,1,1,0)🔗
- voidset_polygon(value:PackedVector2Array)
voidset_polygon(value:PackedVector2Array)
- PackedVector2Arrayget_polygon()
PackedVector2Arrayget_polygon()
The point array that defines the 2D polygon that is extruded. This can be a convex or concave polygon with 3 or more points. The polygon mustnothave any intersecting edges. Otherwise, triangulation will fail and no mesh will be generated.
Note:If only 1 or 2 points are defined inpolygon, no mesh will be generated.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedVector2Arrayfor more details.
boolsmooth_faces=false🔗
- voidset_smooth_faces(value:bool)
voidset_smooth_faces(value:bool)
- boolget_smooth_faces()
boolget_smooth_faces()
Iftrue, applies smooth shading to the extrusions.
floatspin_degrees🔗
- voidset_spin_degrees(value:float)
voidset_spin_degrees(value:float)
- floatget_spin_degrees()
floatget_spin_degrees()
WhenmodeisMODE_SPIN, the total number of degrees thepolygonis rotated when extruding.
intspin_sides🔗
- voidset_spin_sides(value:int)
voidset_spin_sides(value:int)
- intget_spin_sides()
intget_spin_sides()
WhenmodeisMODE_SPIN, the number of extrusions made.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
