# TileMapPattern in English

# TileMapPattern
Inherits:Resource<RefCounted<Object
Holds a pattern to be copied from or pasted intoTileMaps.

## Description
This resource holds a set of cells to help bulk manipulations ofTileMap.
A pattern always starts at the(0,0)coordinates and cannot have cells with negative coordinates.

## Methods

| int | get_cell_alternative_tile(coords:Vector2i)const |
|---|---|
| Vector2i | get_cell_atlas_coords(coords:Vector2i)const |
| int | get_cell_source_id(coords:Vector2i)const |
| Vector2i | get_size()const |
| Array[Vector2i] | get_used_cells()const |
| bool | has_cell(coords:Vector2i)const |
| bool | is_empty()const |
| void | remove_cell(coords:Vector2i, update_size:bool) |
| void | set_cell(coords:Vector2i, source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= -1) |
| void | set_size(size:Vector2i) |

get_cell_alternative_tile(coords:Vector2i)const
Vector2i
get_cell_atlas_coords(coords:Vector2i)const
get_cell_source_id(coords:Vector2i)const
Vector2i
get_size()const
Array[Vector2i]
get_used_cells()const
bool
has_cell(coords:Vector2i)const
bool
is_empty()const
void
remove_cell(coords:Vector2i, update_size:bool)
void
set_cell(coords:Vector2i, source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= -1)
void
set_size(size:Vector2i)

## Method Descriptions
intget_cell_alternative_tile(coords:Vector2i)const🔗
Returns the tile alternative ID of the cell atcoords.
Vector2iget_cell_atlas_coords(coords:Vector2i)const🔗
Returns the tile atlas coordinates ID of the cell atcoords.
intget_cell_source_id(coords:Vector2i)const🔗
Returns the tile source ID of the cell atcoords.
Vector2iget_size()const🔗
Returns the size, in cells, of the pattern.
Array[Vector2i]get_used_cells()const🔗
Returns the list of used cell coordinates in the pattern.
boolhas_cell(coords:Vector2i)const🔗
Returns whether the pattern has a tile at the given coordinates.
boolis_empty()const🔗
Returns whether the pattern is empty or not.
voidremove_cell(coords:Vector2i, update_size:bool)🔗
Remove the cell at the given coordinates.
voidset_cell(coords:Vector2i, source_id:int= -1, atlas_coords:Vector2i= Vector2i(-1, -1), alternative_tile:int= -1)🔗
Sets the tile identifiers for the cell at coordinatescoords. SeeTileMap.set_cell().
voidset_size(size:Vector2i)🔗
Sets the size of the pattern.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.