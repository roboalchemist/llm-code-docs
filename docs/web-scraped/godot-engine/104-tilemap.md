# TileMap

# TileMap

Deprecated:Use multipleTileMapLayernodes instead. To convert a TileMap to a set of TileMapLayer nodes, open the TileMap bottom panel with the node selected, click the toolbox icon in the top-right corner and choose 'Extract TileMap layers as individual TileMapLayer nodes'.
Inherits:Node2D<CanvasItem<Node<Object
Node for 2D tile-based maps.

## Description

Node for 2D tile-based maps. Tilemaps use aTileSetwhich contain a list of tiles which are used to create grid-based maps. A TileMap may have several layers, layouting tiles on top of each other.
For performance reasons, all TileMap updates are batched at the end of a frame. Notably, this means that scene tiles from aTileSetScenesCollectionSourcemay be initialized after their parent. This is only queued when inside the scene tree.
To force an update earlier on, callupdate_internals().
Note:For performance and compatibility reasons, the coordinates serialized byTileMapare limited to 16-bit signed integers, i.e. the range for X and Y coordinates is from-32768to32767. When saving tile data, tiles outside this range are wrapped.

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

| bool | collision_animatable | false |
|---|---|---|
| VisibilityMode | collision_visibility_mode | 0 |
| VisibilityMode | navigation_visibility_mode | 0 |
| int | rendering_quadrant_size | 16 |
| TileSet | tile_set |  |

bool
collision_animatable
false
VisibilityMode
collision_visibility_mode
VisibilityMode
navigation_visibility_mode
rendering_quadrant_size
TileSet
tile_set

## Methods

| void | _tile_data_runtime_update(layer:int, coords:Vector2i, tile_data:TileData)virtual |
|---|---|
| bool | _use_tile_data_runtime_update(layer:int, coords:Vector2i)virtual |
| void | add_layer(to_position:int) |
| void | clear() |
| void | clear_layer(layer:int) |
| void | erase_cell(layer:int, coords:Vector2i) |
| void | fix_invalid_tiles() |
| void | force_update(layer:int= -1) |
| int | get_cell_alternative_tile(layer:int, coords:Vector2i, use_proxies:bool= false)const |
| Vector2i | get_cell_atlas_coords(layer:int, coords:Vector2i, use_proxies:bool= false)const |
| int | get_cell_source_id(layer:int, coords:Vector2i, use_proxies:bool= false)const |
| TileData | get_cell_tile_data(layer:int, coords:Vector2i, use_proxies:bool= false)const |
| Vector2i | get_coords_for_body_rid(body:RID) |
| int | get_layer_for_body_rid(body:RID) |
| Color | get_layer_modulate(layer:int)const |
| String | get_layer_name(layer:int)const |
| RID | get_layer_navigation_map(layer:int)const |
| int | get_layer_y_sort_origin(layer:int)const |
| int | get_layer_z_index(layer:int)const |
| int | get_layers_count()const |
| RID | get_navigation_map(layer:int)const |
| Vector2i | get_neighbor_cell(coords:Vector2i, neighbor:CellNeighbor)const |
| TileMapPattern | get_pattern(layer:int, coords_array:Array[Vector2i]) |
| Array[Vector2i] | get_surrounding_cells(coords:Vector2i) |
| Array[Vector2i] | get_used_cells(layer:int)const |
| Array[Vector2i] | get_used_cells_by_id(layer:int, source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= -1)const |
| Rect2i | get_used_rect()const |
| bool | is_cell_flipped_h(layer:int, coords:Vector2i, use_proxies:bool= false)const |
| bool | is_cell_flipped_v(layer:int, coords:Vector2i, use_proxies:bool= false)const |
| bool | is_cell_transposed(layer:int, coords:Vector2i, use_proxies:bool= false)const |
| bool | is_layer_enabled(layer:int)const |
| bool | is_layer_navigation_enabled(layer:int)const |
| bool | is_layer_y_sort_enabled(layer:int)const |
| Vector2i | local_to_map(local_position:Vector2)const |
| Vector2i | map_pattern(position_in_tilemap:Vector2i, coords_in_pattern:Vector2i, pattern:TileMapPattern) |
| Vector2 | map_to_local(map_position:Vector2i)const |
| void | move_layer(layer:int, to_position:int) |
| void | notify_runtime_tile_data_update(layer:int= -1) |
| void | remove_layer(layer:int) |
| void | set_cell(layer:int, coords:Vector2i, source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= 0) |
| void | set_cells_terrain_connect(layer:int, cells:Array[Vector2i], terrain_set:int, terrain:int, ignore_empty_terrains:bool= true) |
| void | set_cells_terrain_path(layer:int, path:Array[Vector2i], terrain_set:int, terrain:int, ignore_empty_terrains:bool= true) |
| void | set_layer_enabled(layer:int, enabled:bool) |
| void | set_layer_modulate(layer:int, modulate:Color) |
| void | set_layer_name(layer:int, name:String) |
| void | set_layer_navigation_enabled(layer:int, enabled:bool) |
| void | set_layer_navigation_map(layer:int, map:RID) |
| void | set_layer_y_sort_enabled(layer:int, y_sort_enabled:bool) |
| void | set_layer_y_sort_origin(layer:int, y_sort_origin:int) |
| void | set_layer_z_index(layer:int, z_index:int) |
| void | set_navigation_map(layer:int, map:RID) |
| void | set_pattern(layer:int, position:Vector2i, pattern:TileMapPattern) |
| void | update_internals() |

