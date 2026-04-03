# TileSetAtlasSource

# TileSetAtlasSource
Inherits:TileSetSource<Resource<RefCounted<Object
Exposes a 2D atlas texture as a set of tiles for aTileSetresource.

## Description
An atlas is a grid of tiles laid out on a texture. Each tile in the grid must be exposed usingcreate_tile(). Those tiles are then indexed using their coordinates in the grid.
Each tile can also have a size in the grid coordinates, making it more or less cells in the atlas.
Alternatives version of a tile can be created usingcreate_alternative_tile(), which are then indexed using an alternative ID. The main tile (the one in the grid), is accessed with an alternative ID equal to 0.
Each tile alternate has a set of properties that is defined by the source'sTileSetlayers. Those properties are stored in a TileData object that can be accessed and modified usingget_tile_data().
As TileData properties are stored directly in the TileSetAtlasSource resource, their properties might also be set usingTileSetAtlasSource.set("<coords_x>:<coords_y>/<alternative_id>/<tile_data_property>").

## Properties

| Vector2i | margins | Vector2i(0,0) |
|---|---|---|
| Vector2i | separation | Vector2i(0,0) |
| Texture2D | texture |  |
| Vector2i | texture_region_size | Vector2i(16,16) |
| bool | use_texture_padding | true |

Vector2i
margins
Vector2i(0,0)
Vector2i
separation
Vector2i(0,0)
Texture2D
texture
Vector2i
texture_region_size
Vector2i(16,16)
bool
use_texture_padding
true

## Methods

| void | clear_tiles_outside_texture() |
|---|---|
| int | create_alternative_tile(atlas_coords:Vector2i, alternative_id_override:int= -1) |
| void | create_tile(atlas_coords:Vector2i, size:Vector2i= Vector2i(1, 1)) |
| Vector2i | get_atlas_grid_size()const |
| int | get_next_alternative_tile_id(atlas_coords:Vector2i)const |
| Texture2D | get_runtime_texture()const |
| Rect2i | get_runtime_tile_texture_region(atlas_coords:Vector2i, frame:int)const |
| int | get_tile_animation_columns(atlas_coords:Vector2i)const |
| float | get_tile_animation_frame_duration(atlas_coords:Vector2i, frame_index:int)const |
| int | get_tile_animation_frames_count(atlas_coords:Vector2i)const |
| TileAnimationMode | get_tile_animation_mode(atlas_coords:Vector2i)const |
| Vector2i | get_tile_animation_separation(atlas_coords:Vector2i)const |
| float | get_tile_animation_speed(atlas_coords:Vector2i)const |
| float | get_tile_animation_total_duration(atlas_coords:Vector2i)const |
| Vector2i | get_tile_at_coords(atlas_coords:Vector2i)const |
| TileData | get_tile_data(atlas_coords:Vector2i, alternative_tile:int)const |
| Vector2i | get_tile_size_in_atlas(atlas_coords:Vector2i)const |
| Rect2i | get_tile_texture_region(atlas_coords:Vector2i, frame:int= 0)const |
| PackedVector2Array | get_tiles_to_be_removed_on_change(texture:Texture2D, margins:Vector2i, separation:Vector2i, texture_region_size:Vector2i) |
| bool | has_room_for_tile(atlas_coords:Vector2i, size:Vector2i, animation_columns:int, animation_separation:Vector2i, frames_count:int, ignored_tile:Vector2i= Vector2i(-1, -1))const |
| bool | has_tiles_outside_texture()const |
| void | move_tile_in_atlas(atlas_coords:Vector2i, new_atlas_coords:Vector2i= Vector2i(-1, -1), new_size:Vector2i= Vector2i(-1, -1)) |
| void | remove_alternative_tile(atlas_coords:Vector2i, alternative_tile:int) |
| void | remove_tile(atlas_coords:Vector2i) |
| void | set_alternative_tile_id(atlas_coords:Vector2i, alternative_tile:int, new_id:int) |
| void | set_tile_animation_columns(atlas_coords:Vector2i, frame_columns:int) |
| void | set_tile_animation_frame_duration(atlas_coords:Vector2i, frame_index:int, duration:float) |
| void | set_tile_animation_frames_count(atlas_coords:Vector2i, frames_count:int) |
| void | set_tile_animation_mode(atlas_coords:Vector2i, mode:TileAnimationMode) |
| void | set_tile_animation_separation(atlas_coords:Vector2i, separation:Vector2i) |
| void | set_tile_animation_speed(atlas_coords:Vector2i, speed:float) |

