:github_url: hide



# TileSetAtlasSource

**Inherits:** [TileSetSource<class_TileSetSource>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Exposes a 2D atlas texture as a set of tiles for a [TileSet<class_TileSet>] resource.


## Description

An atlas is a grid of tiles laid out on a texture. Each tile in the grid must be exposed using [create_tile()<class_TileSetAtlasSource_method_create_tile>]. Those tiles are then indexed using their coordinates in the grid.

Each tile can also have a size in the grid coordinates, making it more or less cells in the atlas.

Alternatives version of a tile can be created using [create_alternative_tile()<class_TileSetAtlasSource_method_create_alternative_tile>], which are then indexed using an alternative ID. The main tile (the one in the grid), is accessed with an alternative ID equal to 0.

Each tile alternate has a set of properties that is defined by the source's [TileSet<class_TileSet>] layers. Those properties are stored in a TileData object that can be accessed and modified using [get_tile_data()<class_TileSetAtlasSource_method_get_tile_data>].

As TileData properties are stored directly in the TileSetAtlasSource resource, their properties might also be set using `TileSetAtlasSource.set("<coords_x>:<coords_y>/<alternative_id>/<tile_data_property>")`.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+-----------------------------------------------------------------------------------+----------------------+
> | :ref:`Vector2i<class_Vector2i>`   | :ref:`margins<class_TileSetAtlasSource_property_margins>`                         | ``Vector2i(0, 0)``   |
> +-----------------------------------+-----------------------------------------------------------------------------------+----------------------+
> | :ref:`Vector2i<class_Vector2i>`   | :ref:`separation<class_TileSetAtlasSource_property_separation>`                   | ``Vector2i(0, 0)``   |
> +-----------------------------------+-----------------------------------------------------------------------------------+----------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`texture<class_TileSetAtlasSource_property_texture>`                         |                      |
> +-----------------------------------+-----------------------------------------------------------------------------------+----------------------+
> | :ref:`Vector2i<class_Vector2i>`   | :ref:`texture_region_size<class_TileSetAtlasSource_property_texture_region_size>` | ``Vector2i(16, 16)`` |
> +-----------------------------------+-----------------------------------------------------------------------------------+----------------------+
> | :ref:`bool<class_bool>`           | :ref:`use_texture_padding<class_TileSetAtlasSource_property_use_texture_padding>` | ``true``             |
> +-----------------------------------+-----------------------------------------------------------------------------------+----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`clear_tiles_outside_texture<class_TileSetAtlasSource_method_clear_tiles_outside_texture>`\ (\ )                                                                                                                                                                                                                                                                                         |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                               | :ref:`create_alternative_tile<class_TileSetAtlasSource_method_create_alternative_tile>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, alternative_id_override\: :ref:`int<class_int>` = -1\ )                                                                                                                                                                                           |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`create_tile<class_TileSetAtlasSource_method_create_tile>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, size\: :ref:`Vector2i<class_Vector2i>` = Vector2i(1, 1)\ )                                                                                                                                                                                                                |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>`                                     | :ref:`get_atlas_grid_size<class_TileSetAtlasSource_method_get_atlas_grid_size>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                 |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                               | :ref:`get_next_alternative_tile_id<class_TileSetAtlasSource_method_get_next_alternative_tile_id>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                                                                                                                                               |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>`                                   | :ref:`get_runtime_texture<class_TileSetAtlasSource_method_get_runtime_texture>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                 |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>`                                         | :ref:`get_runtime_tile_texture_region<class_TileSetAtlasSource_method_get_runtime_tile_texture_region>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, frame\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                          |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                               | :ref:`get_tile_animation_columns<class_TileSetAtlasSource_method_get_tile_animation_columns>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                                                                                                                                                   |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`get_tile_animation_frame_duration<class_TileSetAtlasSource_method_get_tile_animation_frame_duration>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, frame_index\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                               | :ref:`get_tile_animation_frames_count<class_TileSetAtlasSource_method_get_tile_animation_frames_count>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                                                                                                                                         |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>` | :ref:`get_tile_animation_mode<class_TileSetAtlasSource_method_get_tile_animation_mode>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                                                                                                                                                         |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>`                                     | :ref:`get_tile_animation_separation<class_TileSetAtlasSource_method_get_tile_animation_separation>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                                                                                                                                             |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`get_tile_animation_speed<class_TileSetAtlasSource_method_get_tile_animation_speed>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                                                                                                                                                       |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`get_tile_animation_total_duration<class_TileSetAtlasSource_method_get_tile_animation_total_duration>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                                                                                                                                     |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>`                                     | :ref:`get_tile_at_coords<class_TileSetAtlasSource_method_get_tile_at_coords>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                                                                                                                                                                   |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TileData<class_TileData>`                                     | :ref:`get_tile_data<class_TileSetAtlasSource_method_get_tile_data>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, alternative_tile\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                   |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>`                                     | :ref:`get_tile_size_in_atlas<class_TileSetAtlasSource_method_get_tile_size_in_atlas>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                                                                                                                                                           |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2i<class_Rect2i>`                                         | :ref:`get_tile_texture_region<class_TileSetAtlasSource_method_get_tile_texture_region>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, frame\: :ref:`int<class_int>` = 0\ ) |const|                                                                                                                                                                                                      |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>`                 | :ref:`get_tiles_to_be_removed_on_change<class_TileSetAtlasSource_method_get_tiles_to_be_removed_on_change>`\ (\ texture\: :ref:`Texture2D<class_Texture2D>`, margins\: :ref:`Vector2i<class_Vector2i>`, separation\: :ref:`Vector2i<class_Vector2i>`, texture_region_size\: :ref:`Vector2i<class_Vector2i>`\ )                                                                                |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                             | :ref:`has_room_for_tile<class_TileSetAtlasSource_method_has_room_for_tile>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, size\: :ref:`Vector2i<class_Vector2i>`, animation_columns\: :ref:`int<class_int>`, animation_separation\: :ref:`Vector2i<class_Vector2i>`, frames_count\: :ref:`int<class_int>`, ignored_tile\: :ref:`Vector2i<class_Vector2i>` = Vector2i(-1, -1)\ ) |const| |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                             | :ref:`has_tiles_outside_texture<class_TileSetAtlasSource_method_has_tiles_outside_texture>`\ (\ ) |const|                                                                                                                                                                                                                                                                                     |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`move_tile_in_atlas<class_TileSetAtlasSource_method_move_tile_in_atlas>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, new_atlas_coords\: :ref:`Vector2i<class_Vector2i>` = Vector2i(-1, -1), new_size\: :ref:`Vector2i<class_Vector2i>` = Vector2i(-1, -1)\ )                                                                                                                     |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`remove_alternative_tile<class_TileSetAtlasSource_method_remove_alternative_tile>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, alternative_tile\: :ref:`int<class_int>`\ )                                                                                                                                                                                                       |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`remove_tile<class_TileSetAtlasSource_method_remove_tile>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`\ )                                                                                                                                                                                                                                                                         |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`set_alternative_tile_id<class_TileSetAtlasSource_method_set_alternative_tile_id>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, alternative_tile\: :ref:`int<class_int>`, new_id\: :ref:`int<class_int>`\ )                                                                                                                                                                       |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`set_tile_animation_columns<class_TileSetAtlasSource_method_set_tile_animation_columns>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, frame_columns\: :ref:`int<class_int>`\ )                                                                                                                                                                                                    |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`set_tile_animation_frame_duration<class_TileSetAtlasSource_method_set_tile_animation_frame_duration>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, frame_index\: :ref:`int<class_int>`, duration\: :ref:`float<class_float>`\ )                                                                                                                                                  |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`set_tile_animation_frames_count<class_TileSetAtlasSource_method_set_tile_animation_frames_count>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, frames_count\: :ref:`int<class_int>`\ )                                                                                                                                                                                           |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`set_tile_animation_mode<class_TileSetAtlasSource_method_set_tile_animation_mode>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, mode\: :ref:`TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>`\ )                                                                                                                                                                     |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`set_tile_animation_separation<class_TileSetAtlasSource_method_set_tile_animation_separation>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, separation\: :ref:`Vector2i<class_Vector2i>`\ )                                                                                                                                                                                       |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`set_tile_animation_speed<class_TileSetAtlasSource_method_set_tile_animation_speed>`\ (\ atlas_coords\: :ref:`Vector2i<class_Vector2i>`, speed\: :ref:`float<class_float>`\ )                                                                                                                                                                                                            |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **TileAnimationMode**: [🔗<enum_TileSetAtlasSource_TileAnimationMode>]



[TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>] **TILE_ANIMATION_MODE_DEFAULT** = `0`

Tile animations start at same time, looking identical.



[TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>] **TILE_ANIMATION_MODE_RANDOM_START_TIMES** = `1`

Tile animations start at random times, looking varied.



[TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>] **TILE_ANIMATION_MODE_MAX** = `2`

Represents the size of the [TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>] enum.


----


## Constants



**TRANSFORM_FLIP_H** = `4096` [🔗<class_TileSetAtlasSource_constant_TRANSFORM_FLIP_H>]

Represents cell's horizontal flip flag. Should be used directly with [TileMapLayer<class_TileMapLayer>] to flip placed tiles by altering their alternative IDs.

::

    var alternate_id = $TileMapLayer.get_cell_alternative_tile(Vector2i(2, 2))
    if not alternate_id & TileSetAtlasSource.TRANSFORM_FLIP_H:
        # If tile is not already flipped, flip it.
        $TileMapLayer.set_cell(Vector2i(2, 2), source_id, atlas_coords, alternate_id | TileSetAtlasSource.TRANSFORM_FLIP_H)

\ **Note:** These transformations can be combined to do the equivalent of 0, 90, 180, and 270 degree rotations, as shown below:

::

    enum TileTransform {
        ROTATE_0 = 0,
        ROTATE_90 = TileSetAtlasSource.TRANSFORM_TRANSPOSE | TileSetAtlasSource.TRANSFORM_FLIP_H,
        ROTATE_180 = TileSetAtlasSource.TRANSFORM_FLIP_H | TileSetAtlasSource.TRANSFORM_FLIP_V,
        ROTATE_270 = TileSetAtlasSource.TRANSFORM_TRANSPOSE | TileSetAtlasSource.TRANSFORM_FLIP_V,
    }



