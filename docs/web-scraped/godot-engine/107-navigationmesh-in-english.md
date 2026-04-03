# NavigationMesh in English

# NavigationMesh
Experimental:This class may be changed or removed in future versions.
Inherits:Resource<RefCounted<Object
A navigation mesh that defines traversable areas and obstacles.

## Description
A navigation mesh is a collection of polygons that define which areas of an environment are traversable to aid agents in pathfinding through complicated spaces.

## Tutorials
- Using NavigationMeshes
Using NavigationMeshes
- 3D Navigation Demo
3D Navigation Demo

## Properties

| float | agent_height | 1.5 |
|---|---|---|
| float | agent_max_climb | 0.25 |
| float | agent_max_slope | 45.0 |
| float | agent_radius | 0.5 |
| float | border_size | 0.0 |
| float | cell_height | 0.25 |
| float | cell_size | 0.25 |
| float | detail_sample_distance | 6.0 |
| float | detail_sample_max_error | 1.0 |
| float | edge_max_error | 1.3 |
| float | edge_max_length | 0.0 |
| AABB | filter_baking_aabb | AABB(0,0,0,0,0,0) |
| Vector3 | filter_baking_aabb_offset | Vector3(0,0,0) |
| bool | filter_ledge_spans | false |
| bool | filter_low_hanging_obstacles | false |
| bool | filter_walkable_low_height_spans | false |
| int | geometry_collision_mask | 4294967295 |
| ParsedGeometryType | geometry_parsed_geometry_type | 2 |
| SourceGeometryMode | geometry_source_geometry_mode | 0 |
| StringName | geometry_source_group_name | &"navigation_mesh_source_group" |
| float | region_merge_size | 20.0 |
| float | region_min_size | 2.0 |
| SamplePartitionType | sample_partition_type | 0 |
| float | vertices_per_polygon | 6.0 |

float
agent_height
float
agent_max_climb
0.25
float
agent_max_slope
45.0
float
agent_radius
float
border_size
float
cell_height
0.25
float
cell_size
0.25
float
detail_sample_distance
float
detail_sample_max_error
float
edge_max_error
float
edge_max_length
AABB
filter_baking_aabb
AABB(0,0,0,0,0,0)
Vector3
filter_baking_aabb_offset
Vector3(0,0,0)
bool
filter_ledge_spans
false
bool
filter_low_hanging_obstacles
false
bool
filter_walkable_low_height_spans
false
geometry_collision_mask
4294967295
ParsedGeometryType
geometry_parsed_geometry_type
SourceGeometryMode
geometry_source_geometry_mode
StringName
geometry_source_group_name
&"navigation_mesh_source_group"
float
region_merge_size
20.0
float
region_min_size
SamplePartitionType
sample_partition_type
float
vertices_per_polygon

## Methods

| void | add_polygon(polygon:PackedInt32Array) |
|---|---|
| void | clear() |
| void | clear_polygons() |
| void | create_from_mesh(mesh:Mesh) |
| bool | get_collision_mask_value(layer_number:int)const |
| PackedInt32Array | get_polygon(idx:int) |
| int | get_polygon_count()const |
| PackedVector3Array | get_vertices()const |
| void | set_collision_mask_value(layer_number:int, value:bool) |
| void | set_vertices(vertices:PackedVector3Array) |

void
add_polygon(polygon:PackedInt32Array)
void
clear()
void
clear_polygons()
void
create_from_mesh(mesh:Mesh)
bool
get_collision_mask_value(layer_number:int)const
PackedInt32Array
get_polygon(idx:int)
get_polygon_count()const
PackedVector3Array
get_vertices()const
void
set_collision_mask_value(layer_number:int, value:bool)
void
set_vertices(vertices:PackedVector3Array)