void
clear_tiles_outside_texture()
create_alternative_tile(atlas_coords:Vector2i, alternative_id_override:int= -1)
void
create_tile(atlas_coords:Vector2i, size:Vector2i= Vector2i(1, 1))
Vector2i
get_atlas_grid_size()const
get_next_alternative_tile_id(atlas_coords:Vector2i)const
Texture2D
get_runtime_texture()const
Rect2i
get_runtime_tile_texture_region(atlas_coords:Vector2i, frame:int)const
get_tile_animation_columns(atlas_coords:Vector2i)const
float
get_tile_animation_frame_duration(atlas_coords:Vector2i, frame_index:int)const
get_tile_animation_frames_count(atlas_coords:Vector2i)const
TileAnimationMode
get_tile_animation_mode(atlas_coords:Vector2i)const
Vector2i
get_tile_animation_separation(atlas_coords:Vector2i)const
float
get_tile_animation_speed(atlas_coords:Vector2i)const
float
get_tile_animation_total_duration(atlas_coords:Vector2i)const
Vector2i
get_tile_at_coords(atlas_coords:Vector2i)const
TileData
get_tile_data(atlas_coords:Vector2i, alternative_tile:int)const
Vector2i
get_tile_size_in_atlas(atlas_coords:Vector2i)const
Rect2i
get_tile_texture_region(atlas_coords:Vector2i, frame:int= 0)const
PackedVector2Array
get_tiles_to_be_removed_on_change(texture:Texture2D, margins:Vector2i, separation:Vector2i, texture_region_size:Vector2i)
bool
has_room_for_tile(atlas_coords:Vector2i, size:Vector2i, animation_columns:int, animation_separation:Vector2i, frames_count:int, ignored_tile:Vector2i= Vector2i(-1, -1))const
bool
has_tiles_outside_texture()const
void
move_tile_in_atlas(atlas_coords:Vector2i, new_atlas_coords:Vector2i= Vector2i(-1, -1), new_size:Vector2i= Vector2i(-1, -1))
void
remove_alternative_tile(atlas_coords:Vector2i, alternative_tile:int)
void
remove_tile(atlas_coords:Vector2i)
void
set_alternative_tile_id(atlas_coords:Vector2i, alternative_tile:int, new_id:int)
void
set_tile_animation_columns(atlas_coords:Vector2i, frame_columns:int)
void
set_tile_animation_frame_duration(atlas_coords:Vector2i, frame_index:int, duration:float)
void
set_tile_animation_frames_count(atlas_coords:Vector2i, frames_count:int)
void
set_tile_animation_mode(atlas_coords:Vector2i, mode:TileAnimationMode)
void
set_tile_animation_separation(atlas_coords:Vector2i, separation:Vector2i)
void
set_tile_animation_speed(atlas_coords:Vector2i, speed:float)

## Enumerations
enumTileAnimationMode:🔗
TileAnimationModeTILE_ANIMATION_MODE_DEFAULT=0
Tile animations start at same time, looking identical.
TileAnimationModeTILE_ANIMATION_MODE_RANDOM_START_TIMES=1
Tile animations start at random times, looking varied.
TileAnimationModeTILE_ANIMATION_MODE_MAX=2
Represents the size of theTileAnimationModeenum.

## Constants
TRANSFORM_FLIP_H=4096🔗
Represents cell's horizontal flip flag. Should be used directly withTileMapLayerto flip placed tiles by altering their alternative IDs.
```
var alternate_id = $TileMapLayer.get_cell_alternative_tile(Vector2i(2, 2))
if not alternate_id & TileSetAtlasSource.TRANSFORM_FLIP_H:
    # If tile is not already flipped, flip it.
    $TileMapLayer.set_cell(Vector2i(2, 2), source_id, atlas_coords, alternate_id | TileSetAtlasSource.TRANSFORM_FLIP_H)
```
Note:These transformations can be combined to do the equivalent of 0, 90, 180, and 270 degree rotations, as shown below:
```
enum TileTransform {
    ROTATE_0 = 0,
    ROTATE_90 = TileSetAtlasSource.TRANSFORM_TRANSPOSE | TileSetAtlasSource.TRANSFORM_FLIP_H,
    ROTATE_180 = TileSetAtlasSource.TRANSFORM_FLIP_H | TileSetAtlasSource.TRANSFORM_FLIP_V,
    ROTATE_270 = TileSetAtlasSource.TRANSFORM_TRANSPOSE | TileSetAtlasSource.TRANSFORM_FLIP_V,
}
```
TRANSFORM_FLIP_V=8192🔗
Represents cell's vertical flip flag. SeeTRANSFORM_FLIP_Hfor usage.
TRANSFORM_TRANSPOSE=16384🔗
Represents cell's transposed flag. SeeTRANSFORM_FLIP_Hfor usage.

