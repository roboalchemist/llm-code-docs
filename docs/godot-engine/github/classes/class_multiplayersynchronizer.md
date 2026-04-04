:github_url: hide

> **META**
	:keywords: network



# MultiplayerSynchronizer

**Inherits:** [Node<class_Node>] **<** [Object<class_Object>]

Synchronizes properties from the multiplayer authority to the remote peers.


## Description

By default, **MultiplayerSynchronizer** synchronizes configured properties to all peers.

Visibility can be handled directly with [set_visibility_for()<class_MultiplayerSynchronizer_method_set_visibility_for>] or as-needed with [add_visibility_filter()<class_MultiplayerSynchronizer_method_add_visibility_filter>] and [update_visibility()<class_MultiplayerSynchronizer_method_update_visibility>].

\ [MultiplayerSpawner<class_MultiplayerSpawner>]\ s will handle nodes according to visibility of synchronizers as long as the node at [root_path<class_MultiplayerSynchronizer_property_root_path>] was spawned by one.

Internally, **MultiplayerSynchronizer** uses [MultiplayerAPI.object_configuration_add()<class_MultiplayerAPI_method_object_configuration_add>] to notify synchronization start passing the [Node<class_Node>] at [root_path<class_MultiplayerSynchronizer_property_root_path>] as the `object` and itself as the `configuration`, and uses [MultiplayerAPI.object_configuration_remove()<class_MultiplayerAPI_method_object_configuration_remove>] to notify synchronization end in a similar way.

\ **Note:** Synchronization is not supported for [Object<class_Object>] type properties, like [Resource<class_Resource>]. Properties that are unique to each peer, like the instance IDs of [Object<class_Object>]\ s (see [Object.get_instance_id()<class_Object_method_get_instance_id>]) or [RID<class_RID>]\ s, will also not work in synchronization.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+--------------------+
> | :ref:`float<class_float>`                                                      | :ref:`delta_interval<class_MultiplayerSynchronizer_property_delta_interval>`                 | ``0.0``            |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+--------------------+
> | :ref:`bool<class_bool>`                                                        | :ref:`public_visibility<class_MultiplayerSynchronizer_property_public_visibility>`           | ``true``           |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+--------------------+
> | :ref:`SceneReplicationConfig<class_SceneReplicationConfig>`                    | :ref:`replication_config<class_MultiplayerSynchronizer_property_replication_config>`         |                    |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+--------------------+
> | :ref:`float<class_float>`                                                      | :ref:`replication_interval<class_MultiplayerSynchronizer_property_replication_interval>`     | ``0.0``            |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+--------------------+
> | :ref:`NodePath<class_NodePath>`                                                | :ref:`root_path<class_MultiplayerSynchronizer_property_root_path>`                           | ``NodePath("..")`` |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+--------------------+
> | :ref:`VisibilityUpdateMode<enum_MultiplayerSynchronizer_VisibilityUpdateMode>` | :ref:`visibility_update_mode<class_MultiplayerSynchronizer_property_visibility_update_mode>` | ``0``              |
> +--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+--------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`add_visibility_filter<class_MultiplayerSynchronizer_method_add_visibility_filter>`\ (\ filter\: :ref:`Callable<class_Callable>`\ )                  |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`get_visibility_for<class_MultiplayerSynchronizer_method_get_visibility_for>`\ (\ peer\: :ref:`int<class_int>`\ ) |const|                            |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`remove_visibility_filter<class_MultiplayerSynchronizer_method_remove_visibility_filter>`\ (\ filter\: :ref:`Callable<class_Callable>`\ )            |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`set_visibility_for<class_MultiplayerSynchronizer_method_set_visibility_for>`\ (\ peer\: :ref:`int<class_int>`, visible\: :ref:`bool<class_bool>`\ ) |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`update_visibility<class_MultiplayerSynchronizer_method_update_visibility>`\ (\ for_peer\: :ref:`int<class_int>` = 0\ )                              |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**delta_synchronized**\ (\ ) [🔗<class_MultiplayerSynchronizer_signal_delta_synchronized>]

Emitted when a new delta synchronization state is received by this synchronizer after the properties have been updated.


----



**synchronized**\ (\ ) [🔗<class_MultiplayerSynchronizer_signal_synchronized>]

Emitted when a new synchronization state is received by this synchronizer after the properties have been updated.


----



**visibility_changed**\ (\ for_peer\: [int<class_int>]\ ) [🔗<class_MultiplayerSynchronizer_signal_visibility_changed>]

Emitted when visibility of `for_peer` is updated. See [update_visibility()<class_MultiplayerSynchronizer_method_update_visibility>].


----


## Enumerations



enum **VisibilityUpdateMode**: [🔗<enum_MultiplayerSynchronizer_VisibilityUpdateMode>]



[VisibilityUpdateMode<enum_MultiplayerSynchronizer_VisibilityUpdateMode>] **VISIBILITY_PROCESS_IDLE** = `0`

Visibility filters are updated during process frames (see [Node.NOTIFICATION_INTERNAL_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>]).