## Enumerations
enumSamplePartitionType:🔗
SamplePartitionTypeSAMPLE_PARTITION_WATERSHED=0
Watershed partitioning. Generally the best choice if you precompute the navigation mesh, use this if you have large open areas.
SamplePartitionTypeSAMPLE_PARTITION_MONOTONE=1
Monotone partitioning. Use this if you want fast navigation mesh generation.
SamplePartitionTypeSAMPLE_PARTITION_LAYERS=2
Layer partitioning. Good choice to use for tiled navigation mesh with medium and small sized tiles.
SamplePartitionTypeSAMPLE_PARTITION_MAX=3
Represents the size of theSamplePartitionTypeenum.
enumParsedGeometryType:🔗
ParsedGeometryTypePARSED_GEOMETRY_MESH_INSTANCES=0
Parses mesh instances as geometry. This includesMeshInstance3D,CSGShape3D, andGridMapnodes.
ParsedGeometryTypePARSED_GEOMETRY_STATIC_COLLIDERS=1
ParsesStaticBody3Dcolliders as geometry. The collider should be in any of the layers specified bygeometry_collision_mask.
ParsedGeometryTypePARSED_GEOMETRY_BOTH=2
BothPARSED_GEOMETRY_MESH_INSTANCESandPARSED_GEOMETRY_STATIC_COLLIDERS.
ParsedGeometryTypePARSED_GEOMETRY_MAX=3
Represents the size of theParsedGeometryTypeenum.
enumSourceGeometryMode:🔗
SourceGeometryModeSOURCE_GEOMETRY_ROOT_NODE_CHILDREN=0
Scans the child nodes of the root node recursively for geometry.
SourceGeometryModeSOURCE_GEOMETRY_GROUPS_WITH_CHILDREN=1
Scans nodes in a group and their child nodes recursively for geometry. The group is specified bygeometry_source_group_name.
SourceGeometryModeSOURCE_GEOMETRY_GROUPS_EXPLICIT=2
Uses nodes in a group for geometry. The group is specified bygeometry_source_group_name.
SourceGeometryModeSOURCE_GEOMETRY_MAX=3
Represents the size of theSourceGeometryModeenum.

