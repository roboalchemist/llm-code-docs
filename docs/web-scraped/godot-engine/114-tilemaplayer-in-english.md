# TileMapLayer in English

# TileMapLayer
Inherits:Node2D<CanvasItem<Node<Object
Node for 2D tile-based maps.

## Description
Node for 2D tile-based maps. ATileMapLayeruses aTileSetwhich contain a list of tiles which are used to create grid-based maps. Unlike theTileMapnode, which is deprecated,TileMapLayerhas only one layer of tiles. You can use severalTileMapLayerto achieve the same result as aTileMapnode.
For performance reasons, all TileMap updates are batched at the end of a frame. Notably, this means that scene tiles from aTileSetScenesCollectionSourceare initialized after their parent. This is only queued when inside the scene tree.
To force an update earlier on, callupdate_internals().
Note:For performance and compatibility reasons, the coordinates serialized byTileMapLayerare limited to 16-bit signed integers, i.e. the range for X and Y coordinates is from-32768to32767. When saving tile data, tiles outside this range are wrapped.

## Tutorials
- Using Tilemaps
Using Tilemaps
- 2D Platformer Demo
2D Platformer Demo
- 2D Isometric Demo
2D Isometric Demo
- 2D Hexagonal Demo
2D Hexagonal Demo
- 2D Grid-based Navigation with AStarGrid2D Demo
2D Grid-based Navigation with AStarGrid2D Demo
- 2D Role Playing Game (RPG) Demo
2D Role Playing Game (RPG) Demo
- 2D Kinematic Character Demo
2D Kinematic Character Demo
- 2D Dynamic TileMap Layers Demo
2D Dynamic TileMap Layers Demo

## Properties

| bool | collision_enabled | true |
|---|---|---|
| DebugVisibilityMode | collision_visibility_mode | 0 |
| bool | enabled | true |
| bool | navigation_enabled | true |
| DebugVisibilityMode | navigation_visibility_mode | 0 |
| bool | occlusion_enabled | true |
| int | physics_quadrant_size | 16 |
| int | rendering_quadrant_size | 16 |
| PackedByteArray | tile_map_data | PackedByteArray() |
| TileSet | tile_set |  |
| bool | use_kinematic_bodies | false |
| bool | x_draw_order_reversed | false |
| int | y_sort_origin | 0 |

bool
collision_enabled
true
DebugVisibilityMode
collision_visibility_mode
bool
enabled
true
bool
navigation_enabled
true
DebugVisibilityMode
navigation_visibility_mode
bool
occlusion_enabled
true
physics_quadrant_size
rendering_quadrant_size
PackedByteArray
tile_map_data
PackedByteArray()
TileSet
tile_set
bool
use_kinematic_bodies
false
bool
x_draw_order_reversed
false
y_sort_origin

## Methods

| void | _tile_data_runtime_update(coords:Vector2i, tile_data:TileData)virtual |
|---|---|
| void | _update_cells(coords:Array[Vector2i], forced_cleanup:bool)virtual |
| bool | _use_tile_data_runtime_update(coords:Vector2i)virtual |
| void | clear() |
| void | erase_cell(coords:Vector2i) |
| void | fix_invalid_tiles() |
| int | get_cell_alternative_tile(coords:Vector2i)const |
| Vector2i | get_cell_atlas_coords(coords:Vector2i)const |
| int | get_cell_source_id(coords:Vector2i)const |
| TileData | get_cell_tile_data(coords:Vector2i)const |
| Vector2i | get_coords_for_body_rid(body:RID)const |
| RID | get_navigation_map()const |
| Vector2i | get_neighbor_cell(coords:Vector2i, neighbor:CellNeighbor)const |
| TileMapPattern | get_pattern(coords_array:Array[Vector2i]) |
| Array[Vector2i] | get_surrounding_cells(coords:Vector2i) |
| Array[Vector2i] | get_used_cells()const |
| Array[Vector2i] | get_used_cells_by_id(source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= -1)const |
| Rect2i | get_used_rect()const |
| bool | has_body_rid(body:RID)const |
| bool | is_cell_flipped_h(coords:Vector2i)const |
| bool | is_cell_flipped_v(coords:Vector2i)const |
| bool | is_cell_transposed(coords:Vector2i)const |
| Vector2i | local_to_map(local_position:Vector2)const |
| Vector2i | map_pattern(position_in_tilemap:Vector2i, coords_in_pattern:Vector2i, pattern:TileMapPattern) |
| Vector2 | map_to_local(map_position:Vector2i)const |
| void | notify_runtime_tile_data_update() |
| void | set_cell(coords:Vector2i, source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= 0) |
| void | set_cells_terrain_connect(cells:Array[Vector2i], terrain_set:int, terrain:int, ignore_empty_terrains:bool= true) |
| void | set_cells_terrain_path(path:Array[Vector2i], terrain_set:int, terrain:int, ignore_empty_terrains:bool= true) |
| void | set_navigation_map(map:RID) |
| void | set_pattern(position:Vector2i, pattern:TileMapPattern) |
| void | update_internals() |

