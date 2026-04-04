# Polygon2D

# Polygon2D
Inherits:Node2D<CanvasItem<Node<Object
A 2D polygon.

## Description
A Polygon2D is defined by a set of points. Each point is connected to the next, with the final point being connected to the first, resulting in a closed polygon. Polygon2Ds can be filled with color (solid or gradient) or filled with a given texture.

## Properties

| bool | antialiased | false |
|---|---|---|
| Color | color | Color(1,1,1,1) |
| int | internal_vertex_count | 0 |
| float | invert_border | 100.0 |
| bool | invert_enabled | false |
| Vector2 | offset | Vector2(0,0) |
| PackedVector2Array | polygon | PackedVector2Array() |
| Array | polygons | [] |
| NodePath | skeleton | NodePath("") |
| Texture2D | texture |  |
| Vector2 | texture_offset | Vector2(0,0) |
| float | texture_rotation | 0.0 |
| Vector2 | texture_scale | Vector2(1,1) |
| PackedVector2Array | uv | PackedVector2Array() |
| PackedColorArray | vertex_colors | PackedColorArray() |

bool
antialiased
false
Color
color
Color(1,1,1,1)
internal_vertex_count
float
invert_border
100.0
bool
invert_enabled
false
Vector2
offset
Vector2(0,0)
PackedVector2Array
polygon
PackedVector2Array()
Array
polygons
NodePath
skeleton
NodePath("")
Texture2D
texture
Vector2
texture_offset
Vector2(0,0)
float
texture_rotation
Vector2
texture_scale
Vector2(1,1)
PackedVector2Array
PackedVector2Array()
PackedColorArray
vertex_colors
PackedColorArray()

## Methods

| void | add_bone(path:NodePath, weights:PackedFloat32Array) |
|---|---|
| void | clear_bones() |
| void | erase_bone(index:int) |
| int | get_bone_count()const |
| NodePath | get_bone_path(index:int)const |
| PackedFloat32Array | get_bone_weights(index:int)const |
| void | set_bone_path(index:int, path:NodePath) |
| void | set_bone_weights(index:int, weights:PackedFloat32Array) |

void
add_bone(path:NodePath, weights:PackedFloat32Array)
void
clear_bones()
void
erase_bone(index:int)
get_bone_count()const
NodePath
get_bone_path(index:int)const
PackedFloat32Array
get_bone_weights(index:int)const
void
set_bone_path(index:int, path:NodePath)
void
set_bone_weights(index:int, weights:PackedFloat32Array)