## Property Descriptions
Vector2imargins=Vector2i(0,0)🔗
- voidset_margins(value:Vector2i)
voidset_margins(value:Vector2i)
- Vector2iget_margins()
Vector2iget_margins()
Margins, in pixels, to offset the origin of the grid in the texture.
Vector2iseparation=Vector2i(0,0)🔗
- voidset_separation(value:Vector2i)
voidset_separation(value:Vector2i)
- Vector2iget_separation()
Vector2iget_separation()
Separation, in pixels, between each tile texture region of the grid.
Texture2Dtexture🔗
- voidset_texture(value:Texture2D)
voidset_texture(value:Texture2D)
- Texture2Dget_texture()
Texture2Dget_texture()
The atlas texture.
Vector2itexture_region_size=Vector2i(16,16)🔗
- voidset_texture_region_size(value:Vector2i)
voidset_texture_region_size(value:Vector2i)
- Vector2iget_texture_region_size()
Vector2iget_texture_region_size()
The base tile size in the texture (in pixel). This size must be bigger than or equal to the TileSet'stile_sizevalue.
booluse_texture_padding=true🔗
- voidset_use_texture_padding(value:bool)
voidset_use_texture_padding(value:bool)
- boolget_use_texture_padding()
boolget_use_texture_padding()
Iftrue, generates an internal texture with an additional one pixel padding around each tile. Texture padding avoids a common artifact where lines appear between tiles.
Disabling this setting might lead a small performance improvement, as generating the internal texture requires both memory and processing time when the TileSetAtlasSource resource is modified.

