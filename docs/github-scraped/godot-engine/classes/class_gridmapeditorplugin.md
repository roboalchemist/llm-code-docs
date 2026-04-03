:github_url: hide

> **META**
	:keywords: tilemap



# GridMapEditorPlugin

**Inherits:** [EditorPlugin<class_EditorPlugin>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Editor for [GridMap<class_GridMap>] nodes.


## Description

GridMapEditorPlugin provides access to the [GridMap<class_GridMap>] editor functionality.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`clear_selection<class_GridMapEditorPlugin_method_clear_selection>`\ (\ )                                                                             |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GridMap<class_GridMap>` | :ref:`get_current_grid_map<class_GridMapEditorPlugin_method_get_current_grid_map>`\ (\ ) |const|                                                           |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`     | :ref:`get_selected_cells<class_GridMapEditorPlugin_method_get_selected_cells>`\ (\ ) |const|                                                               |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`         | :ref:`get_selected_palette_item<class_GridMapEditorPlugin_method_get_selected_palette_item>`\ (\ ) |const|                                                 |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AABB<class_AABB>`       | :ref:`get_selection<class_GridMapEditorPlugin_method_get_selection>`\ (\ ) |const|                                                                         |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`has_selection<class_GridMapEditorPlugin_method_has_selection>`\ (\ ) |const|                                                                         |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_selected_palette_item<class_GridMapEditorPlugin_method_set_selected_palette_item>`\ (\ item\: :ref:`int<class_int>`\ ) |const|                   |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_selection<class_GridMapEditorPlugin_method_set_selection>`\ (\ begin\: :ref:`Vector3i<class_Vector3i>`, end\: :ref:`Vector3i<class_Vector3i>`\ ) |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **clear_selection**\ (\ ) [🔗<class_GridMapEditorPlugin_method_clear_selection>]

Deselects any currently selected cells.


----



[GridMap<class_GridMap>] **get_current_grid_map**\ (\ ) |const| [🔗<class_GridMapEditorPlugin_method_get_current_grid_map>]

Returns the [GridMap<class_GridMap>] node currently edited by the grid map editor.


----



[Array<class_Array>] **get_selected_cells**\ (\ ) |const| [🔗<class_GridMapEditorPlugin_method_get_selected_cells>]

Returns an array of [Vector3i<class_Vector3i>]\ s with the selected cells' coordinates.


----



[int<class_int>] **get_selected_palette_item**\ (\ ) |const| [🔗<class_GridMapEditorPlugin_method_get_selected_palette_item>]

Returns the index of the selected [MeshLibrary<class_MeshLibrary>] item in the grid map editor's palette or `-1` if no item is selected.

\ **Note:** The indices might not be in the same order as they appear in the editor's interface.


----



[AABB<class_AABB>] **get_selection**\ (\ ) |const| [🔗<class_GridMapEditorPlugin_method_get_selection>]

Returns the cell coordinate bounds of the current selection. Use [has_selection()<class_GridMapEditorPlugin_method_has_selection>] to check if there is an active selection.


----



[bool<class_bool>] **has_selection**\ (\ ) |const| [🔗<class_GridMapEditorPlugin_method_has_selection>]

Returns `true` if there are selected cells.


----



|void| **set_selected_palette_item**\ (\ item\: [int<class_int>]\ ) |const| [🔗<class_GridMapEditorPlugin_method_set_selected_palette_item>]

Selects the [MeshLibrary<class_MeshLibrary>] item with the given index in the grid map editor's palette. If a negative index is given, no item will be selected. If a value greater than the last index is given, the last item will be selected.

\ **Note:** The indices might not be in the same order as they appear in the editor's interface.


----



|void| **set_selection**\ (\ begin\: [Vector3i<class_Vector3i>], end\: [Vector3i<class_Vector3i>]\ ) [🔗<class_GridMapEditorPlugin_method_set_selection>]

Selects the cells inside the given bounds from `begin` to `end`.

