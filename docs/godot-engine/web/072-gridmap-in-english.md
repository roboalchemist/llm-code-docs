# GridMap in English

# GridMap

Inherits:Node3D<Node<Object
Node for 3D tile-based maps.

## Description

GridMap lets you place meshes on a grid interactively. It works both from the editor and from scripts, which can help you create in-game level editors.
GridMaps use aMeshLibrarywhich contains a list of tiles. Each tile is a mesh with materials plus optional collision and navigation shapes.
A GridMap contains a collection of cells. Each grid cell refers to a tile in theMeshLibrary. All cells in the map have the same dimensions.
Internally, a GridMap is split into a sparse collection of octants for efficient rendering and physics processing. Every octant has the same dimensions and can contain several cells.
Note:GridMap doesn't extendVisualInstance3Dand therefore can't be hidden or cull masked based onVisualInstance3D.layers. If you make a light not affect the first layer, the whole GridMap won't be lit by the light in question.

## Tutorials

- Using gridmaps
Using gridmaps
- 3D Platformer Demo
3D Platformer Demo
- 3D Kinematic Character Demo
3D Kinematic Character Demo

## Properties

| bool | bake_navigation | false |
|---|---|---|
| bool | cell_center_x | true |
| bool | cell_center_y | true |
| bool | cell_center_z | true |
| int | cell_octant_size | 8 |
| float | cell_scale | 1.0 |
| Vector3 | cell_size | Vector3(2,2,2) |
| int | collision_layer | 1 |
| int | collision_mask | 1 |
| float | collision_priority | 1.0 |
| MeshLibrary | mesh_library |  |
| PhysicsMaterial | physics_material |  |

bool
bake_navigation
false
bool
cell_center_x
true
bool
cell_center_y
true
bool
cell_center_z
true
cell_octant_size
float
cell_scale
Vector3
cell_size
Vector3(2,2,2)
collision_layer
collision_mask
float
collision_priority
MeshLibrary
mesh_library
PhysicsMaterial
physics_material

## Methods

| void | clear() |
|---|---|
| void | clear_baked_meshes() |
| RID | get_bake_mesh_instance(idx:int) |
| Array | get_bake_meshes() |
| Basis | get_basis_with_orthogonal_index(index:int)const |
| int | get_cell_item(position:Vector3i)const |
| Basis | get_cell_item_basis(position:Vector3i)const |
| int | get_cell_item_orientation(position:Vector3i)const |
| bool | get_collision_layer_value(layer_number:int)const |
| bool | get_collision_mask_value(layer_number:int)const |
| Array | get_meshes()const |
| RID | get_navigation_map()const |
| int | get_orthogonal_index_from_basis(basis:Basis)const |
| Array[Vector3i] | get_used_cells()const |
| Array[Vector3i] | get_used_cells_by_item(item:int)const |
| Vector3i | local_to_map(local_position:Vector3)const |
| void | make_baked_meshes(gen_lightmap_uv:bool= false, lightmap_uv_texel_size:float= 0.1) |
| Vector3 | map_to_local(map_position:Vector3i)const |
| void | resource_changed(resource:Resource) |
| void | set_cell_item(position:Vector3i, item:int, orientation:int= 0) |
| void | set_collision_layer_value(layer_number:int, value:bool) |
| void | set_collision_mask_value(layer_number:int, value:bool) |
| void | set_navigation_map(navigation_map:RID) |

void
clear()
void
clear_baked_meshes()
get_bake_mesh_instance(idx:int)
Array
get_bake_meshes()
Basis
get_basis_with_orthogonal_index(index:int)const
get_cell_item(position:Vector3i)const
Basis
get_cell_item_basis(position:Vector3i)const
get_cell_item_orientation(position:Vector3i)const
bool
get_collision_layer_value(layer_number:int)const
bool
get_collision_mask_value(layer_number:int)const
Array
get_meshes()const
get_navigation_map()const
get_orthogonal_index_from_basis(basis:Basis)const
Array[Vector3i]
get_used_cells()const
Array[Vector3i]
get_used_cells_by_item(item:int)const
Vector3i
local_to_map(local_position:Vector3)const
void
make_baked_meshes(gen_lightmap_uv:bool= false, lightmap_uv_texel_size:float= 0.1)
Vector3
map_to_local(map_position:Vector3i)const
void
resource_changed(resource:Resource)
void
set_cell_item(position:Vector3i, item:int, orientation:int= 0)
void
set_collision_layer_value(layer_number:int, value:bool)
void
set_collision_mask_value(layer_number:int, value:bool)
void
set_navigation_map(navigation_map:RID)