## Property Descriptions
floatagent_height=1.5🔗
- voidset_agent_height(value:float)
voidset_agent_height(value:float)
- floatget_agent_height()
floatget_agent_height()
The minimum floor to ceiling height that will still allow the floor area to be considered walkable.
Note:While baking, this value will be rounded up to the nearest multiple ofcell_height.
floatagent_max_climb=0.25🔗
- voidset_agent_max_climb(value:float)
voidset_agent_max_climb(value:float)
- floatget_agent_max_climb()
floatget_agent_max_climb()
The minimum ledge height that is considered to still be traversable.
Note:While baking, this value will be rounded down to the nearest multiple ofcell_height.
floatagent_max_slope=45.0🔗
- voidset_agent_max_slope(value:float)
voidset_agent_max_slope(value:float)
- floatget_agent_max_slope()
floatget_agent_max_slope()
The maximum slope that is considered walkable, in degrees.
floatagent_radius=0.5🔗
- voidset_agent_radius(value:float)
voidset_agent_radius(value:float)
- floatget_agent_radius()
floatget_agent_radius()
The distance to erode/shrink the walkable area of the heightfield away from obstructions.
Note:While baking, this value will be rounded up to the nearest multiple ofcell_size.
Note:The radius must be equal or higher than0.0. If the radius is0.0, it won't be possible to fix invalid outline overlaps and other precision errors during the baking process. As a result, some obstacles may be excluded incorrectly from the final navigation mesh, or may delete the navigation mesh's polygons.
floatborder_size=0.0🔗
- voidset_border_size(value:float)
voidset_border_size(value:float)
- floatget_border_size()
floatget_border_size()
The size of the non-navigable border around the bake bounding area.
In conjunction with thefilter_baking_aabband aedge_max_errorvalue at1.0or below the border size can be used to bake tile aligned navigation meshes without the tile edges being shrunk byagent_radius.
Note:If this value is not0.0, it will be rounded up to the nearest multiple ofcell_sizeduring baking.
floatcell_height=0.25🔗
- voidset_cell_height(value:float)
voidset_cell_height(value:float)
- floatget_cell_height()
floatget_cell_height()
The cell height used to rasterize the navigation mesh vertices on the Y axis. Must match with the cell height on the navigation map.
floatcell_size=0.25🔗
- voidset_cell_size(value:float)
voidset_cell_size(value:float)
- floatget_cell_size()
floatget_cell_size()
The cell size used to rasterize the navigation mesh vertices on the XZ plane. Must match with the cell size on the navigation map.
floatdetail_sample_distance=6.0🔗
- voidset_detail_sample_distance(value:float)
voidset_detail_sample_distance(value:float)
- floatget_detail_sample_distance()
floatget_detail_sample_distance()
The sampling distance to use when generating the detail mesh, in cell unit.
floatdetail_sample_max_error=1.0🔗
- voidset_detail_sample_max_error(value:float)
voidset_detail_sample_max_error(value:float)
- floatget_detail_sample_max_error()
floatget_detail_sample_max_error()
The maximum distance the detail mesh surface should deviate from heightfield, in cell unit.
floatedge_max_error=1.3🔗
- voidset_edge_max_error(value:float)
voidset_edge_max_error(value:float)
- floatget_edge_max_error()
floatget_edge_max_error()
The maximum distance a simplified contour's border edges should deviate the original raw contour.
floatedge_max_length=0.0🔗
- voidset_edge_max_length(value:float)
voidset_edge_max_length(value:float)
- floatget_edge_max_length()
floatget_edge_max_length()
The maximum allowed length for contour edges along the border of the mesh. A value of0.0disables this feature.
Note:While baking, this value will be rounded up to the nearest multiple ofcell_size.
AABBfilter_baking_aabb=AABB(0,0,0,0,0,0)🔗
- voidset_filter_baking_aabb(value:AABB)
voidset_filter_baking_aabb(value:AABB)
- AABBget_filter_baking_aabb()
AABBget_filter_baking_aabb()
If the bakingAABBhas a volume the navigation mesh baking will be restricted to its enclosing area.
Vector3filter_baking_aabb_offset=Vector3(0,0,0)🔗
- voidset_filter_baking_aabb_offset(value:Vector3)
voidset_filter_baking_aabb_offset(value:Vector3)
- Vector3get_filter_baking_aabb_offset()
Vector3get_filter_baking_aabb_offset()
The position offset applied to thefilter_baking_aabbAABB.
boolfilter_ledge_spans=false🔗
- voidset_filter_ledge_spans(value:bool)
voidset_filter_ledge_spans(value:bool)
- boolget_filter_ledge_spans()
boolget_filter_ledge_spans()
Iftrue, marks spans that are ledges as non-walkable.
boolfilter_low_hanging_obstacles=false🔗
- voidset_filter_low_hanging_obstacles(value:bool)
voidset_filter_low_hanging_obstacles(value:bool)
- boolget_filter_low_hanging_obstacles()
boolget_filter_low_hanging_obstacles()
Iftrue, marks non-walkable spans as walkable if their maximum is withinagent_max_climbof a walkable neighbor.
boolfilter_walkable_low_height_spans=false🔗
- voidset_filter_walkable_low_height_spans(value:bool)
voidset_filter_walkable_low_height_spans(value:bool)
- boolget_filter_walkable_low_height_spans()
boolget_filter_walkable_low_height_spans()
Iftrue, marks walkable spans as not walkable if the clearance above the span is less thanagent_height.
intgeometry_collision_mask=4294967295🔗
- voidset_collision_mask(value:int)
voidset_collision_mask(value:int)
- intget_collision_mask()
intget_collision_mask()
The physics layers to scan for static colliders.
Only used whengeometry_parsed_geometry_typeisPARSED_GEOMETRY_STATIC_COLLIDERSorPARSED_GEOMETRY_BOTH.
ParsedGeometryTypegeometry_parsed_geometry_type=2🔗
- voidset_parsed_geometry_type(value:ParsedGeometryType)
voidset_parsed_geometry_type(value:ParsedGeometryType)
- ParsedGeometryTypeget_parsed_geometry_type()
ParsedGeometryTypeget_parsed_geometry_type()
Determines which type of nodes will be parsed as geometry.
SourceGeometryModegeometry_source_geometry_mode=0🔗
- voidset_source_geometry_mode(value:SourceGeometryMode)
voidset_source_geometry_mode(value:SourceGeometryMode)
- SourceGeometryModeget_source_geometry_mode()
SourceGeometryModeget_source_geometry_mode()
The source of the geometry used when baking.
StringNamegeometry_source_group_name=&"navigation_mesh_source_group"🔗
- voidset_source_group_name(value:StringName)
voidset_source_group_name(value:StringName)
- StringNameget_source_group_name()
StringNameget_source_group_name()
The name of the group to scan for geometry.
Only used whengeometry_source_geometry_modeisSOURCE_GEOMETRY_GROUPS_WITH_CHILDRENorSOURCE_GEOMETRY_GROUPS_EXPLICIT.
floatregion_merge_size=20.0🔗
- voidset_region_merge_size(value:float)
voidset_region_merge_size(value:float)
- floatget_region_merge_size()
floatget_region_merge_size()
Any regions with a size smaller than this will be merged with larger regions if possible.
Note:This value will be squared to calculate the number of cells. For example, a value of 20 will set the number of cells to 400.
floatregion_min_size=2.0🔗
- voidset_region_min_size(value:float)
voidset_region_min_size(value:float)
- floatget_region_min_size()
floatget_region_min_size()
The minimum size of a region for it to be created.
Note:This value will be squared to calculate the minimum number of cells allowed to form isolated island areas. For example, a value of 8 will set the number of cells to 64.
SamplePartitionTypesample_partition_type=0🔗
- voidset_sample_partition_type(value:SamplePartitionType)
voidset_sample_partition_type(value:SamplePartitionType)
- SamplePartitionTypeget_sample_partition_type()
SamplePartitionTypeget_sample_partition_type()
Partitioning algorithm for creating the navigation mesh polys.
floatvertices_per_polygon=6.0🔗
- voidset_vertices_per_polygon(value:float)
voidset_vertices_per_polygon(value:float)
- floatget_vertices_per_polygon()
floatget_vertices_per_polygon()
The maximum number of vertices allowed for polygons generated during the contour to polygon conversion process.

