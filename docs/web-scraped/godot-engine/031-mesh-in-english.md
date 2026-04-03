# Mesh in English

# Mesh
Inherits:Resource<RefCounted<Object
Inherited By:ArrayMesh,ImmediateMesh,PlaceholderMesh,PrimitiveMesh
AResourcethat contains vertex array-based geometry.

## Description
Mesh is a type ofResourcethat contains vertex array-based geometry, divided insurfaces. Each surface contains a completely separate array and a material used to draw it. Design wise, a mesh with multiple surfaces is preferred to a single surface, because objects created in 3D editing software commonly contain multiple materials. The maximum number of surfaces per mesh isRenderingServer.MAX_MESH_SURFACES.

## Tutorials
- 3D Material Testers Demo
3D Material Testers Demo
- 3D Kinematic Character Demo
3D Kinematic Character Demo
- 3D Platformer Demo
3D Platformer Demo
- Third Person Shooter (TPS) Demo
Third Person Shooter (TPS) Demo

## Properties

| Vector2i | lightmap_size_hint | Vector2i(0,0) |

Vector2i
lightmap_size_hint
Vector2i(0,0)

## Methods

| AABB | _get_aabb()virtualrequiredconst |
|---|---|
| int | _get_blend_shape_count()virtualrequiredconst |
| StringName | _get_blend_shape_name(index:int)virtualrequiredconst |
| int | _get_surface_count()virtualrequiredconst |
| void | _set_blend_shape_name(index:int, name:StringName)virtualrequired |
| int | _surface_get_array_index_len(index:int)virtualrequiredconst |
| int | _surface_get_array_len(index:int)virtualrequiredconst |
| Array | _surface_get_arrays(index:int)virtualrequiredconst |
| Array[Array] | _surface_get_blend_shape_arrays(index:int)virtualrequiredconst |
| int | _surface_get_format(index:int)virtualrequiredconst |
| Dictionary | _surface_get_lods(index:int)virtualrequiredconst |
| Material | _surface_get_material(index:int)virtualrequiredconst |
| int | _surface_get_primitive_type(index:int)virtualrequiredconst |
| void | _surface_set_material(index:int, material:Material)virtualrequired |
| ConvexPolygonShape3D | create_convex_shape(clean:bool= true, simplify:bool= false)const |
| Mesh | create_outline(margin:float)const |
| Resource | create_placeholder()const |
| ConcavePolygonShape3D | create_trimesh_shape()const |
| TriangleMesh | generate_triangle_mesh()const |
| AABB | get_aabb()const |
| PackedVector3Array | get_faces()const |
| int | get_surface_count()const |
| Array | surface_get_arrays(surf_idx:int)const |
| Array[Array] | surface_get_blend_shape_arrays(surf_idx:int)const |
| Material | surface_get_material(surf_idx:int)const |
| void | surface_set_material(surf_idx:int, material:Material) |

AABB
_get_aabb()virtualrequiredconst
_get_blend_shape_count()virtualrequiredconst
StringName
_get_blend_shape_name(index:int)virtualrequiredconst
_get_surface_count()virtualrequiredconst
void
_set_blend_shape_name(index:int, name:StringName)virtualrequired
_surface_get_array_index_len(index:int)virtualrequiredconst
_surface_get_array_len(index:int)virtualrequiredconst
Array
_surface_get_arrays(index:int)virtualrequiredconst
Array[Array]
_surface_get_blend_shape_arrays(index:int)virtualrequiredconst
_surface_get_format(index:int)virtualrequiredconst
Dictionary
_surface_get_lods(index:int)virtualrequiredconst
Material
_surface_get_material(index:int)virtualrequiredconst
_surface_get_primitive_type(index:int)virtualrequiredconst
void
_surface_set_material(index:int, material:Material)virtualrequired
ConvexPolygonShape3D
create_convex_shape(clean:bool= true, simplify:bool= false)const
Mesh
create_outline(margin:float)const
Resource
create_placeholder()const
ConcavePolygonShape3D
create_trimesh_shape()const
TriangleMesh
generate_triangle_mesh()const
AABB
get_aabb()const
PackedVector3Array
get_faces()const
get_surface_count()const
Array
surface_get_arrays(surf_idx:int)const
Array[Array]
surface_get_blend_shape_arrays(surf_idx:int)const
Material
surface_get_material(surf_idx:int)const
void
surface_set_material(surf_idx:int, material:Material)