## Signals

cell_size_changed(cell_size:Vector3)🔗
Emitted whencell_sizechanges.
changed()🔗
Emitted when theMeshLibraryof this GridMap changes.

## Constants

INVALID_CELL_ITEM=-1🔗
Invalid cell item that can be used inset_cell_item()to clear cells (or represent an empty cell inget_cell_item()).

## Property Descriptions

boolbake_navigation=false🔗

- voidset_bake_navigation(value:bool)
voidset_bake_navigation(value:bool)
- boolis_baking_navigation()
boolis_baking_navigation()
Iftrue, this GridMap creates a navigation region for each cell that uses amesh_libraryitem with a navigation mesh. The created navigation region will use the navigation layers bitmask assigned to theMeshLibrary's item.
boolcell_center_x=true🔗
- voidset_center_x(value:bool)
voidset_center_x(value:bool)
- boolget_center_x()
boolget_center_x()
Iftrue, grid items are centered on the X axis.
boolcell_center_y=true🔗
- voidset_center_y(value:bool)
voidset_center_y(value:bool)
- boolget_center_y()
boolget_center_y()
Iftrue, grid items are centered on the Y axis.
boolcell_center_z=true🔗
- voidset_center_z(value:bool)
voidset_center_z(value:bool)
- boolget_center_z()
boolget_center_z()
Iftrue, grid items are centered on the Z axis.
intcell_octant_size=8🔗
- voidset_octant_size(value:int)
voidset_octant_size(value:int)
- intget_octant_size()
intget_octant_size()
The size of each octant measured in number of cells. This applies to all three axis.
floatcell_scale=1.0🔗
- voidset_cell_scale(value:float)
voidset_cell_scale(value:float)
- floatget_cell_scale()
floatget_cell_scale()
The scale of the cell items.
This does not affect the size of the grid cells themselves, only the items in them. This can be used to make cell items overlap their neighbors.
Vector3cell_size=Vector3(2,2,2)🔗
- voidset_cell_size(value:Vector3)
voidset_cell_size(value:Vector3)
- Vector3get_cell_size()
Vector3get_cell_size()
The dimensions of the grid's cells.
This does not affect the size of the meshes. Seecell_scale.
intcollision_layer=1🔗
- voidset_collision_layer(value:int)
voidset_collision_layer(value:int)
- intget_collision_layer()
intget_collision_layer()
The physics layers this GridMap is in.
GridMaps act as static bodies, meaning they aren't affected by gravity or other forces. They only affect other physics bodies that collide with them.
intcollision_mask=1🔗
- voidset_collision_mask(value:int)
voidset_collision_mask(value:int)
- intget_collision_mask()
intget_collision_mask()
The physics layers this GridMap detects collisions in. SeeCollision layers and masksin the documentation for more information.
floatcollision_priority=1.0🔗
- voidset_collision_priority(value:float)
voidset_collision_priority(value:float)
- floatget_collision_priority()
floatget_collision_priority()
The priority used to solve colliding when occurring penetration. The higher the priority is, the lower the penetration into the object will be. This can for example be used to prevent the player from breaking through the boundaries of a level.
MeshLibrarymesh_library🔗
- voidset_mesh_library(value:MeshLibrary)
voidset_mesh_library(value:MeshLibrary)
- MeshLibraryget_mesh_library()
MeshLibraryget_mesh_library()
The assignedMeshLibrary.
PhysicsMaterialphysics_material🔗
- voidset_physics_material(value:PhysicsMaterial)
voidset_physics_material(value:PhysicsMaterial)
- PhysicsMaterialget_physics_material()
PhysicsMaterialget_physics_material()
Overrides the default friction and bounce physics properties for the wholeGridMap.

## Method Descriptions

