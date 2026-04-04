# SurfaceTool

# SurfaceTool

Inherits:RefCounted<Object
Helper tool to create geometry.

## Description

TheSurfaceToolis used to construct aMeshby specifying vertex attributes individually. It can be used to construct aMeshfrom a script. All properties except indices need to be added before callingadd_vertex(). For example, to add vertex colors and UVs:

```
var st = SurfaceTool.new()
st.begin(Mesh.PRIMITIVE_TRIANGLES)
st.set_color(Color(1, 0, 0))
st.set_uv(Vector2(0, 0))
st.add_vertex(Vector3(0, 0, 0))
```

```
var st = new SurfaceTool();
st.Begin(Mesh.PrimitiveType.Triangles);
st.SetColor(new Color(1, 0, 0));
st.SetUV(new Vector2(0, 0));
st.AddVertex(new Vector3(0, 0, 0));
```

The aboveSurfaceToolnow contains one vertex of a triangle which has a UV coordinate and a specifiedColor. If another vertex were added without callingset_uv()orset_color(), then the last values would be used.
Vertex attributes must be passedbeforecallingadd_vertex(). Failure to do so will result in an error when committing the vertex information to a mesh.
Additionally, the attributes used before the first vertex is added determine the format of the mesh. For example, if you only add UVs to the first vertex, you cannot add color to any of the subsequent vertices.
See alsoArrayMesh,ImmediateMeshandMeshDataToolfor procedural geometry generation.
Note:Godot uses clockwisewinding orderfor front faces of triangle primitive modes.

## Tutorials

- Using the SurfaceTool
Using the SurfaceTool
- 3D Voxel Demo
3D Voxel Demo

## Methods

| void | add_index(index:int) |
|---|---|
| void | add_triangle_fan(vertices:PackedVector3Array, uvs:PackedVector2Array= PackedVector2Array(), colors:PackedColorArray= PackedColorArray(), uv2s:PackedVector2Array= PackedVector2Array(), normals:PackedVector3Array= PackedVector3Array(), tangents:Array[Plane] = []) |
| void | add_vertex(vertex:Vector3) |
| void | append_from(existing:Mesh, surface:int, transform:Transform3D) |
| void | begin(primitive:PrimitiveType) |
| void | clear() |
| ArrayMesh | commit(existing:ArrayMesh= null, flags:int= 0) |
| Array | commit_to_arrays() |
| void | create_from(existing:Mesh, surface:int) |
| void | create_from_arrays(arrays:Array, primitive_type:PrimitiveType= 3) |
| void | create_from_blend_shape(existing:Mesh, surface:int, blend_shape:String) |
| void | deindex() |
| PackedInt32Array | generate_lod(nd_threshold:float, target_index_count:int= 3) |
| void | generate_normals(flip:bool= false) |
| void | generate_tangents() |
| AABB | get_aabb()const |
| CustomFormat | get_custom_format(channel_index:int)const |
| PrimitiveType | get_primitive_type()const |
| SkinWeightCount | get_skin_weight_count()const |
| void | index() |
| void | optimize_indices_for_cache() |
| void | set_bones(bones:PackedInt32Array) |
| void | set_color(color:Color) |
| void | set_custom(channel_index:int, custom_color:Color) |
| void | set_custom_format(channel_index:int, format:CustomFormat) |
| void | set_material(material:Material) |
| void | set_normal(normal:Vector3) |
| void | set_skin_weight_count(count:SkinWeightCount) |
| void | set_smooth_group(index:int) |
| void | set_tangent(tangent:Plane) |
| void | set_uv(uv:Vector2) |
| void | set_uv2(uv2:Vector2) |
| void | set_weights(weights:PackedFloat32Array) |