## Method Descriptions
voidclear_tiles_outside_texture()🔗
Removes all tiles that don't fit the available texture area. This method iterates over all the source's tiles, so it's advised to usehas_tiles_outside_texture()beforehand.
intcreate_alternative_tile(atlas_coords:Vector2i, alternative_id_override:int= -1)🔗
Creates an alternative tile for the tile at coordinatesatlas_coords. Ifalternative_id_overrideis -1, give it an automatically generated unique ID, or assigns it the given ID otherwise.
Returns the new alternative identifier, or -1 if the alternative could not be created with a providedalternative_id_override.
voidcreate_tile(atlas_coords:Vector2i, size:Vector2i= Vector2i(1, 1))🔗
Creates a new tile at coordinatesatlas_coordswith the givensize.
Vector2iget_atlas_grid_size()const🔗
Returns the atlas grid size, which depends on how many tiles can fit in the texture. It thus depends on thetexture's size, the atlasmargins, and the tiles'texture_region_size.
intget_next_alternative_tile_id(atlas_coords:Vector2i)const🔗
Returns the alternative ID a following call tocreate_alternative_tile()would return.
Texture2Dget_runtime_texture()const🔗
Ifuse_texture_paddingisfalse, returnstexture. Otherwise, returns an internalImageTexturecreated that includes the padding.
Rect2iget_runtime_tile_texture_region(atlas_coords:Vector2i, frame:int)const🔗
Returns the region of the tile at coordinatesatlas_coordsfor the givenframeinside the texture returned byget_runtime_texture().
Note:Ifuse_texture_paddingisfalse, returns the same asget_tile_texture_region().
intget_tile_animation_columns(atlas_coords:Vector2i)const🔗
Returns how many columns the tile atatlas_coordshas in its animation layout.
floatget_tile_animation_frame_duration(atlas_coords:Vector2i, frame_index:int)const🔗
Returns the animation frame duration of frameframe_indexfor the tile at coordinatesatlas_coords.
intget_tile_animation_frames_count(atlas_coords:Vector2i)const🔗
Returns how many animation frames has the tile at coordinatesatlas_coords.
TileAnimationModeget_tile_animation_mode(atlas_coords:Vector2i)const🔗
Returns the tile animation mode of the tile atatlas_coords. See alsoset_tile_animation_mode().
Vector2iget_tile_animation_separation(atlas_coords:Vector2i)const🔗
Returns the separation (as in the atlas grid) between each frame of an animated tile at coordinatesatlas_coords.
floatget_tile_animation_speed(atlas_coords:Vector2i)const🔗
Returns the animation speed of the tile at coordinatesatlas_coords.
floatget_tile_animation_total_duration(atlas_coords:Vector2i)const🔗
Returns the sum of the sum of the frame durations of the tile at coordinatesatlas_coords. This value needs to be divided by the animation speed to get the actual animation loop duration.
Vector2iget_tile_at_coords(atlas_coords:Vector2i)const🔗
If there is a tile covering theatlas_coordscoordinates, returns the top-left coordinates of the tile (thus its coordinate ID). ReturnsVector2i(-1,-1)otherwise.
TileDataget_tile_data(atlas_coords:Vector2i, alternative_tile:int)const🔗
Returns theTileDataobject for the given atlas coordinates and alternative ID.
Vector2iget_tile_size_in_atlas(atlas_coords:Vector2i)const🔗
Returns the size of the tile (in the grid coordinates system) at coordinatesatlas_coords.
Rect2iget_tile_texture_region(atlas_coords:Vector2i, frame:int= 0)const🔗
Returns a tile's texture region in the atlas texture. For animated tiles, aframeargument might be provided for the different frames of the animation.
PackedVector2Arrayget_tiles_to_be_removed_on_change(texture:Texture2D, margins:Vector2i, separation:Vector2i, texture_region_size:Vector2i)🔗
Returns an array of tiles coordinates ID that will be automatically removed when modifying one or several of those properties:texture,margins,separationortexture_region_size. This can be used to undo changes that would have caused tiles data loss.
boolhas_room_for_tile(atlas_coords:Vector2i, size:Vector2i, animation_columns:int, animation_separation:Vector2i, frames_count:int, ignored_tile:Vector2i= Vector2i(-1, -1))const🔗
Returns whether there is enough room in an atlas to create/modify a tile with the given properties. Ifignored_tileis provided, act as is the given tile was not present in the atlas. This may be used when you want to modify a tile's properties.
boolhas_tiles_outside_texture()const🔗
Checks if the source has any tiles that don't fit the texture area (either partially or completely).
voidmove_tile_in_atlas(atlas_coords:Vector2i, new_atlas_coords:Vector2i= Vector2i(-1, -1), new_size:Vector2i= Vector2i(-1, -1))🔗
Move the tile and its alternatives at theatlas_coordscoordinates to thenew_atlas_coordscoordinates with thenew_sizesize. This functions will fail if a tile is already present in the given area.
Ifnew_atlas_coordsisVector2i(-1,-1), keeps the tile's coordinates. Ifnew_sizeisVector2i(-1,-1), keeps the tile's size.
To avoid an error, first check if a move is possible usinghas_room_for_tile().
voidremove_alternative_tile(atlas_coords:Vector2i, alternative_tile:int)🔗
Remove a tile's alternative with alternative IDalternative_tile.
Calling this function withalternative_tileequals to 0 will fail, as the base tile alternative cannot be removed.
voidremove_tile(atlas_coords:Vector2i)🔗
Remove a tile and its alternative at coordinatesatlas_coords.
voidset_alternative_tile_id(atlas_coords:Vector2i, alternative_tile:int, new_id:int)🔗
Change a tile's alternative ID fromalternative_tiletonew_id.
Calling this function withnew_idof 0 will fail, as the base tile alternative cannot be moved.
voidset_tile_animation_columns(atlas_coords:Vector2i, frame_columns:int)🔗
Sets the number of columns in the animation layout of the tile at coordinatesatlas_coords. If set to 0, then the different frames of the animation are laid out as a single horizontal line in the atlas.
voidset_tile_animation_frame_duration(atlas_coords:Vector2i, frame_index:int, duration:float)🔗
Sets the animation framedurationof frameframe_indexfor the tile at coordinatesatlas_coords.
voidset_tile_animation_frames_count(atlas_coords:Vector2i, frames_count:int)🔗
Sets how many animation frames the tile at coordinatesatlas_coordshas.
voidset_tile_animation_mode(atlas_coords:Vector2i, mode:TileAnimationMode)🔗
Sets the tile animation mode of the tile atatlas_coordstomode. See alsoget_tile_animation_mode().
voidset_tile_animation_separation(atlas_coords:Vector2i, separation:Vector2i)🔗
Sets the margin (in grid tiles) between each tile in the animation layout of the tile at coordinatesatlas_coordshas.
voidset_tile_animation_speed(atlas_coords:Vector2i, speed:float)🔗
Sets the animation speed of the tile at coordinatesatlas_coordshas.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.