voidclear()🔗
Clear all cells.
voidclear_baked_meshes()🔗
Clears all baked meshes. Seemake_baked_meshes().
RIDget_bake_mesh_instance(idx:int)🔗
ReturnsRIDof a baked mesh with the givenidx.
Arrayget_bake_meshes()🔗
Returns an array ofArrayMeshes andTransform3Dreferences of all bake meshes that exist within the current GridMap. Even indices containArrayMeshes, while odd indices containTransform3Ds that are always equal toTransform3D.IDENTITY.
This method relies on the output ofmake_baked_meshes(), which will be called withgen_lightmap_uvset totrueandlightmap_uv_texel_sizeset to0.1if it hasn't been called yet.
Basisget_basis_with_orthogonal_index(index:int)const🔗
Returns one of 24 possible rotations that lie along the vectors (x,y,z) with each component being either -1, 0, or 1. For further details, refer to the Godot source code.
intget_cell_item(position:Vector3i)const🔗
TheMeshLibraryitem index located at the given grid coordinates. If the cell is empty,INVALID_CELL_ITEMwill be returned.
Basisget_cell_item_basis(position:Vector3i)const🔗
Returns the basis that gives the specified cell its orientation.
intget_cell_item_orientation(position:Vector3i)const🔗
The orientation of the cell at the given grid coordinates.-1is returned if the cell is empty.
boolget_collision_layer_value(layer_number:int)const🔗
Returns whether or not the specified layer of thecollision_layeris enabled, given alayer_numberbetween 1 and 32.
boolget_collision_mask_value(layer_number:int)const🔗
Returns whether or not the specified layer of thecollision_maskis enabled, given alayer_numberbetween 1 and 32.
Arrayget_meshes()const🔗
Returns an array ofTransform3DandMeshreferences corresponding to the non-empty cells in the grid. The transforms are specified in local space. Even indices containTransform3Ds, while odd indices containMeshes related to theTransform3Din the index preceding it.
RIDget_navigation_map()const🔗
Returns theRIDof the navigation map this GridMap node uses for its cell baked navigation meshes.
This function returns always the map set on the GridMap node and not the map on the NavigationServer. If the map is changed directly with the NavigationServer API the GridMap node will not be aware of the map change.
intget_orthogonal_index_from_basis(basis:Basis)const🔗
This function considers a discretization of rotations into 24 points on unit sphere, lying along the vectors (x,y,z) with each component being either -1, 0, or 1, and returns the index (in the range from 0 to 23) of the point best representing the orientation of the object. For further details, refer to the Godot source code.
Array[Vector3i]get_used_cells()const🔗
Returns an array ofVector3with the non-empty cell coordinates in the grid map.
Array[Vector3i]get_used_cells_by_item(item:int)const🔗
Returns an array of all cells with the given item index specified initem.
Vector3ilocal_to_map(local_position:Vector3)const🔗
Returns the map coordinates of the cell containing the givenlocal_position. Iflocal_positionis in global coordinates, consider usingNode3D.to_local()before passing it to this method. See alsomap_to_local().
voidmake_baked_meshes(gen_lightmap_uv:bool= false, lightmap_uv_texel_size:float= 0.1)🔗
Generates a baked mesh that represents all meshes in the assignedMeshLibraryfor use withLightmapGI. Ifgen_lightmap_uvistrue, UV2 data will be generated for each mesh currently used in theGridMap. Otherwise, only meshes that already have UV2 data present will be able to use baked lightmaps. When generating UV2,lightmap_uv_texel_sizecontrols the texel density for lightmaps, with lower values resulting in more detailed lightmaps.lightmap_uv_texel_sizeis ignored ifgen_lightmap_uvisfalse. See alsoget_bake_meshes(), which relies on the output of this method.
Note:Calling this method will not actually bake lightmaps, as lightmap baking is performed using theLightmapGInode.
Vector3map_to_local(map_position:Vector3i)const🔗
Returns the position of a grid cell in the GridMap's local coordinate space. To convert the returned value into global coordinates, useNode3D.to_global(). See alsolocal_to_map().
voidresource_changed(resource:Resource)🔗
Deprecated:UseResource.changedinstead.
This method does nothing.
voidset_cell_item(position:Vector3i, item:int, orientation:int= 0)🔗
Sets the mesh index for the cell referenced by its grid coordinates.
A negative item index such asINVALID_CELL_ITEMwill clear the cell.
Optionally, the item's orientation can be passed. For valid orientation values, seeget_orthogonal_index_from_basis().
voidset_collision_layer_value(layer_number:int, value:bool)🔗
Based onvalue, enables or disables the specified layer in thecollision_layer, given alayer_numberbetween 1 and 32.
voidset_collision_mask_value(layer_number:int, value:bool)🔗
Based onvalue, enables or disables the specified layer in thecollision_mask, given alayer_numberbetween 1 and 32.
voidset_navigation_map(navigation_map:RID)🔗
Sets theRIDof the navigation map this GridMap node should use for its cell baked navigation meshes.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
