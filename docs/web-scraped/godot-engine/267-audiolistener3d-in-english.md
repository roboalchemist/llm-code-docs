# AudioListener3D in English

# AudioListener3D
Inherits:Node3D<Node<Object
Overrides the location sounds are heard from.

## Description
Once added to the scene tree and enabled usingmake_current(), this node will override the location sounds are heard from. This can be used to listen from a location different from theCamera3D.

## Properties

| DopplerTracking | doppler_tracking | 0 |

DopplerTracking
doppler_tracking

## Methods

| void | clear_current() |
|---|---|
| Transform3D | get_listener_transform()const |
| bool | is_current()const |
| void | make_current() |

void
clear_current()
Transform3D
get_listener_transform()const
bool
is_current()const
void
make_current()

## Enumerations
enumDopplerTracking:🔗
DopplerTrackingDOPPLER_TRACKING_DISABLED=0
DisablesDoppler effectsimulation (default).
DopplerTrackingDOPPLER_TRACKING_IDLE_STEP=1
SimulateDoppler effectby tracking positions of objects that are changed in_process. Changes in the relative velocity of this listener compared to those objects affect how audio is perceived (changing the audio'sAudioStreamPlayer3D.pitch_scale).
DopplerTrackingDOPPLER_TRACKING_PHYSICS_STEP=2
SimulateDoppler effectby tracking positions of objects that are changed in_physics_process. Changes in the relative velocity of this listener compared to those objects affect how audio is perceived (changing the audio'sAudioStreamPlayer3D.pitch_scale).

## Property Descriptions
DopplerTrackingdoppler_tracking=0🔗
- voidset_doppler_tracking(value:DopplerTracking)
voidset_doppler_tracking(value:DopplerTracking)
- DopplerTrackingget_doppler_tracking()
DopplerTrackingget_doppler_tracking()
If notDOPPLER_TRACKING_DISABLED, this listener will simulate theDoppler effectfor objects changed in particular_processmethods.
Note:The Doppler effect will only be heard onAudioStreamPlayer3Ds ifAudioStreamPlayer3D.doppler_trackingis not set toAudioStreamPlayer3D.DOPPLER_TRACKING_DISABLED.

## Method Descriptions
voidclear_current()🔗
Disables the listener to use the current camera's listener instead.
Transform3Dget_listener_transform()const🔗
Returns the listener's global orthonormalizedTransform3D.
boolis_current()const🔗
Returnstrueif the listener was made current usingmake_current(),falseotherwise.
Note:There may be more than one AudioListener3D marked as "current" in the scene tree, but only the one that was made current last will be used.
voidmake_current()🔗
Enables the listener. This will override the current camera's listener.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.