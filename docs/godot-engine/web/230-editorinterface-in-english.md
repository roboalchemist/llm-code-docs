# EditorInterface in English

# EditorInterface

Inherits:Object
Godot editor's interface.

## Description

EditorInterfacegives you control over Godot editor's window. It allows customizing the window, saving and (re-)loading scenes, rendering mesh previews, inspecting and editing resources and objects, and provides access toEditorSettings,EditorFileSystem,EditorResourcePreview,ScriptEditor, the editor viewport, and information about scenes.
Note:This class shouldn't be instantiated directly. Instead, access the singleton directly by its name.

```
var editor_settings = EditorInterface.get_editor_settings()
```

```
// In C# you can access it via the static Singleton property.
EditorSettings settings = EditorInterface.Singleton.GetEditorSettings();
```

## Properties

| bool | distraction_free_mode |
|---|---|
| bool | movie_maker_enabled |

bool
distraction_free_mode
bool
movie_maker_enabled

## Methods

| void | add_root_node(node:Node) |
|---|---|
| Error | close_scene() |
| void | edit_node(node:Node) |
| void | edit_resource(resource:Resource) |
| void | edit_script(script:Script, line:int= -1, column:int= 0, grab_focus:bool= true) |
| Control | get_base_control()const |
| EditorCommandPalette | get_command_palette()const |
| String | get_current_directory()const |
| String | get_current_feature_profile()const |
| String | get_current_path()const |
| Node | get_edited_scene_root()const |
| String | get_editor_language()const |
| VBoxContainer | get_editor_main_screen()const |
| EditorPaths | get_editor_paths()const |
| float | get_editor_scale()const |
| EditorSettings | get_editor_settings()const |
| Theme | get_editor_theme()const |
| EditorToaster | get_editor_toaster()const |
| EditorUndoRedoManager | get_editor_undo_redo()const |
| SubViewport | get_editor_viewport_2d()const |
| SubViewport | get_editor_viewport_3d(idx:int= 0)const |
| FileSystemDock | get_file_system_dock()const |
| EditorInspector | get_inspector()const |
| float | get_node_3d_rotate_snap()const |
| float | get_node_3d_scale_snap()const |
| float | get_node_3d_translate_snap()const |
| Array[Node] | get_open_scene_roots()const |
| PackedStringArray | get_open_scenes()const |
| String | get_playing_scene()const |
| EditorFileSystem | get_resource_filesystem()const |
| EditorResourcePreview | get_resource_previewer()const |
| ScriptEditor | get_script_editor()const |
| PackedStringArray | get_selected_paths()const |
| EditorSelection | get_selection()const |
| void | inspect_object(object:Object, for_property:String= "", inspector_only:bool= false) |
| bool | is_multi_window_enabled()const |
| bool | is_node_3d_snap_enabled()const |
| bool | is_object_edited(object:Object)const |
| bool | is_playing_scene()const |
| bool | is_plugin_enabled(plugin:String)const |
| Array[Texture2D] | make_mesh_previews(meshes:Array[Mesh], preview_size:int) |
| void | mark_scene_as_unsaved() |
| void | open_scene_from_path(scene_filepath:String, set_inherited:bool= false) |
| void | play_current_scene() |
| void | play_custom_scene(scene_filepath:String) |
| void | play_main_scene() |
| void | popup_create_dialog(callback:Callable, base_type:StringName= "", current_type:String= "", dialog_title:String= "", type_blocklist:Array[StringName] = []) |
| void | popup_dialog(dialog:Window, rect:Rect2i= Rect2i(0, 0, 0, 0)) |
| void | popup_dialog_centered(dialog:Window, minsize:Vector2i= Vector2i(0, 0)) |
| void | popup_dialog_centered_clamped(dialog:Window, minsize:Vector2i= Vector2i(0, 0), fallback_ratio:float= 0.75) |
| void | popup_dialog_centered_ratio(dialog:Window, ratio:float= 0.8) |
| void | popup_method_selector(object:Object, callback:Callable, current_value:String= "") |
| void | popup_node_selector(callback:Callable, valid_types:Array[StringName] = [], current_value:Node= null) |
| void | popup_property_selector(object:Object, callback:Callable, type_filter:PackedInt32Array= PackedInt32Array(), current_value:String= "") |
| void | popup_quick_open(callback:Callable, base_types:Array[StringName] = []) |
| void | reload_scene_from_path(scene_filepath:String) |
| void | restart_editor(save:bool= true) |
| void | save_all_scenes() |
| Error | save_scene() |
| void | save_scene_as(path:String, with_preview:bool= true) |
| void | select_file(file:String) |
| void | set_current_feature_profile(profile_name:String) |
| void | set_main_screen_editor(name:String) |
| void | set_object_edited(object:Object, edited:bool) |
| void | set_plugin_enabled(plugin:String, enabled:bool) |
| void | stop_playing_scene() |

