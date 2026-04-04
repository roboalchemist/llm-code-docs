:github_url: hide



# TileData

**Inherits:** [Object<class_Object>]

Settings for a single tile in a [TileSet<class_TileSet>].


## Description

**TileData** object represents a single tile in a [TileSet<class_TileSet>]. It is usually edited using the tileset editor, but it can be modified at runtime using [TileMapLayer._tile_data_runtime_update()<class_TileMapLayer_private_method__tile_data_runtime_update>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`         | :ref:`flip_h<class_TileData_property_flip_h>`                 | ``false``             |
> +---------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`         | :ref:`flip_v<class_TileData_property_flip_v>`                 | ``false``             |
> +---------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`Material<class_Material>` | :ref:`material<class_TileData_property_material>`             |                       |
> +---------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`       | :ref:`modulate<class_TileData_property_modulate>`             | ``Color(1, 1, 1, 1)`` |
> +---------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`       | :ref:`probability<class_TileData_property_probability>`       | ``1.0``               |
> +---------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`           | :ref:`terrain<class_TileData_property_terrain>`               | ``-1``                |
> +---------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`           | :ref:`terrain_set<class_TileData_property_terrain_set>`       | ``-1``                |
> +---------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`Vector2i<class_Vector2i>` | :ref:`texture_origin<class_TileData_property_texture_origin>` | ``Vector2i(0, 0)``    |
> +---------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`         | :ref:`transpose<class_TileData_property_transpose>`           | ``false``             |
> +---------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`           | :ref:`y_sort_origin<class_TileData_property_y_sort_origin>`   | ``0``                 |
> +---------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`           | :ref:`z_index<class_TileData_property_z_index>`               | ``0``                 |
> +---------------------------------+---------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`add_collision_polygon<class_TileData_method_add_collision_polygon>`\ (\ layer_id\: :ref:`int<class_int>`\ )                                                                                                                                                                               |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`add_occluder_polygon<class_TileData_method_add_occluder_polygon>`\ (\ layer_id\: :ref:`int<class_int>`\ )                                                                                                                                                                                 |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                           | :ref:`get_collision_polygon_one_way_margin<class_TileData_method_get_collision_polygon_one_way_margin>`\ (\ layer_id\: :ref:`int<class_int>`, polygon_index\: :ref:`int<class_int>`\ ) |const|                                                                                                  |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>` | :ref:`get_collision_polygon_points<class_TileData_method_get_collision_polygon_points>`\ (\ layer_id\: :ref:`int<class_int>`, polygon_index\: :ref:`int<class_int>`\ ) |const|                                                                                                                  |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_collision_polygons_count<class_TileData_method_get_collision_polygons_count>`\ (\ layer_id\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                         |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                           | :ref:`get_constant_angular_velocity<class_TileData_method_get_constant_angular_velocity>`\ (\ layer_id\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                       |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                       | :ref:`get_constant_linear_velocity<class_TileData_method_get_constant_linear_velocity>`\ (\ layer_id\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                         |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                       | :ref:`get_custom_data<class_TileData_method_get_custom_data>`\ (\ layer_name\: :ref:`String<class_String>`\ ) |const|                                                                                                                                                                           |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                       | :ref:`get_custom_data_by_layer_id<class_TileData_method_get_custom_data_by_layer_id>`\ (\ layer_id\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                           |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`NavigationPolygon<class_NavigationPolygon>`   | :ref:`get_navigation_polygon<class_TileData_method_get_navigation_polygon>`\ (\ layer_id\: :ref:`int<class_int>`, flip_h\: :ref:`bool<class_bool>` = false, flip_v\: :ref:`bool<class_bool>` = false, transpose\: :ref:`bool<class_bool>` = false\ ) |const|                                    |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`OccluderPolygon2D<class_OccluderPolygon2D>`   | :ref:`get_occluder<class_TileData_method_get_occluder>`\ (\ layer_id\: :ref:`int<class_int>`, flip_h\: :ref:`bool<class_bool>` = false, flip_v\: :ref:`bool<class_bool>` = false, transpose\: :ref:`bool<class_bool>` = false\ ) |const|                                                        |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`OccluderPolygon2D<class_OccluderPolygon2D>`   | :ref:`get_occluder_polygon<class_TileData_method_get_occluder_polygon>`\ (\ layer_id\: :ref:`int<class_int>`, polygon_index\: :ref:`int<class_int>`, flip_h\: :ref:`bool<class_bool>` = false, flip_v\: :ref:`bool<class_bool>` = false, transpose\: :ref:`bool<class_bool>` = false\ ) |const| |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_occluder_polygons_count<class_TileData_method_get_occluder_polygons_count>`\ (\ layer_id\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                           |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_terrain_peering_bit<class_TileData_method_get_terrain_peering_bit>`\ (\ peering_bit\: :ref:`CellNeighbor<enum_TileSet_CellNeighbor>`\ ) |const|                                                                                                                                       |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`has_custom_data<class_TileData_method_has_custom_data>`\ (\ layer_name\: :ref:`String<class_String>`\ ) |const|                                                                                                                                                                           |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`is_collision_polygon_one_way<class_TileData_method_is_collision_polygon_one_way>`\ (\ layer_id\: :ref:`int<class_int>`, polygon_index\: :ref:`int<class_int>`\ ) |const|                                                                                                                  |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`is_valid_terrain_peering_bit<class_TileData_method_is_valid_terrain_peering_bit>`\ (\ peering_bit\: :ref:`CellNeighbor<enum_TileSet_CellNeighbor>`\ ) |const|                                                                                                                             |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`remove_collision_polygon<class_TileData_method_remove_collision_polygon>`\ (\ layer_id\: :ref:`int<class_int>`, polygon_index\: :ref:`int<class_int>`\ )                                                                                                                                  |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`remove_occluder_polygon<class_TileData_method_remove_occluder_polygon>`\ (\ layer_id\: :ref:`int<class_int>`, polygon_index\: :ref:`int<class_int>`\ )                                                                                                                                    |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_collision_polygon_one_way<class_TileData_method_set_collision_polygon_one_way>`\ (\ layer_id\: :ref:`int<class_int>`, polygon_index\: :ref:`int<class_int>`, one_way\: :ref:`bool<class_bool>`\ )                                                                                     |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_collision_polygon_one_way_margin<class_TileData_method_set_collision_polygon_one_way_margin>`\ (\ layer_id\: :ref:`int<class_int>`, polygon_index\: :ref:`int<class_int>`, one_way_margin\: :ref:`float<class_float>`\ )                                                              |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_collision_polygon_points<class_TileData_method_set_collision_polygon_points>`\ (\ layer_id\: :ref:`int<class_int>`, polygon_index\: :ref:`int<class_int>`, polygon\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                           |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_collision_polygons_count<class_TileData_method_set_collision_polygons_count>`\ (\ layer_id\: :ref:`int<class_int>`, polygons_count\: :ref:`int<class_int>`\ )                                                                                                                         |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_constant_angular_velocity<class_TileData_method_set_constant_angular_velocity>`\ (\ layer_id\: :ref:`int<class_int>`, velocity\: :ref:`float<class_float>`\ )                                                                                                                         |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_constant_linear_velocity<class_TileData_method_set_constant_linear_velocity>`\ (\ layer_id\: :ref:`int<class_int>`, velocity\: :ref:`Vector2<class_Vector2>`\ )                                                                                                                       |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_custom_data<class_TileData_method_set_custom_data>`\ (\ layer_name\: :ref:`String<class_String>`, value\: :ref:`Variant<class_Variant>`\ )                                                                                                                                            |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_custom_data_by_layer_id<class_TileData_method_set_custom_data_by_layer_id>`\ (\ layer_id\: :ref:`int<class_int>`, value\: :ref:`Variant<class_Variant>`\ )                                                                                                                            |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_navigation_polygon<class_TileData_method_set_navigation_polygon>`\ (\ layer_id\: :ref:`int<class_int>`, navigation_polygon\: :ref:`NavigationPolygon<class_NavigationPolygon>`\ )                                                                                                     |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_occluder<class_TileData_method_set_occluder>`\ (\ layer_id\: :ref:`int<class_int>`, occluder_polygon\: :ref:`OccluderPolygon2D<class_OccluderPolygon2D>`\ )                                                                                                                           |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_occluder_polygon<class_TileData_method_set_occluder_polygon>`\ (\ layer_id\: :ref:`int<class_int>`, polygon_index\: :ref:`int<class_int>`, polygon\: :ref:`OccluderPolygon2D<class_OccluderPolygon2D>`\ )                                                                             |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_occluder_polygons_count<class_TileData_method_set_occluder_polygons_count>`\ (\ layer_id\: :ref:`int<class_int>`, polygons_count\: :ref:`int<class_int>`\ )                                                                                                                           |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_terrain_peering_bit<class_TileData_method_set_terrain_peering_bit>`\ (\ peering_bit\: :ref:`CellNeighbor<enum_TileSet_CellNeighbor>`, terrain\: :ref:`int<class_int>`\ )                                                                                                              |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**changed**\ (\ ) [🔗<class_TileData_signal_changed>]

Emitted when any of the properties are changed.


----


## Property Descriptions



[bool<class_bool>] **flip_h** = `false` [🔗<class_TileData_property_flip_h>]


- |void| **set_flip_h**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flip_h**\ (\ )

If `true`, the tile will have its texture flipped horizontally.


----



[bool<class_bool>] **flip_v** = `false` [🔗<class_TileData_property_flip_v>]


- |void| **set_flip_v**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flip_v**\ (\ )

If `true`, the tile will have its texture flipped vertically.


----



[Material<class_Material>] **material** [🔗<class_TileData_property_material>]


- |void| **set_material**\ (\ value\: [Material<class_Material>]\ )
- [Material<class_Material>] **get_material**\ (\ )

The [Material<class_Material>] to use for this **TileData**. This can be a [CanvasItemMaterial<class_CanvasItemMaterial>] to use the default shader, or a [ShaderMaterial<class_ShaderMaterial>] to use a custom shader.


----



[Color<class_Color>] **modulate** = `Color(1, 1, 1, 1)` [🔗<class_TileData_property_modulate>]


- |void| **set_modulate**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_modulate**\ (\ )

Color modulation of the tile.


----



[float<class_float>] **probability** = `1.0` [🔗<class_TileData_property_probability>]


- |void| **set_probability**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_probability**\ (\ )

Relative probability of this tile being selected when drawing a pattern of random tiles.


----



[int<class_int>] **terrain** = `-1` [🔗<class_TileData_property_terrain>]


- |void| **set_terrain**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_terrain**\ (\ )

ID of the terrain from the terrain set that the tile uses.


----



[int<class_int>] **terrain_set** = `-1` [🔗<class_TileData_property_terrain_set>]


- |void| **set_terrain_set**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_terrain_set**\ (\ )

ID of the terrain set that the tile uses.


----



[Vector2i<class_Vector2i>] **texture_origin** = `Vector2i(0, 0)` [🔗<class_TileData_property_texture_origin>]


- |void| **set_texture_origin**\ (\ value\: [Vector2i<class_Vector2i>]\ )
- [Vector2i<class_Vector2i>] **get_texture_origin**\ (\ )

Offsets the position of where the tile is drawn.


----



[bool<class_bool>] **transpose** = `false` [🔗<class_TileData_property_transpose>]


- |void| **set_transpose**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_transpose**\ (\ )

If `true`, the tile will display transposed, i.e. with horizontal and vertical texture UVs swapped.


----



[int<class_int>] **y_sort_origin** = `0` [🔗<class_TileData_property_y_sort_origin>]


- |void| **set_y_sort_origin**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_y_sort_origin**\ (\ )

Vertical point of the tile used for determining y-sorted order.


----



[int<class_int>] **z_index** = `0` [🔗<class_TileData_property_z_index>]


- |void| **set_z_index**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_z_index**\ (\ )

Ordering index of this tile, relative to [TileMapLayer<class_TileMapLayer>].


----


## Method Descriptions



|void| **add_collision_polygon**\ (\ layer_id\: [int<class_int>]\ ) [🔗<class_TileData_method_add_collision_polygon>]

Adds a collision polygon to the tile on the given TileSet physics layer.


----



|void| **add_occluder_polygon**\ (\ layer_id\: [int<class_int>]\ ) [🔗<class_TileData_method_add_occluder_polygon>]

Adds an occlusion polygon to the tile on the TileSet occlusion layer with index `layer_id`.


----



[float<class_float>] **get_collision_polygon_one_way_margin**\ (\ layer_id\: [int<class_int>], polygon_index\: [int<class_int>]\ ) |const| [🔗<class_TileData_method_get_collision_polygon_one_way_margin>]

Returns the one-way margin (for one-way platforms) of the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.


----



[PackedVector2Array<class_PackedVector2Array>] **get_collision_polygon_points**\ (\ layer_id\: [int<class_int>], polygon_index\: [int<class_int>]\ ) |const| [🔗<class_TileData_method_get_collision_polygon_points>]

Returns the points of the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.


----



[int<class_int>] **get_collision_polygons_count**\ (\ layer_id\: [int<class_int>]\ ) |const| [🔗<class_TileData_method_get_collision_polygons_count>]

Returns how many polygons the tile has for TileSet physics layer with index `layer_id`.


----



[float<class_float>] **get_constant_angular_velocity**\ (\ layer_id\: [int<class_int>]\ ) |const| [🔗<class_TileData_method_get_constant_angular_velocity>]

Returns the constant angular velocity applied to objects colliding with this tile.


----



[Vector2<class_Vector2>] **get_constant_linear_velocity**\ (\ layer_id\: [int<class_int>]\ ) |const| [🔗<class_TileData_method_get_constant_linear_velocity>]

Returns the constant linear velocity applied to objects colliding with this tile.


----



[Variant<class_Variant>] **get_custom_data**\ (\ layer_name\: [String<class_String>]\ ) |const| [🔗<class_TileData_method_get_custom_data>]

Returns the custom data value for custom data layer named `layer_name`. To check if a custom data layer exists, use [has_custom_data()<class_TileData_method_has_custom_data>].


----



[Variant<class_Variant>] **get_custom_data_by_layer_id**\ (\ layer_id\: [int<class_int>]\ ) |const| [🔗<class_TileData_method_get_custom_data_by_layer_id>]

Returns the custom data value for custom data layer with index `layer_id`.


----



[NavigationPolygon<class_NavigationPolygon>] **get_navigation_polygon**\ (\ layer_id\: [int<class_int>], flip_h\: [bool<class_bool>] = false, flip_v\: [bool<class_bool>] = false, transpose\: [bool<class_bool>] = false\ ) |const| [🔗<class_TileData_method_get_navigation_polygon>]

Returns the navigation polygon of the tile for the TileSet navigation layer with index `layer_id`.

\ `flip_h`, `flip_v`, and `transpose` allow transforming the returned polygon.


----



[OccluderPolygon2D<class_OccluderPolygon2D>] **get_occluder**\ (\ layer_id\: [int<class_int>], flip_h\: [bool<class_bool>] = false, flip_v\: [bool<class_bool>] = false, transpose\: [bool<class_bool>] = false\ ) |const| [🔗<class_TileData_method_get_occluder>]

**Deprecated:** Use [get_occluder_polygon()<class_TileData_method_get_occluder_polygon>] instead.

Returns the occluder polygon of the tile for the TileSet occlusion layer with index `layer_id`.

\ `flip_h`, `flip_v`, and `transpose` allow transforming the returned polygon.


----



[OccluderPolygon2D<class_OccluderPolygon2D>] **get_occluder_polygon**\ (\ layer_id\: [int<class_int>], polygon_index\: [int<class_int>], flip_h\: [bool<class_bool>] = false, flip_v\: [bool<class_bool>] = false, transpose\: [bool<class_bool>] = false\ ) |const| [🔗<class_TileData_method_get_occluder_polygon>]

Returns the occluder polygon at index `polygon_index` from the TileSet occlusion layer with index `layer_id`.

The `flip_h`, `flip_v`, and `transpose` parameters can be `true` to transform the returned polygon.


----



[int<class_int>] **get_occluder_polygons_count**\ (\ layer_id\: [int<class_int>]\ ) |const| [🔗<class_TileData_method_get_occluder_polygons_count>]

Returns the number of occluder polygons of the tile in the TileSet occlusion layer with index `layer_id`.


----



[int<class_int>] **get_terrain_peering_bit**\ (\ peering_bit\: [CellNeighbor<enum_TileSet_CellNeighbor>]\ ) |const| [🔗<class_TileData_method_get_terrain_peering_bit>]

Returns the tile's terrain bit for the given `peering_bit` direction. To check that a direction is valid, use [is_valid_terrain_peering_bit()<class_TileData_method_is_valid_terrain_peering_bit>].


----



[bool<class_bool>] **has_custom_data**\ (\ layer_name\: [String<class_String>]\ ) |const| [🔗<class_TileData_method_has_custom_data>]

Returns whether there exists a custom data layer named `layer_name`.


----



[bool<class_bool>] **is_collision_polygon_one_way**\ (\ layer_id\: [int<class_int>], polygon_index\: [int<class_int>]\ ) |const| [🔗<class_TileData_method_is_collision_polygon_one_way>]

Returns whether one-way collisions are enabled for the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.


----



[bool<class_bool>] **is_valid_terrain_peering_bit**\ (\ peering_bit\: [CellNeighbor<enum_TileSet_CellNeighbor>]\ ) |const| [🔗<class_TileData_method_is_valid_terrain_peering_bit>]

Returns whether the given `peering_bit` direction is valid for this tile.


----



|void| **remove_collision_polygon**\ (\ layer_id\: [int<class_int>], polygon_index\: [int<class_int>]\ ) [🔗<class_TileData_method_remove_collision_polygon>]

Removes the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.


----



|void| **remove_occluder_polygon**\ (\ layer_id\: [int<class_int>], polygon_index\: [int<class_int>]\ ) [🔗<class_TileData_method_remove_occluder_polygon>]

Removes the polygon at index `polygon_index` for TileSet occlusion layer with index `layer_id`.


----



|void| **set_collision_polygon_one_way**\ (\ layer_id\: [int<class_int>], polygon_index\: [int<class_int>], one_way\: [bool<class_bool>]\ ) [🔗<class_TileData_method_set_collision_polygon_one_way>]

Enables/disables one-way collisions on the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.


----



|void| **set_collision_polygon_one_way_margin**\ (\ layer_id\: [int<class_int>], polygon_index\: [int<class_int>], one_way_margin\: [float<class_float>]\ ) [🔗<class_TileData_method_set_collision_polygon_one_way_margin>]

Sets the one-way margin (for one-way platforms) of the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.


----



|void| **set_collision_polygon_points**\ (\ layer_id\: [int<class_int>], polygon_index\: [int<class_int>], polygon\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_TileData_method_set_collision_polygon_points>]

Sets the points of the polygon at index `polygon_index` for TileSet physics layer with index `layer_id`.


----



|void| **set_collision_polygons_count**\ (\ layer_id\: [int<class_int>], polygons_count\: [int<class_int>]\ ) [🔗<class_TileData_method_set_collision_polygons_count>]

Sets the polygons count for TileSet physics layer with index `layer_id`.


----



|void| **set_constant_angular_velocity**\ (\ layer_id\: [int<class_int>], velocity\: [float<class_float>]\ ) [🔗<class_TileData_method_set_constant_angular_velocity>]

Sets the constant angular velocity. This does not rotate the tile. This angular velocity is applied to objects colliding with this tile.


----



|void| **set_constant_linear_velocity**\ (\ layer_id\: [int<class_int>], velocity\: [Vector2<class_Vector2>]\ ) [🔗<class_TileData_method_set_constant_linear_velocity>]

Sets the constant linear velocity. This does not move the tile. This linear velocity is applied to objects colliding with this tile. This is useful to create conveyor belts.


----



|void| **set_custom_data**\ (\ layer_name\: [String<class_String>], value\: [Variant<class_Variant>]\ ) [🔗<class_TileData_method_set_custom_data>]

Sets the tile's custom data value for the TileSet custom data layer with name `layer_name`.


----



|void| **set_custom_data_by_layer_id**\ (\ layer_id\: [int<class_int>], value\: [Variant<class_Variant>]\ ) [🔗<class_TileData_method_set_custom_data_by_layer_id>]

Sets the tile's custom data value for the TileSet custom data layer with index `layer_id`.


----



|void| **set_navigation_polygon**\ (\ layer_id\: [int<class_int>], navigation_polygon\: [NavigationPolygon<class_NavigationPolygon>]\ ) [🔗<class_TileData_method_set_navigation_polygon>]

Sets the navigation polygon for the TileSet navigation layer with index `layer_id`.


----



|void| **set_occluder**\ (\ layer_id\: [int<class_int>], occluder_polygon\: [OccluderPolygon2D<class_OccluderPolygon2D>]\ ) [🔗<class_TileData_method_set_occluder>]

**Deprecated:** Use [set_occluder_polygon()<class_TileData_method_set_occluder_polygon>] instead.

Sets the occluder for the TileSet occlusion layer with index `layer_id`.


----



|void| **set_occluder_polygon**\ (\ layer_id\: [int<class_int>], polygon_index\: [int<class_int>], polygon\: [OccluderPolygon2D<class_OccluderPolygon2D>]\ ) [🔗<class_TileData_method_set_occluder_polygon>]

Sets the occluder for polygon with index `polygon_index` in the TileSet occlusion layer with index `layer_id`.


----



|void| **set_occluder_polygons_count**\ (\ layer_id\: [int<class_int>], polygons_count\: [int<class_int>]\ ) [🔗<class_TileData_method_set_occluder_polygons_count>]

Sets the occluder polygon count in the TileSet occlusion layer with index `layer_id`.


----



|void| **set_terrain_peering_bit**\ (\ peering_bit\: [CellNeighbor<enum_TileSet_CellNeighbor>], terrain\: [int<class_int>]\ ) [🔗<class_TileData_method_set_terrain_peering_bit>]

Sets the tile's terrain bit for the given `peering_bit` direction. To check that a direction is valid, use [is_valid_terrain_peering_bit()<class_TileData_method_is_valid_terrain_peering_bit>].

