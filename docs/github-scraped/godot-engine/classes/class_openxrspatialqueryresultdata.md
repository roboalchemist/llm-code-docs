:github_url: hide



# OpenXRSpatialQueryResultData

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Object for storing the main query result data.


## Description

Object for storing the main query result data when calling [OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>]. This must always be the first component requested.


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                           | :ref:`get_capacity<class_OpenXRSpatialQueryResultData_method_get_capacity>`\ (\ ) |const|                                        |
> +---------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                           | :ref:`get_entity_id<class_OpenXRSpatialQueryResultData_method_get_entity_id>`\ (\ index\: :ref:`int<class_int>`\ ) |const|       |
> +---------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>` | :ref:`get_entity_state<class_OpenXRSpatialQueryResultData_method_get_entity_state>`\ (\ index\: :ref:`int<class_int>`\ ) |const| |
> +---------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **get_capacity**\ (\ ) |const| [🔗<class_OpenXRSpatialQueryResultData_method_get_capacity>]

Returns the number of entities that were retrieved.


----



[int<class_int>] **get_entity_id**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRSpatialQueryResultData_method_get_entity_id>]

Returns the entity id (`XrSpatialEntityIdEXT`) for the entity at this `index`.


----



[EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>] **get_entity_state**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRSpatialQueryResultData_method_get_entity_state>]

Returns the entity state for the entity at this `index`.

