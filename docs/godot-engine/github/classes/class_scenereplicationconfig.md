:github_url: hide



# SceneReplicationConfig

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Configuration for properties to synchronize with a [MultiplayerSynchronizer<class_MultiplayerSynchronizer>].


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`add_property<class_SceneReplicationConfig_method_add_property>`\ (\ path\: :ref:`NodePath<class_NodePath>`, index\: :ref:`int<class_int>` = -1\ )                                                                           |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`NodePath<class_NodePath>`\]        | :ref:`get_properties<class_SceneReplicationConfig_method_get_properties>`\ (\ ) |const|                                                                                                                                           |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                             | :ref:`has_property<class_SceneReplicationConfig_method_has_property>`\ (\ path\: :ref:`NodePath<class_NodePath>`\ ) |const|                                                                                                       |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                               | :ref:`property_get_index<class_SceneReplicationConfig_method_property_get_index>`\ (\ path\: :ref:`NodePath<class_NodePath>`\ ) |const|                                                                                           |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>` | :ref:`property_get_replication_mode<class_SceneReplicationConfig_method_property_get_replication_mode>`\ (\ path\: :ref:`NodePath<class_NodePath>`\ )                                                                             |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                             | :ref:`property_get_spawn<class_SceneReplicationConfig_method_property_get_spawn>`\ (\ path\: :ref:`NodePath<class_NodePath>`\ )                                                                                                   |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                             | :ref:`property_get_sync<class_SceneReplicationConfig_method_property_get_sync>`\ (\ path\: :ref:`NodePath<class_NodePath>`\ )                                                                                                     |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                             | :ref:`property_get_watch<class_SceneReplicationConfig_method_property_get_watch>`\ (\ path\: :ref:`NodePath<class_NodePath>`\ )                                                                                                   |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`property_set_replication_mode<class_SceneReplicationConfig_method_property_set_replication_mode>`\ (\ path\: :ref:`NodePath<class_NodePath>`, mode\: :ref:`ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>`\ ) |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`property_set_spawn<class_SceneReplicationConfig_method_property_set_spawn>`\ (\ path\: :ref:`NodePath<class_NodePath>`, enabled\: :ref:`bool<class_bool>`\ )                                                                |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`property_set_sync<class_SceneReplicationConfig_method_property_set_sync>`\ (\ path\: :ref:`NodePath<class_NodePath>`, enabled\: :ref:`bool<class_bool>`\ )                                                                  |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`property_set_watch<class_SceneReplicationConfig_method_property_set_watch>`\ (\ path\: :ref:`NodePath<class_NodePath>`, enabled\: :ref:`bool<class_bool>`\ )                                                                |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                              | :ref:`remove_property<class_SceneReplicationConfig_method_remove_property>`\ (\ path\: :ref:`NodePath<class_NodePath>`\ )                                                                                                         |
> +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ReplicationMode**: [🔗<enum_SceneReplicationConfig_ReplicationMode>]



[ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>] **REPLICATION_MODE_NEVER** = `0`

Do not keep the given property synchronized.



[ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>] **REPLICATION_MODE_ALWAYS** = `1`

Replicate the given property on process by constantly sending updates using unreliable transfer mode.



[ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>] **REPLICATION_MODE_ON_CHANGE** = `2`

Replicate the given property on process by sending updates using reliable transfer mode when its value changes.


----


## Method Descriptions



|void| **add_property**\ (\ path\: [NodePath<class_NodePath>], index\: [int<class_int>] = -1\ ) [🔗<class_SceneReplicationConfig_method_add_property>]

Adds the property identified by the given `path` to the list of the properties being synchronized, optionally passing an `index`.

\ **Note:** For details on restrictions and limitations on property synchronization, see [MultiplayerSynchronizer<class_MultiplayerSynchronizer>].


----



[Array<class_Array>]\[[NodePath<class_NodePath>]\] **get_properties**\ (\ ) |const| [🔗<class_SceneReplicationConfig_method_get_properties>]

Returns a list of synchronized property [NodePath<class_NodePath>]\ s.


----



[bool<class_bool>] **has_property**\ (\ path\: [NodePath<class_NodePath>]\ ) |const| [🔗<class_SceneReplicationConfig_method_has_property>]

Returns `true` if the given `path` is configured for synchronization.


----



[int<class_int>] **property_get_index**\ (\ path\: [NodePath<class_NodePath>]\ ) |const| [🔗<class_SceneReplicationConfig_method_property_get_index>]

Finds the index of the given `path`.


----



[ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>] **property_get_replication_mode**\ (\ path\: [NodePath<class_NodePath>]\ ) [🔗<class_SceneReplicationConfig_method_property_get_replication_mode>]

Returns the replication mode for the property identified by the given `path`.


----



[bool<class_bool>] **property_get_spawn**\ (\ path\: [NodePath<class_NodePath>]\ ) [🔗<class_SceneReplicationConfig_method_property_get_spawn>]

Returns `true` if the property identified by the given `path` is configured to be synchronized on spawn.


----



[bool<class_bool>] **property_get_sync**\ (\ path\: [NodePath<class_NodePath>]\ ) [🔗<class_SceneReplicationConfig_method_property_get_sync>]

**Deprecated:** Use [property_get_replication_mode()<class_SceneReplicationConfig_method_property_get_replication_mode>] instead.

Returns `true` if the property identified by the given `path` is configured to be synchronized on process.


----



[bool<class_bool>] **property_get_watch**\ (\ path\: [NodePath<class_NodePath>]\ ) [🔗<class_SceneReplicationConfig_method_property_get_watch>]

**Deprecated:** Use [property_get_replication_mode()<class_SceneReplicationConfig_method_property_get_replication_mode>] instead.

Returns `true` if the property identified by the given `path` is configured to be reliably synchronized when changes are detected on process.


----



|void| **property_set_replication_mode**\ (\ path\: [NodePath<class_NodePath>], mode\: [ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>]\ ) [🔗<class_SceneReplicationConfig_method_property_set_replication_mode>]

Sets the synchronization mode for the property identified by the given `path`.


----



|void| **property_set_spawn**\ (\ path\: [NodePath<class_NodePath>], enabled\: [bool<class_bool>]\ ) [🔗<class_SceneReplicationConfig_method_property_set_spawn>]

Sets whether the property identified by the given `path` is configured to be synchronized on spawn.


----



|void| **property_set_sync**\ (\ path\: [NodePath<class_NodePath>], enabled\: [bool<class_bool>]\ ) [🔗<class_SceneReplicationConfig_method_property_set_sync>]

**Deprecated:** Use [property_set_replication_mode()<class_SceneReplicationConfig_method_property_set_replication_mode>] with [REPLICATION_MODE_ALWAYS<class_SceneReplicationConfig_constant_REPLICATION_MODE_ALWAYS>] instead.

Sets whether the property identified by the given `path` is configured to be synchronized on process.


----



|void| **property_set_watch**\ (\ path\: [NodePath<class_NodePath>], enabled\: [bool<class_bool>]\ ) [🔗<class_SceneReplicationConfig_method_property_set_watch>]

**Deprecated:** Use [property_set_replication_mode()<class_SceneReplicationConfig_method_property_set_replication_mode>] with [REPLICATION_MODE_ON_CHANGE<class_SceneReplicationConfig_constant_REPLICATION_MODE_ON_CHANGE>] instead.

Sets whether the property identified by the given `path` is configured to be reliably synchronized when changes are detected on process.


----



|void| **remove_property**\ (\ path\: [NodePath<class_NodePath>]\ ) [🔗<class_SceneReplicationConfig_method_remove_property>]

Removes the property identified by the given `path` from the configuration.