## Property Descriptions
boolantialiased=false🔗
- voidset_antialiased(value:bool)
voidset_antialiased(value:bool)
- boolget_antialiased()
boolget_antialiased()
Iftrue, polygon edges will be anti-aliased.
Colorcolor=Color(1,1,1,1)🔗
- voidset_color(value:Color)
voidset_color(value:Color)
- Colorget_color()
Colorget_color()
The polygon's fill color. Iftextureis set, it will be multiplied by this color. It will also be the default color for vertices not set invertex_colors.
intinternal_vertex_count=0🔗
- voidset_internal_vertex_count(value:int)
voidset_internal_vertex_count(value:int)
- intget_internal_vertex_count()
intget_internal_vertex_count()
Number of internal vertices, used for UV mapping.
floatinvert_border=100.0🔗
- voidset_invert_border(value:float)
voidset_invert_border(value:float)
- floatget_invert_border()
floatget_invert_border()
Added padding applied to the bounding box wheninvert_enabledis set totrue. Setting this value too small may result in a "Bad Polygon" error.
boolinvert_enabled=false🔗
- voidset_invert_enabled(value:bool)
voidset_invert_enabled(value:bool)
- boolget_invert_enabled()
boolget_invert_enabled()
Iftrue, the polygon will be inverted, containing the area outside the defined points and extending to theinvert_border.
Vector2offset=Vector2(0,0)🔗
- voidset_offset(value:Vector2)
voidset_offset(value:Vector2)
- Vector2get_offset()
Vector2get_offset()
The offset applied to each vertex.
PackedVector2Arraypolygon=PackedVector2Array()🔗
- voidset_polygon(value:PackedVector2Array)
voidset_polygon(value:PackedVector2Array)
- PackedVector2Arrayget_polygon()
PackedVector2Arrayget_polygon()
The polygon's list of vertices. The final point will be connected to the first.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedVector2Arrayfor more details.
Arraypolygons=[]🔗
- voidset_polygons(value:Array)
voidset_polygons(value:Array)
- Arrayget_polygons()
Arrayget_polygons()
The list of polygons, in case more than one is being represented. Every individual polygon is stored as aPackedInt32Arraywhere eachintis an index to a point inpolygon. If empty, this property will be ignored, and the resulting single polygon will be composed of all points inpolygon, using the order they are stored in.
NodePathskeleton=NodePath("")🔗
- voidset_skeleton(value:NodePath)
voidset_skeleton(value:NodePath)
- NodePathget_skeleton()
NodePathget_skeleton()
Path to aSkeleton2Dnode used for skeleton-based deformations of this polygon. If empty or invalid, skeletal deformations will not be used.
Texture2Dtexture🔗
- voidset_texture(value:Texture2D)
voidset_texture(value:Texture2D)
- Texture2Dget_texture()
Texture2Dget_texture()
The polygon's fill texture. Useuvto set texture coordinates.
Vector2texture_offset=Vector2(0,0)🔗
- voidset_texture_offset(value:Vector2)
voidset_texture_offset(value:Vector2)
- Vector2get_texture_offset()
Vector2get_texture_offset()
Amount to offset the polygon'stexture. If set toVector2(0,0), the texture's origin (its top-left corner) will be placed at the polygon's position.
floattexture_rotation=0.0🔗
- voidset_texture_rotation(value:float)
voidset_texture_rotation(value:float)
- floatget_texture_rotation()
floatget_texture_rotation()
The texture's rotation in radians.
Vector2texture_scale=Vector2(1,1)🔗
- voidset_texture_scale(value:Vector2)
voidset_texture_scale(value:Vector2)
- Vector2get_texture_scale()
Vector2get_texture_scale()
Amount to multiply theuvcoordinates when usingtexture. Larger values make the texture smaller, and vice versa.
PackedVector2Arrayuv=PackedVector2Array()🔗
- voidset_uv(value:PackedVector2Array)
voidset_uv(value:PackedVector2Array)
- PackedVector2Arrayget_uv()
PackedVector2Arrayget_uv()
Texture coordinates for each vertex of the polygon. There should be one UV value per polygon vertex. If there are fewer, undefined vertices will useVector2(0,0).
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedVector2Arrayfor more details.
PackedColorArrayvertex_colors=PackedColorArray()🔗
- voidset_vertex_colors(value:PackedColorArray)
voidset_vertex_colors(value:PackedColorArray)
- PackedColorArrayget_vertex_colors()
PackedColorArrayget_vertex_colors()
Color for each vertex. Colors are interpolated between vertices, resulting in smooth gradients. There should be one per polygon vertex. If there are fewer, undefined vertices will usecolor.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedColorArrayfor more details.

## Method Descriptions
voidadd_bone(path:NodePath, weights:PackedFloat32Array)🔗
Adds a bone with the specifiedpathandweights.
voidclear_bones()🔗
Removes all bones from thisPolygon2D.
voiderase_bone(index:int)🔗
Removes the specified bone from thisPolygon2D.
intget_bone_count()const🔗
Returns the number of bones in thisPolygon2D.
NodePathget_bone_path(index:int)const🔗
Returns the path to the node associated with the specified bone.
PackedFloat32Arrayget_bone_weights(index:int)const🔗
Returns the weight values of the specified bone.
voidset_bone_path(index:int, path:NodePath)🔗
Sets the path to the node associated with the specified bone.
voidset_bone_weights(index:int, weights:PackedFloat32Array)🔗
Sets the weight values for the specified bone.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.