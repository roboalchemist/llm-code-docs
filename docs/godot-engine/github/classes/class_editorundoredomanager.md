:github_url: hide



# EditorUndoRedoManager

**Inherits:** [Object<class_Object>]

Manages undo history of scenes opened in the editor.


## Description

**EditorUndoRedoManager** is a manager for [UndoRedo<class_UndoRedo>] objects associated with edited scenes. Each scene has its own undo history and **EditorUndoRedoManager** ensures that each action performed in the editor gets associated with a proper scene. For actions not related to scenes ([ProjectSettings<class_ProjectSettings>] edits, external resources, etc.), a separate global history is used.

The usage is mostly the same as [UndoRedo<class_UndoRedo>]. You create and commit actions and the manager automatically decides under-the-hood what scenes it belongs to. The scene is deduced based on the first operation in an action, using the object from the operation. The rules are as follows:

- If the object is a [Node<class_Node>], use the currently edited scene;

- If the object is a built-in resource, use the scene from its path;

- If the object is external resource or anything else, use global history.

This guessing can sometimes yield false results, so you can provide a custom context object when creating an action.

\ **EditorUndoRedoManager** is intended to be used by Godot editor plugins. You can obtain it using [EditorPlugin.get_undo_redo()<class_EditorPlugin_method_get_undo_redo>]. For non-editor uses or plugins that don't need to integrate with the editor's undo history, use [UndoRedo<class_UndoRedo>] instead.

The manager's API is mostly the same as in [UndoRedo<class_UndoRedo>], so you can refer to its documentation for more examples. The main difference is that **EditorUndoRedoManager** uses object + method name for actions, instead of [Callable<class_Callable>].


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`add_do_method<class_EditorUndoRedoManager_method_add_do_method>`\ (\ object\: :ref:`Object<class_Object>`, method\: :ref:`StringName<class_StringName>`, ...\ ) |vararg|                                                                                                                                                        |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`add_do_property<class_EditorUndoRedoManager_method_add_do_property>`\ (\ object\: :ref:`Object<class_Object>`, property\: :ref:`StringName<class_StringName>`, value\: :ref:`Variant<class_Variant>`\ )                                                                                                                         |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`add_do_reference<class_EditorUndoRedoManager_method_add_do_reference>`\ (\ object\: :ref:`Object<class_Object>`\ )                                                                                                                                                                                                              |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`add_undo_method<class_EditorUndoRedoManager_method_add_undo_method>`\ (\ object\: :ref:`Object<class_Object>`, method\: :ref:`StringName<class_StringName>`, ...\ ) |vararg|                                                                                                                                                    |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`add_undo_property<class_EditorUndoRedoManager_method_add_undo_property>`\ (\ object\: :ref:`Object<class_Object>`, property\: :ref:`StringName<class_StringName>`, value\: :ref:`Variant<class_Variant>`\ )                                                                                                                     |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`add_undo_reference<class_EditorUndoRedoManager_method_add_undo_reference>`\ (\ object\: :ref:`Object<class_Object>`\ )                                                                                                                                                                                                          |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`clear_history<class_EditorUndoRedoManager_method_clear_history>`\ (\ id\: :ref:`int<class_int>` = -99, increase_version\: :ref:`bool<class_bool>` = true\ )                                                                                                                                                                     |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`commit_action<class_EditorUndoRedoManager_method_commit_action>`\ (\ execute\: :ref:`bool<class_bool>` = true\ )                                                                                                                                                                                                                |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`create_action<class_EditorUndoRedoManager_method_create_action>`\ (\ name\: :ref:`String<class_String>`, merge_mode\: :ref:`MergeMode<enum_UndoRedo_MergeMode>` = 0, custom_context\: :ref:`Object<class_Object>` = null, backward_undo_ops\: :ref:`bool<class_bool>` = false, mark_unsaved\: :ref:`bool<class_bool>` = true\ ) |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`force_fixed_history<class_EditorUndoRedoManager_method_force_fixed_history>`\ (\ )                                                                                                                                                                                                                                              |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`UndoRedo<class_UndoRedo>` | :ref:`get_history_undo_redo<class_EditorUndoRedoManager_method_get_history_undo_redo>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                      |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`get_object_history_id<class_EditorUndoRedoManager_method_get_object_history_id>`\ (\ object\: :ref:`Object<class_Object>`\ ) |const|                                                                                                                                                                                            |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`         | :ref:`is_committing_action<class_EditorUndoRedoManager_method_is_committing_action>`\ (\ ) |const|                                                                                                                                                                                                                                    |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**history_changed**\ (\ ) [🔗<class_EditorUndoRedoManager_signal_history_changed>]