void
add_index(index:int)
void
add_triangle_fan(vertices:PackedVector3Array, uvs:PackedVector2Array= PackedVector2Array(), colors:PackedColorArray= PackedColorArray(), uv2s:PackedVector2Array= PackedVector2Array(), normals:PackedVector3Array= PackedVector3Array(), tangents:Array[Plane] = [])
void
add_vertex(vertex:Vector3)
void
append_from(existing:Mesh, surface:int, transform:Transform3D)
void
begin(primitive:PrimitiveType)
void
clear()
ArrayMesh
commit(existing:ArrayMesh= null, flags:int= 0)
Array
commit_to_arrays()
void
create_from(existing:Mesh, surface:int)
void
create_from_arrays(arrays:Array, primitive_type:PrimitiveType= 3)
void
create_from_blend_shape(existing:Mesh, surface:int, blend_shape:String)
void
deindex()
PackedInt32Array
generate_lod(nd_threshold:float, target_index_count:int= 3)
void
generate_normals(flip:bool= false)
void
generate_tangents()
AABB
get_aabb()const
CustomFormat
get_custom_format(channel_index:int)const
PrimitiveType
get_primitive_type()const
SkinWeightCount
get_skin_weight_count()const
void
index()
void
optimize_indices_for_cache()
void
set_bones(bones:PackedInt32Array)
void
set_color(color:Color)
void
set_custom(channel_index:int, custom_color:Color)
void
set_custom_format(channel_index:int, format:CustomFormat)
void
set_material(material:Material)
void
set_normal(normal:Vector3)
void
set_skin_weight_count(count:SkinWeightCount)
void
set_smooth_group(index:int)
void
set_tangent(tangent:Plane)
void
set_uv(uv:Vector2)
void
set_uv2(uv2:Vector2)
void
set_weights(weights:PackedFloat32Array)

## Enumerations

enumCustomFormat:🔗
CustomFormatCUSTOM_RGBA8_UNORM=0
Limits range of data passed toset_custom()to unsigned normalized 0 to 1 stored in 8 bits per channel. SeeMesh.ARRAY_CUSTOM_RGBA8_UNORM.
CustomFormatCUSTOM_RGBA8_SNORM=1
Limits range of data passed toset_custom()to signed normalized -1 to 1 stored in 8 bits per channel. SeeMesh.ARRAY_CUSTOM_RGBA8_SNORM.
CustomFormatCUSTOM_RG_HALF=2
Stores data passed toset_custom()as half precision floats, and uses only red and green color channels. SeeMesh.ARRAY_CUSTOM_RG_HALF.
CustomFormatCUSTOM_RGBA_HALF=3
Stores data passed toset_custom()as half precision floats and uses all color channels. SeeMesh.ARRAY_CUSTOM_RGBA_HALF.
CustomFormatCUSTOM_R_FLOAT=4
Stores data passed toset_custom()as full precision floats, and uses only red color channel. SeeMesh.ARRAY_CUSTOM_R_FLOAT.
CustomFormatCUSTOM_RG_FLOAT=5
Stores data passed toset_custom()as full precision floats, and uses only red and green color channels. SeeMesh.ARRAY_CUSTOM_RG_FLOAT.
CustomFormatCUSTOM_RGB_FLOAT=6
Stores data passed toset_custom()as full precision floats, and uses only red, green and blue color channels. SeeMesh.ARRAY_CUSTOM_RGB_FLOAT.
CustomFormatCUSTOM_RGBA_FLOAT=7
Stores data passed toset_custom()as full precision floats, and uses all color channels. SeeMesh.ARRAY_CUSTOM_RGBA_FLOAT.
CustomFormatCUSTOM_MAX=8
Used to indicate a disabled custom channel.
enumSkinWeightCount:🔗
SkinWeightCountSKIN_4_WEIGHTS=0
Each individual vertex can be influenced by only 4 bone weights.
SkinWeightCountSKIN_8_WEIGHTS=1
Each individual vertex can be influenced by up to 8 bone weights.

## Method Descriptions

