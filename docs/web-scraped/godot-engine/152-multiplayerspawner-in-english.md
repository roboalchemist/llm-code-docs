# MultiplayerSpawner in English

# MultiplayerSpawner
Inherits:Node<Object
Automatically replicates spawnable nodes from the authority to other multiplayer peers.

## Description
Spawnable scenes can be configured in the editor or through code (seeadd_spawnable_scene()).
Also supports custom node spawns throughspawn(), callingspawn_functionon all peers.
Internally,MultiplayerSpawnerusesMultiplayerAPI.object_configuration_add()to notify spawns passing the spawned node as theobjectand itself as theconfiguration, andMultiplayerAPI.object_configuration_remove()to notify despawns in a similar way.

## Properties

| Callable | spawn_function |  |
|---|---|---|
| int | spawn_limit | 0 |
| NodePath | spawn_path | NodePath("") |

Callable
spawn_function
spawn_limit
NodePath
spawn_path
NodePath("")

## Methods

| void | add_spawnable_scene(path:String) |
|---|---|
| void | clear_spawnable_scenes() |
| String | get_spawnable_scene(index:int)const |
| int | get_spawnable_scene_count()const |
| Node | spawn(data:Variant= null) |

void
add_spawnable_scene(path:String)
void
clear_spawnable_scenes()
String
get_spawnable_scene(index:int)const
get_spawnable_scene_count()const
Node
spawn(data:Variant= null)

## Signals
despawned(node:Node)🔗
Emitted when a spawnable scene or custom spawn was despawned by the multiplayer authority. Only called on remote peers.
spawned(node:Node)🔗
Emitted when a spawnable scene or custom spawn was spawned by the multiplayer authority. Only called on remote peers.

## Property Descriptions
Callablespawn_function🔗
- voidset_spawn_function(value:Callable)
voidset_spawn_function(value:Callable)
- Callableget_spawn_function()
Callableget_spawn_function()
Method called on all peers when a customspawn()is requested by the authority. Will receive thedataparameter, and should return aNodethat is not in the scene tree.
Note:The returned node shouldnotbe added to the scene withNode.add_child(). This is done automatically.
intspawn_limit=0🔗
- voidset_spawn_limit(value:int)
voidset_spawn_limit(value:int)
- intget_spawn_limit()
intget_spawn_limit()
Maximum number of nodes allowed to be spawned by this spawner. Includes both spawnable scenes and custom spawns.
When set to0(the default), there is no limit.
NodePathspawn_path=NodePath("")🔗
- voidset_spawn_path(value:NodePath)
voidset_spawn_path(value:NodePath)
- NodePathget_spawn_path()
NodePathget_spawn_path()
Path to the spawn root. Spawnable scenes that are added as direct children are replicated to other peers.

## Method Descriptions
voidadd_spawnable_scene(path:String)🔗
Adds a scene path to spawnable scenes, making it automatically replicated from the multiplayer authority to other peers when added as children of the node pointed byspawn_path.
voidclear_spawnable_scenes()🔗
Clears all spawnable scenes. Does not despawn existing instances on remote peers.
Stringget_spawnable_scene(index:int)const🔗
Returns the spawnable scene path by index.
intget_spawnable_scene_count()const🔗
Returns the count of spawnable scene paths.
Nodespawn(data:Variant= null)🔗
Requests a custom spawn, withdatapassed tospawn_functionon all peers. Returns the locally spawned node instance already inside the scene tree, and added as a child of the node pointed byspawn_path.
Note:Spawnable scenes are spawned automatically.spawn()is only needed for custom spawns.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.