**TRANSFORM_FLIP_V** = `8192` [🔗<class_TileSetAtlasSource_constant_TRANSFORM_FLIP_V>]

Represents cell's vertical flip flag. See [TRANSFORM_FLIP_H<class_TileSetAtlasSource_constant_TRANSFORM_FLIP_H>] for usage.



**TRANSFORM_TRANSPOSE** = `16384` [🔗<class_TileSetAtlasSource_constant_TRANSFORM_TRANSPOSE>]

Represents cell's transposed flag. See [TRANSFORM_FLIP_H<class_TileSetAtlasSource_constant_TRANSFORM_FLIP_H>] for usage.


----


## Property Descriptions



[Vector2i<class_Vector2i>] **margins** = `Vector2i(0, 0)` [🔗<class_TileSetAtlasSource_property_margins>]


- |void| **set_margins**\ (\ value\: [Vector2i<class_Vector2i>]\ )
- [Vector2i<class_Vector2i>] **get_margins**\ (\ )

Margins, in pixels, to offset the origin of the grid in the texture.


----



[Vector2i<class_Vector2i>] **separation** = `Vector2i(0, 0)` [🔗<class_TileSetAtlasSource_property_separation>]


- |void| **set_separation**\ (\ value\: [Vector2i<class_Vector2i>]\ )
- [Vector2i<class_Vector2i>] **get_separation**\ (\ )

Separation, in pixels, between each tile texture region of the grid.


----



[Texture2D<class_Texture2D>] **texture** [🔗<class_TileSetAtlasSource_property_texture>]


- |void| **set_texture**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_texture**\ (\ )

The atlas texture.


----



[Vector2i<class_Vector2i>] **texture_region_size** = `Vector2i(16, 16)` [🔗<class_TileSetAtlasSource_property_texture_region_size>]


