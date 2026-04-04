# SceneTree in English

# SceneTree

Inherits:MainLoop<Object
Manages the game loop via a hierarchy of nodes.

## Description

As one of the most important classes, theSceneTreemanages the hierarchy of nodes in a scene, as well as scenes themselves. Nodes can be added, fetched and removed. The whole scene tree (and thus the current scene) can be paused. Scenes can be loaded, switched and reloaded.
You can also use theSceneTreeto organize your nodes intogroups: every node can be added to as many groups as you want to create, e.g. an "enemy" group. You can then iterate these groups or even call methods and set properties on all the nodes belonging to any given group.
SceneTreeis the defaultMainLoopimplementation used by the engine, and is thus in charge of the game loop.

## Tutorials

- SceneTree
SceneTree
- Multiple resolutions
Multiple resolutions

## Properties

| bool | auto_accept_quit | true |
|---|---|---|
| Node | current_scene |  |
| bool | debug_collisions_hint | false |
| bool | debug_navigation_hint | false |
| bool | debug_paths_hint | false |
| Node | edited_scene_root |  |
| bool | multiplayer_poll | true |
| bool | paused | false |
| bool | physics_interpolation | false |
| bool | quit_on_go_back | true |
| Window | root |  |

bool
auto_accept_quit
true
Node
current_scene
bool
debug_collisions_hint
false
bool
debug_navigation_hint
false
bool
debug_paths_hint
false
Node
edited_scene_root
bool
multiplayer_poll
true
bool
paused
false
bool
physics_interpolation
false
bool
quit_on_go_back
true
Window
root

## Methods

| void | call_group(group:StringName, method:StringName, ...)vararg |
|---|---|
| void | call_group_flags(flags:int, group:StringName, method:StringName, ...)vararg |
| Error | change_scene_to_file(path:String) |
| Error | change_scene_to_node(node:Node) |
| Error | change_scene_to_packed(packed_scene:PackedScene) |
| SceneTreeTimer | create_timer(time_sec:float, process_always:bool= true, process_in_physics:bool= false, ignore_time_scale:bool= false) |
| Tween | create_tween() |
| Node | get_first_node_in_group(group:StringName) |
| int | get_frame()const |
| MultiplayerAPI | get_multiplayer(for_path:NodePath= NodePath(""))const |
| int | get_node_count()const |
| int | get_node_count_in_group(group:StringName)const |
| Array[Node] | get_nodes_in_group(group:StringName) |
| Array[Tween] | get_processed_tweens() |
| bool | has_group(name:StringName)const |
| bool | is_accessibility_enabled()const |
| bool | is_accessibility_supported()const |
| void | notify_group(group:StringName, notification:int) |
| void | notify_group_flags(call_flags:int, group:StringName, notification:int) |
| void | queue_delete(obj:Object) |
| void | quit(exit_code:int= 0) |
| Error | reload_current_scene() |
| void | set_group(group:StringName, property:String, value:Variant) |
| void | set_group_flags(call_flags:int, group:StringName, property:String, value:Variant) |
| void | set_multiplayer(multiplayer:MultiplayerAPI, root_path:NodePath= NodePath("")) |
| void | unload_current_scene() |

void
call_group(group:StringName, method:StringName, ...)vararg
void
call_group_flags(flags:int, group:StringName, method:StringName, ...)vararg
Error
change_scene_to_file(path:String)
Error
change_scene_to_node(node:Node)
Error
change_scene_to_packed(packed_scene:PackedScene)
SceneTreeTimer
create_timer(time_sec:float, process_always:bool= true, process_in_physics:bool= false, ignore_time_scale:bool= false)
Tween
create_tween()
Node
get_first_node_in_group(group:StringName)
get_frame()const
MultiplayerAPI
get_multiplayer(for_path:NodePath= NodePath(""))const
get_node_count()const
get_node_count_in_group(group:StringName)const
Array[Node]
get_nodes_in_group(group:StringName)
Array[Tween]
get_processed_tweens()
bool
has_group(name:StringName)const
bool
is_accessibility_enabled()const
bool
is_accessibility_supported()const
void
notify_group(group:StringName, notification:int)
void
notify_group_flags(call_flags:int, group:StringName, notification:int)
void
queue_delete(obj:Object)
void
quit(exit_code:int= 0)
Error
reload_current_scene()
void
set_group(group:StringName, property:String, value:Variant)
void
set_group_flags(call_flags:int, group:StringName, property:String, value:Variant)
void
set_multiplayer(multiplayer:MultiplayerAPI, root_path:NodePath= NodePath(""))
void
unload_current_scene()

