# Node in English

# Node

Inherits:Object
Inherited By:AnimationMixer,AudioStreamPlayer,CanvasItem,CanvasLayer,EditorFileSystem,EditorPlugin,EditorResourcePreview,HTTPRequest,InstancePlaceholder,MissingNode,MultiplayerSpawner,MultiplayerSynchronizer,NavigationAgent2D,NavigationAgent3D,Node3D,ResourcePreloader,ShaderGlobalsOverride,StatusIndicator,Timer,Viewport,WorldEnvironment
Base class for all scene objects.

## Description

Nodes are Godot's building blocks. They can be assigned as the child of another node, resulting in a tree arrangement. A given node can contain any number of nodes as children with the requirement that all siblings (direct children of a node) should have unique names.
A tree of nodes is called ascene. Scenes can be saved to the disk and then instantiated into other scenes. This allows for very high flexibility in the architecture and data model of Godot projects.
Scene tree:TheSceneTreecontains the active tree of nodes. When a node is added to the scene tree, it receives theNOTIFICATION_ENTER_TREEnotification and its_enter_tree()callback is triggered. Child nodes are always addedaftertheir parent node, i.e. the_enter_tree()callback of a parent node will be triggered before its child's.
Once all nodes have been added in the scene tree, they receive theNOTIFICATION_READYnotification and their respective_ready()callbacks are triggered. For groups of nodes, the_ready()callback is called in reverse order, starting with the children and moving up to the parent nodes.
This means that when adding a node to the scene tree, the following order will be used for the callbacks:_enter_tree()of the parent,_enter_tree()of the children,_ready()of the children and finally_ready()of the parent (recursively for the entire scene tree).
Processing:Nodes can override the "process" state, so that they receive a callback on each frame requesting them to process (do something). Normal processing (callback_process(), toggled withset_process()) happens as fast as possible and is dependent on the frame rate, so the processing timedelta(in seconds) is passed as an argument. Physics processing (callback_physics_process(), toggled withset_physics_process()) happens a fixed number of times per second (60 by default) and is useful for code related to the physics engine.
Nodes can also process input events. When present, the_input()function will be called for each input that the program receives. In many cases, this can be overkill (unless used for simple projects), and the_unhandled_input()function might be preferred; it is called when the input event was not handled by anyone else (typically, GUIControlnodes), ensuring that the node only receives the events that were meant for it.
To keep track of the scene hierarchy (especially when instantiating scenes into other scenes), an "owner" can be set for the node with theownerproperty. This keeps track of who instantiated what. This is mostly useful when writing editors and tools, though.
Finally, when a node is freed withObject.free()orqueue_free(), it will also free all its children.
Groups:Nodes can be added to as many groups as you want to be easy to manage, you could create groups like "enemies" or "collectables" for example, depending on your game. Seeadd_to_group(),is_in_group()andremove_from_group(). You can then retrieve all nodes in these groups, iterate them and even call methods on groups via the methods onSceneTree.
Networking with nodes:After connecting to a server (or making one, seeENetMultiplayerPeer), it is possible to use the built-in RPC (remote procedure call) system to communicate over the network. By callingrpc()with a method name, it will be called locally and in all connected peers (peers = clients and the server that accepts connections). To identify which node receives the RPC call, Godot will use itsNodePath(make sure node names are the same on all peers). Also, take a look at the high-level networking tutorial and corresponding demos.
Note:Thescriptproperty is part of theObjectclass, notNode. It isn't exposed like most properties but does have a setter and getter (seeObject.set_script()andObject.get_script()).

## Tutorials

- Nodes and scenes
Nodes and scenes
- All Demos
All Demos

## Properties

| AutoTranslateMode | auto_translate_mode | 0 |
|---|---|---|
| String | editor_description | "" |
| MultiplayerAPI | multiplayer |  |
| StringName | name |  |
| Node | owner |  |
| PhysicsInterpolationMode | physics_interpolation_mode | 0 |
| ProcessMode | process_mode | 0 |
| int | process_physics_priority | 0 |
| int | process_priority | 0 |
| ProcessThreadGroup | process_thread_group | 0 |
| int | process_thread_group_order |  |
| BitField[ProcessThreadMessages] | process_thread_messages |  |
| String | scene_file_path |  |
| bool | unique_name_in_owner | false |

AutoTranslateMode
auto_translate_mode
String
editor_description
MultiplayerAPI
multiplayer
StringName
name
Node
owner
PhysicsInterpolationMode
physics_interpolation_mode
ProcessMode
process_mode
process_physics_priority
process_priority
ProcessThreadGroup
process_thread_group
process_thread_group_order
BitField[ProcessThreadMessages]
process_thread_messages
String
scene_file_path
bool
unique_name_in_owner
false

## Methods

| void | _enter_tree()virtual |
|---|---|
| void | _exit_tree()virtual |
| PackedStringArray | _get_accessibility_configuration_warnings()virtualconst |
| PackedStringArray | _get_configuration_warnings()virtualconst |
| RID | _get_focused_accessibility_element()virtualconst |
| void | _input(event:InputEvent)virtual |
| void | _physics_process(delta:float)virtual |
| void | _process(delta:float)virtual |
| void | _ready()virtual |
| void | _shortcut_input(event:InputEvent)virtual |
| void | _unhandled_input(event:InputEvent)virtual |
| void | _unhandled_key_input(event:InputEvent)virtual |
| void | add_child(node:Node, force_readable_name:bool= false, internal:InternalMode= 0) |
| void | add_sibling(sibling:Node, force_readable_name:bool= false) |
| void | add_to_group(group:StringName, persistent:bool= false) |
| String | atr(message:String, context:StringName= "")const |
| String | atr_n(message:String, plural_message:StringName, n:int, context:StringName= "")const |
| Variant | call_deferred_thread_group(method:StringName, ...)vararg |
| Variant | call_thread_safe(method:StringName, ...)vararg |
| bool | can_auto_translate()const |
| bool | can_process()const |
| Tween | create_tween() |
| Node | duplicate(flags:int= 15)const |
| Node | find_child(pattern:String, recursive:bool= true, owned:bool= true)const |
| Array[Node] | find_children(pattern:String, type:String= "", recursive:bool= true, owned:bool= true)const |
| Node | find_parent(pattern:String)const |
| RID | get_accessibility_element()const |
| Node | get_child(idx:int, include_internal:bool= false)const |
| int | get_child_count(include_internal:bool= false)const |
| Array[Node] | get_children(include_internal:bool= false)const |
| Array[StringName] | get_groups()const |
| int | get_index(include_internal:bool= false)const |
| Window | get_last_exclusive_window()const |
| int | get_multiplayer_authority()const |
| Node | get_node(path:NodePath)const |
| Array | get_node_and_resource(path:NodePath) |
| Node | get_node_or_null(path:NodePath)const |
| Variant | get_node_rpc_config()const |
| Array[int] | get_orphan_node_ids()static |
| Node | get_parent()const |
| NodePath | get_path()const |
| NodePath | get_path_to(node:Node, use_unique_path:bool= false)const |
| float | get_physics_process_delta_time()const |
| float | get_process_delta_time()const |
| bool | get_scene_instance_load_placeholder()const |
| SceneTree | get_tree()const |
| String | get_tree_string() |
| String | get_tree_string_pretty() |
| Viewport | get_viewport()const |
| Window | get_window()const |
| bool | has_node(path:NodePath)const |
| bool | has_node_and_resource(path:NodePath)const |
| bool | is_ancestor_of(node:Node)const |
| bool | is_displayed_folded()const |
| bool | is_editable_instance(node:Node)const |
| bool | is_greater_than(node:Node)const |
| bool | is_in_group(group:StringName)const |
| bool | is_inside_tree()const |
| bool | is_multiplayer_authority()const |
| bool | is_node_ready()const |
| bool | is_part_of_edited_scene()const |
| bool | is_physics_interpolated()const |
| bool | is_physics_interpolated_and_enabled()const |
| bool | is_physics_processing()const |
| bool | is_physics_processing_internal()const |
| bool | is_processing()const |
| bool | is_processing_input()const |
| bool | is_processing_internal()const |
| bool | is_processing_shortcut_input()const |
| bool | is_processing_unhandled_input()const |
| bool | is_processing_unhandled_key_input()const |
| void | move_child(child_node:Node, to_index:int) |
| void | notify_deferred_thread_group(what:int) |
| void | notify_thread_safe(what:int) |
| void | print_orphan_nodes()static |
| void | print_tree() |
| void | print_tree_pretty() |
| void | propagate_call(method:StringName, args:Array= [], parent_first:bool= false) |
| void | propagate_notification(what:int) |
| void | queue_accessibility_update() |
| void | queue_free() |
| void | remove_child(node:Node) |
| void | remove_from_group(group:StringName) |
| void | reparent(new_parent:Node, keep_global_transform:bool= true) |
| void | replace_by(node:Node, keep_groups:bool= false) |
| void | request_ready() |
| void | reset_physics_interpolation() |
| Error | rpc(method:StringName, ...)vararg |
| void | rpc_config(method:StringName, config:Variant) |
| Error | rpc_id(peer_id:int, method:StringName, ...)vararg |
| void | set_deferred_thread_group(property:StringName, value:Variant) |
| void | set_display_folded(fold:bool) |
| void | set_editable_instance(node:Node, is_editable:bool) |
| void | set_multiplayer_authority(id:int, recursive:bool= true) |
| void | set_physics_process(enable:bool) |
| void | set_physics_process_internal(enable:bool) |
| void | set_process(enable:bool) |
| void | set_process_input(enable:bool) |
| void | set_process_internal(enable:bool) |
| void | set_process_shortcut_input(enable:bool) |
| void | set_process_unhandled_input(enable:bool) |
| void | set_process_unhandled_key_input(enable:bool) |
| void | set_scene_instance_load_placeholder(load_placeholder:bool) |
| void | set_thread_safe(property:StringName, value:Variant) |
| void | set_translation_domain_inherited() |
| void | update_configuration_warnings() |