void
_tile_data_runtime_update(layer:int, coords:Vector2i, tile_data:TileData)virtual
bool
_use_tile_data_runtime_update(layer:int, coords:Vector2i)virtual
void
add_layer(to_position:int)
void
clear()
void
clear_layer(layer:int)
void
erase_cell(layer:int, coords:Vector2i)
void
fix_invalid_tiles()
void
force_update(layer:int= -1)
get_cell_alternative_tile(layer:int, coords:Vector2i, use_proxies:bool= false)const
Vector2i
get_cell_atlas_coords(layer:int, coords:Vector2i, use_proxies:bool= false)const
get_cell_source_id(layer:int, coords:Vector2i, use_proxies:bool= false)const
TileData
get_cell_tile_data(layer:int, coords:Vector2i, use_proxies:bool= false)const
Vector2i
get_coords_for_body_rid(body:RID)
get_layer_for_body_rid(body:RID)
Color
get_layer_modulate(layer:int)const
String
get_layer_name(layer:int)const
get_layer_navigation_map(layer:int)const
get_layer_y_sort_origin(layer:int)const
get_layer_z_index(layer:int)const
get_layers_count()const
get_navigation_map(layer:int)const
Vector2i
get_neighbor_cell(coords:Vector2i, neighbor:CellNeighbor)const
TileMapPattern
get_pattern(layer:int, coords_array:Array[Vector2i])
Array[Vector2i]
get_surrounding_cells(coords:Vector2i)
Array[Vector2i]
get_used_cells(layer:int)const
Array[Vector2i]
get_used_cells_by_id(layer:int, source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= -1)const
Rect2i
get_used_rect()const
bool
is_cell_flipped_h(layer:int, coords:Vector2i, use_proxies:bool= false)const
bool
is_cell_flipped_v(layer:int, coords:Vector2i, use_proxies:bool= false)const
bool
is_cell_transposed(layer:int, coords:Vector2i, use_proxies:bool= false)const
bool
is_layer_enabled(layer:int)const
bool
is_layer_navigation_enabled(layer:int)const
bool
is_layer_y_sort_enabled(layer:int)const
Vector2i
local_to_map(local_position:Vector2)const
Vector2i
map_pattern(position_in_tilemap:Vector2i, coords_in_pattern:Vector2i, pattern:TileMapPattern)
Vector2
map_to_local(map_position:Vector2i)const
void
move_layer(layer:int, to_position:int)
void
notify_runtime_tile_data_update(layer:int= -1)
void
remove_layer(layer:int)
void
set_cell(layer:int, coords:Vector2i, source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= 0)
void
set_cells_terrain_connect(layer:int, cells:Array[Vector2i], terrain_set:int, terrain:int, ignore_empty_terrains:bool= true)
void
set_cells_terrain_path(layer:int, path:Array[Vector2i], terrain_set:int, terrain:int, ignore_empty_terrains:bool= true)
void
set_layer_enabled(layer:int, enabled:bool)
void
set_layer_modulate(layer:int, modulate:Color)
void
set_layer_name(layer:int, name:String)
void
set_layer_navigation_enabled(layer:int, enabled:bool)
void
set_layer_navigation_map(layer:int, map:RID)
void
set_layer_y_sort_enabled(layer:int, y_sort_enabled:bool)
void
set_layer_y_sort_origin(layer:int, y_sort_origin:int)
void
set_layer_z_index(layer:int, z_index:int)
void
set_navigation_map(layer:int, map:RID)
void
set_pattern(layer:int, position:Vector2i, pattern:TileMapPattern)
void
update_internals()