- |void| **set_texture_region_size**\ (\ value\: [Vector2i<class_Vector2i>]\ )
- [Vector2i<class_Vector2i>] **get_texture_region_size**\ (\ )

The base tile size in the texture (in pixel). This size must be bigger than or equal to the TileSet's `tile_size` value.


----



[bool<class_bool>] **use_texture_padding** = `true` [🔗<class_TileSetAtlasSource_property_use_texture_padding>]


- |void| **set_use_texture_padding**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_use_texture_padding**\ (\ )

If `true`, generates an internal texture with an additional one pixel padding around each tile. Texture padding avoids a common artifact where lines appear between tiles.

Disabling this setting might lead a small performance improvement, as generating the internal texture requires both memory and processing time when the TileSetAtlasSource resource is modified.


----


## Method Descriptions



|void| **clear_tiles_outside_texture**\ (\ ) [🔗<class_TileSetAtlasSource_method_clear_tiles_outside_texture>]

Removes all tiles that don't fit the available texture area. This method iterates over all the source's tiles, so it's advised to use [has_tiles_outside_texture()<class_TileSetAtlasSource_method_has_tiles_outside_texture>] beforehand.


----



[int<class_int>] **create_alternative_tile**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], alternative_id_override\: [int<class_int>] = -1\ ) [🔗<class_TileSetAtlasSource_method_create_alternative_tile>]

Creates an alternative tile for the tile at coordinates `atlas_coords`. If `alternative_id_override` is -1, give it an automatically generated unique ID, or assigns it the given ID otherwise.

Returns the new alternative identifier, or -1 if the alternative could not be created with a provided `alternative_id_override`.


----



|void| **create_tile**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], size\: [Vector2i<class_Vector2i>] = Vector2i(1, 1)\ ) [🔗<class_TileSetAtlasSource_method_create_tile>]

Creates a new tile at coordinates `atlas_coords` with the given `size`.


----



[Vector2i<class_Vector2i>] **get_atlas_grid_size**\ (\ ) |const| [🔗<class_TileSetAtlasSource_method_get_atlas_grid_size>]

Returns the atlas grid size, which depends on how many tiles can fit in the texture. It thus depends on the [texture<class_TileSetAtlasSource_property_texture>]'s size, the atlas [margins<class_TileSetAtlasSource_property_margins>], and the tiles' [texture_region_size<class_TileSetAtlasSource_property_texture_region_size>].


----



[int<class_int>] **get_next_alternative_tile_id**\ (\ atlas_coords\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_TileSetAtlasSource_method_get_next_alternative_tile_id>]

Returns the alternative ID a following call to [create_alternative_tile()<class_TileSetAtlasSource_method_create_alternative_tile>] would return.


----



[Texture2D<class_Texture2D>] **get_runtime_texture**\ (\ ) |const| [🔗<class_TileSetAtlasSource_method_get_runtime_texture>]

If [use_texture_padding<class_TileSetAtlasSource_property_use_texture_padding>] is `false`, returns [texture<class_TileSetAtlasSource_property_texture>]. Otherwise, returns an internal [ImageTexture<class_ImageTexture>] created that includes the padding.


----



[Rect2i<class_Rect2i>] **get_runtime_tile_texture_region**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], frame\: [int<class_int>]\ ) |const| [🔗<class_TileSetAtlasSource_method_get_runtime_tile_texture_region>]

Returns the region of the tile at coordinates `atlas_coords` for the given `frame` inside the texture returned by [get_runtime_texture()<class_TileSetAtlasSource_method_get_runtime_texture>].

\ **Note:** If [use_texture_padding<class_TileSetAtlasSource_property_use_texture_padding>] is `false`, returns the same as [get_tile_texture_region()<class_TileSetAtlasSource_method_get_tile_texture_region>].


----



[int<class_int>] **get_tile_animation_columns**\ (\ atlas_coords\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_TileSetAtlasSource_method_get_tile_animation_columns>]

Returns how many columns the tile at `atlas_coords` has in its animation layout.


----



