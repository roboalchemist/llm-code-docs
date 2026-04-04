:github_url: hide



# TileMapPattern

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Holds a pattern to be copied from or pasted into [TileMap<class_TileMap>]\ s.


## Description

This resource holds a set of cells to help bulk manipulations of [TileMap<class_TileMap>].

A pattern always starts at the `(0, 0)` coordinates and cannot have cells with negative coordinates.


## Methods

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                        | :ref:`get_cell_alternative_tile<class_TileMapPattern_method_get_cell_alternative_tile>`\ (\ coords\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                                 |
> +--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>`                              | :ref:`get_cell_atlas_coords<class_TileMapPattern_method_get_cell_atlas_coords>`\ (\ coords\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                                         |
> +--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                        | :ref:`get_cell_source_id<class_TileMapPattern_method_get_cell_source_id>`\ (\ coords\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                                               |
> +--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>`                              | :ref:`get_size<class_TileMapPattern_method_get_size>`\ (\ ) |const|                                                                                                                                                                                             |
> +--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Vector2i<class_Vector2i>`\] | :ref:`get_used_cells<class_TileMapPattern_method_get_used_cells>`\ (\ ) |const|                                                                                                                                                                                 |
> +--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                      | :ref:`has_cell<class_TileMapPattern_method_has_cell>`\ (\ coords\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                                                                                                                   |
> +--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                      | :ref:`is_empty<class_TileMapPattern_method_is_empty>`\ (\ ) |const|                                                                                                                                                                                             |
> +--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                       | :ref:`remove_cell<class_TileMapPattern_method_remove_cell>`\ (\ coords\: :ref:`Vector2i<class_Vector2i>`, update_size\: :ref:`bool<class_bool>`\ )                                                                                                              |
> +--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                       | :ref:`set_cell<class_TileMapPattern_method_set_cell>`\ (\ coords\: :ref:`Vector2i<class_Vector2i>`, source_id\: :ref:`int<class_int>` = -1, atlas_coords\: :ref:`Vector2i<class_Vector2i>` = Vector2i(-1, -1), alternative_tile\: :ref:`int<class_int>` = -1\ ) |
> +--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                       | :ref:`set_size<class_TileMapPattern_method_set_size>`\ (\ size\: :ref:`Vector2i<class_Vector2i>`\ )                                                                                                                                                             |
> +--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **get_cell_alternative_tile**\ (\ coords\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_TileMapPattern_method_get_cell_alternative_tile>]

Returns the tile alternative ID of the cell at `coords`.


----



[Vector2i<class_Vector2i>] **get_cell_atlas_coords**\ (\ coords\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_TileMapPattern_method_get_cell_atlas_coords>]

Returns the tile atlas coordinates ID of the cell at `coords`.


----



[int<class_int>] **get_cell_source_id**\ (\ coords\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_TileMapPattern_method_get_cell_source_id>]

Returns the tile source ID of the cell at `coords`.


----



[Vector2i<class_Vector2i>] **get_size**\ (\ ) |const| [🔗<class_TileMapPattern_method_get_size>]

Returns the size, in cells, of the pattern.


----



[Array<class_Array>]\[[Vector2i<class_Vector2i>]\] **get_used_cells**\ (\ ) |const| [🔗<class_TileMapPattern_method_get_used_cells>]

Returns the list of used cell coordinates in the pattern.


----



[bool<class_bool>] **has_cell**\ (\ coords\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_TileMapPattern_method_has_cell>]

Returns whether the pattern has a tile at the given coordinates.


----



[bool<class_bool>] **is_empty**\ (\ ) |const| [🔗<class_TileMapPattern_method_is_empty>]

Returns whether the pattern is empty or not.


----



|void| **remove_cell**\ (\ coords\: [Vector2i<class_Vector2i>], update_size\: [bool<class_bool>]\ ) [🔗<class_TileMapPattern_method_remove_cell>]

Remove the cell at the given coordinates.


----



|void| **set_cell**\ (\ coords\: [Vector2i<class_Vector2i>], source_id\: [int<class_int>] = -1, atlas_coords\: [Vector2i<class_Vector2i>] = Vector2i(-1, -1), alternative_tile\: [int<class_int>] = -1\ ) [🔗<class_TileMapPattern_method_set_cell>]

Sets the tile identifiers for the cell at coordinates `coords`. See [TileMap.set_cell()<class_TileMap_method_set_cell>].


----



|void| **set_size**\ (\ size\: [Vector2i<class_Vector2i>]\ ) [🔗<class_TileMapPattern_method_set_size>]

Sets the size of the pattern.