## Signals

changed()🔗
Emitted when theTileSetof this TileMap changes.

## Enumerations

enumVisibilityMode:🔗
VisibilityModeVISIBILITY_MODE_DEFAULT=0
Use the debug settings to determine visibility.
VisibilityModeVISIBILITY_MODE_FORCE_HIDE=2
Always hide.
VisibilityModeVISIBILITY_MODE_FORCE_SHOW=1
Always show.

## Property Descriptions

boolcollision_animatable=false🔗

- voidset_collision_animatable(value:bool)
voidset_collision_animatable(value:bool)
- boolis_collision_animatable()
boolis_collision_animatable()
If enabled, the TileMap will see its collisions synced to the physics tick and change its collision type from static to kinematic. This is required to create TileMap-based moving platform.
Note:Enablingcollision_animatablemay have a small performance impact, only do it if the TileMap is moving and has colliding tiles.
VisibilityModecollision_visibility_mode=0🔗
- voidset_collision_visibility_mode(value:VisibilityMode)
voidset_collision_visibility_mode(value:VisibilityMode)
- VisibilityModeget_collision_visibility_mode()
VisibilityModeget_collision_visibility_mode()
Show or hide the TileMap's collision shapes. If set toVISIBILITY_MODE_DEFAULT, this depends on the show collision debug settings.
VisibilityModenavigation_visibility_mode=0🔗
- voidset_navigation_visibility_mode(value:VisibilityMode)
voidset_navigation_visibility_mode(value:VisibilityMode)
- VisibilityModeget_navigation_visibility_mode()
VisibilityModeget_navigation_visibility_mode()
Show or hide the TileMap's navigation meshes. If set toVISIBILITY_MODE_DEFAULT, this depends on the show navigation debug settings.
intrendering_quadrant_size=16🔗
- voidset_rendering_quadrant_size(value:int)
voidset_rendering_quadrant_size(value:int)
- intget_rendering_quadrant_size()
intget_rendering_quadrant_size()
The TileMap's quadrant size. A quadrant is a group of tiles to be drawn together on a single canvas item, for optimization purposes.rendering_quadrant_sizedefines the length of a square's side, in the map's coordinate system, that forms the quadrant. Thus, the default quadrant size groups together16*16=256tiles.
The quadrant size does not apply on Y-sorted layers, as tiles are grouped by Y position instead in that case.
Note:As quadrants are created according to the map's coordinate system, the quadrant's "square shape" might not look like square in the TileMap's local coordinate system.
TileSettile_set🔗
- voidset_tileset(value:TileSet)
voidset_tileset(value:TileSet)
- TileSetget_tileset()
TileSetget_tileset()
TheTileSetused by thisTileMap. The textures, collisions, and additional behavior of all available tiles are stored here.

## Method Descriptions