## Signals

node_added(node:Node)🔗
Emitted when thenodeenters this tree.
node_configuration_warning_changed(node:Node)🔗
Emitted when thenode'sNode.update_configuration_warnings()is called. Only emitted in the editor.
node_removed(node:Node)🔗
Emitted when thenodeexits this tree.
node_renamed(node:Node)🔗
Emitted when thenode'sNode.nameis changed.
physics_frame()🔗
Emitted immediately beforeNode._physics_process()is called on every node in this tree.
process_frame()🔗
Emitted immediately beforeNode._process()is called on every node in this tree.
scene_changed()🔗
Emitted after the new scene is added to scene tree and initialized. Can be used to reliably accesscurrent_scenewhen changing scenes.

```
# This code should be inside an autoload.
get_tree().change_scene_to_file(other_scene_path)
await get_tree().scene_changed
print(get_tree().current_scene) # Prints the new scene.
```

tree_changed()🔗
Emitted any time the tree's hierarchy changes (nodes being moved, renamed, etc.).
tree_process_mode_changed()🔗
Emitted when theNode.process_modeof any node inside the tree is changed. Only emitted in the editor, to update the visibility of disabled nodes.

## Enumerations

enumGroupCallFlags:🔗
GroupCallFlagsGROUP_CALL_DEFAULT=0
Call nodes within a group with no special behavior (default).
GroupCallFlagsGROUP_CALL_REVERSE=1
Call nodes within a group in reverse tree hierarchy order (all nested children are called before their respective parent nodes).
GroupCallFlagsGROUP_CALL_DEFERRED=2
Call nodes within a group at the end of the current frame (can be either process or physics frame), similar toObject.call_deferred().
GroupCallFlagsGROUP_CALL_UNIQUE=4
Call nodes within a group only once, even if the call is executed many times in the same frame. Must be combined withGROUP_CALL_DEFERREDto work.
Note:Different arguments are not taken into account. Therefore, when the same call is executed with different arguments, only the first call will be performed.

## Property Descriptions

boolauto_accept_quit=true🔗