void
_enter_tree()virtual
void
_exit_tree()virtual
PackedStringArray
_get_accessibility_configuration_warnings()virtualconst
PackedStringArray
_get_configuration_warnings()virtualconst
_get_focused_accessibility_element()virtualconst
void
_input(event:InputEvent)virtual
void
_physics_process(delta:float)virtual
void
_process(delta:float)virtual
void
_ready()virtual
void
_shortcut_input(event:InputEvent)virtual
void
_unhandled_input(event:InputEvent)virtual
void
_unhandled_key_input(event:InputEvent)virtual
void
add_child(node:Node, force_readable_name:bool= false, internal:InternalMode= 0)
void
add_sibling(sibling:Node, force_readable_name:bool= false)
void
add_to_group(group:StringName, persistent:bool= false)
String
atr(message:String, context:StringName= "")const
String
atr_n(message:String, plural_message:StringName, n:int, context:StringName= "")const
Variant
call_deferred_thread_group(method:StringName, ...)vararg
Variant
call_thread_safe(method:StringName, ...)vararg
bool
can_auto_translate()const
bool
can_process()const
Tween
create_tween()
Node
duplicate(flags:int= 15)const
Node
find_child(pattern:String, recursive:bool= true, owned:bool= true)const
Array[Node]
find_children(pattern:String, type:String= "", recursive:bool= true, owned:bool= true)const
Node
find_parent(pattern:String)const
get_accessibility_element()const
Node
get_child(idx:int, include_internal:bool= false)const
get_child_count(include_internal:bool= false)const
Array[Node]
get_children(include_internal:bool= false)const
Array[StringName]
get_groups()const
get_index(include_internal:bool= false)const
Window
get_last_exclusive_window()const
get_multiplayer_authority()const
Node
get_node(path:NodePath)const
Array
get_node_and_resource(path:NodePath)
Node
get_node_or_null(path:NodePath)const
Variant
get_node_rpc_config()const
Array[int]
get_orphan_node_ids()static
Node
get_parent()const
NodePath
get_path()const
NodePath
get_path_to(node:Node, use_unique_path:bool= false)const
float
get_physics_process_delta_time()const
float
get_process_delta_time()const
bool
get_scene_instance_load_placeholder()const
SceneTree
get_tree()const
String
get_tree_string()
String
get_tree_string_pretty()
Viewport
get_viewport()const
Window
get_window()const
bool
has_node(path:NodePath)const
bool
has_node_and_resource(path:NodePath)const
bool
is_ancestor_of(node:Node)const
bool
is_displayed_folded()const
bool
is_editable_instance(node:Node)const
bool
is_greater_than(node:Node)const
bool
is_in_group(group:StringName)const
bool
is_inside_tree()const
bool
is_multiplayer_authority()const
bool
is_node_ready()const
bool
is_part_of_edited_scene()const
bool
is_physics_interpolated()const
bool
is_physics_interpolated_and_enabled()const
bool
is_physics_processing()const
bool
is_physics_processing_internal()const
bool
is_processing()const
bool
is_processing_input()const
bool
is_processing_internal()const
bool
is_processing_shortcut_input()const
bool
is_processing_unhandled_input()const
bool
is_processing_unhandled_key_input()const
void
move_child(child_node:Node, to_index:int)
void
notify_deferred_thread_group(what:int)
void
notify_thread_safe(what:int)
void
print_orphan_nodes()static
void
print_tree()
void
print_tree_pretty()
void
propagate_call(method:StringName, args:Array= [], parent_first:bool= false)
void
propagate_notification(what:int)
void
queue_accessibility_update()
void
queue_free()
void
remove_child(node:Node)
void
remove_from_group(group:StringName)
void
reparent(new_parent:Node, keep_global_transform:bool= true)
void
replace_by(node:Node, keep_groups:bool= false)
void
request_ready()
void
reset_physics_interpolation()
Error
rpc(method:StringName, ...)vararg
void
rpc_config(method:StringName, config:Variant)
Error
rpc_id(peer_id:int, method:StringName, ...)vararg
void
set_deferred_thread_group(property:StringName, value:Variant)
void
set_display_folded(fold:bool)
void
set_editable_instance(node:Node, is_editable:bool)
void
set_multiplayer_authority(id:int, recursive:bool= true)
void
set_physics_process(enable:bool)
void
set_physics_process_internal(enable:bool)
void
set_process(enable:bool)
void
set_process_input(enable:bool)
void
set_process_internal(enable:bool)
void
set_process_shortcut_input(enable:bool)
void
set_process_unhandled_input(enable:bool)
void
set_process_unhandled_key_input(enable:bool)
void
set_scene_instance_load_placeholder(load_placeholder:bool)
void
set_thread_safe(property:StringName, value:Variant)
void
set_translation_domain_inherited()
void
update_configuration_warnings()

## Signals

child_entered_tree(node:Node)🔗
Emitted when the childnodeenters theSceneTree, usually because this node entered the tree (seetree_entered), oradd_child()has been called.
This signal is emittedafterthe child node's ownNOTIFICATION_ENTER_TREEandtree_entered.
child_exiting_tree(node:Node)🔗
Emitted when the childnodeis about to exit theSceneTree, usually because this node is exiting the tree (seetree_exiting), or because the childnodeis being removed or freed.
When this signal is received, the childnodeis still accessible inside the tree. This signal is emittedafterthe child node's owntree_exitingandNOTIFICATION_EXIT_TREE.
child_order_changed()🔗
Emitted when the list of children is changed. This happens when child nodes are added, moved or removed.
editor_description_changed(node:Node)🔗
Emitted when the node's editor description field changed.
editor_state_changed()🔗
Emitted when an attribute of the node that is relevant to the editor is changed. Only emitted in the editor.
ready()🔗
Emitted when the node is considered ready, after_ready()is called.
renamed()🔗
Emitted when the node'snameis changed, if the node is inside the tree.
replacing_by(node:Node)🔗
Emitted when this node is being replaced by thenode, seereplace_by().
This signal is emittedafternodehas been added as a child of the original parent node, butbeforeall original child nodes have been reparented tonode.
tree_entered()🔗
Emitted when the node enters the tree.
This signal is emittedafterthe relatedNOTIFICATION_ENTER_TREEnotification.
tree_exited()🔗
Emitted after the node exits the tree and is no longer active.
This signal is emittedafterthe relatedNOTIFICATION_EXIT_TREEnotification.
tree_exiting()🔗
Emitted when the node is just about to exit the tree. The node is still valid. As such, this is the right place for de-initialization (or a "destructor", if you will).
This signal is emittedafterthe node's_exit_tree(), andbeforethe relatedNOTIFICATION_EXIT_TREE.

## Enumerations

enumProcessMode:🔗
ProcessModePROCESS_MODE_INHERIT=0
Inheritsprocess_modefrom the node's parent. This is the default for any newly created node.
ProcessModePROCESS_MODE_PAUSABLE=1
Stops processing whenSceneTree.pausedistrue. This is the inverse ofPROCESS_MODE_WHEN_PAUSED, and the default for the root node.
ProcessModePROCESS_MODE_WHEN_PAUSED=2
ProcessonlywhenSceneTree.pausedistrue. This is the inverse ofPROCESS_MODE_PAUSABLE.
ProcessModePROCESS_MODE_ALWAYS=3
Always process. Keeps processing, ignoringSceneTree.paused. This is the inverse ofPROCESS_MODE_DISABLED.
ProcessModePROCESS_MODE_DISABLED=4
Never process. Completely disables processing, ignoringSceneTree.paused. This is the inverse ofPROCESS_MODE_ALWAYS.
enumProcessThreadGroup:🔗
ProcessThreadGroupPROCESS_THREAD_GROUP_INHERIT=0
Process this node based on the thread group mode of the first parent (or grandparent) node that has a thread group mode that is not inherit. Seeprocess_thread_groupfor more information.
ProcessThreadGroupPROCESS_THREAD_GROUP_MAIN_THREAD=1
Process this node (and child nodes set to inherit) on the main thread. Seeprocess_thread_groupfor more information.
ProcessThreadGroupPROCESS_THREAD_GROUP_SUB_THREAD=2
Process this node (and child nodes set to inherit) on a sub-thread. Seeprocess_thread_groupfor more information.
flagsProcessThreadMessages:🔗
ProcessThreadMessagesFLAG_PROCESS_THREAD_MESSAGES=1
Allows this node to process threaded messages created withcall_deferred_thread_group()right before_process()is called.
ProcessThreadMessagesFLAG_PROCESS_THREAD_MESSAGES_PHYSICS=2
Allows this node to process threaded messages created withcall_deferred_thread_group()right before_physics_process()is called.
ProcessThreadMessagesFLAG_PROCESS_THREAD_MESSAGES_ALL=3
Allows this node to process threaded messages created withcall_deferred_thread_group()right before either_process()or_physics_process()are called.
enumPhysicsInterpolationMode:🔗
PhysicsInterpolationModePHYSICS_INTERPOLATION_MODE_INHERIT=0
Inheritsphysics_interpolation_modefrom the node's parent. This is the default for any newly created node.
PhysicsInterpolationModePHYSICS_INTERPOLATION_MODE_ON=1
Enables physics interpolation for this node and for children set toPHYSICS_INTERPOLATION_MODE_INHERIT. This is the default for the root node.
PhysicsInterpolationModePHYSICS_INTERPOLATION_MODE_OFF=2
Disables physics interpolation for this node and for children set toPHYSICS_INTERPOLATION_MODE_INHERIT.
enumDuplicateFlags:🔗
DuplicateFlagsDUPLICATE_SIGNALS=1
Duplicate the node's signal connections that are connected with theObject.CONNECT_PERSISTflag.
DuplicateFlagsDUPLICATE_GROUPS=2
Duplicate the node's groups.
DuplicateFlagsDUPLICATE_SCRIPTS=4
Duplicate the node's script (also overriding the duplicated children's scripts, if combined withDUPLICATE_USE_INSTANTIATION).
DuplicateFlagsDUPLICATE_USE_INSTANTIATION=8
Duplicate usingPackedScene.instantiate(). If the node comes from a scene saved on disk, reusesPackedScene.instantiate()as the base for the duplicated node and its children.
DuplicateFlagsDUPLICATE_INTERNAL_STATE=16
Duplicate also non-serializable variables (i.e. without@GlobalScope.PROPERTY_USAGE_STORAGE).
DuplicateFlagsDUPLICATE_DEFAULT=15
Duplicate using default flags. This constant is useful to add or remove a single flag.

