:github_url: hide

> **META**
	:keywords: network



# MultiplayerSpawner

**Inherits:** [Node<class_Node>] **<** [Object<class_Object>]

Automatically replicates spawnable nodes from the authority to other multiplayer peers.


## Description

Spawnable scenes can be configured in the editor or through code (see [add_spawnable_scene()<class_MultiplayerSpawner_method_add_spawnable_scene>]).

Also supports custom node spawns through [spawn()<class_MultiplayerSpawner_method_spawn>], calling [spawn_function<class_MultiplayerSpawner_property_spawn_function>] on all peers.

Internally, **MultiplayerSpawner** uses [MultiplayerAPI.object_configuration_add()<class_MultiplayerAPI_method_object_configuration_add>] to notify spawns passing the spawned node as the `object` and itself as the `configuration`, and [MultiplayerAPI.object_configuration_remove()<class_MultiplayerAPI_method_object_configuration_remove>] to notify despawns in a similar way.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+-------------------------------------------------------------------------+------------------+
> | :ref:`Callable<class_Callable>` | :ref:`spawn_function<class_MultiplayerSpawner_property_spawn_function>` |                  |
> +---------------------------------+-------------------------------------------------------------------------+------------------+
> | :ref:`int<class_int>`           | :ref:`spawn_limit<class_MultiplayerSpawner_property_spawn_limit>`       | ``0``            |
> +---------------------------------+-------------------------------------------------------------------------+------------------+
> | :ref:`NodePath<class_NodePath>` | :ref:`spawn_path<class_MultiplayerSpawner_property_spawn_path>`         | ``NodePath("")`` |
> +---------------------------------+-------------------------------------------------------------------------+------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`add_spawnable_scene<class_MultiplayerSpawner_method_add_spawnable_scene>`\ (\ path\: :ref:`String<class_String>`\ )    |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`clear_spawnable_scenes<class_MultiplayerSpawner_method_clear_spawnable_scenes>`\ (\ )                                  |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`get_spawnable_scene<class_MultiplayerSpawner_method_get_spawnable_scene>`\ (\ index\: :ref:`int<class_int>`\ ) |const| |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_spawnable_scene_count<class_MultiplayerSpawner_method_get_spawnable_scene_count>`\ (\ ) |const|                    |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Node<class_Node>`     | :ref:`spawn<class_MultiplayerSpawner_method_spawn>`\ (\ data\: :ref:`Variant<class_Variant>` = null\ )                       |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**despawned**\ (\ node\: [Node<class_Node>]\ ) [🔗<class_MultiplayerSpawner_signal_despawned>]

Emitted when a spawnable scene or custom spawn was despawned by the multiplayer authority. Only called on remote peers.


----



**spawned**\ (\ node\: [Node<class_Node>]\ ) [🔗<class_MultiplayerSpawner_signal_spawned>]

Emitted when a spawnable scene or custom spawn was spawned by the multiplayer authority. Only called on remote peers.


----


## Property Descriptions



[Callable<class_Callable>] **spawn_function** [🔗<class_MultiplayerSpawner_property_spawn_function>]


- |void| **set_spawn_function**\ (\ value\: [Callable<class_Callable>]\ )
- [Callable<class_Callable>] **get_spawn_function**\ (\ )

Method called on all peers when a custom [spawn()<class_MultiplayerSpawner_method_spawn>] is requested by the authority. Will receive the `data` parameter, and should return a [Node<class_Node>] that is not in the scene tree.

\ **Note:** The returned node should **not** be added to the scene with [Node.add_child()<class_Node_method_add_child>]. This is done automatically.


----



[int<class_int>] **spawn_limit** = `0` [🔗<class_MultiplayerSpawner_property_spawn_limit>]


- |void| **set_spawn_limit**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_spawn_limit**\ (\ )

Maximum number of nodes allowed to be spawned by this spawner. Includes both spawnable scenes and custom spawns.

When set to `0` (the default), there is no limit.


----



[NodePath<class_NodePath>] **spawn_path** = `NodePath("")` [🔗<class_MultiplayerSpawner_property_spawn_path>]


- |void| **set_spawn_path**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_spawn_path**\ (\ )

Path to the spawn root. Spawnable scenes that are added as direct children are replicated to other peers.


----


## Method Descriptions



|void| **add_spawnable_scene**\ (\ path\: [String<class_String>]\ ) [🔗<class_MultiplayerSpawner_method_add_spawnable_scene>]

Adds a scene path to spawnable scenes, making it automatically replicated from the multiplayer authority to other peers when added as children of the node pointed by [spawn_path<class_MultiplayerSpawner_property_spawn_path>].


----



|void| **clear_spawnable_scenes**\ (\ ) [🔗<class_MultiplayerSpawner_method_clear_spawnable_scenes>]

Clears all spawnable scenes. Does not despawn existing instances on remote peers.


----



[String<class_String>] **get_spawnable_scene**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_MultiplayerSpawner_method_get_spawnable_scene>]

Returns the spawnable scene path by index.


----



[int<class_int>] **get_spawnable_scene_count**\ (\ ) |const| [🔗<class_MultiplayerSpawner_method_get_spawnable_scene_count>]

Returns the count of spawnable scene paths.


----



[Node<class_Node>] **spawn**\ (\ data\: [Variant<class_Variant>] = null\ ) [🔗<class_MultiplayerSpawner_method_spawn>]

Requests a custom spawn, with `data` passed to [spawn_function<class_MultiplayerSpawner_property_spawn_function>] on all peers. Returns the locally spawned node instance already inside the scene tree, and added as a child of the node pointed by [spawn_path<class_MultiplayerSpawner_property_spawn_path>].

\ **Note:** Spawnable scenes are spawned automatically. [spawn()<class_MultiplayerSpawner_method_spawn>] is only needed for custom spawns.

