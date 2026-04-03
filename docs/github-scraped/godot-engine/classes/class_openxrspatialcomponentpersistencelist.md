:github_url: hide



# OpenXRSpatialComponentPersistenceList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Object for storing the query persistence result data.


## Description

Object for storing the query persistence result data when calling [OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>].


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_persistent_state<class_OpenXRSpatialComponentPersistenceList_method_get_persistent_state>`\ (\ index\: :ref:`int<class_int>`\ ) |const| |
> +-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`get_persistent_uuid<class_OpenXRSpatialComponentPersistenceList_method_get_persistent_uuid>`\ (\ index\: :ref:`int<class_int>`\ ) |const|   |
> +-----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **get_persistent_state**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRSpatialComponentPersistenceList_method_get_persistent_state>]

Returns the persistent state (`XrSpatialPersistenceStateEXT`) for the entity at this `index`.


----



[String<class_String>] **get_persistent_uuid**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_OpenXRSpatialComponentPersistenceList_method_get_persistent_uuid>]

Returns the persistent uuid for the entity at this `index`.