```
# Duplicate non-exported variables.
var dupe = duplicate(DUPLICATE_DEFAULT | DUPLICATE_INTERNAL_STATE)
```

enumInternalMode:🔗
InternalModeINTERNAL_MODE_DISABLED=0
The node will not be internal.
InternalModeINTERNAL_MODE_FRONT=1
The node will be placed at the beginning of the parent's children, before any non-internal sibling.
InternalModeINTERNAL_MODE_BACK=2
The node will be placed at the end of the parent's children, after any non-internal sibling.
enumAutoTranslateMode:🔗
AutoTranslateModeAUTO_TRANSLATE_MODE_INHERIT=0
Inheritsauto_translate_modefrom the node's parent. This is the default for any newly created node.
AutoTranslateModeAUTO_TRANSLATE_MODE_ALWAYS=1
Always automatically translate. This is the inverse ofAUTO_TRANSLATE_MODE_DISABLED, and the default for the root node.
AutoTranslateModeAUTO_TRANSLATE_MODE_DISABLED=2
Never automatically translate. This is the inverse ofAUTO_TRANSLATE_MODE_ALWAYS.
String parsing for translation template generation will be skipped for this node and children that are set toAUTO_TRANSLATE_MODE_INHERIT.

## Constants

NOTIFICATION_ENTER_TREE=10🔗
Notification received when the node enters aSceneTree. See_enter_tree().
This notification is receivedbeforethe relatedtree_enteredsignal.
NOTIFICATION_EXIT_TREE=11🔗
Notification received when the node is about to exit aSceneTree. See_exit_tree().
This notification is receivedafterthe relatedtree_exitingsignal.
This notification is sent in reversed order.
NOTIFICATION_MOVED_IN_PARENT=12🔗
Deprecated:This notification is no longer sent by the engine. UseNOTIFICATION_CHILD_ORDER_CHANGEDinstead.
NOTIFICATION_READY=13🔗
Notification received when the node is ready. See_ready().
NOTIFICATION_PAUSED=14🔗
Notification received when the node is paused. Seeprocess_mode.
NOTIFICATION_UNPAUSED=15🔗
Notification received when the node is unpaused. Seeprocess_mode.
NOTIFICATION_PHYSICS_PROCESS=16🔗
Notification received from the tree every physics frame whenis_physics_processing()returnstrue. See_physics_process().
NOTIFICATION_PROCESS=17🔗
Notification received from the tree every rendered frame whenis_processing()returnstrue. See_process().
NOTIFICATION_PARENTED=18🔗
Notification received when the node is set as a child of another node (seeadd_child()andadd_sibling()).
Note:This doesnotmean that the node entered theSceneTree.
NOTIFICATION_UNPARENTED=19🔗
Notification received when the parent node callsremove_child()on this node.
Note:This doesnotmean that the node exited theSceneTree.
NOTIFICATION_SCENE_INSTANTIATED=20🔗
Notification receivedonlyby the newly instantiated scene root node, whenPackedScene.instantiate()is completed.
NOTIFICATION_DRAG_BEGIN=21🔗
Notification received when a drag operation begins. All nodes receive this notification, not only the dragged one.
Can be triggered either by dragging aControlthat provides drag data (seeControl._get_drag_data()) or usingControl.force_drag().
UseViewport.gui_get_drag_data()to get the dragged data.
NOTIFICATION_DRAG_END=22🔗
Notification received when a drag operation ends.
UseViewport.gui_is_drag_successful()to check if the drag succeeded.
NOTIFICATION_PATH_RENAMED=23🔗
Notification received when the node'snameor one of its ancestors'nameis changed. This notification isnotreceived when the node is removed from theSceneTree.
NOTIFICATION_CHILD_ORDER_CHANGED=24🔗
Notification received when the list of children is changed. This happens when child nodes are added, moved or removed.
NOTIFICATION_INTERNAL_PROCESS=25🔗
Notification received from the tree every rendered frame whenis_processing_internal()returnstrue.
NOTIFICATION_INTERNAL_PHYSICS_PROCESS=26🔗
Notification received from the tree every physics frame whenis_physics_processing_internal()returnstrue.
NOTIFICATION_POST_ENTER_TREE=27🔗
Notification received when the node enters the tree, just beforeNOTIFICATION_READYmay be received. Unlike the latter, it is sent every time the node enters tree, not just once.
NOTIFICATION_DISABLED=28🔗
Notification received when the node is disabled. SeePROCESS_MODE_DISABLED.
NOTIFICATION_ENABLED=29🔗
Notification received when the node is enabled again after being disabled. SeePROCESS_MODE_DISABLED.
NOTIFICATION_RESET_PHYSICS_INTERPOLATION=2001🔗
Notification received whenreset_physics_interpolation()is called on the node or its ancestors.
NOTIFICATION_EDITOR_PRE_SAVE=9001🔗
Notification received right before the scene with the node is saved in the editor. This notification is only sent in the Godot editor and will not occur in exported projects.
NOTIFICATION_EDITOR_POST_SAVE=9002🔗
Notification received right after the scene with the node is saved in the editor. This notification is only sent in the Godot editor and will not occur in exported projects.
NOTIFICATION_WM_MOUSE_ENTER=1002🔗
Notification received when the mouse enters the window.
Implemented for embedded windows and on desktop and web platforms.
NOTIFICATION_WM_MOUSE_EXIT=1003🔗
Notification received when the mouse leaves the window.
Implemented for embedded windows and on desktop and web platforms.
NOTIFICATION_WM_WINDOW_FOCUS_IN=1004🔗
Notification received from the OS when the node'sWindowancestor is focused. This may be a change of focus between two windows of the same engine instance, or from the OS desktop or a third-party application to a window of the game (in which caseNOTIFICATION_APPLICATION_FOCUS_INis also received).
AWindownode receives this notification when it is focused.
NOTIFICATION_WM_WINDOW_FOCUS_OUT=1005🔗
Notification received from the OS when the node'sWindowancestor is defocused. This may be a change of focus between two windows of the same engine instance, or from a window of the game to the OS desktop or a third-party application (in which caseNOTIFICATION_APPLICATION_FOCUS_OUTis also received).
AWindownode receives this notification when it is defocused.
NOTIFICATION_WM_CLOSE_REQUEST=1006🔗
Notification received from the OS when a close request is sent (e.g. closing the window with a "Close" button orAlt+F4).
Implemented on desktop platforms.
NOTIFICATION_WM_GO_BACK_REQUEST=1007🔗
Notification received from the OS when a go back request is sent (e.g. pressing the "Back" button on Android).
Implemented only on Android.
NOTIFICATION_WM_SIZE_CHANGED=1008🔗
Notification received when the window is resized.
Note:Only the resizedWindownode receives this notification, and it's not propagated to the child nodes.
NOTIFICATION_WM_DPI_CHANGE=1009🔗
Notification received from the OS when the screen's dots per inch (DPI) scale is changed. Only implemented on macOS.
NOTIFICATION_VP_MOUSE_ENTER=1010🔗
Notification received when the mouse cursor enters theViewport's visible area, that is not occluded behind otherControls orWindows, provided itsViewport.gui_disable_inputisfalseand regardless if it's currently focused or not.
NOTIFICATION_VP_MOUSE_EXIT=1011🔗
Notification received when the mouse cursor leaves theViewport's visible area, that is not occluded behind otherControls orWindows, provided itsViewport.gui_disable_inputisfalseand regardless if it's currently focused or not.
NOTIFICATION_WM_POSITION_CHANGED=1012🔗
Notification received when the window is moved.
NOTIFICATION_OS_MEMORY_WARNING=2009🔗
Notification received from the OS when the application is exceeding its allocated memory.
Implemented only on iOS.
NOTIFICATION_TRANSLATION_CHANGED=2010🔗
Notification received when translations may have changed. Can be triggered by the user changing the locale, changingauto_translate_modeor when the node enters the scene tree. Can be used to respond to language changes, for example to change the UI strings on the fly. Useful when working with the built-in translation support, likeObject.tr().
Note:This notification is received alongsideNOTIFICATION_ENTER_TREE, so if you are instantiating a scene, the child nodes will not be initialized yet. You can use it to setup translations for this node, child nodes created from script, or if you want to access child nodes added in the editor, make sure the node is ready usingis_node_ready().

```
func _notification(what):
    if what == NOTIFICATION_TRANSLATION_CHANGED:
        if not is_node_ready():
            await ready # Wait until ready signal.
        $Label.text = atr("%d Bananas") % banana_counter
```

NOTIFICATION_WM_ABOUT=2011🔗
Notification received from the OS when a request for "About" information is sent.
Implemented only on macOS.
NOTIFICATION_CRASH=2012🔗
Notification received from Godot's crash handler when the engine is about to crash.
Implemented on desktop platforms, if the crash handler is enabled.
NOTIFICATION_OS_IME_UPDATE=2013🔗
Notification received from the OS when an update of the Input Method Engine occurs (e.g. change of IME cursor position or composition string).
Implemented on desktop and web platforms.
NOTIFICATION_APPLICATION_RESUMED=2014🔗
Notification received from the OS when the application is resumed.
Specific to the Android and iOS platforms.
NOTIFICATION_APPLICATION_PAUSED=2015🔗
Notification received from the OS when the application is paused.
Specific to the Android and iOS platforms.
Note:On iOS, you only have approximately 5 seconds to finish a task started by this signal. If you go over this allotment, iOS will kill the app instead of pausing it.
NOTIFICATION_APPLICATION_FOCUS_IN=2016🔗
Notification received from the OS when the application is focused, i.e. when changing the focus from the OS desktop or a thirdparty application to any open window of the Godot instance.
Implemented on desktop and mobile platforms.
NOTIFICATION_APPLICATION_FOCUS_OUT=2017🔗
Notification received from the OS when the application is defocused, i.e. when changing the focus from any open window of the Godot instance to the OS desktop or a thirdparty application.
Implemented on desktop and mobile platforms.
NOTIFICATION_TEXT_SERVER_CHANGED=2018🔗
Notification received when theTextServeris changed.
NOTIFICATION_ACCESSIBILITY_UPDATE=3000🔗
Notification received when an accessibility information update is required.
NOTIFICATION_ACCESSIBILITY_INVALIDATE=3001🔗
Notification received when accessibility elements are invalidated. All node accessibility elements are automatically deleted after receiving this message, therefore all existing references to such elements should be discarded.