- voidset_auto_accept_quit(value:bool)
voidset_auto_accept_quit(value:bool)
- boolis_auto_accept_quit()
boolis_auto_accept_quit()
Iftrue, the application automatically accepts quitting requests.
For mobile platforms, seequit_on_go_back.
Nodecurrent_scene🔗
- voidset_current_scene(value:Node)
voidset_current_scene(value:Node)
- Nodeget_current_scene()
Nodeget_current_scene()
The root node of the currently loaded main scene, usually as a direct child ofroot. See alsochange_scene_to_file(),change_scene_to_packed(), andreload_current_scene().
Warning:Setting this property directly may not work as expected, as it doesnotadd or remove any nodes from this tree.
booldebug_collisions_hint=false🔗
- voidset_debug_collisions_hint(value:bool)
voidset_debug_collisions_hint(value:bool)
- boolis_debugging_collisions_hint()
boolis_debugging_collisions_hint()
Iftrue, collision shapes will be visible when running the game from the editor for debugging purposes.
Note:This property is not designed to be changed at run-time. Changing the value ofdebug_collisions_hintwhile the project is running will not have the desired effect.
booldebug_navigation_hint=false🔗
- voidset_debug_navigation_hint(value:bool)
voidset_debug_navigation_hint(value:bool)
- boolis_debugging_navigation_hint()
boolis_debugging_navigation_hint()
Iftrue, navigation polygons will be visible when running the game from the editor for debugging purposes.
Note:This property is not designed to be changed at run-time. Changing the value ofdebug_navigation_hintwhile the project is running will not have the desired effect.
booldebug_paths_hint=false🔗
- voidset_debug_paths_hint(value:bool)
voidset_debug_paths_hint(value:bool)
- boolis_debugging_paths_hint()
boolis_debugging_paths_hint()
Iftrue, curves fromPath2DandPath3Dnodes will be visible when running the game from the editor for debugging purposes.
Note:This property is not designed to be changed at run-time. Changing the value ofdebug_paths_hintwhile the project is running will not have the desired effect.
Nodeedited_scene_root🔗
- voidset_edited_scene_root(value:Node)
voidset_edited_scene_root(value:Node)
- Nodeget_edited_scene_root()
Nodeget_edited_scene_root()
The root of the scene currently being edited in the editor. This is usually a direct child ofroot.
Note:This property does nothing in release builds.
boolmultiplayer_poll=true🔗
- voidset_multiplayer_poll_enabled(value:bool)
voidset_multiplayer_poll_enabled(value:bool)
- boolis_multiplayer_poll_enabled()
boolis_multiplayer_poll_enabled()
Iftrue(default value), enables automatic polling of theMultiplayerAPIfor this SceneTree duringprocess_frame.
Iffalse, you need to manually callMultiplayerAPI.poll()to process network packets and deliver RPCs. This allows running RPCs in a different loop (e.g. physics, thread, specific time step) and for manualMutexprotection when accessing theMultiplayerAPIfrom threads.
boolpaused=false🔗
- voidset_pause(value:bool)
voidset_pause(value:bool)
- boolis_paused()
boolis_paused()
Iftrue, the scene tree is considered paused. This causes the following behavior:
- 2D and 3D physics will be stopped, as well as collision detection and related signals.
2D and 3D physics will be stopped, as well as collision detection and related signals.
- Depending on each node'sNode.process_mode, theirNode._process(),Node._physics_process()andNode._input()callback methods may not called anymore.
Depending on each node'sNode.process_mode, theirNode._process(),Node._physics_process()andNode._input()callback methods may not called anymore.
boolphysics_interpolation=false🔗
- voidset_physics_interpolation_enabled(value:bool)
voidset_physics_interpolation_enabled(value:bool)
- boolis_physics_interpolation_enabled()
boolis_physics_interpolation_enabled()
Iftrue, the renderer will interpolate the transforms of objects (both physics and non-physics) between the last two transforms, so that smooth motion is seen even when physics ticks do not coincide with rendered frames.
The default value of this property is controlled byProjectSettings.physics/common/physics_interpolation.
Note:Although this is a global setting, finer control of individual branches of theSceneTreeis possible usingNode.physics_interpolation_mode.
boolquit_on_go_back=true🔗
- voidset_quit_on_go_back(value:bool)
voidset_quit_on_go_back(value:bool)
- boolis_quit_on_go_back()
boolis_quit_on_go_back()
Iftrue, the application quits automatically when navigating back (e.g. using the system "Back" button on Android).
To handle 'Go Back' button when this option is disabled, useDisplayServer.WINDOW_EVENT_GO_BACK_REQUEST.
Windowroot🔗
- Windowget_root()
Windowget_root()
The tree's rootWindow. This is top-mostNodeof the scene tree, and is always present. An absoluteNodePathalways starts from this node. Children of the root node may include the loadedcurrent_scene, as well as anyAutoLoadconfigured in the Project Settings.
Warning:Do not delete this node. This will result in unstable behavior, followed by a crash.

## Method Descriptions

voidcall_group(group:StringName, method:StringName, ...)vararg🔗
Callsmethodon each node inside this tree added to the givengroup. You can pass arguments tomethodby specifying them at the end of this method call. Nodes that cannot callmethod(either because the method doesn't exist or the arguments do not match) are ignored. See alsoset_group()andnotify_group().
Note:This method acts immediately on all selected nodes at once, which may cause stuttering in some performance-intensive situations.
Note:In C#,methodmust be in snake_case when referring to built-in Godot methods. Prefer using the names exposed in theMethodNameclass to avoid allocating a newStringNameon each call.
voidcall_group_flags(flags:int, group:StringName, method:StringName, ...)vararg🔗
Calls the givenmethodon each node inside this tree added to the givengroup. Useflagsto customize this method's behavior (seeGroupCallFlags). Additional arguments formethodcan be passed at the end of this method. Nodes that cannot callmethod(either because the method doesn't exist or the arguments do not match) are ignored.

```
# Calls "hide" to all nodes of the "enemies" group, at the end of the frame and in reverse tree order.
get_tree().call_group_flags(
        SceneTree.GROUP_CALL_DEFERRED | SceneTree.GROUP_CALL_REVERSE,
        "enemies", "hide")
```