void
_tile_data_runtime_update(coords:Vector2i, tile_data:TileData)virtual
void
_update_cells(coords:Array[Vector2i], forced_cleanup:bool)virtual
bool
_use_tile_data_runtime_update(coords:Vector2i)virtual
void
clear()
void
erase_cell(coords:Vector2i)
void
fix_invalid_tiles()
get_cell_alternative_tile(coords:Vector2i)const
Vector2i
get_cell_atlas_coords(coords:Vector2i)const
get_cell_source_id(coords:Vector2i)const
TileData
get_cell_tile_data(coords:Vector2i)const
Vector2i
get_coords_for_body_rid(body:RID)const
get_navigation_map()const
Vector2i
get_neighbor_cell(coords:Vector2i, neighbor:CellNeighbor)const
TileMapPattern
get_pattern(coords_array:Array[Vector2i])
Array[Vector2i]
get_surrounding_cells(coords:Vector2i)
Array[Vector2i]
get_used_cells()const
Array[Vector2i]
get_used_cells_by_id(source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= -1)const
Rect2i
get_used_rect()const
bool
has_body_rid(body:RID)const
bool
is_cell_flipped_h(coords:Vector2i)const
bool
is_cell_flipped_v(coords:Vector2i)const
bool
is_cell_transposed(coords:Vector2i)const
Vector2i
local_to_map(local_position:Vector2)const
Vector2i
map_pattern(position_in_tilemap:Vector2i, coords_in_pattern:Vector2i, pattern:TileMapPattern)
Vector2
map_to_local(map_position:Vector2i)const
void
notify_runtime_tile_data_update()
void
set_cell(coords:Vector2i, source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= 0)
void
set_cells_terrain_connect(cells:Array[Vector2i], terrain_set:int, terrain:int, ignore_empty_terrains:bool= true)
void
set_cells_terrain_path(path:Array[Vector2i], terrain_set:int, terrain:int, ignore_empty_terrains:bool= true)
void
set_navigation_map(map:RID)
void
set_pattern(position:Vector2i, pattern:TileMapPattern)
void
update_internals()

## Signals
changed()🔗
Emitted when thisTileMapLayer's properties changes. This includes modified cells, properties, or changes made to its assignedTileSet.
Note:This signal may be emitted very often when batch-modifying aTileMapLayer. Avoid executing complex processing in a connected function, and consider delaying it to the end of the frame instead (i.e. callingObject.call_deferred()).

## Enumerations
enumDebugVisibilityMode:🔗
DebugVisibilityModeDEBUG_VISIBILITY_MODE_DEFAULT=0
Hide the collisions or navigation debug shapes in the editor, and use the debug settings to determine their visibility in game (i.e.SceneTree.debug_collisions_hintorSceneTree.debug_navigation_hint).
DebugVisibilityModeDEBUG_VISIBILITY_MODE_FORCE_HIDE=2
Always hide the collisions or navigation debug shapes.
DebugVisibilityModeDEBUG_VISIBILITY_MODE_FORCE_SHOW=1
Always show the collisions or navigation debug shapes.