void
add_root_node(node:Node)
Error
close_scene()
void
edit_node(node:Node)
void
edit_resource(resource:Resource)
void
edit_script(script:Script, line:int= -1, column:int= 0, grab_focus:bool= true)
Control
get_base_control()const
EditorCommandPalette
get_command_palette()const
String
get_current_directory()const
String
get_current_feature_profile()const
String
get_current_path()const
Node
get_edited_scene_root()const
String
get_editor_language()const
VBoxContainer
get_editor_main_screen()const
EditorPaths
get_editor_paths()const
float
get_editor_scale()const
EditorSettings
get_editor_settings()const
Theme
get_editor_theme()const
EditorToaster
get_editor_toaster()const
EditorUndoRedoManager
get_editor_undo_redo()const
SubViewport
get_editor_viewport_2d()const
SubViewport
get_editor_viewport_3d(idx:int= 0)const
FileSystemDock
get_file_system_dock()const
EditorInspector
get_inspector()const
float
get_node_3d_rotate_snap()const
float
get_node_3d_scale_snap()const
float
get_node_3d_translate_snap()const
Array[Node]
get_open_scene_roots()const
PackedStringArray
get_open_scenes()const
String
get_playing_scene()const
EditorFileSystem
get_resource_filesystem()const
EditorResourcePreview
get_resource_previewer()const
ScriptEditor
get_script_editor()const
PackedStringArray
get_selected_paths()const
EditorSelection
get_selection()const
void
inspect_object(object:Object, for_property:String= "", inspector_only:bool= false)
bool
is_multi_window_enabled()const
bool
is_node_3d_snap_enabled()const
bool
is_object_edited(object:Object)const
bool
is_playing_scene()const
bool
is_plugin_enabled(plugin:String)const
Array[Texture2D]
make_mesh_previews(meshes:Array[Mesh], preview_size:int)
void
mark_scene_as_unsaved()
void
open_scene_from_path(scene_filepath:String, set_inherited:bool= false)
void
play_current_scene()
void
play_custom_scene(scene_filepath:String)
void
play_main_scene()
void
popup_create_dialog(callback:Callable, base_type:StringName= "", current_type:String= "", dialog_title:String= "", type_blocklist:Array[StringName] = [])
void
popup_dialog(dialog:Window, rect:Rect2i= Rect2i(0, 0, 0, 0))
void
popup_dialog_centered(dialog:Window, minsize:Vector2i= Vector2i(0, 0))
void
popup_dialog_centered_clamped(dialog:Window, minsize:Vector2i= Vector2i(0, 0), fallback_ratio:float= 0.75)
void
popup_dialog_centered_ratio(dialog:Window, ratio:float= 0.8)
void
popup_method_selector(object:Object, callback:Callable, current_value:String= "")
void
popup_node_selector(callback:Callable, valid_types:Array[StringName] = [], current_value:Node= null)
void
popup_property_selector(object:Object, callback:Callable, type_filter:PackedInt32Array= PackedInt32Array(), current_value:String= "")
void
popup_quick_open(callback:Callable, base_types:Array[StringName] = [])
void
reload_scene_from_path(scene_filepath:String)
void
restart_editor(save:bool= true)
void
save_all_scenes()
Error
save_scene()
void
save_scene_as(path:String, with_preview:bool= true)
void
select_file(file:String)
void
set_current_feature_profile(profile_name:String)
void
set_main_screen_editor(name:String)
void
set_object_edited(object:Object, edited:bool)
void
set_plugin_enabled(plugin:String, enabled:bool)
void
stop_playing_scene()

