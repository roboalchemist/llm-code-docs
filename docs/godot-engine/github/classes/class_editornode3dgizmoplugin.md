:github_url: hide



# EditorNode3DGizmoPlugin

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A class used by the editor to define Node3D gizmo types.


## Description

**EditorNode3DGizmoPlugin** allows you to define a new type of Gizmo. There are two main ways to do so: extending **EditorNode3DGizmoPlugin** for the simpler gizmos, or creating a new [EditorNode3DGizmo<class_EditorNode3DGizmo>] type. See the tutorial in the documentation for more info.

To use **EditorNode3DGizmoPlugin**, register it using the [EditorPlugin.add_node_3d_gizmo_plugin()<class_EditorPlugin_method_add_node_3d_gizmo_plugin>] method first.


## Tutorials

- [../tutorials/plugins/editor/3d_gizmos](Node3D gizmo plugins .md)


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`_begin_handle_action<class_EditorNode3DGizmoPlugin_private_method__begin_handle_action>`\ (\ gizmo\: :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`, handle_id\: :ref:`int<class_int>`, secondary\: :ref:`bool<class_bool>`\ ) |virtual|                                                                                           |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`_can_be_hidden<class_EditorNode3DGizmoPlugin_private_method__can_be_hidden>`\ (\ ) |virtual| |const|                                                                                                                                                                                                                                  |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`_commit_handle<class_EditorNode3DGizmoPlugin_private_method__commit_handle>`\ (\ gizmo\: :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`, handle_id\: :ref:`int<class_int>`, secondary\: :ref:`bool<class_bool>`, restore\: :ref:`Variant<class_Variant>`, cancel\: :ref:`bool<class_bool>`\ ) |virtual|                            |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`_commit_subgizmos<class_EditorNode3DGizmoPlugin_private_method__commit_subgizmos>`\ (\ gizmo\: :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`, ids\: :ref:`PackedInt32Array<class_PackedInt32Array>`, restores\: :ref:`Array<class_Array>`\[:ref:`Transform3D<class_Transform3D>`\], cancel\: :ref:`bool<class_bool>`\ ) |virtual| |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`   | :ref:`_create_gizmo<class_EditorNode3DGizmoPlugin_private_method__create_gizmo>`\ (\ for_node_3d\: :ref:`Node3D<class_Node3D>`\ ) |virtual| |const|                                                                                                                                                                                         |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                         | :ref:`_get_gizmo_name<class_EditorNode3DGizmoPlugin_private_method__get_gizmo_name>`\ (\ ) |virtual| |const|                                                                                                                                                                                                                                |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                         | :ref:`_get_handle_name<class_EditorNode3DGizmoPlugin_private_method__get_handle_name>`\ (\ gizmo\: :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`, handle_id\: :ref:`int<class_int>`, secondary\: :ref:`bool<class_bool>`\ ) |virtual| |const|                                                                                           |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                       | :ref:`_get_handle_value<class_EditorNode3DGizmoPlugin_private_method__get_handle_value>`\ (\ gizmo\: :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`, handle_id\: :ref:`int<class_int>`, secondary\: :ref:`bool<class_bool>`\ ) |virtual| |const|                                                                                         |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`_get_priority<class_EditorNode3DGizmoPlugin_private_method__get_priority>`\ (\ ) |virtual| |const|                                                                                                                                                                                                                                    |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`               | :ref:`_get_subgizmo_transform<class_EditorNode3DGizmoPlugin_private_method__get_subgizmo_transform>`\ (\ gizmo\: :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`, subgizmo_id\: :ref:`int<class_int>`\ ) |virtual| |const|                                                                                                                |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`_has_gizmo<class_EditorNode3DGizmoPlugin_private_method__has_gizmo>`\ (\ for_node_3d\: :ref:`Node3D<class_Node3D>`\ ) |virtual| |const|                                                                                                                                                                                               |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`_is_handle_highlighted<class_EditorNode3DGizmoPlugin_private_method__is_handle_highlighted>`\ (\ gizmo\: :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`, handle_id\: :ref:`int<class_int>`, secondary\: :ref:`bool<class_bool>`\ ) |virtual| |const|                                                                               |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`_is_selectable_when_hidden<class_EditorNode3DGizmoPlugin_private_method__is_selectable_when_hidden>`\ (\ ) |virtual| |const|                                                                                                                                                                                                          |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`_redraw<class_EditorNode3DGizmoPlugin_private_method__redraw>`\ (\ gizmo\: :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`\ ) |virtual|                                                                                                                                                                                             |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`_set_handle<class_EditorNode3DGizmoPlugin_private_method__set_handle>`\ (\ gizmo\: :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`, handle_id\: :ref:`int<class_int>`, secondary\: :ref:`bool<class_bool>`, camera\: :ref:`Camera3D<class_Camera3D>`, screen_pos\: :ref:`Vector2<class_Vector2>`\ ) |virtual|                       |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`_set_subgizmo_transform<class_EditorNode3DGizmoPlugin_private_method__set_subgizmo_transform>`\ (\ gizmo\: :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`, subgizmo_id\: :ref:`int<class_int>`, transform\: :ref:`Transform3D<class_Transform3D>`\ ) |virtual|                                                                     |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`     | :ref:`_subgizmos_intersect_frustum<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_frustum>`\ (\ gizmo\: :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`, camera\: :ref:`Camera3D<class_Camera3D>`, frustum_planes\: :ref:`Array<class_Array>`\[:ref:`Plane<class_Plane>`\]\ ) |virtual| |const|                        |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`_subgizmos_intersect_ray<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_ray>`\ (\ gizmo\: :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>`, camera\: :ref:`Camera3D<class_Camera3D>`, screen_pos\: :ref:`Vector2<class_Vector2>`\ ) |virtual| |const|                                                             |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`add_material<class_EditorNode3DGizmoPlugin_method_add_material>`\ (\ name\: :ref:`String<class_String>`, material\: :ref:`StandardMaterial3D<class_StandardMaterial3D>`\ )                                                                                                                                                            |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`create_handle_material<class_EditorNode3DGizmoPlugin_method_create_handle_material>`\ (\ name\: :ref:`String<class_String>`, billboard\: :ref:`bool<class_bool>` = false, texture\: :ref:`Texture2D<class_Texture2D>` = null\ )                                                                                                       |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`create_icon_material<class_EditorNode3DGizmoPlugin_method_create_icon_material>`\ (\ name\: :ref:`String<class_String>`, texture\: :ref:`Texture2D<class_Texture2D>`, on_top\: :ref:`bool<class_bool>` = false, color\: :ref:`Color<class_Color>` = Color(1, 1, 1, 1)\ )                                                              |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`create_material<class_EditorNode3DGizmoPlugin_method_create_material>`\ (\ name\: :ref:`String<class_String>`, color\: :ref:`Color<class_Color>`, billboard\: :ref:`bool<class_bool>` = false, on_top\: :ref:`bool<class_bool>` = false, use_vertex_color\: :ref:`bool<class_bool>` = false\ )                                        |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StandardMaterial3D<class_StandardMaterial3D>` | :ref:`get_material<class_EditorNode3DGizmoPlugin_method_get_material>`\ (\ name\: :ref:`String<class_String>`, gizmo\: :ref:`EditorNode3DGizmo<class_EditorNode3DGizmo>` = null\ )                                                                                                                                                          |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **_begin_handle_action**\ (\ gizmo\: [EditorNode3DGizmo<class_EditorNode3DGizmo>], handle_id\: [int<class_int>], secondary\: [bool<class_bool>]\ ) |virtual| [🔗<class_EditorNode3DGizmoPlugin_private_method__begin_handle_action>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_can_be_hidden**\ (\ ) |virtual| |const| [🔗<class_EditorNode3DGizmoPlugin_private_method__can_be_hidden>]

Override this method to define whether the gizmos handled by this plugin can be hidden or not. Returns `true` if not overridden.


----



|void| **_commit_handle**\ (\ gizmo\: [EditorNode3DGizmo<class_EditorNode3DGizmo>], handle_id\: [int<class_int>], secondary\: [bool<class_bool>], restore\: [Variant<class_Variant>], cancel\: [bool<class_bool>]\ ) |virtual| [🔗<class_EditorNode3DGizmoPlugin_private_method__commit_handle>]

Override this method to commit a handle being edited (handles must have been previously added by [EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>] during [_redraw()<class_EditorNode3DGizmoPlugin_private_method__redraw>]). This usually means creating an [UndoRedo<class_UndoRedo>] action for the change, using the current handle value as "do" and the `restore` argument as "undo".

If the `cancel` argument is `true`, the `restore` value should be directly set, without any [UndoRedo<class_UndoRedo>] action.

The `secondary` argument is `true` when the committed handle is secondary (see [EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>] for more information).

Called for this plugin's active gizmos.


----



|void| **_commit_subgizmos**\ (\ gizmo\: [EditorNode3DGizmo<class_EditorNode3DGizmo>], ids\: [PackedInt32Array<class_PackedInt32Array>], restores\: [Array<class_Array>]\[[Transform3D<class_Transform3D>]\], cancel\: [bool<class_bool>]\ ) |virtual| [🔗<class_EditorNode3DGizmoPlugin_private_method__commit_subgizmos>]

Override this method to commit a group of subgizmos being edited (see [_subgizmos_intersect_ray()<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_ray>] and [_subgizmos_intersect_frustum()<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_frustum>]). This usually means creating an [UndoRedo<class_UndoRedo>] action for the change, using the current transforms as "do" and the `restores` transforms as "undo".

If the `cancel` argument is `true`, the `restores` transforms should be directly set, without any [UndoRedo<class_UndoRedo>] action. As with all subgizmo methods, transforms are given in local space respect to the gizmo's Node3D. Called for this plugin's active gizmos.


----



[EditorNode3DGizmo<class_EditorNode3DGizmo>] **_create_gizmo**\ (\ for_node_3d\: [Node3D<class_Node3D>]\ ) |virtual| |const| [🔗<class_EditorNode3DGizmoPlugin_private_method__create_gizmo>]

Override this method to return a custom [EditorNode3DGizmo<class_EditorNode3DGizmo>] for the 3D nodes of your choice, return `null` for the rest of nodes. See also [_has_gizmo()<class_EditorNode3DGizmoPlugin_private_method__has_gizmo>].


----



[String<class_String>] **_get_gizmo_name**\ (\ ) |virtual| |const| [🔗<class_EditorNode3DGizmoPlugin_private_method__get_gizmo_name>]

Override this method to provide the name that will appear in the gizmo visibility menu.


----



[String<class_String>] **_get_handle_name**\ (\ gizmo\: [EditorNode3DGizmo<class_EditorNode3DGizmo>], handle_id\: [int<class_int>], secondary\: [bool<class_bool>]\ ) |virtual| |const| [🔗<class_EditorNode3DGizmoPlugin_private_method__get_handle_name>]

Override this method to provide gizmo's handle names. The `secondary` argument is `true` when the requested handle is secondary (see [EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>] for more information). Called for this plugin's active gizmos.


----



[Variant<class_Variant>] **_get_handle_value**\ (\ gizmo\: [EditorNode3DGizmo<class_EditorNode3DGizmo>], handle_id\: [int<class_int>], secondary\: [bool<class_bool>]\ ) |virtual| |const| [🔗<class_EditorNode3DGizmoPlugin_private_method__get_handle_value>]

Override this method to return the current value of a handle. This value will be requested at the start of an edit and used as the `restore` argument in [_commit_handle()<class_EditorNode3DGizmoPlugin_private_method__commit_handle>].

The `secondary` argument is `true` when the requested handle is secondary (see [EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>] for more information).

Called for this plugin's active gizmos.


----



[int<class_int>] **_get_priority**\ (\ ) |virtual| |const| [🔗<class_EditorNode3DGizmoPlugin_private_method__get_priority>]

Override this method to set the gizmo's priority. Gizmos with higher priority will have precedence when processing inputs like handles or subgizmos selection.

All built-in editor gizmos return a priority of `-1`. If not overridden, this method will return `0`, which means custom gizmos will automatically get higher priority than built-in gizmos.


----



[Transform3D<class_Transform3D>] **_get_subgizmo_transform**\ (\ gizmo\: [EditorNode3DGizmo<class_EditorNode3DGizmo>], subgizmo_id\: [int<class_int>]\ ) |virtual| |const| [🔗<class_EditorNode3DGizmoPlugin_private_method__get_subgizmo_transform>]

Override this method to return the current transform of a subgizmo. As with all subgizmo methods, the transform should be in local space respect to the gizmo's Node3D. This transform will be requested at the start of an edit and used in the `restore` argument in [_commit_subgizmos()<class_EditorNode3DGizmoPlugin_private_method__commit_subgizmos>]. Called for this plugin's active gizmos.


----



[bool<class_bool>] **_has_gizmo**\ (\ for_node_3d\: [Node3D<class_Node3D>]\ ) |virtual| |const| [🔗<class_EditorNode3DGizmoPlugin_private_method__has_gizmo>]

Override this method to define which Node3D nodes have a gizmo from this plugin. Whenever a [Node3D<class_Node3D>] node is added to a scene this method is called, if it returns `true` the node gets a generic [EditorNode3DGizmo<class_EditorNode3DGizmo>] assigned and is added to this plugin's list of active gizmos.


----



[bool<class_bool>] **_is_handle_highlighted**\ (\ gizmo\: [EditorNode3DGizmo<class_EditorNode3DGizmo>], handle_id\: [int<class_int>], secondary\: [bool<class_bool>]\ ) |virtual| |const| [🔗<class_EditorNode3DGizmoPlugin_private_method__is_handle_highlighted>]

Override this method to return `true` whenever to given handle should be highlighted in the editor. The `secondary` argument is `true` when the requested handle is secondary (see [EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>] for more information). Called for this plugin's active gizmos.


----



[bool<class_bool>] **_is_selectable_when_hidden**\ (\ ) |virtual| |const| [🔗<class_EditorNode3DGizmoPlugin_private_method__is_selectable_when_hidden>]

Override this method to define whether Node3D with this gizmo should be selectable even when the gizmo is hidden.


----



|void| **_redraw**\ (\ gizmo\: [EditorNode3DGizmo<class_EditorNode3DGizmo>]\ ) |virtual| [🔗<class_EditorNode3DGizmoPlugin_private_method__redraw>]

Override this method to add all the gizmo elements whenever a gizmo update is requested. It's common to call [EditorNode3DGizmo.clear()<class_EditorNode3DGizmo_method_clear>] at the beginning of this method and then add visual elements depending on the node's properties.


----



|void| **_set_handle**\ (\ gizmo\: [EditorNode3DGizmo<class_EditorNode3DGizmo>], handle_id\: [int<class_int>], secondary\: [bool<class_bool>], camera\: [Camera3D<class_Camera3D>], screen_pos\: [Vector2<class_Vector2>]\ ) |virtual| [🔗<class_EditorNode3DGizmoPlugin_private_method__set_handle>]

Override this method to update the node's properties when the user drags a gizmo handle (previously added with [EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>]). The provided `screen_pos` is the mouse position in screen coordinates and the `camera` can be used to convert it to raycasts.

The `secondary` argument is `true` when the edited handle is secondary (see [EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>] for more information).

Called for this plugin's active gizmos.


----



|void| **_set_subgizmo_transform**\ (\ gizmo\: [EditorNode3DGizmo<class_EditorNode3DGizmo>], subgizmo_id\: [int<class_int>], transform\: [Transform3D<class_Transform3D>]\ ) |virtual| [🔗<class_EditorNode3DGizmoPlugin_private_method__set_subgizmo_transform>]

Override this method to update the node properties during subgizmo editing (see [_subgizmos_intersect_ray()<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_ray>] and [_subgizmos_intersect_frustum()<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_frustum>]). The `transform` is given in the Node3D's local coordinate system. Called for this plugin's active gizmos.


----



[PackedInt32Array<class_PackedInt32Array>] **_subgizmos_intersect_frustum**\ (\ gizmo\: [EditorNode3DGizmo<class_EditorNode3DGizmo>], camera\: [Camera3D<class_Camera3D>], frustum_planes\: [Array<class_Array>]\[[Plane<class_Plane>]\]\ ) |virtual| |const| [🔗<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_frustum>]

Override this method to allow selecting subgizmos using mouse drag box selection. Given a `camera` and `frustum_planes`, this method should return which subgizmos are contained within the frustums. The `frustum_planes` argument consists of an array with all the [Plane<class_Plane>]\ s that make up the selection frustum. The returned value should contain a list of unique subgizmo identifiers, these identifiers can have any non-negative value and will be used in other virtual methods like [_get_subgizmo_transform()<class_EditorNode3DGizmoPlugin_private_method__get_subgizmo_transform>] or [_commit_subgizmos()<class_EditorNode3DGizmoPlugin_private_method__commit_subgizmos>]. Called for this plugin's active gizmos.


----



[int<class_int>] **_subgizmos_intersect_ray**\ (\ gizmo\: [EditorNode3DGizmo<class_EditorNode3DGizmo>], camera\: [Camera3D<class_Camera3D>], screen_pos\: [Vector2<class_Vector2>]\ ) |virtual| |const| [🔗<class_EditorNode3DGizmoPlugin_private_method__subgizmos_intersect_ray>]

Override this method to allow selecting subgizmos using mouse clicks. Given a `camera` and a `screen_pos` in screen coordinates, this method should return which subgizmo should be selected. The returned value should be a unique subgizmo identifier, which can have any non-negative value and will be used in other virtual methods like [_get_subgizmo_transform()<class_EditorNode3DGizmoPlugin_private_method__get_subgizmo_transform>] or [_commit_subgizmos()<class_EditorNode3DGizmoPlugin_private_method__commit_subgizmos>]. Called for this plugin's active gizmos.


----



|void| **add_material**\ (\ name\: [String<class_String>], material\: [StandardMaterial3D<class_StandardMaterial3D>]\ ) [🔗<class_EditorNode3DGizmoPlugin_method_add_material>]

Adds a new material to the internal material list for the plugin. It can then be accessed with [get_material()<class_EditorNode3DGizmoPlugin_method_get_material>]. Should not be overridden.


----



|void| **create_handle_material**\ (\ name\: [String<class_String>], billboard\: [bool<class_bool>] = false, texture\: [Texture2D<class_Texture2D>] = null\ ) [🔗<class_EditorNode3DGizmoPlugin_method_create_handle_material>]

Creates a handle material with its variants (selected and/or editable) and adds them to the internal material list. They can then be accessed with [get_material()<class_EditorNode3DGizmoPlugin_method_get_material>] and used in [EditorNode3DGizmo.add_handles()<class_EditorNode3DGizmo_method_add_handles>]. Should not be overridden.

You can optionally provide a texture to use instead of the default icon.


----



|void| **create_icon_material**\ (\ name\: [String<class_String>], texture\: [Texture2D<class_Texture2D>], on_top\: [bool<class_bool>] = false, color\: [Color<class_Color>] = Color(1, 1, 1, 1)\ ) [🔗<class_EditorNode3DGizmoPlugin_method_create_icon_material>]

Creates an icon material with its variants (selected and/or editable) and adds them to the internal material list. They can then be accessed with [get_material()<class_EditorNode3DGizmoPlugin_method_get_material>] and used in [EditorNode3DGizmo.add_unscaled_billboard()<class_EditorNode3DGizmo_method_add_unscaled_billboard>]. Should not be overridden.


----



|void| **create_material**\ (\ name\: [String<class_String>], color\: [Color<class_Color>], billboard\: [bool<class_bool>] = false, on_top\: [bool<class_bool>] = false, use_vertex_color\: [bool<class_bool>] = false\ ) [🔗<class_EditorNode3DGizmoPlugin_method_create_material>]

Creates an unshaded material with its variants (selected and/or editable) and adds them to the internal material list. They can then be accessed with [get_material()<class_EditorNode3DGizmoPlugin_method_get_material>] and used in [EditorNode3DGizmo.add_mesh()<class_EditorNode3DGizmo_method_add_mesh>] and [EditorNode3DGizmo.add_lines()<class_EditorNode3DGizmo_method_add_lines>]. Should not be overridden.


----



[StandardMaterial3D<class_StandardMaterial3D>] **get_material**\ (\ name\: [String<class_String>], gizmo\: [EditorNode3DGizmo<class_EditorNode3DGizmo>] = null\ ) [🔗<class_EditorNode3DGizmoPlugin_method_get_material>]

Gets material from the internal list of materials. If an [EditorNode3DGizmo<class_EditorNode3DGizmo>] is provided, it will try to get the corresponding variant (selected and/or editable).