## Enumerations
enumPrimitiveType:🔗
PrimitiveTypePRIMITIVE_POINTS=0
Render array as points (one vertex equals one point).
PrimitiveTypePRIMITIVE_LINES=1
Render array as lines (every two vertices a line is created).
PrimitiveTypePRIMITIVE_LINE_STRIP=2
Render array as line strip.
PrimitiveTypePRIMITIVE_TRIANGLES=3
Render array as triangles (every three vertices a triangle is created).
PrimitiveTypePRIMITIVE_TRIANGLE_STRIP=4
Render array as triangle strips.
enumArrayType:🔗
ArrayTypeARRAY_VERTEX=0
PackedVector3Array,PackedVector2Array, orArrayof vertex positions.
ArrayTypeARRAY_NORMAL=1
PackedVector3Arrayof vertex normals.
Note:The array has to consist of normal vectors, otherwise they will be normalized by the engine, potentially causing visual discrepancies.
ArrayTypeARRAY_TANGENT=2
PackedFloat32Arrayof vertex tangents. Each element in groups of 4 floats, first 3 floats determine the tangent, and the last the binormal direction as -1 or 1.
ArrayTypeARRAY_COLOR=3
PackedColorArrayof vertex colors.
ArrayTypeARRAY_TEX_UV=4
PackedVector2Arrayfor UV coordinates.
ArrayTypeARRAY_TEX_UV2=5
PackedVector2Arrayfor second UV coordinates.
ArrayTypeARRAY_CUSTOM0=6
Contains custom color channel 0.PackedByteArrayif(format>>Mesh.ARRAY_FORMAT_CUSTOM0_SHIFT)&Mesh.ARRAY_FORMAT_CUSTOM_MASKisARRAY_CUSTOM_RGBA8_UNORM,ARRAY_CUSTOM_RGBA8_SNORM,ARRAY_CUSTOM_RG_HALF, orARRAY_CUSTOM_RGBA_HALF.PackedFloat32Arrayotherwise.
ArrayTypeARRAY_CUSTOM1=7
Contains custom color channel 1.PackedByteArrayif(format>>Mesh.ARRAY_FORMAT_CUSTOM1_SHIFT)&Mesh.ARRAY_FORMAT_CUSTOM_MASKisARRAY_CUSTOM_RGBA8_UNORM,ARRAY_CUSTOM_RGBA8_SNORM,ARRAY_CUSTOM_RG_HALF, orARRAY_CUSTOM_RGBA_HALF.PackedFloat32Arrayotherwise.
ArrayTypeARRAY_CUSTOM2=8
Contains custom color channel 2.PackedByteArrayif(format>>Mesh.ARRAY_FORMAT_CUSTOM2_SHIFT)&Mesh.ARRAY_FORMAT_CUSTOM_MASKisARRAY_CUSTOM_RGBA8_UNORM,ARRAY_CUSTOM_RGBA8_SNORM,ARRAY_CUSTOM_RG_HALF, orARRAY_CUSTOM_RGBA_HALF.PackedFloat32Arrayotherwise.
ArrayTypeARRAY_CUSTOM3=9
Contains custom color channel 3.PackedByteArrayif(format>>Mesh.ARRAY_FORMAT_CUSTOM3_SHIFT)&Mesh.ARRAY_FORMAT_CUSTOM_MASKisARRAY_CUSTOM_RGBA8_UNORM,ARRAY_CUSTOM_RGBA8_SNORM,ARRAY_CUSTOM_RG_HALF, orARRAY_CUSTOM_RGBA_HALF.PackedFloat32Arrayotherwise.
ArrayTypeARRAY_BONES=10
PackedFloat32ArrayorPackedInt32Arrayof bone indices. Contains either 4 or 8 numbers per vertex depending on the presence of theARRAY_FLAG_USE_8_BONE_WEIGHTSflag.
ArrayTypeARRAY_WEIGHTS=11
PackedFloat32ArrayorPackedFloat64Arrayof bone weights in the range0.0to1.0(inclusive). Contains either 4 or 8 numbers per vertex depending on the presence of theARRAY_FLAG_USE_8_BONE_WEIGHTSflag.
ArrayTypeARRAY_INDEX=12
PackedInt32Arrayof integers used as indices referencing vertices, colors, normals, tangents, and textures. All of those arrays must have the same number of elements as the vertex array. No index can be beyond the vertex array size. When this index array is present, it puts the function into "index mode," where the index selects thei'th vertex, normal, tangent, color, UV, etc. This means if you want to have different normals or colors along an edge, you have to duplicate the vertices.
For triangles, the index array is interpreted as triples, referring to the vertices of each triangle. For lines, the index array is in pairs indicating the start and end of each line.
ArrayTypeARRAY_MAX=13
Represents the size of theArrayTypeenum.
enumArrayCustomFormat:🔗
ArrayCustomFormatARRAY_CUSTOM_RGBA8_UNORM=0
Indicates this custom channel contains unsigned normalized byte colors from 0 to 1, encoded asPackedByteArray.
ArrayCustomFormatARRAY_CUSTOM_RGBA8_SNORM=1
Indicates this custom channel contains signed normalized byte colors from -1 to 1, encoded asPackedByteArray.
ArrayCustomFormatARRAY_CUSTOM_RG_HALF=2
Indicates this custom channel contains half precision float colors, encoded asPackedByteArray. Only red and green channels are used.
ArrayCustomFormatARRAY_CUSTOM_RGBA_HALF=3
Indicates this custom channel contains half precision float colors, encoded asPackedByteArray.
ArrayCustomFormatARRAY_CUSTOM_R_FLOAT=4
Indicates this custom channel contains full float colors, in aPackedFloat32Array. Only the red channel is used.
ArrayCustomFormatARRAY_CUSTOM_RG_FLOAT=5
Indicates this custom channel contains full float colors, in aPackedFloat32Array. Only red and green channels are used.
ArrayCustomFormatARRAY_CUSTOM_RGB_FLOAT=6
Indicates this custom channel contains full float colors, in aPackedFloat32Array. Only red, green and blue channels are used.
ArrayCustomFormatARRAY_CUSTOM_RGBA_FLOAT=7
Indicates this custom channel contains full float colors, in aPackedFloat32Array.
ArrayCustomFormatARRAY_CUSTOM_MAX=8
Represents the size of theArrayCustomFormatenum.
flagsArrayFormat:🔗
ArrayFormatARRAY_FORMAT_VERTEX=1
Mesh array contains vertices. All meshes require a vertex array so this should always be present.
ArrayFormatARRAY_FORMAT_NORMAL=2
Mesh array contains normals.
ArrayFormatARRAY_FORMAT_TANGENT=4
Mesh array contains tangents.
ArrayFormatARRAY_FORMAT_COLOR=8
Mesh array contains colors.
ArrayFormatARRAY_FORMAT_TEX_UV=16
Mesh array contains UVs.
ArrayFormatARRAY_FORMAT_TEX_UV2=32
Mesh array contains second UV.
ArrayFormatARRAY_FORMAT_CUSTOM0=64
Mesh array contains custom channel index 0.
ArrayFormatARRAY_FORMAT_CUSTOM1=128
Mesh array contains custom channel index 1.
ArrayFormatARRAY_FORMAT_CUSTOM2=256
Mesh array contains custom channel index 2.
ArrayFormatARRAY_FORMAT_CUSTOM3=512
Mesh array contains custom channel index 3.
ArrayFormatARRAY_FORMAT_BONES=1024
Mesh array contains bones.
ArrayFormatARRAY_FORMAT_WEIGHTS=2048
Mesh array contains bone weights.
ArrayFormatARRAY_FORMAT_INDEX=4096
Mesh array uses indices.
ArrayFormatARRAY_FORMAT_BLEND_SHAPE_MASK=7
Mask of mesh channels permitted in blend shapes.
ArrayFormatARRAY_FORMAT_CUSTOM_BASE=13
Shift of first custom channel.
ArrayFormatARRAY_FORMAT_CUSTOM_BITS=3
Number of format bits per custom channel. SeeArrayCustomFormat.
ArrayFormatARRAY_FORMAT_CUSTOM0_SHIFT=13
Amount to shiftArrayCustomFormatfor custom channel index 0.
ArrayFormatARRAY_FORMAT_CUSTOM1_SHIFT=16
Amount to shiftArrayCustomFormatfor custom channel index 1.
ArrayFormatARRAY_FORMAT_CUSTOM2_SHIFT=19
Amount to shiftArrayCustomFormatfor custom channel index 2.
ArrayFormatARRAY_FORMAT_CUSTOM3_SHIFT=22
Amount to shiftArrayCustomFormatfor custom channel index 3.
ArrayFormatARRAY_FORMAT_CUSTOM_MASK=7
Mask of custom format bits per custom channel. Must be shifted by one of the SHIFT constants. SeeArrayCustomFormat.
ArrayFormatARRAY_COMPRESS_FLAGS_BASE=25
Shift of first compress flag. Compress flags should be passed toArrayMesh.add_surface_from_arrays()andSurfaceTool.commit().
ArrayFormatARRAY_FLAG_USE_2D_VERTICES=33554432
Flag used to mark that the array contains 2D vertices.
ArrayFormatARRAY_FLAG_USE_DYNAMIC_UPDATE=67108864
Flag used to mark that the mesh data will useGL_DYNAMIC_DRAWon GLES. Unused on Vulkan.
ArrayFormatARRAY_FLAG_USE_8_BONE_WEIGHTS=134217728
Flag used to mark that the mesh contains up to 8 bone influences per vertex. This flag indicates thatARRAY_BONESandARRAY_WEIGHTSelements will have double length.
ArrayFormatARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY=268435456
Flag used to mark that the mesh intentionally contains no vertex array.
ArrayFormatARRAY_FLAG_COMPRESS_ATTRIBUTES=536870912
Flag used to mark that a mesh is using compressed attributes (vertices, normals, tangents, UVs). When this form of compression is enabled, vertex positions will be packed into an RGBA16UNORM attribute and scaled in the vertex shader. The normal and tangent will be packed into an RG16UNORM representing an axis, and a 16-bit float stored in the A-channel of the vertex. UVs will use 16-bit normalized floats instead of full 32-bit signed floats. When using this compression mode you must use either vertices, normals, and tangents or only vertices. You cannot use normals without tangents. Importers will automatically enable this compression if they can.
enumBlendShapeMode:🔗
BlendShapeModeBLEND_SHAPE_MODE_NORMALIZED=0
Blend shapes are normalized.
BlendShapeModeBLEND_SHAPE_MODE_RELATIVE=1
Blend shapes are relative to base weight.