## Property Descriptions
boolcollision_enabled=true🔗
- voidset_collision_enabled(value:bool)
voidset_collision_enabled(value:bool)
- boolis_collision_enabled()
boolis_collision_enabled()
Enable or disable collisions.
DebugVisibilityModecollision_visibility_mode=0🔗
- voidset_collision_visibility_mode(value:DebugVisibilityMode)
voidset_collision_visibility_mode(value:DebugVisibilityMode)
- DebugVisibilityModeget_collision_visibility_mode()
DebugVisibilityModeget_collision_visibility_mode()
Show or hide theTileMapLayer's collision shapes. If set toDEBUG_VISIBILITY_MODE_DEFAULT, this depends on the show collision debug settings.
boolenabled=true🔗
- voidset_enabled(value:bool)
voidset_enabled(value:bool)
- boolis_enabled()
boolis_enabled()
Iffalse, disables thisTileMapLayercompletely (rendering, collision, navigation, scene tiles, etc.)
boolnavigation_enabled=true🔗
- voidset_navigation_enabled(value:bool)
voidset_navigation_enabled(value:bool)
- boolis_navigation_enabled()
boolis_navigation_enabled()
Iftrue, navigation regions are enabled.
DebugVisibilityModenavigation_visibility_mode=0🔗
- voidset_navigation_visibility_mode(value:DebugVisibilityMode)
voidset_navigation_visibility_mode(value:DebugVisibilityMode)
- DebugVisibilityModeget_navigation_visibility_mode()
DebugVisibilityModeget_navigation_visibility_mode()
Show or hide theTileMapLayer's navigation meshes. If set toDEBUG_VISIBILITY_MODE_DEFAULT, this depends on the show navigation debug settings.
boolocclusion_enabled=true🔗
- voidset_occlusion_enabled(value:bool)
voidset_occlusion_enabled(value:bool)
- boolis_occlusion_enabled()
boolis_occlusion_enabled()
Enable or disable light occlusion.
intphysics_quadrant_size=16🔗
- voidset_physics_quadrant_size(value:int)
voidset_physics_quadrant_size(value:int)
- intget_physics_quadrant_size()
intget_physics_quadrant_size()
TheTileMapLayer's physics quadrant size. Within a physics quadrant, cells with similar physics properties are grouped together and their collision shapes get merged.physics_quadrant_sizedefines the length of a square's side, in the map's coordinate system, that forms the quadrant. Thus, the default quadrant size groups together16*16=256tiles.
Note:As quadrants are created according to the map's coordinate system, the quadrant's "square shape" might not look like square in theTileMapLayer's local coordinate system.
Note:This impacts the value returned byget_coords_for_body_rid(). Higher values will make that function less precise. To get the exact cell coordinates, you need to setphysics_quadrant_sizeto1, which disables physics chunking.
intrendering_quadrant_size=16🔗
- voidset_rendering_quadrant_size(value:int)
voidset_rendering_quadrant_size(value:int)
- intget_rendering_quadrant_size()
intget_rendering_quadrant_size()
TheTileMapLayer's rendering quadrant size. A quadrant is a group of tiles to be drawn together on a single canvas item, for optimization purposes.rendering_quadrant_sizedefines the length of a square's side, in the map's coordinate system, that forms the quadrant. Thus, the default quadrant size groups together16*16=256tiles.
The quadrant size does not apply on a Y-sortedTileMapLayer, as tiles are grouped by Y position instead in that case.
Note:As quadrants are created according to the map's coordinate system, the quadrant's "square shape" might not look like square in theTileMapLayer's local coordinate system.
PackedByteArraytile_map_data=PackedByteArray()🔗
- voidset_tile_map_data_from_array(value:PackedByteArray)
voidset_tile_map_data_from_array(value:PackedByteArray)
- PackedByteArrayget_tile_map_data_as_array()
PackedByteArrayget_tile_map_data_as_array()
The raw tile map data as a byte array.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedByteArrayfor more details.
TileSettile_set🔗
- voidset_tile_set(value:TileSet)
voidset_tile_set(value:TileSet)
- TileSetget_tile_set()
TileSetget_tile_set()
TheTileSetused by this layer. The textures, collisions, and additional behavior of all available tiles are stored here.
booluse_kinematic_bodies=false🔗
- voidset_use_kinematic_bodies(value:bool)
voidset_use_kinematic_bodies(value:bool)
- boolis_using_kinematic_bodies()
boolis_using_kinematic_bodies()
Iftrue, thisTileMapLayercollision shapes will be instantiated as kinematic bodies. This can be needed for movingTileMapLayernodes (i.e. moving platforms).
boolx_draw_order_reversed=false🔗
- voidset_x_draw_order_reversed(value:bool)
voidset_x_draw_order_reversed(value:bool)
- boolis_x_draw_order_reversed()
boolis_x_draw_order_reversed()
IfCanvasItem.y_sort_enabledis enabled, setting this totruewill reverse the order the tiles are drawn on the X-axis.
inty_sort_origin=0🔗
- voidset_y_sort_origin(value:int)
voidset_y_sort_origin(value:int)
- intget_y_sort_origin()
intget_y_sort_origin()
This Y-sort origin value is added to each tile's Y-sort origin value. This allows, for example, to fake a different height level. This can be useful for top-down view games.