Note:In C#,methodmust be in snake_case when referring to built-in Godot methods. Prefer using the names exposed in theMethodNameclass to avoid allocating a newStringNameon each call.
Errorchange_scene_to_file(path:String)🔗
Changes the running scene to the one at the givenpath, after loading it into aPackedSceneand creating a new instance.
Returns@GlobalScope.OKon success,@GlobalScope.ERR_CANT_OPENif thepathcannot be loaded into aPackedScene, or@GlobalScope.ERR_CANT_CREATEif that scene cannot be instantiated.
Note:Seechange_scene_to_node()for details on the order of operations.
Errorchange_scene_to_node(node:Node)🔗
Changes the running scene to the providedNode. Useful when you want to set up the new scene before changing.
Returns@GlobalScope.OKon success,@GlobalScope.ERR_INVALID_PARAMETERif thenodeisnull, or@GlobalScope.ERR_UNCONFIGUREDif thenodeis already inside the scene tree.
Note:Operations happen in the following order whenchange_scene_to_node()is called:

- The current scene node is immediately removed from the tree. From that point,Node.get_tree()called on the current (outgoing) scene will returnnull.current_scenewill benulltoo, because the new scene is not available yet.
The current scene node is immediately removed from the tree. From that point,Node.get_tree()called on the current (outgoing) scene will returnnull.current_scenewill benulltoo, because the new scene is not available yet.
- At the end of the frame, the formerly current scene, already removed from the tree, will be deleted (freed from memory) and then the new scene node will be added to the tree.Node.get_tree()andcurrent_scenewill be back to working as usual.
At the end of the frame, the formerly current scene, already removed from the tree, will be deleted (freed from memory) and then the new scene node will be added to the tree.Node.get_tree()andcurrent_scenewill be back to working as usual.
This ensures that both scenes aren't running at the same time, while still freeing the previous scene in a safe way similar toNode.queue_free().
If you want to reliably access the new scene, await thescene_changedsignal.
Warning:After using this method, theSceneTreewill take ownership of the node and will free it automatically when changing scene again. Any references you had to that node will become invalid.
Errorchange_scene_to_packed(packed_scene:PackedScene)🔗
Changes the running scene to a new instance of the givenPackedScene(which must be valid).
Returns@GlobalScope.OKon success,@GlobalScope.ERR_CANT_CREATEif the scene cannot be instantiated, or@GlobalScope.ERR_INVALID_PARAMETERif the scene is invalid.
Note:Seechange_scene_to_node()for details on the order of operations.
SceneTreeTimercreate_timer(time_sec:float, process_always:bool= true, process_in_physics:bool= false, ignore_time_scale:bool= false)🔗
Returns a newSceneTreeTimer. Aftertime_secin seconds have passed, the timer will emitSceneTreeTimer.timeoutand will be automatically freed.
Ifprocess_alwaysisfalse, the timer will be paused when settingpausedtotrue.
Ifprocess_in_physicsistrue, the timer will update at the end of the physics frame, instead of the process frame.
Ifignore_time_scaleistrue, the timer will ignoreEngine.time_scaleand update with the real, elapsed time.
This method is commonly used to create a one-shot delay timer, as in the following example:

```
func some_function():
    print("start")
    await get_tree().create_timer(1.0).timeout
    print("end")
```

```
public async Task SomeFunction()
{
    GD.Print("start");
    await ToSignal(GetTree().CreateTimer(1.0f), SceneTreeTimer.SignalName.Timeout);
    GD.Print("end");
}
```