[float<class_float>] **get_tile_animation_frame_duration**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], frame_index\: [int<class_int>]\ ) |const| [🔗<class_TileSetAtlasSource_method_get_tile_animation_frame_duration>]

Returns the animation frame duration of frame `frame_index` for the tile at coordinates `atlas_coords`.


----



[int<class_int>] **get_tile_animation_frames_count**\ (\ atlas_coords\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_TileSetAtlasSource_method_get_tile_animation_frames_count>]

Returns how many animation frames has the tile at coordinates `atlas_coords`.


----



[TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>] **get_tile_animation_mode**\ (\ atlas_coords\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_TileSetAtlasSource_method_get_tile_animation_mode>]

Returns the tile animation mode of the tile at `atlas_coords`. See also [set_tile_animation_mode()<class_TileSetAtlasSource_method_set_tile_animation_mode>].


----



[Vector2i<class_Vector2i>] **get_tile_animation_separation**\ (\ atlas_coords\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_TileSetAtlasSource_method_get_tile_animation_separation>]

Returns the separation (as in the atlas grid) between each frame of an animated tile at coordinates `atlas_coords`.


----



[float<class_float>] **get_tile_animation_speed**\ (\ atlas_coords\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_TileSetAtlasSource_method_get_tile_animation_speed>]

Returns the animation speed of the tile at coordinates `atlas_coords`.


----



[float<class_float>] **get_tile_animation_total_duration**\ (\ atlas_coords\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_TileSetAtlasSource_method_get_tile_animation_total_duration>]

Returns the sum of the sum of the frame durations of the tile at coordinates `atlas_coords`. This value needs to be divided by the animation speed to get the actual animation loop duration.


----



[Vector2i<class_Vector2i>] **get_tile_at_coords**\ (\ atlas_coords\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_TileSetAtlasSource_method_get_tile_at_coords>]

If there is a tile covering the `atlas_coords` coordinates, returns the top-left coordinates of the tile (thus its coordinate ID). Returns `Vector2i(-1, -1)` otherwise.


----



[TileData<class_TileData>] **get_tile_data**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], alternative_tile\: [int<class_int>]\ ) |const| [🔗<class_TileSetAtlasSource_method_get_tile_data>]

Returns the [TileData<class_TileData>] object for the given atlas coordinates and alternative ID.


----



[Vector2i<class_Vector2i>] **get_tile_size_in_atlas**\ (\ atlas_coords\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_TileSetAtlasSource_method_get_tile_size_in_atlas>]

Returns the size of the tile (in the grid coordinates system) at coordinates `atlas_coords`.


----



[Rect2i<class_Rect2i>] **get_tile_texture_region**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], frame\: [int<class_int>] = 0\ ) |const| [🔗<class_TileSetAtlasSource_method_get_tile_texture_region>]

Returns a tile's texture region in the atlas texture. For animated tiles, a `frame` argument might be provided for the different frames of the animation.


----



[PackedVector2Array<class_PackedVector2Array>] **get_tiles_to_be_removed_on_change**\ (\ texture\: [Texture2D<class_Texture2D>], margins\: [Vector2i<class_Vector2i>], separation\: [Vector2i<class_Vector2i>], texture_region_size\: [Vector2i<class_Vector2i>]\ ) [🔗<class_TileSetAtlasSource_method_get_tiles_to_be_removed_on_change>]

Returns an array of tiles coordinates ID that will be automatically removed when modifying one or several of those properties: `texture`, `margins`, `separation` or `texture_region_size`. This can be used to undo changes that would have caused tiles data loss.


----



[bool<class_bool>] **has_room_for_tile**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], size\: [Vector2i<class_Vector2i>], animation_columns\: [int<class_int>], animation_separation\: [Vector2i<class_Vector2i>], frames_count\: [int<class_int>], ignored_tile\: [Vector2i<class_Vector2i>] = Vector2i(-1, -1)\ ) |const| [🔗<class_TileSetAtlasSource_method_has_room_for_tile>]