void_tile_data_runtime_update(layer:int, coords:Vector2i, tile_data:TileData)virtual🔗
Called with a TileData object about to be used internally by the TileMap, allowing its modification at runtime.
This method is only called if_use_tile_data_runtime_update()is implemented and returnstruefor the given tilecoordsandlayer.
Warning:Thetile_dataobject's sub-resources are the same as the one in the TileSet. Modifying them might impact the whole TileSet. Instead, make sure to duplicate those resources.
Note:If the properties oftile_dataobject should change over time, usenotify_runtime_tile_data_update()to notify the TileMap it needs an update.
bool_use_tile_data_runtime_update(layer:int, coords:Vector2i)virtual🔗
Should returntrueif the tile at coordinatescoordson layerlayerrequires a runtime update.
Warning:Make sure this function only returntruewhen needed. Any tile processed at runtime without a need for it will imply a significant performance penalty.
Note:If the result of this function should changed, usenotify_runtime_tile_data_update()to notify the TileMap it needs an update.
voidadd_layer(to_position:int)🔗
Adds a layer at the given positionto_positionin the array. Ifto_positionis negative, the position is counted from the end, with-1adding the layer at the end of the array.
voidclear()🔗
Clears all cells.
voidclear_layer(layer:int)🔗
Clears all cells on the given layer.
Iflayeris negative, the layers are accessed from the last one.
voiderase_cell(layer:int, coords:Vector2i)🔗
Erases the cell on layerlayerat coordinatescoords.
Iflayeris negative, the layers are accessed from the last one.
voidfix_invalid_tiles()🔗
Clears cells that do not exist in the tileset.
voidforce_update(layer:int= -1)🔗
Deprecated:Usenotify_runtime_tile_data_update()and/orupdate_internals()instead.
Forces the TileMap and the layerlayerto update.
intget_cell_alternative_tile(layer:int, coords:Vector2i, use_proxies:bool= false)const🔗
Returns the tile alternative ID of the cell on layerlayeratcoords.
Ifuse_proxiesisfalse, ignores theTileSet's tile proxies, returning the raw alternative identifier. SeeTileSet.map_tile_proxy().
Iflayeris negative, the layers are accessed from the last one.
Vector2iget_cell_atlas_coords(layer:int, coords:Vector2i, use_proxies:bool= false)const🔗
Returns the tile atlas coordinates ID of the cell on layerlayerat coordinatescoords. ReturnsVector2i(-1,-1)if the cell does not exist.
Ifuse_proxiesisfalse, ignores theTileSet's tile proxies, returning the raw atlas coordinate identifier. SeeTileSet.map_tile_proxy().
Iflayeris negative, the layers are accessed from the last one.
intget_cell_source_id(layer:int, coords:Vector2i, use_proxies:bool= false)const🔗
Returns the tile source ID of the cell on layerlayerat coordinatescoords. Returns-1if the cell does not exist.
Ifuse_proxiesisfalse, ignores theTileSet's tile proxies, returning the raw source identifier. SeeTileSet.map_tile_proxy().
Iflayeris negative, the layers are accessed from the last one.
TileDataget_cell_tile_data(layer:int, coords:Vector2i, use_proxies:bool= false)const🔗
Returns theTileDataobject associated with the given cell, ornullif the cell does not exist or is not aTileSetAtlasSource.
Iflayeris negative, the layers are accessed from the last one.

```
func get_clicked_tile_power():
    var clicked_cell = tile_map.local_to_map(tile_map.get_local_mouse_position())
    var data = tile_map.get_cell_tile_data(0, clicked_cell)
    if data:
        return data.get_custom_data("power")
    else:
        return 0
```