## Property Descriptions

AutoTranslateModeauto_translate_mode=0🔗

- voidset_auto_translate_mode(value:AutoTranslateMode)
voidset_auto_translate_mode(value:AutoTranslateMode)
- AutoTranslateModeget_auto_translate_mode()
AutoTranslateModeget_auto_translate_mode()
Defines if any text should automatically change to its translated version depending on the current locale (for nodes such asLabel,RichTextLabel,Window, etc.). Also decides if the node's strings should be parsed for translation template generation.
Note:For the root node, auto translate mode can also be set viaProjectSettings.internationalization/rendering/root_node_auto_translate.
Stringeditor_description=""🔗
- voidset_editor_description(value:String)
voidset_editor_description(value:String)
- Stringget_editor_description()
Stringget_editor_description()
An optional description to the node. It will be displayed as a tooltip when hovering over the node in the editor's Scene dock.
MultiplayerAPImultiplayer🔗
- MultiplayerAPIget_multiplayer()
MultiplayerAPIget_multiplayer()
TheMultiplayerAPIinstance associated with this node. SeeSceneTree.get_multiplayer().
Note:Renaming the node, or moving it in the tree, will not move theMultiplayerAPIto the new path, you will have to update this manually.
StringNamename🔗
- voidset_name(value:StringName)
voidset_name(value:StringName)
- StringNameget_name()
StringNameget_name()
The name of the node. This name must be unique among the siblings (other child nodes from the same parent). When set to an existing sibling's name, the node is automatically renamed.
Note:When changing the name, the following characters will be replaced with an underscore: (.:@/"%). In particular, the@character is reserved for auto-generated names. See alsoString.validate_node_name().
Nodeowner🔗
- voidset_owner(value:Node)
voidset_owner(value:Node)
- Nodeget_owner()
Nodeget_owner()
The owner of this node. The owner must be an ancestor of this node. When packing the owner node in aPackedScene, all the nodes it owns are also saved with it. See alsounique_name_in_owner.
Note:In the editor, nodes not owned by the scene root are usually not displayed in the Scene dock, and willnotbe saved. To prevent this, remember to set the owner after callingadd_child().
Note:The owner needs to be the current scene root. SeeInstancing scenesin the documentation for more information.
PhysicsInterpolationModephysics_interpolation_mode=0🔗
- voidset_physics_interpolation_mode(value:PhysicsInterpolationMode)
voidset_physics_interpolation_mode(value:PhysicsInterpolationMode)
- PhysicsInterpolationModeget_physics_interpolation_mode()
PhysicsInterpolationModeget_physics_interpolation_mode()
The physics interpolation mode to use for this node. Only effective ifProjectSettings.physics/common/physics_interpolationorSceneTree.physics_interpolationistrue.
By default, nodes inherit the physics interpolation mode from their parent. This property can enable or disable physics interpolation individually for each node, regardless of their parents' physics interpolation mode.
Note:Some node types likeVehicleWheel3Dhave physics interpolation disabled by default, as they rely on their own custom solution.
Note:When teleporting a node to a distant position, it's recommended to temporarily disable interpolation withreset_physics_interpolation()aftermoving the node. This avoids creating a visual streak between the old and new positions.
ProcessModeprocess_mode=0🔗
- voidset_process_mode(value:ProcessMode)
voidset_process_mode(value:ProcessMode)
- ProcessModeget_process_mode()
ProcessModeget_process_mode()
The node's processing behavior. To check if the node can process in its current mode, usecan_process().
intprocess_physics_priority=0🔗
- voidset_physics_process_priority(value:int)
voidset_physics_process_priority(value:int)
- intget_physics_process_priority()
intget_physics_process_priority()
Similar toprocess_prioritybut forNOTIFICATION_PHYSICS_PROCESS,_physics_process(), orNOTIFICATION_INTERNAL_PHYSICS_PROCESS.
intprocess_priority=0🔗
- voidset_process_priority(value:int)
voidset_process_priority(value:int)
- intget_process_priority()
intget_process_priority()
The node's execution order of the process callbacks (_process(),NOTIFICATION_PROCESS, andNOTIFICATION_INTERNAL_PROCESS). Nodes whose priority value islowercall their process callbacks first, regardless of tree order.
ProcessThreadGroupprocess_thread_group=0🔗
- voidset_process_thread_group(value:ProcessThreadGroup)
voidset_process_thread_group(value:ProcessThreadGroup)
- ProcessThreadGroupget_process_thread_group()
ProcessThreadGroupget_process_thread_group()
Set the process thread group for this node (basically, whether it receivesNOTIFICATION_PROCESS,NOTIFICATION_PHYSICS_PROCESS,_process()or_physics_process()(and the internal versions) on the main thread or in a sub-thread.
By default, the thread group isPROCESS_THREAD_GROUP_INHERIT, which means that this node belongs to the same thread group as the parent node. The thread groups means that nodes in a specific thread group will process together, separate to other thread groups (depending onprocess_thread_group_order). If the value is set isPROCESS_THREAD_GROUP_SUB_THREAD, this thread group will occur on a sub thread (not the main thread), otherwise if set toPROCESS_THREAD_GROUP_MAIN_THREADit will process on the main thread. If there is not a parent or grandparent node set to something other than inherit, the node will belong to thedefault thread group. This default group will process on the main thread and its group order is 0.
During processing in a sub-thread, accessing most functions in nodes outside the thread group is forbidden (and it will result in an error in debug mode). UseObject.call_deferred(),call_thread_safe(),call_deferred_thread_group()and the likes in order to communicate from the thread groups to the main thread (or to other thread groups).
To better understand process thread groups, the idea is that any node set to any other value thanPROCESS_THREAD_GROUP_INHERITwill include any child (and grandchild) nodes set to inherit into its process thread group. This means that the processing of all the nodes in the group will happen together, at the same time as the node including them.
intprocess_thread_group_order🔗
- voidset_process_thread_group_order(value:int)
voidset_process_thread_group_order(value:int)
- intget_process_thread_group_order()
intget_process_thread_group_order()
Change the process thread group order. Groups with a lesser order will process before groups with a greater order. This is useful when a large amount of nodes process in sub thread and, afterwards, another group wants to collect their result in the main thread, as an example.
BitField[ProcessThreadMessages]process_thread_messages🔗
- voidset_process_thread_messages(value:BitField[ProcessThreadMessages])
voidset_process_thread_messages(value:BitField[ProcessThreadMessages])
- BitField[ProcessThreadMessages]get_process_thread_messages()
BitField[ProcessThreadMessages]get_process_thread_messages()
Set whether the current thread group will process messages (calls tocall_deferred_thread_group()on threads), and whether it wants to receive them during regular process or physics process callbacks.
Stringscene_file_path🔗
- voidset_scene_file_path(value:String)
voidset_scene_file_path(value:String)
- Stringget_scene_file_path()
Stringget_scene_file_path()
The original scene's file path, if the node has been instantiated from aPackedScenefile. Only scene root nodes contains this.
boolunique_name_in_owner=false🔗
- voidset_unique_name_in_owner(value:bool)
voidset_unique_name_in_owner(value:bool)
- boolis_unique_name_in_owner()
boolis_unique_name_in_owner()
Iftrue, the node can be accessed from any node sharing the sameowneror from theowneritself, with special%Namesyntax inget_node().
Note:If another node with the sameownershares the samenameas this node, the other node will no longer be accessible as unique.

## Method Descriptions

void_enter_tree()virtual🔗
Called when the node enters theSceneTree(e.g. upon instantiating, scene changing, or after callingadd_child()in a script). If the node has children, its_enter_tree()callback will be called first, and then that of the children.
Corresponds to theNOTIFICATION_ENTER_TREEnotification inObject._notification().
void_exit_tree()virtual🔗
Called when the node is about to leave theSceneTree(e.g. upon freeing, scene changing, or after callingremove_child()in a script). If the node has children, its_exit_tree()callback will be called last, after all its children have left the tree.
Corresponds to theNOTIFICATION_EXIT_TREEnotification inObject._notification()and signaltree_exiting. To get notified when the node has already left the active tree, connect to thetree_exited.
PackedStringArray_get_accessibility_configuration_warnings()virtualconst🔗
The elements in the array returned from this method are displayed as warnings in the Scene dock if the script that overrides it is atoolscript, and accessibility warnings are enabled in the editor settings.
Returning an empty array produces no warnings.
PackedStringArray_get_configuration_warnings()virtualconst🔗
The elements in the array returned from this method are displayed as warnings in the Scene dock if the script that overrides it is atoolscript.
Returning an empty array produces no warnings.
Callupdate_configuration_warnings()when the warnings need to be updated for this node.

```
@export var energy = 0:
    set(value):
        energy = value
        update_configuration_warnings()

func _get_configuration_warnings():
    if energy < 0:
        return ["Energy must be 0 or greater."]
    else:
        return []
```

RID_get_focused_accessibility_element()virtualconst🔗
Called during accessibility information updates to determine the currently focused sub-element, should return a sub-element RID or the value returned byget_accessibility_element().
void_input(event:InputEvent)virtual🔗
Called when there is an input event. The input event propagates up through the node tree until a node consumes it.
It is only called if input processing is enabled, which is done automatically if this method is overridden, and can be toggled withset_process_input().
To consume the input event and stop it propagating further to other nodes,Viewport.set_input_as_handled()can be called.
For gameplay input,_unhandled_input()and_unhandled_key_input()are usually a better fit as they allow the GUI to intercept the events first.
Note:This method is only called if the node is present in the scene tree (i.e. if it's not an orphan).
void_physics_process(delta:float)virtual🔗
Called once on each physics tick, and allows Nodes to synchronize their logic with physics ticks.deltais the logical time between physics ticks in seconds and is equal toEngine.time_scale/Engine.physics_ticks_per_second.
It is only called if physics processing is enabled for this Node, which is done automatically if this method is overridden, and can be toggled withset_physics_process().
Processing happens in order ofprocess_physics_priority, lower priority values are called first. Nodes with the same priority are processed in tree order, or top to bottom as seen in the editor (also known as pre-order traversal).
Corresponds to theNOTIFICATION_PHYSICS_PROCESSnotification inObject._notification().
Note:This method is only called if the node is present in the scene tree (i.e. if it's not an orphan).
Note:Accumulateddeltamay diverge from real world seconds.
void_process(delta:float)virtual🔗
Called on each idle frame, prior to rendering, and after physics ticks have been processed.deltais the time between frames in seconds.
It is only called if processing is enabled for this Node, which is done automatically if this method is overridden, and can be toggled withset_process().
Processing happens in order ofprocess_priority, lower priority values are called first. Nodes with the same priority are processed in tree order, or top to bottom as seen in the editor (also known as pre-order traversal).
Corresponds to theNOTIFICATION_PROCESSnotification inObject._notification().
Note:This method is only called if the node is present in the scene tree (i.e. if it's not an orphan).
Note:When the engine is struggling and the frame rate is lowered,deltawill increase. Whendeltais increased, it's capped at a maximum ofEngine.time_scale*Engine.max_physics_steps_per_frame/Engine.physics_ticks_per_second. As a result, accumulateddeltamay not represent real world time.
Note:When--fixed-fpsis enabled or the engine is running in Movie Maker mode (seeMovieWriter), processdeltawill always be the same for every frame, regardless of how much time the frame took to render.
Note:Frame delta may be post-processed byOS.delta_smoothingif this is enabled for the project.
void_ready()virtual🔗
Called when the node is "ready", i.e. when both the node and its children have entered the scene tree. If the node has children, their_ready()callbacks get triggered first, and the parent node will receive the ready notification afterwards.
Corresponds to theNOTIFICATION_READYnotification inObject._notification(). See also the@onreadyannotation for variables.
Usually used for initialization. For even earlier initialization,Object._init()may be used. See also_enter_tree().
Note:This method may be called only once for each node. After removing a node from the scene tree and adding it again,_ready()willnotbe called a second time. This can be bypassed by requesting another call withrequest_ready(), which may be called anywhere before adding the node again.
void_shortcut_input(event:InputEvent)virtual🔗
Called when anInputEventKey,InputEventShortcut, orInputEventJoypadButtonhasn't been consumed by_input()or any GUIControlitem. It is called before_unhandled_key_input()and_unhandled_input(). The input event propagates up through the node tree until a node consumes it.
It is only called if shortcut processing is enabled, which is done automatically if this method is overridden, and can be toggled withset_process_shortcut_input().
To consume the input event and stop it propagating further to other nodes,Viewport.set_input_as_handled()can be called.
This method can be used to handle shortcuts. For generic GUI events, use_input()instead. Gameplay events should usually be handled with either_unhandled_input()or_unhandled_key_input().
Note:This method is only called if the node is present in the scene tree (i.e. if it's not orphan).
void_unhandled_input(event:InputEvent)virtual🔗
Called when anInputEventhasn't been consumed by_input()or any GUIControlitem. It is called after_shortcut_input()and after_unhandled_key_input(). The input event propagates up through the node tree until a node consumes it.
It is only called if unhandled input processing is enabled, which is done automatically if this method is overridden, and can be toggled withset_process_unhandled_input().
To consume the input event and stop it propagating further to other nodes,Viewport.set_input_as_handled()can be called.
For gameplay input, this method is usually a better fit than_input(), as GUI events need a higher priority. For keyboard shortcuts, consider using_shortcut_input()instead, as it is called before this method. Finally, to handle keyboard events, consider using_unhandled_key_input()for performance reasons.
Note:This method is only called if the node is present in the scene tree (i.e. if it's not an orphan).
void_unhandled_key_input(event:InputEvent)virtual🔗
Called when anInputEventKeyhasn't been consumed by_input()or any GUIControlitem. It is called after_shortcut_input()but before_unhandled_input(). The input event propagates up through the node tree until a node consumes it.
It is only called if unhandled key input processing is enabled, which is done automatically if this method is overridden, and can be toggled withset_process_unhandled_key_input().
To consume the input event and stop it propagating further to other nodes,Viewport.set_input_as_handled()can be called.
This method can be used to handle Unicode character input withAlt,Alt+Ctrl, andAlt+Shiftmodifiers, after shortcuts were handled.
For gameplay input, this and_unhandled_input()are usually a better fit than_input(), as GUI events should be handled first. This method also performs better than_unhandled_input(), since unrelated events such asInputEventMouseMotionare automatically filtered. For shortcuts, consider using_shortcut_input()instead.
Note:This method is only called if the node is present in the scene tree (i.e. if it's not an orphan).
voidadd_child(node:Node, force_readable_name:bool= false, internal:InternalMode= 0)🔗
Adds a childnode. Nodes can have any number of children, but every child must have a unique name. Child nodes are automatically deleted when the parent node is deleted, so an entire scene can be removed by deleting its topmost node.
Ifforce_readable_nameistrue, improves the readability of the addednode. If not named, thenodeis renamed to its type, and if it sharesnamewith a sibling, a number is suffixed more appropriately. This operation is very slow. As such, it is recommended leaving this tofalse, which assigns a dummy name featuring@in both situations.
Ifinternalis different thanINTERNAL_MODE_DISABLED, the child will be added as internal node. These nodes are ignored by methods likeget_children(), unless their parameterinclude_internalistrue. It also prevents these nodes being duplicated with their parent. The intended usage is to hide the internal nodes from the user, so the user won't accidentally delete or modify them. Used by some GUI nodes, e.g.ColorPicker.
Note:Ifnodealready has a parent, this method will fail. Useremove_child()first to removenodefrom its current parent. For example:

```
var child_node = get_child(0)
if child_node.get_parent():
    child_node.get_parent().remove_child(child_node)
add_child(child_node)
```

```
Node childNode = GetChild(0);
if (childNode.GetParent() != null)
{
    childNode.GetParent().RemoveChild(childNode);
}
AddChild(childNode);
```

If you need the child node to be added below a specific node in the list of children, useadd_sibling()instead of this method.
Note:If you want a child to be persisted to aPackedScene, you must setownerin addition to callingadd_child(). This is typically relevant fortool scriptsandeditor plugins. Ifadd_child()is called without settingowner, the newly addedNodewill not be visible in the scene tree, though it will be visible in the 2D/3D view.
voidadd_sibling(sibling:Node, force_readable_name:bool= false)🔗
Adds asiblingnode to this node's parent, and moves the added sibling right below this node.
Ifforce_readable_nameistrue, improves the readability of the addedsibling. If not named, thesiblingis renamed to its type, and if it sharesnamewith a sibling, a number is suffixed more appropriately. This operation is very slow. As such, it is recommended leaving this tofalse, which assigns a dummy name featuring@in both situations.
Useadd_child()instead of this method if you don't need the child node to be added below a specific node in the list of children.
Note:If this node is internal, the added sibling will be internal too (seeadd_child()'sinternalparameter).
voidadd_to_group(group:StringName, persistent:bool= false)🔗
Adds the node to thegroup. Groups can be helpful to organize a subset of nodes, for example"enemies"or"collectables". See notes in the description, and the group methods inSceneTree.
Ifpersistentistrue, the group will be stored when saved inside aPackedScene. All groups created and displayed in the Groups dock are persistent.
Note:To improve performance, the order of group names isnotguaranteed and may vary between project runs. Therefore, do not rely on the group order.
Note:SceneTree's group methods willnotwork on this node if not inside the tree (seeis_inside_tree()).
Stringatr(message:String, context:StringName= "")const🔗
Translates amessage, using the translation catalogs configured in the Project Settings. Furthercontextcan be specified to help with the translation. Note that mostControlnodes automatically translate their strings, so this method is mostly useful for formatted strings or custom drawn text.
This method works the same asObject.tr(), with the addition of respecting theauto_translate_modestate.
IfObject.can_translate_messages()isfalse, or no translation is available, this method returns themessagewithout changes. SeeObject.set_message_translation().
For detailed examples, seeInternationalizing games.
Stringatr_n(message:String, plural_message:StringName, n:int, context:StringName= "")const🔗
Translates amessageorplural_message, using the translation catalogs configured in the Project Settings. Furthercontextcan be specified to help with the translation.
This method works the same asObject.tr_n(), with the addition of respecting theauto_translate_modestate.
IfObject.can_translate_messages()isfalse, or no translation is available, this method returnsmessageorplural_message, without changes. SeeObject.set_message_translation().
Thenis the number, or amount, of the message's subject. It is used by the translation system to fetch the correct plural form for the current language.
For detailed examples, seeLocalization using gettext.
Note:Negative andfloatnumbers may not properly apply to some countable subjects. It's recommended to handle these cases withatr().
Variantcall_deferred_thread_group(method:StringName, ...)vararg🔗
This function is similar toObject.call_deferred()except that the call will take place when the node thread group is processed. If the node thread group processes in sub-threads, then the call will be done on that thread, right beforeNOTIFICATION_PROCESSorNOTIFICATION_PHYSICS_PROCESS, the_process()or_physics_process()or their internal versions are called.
Variantcall_thread_safe(method:StringName, ...)vararg🔗
This function ensures that the calling of this function will succeed, no matter whether it's being done from a thread or not. If called from a thread that is not allowed to call the function, the call will become deferred. Otherwise, the call will go through directly.
boolcan_auto_translate()const🔗
Returnstrueif this node can automatically translate messages depending on the current locale. Seeauto_translate_mode,atr(), andatr_n().
boolcan_process()const🔗
Returnstrueif the node can receive processing notifications and input callbacks (NOTIFICATION_PROCESS,_input(), etc.) from theSceneTreeandViewport. The returned value depends onprocess_mode:

- If set toPROCESS_MODE_PAUSABLE, returnstruewhen the game is processing, i.e.SceneTree.pausedisfalse;
If set toPROCESS_MODE_PAUSABLE, returnstruewhen the game is processing, i.e.SceneTree.pausedisfalse;
- If set toPROCESS_MODE_WHEN_PAUSED, returnstruewhen the game is paused, i.e.SceneTree.pausedistrue;
If set toPROCESS_MODE_WHEN_PAUSED, returnstruewhen the game is paused, i.e.SceneTree.pausedistrue;
- If set toPROCESS_MODE_ALWAYS, always returnstrue;
If set toPROCESS_MODE_ALWAYS, always returnstrue;
- If set toPROCESS_MODE_DISABLED, always returnsfalse;
If set toPROCESS_MODE_DISABLED, always returnsfalse;
- If set toPROCESS_MODE_INHERIT, use the parent node'sprocess_modeto determine the result.
If set toPROCESS_MODE_INHERIT, use the parent node'sprocess_modeto determine the result.
If the node is not inside the tree, returnsfalseno matter the value ofprocess_mode.
Tweencreate_tween()🔗
Creates a newTweenand binds it to this node.
This is the equivalent of doing:

```
get_tree().create_tween().bind_node(self)
```

```
GetTree().CreateTween().BindNode(this);
```

The Tween will start automatically on the next process frame or physics frame (depending onTweenProcessMode). SeeTween.bind_node()for more info on Tweens bound to nodes.
Note:The method can still be used when the node is not insideSceneTree. It can fail in an unlikely case of using a customMainLoop.
Nodeduplicate(flags:int= 15)const🔗
Duplicates the node, returning a new node with all of its properties, signals, groups, and children copied from the original, recursively. The behavior can be tweaked through theflags(seeDuplicateFlags). Internal nodes are not duplicated.
Note:For nodes with aScriptattached, ifObject._init()has been defined with required parameters, the duplicated node will not have aScript.
Note:By default, this method will duplicate only properties marked for serialization (i.e. using@GlobalScope.PROPERTY_USAGE_STORAGE, or in GDScript,@GDScript.@export). If you want to duplicate all properties, useDUPLICATE_INTERNAL_STATE.
Nodefind_child(pattern:String, recursive:bool= true, owned:bool= true)const🔗
Finds the first descendant of this node whosenamematchespattern, returningnullif no match is found. The matching is done against node names,nottheir paths, throughString.match(). As such, it is case-sensitive,"*"matches zero or more characters, and"?"matches any single character.
Ifrecursiveisfalse, only this node's direct children are checked. Nodes are checked in tree order, so this node's first direct child is checked first, then its own direct children, etc., before moving to the second direct child, and so on. Internal children are also included in the search (seeinternalparameter inadd_child()).
Ifownedistrue, only descendants with a validownernode are checked.
Note:This method can be very slow. Consider storing a reference to the found node in a variable. Alternatively, useget_node()with unique names (seeunique_name_in_owner).
Note:To find all descendant nodes matching a pattern or a class type, seefind_children().
Array[Node]find_children(pattern:String, type:String= "", recursive:bool= true, owned:bool= true)const🔗
Finds all descendants of this node whose names matchpattern, returning an emptyArrayif no match is found. The matching is done against node names,nottheir paths, throughString.match(). As such, it is case-sensitive,"*"matches zero or more characters, and"?"matches any single character.
Iftypeis not empty, only ancestors inheriting fromtypeare included (seeObject.is_class()).
Ifrecursiveisfalse, only this node's direct children are checked. Nodes are checked in tree order, so this node's first direct child is checked first, then its own direct children, etc., before moving to the second direct child, and so on. Internal children are also included in the search (seeinternalparameter inadd_child()).
Ifownedistrue, only descendants with a validownernode are checked.
Note:This method can be very slow. Consider storing references to the found nodes in a variable.
Note:To find a single descendant node matching a pattern, seefind_child().
Nodefind_parent(pattern:String)const🔗
Finds the first ancestor of this node whosenamematchespattern, returningnullif no match is found. The matching is done throughString.match(). As such, it is case-sensitive,"*"matches zero or more characters, and"?"matches any single character. See alsofind_child()andfind_children().
Note:As this method walks upwards in the scene tree, it can be slow in large, deeply nested nodes. Consider storing a reference to the found node in a variable. Alternatively, useget_node()with unique names (seeunique_name_in_owner).
RIDget_accessibility_element()const🔗
Returns main accessibility element RID.
Note:This method should be called only during accessibility information updates (NOTIFICATION_ACCESSIBILITY_UPDATE).
Nodeget_child(idx:int, include_internal:bool= false)const🔗
Fetches a child node by its index. Each child node has an index relative to its siblings (seeget_index()). The first child is at index 0. Negative values can also be used to start from the end of the list. This method can be used in combination withget_child_count()to iterate over this node's children. If no child exists at the given index, this method returnsnulland an error is generated.
Ifinclude_internalisfalse, internal children are ignored (seeadd_child()'sinternalparameter).

```
# Assuming the following are children of this node, in order:
# First, Middle, Last.

var a = get_child(0).name  # a is "First"
var b = get_child(1).name  # b is "Middle"
var b = get_child(2).name  # b is "Last"
var c = get_child(-1).name # c is "Last"
```

Note:To fetch a node byNodePath, useget_node().
intget_child_count(include_internal:bool= false)const🔗
Returns the number of children of this node.
Ifinclude_internalisfalse, internal children are not counted (seeadd_child()'sinternalparameter).
Array[Node]get_children(include_internal:bool= false)const🔗
Returns all children of this node inside anArray.
Ifinclude_internalisfalse, excludes internal children from the returned array (seeadd_child()'sinternalparameter).
Array[StringName]get_groups()const🔗
Returns anArrayof group names that the node has been added to.
Note:To improve performance, the order of group names isnotguaranteed and may vary between project runs. Therefore, do not rely on the group order.
Note:This method may also return some group names starting with an underscore (_). These are internally used by the engine. To avoid conflicts, do not use custom groups starting with underscores. To exclude internal groups, see the following code snippet:

```
# Stores the node's non-internal groups only (as an array of StringNames).
var non_internal_groups = []
for group in get_groups():
    if not str(group).begins_with("_"):
        non_internal_groups.push_back(group)
```

```
// Stores the node's non-internal groups only (as a List of StringNames).
List<string> nonInternalGroups = new List<string>();
foreach (string group in GetGroups())
{
    if (!group.BeginsWith("_"))
        nonInternalGroups.Add(group);
}
```

intget_index(include_internal:bool= false)const🔗
Returns this node's order among its siblings. The first node's index is0. See alsoget_child().
Ifinclude_internalisfalse, returns the index ignoring internal children. The first, non-internal child will have an index of0(seeadd_child()'sinternalparameter).
Windowget_last_exclusive_window()const🔗
Returns theWindowthat contains this node, or the last exclusive child in a chain of windows starting with the one that contains this node.
intget_multiplayer_authority()const🔗
Returns the peer ID of the multiplayer authority for this node. Seeset_multiplayer_authority().
Nodeget_node(path:NodePath)const🔗
Fetches a node. TheNodePathcan either be a relative path (from this node), or an absolute path (from theSceneTree.root) to a node. Ifpathdoes not point to a valid node, generates an error and returnsnull. Attempts to access methods on the return value will result in an"Attempt to call <method> on a null instance."error.
Note:Fetching by absolute path only works when the node is inside the scene tree (seeis_inside_tree()).
Example:Assume this method is called from the Character node, inside the following tree:

```
┖╴root
   ┠╴Character (you are here!)
   ┃  ┠╴Sword
   ┃  ┖╴Backpack
   ┃     ┖╴Dagger
   ┠╴MyGame
   ┖╴Swamp
      ┠╴Alligator
      ┠╴Mosquito
      ┖╴Goblin
```

The following calls will return a valid node:

```
get_node("Sword")
get_node("Backpack/Dagger")
get_node("../Swamp/Alligator")
get_node("/root/MyGame")
```

```
GetNode("Sword");
GetNode("Backpack/Dagger");
GetNode("../Swamp/Alligator");
GetNode("/root/MyGame");
```

Arrayget_node_and_resource(path:NodePath)🔗
Fetches a node and its most nested resource as specified by theNodePath's subname. Returns anArrayof size3where:

- Element0is theNode, ornullif not found;
Element0is theNode, ornullif not found;
- Element1is the subname's last nestedResource, ornullif not found;
Element1is the subname's last nestedResource, ornullif not found;
- Element2is the remainingNodePath, referring to an existing, non-Resourceproperty (seeObject.get_indexed()).
Element2is the remainingNodePath, referring to an existing, non-Resourceproperty (seeObject.get_indexed()).
Example:Assume that the child'sSprite2D.texturehas been assigned anAtlasTexture:

```
var a = get_node_and_resource("Area2D/Sprite2D")
print(a[0].name) # Prints Sprite2D
print(a[1])      # Prints <null>
print(a[2])      # Prints ^""

var b = get_node_and_resource("Area2D/Sprite2D:texture:atlas")
print(b[0].name)        # Prints Sprite2D
print(b[1].get_class()) # Prints AtlasTexture
print(b[2])             # Prints ^""

var c = get_node_and_resource("Area2D/Sprite2D:texture:atlas:region")
print(c[0].name)        # Prints Sprite2D
print(c[1].get_class()) # Prints AtlasTexture
print(c[2])             # Prints ^":region"
```

```
var a = GetNodeAndResource(NodePath("Area2D/Sprite2D"));
GD.Print(a[0].Name); // Prints Sprite2D
GD.Print(a[1]);      // Prints <null>
GD.Print(a[2]);      // Prints ^"

var b = GetNodeAndResource(NodePath("Area2D/Sprite2D:texture:atlas"));
GD.Print(b[0].name);        // Prints Sprite2D
GD.Print(b[1].get_class()); // Prints AtlasTexture
GD.Print(b[2]);             // Prints ^""

var c = GetNodeAndResource(NodePath("Area2D/Sprite2D:texture:atlas:region"));
GD.Print(c[0].name);        // Prints Sprite2D
GD.Print(c[1].get_class()); // Prints AtlasTexture
GD.Print(c[2]);             // Prints ^":region"
```

Nodeget_node_or_null(path:NodePath)const🔗
Fetches a node byNodePath. Similar toget_node(), but does not generate an error ifpathdoes not point to a valid node.
Variantget_node_rpc_config()const🔗
Returns aDictionarymapping method names to their RPC configuration defined for this node usingrpc_config().
Note:This method only returns the RPC configuration assigned viarpc_config(). SeeScript.get_rpc_config()to retrieve the RPCs defined by theScript.
Array[int]get_orphan_node_ids()static🔗
Returns object IDs of all orphan nodes (nodes outside theSceneTree). Used for debugging.
Note:get_orphan_node_ids()only works in debug builds. When called in a project exported in release mode,get_orphan_node_ids()will return an empty array.
Nodeget_parent()const🔗
Returns this node's parent node, ornullif the node doesn't have a parent.
NodePathget_path()const🔗
Returns the node's absolute path, relative to theSceneTree.root. If the node is not inside the scene tree, this method fails and returns an emptyNodePath.
NodePathget_path_to(node:Node, use_unique_path:bool= false)const🔗
Returns the relativeNodePathfrom this node to the specifiednode. Both nodes must be in the sameSceneTreeor scene hierarchy, otherwise this method fails and returns an emptyNodePath.
Ifuse_unique_pathistrue, returns the shortest path accounting for this node's unique name (seeunique_name_in_owner).
Note:If you get a relative path which starts from a unique node, the path may be longer than a normal relative path, due to the addition of the unique node's name.
floatget_physics_process_delta_time()const🔗
Returns the time elapsed (in seconds) since the last physics callback. This value is identical to_physics_process()'sdeltaparameter, and is often consistent at run-time, unlessEngine.physics_ticks_per_secondis changed. See alsoNOTIFICATION_PHYSICS_PROCESS.
Note:The returned value will be larger than expected if running at a framerate lower thanEngine.physics_ticks_per_second/Engine.max_physics_steps_per_frameFPS. This is done to avoid "spiral of death" scenarios where performance would plummet due to an ever-increasing number of physics steps per frame. This behavior affects both_process()and_physics_process(). As a result, avoid usingdeltafor time measurements in real-world seconds. Use theTimesingleton's methods for this purpose instead, such asTime.get_ticks_usec().
floatget_process_delta_time()const🔗
Returns the time elapsed (in seconds) since the last process callback. This value is identical to_process()'sdeltaparameter, and may vary from frame to frame. See alsoNOTIFICATION_PROCESS.
Note:The returned value will be larger than expected if running at a framerate lower thanEngine.physics_ticks_per_second/Engine.max_physics_steps_per_frameFPS. This is done to avoid "spiral of death" scenarios where performance would plummet due to an ever-increasing number of physics steps per frame. This behavior affects both_process()and_physics_process(). As a result, avoid usingdeltafor time measurements in real-world seconds. Use theTimesingleton's methods for this purpose instead, such asTime.get_ticks_usec().
boolget_scene_instance_load_placeholder()const🔗
Returnstrueif this node is an instance load placeholder. SeeInstancePlaceholderandset_scene_instance_load_placeholder().
SceneTreeget_tree()const🔗
Returns theSceneTreethat contains this node. If this node is not inside the tree, generates an error and returnsnull. See alsois_inside_tree().
Stringget_tree_string()🔗
Returns the tree as aString. Used mainly for debugging purposes. This version displays the path relative to the current node, and is good for copy/pasting into theget_node()function. It also can be used in game UI/UX.
May print, for example:

```
TheGame
TheGame/Menu
TheGame/Menu/Label
TheGame/Menu/Camera2D
TheGame/SplashScreen
TheGame/SplashScreen/Camera2D
```

Stringget_tree_string_pretty()🔗
Similar toget_tree_string(), this returns the tree as aString. This version displays a more graphical representation similar to what is displayed in the Scene Dock. It is useful for inspecting larger trees.
May print, for example:

```
┖╴TheGame
   ┠╴Menu
   ┃  ┠╴Label
   ┃  ┖╴Camera2D
   ┖╴SplashScreen
      ┖╴Camera2D
```

Viewportget_viewport()const🔗
Returns the node's closestViewportancestor, if the node is inside the tree. Otherwise, returnsnull.
Windowget_window()const🔗
Returns theWindowthat contains this node. If the node is in the main window, this is equivalent to getting the root node (get_tree().get_root()).
boolhas_node(path:NodePath)const🔗
Returnstrueif thepathpoints to a valid node. See alsoget_node().
boolhas_node_and_resource(path:NodePath)const🔗
Returnstrueifpathpoints to a valid node and its subnames point to a validResource, e.g.Area2D/CollisionShape2D:shape. Properties that are notResourcetypes (such as nodes or otherVarianttypes) are not considered. See alsoget_node_and_resource().
boolis_ancestor_of(node:Node)const🔗
Returnstrueif the givennodeis a direct or indirect child of this node.
boolis_displayed_folded()const🔗
Returnstrueif the node is folded (collapsed) in the Scene dock. This method is intended to be used in editor plugins and tools. See alsoset_display_folded().
boolis_editable_instance(node:Node)const🔗
Returnstrueifnodehas editable children enabled relative to this node. This method is intended to be used in editor plugins and tools. See alsoset_editable_instance().
boolis_greater_than(node:Node)const🔗
Returnstrueif the givennodeoccurs later in the scene hierarchy than this node. A node occurring later is usually processed last.
boolis_in_group(group:StringName)const🔗
Returnstrueif this node has been added to the givengroup. Seeadd_to_group()andremove_from_group(). See also notes in the description, and theSceneTree's group methods.
boolis_inside_tree()const🔗
Returnstrueif this node is currently inside aSceneTree. See alsoget_tree().
boolis_multiplayer_authority()const🔗
Returnstrueif the local system is the multiplayer authority of this node.
boolis_node_ready()const🔗
Returnstrueif the node is ready, i.e. it's inside scene tree and all its children are initialized.
request_ready()resets it back tofalse.
boolis_part_of_edited_scene()const🔗
Returnstrueif the node is part of the scene currently opened in the editor.
boolis_physics_interpolated()const🔗
Returnstrueif physics interpolation is enabled for this node (seephysics_interpolation_mode).
Note:Interpolation will only be active if both the flag is setandphysics interpolation is enabled within theSceneTree. This can be tested usingis_physics_interpolated_and_enabled().
boolis_physics_interpolated_and_enabled()const🔗
Returnstrueif physics interpolation is enabled (seephysics_interpolation_mode)andenabled in theSceneTree.
This is a convenience version ofis_physics_interpolated()that also checks whether physics interpolation is enabled globally.
SeeSceneTree.physics_interpolationandProjectSettings.physics/common/physics_interpolation.
boolis_physics_processing()const🔗
Returnstrueif physics processing is enabled (seeset_physics_process()).
boolis_physics_processing_internal()const🔗
Returnstrueif internal physics processing is enabled (seeset_physics_process_internal()).
boolis_processing()const🔗
Returnstrueif processing is enabled (seeset_process()).
boolis_processing_input()const🔗
Returnstrueif the node is processing input (seeset_process_input()).
boolis_processing_internal()const🔗
Returnstrueif internal processing is enabled (seeset_process_internal()).
boolis_processing_shortcut_input()const🔗
Returnstrueif the node is processing shortcuts (seeset_process_shortcut_input()).
boolis_processing_unhandled_input()const🔗
Returnstrueif the node is processing unhandled input (seeset_process_unhandled_input()).
boolis_processing_unhandled_key_input()const🔗
Returnstrueif the node is processing unhandled key input (seeset_process_unhandled_key_input()).
voidmove_child(child_node:Node, to_index:int)🔗
Moveschild_nodeto the given index. A node's index is the order among its siblings. Ifto_indexis negative, the index is counted from the end of the list. See alsoget_child()andget_index().
Note:The processing order of several engine callbacks (_ready(),_process(), etc.) and notifications sent throughpropagate_notification()is affected by tree order.CanvasItemnodes are also rendered in tree order. See alsoprocess_priority.
voidnotify_deferred_thread_group(what:int)🔗
Similar tocall_deferred_thread_group(), but for notifications.
voidnotify_thread_safe(what:int)🔗
Similar tocall_thread_safe(), but for notifications.
voidprint_orphan_nodes()static🔗
Prints all orphan nodes (nodes outside theSceneTree). Useful for debugging.
Note:This method only works in debug builds. It does nothing in a project exported in release mode.
voidprint_tree()🔗
Prints the node and its children to the console, recursively. The node does not have to be inside the tree. This method outputsNodePaths relative to this node, and is good for copy/pasting intoget_node(). See alsoprint_tree_pretty().
May print, for example:

```
.
Menu
Menu/Label
Menu/Camera2D
SplashScreen
SplashScreen/Camera2D
```

voidprint_tree_pretty()🔗
Prints the node and its children to the console, recursively. The node does not have to be inside the tree. Similar toprint_tree(), but the graphical representation looks like what is displayed in the editor's Scene dock. It is useful for inspecting larger trees.
May print, for example:

```
┖╴TheGame
   ┠╴Menu
   ┃  ┠╴Label
   ┃  ┖╴Camera2D
   ┖╴SplashScreen
      ┖╴Camera2D
```

voidpropagate_call(method:StringName, args:Array= [], parent_first:bool= false)🔗
Calls the givenmethodname, passingargsas arguments, on this node and all of its children, recursively.
Ifparent_firstistrue, the method is called on this node first, then on all of its children. Iffalse, the children's methods are called first.
voidpropagate_notification(what:int)🔗
CallsObject.notification()withwhaton this node and all of its children, recursively.
voidqueue_accessibility_update()🔗
Queues an accessibility information update for this node.
voidqueue_free()🔗
Queues this node to be deleted at the end of the current frame. When deleted, all of its children are deleted as well, and all references to the node and its children become invalid.
Unlike withObject.free(), the node is not deleted instantly, and it can still be accessed before deletion. It is also safe to callqueue_free()multiple times. UseObject.is_queued_for_deletion()to check if the node will be deleted at the end of the frame.
Note:The node will only be freed after all other deferred calls are finished. Using this method is not always the same as callingObject.free()throughObject.call_deferred().
voidremove_child(node:Node)🔗
Removes a childnode. Thenode, along with its children, arenotdeleted. To delete a node, seequeue_free().
Note:When this node is inside the tree, this method sets theownerof the removednode(or its descendants) tonull, if theirowneris no longer an ancestor (seeis_ancestor_of()).
voidremove_from_group(group:StringName)🔗
Removes the node from the givengroup. Does nothing if the node is not in thegroup. See also notes in the description, and theSceneTree's group methods.
voidreparent(new_parent:Node, keep_global_transform:bool= true)🔗
Changes the parent of thisNodeto thenew_parent. The node needs to already have a parent. The node'sowneris preserved if its owner is still reachable from the new location (i.e., the node is still a descendant of the new parent after the operation).
Ifkeep_global_transformistrue, the node's global transform will be preserved if supported.Node2D,Node3DandControlsupport this argument (butControlkeeps only position).
voidreplace_by(node:Node, keep_groups:bool= false)🔗
Replaces this node by the givennode. All children of this node are moved tonode.
Ifkeep_groupsistrue, thenodeis added to the same groups that the replaced node is in (seeadd_to_group()).
Warning:The replaced node is removed from the tree, but it isnotdeleted. To prevent memory leaks, store a reference to the node in a variable, or useObject.free().
voidrequest_ready()🔗
Requests_ready()to be called again the next time the node enters the tree. Doesnotimmediately call_ready().
Note:This method only affects the current node. If the node's children also need to request ready, this method needs to be called for each one of them. When the node and its children enter the tree again, the order of_ready()callbacks will be the same as normal.
voidreset_physics_interpolation()🔗
When physics interpolation is active, moving a node to a radically different transform (such as placement within a level) can result in a visible glitch as the object is rendered moving from the old to new position over the physics tick.
That glitch can be prevented by calling this method, which temporarily disables interpolation until the physics tick is complete.
The notificationNOTIFICATION_RESET_PHYSICS_INTERPOLATIONwill be received by the node and all children recursively.
Note:This function should be calledaftermoving the node, rather than before.
Errorrpc(method:StringName, ...)vararg🔗
Sends a remote procedure call request for the givenmethodto peers on the network (and locally), sending additional arguments to the method called by the RPC. The call request will only be received by nodes with the sameNodePath, including the exact samename. Behavior depends on the RPC configuration for the givenmethod(seerpc_config()and@GDScript.@rpc). By default, methods are not exposed to RPCs.
May return@GlobalScope.OKif the call is successful,@GlobalScope.ERR_INVALID_PARAMETERif the arguments passed in themethoddo not match,@GlobalScope.ERR_UNCONFIGUREDif the node'smultiplayercannot be fetched (such as when the node is not inside the tree),@GlobalScope.ERR_CONNECTION_ERRORifmultiplayer's connection is not available.
Note:You can only safely use RPCs on clients after you received theMultiplayerAPI.connected_to_serversignal from theMultiplayerAPI. You also need to keep track of the connection state, either by theMultiplayerAPIsignals likeMultiplayerAPI.server_disconnectedor by checking (get_multiplayer().peer.get_connection_status()==CONNECTION_CONNECTED).
voidrpc_config(method:StringName, config:Variant)🔗
Changes the RPC configuration for the givenmethod.configshould either benullto disable the feature (as by default), or aDictionarycontaining the following entries:

- rpc_mode: seeRPCMode;
rpc_mode: seeRPCMode;
- transfer_mode: seeTransferMode;
transfer_mode: seeTransferMode;
- call_local: iftrue, the method will also be called locally;
call_local: iftrue, the method will also be called locally;
- channel: anintrepresenting the channel to send the RPC on.
channel: anintrepresenting the channel to send the RPC on.
Note:In GDScript, this method corresponds to the@GDScript.@rpcannotation, with various parameters passed (@rpc(any),@rpc(authority)...). See also thehigh-level multiplayertutorial.
Errorrpc_id(peer_id:int, method:StringName, ...)vararg🔗
Sends arpc()to a specific peer identified bypeer_id(seeMultiplayerPeer.set_target_peer()).
May return@GlobalScope.OKif the call is successful,@GlobalScope.ERR_INVALID_PARAMETERif the arguments passed in themethoddo not match,@GlobalScope.ERR_UNCONFIGUREDif the node'smultiplayercannot be fetched (such as when the node is not inside the tree),@GlobalScope.ERR_CONNECTION_ERRORifmultiplayer's connection is not available.
voidset_deferred_thread_group(property:StringName, value:Variant)🔗
Similar tocall_deferred_thread_group(), but for setting properties.
voidset_display_folded(fold:bool)🔗
If set totrue, the node appears folded in the Scene dock. As a result, all of its children are hidden. This method is intended to be used in editor plugins and tools, but it also works in release builds. See alsois_displayed_folded().
voidset_editable_instance(node:Node, is_editable:bool)🔗
Set totrueto allow all nodes owned bynodeto be available, and editable, in the Scene dock, even if theirowneris not the scene root. This method is intended to be used in editor plugins and tools, but it also works in release builds. See alsois_editable_instance().
voidset_multiplayer_authority(id:int, recursive:bool= true)🔗
Sets the node's multiplayer authority to the peer with the given peerid. The multiplayer authority is the peer that has authority over the node on the network. Defaults to peer ID 1 (the server). Useful in conjunction withrpc_config()and theMultiplayerAPI.
Ifrecursiveistrue, the given peer is recursively set as the authority for all children of this node.
Warning:This doesnotautomatically replicate the new authority to other peers. It is the developer's responsibility to do so. You may replicate the new authority's information usingMultiplayerSpawner.spawn_function, an RPC, or aMultiplayerSynchronizer. Furthermore, the parent's authority doesnotpropagate to newly added children.
voidset_physics_process(enable:bool)🔗
If set totrue, enables physics (fixed framerate) processing. When a node is being processed, it will receive aNOTIFICATION_PHYSICS_PROCESSat a fixed (usually 60 FPS, seeEngine.physics_ticks_per_secondto change) interval (and the_physics_process()callback will be called if it exists).
Note:If_physics_process()is overridden, this will be automatically enabled before_ready()is called.
voidset_physics_process_internal(enable:bool)🔗
If set totrue, enables internal physics for this node. Internal physics processing happens in isolation from the normal_physics_process()calls and is used by some nodes internally to guarantee proper functioning even if the node is paused or physics processing is disabled for scripting (set_physics_process()).
Warning:Built-in nodes rely on internal processing for their internal logic. Disabling it is unsafe and may lead to unexpected behavior. Use this method if you know what you are doing.
voidset_process(enable:bool)🔗
If set totrue, enables processing. When a node is being processed, it will receive aNOTIFICATION_PROCESSon every drawn frame (and the_process()callback will be called if it exists).
Note:If_process()is overridden, this will be automatically enabled before_ready()is called.
Note:This method only affects the_process()callback, i.e. it has no effect on other callbacks like_physics_process(). If you want to disable all processing for the node, setprocess_modetoPROCESS_MODE_DISABLED.
voidset_process_input(enable:bool)🔗
If set totrue, enables input processing.
Note:If_input()is overridden, this will be automatically enabled before_ready()is called. Input processing is also already enabled for GUI controls, such asButtonandTextEdit.
voidset_process_internal(enable:bool)🔗
If set totrue, enables internal processing for this node. Internal processing happens in isolation from the normal_process()calls and is used by some nodes internally to guarantee proper functioning even if the node is paused or processing is disabled for scripting (set_process()).
Warning:Built-in nodes rely on internal processing for their internal logic. Disabling it is unsafe and may lead to unexpected behavior. Use this method if you know what you are doing.
voidset_process_shortcut_input(enable:bool)🔗
If set totrue, enables shortcut processing for this node.
Note:If_shortcut_input()is overridden, this will be automatically enabled before_ready()is called.
voidset_process_unhandled_input(enable:bool)🔗
If set totrue, enables unhandled input processing. It enables the node to receive all input that was not previously handled (usually by aControl).
Note:If_unhandled_input()is overridden, this will be automatically enabled before_ready()is called. Unhandled input processing is also already enabled for GUI controls, such asButtonandTextEdit.
voidset_process_unhandled_key_input(enable:bool)🔗
If set totrue, enables unhandled key input processing.
Note:If_unhandled_key_input()is overridden, this will be automatically enabled before_ready()is called.
voidset_scene_instance_load_placeholder(load_placeholder:bool)🔗
If set totrue, the node becomes anInstancePlaceholderwhen packed and instantiated from aPackedScene. See alsoget_scene_instance_load_placeholder().
voidset_thread_safe(property:StringName, value:Variant)🔗
Similar tocall_thread_safe(), but for setting properties.
voidset_translation_domain_inherited()🔗
Makes this node inherit the translation domain from its parent node. If this node has no parent, the main translation domain will be used.
This is the default behavior for all nodes. CallingObject.set_translation_domain()disables this behavior.
voidupdate_configuration_warnings()🔗
Refreshes the warnings displayed for this node in the Scene dock. Use_get_configuration_warnings()to customize the warning messages to display.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