Note:The timer is always updatedafterall of the nodes in the tree. A node'sNode._process()method would be called before the timer updates (orNode._physics_process()ifprocess_in_physicsis set totrue).
Tweencreate_tween()🔗
Creates and returns a newTweenprocessed in this tree. The Tween will start automatically on the next process frame or physics frame (depending on itsTweenProcessMode).
Note:ATweencreated using this method is not bound to anyNode. It may keep working until there is nothing left to animate. If you want theTweento be automatically killed when theNodeis freed, useNode.create_tween()orTween.bind_node().
Nodeget_first_node_in_group(group:StringName)🔗
Returns the firstNodefound inside the tree, that has been added to the givengroup, in scene hierarchy order. Returnsnullif no match is found. See alsoget_nodes_in_group().
intget_frame()const🔗
Returns how many physics process steps have been processed, since the application started. This isnota measurement of elapsed time. See alsophysics_frame. For the number of frames rendered, seeEngine.get_process_frames().
MultiplayerAPIget_multiplayer(for_path:NodePath= NodePath(""))const🔗
Searches for theMultiplayerAPIconfigured for the given path, if one does not exist it searches the parent paths until one is found. If the path is empty, or none is found, the default one is returned. Seeset_multiplayer().
intget_node_count()const🔗
Returns the number of nodes inside this tree.
intget_node_count_in_group(group:StringName)const🔗
Returns the number of nodes assigned to the given group.
Array[Node]get_nodes_in_group(group:StringName)🔗
Returns anArraycontaining all nodes inside this tree, that have been added to the givengroup, in scene hierarchy order.
Array[Tween]get_processed_tweens()🔗
Returns anArrayof currently existingTweens in the tree, including paused tweens.
boolhas_group(name:StringName)const🔗
Returnstrueif a node added to the given groupnameexists in the tree.
boolis_accessibility_enabled()const🔗
Returnstrueif accessibility features are enabled, and accessibility information updates are actively processed.
boolis_accessibility_supported()const🔗
Returnstrueif accessibility features are supported by the OS and enabled in project settings.
voidnotify_group(group:StringName, notification:int)🔗
CallsObject.notification()with the givennotificationto all nodes inside this tree added to thegroup. See alsoGodot notificationsandcall_group()andset_group().
Note:This method acts immediately on all selected nodes at once, which may cause stuttering in some performance-intensive situations.
voidnotify_group_flags(call_flags:int, group:StringName, notification:int)🔗
CallsObject.notification()with the givennotificationto all nodes inside this tree added to thegroup. Usecall_flagsto customize this method's behavior (seeGroupCallFlags).
voidqueue_delete(obj:Object)🔗
Queues the givenobjto be deleted, calling itsObject.free()at the end of the current frame. This method is similar toNode.queue_free().
voidquit(exit_code:int= 0)🔗
Quits the application at the end of the current iteration, with the givenexit_code.
By convention, an exit code of0indicates success, whereas any other exit code indicates an error. For portability reasons, it should be between0and125(inclusive).
Note:On iOS this method doesn't work. Instead, as recommended by theiOS Human Interface Guidelines, the user is expected to close apps via the Home button.
Errorreload_current_scene()🔗
Reloads the currently active scene, replacingcurrent_scenewith a new instance of its originalPackedScene.
Returns@GlobalScope.OKon success,@GlobalScope.ERR_UNCONFIGUREDif nocurrent_sceneis defined,@GlobalScope.ERR_CANT_OPENifcurrent_scenecannot be loaded into aPackedScene, or@GlobalScope.ERR_CANT_CREATEif the scene cannot be instantiated.
voidset_group(group:StringName, property:String, value:Variant)🔗
Sets the givenpropertytovalueon all nodes inside this tree added to the givengroup. Nodes that do not have thepropertyare ignored. See alsocall_group()andnotify_group().
Note:This method acts immediately on all selected nodes at once, which may cause stuttering in some performance-intensive situations.
Note:In C#,propertymust be in snake_case when referring to built-in Godot properties. Prefer using the names exposed in thePropertyNameclass to avoid allocating a newStringNameon each call.
voidset_group_flags(call_flags:int, group:StringName, property:String, value:Variant)🔗
Sets the givenpropertytovalueon all nodes inside this tree added to the givengroup. Nodes that do not have thepropertyare ignored. Usecall_flagsto customize this method's behavior (seeGroupCallFlags).
Note:In C#,propertymust be in snake_case when referring to built-in Godot properties. Prefer using the names exposed in thePropertyNameclass to avoid allocating a newStringNameon each call.
voidset_multiplayer(multiplayer:MultiplayerAPI, root_path:NodePath= NodePath(""))🔗
Sets a customMultiplayerAPIwith the givenroot_path(controlling also the relative subpaths), or override the default one ifroot_pathis empty.
Note:NoMultiplayerAPImust be configured for the subpath containingroot_path, nested custom multiplayers are not allowed. I.e. if one is configured for"/root/Foo"setting one for"/root/Foo/Bar"will cause an error.
Note:set_multiplayer()should be calledbeforethe child nodes are ready at the givenroot_path. If multiplayer nodes likeMultiplayerSpawnerorMultiplayerSynchronizerare added to the tree before the custom multiplayer API is set, they will not work.
voidunload_current_scene()🔗
If a current scene is loaded, calling this method will unload it.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