Returns whether there is enough room in an atlas to create/modify a tile with the given properties. If `ignored_tile` is provided, act as is the given tile was not present in the atlas. This may be used when you want to modify a tile's properties.


----



[bool<class_bool>] **has_tiles_outside_texture**\ (\ ) |const| [🔗<class_TileSetAtlasSource_method_has_tiles_outside_texture>]

Checks if the source has any tiles that don't fit the texture area (either partially or completely).


----



|void| **move_tile_in_atlas**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], new_atlas_coords\: [Vector2i<class_Vector2i>] = Vector2i(-1, -1), new_size\: [Vector2i<class_Vector2i>] = Vector2i(-1, -1)\ ) [🔗<class_TileSetAtlasSource_method_move_tile_in_atlas>]

Move the tile and its alternatives at the `atlas_coords` coordinates to the `new_atlas_coords` coordinates with the `new_size` size. This functions will fail if a tile is already present in the given area.

If `new_atlas_coords` is `Vector2i(-1, -1)`, keeps the tile's coordinates. If `new_size` is `Vector2i(-1, -1)`, keeps the tile's size.

To avoid an error, first check if a move is possible using [has_room_for_tile()<class_TileSetAtlasSource_method_has_room_for_tile>].


----



|void| **remove_alternative_tile**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], alternative_tile\: [int<class_int>]\ ) [🔗<class_TileSetAtlasSource_method_remove_alternative_tile>]

Remove a tile's alternative with alternative ID `alternative_tile`.

Calling this function with `alternative_tile` equals to 0 will fail, as the base tile alternative cannot be removed.


----



|void| **remove_tile**\ (\ atlas_coords\: [Vector2i<class_Vector2i>]\ ) [🔗<class_TileSetAtlasSource_method_remove_tile>]

Remove a tile and its alternative at coordinates `atlas_coords`.


----



|void| **set_alternative_tile_id**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], alternative_tile\: [int<class_int>], new_id\: [int<class_int>]\ ) [🔗<class_TileSetAtlasSource_method_set_alternative_tile_id>]

Change a tile's alternative ID from `alternative_tile` to `new_id`.

Calling this function with `new_id` of 0 will fail, as the base tile alternative cannot be moved.


----



|void| **set_tile_animation_columns**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], frame_columns\: [int<class_int>]\ ) [🔗<class_TileSetAtlasSource_method_set_tile_animation_columns>]

Sets the number of columns in the animation layout of the tile at coordinates `atlas_coords`. If set to 0, then the different frames of the animation are laid out as a single horizontal line in the atlas.


----



|void| **set_tile_animation_frame_duration**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], frame_index\: [int<class_int>], duration\: [float<class_float>]\ ) [🔗<class_TileSetAtlasSource_method_set_tile_animation_frame_duration>]

Sets the animation frame `duration` of frame `frame_index` for the tile at coordinates `atlas_coords`.


----



|void| **set_tile_animation_frames_count**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], frames_count\: [int<class_int>]\ ) [🔗<class_TileSetAtlasSource_method_set_tile_animation_frames_count>]

Sets how many animation frames the tile at coordinates `atlas_coords` has.


----



|void| **set_tile_animation_mode**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], mode\: [TileAnimationMode<enum_TileSetAtlasSource_TileAnimationMode>]\ ) [🔗<class_TileSetAtlasSource_method_set_tile_animation_mode>]

Sets the tile animation mode of the tile at `atlas_coords` to `mode`. See also [get_tile_animation_mode()<class_TileSetAtlasSource_method_get_tile_animation_mode>].


----



|void| **set_tile_animation_separation**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], separation\: [Vector2i<class_Vector2i>]\ ) [🔗<class_TileSetAtlasSource_method_set_tile_animation_separation>]

Sets the margin (in grid tiles) between each tile in the animation layout of the tile at coordinates `atlas_coords` has.


----



|void| **set_tile_animation_speed**\ (\ atlas_coords\: [Vector2i<class_Vector2i>], speed\: [float<class_float>]\ ) [🔗<class_TileSetAtlasSource_method_set_tile_animation_speed>]

Sets the animation speed of the tile at coordinates `atlas_coords` has.

