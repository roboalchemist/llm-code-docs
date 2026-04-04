:github_url: hide



# TileSetScenesCollectionSource

**Inherits:** [TileSetSource<class_TileSetSource>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Exposes a set of scenes as tiles for a [TileSet<class_TileSet>] resource.


## Description

When placed on a [TileMapLayer<class_TileMapLayer>], tiles from **TileSetScenesCollectionSource** will automatically instantiate an associated scene at the cell's position in the TileMapLayer.

Scenes are instantiated as children of the [TileMapLayer<class_TileMapLayer>] after it enters the tree, at the end of the frame (their creation is deferred). If you add/remove a scene tile in the [TileMapLayer<class_TileMapLayer>] that is already inside the tree, the [TileMapLayer<class_TileMapLayer>] will automatically instantiate/free the scene accordingly.

\ **Note:** Scene tiles all occupy one tile slot and instead use alternate tile ID to identify scene index. [TileSetSource.get_tiles_count()<class_TileSetSource_method_get_tiles_count>] will always return `1`. Use [get_scene_tiles_count()<class_TileSetScenesCollectionSource_method_get_scene_tiles_count>] to get a number of scenes in a **TileSetScenesCollectionSource**.

Use this code if you want to find the scene path at a given tile in [TileMapLayer<class_TileMapLayer>]:


> **TABS**
>

    var source_id = tile_map_layer.get_cell_source_id(Vector2i(x, y))
    if source_id > -1:
        var scene_source = tile_map_layer.tile_set.get_source(source_id)
        if scene_source is TileSetScenesCollectionSource:
            var alt_id = tile_map_layer.get_cell_alternative_tile(Vector2i(x, y))
            # The assigned PackedScene.
            var scene = scene_source.get_scene_tile_scene(alt_id)


    int sourceId = tileMapLayer.GetCellSourceId(new Vector2I(x, y));
    if (sourceId > -1)
    {
        TileSetSource source = tileMapLayer.TileSet.GetSource(sourceId);
        if (source is TileSetScenesCollectionSource sceneSource)
        {
            int altId = tileMapLayer.GetCellAlternativeTile(new Vector2I(x, y));
            // The assigned PackedScene.
            PackedScene scene = sceneSource.GetSceneTileScene(altId);
## }




## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`create_scene_tile<class_TileSetScenesCollectionSource_method_create_scene_tile>`\ (\ packed_scene\: :ref:`PackedScene<class_PackedScene>`, id_override\: :ref:`int<class_int>` = -1\ )              |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_next_scene_tile_id<class_TileSetScenesCollectionSource_method_get_next_scene_tile_id>`\ (\ ) |const|                                                                                            |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`get_scene_tile_display_placeholder<class_TileSetScenesCollectionSource_method_get_scene_tile_display_placeholder>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                        |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_scene_tile_id<class_TileSetScenesCollectionSource_method_get_scene_tile_id>`\ (\ index\: :ref:`int<class_int>`\ )                                                                               |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedScene<class_PackedScene>` | :ref:`get_scene_tile_scene<class_TileSetScenesCollectionSource_method_get_scene_tile_scene>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                                    |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_scene_tiles_count<class_TileSetScenesCollectionSource_method_get_scene_tiles_count>`\ (\ )                                                                                                      |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`has_scene_tile_id<class_TileSetScenesCollectionSource_method_has_scene_tile_id>`\ (\ id\: :ref:`int<class_int>`\ )                                                                                  |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`remove_scene_tile<class_TileSetScenesCollectionSource_method_remove_scene_tile>`\ (\ id\: :ref:`int<class_int>`\ )                                                                                  |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_scene_tile_display_placeholder<class_TileSetScenesCollectionSource_method_set_scene_tile_display_placeholder>`\ (\ id\: :ref:`int<class_int>`, display_placeholder\: :ref:`bool<class_bool>`\ ) |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_scene_tile_id<class_TileSetScenesCollectionSource_method_set_scene_tile_id>`\ (\ id\: :ref:`int<class_int>`, new_id\: :ref:`int<class_int>`\ )                                                  |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_scene_tile_scene<class_TileSetScenesCollectionSource_method_set_scene_tile_scene>`\ (\ id\: :ref:`int<class_int>`, packed_scene\: :ref:`PackedScene<class_PackedScene>`\ )                      |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **create_scene_tile**\ (\ packed_scene\: [PackedScene<class_PackedScene>], id_override\: [int<class_int>] = -1\ ) [🔗<class_TileSetScenesCollectionSource_method_create_scene_tile>]

Creates a scene-based tile out of the given scene.

Returns a newly generated unique ID.


----



[int<class_int>] **get_next_scene_tile_id**\ (\ ) |const| [🔗<class_TileSetScenesCollectionSource_method_get_next_scene_tile_id>]

Returns the scene ID a following call to [create_scene_tile()<class_TileSetScenesCollectionSource_method_create_scene_tile>] would return.


----



[bool<class_bool>] **get_scene_tile_display_placeholder**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_TileSetScenesCollectionSource_method_get_scene_tile_display_placeholder>]

Returns whether the scene tile with `id` displays a placeholder in the editor.


----



[int<class_int>] **get_scene_tile_id**\ (\ index\: [int<class_int>]\ ) [🔗<class_TileSetScenesCollectionSource_method_get_scene_tile_id>]

Returns the scene tile ID of the scene tile at `index`.


----



[PackedScene<class_PackedScene>] **get_scene_tile_scene**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_TileSetScenesCollectionSource_method_get_scene_tile_scene>]

Returns the [PackedScene<class_PackedScene>] resource of scene tile with `id`.


----



[int<class_int>] **get_scene_tiles_count**\ (\ ) [🔗<class_TileSetScenesCollectionSource_method_get_scene_tiles_count>]

Returns the number or scene tiles this TileSet source has.


----



[bool<class_bool>] **has_scene_tile_id**\ (\ id\: [int<class_int>]\ ) [🔗<class_TileSetScenesCollectionSource_method_has_scene_tile_id>]

Returns whether this TileSet source has a scene tile with `id`.


----



|void| **remove_scene_tile**\ (\ id\: [int<class_int>]\ ) [🔗<class_TileSetScenesCollectionSource_method_remove_scene_tile>]

Remove the scene tile with `id`.


----



|void| **set_scene_tile_display_placeholder**\ (\ id\: [int<class_int>], display_placeholder\: [bool<class_bool>]\ ) [🔗<class_TileSetScenesCollectionSource_method_set_scene_tile_display_placeholder>]

Sets whether or not the scene tile with `id` should display a placeholder in the editor. This might be useful for scenes that are not visible.


----



|void| **set_scene_tile_id**\ (\ id\: [int<class_int>], new_id\: [int<class_int>]\ ) [🔗<class_TileSetScenesCollectionSource_method_set_scene_tile_id>]

Changes a scene tile's ID from `id` to `new_id`. This will fail if there is already a tile with an ID equal to `new_id`.


----



|void| **set_scene_tile_scene**\ (\ id\: [int<class_int>], packed_scene\: [PackedScene<class_PackedScene>]\ ) [🔗<class_TileSetScenesCollectionSource_method_set_scene_tile_scene>]

Assigns a [PackedScene<class_PackedScene>] resource to the scene tile with `id`. This will fail if the scene does not extend [CanvasItem<class_CanvasItem>], as positioning properties are needed to place the scene on the [TileMapLayer<class_TileMapLayer>].