Ifuse_proxiesisfalse, ignores theTileSet's tile proxies. SeeTileSet.map_tile_proxy().
Vector2iget_coords_for_body_rid(body:RID)🔗
Returns the coordinates of the tile for given physics body RID. Such RID can be retrieved fromKinematicCollision2D.get_collider_rid(), when colliding with a tile.
intget_layer_for_body_rid(body:RID)🔗
Returns the tilemap layer of the tile for given physics body RID. Such RID can be retrieved fromKinematicCollision2D.get_collider_rid(), when colliding with a tile.
Colorget_layer_modulate(layer:int)const🔗
Returns a TileMap layer's modulate.
Iflayeris negative, the layers are accessed from the last one.
Stringget_layer_name(layer:int)const🔗
Returns a TileMap layer's name.
Iflayeris negative, the layers are accessed from the last one.
RIDget_layer_navigation_map(layer:int)const🔗
Returns theRIDof theNavigationServer2Dnavigation map assigned to the specified TileMap layerlayer.
By default the TileMap uses the defaultWorld2Dnavigation map for the first TileMap layer. For each additional TileMap layer a new navigation map is created for the additional layer.
In order to makeNavigationAgent2Dswitch between TileMap layer navigation maps useNavigationAgent2D.set_navigation_map()with the navigation map received fromget_layer_navigation_map().
Iflayeris negative, the layers are accessed from the last one.
intget_layer_y_sort_origin(layer:int)const🔗
Returns a TileMap layer's Y sort origin.
Iflayeris negative, the layers are accessed from the last one.
intget_layer_z_index(layer:int)const🔗
Returns a TileMap layer's Z-index value.
Iflayeris negative, the layers are accessed from the last one.
intget_layers_count()const🔗
Returns the number of layers in the TileMap.
RIDget_navigation_map(layer:int)const🔗
Deprecated:Useget_layer_navigation_map()instead.
Returns theRIDof theNavigationServer2Dnavigation map assigned to the specified TileMap layerlayer.
Vector2iget_neighbor_cell(coords:Vector2i, neighbor:CellNeighbor)const🔗
Returns the neighboring cell to the one at coordinatescoords, identified by theneighbordirection. This method takes into account the different layouts a TileMap can take.
TileMapPatternget_pattern(layer:int, coords_array:Array[Vector2i])🔗
Creates a newTileMapPatternfrom the given layer and set of cells.
Iflayeris negative, the layers are accessed from the last one.
Array[Vector2i]get_surrounding_cells(coords:Vector2i)🔗
Returns the list of all neighbourings cells to the one atcoords.
Array[Vector2i]get_used_cells(layer:int)const🔗
Returns aVector2iarray with the positions of all cells containing a tile in the given layer. A cell is considered empty if its source identifier equals -1, its atlas coordinates identifiers isVector2(-1,-1)and its alternative identifier is -1.
Iflayeris negative, the layers are accessed from the last one.
Array[Vector2i]get_used_cells_by_id(layer:int, source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= -1)const🔗
Returns aVector2iarray with the positions of all cells containing a tile in the given layer. Tiles may be filtered according to their source (source_id), their atlas coordinates (atlas_coords) or alternative id (alternative_tile).
If a parameter has its value set to the default one, this parameter is not used to filter a cell. Thus, if all parameters have their respective default value, this method returns the same result asget_used_cells().
A cell is considered empty if its source identifier equals -1, its atlas coordinates identifiers isVector2(-1,-1)and its alternative identifier is -1.
Iflayeris negative, the layers are accessed from the last one.
Rect2iget_used_rect()const🔗
Returns a rectangle enclosing the used (non-empty) tiles of the map, including all layers.
boolis_cell_flipped_h(layer:int, coords:Vector2i, use_proxies:bool= false)const🔗
Returnstrueif the cell on layerlayerat coordinatescoordsis flipped horizontally. The result is valid only for atlas sources.
boolis_cell_flipped_v(layer:int, coords:Vector2i, use_proxies:bool= false)const🔗
Returnstrueif the cell on layerlayerat coordinatescoordsis flipped vertically. The result is valid only for atlas sources.
boolis_cell_transposed(layer:int, coords:Vector2i, use_proxies:bool= false)const🔗
Returnstrueif the cell on layerlayerat coordinatescoordsis transposed. The result is valid only for atlas sources.
boolis_layer_enabled(layer:int)const🔗
Returns if a layer is enabled.
Iflayeris negative, the layers are accessed from the last one.
boolis_layer_navigation_enabled(layer:int)const🔗
Returns if a layer's built-in navigation regions generation is enabled.
boolis_layer_y_sort_enabled(layer:int)const🔗
Returns if a layer Y-sorts its tiles.
Iflayeris negative, the layers are accessed from the last one.
Vector2ilocal_to_map(local_position:Vector2)const🔗
Returns the map coordinates of the cell containing the givenlocal_position. Iflocal_positionis in global coordinates, consider usingNode2D.to_local()before passing it to this method. See alsomap_to_local().
Vector2imap_pattern(position_in_tilemap:Vector2i, coords_in_pattern:Vector2i, pattern:TileMapPattern)🔗
Returns for the given coordinatecoords_in_patternin aTileMapPatternthe corresponding cell coordinates if the pattern was pasted at theposition_in_tilemapcoordinates (seeset_pattern()). This mapping is required as in half-offset tile shapes, the mapping might not work by calculatingposition_in_tile_map+coords_in_pattern.
Vector2map_to_local(map_position:Vector2i)const🔗
Returns the centered position of a cell in the TileMap's local coordinate space. To convert the returned value into global coordinates, useNode2D.to_global(). See alsolocal_to_map().
Note:This may not correspond to the visual position of the tile, i.e. it ignores theTileData.texture_originproperty of individual tiles.
voidmove_layer(layer:int, to_position:int)🔗
Moves the layer at indexlayerto the given positionto_positionin the array.
voidnotify_runtime_tile_data_update(layer:int= -1)🔗
Notifies the TileMap node that calls to_use_tile_data_runtime_update()or_tile_data_runtime_update()will lead to different results. This will thus trigger a TileMap update.
Iflayeris provided, only notifies changes for the given layer. Providing thelayerargument (when applicable) is usually preferred for performance reasons.
Warning:Updating the TileMap is computationally expensive and may impact performance. Try to limit the number of calls to this function to avoid unnecessary update.
Note:This does not trigger a direct update of the TileMap, the update will be done at the end of the frame as usual (unless you callupdate_internals()).
voidremove_layer(layer:int)🔗
Removes the layer at indexlayer.
voidset_cell(layer:int, coords:Vector2i, source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= 0)🔗
Sets the tile identifiers for the cell on layerlayerat coordinatescoords. Each tile of theTileSetis identified using three parts:

