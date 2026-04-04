:github_url: hide



# OpenXRSpatialEntityTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [XRPositionalTracker<class_XRPositionalTracker>] **<** [XRTracker<class_XRTracker>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [OpenXRAnchorTracker<class_OpenXRAnchorTracker>], [OpenXRMarkerTracker<class_OpenXRMarkerTracker>], [OpenXRPlaneTracker<class_OpenXRPlaneTracker>]

Base class for Positional trackers managed by OpenXR's spatial entity extensions.


## Description

These are trackers created and managed by OpenXR's spatial entity extensions that give access to specific data related to OpenXR's spatial entities. They will always be of type `TRACKER_ANCHOR`.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                           | :ref:`entity<class_OpenXRSpatialEntityTracker_property_entity>`                                 | ``RID()``                                                         |
> +---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
> | :ref:`EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>` | :ref:`spatial_tracking_state<class_OpenXRSpatialEntityTracker_property_spatial_tracking_state>` | ``2``                                                             |
> +---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
> | :ref:`TrackerType<enum_XRServer_TrackerType>`                                   | type                                                                                            | ``8`` (overrides :ref:`XRTracker<class_XRTracker_property_type>`) |
> +---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
>

----


## Signals



**spatial_tracking_state_changed**\ (\ spatial_tracking_state\: [int<class_int>]\ ) [🔗<class_OpenXRSpatialEntityTracker_signal_spatial_tracking_state_changed>]

> **CONTAINER**
>
	There is currently no description for this signal. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----


## Enumerations



enum **EntityTrackingState**: [🔗<enum_OpenXRSpatialEntityTracker_EntityTrackingState>]



[EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>] **ENTITY_TRACKING_STATE_STOPPED** = `1`

This anchor has stopped tracking.



[EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>] **ENTITY_TRACKING_STATE_PAUSED** = `2`

Tracking is currently paused.



[EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>] **ENTITY_TRACKING_STATE_TRACKING** = `3`

This anchor is currently being tracked.


----


## Property Descriptions



[RID<class_RID>] **entity** = `RID()` [🔗<class_OpenXRSpatialEntityTracker_property_entity>]


- |void| **set_entity**\ (\ value\: [RID<class_RID>]\ )
- [RID<class_RID>] **get_entity**\ (\ )

The spatial entity associated with this tracker.


----



[EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>] **spatial_tracking_state** = `2` [🔗<class_OpenXRSpatialEntityTracker_property_spatial_tracking_state>]


- |void| **set_spatial_tracking_state**\ (\ value\: [EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>]\ )
- [EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>] **get_spatial_tracking_state**\ (\ )

The spatial tracking state for this tracker.

