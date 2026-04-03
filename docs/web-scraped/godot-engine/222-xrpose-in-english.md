# XRPose in English

# XRPose
Inherits:RefCounted<Object
This object contains all data related to a pose on a tracked object.

## Description
XR runtimes often identify multiple locations on devices such as controllers that are spatially tracked.
Orientation, location, linear velocity and angular velocity are all provided for each pose by the XR runtime. This object contains this state of a pose.

## Tutorials
- XR documentation index
XR documentation index

## Properties

| Vector3 | angular_velocity | Vector3(0,0,0) |
|---|---|---|
| bool | has_tracking_data | false |
| Vector3 | linear_velocity | Vector3(0,0,0) |
| StringName | name | &"" |
| TrackingConfidence | tracking_confidence | 0 |
| Transform3D | transform | Transform3D(1,0,0,0,1,0,0,0,1,0,0,0) |

Vector3
angular_velocity
Vector3(0,0,0)
bool
has_tracking_data
false
Vector3
linear_velocity
Vector3(0,0,0)
StringName
name
TrackingConfidence
tracking_confidence
Transform3D
transform
Transform3D(1,0,0,0,1,0,0,0,1,0,0,0)

## Methods

| Transform3D | get_adjusted_transform()const |

Transform3D
get_adjusted_transform()const

## Enumerations
enumTrackingConfidence:🔗
TrackingConfidenceXR_TRACKING_CONFIDENCE_NONE=0
No tracking information is available for this pose.
TrackingConfidenceXR_TRACKING_CONFIDENCE_LOW=1
Tracking information may be inaccurate or estimated. For example, with inside out tracking this would indicate a controller may be (partially) obscured.
TrackingConfidenceXR_TRACKING_CONFIDENCE_HIGH=2
Tracking information is considered accurate and up to date.

## Property Descriptions
Vector3angular_velocity=Vector3(0,0,0)🔗
- voidset_angular_velocity(value:Vector3)
voidset_angular_velocity(value:Vector3)
- Vector3get_angular_velocity()
Vector3get_angular_velocity()
The angular velocity for this pose.
boolhas_tracking_data=false🔗
- voidset_has_tracking_data(value:bool)
voidset_has_tracking_data(value:bool)
- boolget_has_tracking_data()
boolget_has_tracking_data()
Iftrueour tracking data is up to date. Iffalsewe're no longer receiving new tracking data and our state is whatever that last valid state was.
Vector3linear_velocity=Vector3(0,0,0)🔗
- voidset_linear_velocity(value:Vector3)
voidset_linear_velocity(value:Vector3)
- Vector3get_linear_velocity()
Vector3get_linear_velocity()
The linear velocity of this pose.
StringNamename=&""🔗
- voidset_name(value:StringName)
voidset_name(value:StringName)
- StringNameget_name()
StringNameget_name()
The name of this pose. Usually, this name is derived from an action map set up by the user. Godot also suggests some pose names thatXRInterfaceobjects are expected to implement:
- rootis the root location, often used for tracked objects that do not have further nodes.
rootis the root location, often used for tracked objects that do not have further nodes.
- aimis the tip of a controller with its orientation pointing outwards, often used for raycasts.
aimis the tip of a controller with its orientation pointing outwards, often used for raycasts.
- gripis the location where the user grips the controller.
gripis the location where the user grips the controller.
- skeletonis the root location for a hand mesh, when using hand tracking and an animated skeleton is supplied by the XR runtime.
skeletonis the root location for a hand mesh, when using hand tracking and an animated skeleton is supplied by the XR runtime.
TrackingConfidencetracking_confidence=0🔗
- voidset_tracking_confidence(value:TrackingConfidence)
voidset_tracking_confidence(value:TrackingConfidence)
- TrackingConfidenceget_tracking_confidence()
TrackingConfidenceget_tracking_confidence()
The tracking confidence for this pose, provides insight on how accurate the spatial positioning of this record is.
Transform3Dtransform=Transform3D(1,0,0,0,1,0,0,0,1,0,0,0)🔗
- voidset_transform(value:Transform3D)
voidset_transform(value:Transform3D)
- Transform3Dget_transform()
Transform3Dget_transform()
The transform containing the original and transform as reported by the XR runtime.

## Method Descriptions
Transform3Dget_adjusted_transform()const🔗
Returns thetransformwith world scale and our reference frame applied. This is the transform used to positionXRNode3Dobjects.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.