- The source identifiersource_ididentifies aTileSetSourceidentifier. SeeTileSet.set_source_id(),
The source identifiersource_ididentifies aTileSetSourceidentifier. SeeTileSet.set_source_id(),
- The atlas coordinates identifieratlas_coordsidentifies a tile coordinates in the atlas (if the source is aTileSetAtlasSource). ForTileSetScenesCollectionSourceit should always beVector2i(0,0)),
The atlas coordinates identifieratlas_coordsidentifies a tile coordinates in the atlas (if the source is aTileSetAtlasSource). ForTileSetScenesCollectionSourceit should always beVector2i(0,0)),
- The alternative tile identifieralternative_tileidentifies a tile alternative in the atlas (if the source is aTileSetAtlasSource), and the scene for aTileSetScenesCollectionSource.
The alternative tile identifieralternative_tileidentifies a tile alternative in the atlas (if the source is aTileSetAtlasSource), and the scene for aTileSetScenesCollectionSource.
Ifsource_idis set to-1,atlas_coordstoVector2i(-1,-1)oralternative_tileto-1, the cell will be erased. An erased cell getsallits identifiers automatically set to their respective invalid values, namely-1,Vector2i(-1,-1)and-1.
Iflayeris negative, the layers are accessed from the last one.
voidset_cells_terrain_connect(layer:int, cells:Array[Vector2i], terrain_set:int, terrain:int, ignore_empty_terrains:bool= true)🔗
Update all the cells in thecellscoordinates array so that they use the giventerrainfor the giventerrain_set. If an updated cell has the same terrain as one of its neighboring cells, this function tries to join the two. This function might update neighboring tiles if needed to create correct terrain transitions.
Ifignore_empty_terrainsistrue, empty terrains will be ignored when trying to find the best fitting tile for the given terrain constraints.
Iflayeris negative, the layers are accessed from the last one.
Note:To work correctly, this method requires the TileMap's TileSet to have terrains set up with all required terrain combinations. Otherwise, it may produce unexpected results.
voidset_cells_terrain_path(layer:int, path:Array[Vector2i], terrain_set:int, terrain:int, ignore_empty_terrains:bool= true)🔗
Update all the cells in thepathcoordinates array so that they use the giventerrainfor the giventerrain_set. The function will also connect two successive cell in the path with the same terrain. This function might update neighboring tiles if needed to create correct terrain transitions.
Ifignore_empty_terrainsistrue, empty terrains will be ignored when trying to find the best fitting tile for the given terrain constraints.
Iflayeris negative, the layers are accessed from the last one.
Note:To work correctly, this method requires the TileMap's TileSet to have terrains set up with all required terrain combinations. Otherwise, it may produce unexpected results.
voidset_layer_enabled(layer:int, enabled:bool)🔗
Enables or disables the layerlayer. A disabled layer is not processed at all (no rendering, no physics, etc.).
Iflayeris negative, the layers are accessed from the last one.
voidset_layer_modulate(layer:int, modulate:Color)🔗
Sets a layer's color. It will be multiplied by tile's color and TileMap's modulate.
Iflayeris negative, the layers are accessed from the last one.
voidset_layer_name(layer:int, name:String)🔗
Sets a layer's name. This is mostly useful in the editor.
Iflayeris negative, the layers are accessed from the last one.
voidset_layer_navigation_enabled(layer:int, enabled:bool)🔗
Enables or disables a layer's built-in navigation regions generation. Disable this if you need to bake navigation regions from a TileMap using aNavigationRegion2Dnode.
voidset_layer_navigation_map(layer:int, map:RID)🔗
Assignsmapas aNavigationServer2Dnavigation map for the specified TileMap layerlayer.
By default the TileMap uses the defaultWorld2Dnavigation map for the first TileMap layer. For each additional TileMap layer a new navigation map is created for the additional layer.
In order to makeNavigationAgent2Dswitch between TileMap layer navigation maps useNavigationAgent2D.set_navigation_map()with the navigation map received fromget_layer_navigation_map().
Iflayeris negative, the layers are accessed from the last one.
voidset_layer_y_sort_enabled(layer:int, y_sort_enabled:bool)🔗
Enables or disables a layer's Y-sorting. If a layer is Y-sorted, the layer will behave as a CanvasItem node where each of its tile gets Y-sorted.
Y-sorted layers should usually be on different Z-index values than not Y-sorted layers, otherwise, each of those layer will be Y-sorted as whole with the Y-sorted one. This is usually an undesired behavior.
Iflayeris negative, the layers are accessed from the last one.
voidset_layer_y_sort_origin(layer:int, y_sort_origin:int)🔗
Sets a layer's Y-sort origin value. This Y-sort origin value is added to each tile's Y-sort origin value.
This allows, for example, to fake a different height level on each layer. This can be useful for top-down view games.
Iflayeris negative, the layers are accessed from the last one.
voidset_layer_z_index(layer:int, z_index:int)🔗
Sets a layers Z-index value. This Z-index is added to each tile's Z-index value.
Iflayeris negative, the layers are accessed from the last one.
voidset_navigation_map(layer:int, map:RID)🔗
Deprecated:Useset_layer_navigation_map()instead.
Assignsmapas aNavigationServer2Dnavigation map for the specified TileMap layerlayer.
voidset_pattern(layer:int, position:Vector2i, pattern:TileMapPattern)🔗
Paste the givenTileMapPatternat the givenpositionandlayerin the tile map.
Iflayeris negative, the layers are accessed from the last one.
voidupdate_internals()🔗
Triggers a direct update of the TileMap. Usually, calling this function is not needed, as TileMap node updates automatically when one of its properties or cells is modified.
However, for performance reasons, those updates are batched and delayed to the end of the frame. Calling this function will force the TileMap to update right away instead.
Warning:Updating the TileMap is computationally expensive and may impact performance. Try to limit the number of updates and how many tiles they impact.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