Emitted when the list of actions in any history has changed, either when an action is committed or a history is cleared.


----



**version_changed**\ (\ ) [🔗<class_EditorUndoRedoManager_signal_version_changed>]

Emitted when the version of any history has changed as a result of undo or redo call.


----


## Enumerations



enum **SpecialHistory**: [🔗<enum_EditorUndoRedoManager_SpecialHistory>]



[SpecialHistory<enum_EditorUndoRedoManager_SpecialHistory>] **GLOBAL_HISTORY** = `0`

Global history not associated with any scene, but with external resources etc.



[SpecialHistory<enum_EditorUndoRedoManager_SpecialHistory>] **REMOTE_HISTORY** = `-9`

History associated with remote inspector. Used when live editing a running project.



[SpecialHistory<enum_EditorUndoRedoManager_SpecialHistory>] **INVALID_HISTORY** = `-99`

Invalid "null" history. It's a special value, not associated with any object.


----


## Method Descriptions



|void| **add_do_method**\ (\ object\: [Object<class_Object>], method\: [StringName<class_StringName>], ...\ ) |vararg| [🔗<class_EditorUndoRedoManager_method_add_do_method>]

Register a method that will be called when the action is committed (i.e. the "do" action).

If this is the first operation, the `object` will be used to deduce target undo history.


----



|void| **add_do_property**\ (\ object\: [Object<class_Object>], property\: [StringName<class_StringName>], value\: [Variant<class_Variant>]\ ) [🔗<class_EditorUndoRedoManager_method_add_do_property>]

Register a property value change for "do".

If this is the first operation, the `object` will be used to deduce target undo history.


----



|void| **add_do_reference**\ (\ object\: [Object<class_Object>]\ ) [🔗<class_EditorUndoRedoManager_method_add_do_reference>]

Register a reference for "do" that will be erased if the "do" history is lost. This is useful mostly for new nodes created for the "do" call. Do not use for resources.


----



|void| **add_undo_method**\ (\ object\: [Object<class_Object>], method\: [StringName<class_StringName>], ...\ ) |vararg| [🔗<class_EditorUndoRedoManager_method_add_undo_method>]

Register a method that will be called when the action is undone (i.e. the "undo" action).

If this is the first operation, the `object` will be used to deduce target undo history.


----



|void| **add_undo_property**\ (\ object\: [Object<class_Object>], property\: [StringName<class_StringName>], value\: [Variant<class_Variant>]\ ) [🔗<class_EditorUndoRedoManager_method_add_undo_property>]

Register a property value change for "undo".

If this is the first operation, the `object` will be used to deduce target undo history.


----



|void| **add_undo_reference**\ (\ object\: [Object<class_Object>]\ ) [🔗<class_EditorUndoRedoManager_method_add_undo_reference>]

Register a reference for "undo" that will be erased if the "undo" history is lost. This is useful mostly for nodes removed with the "do" call (not the "undo" call!).


----



|void| **clear_history**\ (\ id\: [int<class_int>] = -99, increase_version\: [bool<class_bool>] = true\ ) [🔗<class_EditorUndoRedoManager_method_clear_history>]

Clears the given undo history. You can clear history for a specific scene, global history, or for all histories at once (except [REMOTE_HISTORY<class_EditorUndoRedoManager_constant_REMOTE_HISTORY>]) if `id` is [INVALID_HISTORY<class_EditorUndoRedoManager_constant_INVALID_HISTORY>].

If `increase_version` is `true`, the undo history version will be increased, marking it as unsaved. Useful for operations that modify the scene, but don't support undo.

