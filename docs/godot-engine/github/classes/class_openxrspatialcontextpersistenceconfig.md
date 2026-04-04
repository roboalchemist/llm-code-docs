:github_url: hide



# OpenXRSpatialContextPersistenceConfig

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRStructureBase<class_OpenXRStructureBase>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Configuration header for spatial persistence.


## Description

Configuration header for spatial persistence. Pass this to [OpenXRSpatialEntityExtension.create_spatial_context()<class_OpenXRSpatialEntityExtension_method_create_spatial_context>] as the next parameter to create a spatial context with spatial persistence capabilities.


## Methods

> **TABLE**
> :widths: auto
>
> +--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`add_persistence_context<class_OpenXRSpatialContextPersistenceConfig_method_add_persistence_context>`\ (\ persistence_context\: :ref:`RID<class_RID>`\ )       |
> +--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`remove_persistence_context<class_OpenXRSpatialContextPersistenceConfig_method_remove_persistence_context>`\ (\ persistence_context\: :ref:`RID<class_RID>`\ ) |
> +--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **add_persistence_context**\ (\ persistence_context\: [RID<class_RID>]\ ) [🔗<class_OpenXRSpatialContextPersistenceConfig_method_add_persistence_context>]

Adds a persistence context to this configuration. You must add at least one persistence context to create a valid configuration. You can create a persistence context by calling [OpenXRSpatialAnchorCapability.create_persistence_context()<class_OpenXRSpatialAnchorCapability_method_create_persistence_context>].


----



|void| **remove_persistence_context**\ (\ persistence_context\: [RID<class_RID>]\ ) [🔗<class_OpenXRSpatialContextPersistenceConfig_method_remove_persistence_context>]

Removes a persistence context.