## Property Descriptions
Vector2ilightmap_size_hint=Vector2i(0,0)🔗
- voidset_lightmap_size_hint(value:Vector2i)
voidset_lightmap_size_hint(value:Vector2i)
- Vector2iget_lightmap_size_hint()
Vector2iget_lightmap_size_hint()
Sets a hint to be used for lightmap resolution.

## Method Descriptions
AABB_get_aabb()virtualrequiredconst🔗
Virtual method to override theAABBfor a custom class extendingMesh.
int_get_blend_shape_count()virtualrequiredconst🔗
Virtual method to override the number of blend shapes for a custom class extendingMesh.
StringName_get_blend_shape_name(index:int)virtualrequiredconst🔗
Virtual method to override the retrieval of blend shape names for a custom class extendingMesh.
int_get_surface_count()virtualrequiredconst🔗
Virtual method to override the surface count for a custom class extendingMesh.
void_set_blend_shape_name(index:int, name:StringName)virtualrequired🔗
Virtual method to override the names of blend shapes for a custom class extendingMesh.
int_surface_get_array_index_len(index:int)virtualrequiredconst🔗
Virtual method to override the surface array index length for a custom class extendingMesh.
int_surface_get_array_len(index:int)virtualrequiredconst🔗
Virtual method to override the surface array length for a custom class extendingMesh.
Array_surface_get_arrays(index:int)virtualrequiredconst🔗
Virtual method to override the surface arrays for a custom class extendingMesh.
Array[Array]_surface_get_blend_shape_arrays(index:int)virtualrequiredconst🔗
Virtual method to override the blend shape arrays for a custom class extendingMesh.
int_surface_get_format(index:int)virtualrequiredconst🔗
Virtual method to override the surface format for a custom class extendingMesh.
Dictionary_surface_get_lods(index:int)virtualrequiredconst🔗
Virtual method to override the surface LODs for a custom class extendingMesh.
Material_surface_get_material(index:int)virtualrequiredconst🔗
Virtual method to override the surface material for a custom class extendingMesh.
int_surface_get_primitive_type(index:int)virtualrequiredconst🔗
Virtual method to override the surface primitive type for a custom class extendingMesh.
void_surface_set_material(index:int, material:Material)virtualrequired🔗
Virtual method to override the setting of amaterialat the givenindexfor a custom class extendingMesh.
ConvexPolygonShape3Dcreate_convex_shape(clean:bool= true, simplify:bool= false)const🔗
Calculate aConvexPolygonShape3Dfrom the mesh.
Ifcleanistrue(default), duplicate and interior vertices are removed automatically. You can set it tofalseto make the process faster if not needed.
Ifsimplifyistrue, the geometry can be further simplified to reduce the number of vertices. Disabled by default.
Meshcreate_outline(margin:float)const🔗
Calculate an outline mesh at a defined offset (margin) from the original mesh.
Note:This method typically returns the vertices in reverse order (e.g. clockwise to counterclockwise).
Resourcecreate_placeholder()const🔗
Creates a placeholder version of this resource (PlaceholderMesh).
ConcavePolygonShape3Dcreate_trimesh_shape()const🔗
Calculate aConcavePolygonShape3Dfrom the mesh.
TriangleMeshgenerate_triangle_mesh()const🔗
Generate aTriangleMeshfrom the mesh. Considers only surfaces using one of these primitive types:PRIMITIVE_TRIANGLES,PRIMITIVE_TRIANGLE_STRIP.
AABBget_aabb()const🔗
Returns the smallestAABBenclosing this mesh in local space. Not affected bycustom_aabb.
Note:This is only implemented forArrayMeshandPrimitiveMesh.
PackedVector3Arrayget_faces()const🔗
Returns all the vertices that make up the faces of the mesh. Each three vertices represent one triangle.
intget_surface_count()const🔗
Returns the number of surfaces that theMeshholds. This is equivalent toMeshInstance3D.get_surface_override_material_count().
Arraysurface_get_arrays(surf_idx:int)const🔗
Returns the arrays for the vertices, normals, UVs, etc. that make up the requested surface (seeArrayMesh.add_surface_from_arrays()).
Array[Array]surface_get_blend_shape_arrays(surf_idx:int)const🔗
Returns the blend shape arrays for the requested surface.
Materialsurface_get_material(surf_idx:int)const🔗
Returns aMaterialin a given surface. Surface is rendered using this material.
Note:This returns the material within theMeshresource, not theMaterialassociated to theMeshInstance3D's Surface Material Override properties. To get theMaterialassociated to theMeshInstance3D's Surface Material Override properties, useMeshInstance3D.get_surface_override_material()instead.
voidsurface_set_material(surf_idx:int, material:Material)🔗
Sets aMaterialfor a given surface. Surface will be rendered using this material.
Note:This assigns the material within theMeshresource, not theMaterialassociated to theMeshInstance3D's Surface Material Override properties. To set theMaterialassociated to theMeshInstance3D's Surface Material Override properties, useMeshInstance3D.set_surface_override_material()instead.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.