::

    var scene_root = EditorInterface.get_edited_scene_root()
    var undo_redo = EditorInterface.get_editor_undo_redo()
    undo_redo.clear_history(undo_redo.get_object_history_id(scene_root))

\ **Note:** If you want to mark an edited scene as unsaved without clearing its history, use [EditorInterface.mark_scene_as_unsaved()<class_EditorInterface_method_mark_scene_as_unsaved>] instead.


----



|void| **commit_action**\ (\ execute\: [bool<class_bool>] = true\ ) [🔗<class_EditorUndoRedoManager_method_commit_action>]

Commits the action. If `execute` is `true` (default), all "do" methods/properties are called/set when this function is called.


----



|void| **create_action**\ (\ name\: [String<class_String>], merge_mode\: [MergeMode<enum_UndoRedo_MergeMode>] = 0, custom_context\: [Object<class_Object>] = null, backward_undo_ops\: [bool<class_bool>] = false, mark_unsaved\: [bool<class_bool>] = true\ ) [🔗<class_EditorUndoRedoManager_method_create_action>]

Create a new action. After this is called, do all your calls to [add_do_method()<class_EditorUndoRedoManager_method_add_do_method>], [add_undo_method()<class_EditorUndoRedoManager_method_add_undo_method>], [add_do_property()<class_EditorUndoRedoManager_method_add_do_property>], and [add_undo_property()<class_EditorUndoRedoManager_method_add_undo_property>], then commit the action with [commit_action()<class_EditorUndoRedoManager_method_commit_action>].

The way actions are merged is dictated by the `merge_mode` argument.

If `custom_context` object is provided, it will be used for deducing target history (instead of using the first operation).

The way undo operation are ordered in actions is dictated by `backward_undo_ops`. When `backward_undo_ops` is `false` undo option are ordered in the same order they were added. Which means the first operation to be added will be the first to be undone.

If `mark_unsaved` is `false`, the action will not mark the history as unsaved. This is useful for example for actions that change a selection, or a setting that will be saved automatically. Otherwise, this should be left to `true` if the action requires saving by the user or if it can cause data loss when left unsaved.


----



|void| **force_fixed_history**\ (\ ) [🔗<class_EditorUndoRedoManager_method_force_fixed_history>]

Forces the next operation (e.g. [add_do_method()<class_EditorUndoRedoManager_method_add_do_method>]) to use the action's history rather than guessing it from the object. This is sometimes needed when a history can't be correctly determined, like for a nested resource that doesn't have a path yet.

This method should only be used when absolutely necessary, otherwise it might cause invalid history state. For most of complex cases, the `custom_context` parameter of [create_action()<class_EditorUndoRedoManager_method_create_action>] is sufficient.


----



[UndoRedo<class_UndoRedo>] **get_history_undo_redo**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_EditorUndoRedoManager_method_get_history_undo_redo>]

Returns the [UndoRedo<class_UndoRedo>] object associated with the given history `id`.

\ `id` above `0` are mapped to the opened scene tabs (but it doesn't match their order). `id` of `0` or lower have special meaning (see [SpecialHistory<enum_EditorUndoRedoManager_SpecialHistory>]).

Best used with [get_object_history_id()<class_EditorUndoRedoManager_method_get_object_history_id>]. This method is only provided in case you need some more advanced methods of [UndoRedo<class_UndoRedo>] (but keep in mind that directly operating on the [UndoRedo<class_UndoRedo>] object might affect editor's stability).


----



[int<class_int>] **get_object_history_id**\ (\ object\: [Object<class_Object>]\ ) |const| [🔗<class_EditorUndoRedoManager_method_get_object_history_id>]

Returns the history ID deduced from the given `object`. It can be used with [get_history_undo_redo()<class_EditorUndoRedoManager_method_get_history_undo_redo>].


----



[bool<class_bool>] **is_committing_action**\ (\ ) |const| [🔗<class_EditorUndoRedoManager_method_is_committing_action>]

Returns `true` if the **EditorUndoRedoManager** is currently committing the action, i.e. running its "do" method or property change (see [commit_action()<class_EditorUndoRedoManager_method_commit_action>]).