## Method Descriptions
voidadd_polygon(polygon:PackedInt32Array)🔗
Adds a polygon using the indices of the vertices you get when callingget_vertices().
voidclear()🔗
Clears the internal arrays for vertices and polygon indices.
voidclear_polygons()🔗
Clears the array of polygons, but it doesn't clear the array of vertices.
voidcreate_from_mesh(mesh:Mesh)🔗
Initializes the navigation mesh by setting the vertices and indices according to aMesh.
Note:The givenmeshmust be of typeMesh.PRIMITIVE_TRIANGLESand have an index array.
boolget_collision_mask_value(layer_number:int)const🔗
Returns whether or not the specified layer of thegeometry_collision_maskis enabled, given alayer_numberbetween 1 and 32.
PackedInt32Arrayget_polygon(idx:int)🔗
Returns aPackedInt32Arraycontaining the indices of the vertices of a created polygon.
intget_polygon_count()const🔗
Returns the number of polygons in the navigation mesh.
PackedVector3Arrayget_vertices()const🔗
Returns aPackedVector3Arraycontaining all the vertices being used to create the polygons.
voidset_collision_mask_value(layer_number:int, value:bool)🔗
Based onvalue, enables or disables the specified layer in thegeometry_collision_mask, given alayer_numberbetween 1 and 32.
voidset_vertices(vertices:PackedVector3Array)🔗
Sets the vertices that can be then indexed to create polygons with theadd_polygon()method.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.