[VisibilityUpdateMode<enum_MultiplayerSynchronizer_VisibilityUpdateMode>] **VISIBILITY_PROCESS_PHYSICS** = `1`

Visibility filters are updated during physics frames (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>]).



[VisibilityUpdateMode<enum_MultiplayerSynchronizer_VisibilityUpdateMode>] **VISIBILITY_PROCESS_NONE** = `2`

Visibility filters are not updated automatically, and must be updated manually by calling [update_visibility()<class_MultiplayerSynchronizer_method_update_visibility>].


----


## Property Descriptions



[float<class_float>] **delta_interval** = `0.0` [🔗<class_MultiplayerSynchronizer_property_delta_interval>]


- |void| **set_delta_interval**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_delta_interval**\ (\ )

Time interval between delta synchronizations. Used when the replication is set to [SceneReplicationConfig.REPLICATION_MODE_ON_CHANGE<class_SceneReplicationConfig_constant_REPLICATION_MODE_ON_CHANGE>]. If set to `0.0` (the default), delta synchronizations happen every network process frame.


----



[bool<class_bool>] **public_visibility** = `true` [🔗<class_MultiplayerSynchronizer_property_public_visibility>]


- |void| **set_visibility_public**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_visibility_public**\ (\ )

Whether synchronization should be visible to all peers by default. See [set_visibility_for()<class_MultiplayerSynchronizer_method_set_visibility_for>] and [add_visibility_filter()<class_MultiplayerSynchronizer_method_add_visibility_filter>] for ways of configuring fine-grained visibility options.


----



[SceneReplicationConfig<class_SceneReplicationConfig>] **replication_config** [🔗<class_MultiplayerSynchronizer_property_replication_config>]


- |void| **set_replication_config**\ (\ value\: [SceneReplicationConfig<class_SceneReplicationConfig>]\ )
- [SceneReplicationConfig<class_SceneReplicationConfig>] **get_replication_config**\ (\ )

Resource containing which properties to synchronize.


----



[float<class_float>] **replication_interval** = `0.0` [🔗<class_MultiplayerSynchronizer_property_replication_interval>]


- |void| **set_replication_interval**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_replication_interval**\ (\ )

Time interval between synchronizations. Used when the replication is set to [SceneReplicationConfig.REPLICATION_MODE_ALWAYS<class_SceneReplicationConfig_constant_REPLICATION_MODE_ALWAYS>]. If set to `0.0` (the default), synchronizations happen every network process frame.


----



[NodePath<class_NodePath>] **root_path** = `NodePath("..")` [🔗<class_MultiplayerSynchronizer_property_root_path>]


- |void| **set_root_path**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_root_path**\ (\ )

Node path that replicated properties are relative to.

If [root_path<class_MultiplayerSynchronizer_property_root_path>] was spawned by a [MultiplayerSpawner<class_MultiplayerSpawner>], the node will be also be spawned and despawned based on this synchronizer visibility options.


----



[VisibilityUpdateMode<enum_MultiplayerSynchronizer_VisibilityUpdateMode>] **visibility_update_mode** = `0` [🔗<class_MultiplayerSynchronizer_property_visibility_update_mode>]


- |void| **set_visibility_update_mode**\ (\ value\: [VisibilityUpdateMode<enum_MultiplayerSynchronizer_VisibilityUpdateMode>]\ )
- [VisibilityUpdateMode<enum_MultiplayerSynchronizer_VisibilityUpdateMode>] **get_visibility_update_mode**\ (\ )

Specifies when visibility filters are updated.


----


## Method Descriptions



|void| **add_visibility_filter**\ (\ filter\: [Callable<class_Callable>]\ ) [🔗<class_MultiplayerSynchronizer_method_add_visibility_filter>]

Adds a peer visibility filter for this synchronizer.

\ `filter` should take a peer ID [int<class_int>] and return a [bool<class_bool>].


----



[bool<class_bool>] **get_visibility_for**\ (\ peer\: [int<class_int>]\ ) |const| [🔗<class_MultiplayerSynchronizer_method_get_visibility_for>]

Queries the current visibility for peer `peer`.


----



|void| **remove_visibility_filter**\ (\ filter\: [Callable<class_Callable>]\ ) [🔗<class_MultiplayerSynchronizer_method_remove_visibility_filter>]

Removes a peer visibility filter from this synchronizer.


----



|void| **set_visibility_for**\ (\ peer\: [int<class_int>], visible\: [bool<class_bool>]\ ) [🔗<class_MultiplayerSynchronizer_method_set_visibility_for>]

Sets the visibility of `peer` to `visible`. If `peer` is `0`, the value of [public_visibility<class_MultiplayerSynchronizer_property_public_visibility>] will be updated instead.


----



|void| **update_visibility**\ (\ for_peer\: [int<class_int>] = 0\ ) [🔗<class_MultiplayerSynchronizer_method_update_visibility>]

Updates the visibility of `for_peer` according to visibility filters. If `for_peer` is `0` (the default), all peers' visibilties are updated.