## Method Descriptions
void_tile_data_runtime_update(coords:Vector2i, tile_data:TileData)virtual🔗
Called with aTileDataobject about to be used internally by theTileMapLayer, allowing its modification at runtime.
This method is only called if_use_tile_data_runtime_update()is implemented and returnstruefor the given tilecoords.
Warning:Thetile_dataobject's sub-resources are the same as the one in the TileSet. Modifying them might impact the whole TileSet. Instead, make sure to duplicate those resources.
Note:If the properties oftile_dataobject should change over time, usenotify_runtime_tile_data_update()to notify theTileMapLayerit needs an update.
void_update_cells(coords:Array[Vector2i], forced_cleanup:bool)virtual🔗
Called when thisTileMapLayer's cells need an internal update. This update may be caused from individual cells being modified or by a change in thetile_set(causing all cells to be queued for an update). The first call to this function is always for initializing all theTileMapLayer's cells.coordscontains the coordinates of all modified cells, roughly in the order they were modified.forced_cleanupistruewhen theTileMapLayer's internals should be fully cleaned up. This is the case when:
- The layer is disabled;
The layer is disabled;
- The layer is not visible;
The layer is not visible;
- tile_setis set tonull;
tile_setis set tonull;
- The node is removed from the tree;
The node is removed from the tree;
- The node is freed.
The node is freed.
Note that any internal update happening while one of these conditions is verified is considered to be a "cleanup". See alsoupdate_internals().
Warning:Implementing this method may degrade theTileMapLayer's performance.
bool_use_tile_data_runtime_update(coords:Vector2i)virtual🔗
Should returntrueif the tile at coordinatescoordsrequires a runtime update.
Warning:Make sure this function only returnstruewhen needed. Any tile processed at runtime without a need for it will imply a significant performance penalty.
Note:If the result of this function should change, usenotify_runtime_tile_data_update()to notify theTileMapLayerit needs an update.
voidclear()🔗
Clears all cells.
voiderase_cell(coords:Vector2i)🔗
Erases the cell at coordinatescoords.
voidfix_invalid_tiles()🔗
Clears cells containing tiles that do not exist in thetile_set.
intget_cell_alternative_tile(coords:Vector2i)const🔗
Returns the tile alternative ID of the cell at coordinatescoords.
Vector2iget_cell_atlas_coords(coords:Vector2i)const🔗
Returns the tile atlas coordinates ID of the cell at coordinatescoords. ReturnsVector2i(-1,-1)if the cell does not exist.
intget_cell_source_id(coords:Vector2i)const🔗
Returns the tile source ID of the cell at coordinatescoords. Returns-1if the cell does not exist.
TileDataget_cell_tile_data(coords:Vector2i)const🔗
Returns theTileDataobject associated with the given cell, ornullif the cell does not exist or is not aTileSetAtlasSource.
```
func get_clicked_tile_power():
    var clicked_cell = tile_map_layer.local_to_map(tile_map_layer.get_local_mouse_position())
    var data = tile_map_layer.get_cell_tile_data(clicked_cell)
    if data:
        return data.get_custom_data("power")
    else:
        return 0
```
Vector2iget_coords_for_body_rid(body:RID)const🔗
Returns the coordinates of the physics quadrant (seephysics_quadrant_size) for given physics bodyRID. Such anRIDcan be retrieved fromKinematicCollision2D.get_collider_rid(), when colliding with a tile.
Note:Higher values ofphysics_quadrant_sizewill make this function less precise. To get the exact cell coordinates, you need to setphysics_quadrant_sizeto1, which disables physics chunking.
RIDget_navigation_map()const🔗
Returns theRIDof theNavigationServer2Dnavigation used by thisTileMapLayer.
By default this returns the defaultWorld2Dnavigation map, unless a custom map was provided usingset_navigation_map().
Vector2iget_neighbor_cell(coords:Vector2i, neighbor:CellNeighbor)const🔗
Returns the neighboring cell to the one at coordinatescoords, identified by theneighbordirection. This method takes into account the different layouts a TileMap can take.
TileMapPatternget_pattern(coords_array:Array[Vector2i])🔗
Creates and returns a newTileMapPatternfrom the given array of cells. See alsoset_pattern().
Array[Vector2i]get_surrounding_cells(coords:Vector2i)🔗
Returns the list of all neighboring cells to the one atcoords. Any neighboring cell is one that is touching edges, so for a square cell 4 cells would be returned, for a hexagon 6 cells are returned.
Array[Vector2i]get_used_cells()const🔗
Returns aVector2iarray with the positions of all cells containing a tile. A cell is considered empty if its source identifier equals-1, its atlas coordinate identifier isVector2(-1,-1)and its alternative identifier is-1.
Array[Vector2i]get_used_cells_by_id(source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= -1)const🔗
Returns aVector2iarray with the positions of all cells containing a tile. Tiles may be filtered according to their source (source_id), their atlas coordinates (atlas_coords), or alternative id (alternative_tile).
If a parameter has its value set to the default one, this parameter is not used to filter a cell. Thus, if all parameters have their respective default values, this method returns the same result asget_used_cells().
A cell is considered empty if its source identifier equals-1, its atlas coordinate identifier isVector2(-1,-1)and its alternative identifier is-1.
Rect2iget_used_rect()const🔗
Returns a rectangle enclosing the used (non-empty) tiles of the map.
boolhas_body_rid(body:RID)const🔗
Returns whether the providedbodyRIDbelongs to one of thisTileMapLayer's cells.
boolis_cell_flipped_h(coords:Vector2i)const🔗
Returnstrueif the cell at coordinatescoordsis flipped horizontally. The result is valid only for atlas sources.
boolis_cell_flipped_v(coords:Vector2i)const🔗
Returnstrueif the cell at coordinatescoordsis flipped vertically. The result is valid only for atlas sources.
boolis_cell_transposed(coords:Vector2i)const🔗
Returnstrueif the cell at coordinatescoordsis transposed. The result is valid only for atlas sources.
Vector2ilocal_to_map(local_position:Vector2)const🔗
Returns the map coordinates of the cell containing the givenlocal_position. Iflocal_positionis in global coordinates, consider usingNode2D.to_local()before passing it to this method. See alsomap_to_local().
Vector2imap_pattern(position_in_tilemap:Vector2i, coords_in_pattern:Vector2i, pattern:TileMapPattern)🔗
Returns for the given coordinatescoords_in_patternin aTileMapPatternthe corresponding cell coordinates if the pattern was pasted at theposition_in_tilemapcoordinates (seeset_pattern()). This mapping is required as in half-offset tile shapes, the mapping might not work by calculatingposition_in_tile_map+coords_in_pattern.
Vector2map_to_local(map_position:Vector2i)const🔗
Returns the centered position of a cell in theTileMapLayer's local coordinate space. To convert the returned value into global coordinates, useNode2D.to_global(). See alsolocal_to_map().
Note:This may not correspond to the visual position of the tile, i.e. it ignores theTileData.texture_originproperty of individual tiles.
voidnotify_runtime_tile_data_update()🔗
Notifies theTileMapLayernode that calls to_use_tile_data_runtime_update()or_tile_data_runtime_update()will lead to different results. This will thus trigger aTileMapLayerupdate.
Warning:Updating theTileMapLayeris computationally expensive and may impact performance. Try to limit the number of calls to this function to avoid unnecessary update.
Note:This does not trigger a direct update of theTileMapLayer, the update will be done at the end of the frame as usual (unless you callupdate_internals()).
voidset_cell(coords:Vector2i, source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= 0)🔗
Sets the tile identifiers for the cell at coordinatescoords. Each tile of theTileSetis identified using three parts:
- The source identifiersource_ididentifies aTileSetSourceidentifier. SeeTileSet.set_source_id(),
The source identifiersource_ididentifies aTileSetSourceidentifier. SeeTileSet.set_source_id(),
- The atlas coordinate identifieratlas_coordsidentifies a tile coordinates in the atlas (if the source is aTileSetAtlasSource). ForTileSetScenesCollectionSourceit should always beVector2i(0,0),
The atlas coordinate identifieratlas_coordsidentifies a tile coordinates in the atlas (if the source is aTileSetAtlasSource). ForTileSetScenesCollectionSourceit should always beVector2i(0,0),
- The alternative tile identifieralternative_tileidentifies a tile alternative in the atlas (if the source is aTileSetAtlasSource), and the scene for aTileSetScenesCollectionSource.
The alternative tile identifieralternative_tileidentifies a tile alternative in the atlas (if the source is aTileSetAtlasSource), and the scene for aTileSetScenesCollectionSource.
Ifsource_idis set to-1,atlas_coordstoVector2i(-1,-1), oralternative_tileto-1, the cell will be erased. An erased cell getsallits identifiers automatically set to their respective invalid values, namely-1,Vector2i(-1,-1)and-1.
voidset_cells_terrain_connect(cells:Array[Vector2i], terrain_set:int, terrain:int, ignore_empty_terrains:bool= true)🔗
Update all the cells in thecellscoordinates array so that they use the giventerrainfor the giventerrain_set. If an updated cell has the same terrain as one of its neighboring cells, this function tries to join the two. This function might update neighboring tiles if needed to create correct terrain transitions.
Ifignore_empty_terrainsistrue, empty terrains will be ignored when trying to find the best fitting tile for the given terrain constraints.
Note:To work correctly, this method requires theTileMapLayer's TileSet to have terrains set up with all required terrain combinations. Otherwise, it may produce unexpected results.
voidset_cells_terrain_path(path:Array[Vector2i], terrain_set:int, terrain:int, ignore_empty_terrains:bool= true)🔗
Update all the cells in thepathcoordinates array so that they use the giventerrainfor the giventerrain_set. The function will also connect two successive cell in the path with the same terrain. This function might update neighboring tiles if needed to create correct terrain transitions.
Ifignore_empty_terrainsistrue, empty terrains will be ignored when trying to find the best fitting tile for the given terrain constraints.
Note:To work correctly, this method requires theTileMapLayer's TileSet to have terrains set up with all required terrain combinations. Otherwise, it may produce unexpected results.
voidset_navigation_map(map:RID)🔗
Sets a custommapas aNavigationServer2Dnavigation map. If not set, uses the defaultWorld2Dnavigation map instead.
voidset_pattern(position:Vector2i, pattern:TileMapPattern)🔗
Pastes theTileMapPatternat the givenpositionin the tile map. See alsoget_pattern().
voidupdate_internals()🔗
Triggers a direct update of theTileMapLayer. Usually, calling this function is not needed, asTileMapLayernode updates automatically when one of its properties or cells is modified.
However, for performance reasons, those updates are batched and delayed to the end of the frame. Calling this function will force theTileMapLayerto update right away instead.
Warning:Updating theTileMapLayeris computationally expensive and may impact performance. Try to limit the number of updates and how many tiles they impact.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.