# OpenXRSpatialEntityTracker

# OpenXRSpatialEntityTracker

Experimental:This class may be changed or removed in future versions.
Inherits:XRPositionalTracker<XRTracker<RefCounted<Object
Inherited By:OpenXRAnchorTracker,OpenXRMarkerTracker,OpenXRPlaneTracker
Base class for Positional trackers managed by OpenXR's spatial entity extensions.

## Description

These are trackers created and managed by OpenXR's spatial entity extensions that give access to specific data related to OpenXR's spatial entities. They will always be of typeTRACKER_ANCHOR.

## Properties

| RID | entity | RID() |
|---|---|---|
| EntityTrackingState | spatial_tracking_state | 2 |
| TrackerType | type | 8(overridesXRTracker) |

entity
RID()
EntityTrackingState
spatial_tracking_state
TrackerType
type
8(overridesXRTracker)

## Signals

spatial_tracking_state_changed(spatial_tracking_state:int)🔗
There is currently no description for this signal. Please help us bycontributing one!

## Enumerations

enumEntityTrackingState:🔗
EntityTrackingStateENTITY_TRACKING_STATE_STOPPED=1
This anchor has stopped tracking.
EntityTrackingStateENTITY_TRACKING_STATE_PAUSED=2
Tracking is currently paused.
EntityTrackingStateENTITY_TRACKING_STATE_TRACKING=3
This anchor is currently being tracked.

## Property Descriptions

RIDentity=RID()🔗

- voidset_entity(value:RID)
voidset_entity(value:RID)
- RIDget_entity()
RIDget_entity()
The spatial entity associated with this tracker.
EntityTrackingStatespatial_tracking_state=2🔗
- voidset_spatial_tracking_state(value:EntityTrackingState)
voidset_spatial_tracking_state(value:EntityTrackingState)
- EntityTrackingStateget_spatial_tracking_state()
EntityTrackingStateget_spatial_tracking_state()
The spatial tracking state for this tracker.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