## Property Descriptions

booldistraction_free_mode🔗

- voidset_distraction_free_mode(value:bool)
voidset_distraction_free_mode(value:bool)
- boolis_distraction_free_mode_enabled()
boolis_distraction_free_mode_enabled()
Iftrue, enables distraction-free mode which hides side docks to increase the space available for the main view.
boolmovie_maker_enabled🔗
- voidset_movie_maker_enabled(value:bool)
voidset_movie_maker_enabled(value:bool)
- boolis_movie_maker_enabled()
boolis_movie_maker_enabled()
Iftrue, the Movie Maker mode is enabled in the editor. SeeMovieWriterfor more information.

## Method Descriptions

voidadd_root_node(node:Node)🔗
Makesnoderoot of the currently opened scene. Only works if the scene is empty. If thenodeis a scene instance, an inheriting scene will be created.
Errorclose_scene()🔗
Closes the currently active scene, discarding any pending changes in the process. Returns@GlobalScope.OKon success or@GlobalScope.ERR_DOES_NOT_EXISTif there is no scene to close.
voidedit_node(node:Node)🔗
Edits the givenNode. The node will be also selected if it's inside the scene tree.
voidedit_resource(resource:Resource)🔗
Edits the givenResource. If the resource is aScriptyou can also edit it withedit_script()to specify the line and column position.
voidedit_script(script:Script, line:int= -1, column:int= 0, grab_focus:bool= true)🔗
Edits the givenScript. The line and column on which to open the script can also be specified. The script will be open with the user-configured editor for the script's language which may be an external editor.
Controlget_base_control()const🔗
Returns the main container of Godot editor's window. For example, you can use it to retrieve the size of the container and place your controls accordingly.
Warning:Removing and freeing this node will render the editor useless and may cause a crash.
EditorCommandPaletteget_command_palette()const🔗
Returns the editor'sEditorCommandPaletteinstance.
Warning:Removing and freeing this node will render a part of the editor useless and may cause a crash.
Stringget_current_directory()const🔗
Returns the current directory being viewed in theFileSystemDock. If a file is selected, its base directory will be returned usingString.get_base_dir()instead.
Stringget_current_feature_profile()const🔗
Returns the name of the currently activated feature profile. If the default profile is currently active, an empty string is returned instead.
In order to get a reference to theEditorFeatureProfile, you must load the feature profile usingEditorFeatureProfile.load_from_file().
Note:Feature profiles created via the user interface are loaded from thefeature_profilesdirectory, as a file with the.profileextension. The editor configuration folder can be found by usingEditorPaths.get_config_dir().
Stringget_current_path()const🔗
Returns the current path being viewed in theFileSystemDock.
Nodeget_edited_scene_root()const🔗
Returns the edited (current) scene's rootNode.
Stringget_editor_language()const🔗
Returns the language currently used for the editor interface.
VBoxContainerget_editor_main_screen()const🔗
Returns the editor control responsible for main screen plugins and tools. Use it with plugins that implementEditorPlugin._has_main_screen().
Note:This node is aVBoxContainer, which means that if you add aControlchild to it, you need to set the child'sControl.size_flags_verticaltoControl.SIZE_EXPAND_FILLto make it use the full available space.
Warning:Removing and freeing this node will render a part of the editor useless and may cause a crash.
EditorPathsget_editor_paths()const🔗
Returns theEditorPathssingleton.
floatget_editor_scale()const🔗
Returns the actual scale of the editor UI (1.0being 100% scale). This can be used to adjust position and dimensions of the UI added by plugins.
Note:This value is set via theEditorSettings.interface/editor/display_scaleandEditorSettings.interface/editor/custom_display_scalesettings. The editor must be restarted for changes to be properly applied.
EditorSettingsget_editor_settings()const🔗
Returns the editor'sEditorSettingsinstance.
Themeget_editor_theme()const🔗
Returns the editor'sTheme.
Note:When creating custom editor UI, prefer accessing theme items directly from your GUI nodes using theget_theme_*methods.
EditorToasterget_editor_toaster()const🔗
Returns the editor'sEditorToaster.
EditorUndoRedoManagerget_editor_undo_redo()const🔗
Returns the editor'sEditorUndoRedoManager.
SubViewportget_editor_viewport_2d()const🔗
Returns the 2D editorSubViewport. It does not have a camera. Instead, the view transforms are done directly and can be accessed withViewport.global_canvas_transform.
SubViewportget_editor_viewport_3d(idx:int= 0)const🔗
Returns the specified 3D editorSubViewport, from0to3. The viewport can be used to access the active editor cameras withViewport.get_camera_3d().
FileSystemDockget_file_system_dock()const🔗
Returns the editor'sFileSystemDockinstance.
Warning:Removing and freeing this node will render a part of the editor useless and may cause a crash.
EditorInspectorget_inspector()const🔗
Returns the editor'sEditorInspectorinstance.
Warning:Removing and freeing this node will render a part of the editor useless and may cause a crash.
floatget_node_3d_rotate_snap()const🔗
Returns the amount of degrees the 3D editor's rotational snapping is set to.
floatget_node_3d_scale_snap()const🔗
Returns the amount of units the 3D editor's scale snapping is set to.
floatget_node_3d_translate_snap()const🔗
Returns the amount of units the 3D editor's translation snapping is set to.
Array[Node]get_open_scene_roots()const🔗
Returns an array with references to the root nodes of the currently opened scenes.
PackedStringArrayget_open_scenes()const🔗
Returns an array with the file paths of the currently opened scenes.
Stringget_playing_scene()const🔗
Returns the name of the scene that is being played. If no scene is currently being played, returns an empty string.
EditorFileSystemget_resource_filesystem()const🔗
Returns the editor'sEditorFileSysteminstance.
EditorResourcePreviewget_resource_previewer()const🔗
Returns the editor'sEditorResourcePreviewinstance.
ScriptEditorget_script_editor()const🔗
Returns the editor'sScriptEditorinstance.
Warning:Removing and freeing this node will render a part of the editor useless and may cause a crash.
PackedStringArrayget_selected_paths()const🔗
Returns an array containing the paths of the currently selected files (and directories) in theFileSystemDock.
EditorSelectionget_selection()const🔗
Returns the editor'sEditorSelectioninstance.
voidinspect_object(object:Object, for_property:String= "", inspector_only:bool= false)🔗
Shows the given property on the givenobjectin the editor's Inspector dock. Ifinspector_onlyistrue, plugins will not attempt to editobject.
boolis_multi_window_enabled()const🔗
Returnstrueif multiple window support is enabled in the editor. Multiple window support is enabled ifallof these statements are true:

- EditorSettings.interface/multi_window/enableistrue.
EditorSettings.interface/multi_window/enableistrue.
- EditorSettings.interface/editor/single_window_modeisfalse.
EditorSettings.interface/editor/single_window_modeisfalse.
- Viewport.gui_embed_subwindowsisfalse. This is forced totrueon platforms that don't support multiple windows such as Web, or when the--single-windowcommand line argumentis used.
Viewport.gui_embed_subwindowsisfalse. This is forced totrueon platforms that don't support multiple windows such as Web, or when the--single-windowcommand line argumentis used.
boolis_node_3d_snap_enabled()const🔗
Returnstrueif the 3D editor currently has snapping mode enabled, andfalseotherwise.
boolis_object_edited(object:Object)const🔗
Returnstrueif the object has been marked as edited throughset_object_edited().
boolis_playing_scene()const🔗
Returnstrueif a scene is currently being played,falseotherwise. Paused scenes are considered as being played.
boolis_plugin_enabled(plugin:String)const🔗
Returnstrueif the specifiedpluginis enabled. The plugin name is the same as its directory name.
Array[Texture2D]make_mesh_previews(meshes:Array[Mesh], preview_size:int)🔗
Returns mesh previews rendered at the given size as anArrayofTexture2Ds.
voidmark_scene_as_unsaved()🔗
Marks the current scene tab as unsaved.
voidopen_scene_from_path(scene_filepath:String, set_inherited:bool= false)🔗
Opens the scene at the given path. Ifset_inheritedistrue, creates a new inherited scene.
voidplay_current_scene()🔗
Plays the currently active scene.
voidplay_custom_scene(scene_filepath:String)🔗
Plays the scene specified by its filepath.
voidplay_main_scene()🔗
Plays the main scene.
voidpopup_create_dialog(callback:Callable, base_type:StringName= "", current_type:String= "", dialog_title:String= "", type_blocklist:Array[StringName] = [])🔗
Experimental:This method may be changed or removed in future versions.
Pops up an editor dialog for creating an object.
Thecallbackmust take a single argument of typeString, which will contain the type name of the selected object (or the script path of the type, if the type is created from a script), or be an empty string if no item is selected.
Thebase_typespecifies the base type of objects to display. For example, if you set this to "Resource", all types derived fromResourcewill display in the create dialog.
Thecurrent_typewill be passed in the search box of the create dialog, and the specified type can be immediately selected when the dialog pops up. If thecurrent_typeis not derived frombase_type, there will be no result of the type in the dialog.
Thedialog_titleallows you to define a custom title for the dialog. This is useful if you want to accurately hint the usage of the dialog. If thedialog_titleis an empty string, the dialog will use "Create New 'Base Type'" as the default title.
Thetype_blocklistcontains a list of type names, and the types in the blocklist will be hidden from the create dialog.
Note:Trying to list the base type in thetype_blocklistwill hide all types derived from the base type from the create dialog.
voidpopup_dialog(dialog:Window, rect:Rect2i= Rect2i(0, 0, 0, 0))🔗
Pops up thedialogin the editor UI withWindow.popup_exclusive(). The dialog must have no current parent, otherwise the method fails.
See alsoWindow.set_unparent_when_invisible().
voidpopup_dialog_centered(dialog:Window, minsize:Vector2i= Vector2i(0, 0))🔗
Pops up thedialogin the editor UI withWindow.popup_exclusive_centered(). The dialog must have no current parent, otherwise the method fails.
See alsoWindow.set_unparent_when_invisible().
voidpopup_dialog_centered_clamped(dialog:Window, minsize:Vector2i= Vector2i(0, 0), fallback_ratio:float= 0.75)🔗
Pops up thedialogin the editor UI withWindow.popup_exclusive_centered_clamped(). The dialog must have no current parent, otherwise the method fails.
See alsoWindow.set_unparent_when_invisible().
voidpopup_dialog_centered_ratio(dialog:Window, ratio:float= 0.8)🔗
Pops up thedialogin the editor UI withWindow.popup_exclusive_centered_ratio(). The dialog must have no current parent, otherwise the method fails.
See alsoWindow.set_unparent_when_invisible().
voidpopup_method_selector(object:Object, callback:Callable, current_value:String= "")🔗
Pops up an editor dialog for selecting a method fromobject. Thecallbackmust take a single argument of typeStringwhich will contain the name of the selected method or be empty if the dialog is canceled. Ifcurrent_valueis provided, the method will be selected automatically in the method list, if it exists.
voidpopup_node_selector(callback:Callable, valid_types:Array[StringName] = [], current_value:Node= null)🔗
Pops up an editor dialog for selecting aNodefrom the edited scene. Thecallbackmust take a single argument of typeNodePath. It is called on the selectedNodePathor the empty path^""if the dialog is canceled. Ifvalid_typesis provided, the dialog will only show Nodes that match one of the listed Node types. Ifcurrent_valueis provided, the Node will be automatically selected in the tree, if it exists.
Example:Display the node selection dialog as soon as this node is added to the tree for the first time:

