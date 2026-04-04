# EditorUndoRedoManager

# EditorUndoRedoManager
Inherits:Object
Manages undo history of scenes opened in the editor.

## Description
EditorUndoRedoManageris a manager forUndoRedoobjects associated with edited scenes. Each scene has its own undo history andEditorUndoRedoManagerensures that each action performed in the editor gets associated with a proper scene. For actions not related to scenes (ProjectSettingsedits, external resources, etc.), a separate global history is used.
The usage is mostly the same asUndoRedo. You create and commit actions and the manager automatically decides under-the-hood what scenes it belongs to. The scene is deduced based on the first operation in an action, using the object from the operation. The rules are as follows:
- If the object is aNode, use the currently edited scene;
If the object is aNode, use the currently edited scene;
- If the object is a built-in resource, use the scene from its path;
If the object is a built-in resource, use the scene from its path;
- If the object is external resource or anything else, use global history.
If the object is external resource or anything else, use global history.
This guessing can sometimes yield false results, so you can provide a custom context object when creating an action.
EditorUndoRedoManageris intended to be used by Godot editor plugins. You can obtain it usingEditorPlugin.get_undo_redo(). For non-editor uses or plugins that don't need to integrate with the editor's undo history, useUndoRedoinstead.
The manager's API is mostly the same as inUndoRedo, so you can refer to its documentation for more examples. The main difference is thatEditorUndoRedoManageruses object + method name for actions, instead ofCallable.

## Methods

| void | add_do_method(object:Object, method:StringName, ...)vararg |
|---|---|
| void | add_do_property(object:Object, property:StringName, value:Variant) |
| void | add_do_reference(object:Object) |
| void | add_undo_method(object:Object, method:StringName, ...)vararg |
| void | add_undo_property(object:Object, property:StringName, value:Variant) |
| void | add_undo_reference(object:Object) |
| void | clear_history(id:int= -99, increase_version:bool= true) |
| void | commit_action(execute:bool= true) |
| void | create_action(name:String, merge_mode:MergeMode= 0, custom_context:Object= null, backward_undo_ops:bool= false, mark_unsaved:bool= true) |
| void | force_fixed_history() |
| UndoRedo | get_history_undo_redo(id:int)const |
| int | get_object_history_id(object:Object)const |
| bool | is_committing_action()const |

void
add_do_method(object:Object, method:StringName, ...)vararg
void
add_do_property(object:Object, property:StringName, value:Variant)
void
add_do_reference(object:Object)
void
add_undo_method(object:Object, method:StringName, ...)vararg
void
add_undo_property(object:Object, property:StringName, value:Variant)
void
add_undo_reference(object:Object)
void
clear_history(id:int= -99, increase_version:bool= true)
void
commit_action(execute:bool= true)
void
create_action(name:String, merge_mode:MergeMode= 0, custom_context:Object= null, backward_undo_ops:bool= false, mark_unsaved:bool= true)
void
force_fixed_history()
UndoRedo
get_history_undo_redo(id:int)const
get_object_history_id(object:Object)const
bool
is_committing_action()const

## Signals
history_changed()🔗
Emitted when the list of actions in any history has changed, either when an action is committed or a history is cleared.
version_changed()🔗
Emitted when the version of any history has changed as a result of undo or redo call.

## Enumerations
enumSpecialHistory:🔗
SpecialHistoryGLOBAL_HISTORY=0
Global history not associated with any scene, but with external resources etc.
SpecialHistoryREMOTE_HISTORY=-9
History associated with remote inspector. Used when live editing a running project.
SpecialHistoryINVALID_HISTORY=-99
Invalid "null" history. It's a special value, not associated with any object.

## Method Descriptions
voidadd_do_method(object:Object, method:StringName, ...)vararg🔗
Register a method that will be called when the action is committed (i.e. the "do" action).
If this is the first operation, theobjectwill be used to deduce target undo history.
voidadd_do_property(object:Object, property:StringName, value:Variant)🔗
Register a property value change for "do".
If this is the first operation, theobjectwill be used to deduce target undo history.
voidadd_do_reference(object:Object)🔗
Register a reference for "do" that will be erased if the "do" history is lost. This is useful mostly for new nodes created for the "do" call. Do not use for resources.
voidadd_undo_method(object:Object, method:StringName, ...)vararg🔗
Register a method that will be called when the action is undone (i.e. the "undo" action).
If this is the first operation, theobjectwill be used to deduce target undo history.
voidadd_undo_property(object:Object, property:StringName, value:Variant)🔗
Register a property value change for "undo".
If this is the first operation, theobjectwill be used to deduce target undo history.
voidadd_undo_reference(object:Object)🔗
Register a reference for "undo" that will be erased if the "undo" history is lost. This is useful mostly for nodes removed with the "do" call (not the "undo" call!).
voidclear_history(id:int= -99, increase_version:bool= true)🔗
Clears the given undo history. You can clear history for a specific scene, global history, or for all histories at once (exceptREMOTE_HISTORY) ifidisINVALID_HISTORY.
Ifincrease_versionistrue, the undo history version will be increased, marking it as unsaved. Useful for operations that modify the scene, but don't support undo.
```
var scene_root = EditorInterface.get_edited_scene_root()
var undo_redo = EditorInterface.get_editor_undo_redo()
undo_redo.clear_history(undo_redo.get_object_history_id(scene_root))
```
Note:If you want to mark an edited scene as unsaved without clearing its history, useEditorInterface.mark_scene_as_unsaved()instead.
voidcommit_action(execute:bool= true)🔗
Commits the action. Ifexecuteistrue(default), all "do" methods/properties are called/set when this function is called.
voidcreate_action(name:String, merge_mode:MergeMode= 0, custom_context:Object= null, backward_undo_ops:bool= false, mark_unsaved:bool= true)🔗
Create a new action. After this is called, do all your calls toadd_do_method(),add_undo_method(),add_do_property(), andadd_undo_property(), then commit the action withcommit_action().
The way actions are merged is dictated by themerge_modeargument.
Ifcustom_contextobject is provided, it will be used for deducing target history (instead of using the first operation).
The way undo operation are ordered in actions is dictated bybackward_undo_ops. Whenbackward_undo_opsisfalseundo option are ordered in the same order they were added. Which means the first operation to be added will be the first to be undone.
Ifmark_unsavedisfalse, the action will not mark the history as unsaved. This is useful for example for actions that change a selection, or a setting that will be saved automatically. Otherwise, this should be left totrueif the action requires saving by the user or if it can cause data loss when left unsaved.
voidforce_fixed_history()🔗
Forces the next operation (e.g.add_do_method()) to use the action's history rather than guessing it from the object. This is sometimes needed when a history can't be correctly determined, like for a nested resource that doesn't have a path yet.
This method should only be used when absolutely necessary, otherwise it might cause invalid history state. For most of complex cases, thecustom_contextparameter ofcreate_action()is sufficient.
UndoRedoget_history_undo_redo(id:int)const🔗
Returns theUndoRedoobject associated with the given historyid.
idabove0are mapped to the opened scene tabs (but it doesn't match their order).idof0or lower have special meaning (seeSpecialHistory).
Best used withget_object_history_id(). This method is only provided in case you need some more advanced methods ofUndoRedo(but keep in mind that directly operating on theUndoRedoobject might affect editor's stability).
intget_object_history_id(object:Object)const🔗
Returns the history ID deduced from the givenobject. It can be used withget_history_undo_redo().
boolis_committing_action()const🔗
Returnstrueif theEditorUndoRedoManageris currently committing the action, i.e. running its "do" method or property change (seecommit_action()).

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.