voidadd_index(index:int)🔗
Adds a vertex to index array if you are using indexed vertices. Does not need to be called before adding vertices.
voidadd_triangle_fan(vertices:PackedVector3Array, uvs:PackedVector2Array= PackedVector2Array(), colors:PackedColorArray= PackedColorArray(), uv2s:PackedVector2Array= PackedVector2Array(), normals:PackedVector3Array= PackedVector3Array(), tangents:Array[Plane] = [])🔗
Inserts a triangle fan made of array data intoMeshbeing constructed.
Requires the primitive type be set toMesh.PRIMITIVE_TRIANGLES.
voidadd_vertex(vertex:Vector3)🔗
Specifies the position of current vertex. Should be called after specifying other vertex properties (e.g. Color, UV).
voidappend_from(existing:Mesh, surface:int, transform:Transform3D)🔗
Append vertices from a givenMeshsurface onto the current vertex array with specifiedTransform3D.
voidbegin(primitive:PrimitiveType)🔗
Called before adding any vertices. Takes the primitive type as an argument (e.g.Mesh.PRIMITIVE_TRIANGLES).
voidclear()🔗
Clear all information passed into the surface tool so far.
ArrayMeshcommit(existing:ArrayMesh= null, flags:int= 0)🔗
Returns a constructedArrayMeshfrom current information passed in. If an existingArrayMeshis passed in as an argument, will add an extra surface to the existingArrayMesh.
Theflagsargument can be the bitwise OR ofMesh.ARRAY_FLAG_USE_DYNAMIC_UPDATE,Mesh.ARRAY_FLAG_USE_8_BONE_WEIGHTS, orMesh.ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY.
Arraycommit_to_arrays()🔗
Commits the data to the same format used byArrayMesh.add_surface_from_arrays(),ImporterMesh.add_surface(), andcreate_from_arrays(). This way you can further process the mesh data using theArrayMeshorImporterMeshAPIs.
voidcreate_from(existing:Mesh, surface:int)🔗
Creates a vertex array from an existingMesh.
voidcreate_from_arrays(arrays:Array, primitive_type:PrimitiveType= 3)🔗
Creates this SurfaceTool from existing vertex arrays such as returned bycommit_to_arrays(),Mesh.surface_get_arrays(),Mesh.surface_get_blend_shape_arrays(),ImporterMesh.get_surface_arrays(), andImporterMesh.get_surface_blend_shape_arrays().primitive_typecontrols the type of mesh data, defaulting toMesh.PRIMITIVE_TRIANGLES.
voidcreate_from_blend_shape(existing:Mesh, surface:int, blend_shape:String)🔗
Creates a vertex array from the specified blend shape of an existingMesh. This can be used to extract a specific pose from a blend shape.
voiddeindex()🔗
Removes the index array by expanding the vertex array.
PackedInt32Arraygenerate_lod(nd_threshold:float, target_index_count:int= 3)🔗
Deprecated:This method is unused internally, as it does not preserve normals or UVs. Consider usingImporterMesh.generate_lods()instead.
Generates an LOD for a givennd_thresholdin linear units (square root of quadric error metric), using at mosttarget_index_countindices.
voidgenerate_normals(flip:bool= false)🔗
Generates normals from vertices so you do not have to do it manually. Ifflipistrue, the resulting normals will be inverted.generate_normals()should be calledaftergenerating geometry andbeforecommitting the mesh usingcommit()orcommit_to_arrays(). For correct display of normal-mapped surfaces, you will also have to generate tangents usinggenerate_tangents().
Note:generate_normals()only works if the primitive type is set toMesh.PRIMITIVE_TRIANGLES.
Note:generate_normals()takes smooth groups into account. To generate smooth normals, set the smooth group to a value greater than or equal to0usingset_smooth_group()or leave the smooth group at the default of0. To generate flat normals, set the smooth group to-1usingset_smooth_group()prior to adding vertices.
voidgenerate_tangents()🔗
Generates a tangent vector for each vertex. Requires that each vertex already has UVs and normals set (seegenerate_normals()).
AABBget_aabb()const🔗
Returns the axis-aligned bounding box of the vertex positions.
CustomFormatget_custom_format(channel_index:int)const🔗
Returns the format for customchannel_index(currently up to 4). ReturnsCUSTOM_MAXif this custom channel is unused.
PrimitiveTypeget_primitive_type()const🔗
Returns the type of mesh geometry, such asMesh.PRIMITIVE_TRIANGLES.
SkinWeightCountget_skin_weight_count()const🔗
By default, returnsSKIN_4_WEIGHTSto indicate only 4 bone influences per vertex are used.
ReturnsSKIN_8_WEIGHTSif up to 8 influences are used.
Note:This function returns an enum, not the exact number of weights.
voidindex()🔗
Shrinks the vertex array by creating an index array. This can improve performance by avoiding vertex reuse.
voidoptimize_indices_for_cache()🔗
Optimizes triangle sorting for performance. Requires thatget_primitive_type()isMesh.PRIMITIVE_TRIANGLES.
voidset_bones(bones:PackedInt32Array)🔗
Specifies an array of bones to use for thenextvertex.bonesmust contain 4 integers.
voidset_color(color:Color)🔗
Specifies aColorto use for thenextvertex. If every vertex needs to have this information set and you fail to submit it for the first vertex, this information may not be used at all.
Note:The material must haveBaseMaterial3D.vertex_color_use_as_albedoenabled for the vertex color to be visible.
voidset_custom(channel_index:int, custom_color:Color)🔗
Sets the custom value on this vertex forchannel_index.
set_custom_format()must be called first for thischannel_index. Formats which are not RGBA will ignore other color channels.
voidset_custom_format(channel_index:int, format:CustomFormat)🔗
Sets the color format for this customchannel_index. UseCUSTOM_MAXto disable.
Must be invoked afterbegin()and should be set beforecommit()orcommit_to_arrays().
voidset_material(material:Material)🔗
SetsMaterialto be used by theMeshyou are constructing.
voidset_normal(normal:Vector3)🔗
Specifies a normal to use for thenextvertex. If every vertex needs to have this information set and you fail to submit it for the first vertex, this information may not be used at all.
voidset_skin_weight_count(count:SkinWeightCount)🔗
Set toSKIN_8_WEIGHTSto indicate that up to 8 bone influences per vertex may be used.
By default, only 4 bone influences are used (SKIN_4_WEIGHTS).
Note:This function takes an enum, not the exact number of weights.
voidset_smooth_group(index:int)🔗
Specifies the smooth group to use for thenextvertex. If this is never called, all vertices will have the default smooth group of0and will be smoothed with adjacent vertices of the same group. To produce a mesh with flat normals, set the smooth group to-1.
Note:This function actually takes auint32_t, so C# users should useuint32.MaxValueinstead of-1to produce a mesh with flat normals.
voidset_tangent(tangent:Plane)🔗
Specifies a tangent to use for thenextvertex. If every vertex needs to have this information set and you fail to submit it for the first vertex, this information may not be used at all.
Note:Even thoughtangentis aPlane, it does not directly represent the tangent plane. ItsPlane.x,Plane.y, andPlane.zrepresent the tangent vector andPlane.dshould be either-1or1. See alsoMesh.ARRAY_TANGENT.
voidset_uv(uv:Vector2)🔗
Specifies a set of UV coordinates to use for thenextvertex. If every vertex needs to have this information set and you fail to submit it for the first vertex, this information may not be used at all.
voidset_uv2(uv2:Vector2)🔗
Specifies an optional second set of UV coordinates to use for thenextvertex. If every vertex needs to have this information set and you fail to submit it for the first vertex, this information may not be used at all.
voidset_weights(weights:PackedFloat32Array)🔗
Specifies weight values to use for thenextvertex.weightsmust contain 4 values. If every vertex needs to have this information set and you fail to submit it for the first vertex, this information may not be used at all.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