```
func _ready():
    if Engine.is_editor_hint():
        EditorInterface.popup_node_selector(_on_node_selected, ["Button"])

func _on_node_selected(node_path):
    if node_path.is_empty():
        print("node selection canceled")
    else:
        print("selected ", node_path)
```

voidpopup_property_selector(object:Object, callback:Callable, type_filter:PackedInt32Array= PackedInt32Array(), current_value:String= "")🔗
Pops up an editor dialog for selecting properties fromobject. Thecallbackmust take a single argument of typeNodePath. It is called on the selected property path (seeNodePath.get_as_property_path()) or the empty path^""if the dialog is canceled. Iftype_filteris provided, the dialog will only show properties that match one of the listedVariant.Typevalues. Ifcurrent_valueis provided, the property will be selected automatically in the property list, if it exists.

```
func _ready():
    if Engine.is_editor_hint():
        EditorInterface.popup_property_selector(this, _on_property_selected, [TYPE_INT])

func _on_property_selected(property_path):
    if property_path.is_empty():
        print("property selection canceled")
    else:
        print("selected ", property_path)
```

voidpopup_quick_open(callback:Callable, base_types:Array[StringName] = [])🔗
Pops up an editor dialog for quick selecting a resource file. Thecallbackmust take a single argument of typeStringwhich will contain the path of the selected resource or be empty if the dialog is canceled. Ifbase_typesis provided, the dialog will only show resources that match these types. Only types deriving fromResourceare supported.
voidreload_scene_from_path(scene_filepath:String)🔗
Reloads the scene at the given path.
voidrestart_editor(save:bool= true)🔗
Restarts the editor. This closes the editor and then opens the same project. Ifsaveistrue, the project will be saved before restarting.
voidsave_all_scenes()🔗
Saves all opened scenes in the editor.
Errorsave_scene()🔗
Saves the currently active scene. Returns either@GlobalScope.OKor@GlobalScope.ERR_CANT_CREATE.
voidsave_scene_as(path:String, with_preview:bool= true)🔗
Saves the currently active scene as a file atpath.
voidselect_file(file:String)🔗
Selects the file, with the path provided byfile, in the FileSystem dock.
voidset_current_feature_profile(profile_name:String)🔗
Selects and activates the specified feature profile with the givenprofile_name. Setprofile_nameto an empty string to reset to the default feature profile.
A feature profile can be created programmatically using theEditorFeatureProfileclass.
Note:The feature profile that gets activated must be located in thefeature_profilesdirectory, as a file with the.profileextension. If a profile could not be found, an error occurs. The editor configuration folder can be found by usingEditorPaths.get_config_dir().
voidset_main_screen_editor(name:String)🔗
Sets the editor's current main screen to the one specified inname.namemust match the title of the tab in question exactly (e.g.2D,3D,Script,Game, orAssetLibfor default tabs).
voidset_object_edited(object:Object, edited:bool)🔗
Ifeditedistrue, the object is marked as edited.
Note:This is primarily used by the editor forResourcebased objects to track their modified state. For example, any changes to an open scene, a resource in the inspector, or an edited script will cause this method to be called withtrue. Saving the scene, script, or resource resets the edited state by calling this method withfalse.
Note:Each call to this method increments the object's edited version. This is used to track changes in the editor and to trigger when thumbnails should be regenerated for resources.
voidset_plugin_enabled(plugin:String, enabled:bool)🔗
Sets the enabled status of a plugin. The plugin name is the same as its directory name.
voidstop_playing_scene()🔗
Stops the scene that is currently playing.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
