:github_url: hide



# EditorSelection

**Inherits:** [Object<class_Object>]

Manages the SceneTree selection in the editor.


## Description

This object manages the SceneTree selection in the editor.

\ **Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_selection()<class_EditorInterface_method_get_selection>].


## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
> | |void|                                               | :ref:`add_node<class_EditorSelection_method_add_node>`\ (\ node\: :ref:`Node<class_Node>`\ )                 |
> +------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
> | |void|                                               | :ref:`clear<class_EditorSelection_method_clear>`\ (\ )                                                       |
> +------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Node<class_Node>`\] | :ref:`get_selected_nodes<class_EditorSelection_method_get_selected_nodes>`\ (\ )                             |
> +------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Node<class_Node>`\] | :ref:`get_top_selected_nodes<class_EditorSelection_method_get_top_selected_nodes>`\ (\ )                     |
> +------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Node<class_Node>`\] | :ref:`get_transformable_selected_nodes<class_EditorSelection_method_get_transformable_selected_nodes>`\ (\ ) |
> +------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
> | |void|                                               | :ref:`remove_node<class_EditorSelection_method_remove_node>`\ (\ node\: :ref:`Node<class_Node>`\ )           |
> +------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**selection_changed**\ (\ ) [🔗<class_EditorSelection_signal_selection_changed>]

Emitted when the selection changes.


----


## Method Descriptions



|void| **add_node**\ (\ node\: [Node<class_Node>]\ ) [🔗<class_EditorSelection_method_add_node>]

Adds a node to the selection.

\ **Note:** The newly selected node will not be automatically edited in the inspector. If you want to edit a node, use [EditorInterface.edit_node()<class_EditorInterface_method_edit_node>].


----



|void| **clear**\ (\ ) [🔗<class_EditorSelection_method_clear>]

Clear the selection.


----



[Array<class_Array>]\[[Node<class_Node>]\] **get_selected_nodes**\ (\ ) [🔗<class_EditorSelection_method_get_selected_nodes>]

Returns the list of selected nodes.


----



[Array<class_Array>]\[[Node<class_Node>]\] **get_top_selected_nodes**\ (\ ) [🔗<class_EditorSelection_method_get_top_selected_nodes>]

Returns the list of top selected nodes only, excluding any children. This is useful for performing transform operations (moving them, rotating, etc.).

For example, if there is a node A with a child B and a sibling C, then selecting all three will cause this method to return only A and C. Changing the global transform of A will affect the global transform of B, so there is no need to change B separately.


----



[Array<class_Array>]\[[Node<class_Node>]\] **get_transformable_selected_nodes**\ (\ ) [🔗<class_EditorSelection_method_get_transformable_selected_nodes>]

**Deprecated:** Use [get_top_selected_nodes()<class_EditorSelection_method_get_top_selected_nodes>] instead.

Returns the list of top selected nodes only, excluding any children. This is useful for performing transform operations (moving them, rotating, etc.). See [get_top_selected_nodes()<class_EditorSelection_method_get_top_selected_nodes>].


----



|void| **remove_node**\ (\ node\: [Node<class_Node>]\ ) [🔗<class_EditorSelection_method_remove_node>]

Removes a node from the selection.

