:github_url: hide



# XRHandTracker

**Inherits:** [XRPositionalTracker<class_XRPositionalTracker>] **<** [XRTracker<class_XRTracker>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A tracked hand in XR.


## Description

A hand tracking system will create an instance of this object and add it to the [XRServer<class_XRServer>]. This tracking system will then obtain skeleton data, convert it to the Godot Humanoid hand skeleton and store this data on the **XRHandTracker** object.

Use [XRHandModifier3D<class_XRHandModifier3D>] to animate a hand mesh using hand tracking data.


## Tutorials

- [../tutorials/xr/index](XR documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
> | :ref:`TrackerHand<enum_XRPositionalTracker_TrackerHand>`         | hand                                                                           | ``1`` (overrides :ref:`XRPositionalTracker<class_XRPositionalTracker_property_hand>`) |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
> | :ref:`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>` | :ref:`hand_tracking_source<class_XRHandTracker_property_hand_tracking_source>` | ``0``                                                                                 |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`has_tracking_data<class_XRHandTracker_property_has_tracking_data>`       | ``false``                                                                             |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
> | :ref:`TrackerType<enum_XRServer_TrackerType>`                    | type                                                                           | ``16`` (overrides :ref:`XRTracker<class_XRTracker_property_type>`)                    |
> +------------------------------------------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                          | :ref:`get_hand_joint_angular_velocity<class_XRHandTracker_method_get_hand_joint_angular_velocity>`\ (\ joint\: :ref:`HandJoint<enum_XRHandTracker_HandJoint>`\ ) |const|                                                   |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |bitfield|\[:ref:`HandJointFlags<enum_XRHandTracker_HandJointFlags>`\] | :ref:`get_hand_joint_flags<class_XRHandTracker_method_get_hand_joint_flags>`\ (\ joint\: :ref:`HandJoint<enum_XRHandTracker_HandJoint>`\ ) |const|                                                                         |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                          | :ref:`get_hand_joint_linear_velocity<class_XRHandTracker_method_get_hand_joint_linear_velocity>`\ (\ joint\: :ref:`HandJoint<enum_XRHandTracker_HandJoint>`\ ) |const|                                                     |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                              | :ref:`get_hand_joint_radius<class_XRHandTracker_method_get_hand_joint_radius>`\ (\ joint\: :ref:`HandJoint<enum_XRHandTracker_HandJoint>`\ ) |const|                                                                       |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                                  | :ref:`get_hand_joint_transform<class_XRHandTracker_method_get_hand_joint_transform>`\ (\ joint\: :ref:`HandJoint<enum_XRHandTracker_HandJoint>`\ ) |const|                                                                 |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_hand_joint_angular_velocity<class_XRHandTracker_method_set_hand_joint_angular_velocity>`\ (\ joint\: :ref:`HandJoint<enum_XRHandTracker_HandJoint>`, angular_velocity\: :ref:`Vector3<class_Vector3>`\ )         |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_hand_joint_flags<class_XRHandTracker_method_set_hand_joint_flags>`\ (\ joint\: :ref:`HandJoint<enum_XRHandTracker_HandJoint>`, flags\: |bitfield|\[:ref:`HandJointFlags<enum_XRHandTracker_HandJointFlags>`\]\ ) |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_hand_joint_linear_velocity<class_XRHandTracker_method_set_hand_joint_linear_velocity>`\ (\ joint\: :ref:`HandJoint<enum_XRHandTracker_HandJoint>`, linear_velocity\: :ref:`Vector3<class_Vector3>`\ )            |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_hand_joint_radius<class_XRHandTracker_method_set_hand_joint_radius>`\ (\ joint\: :ref:`HandJoint<enum_XRHandTracker_HandJoint>`, radius\: :ref:`float<class_float>`\ )                                           |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                 | :ref:`set_hand_joint_transform<class_XRHandTracker_method_set_hand_joint_transform>`\ (\ joint\: :ref:`HandJoint<enum_XRHandTracker_HandJoint>`, transform\: :ref:`Transform3D<class_Transform3D>`\ )                      |
> +------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **HandTrackingSource**: [🔗<enum_XRHandTracker_HandTrackingSource>]



[HandTrackingSource<enum_XRHandTracker_HandTrackingSource>] **HAND_TRACKING_SOURCE_UNKNOWN** = `0`

The source of hand tracking data is unknown.



[HandTrackingSource<enum_XRHandTracker_HandTrackingSource>] **HAND_TRACKING_SOURCE_UNOBSTRUCTED** = `1`

The source of hand tracking data is unobstructed, meaning that an accurate method of hand tracking is used. These include optical hand tracking, data gloves, etc.



[HandTrackingSource<enum_XRHandTracker_HandTrackingSource>] **HAND_TRACKING_SOURCE_CONTROLLER** = `2`

The source of hand tracking data is a controller, meaning that joint positions are inferred from controller inputs.



[HandTrackingSource<enum_XRHandTracker_HandTrackingSource>] **HAND_TRACKING_SOURCE_NOT_TRACKED** = `3`

No hand tracking data is tracked, this either means the hand is obscured, the controller is turned off, or tracking is not supported for the current input type.



[HandTrackingSource<enum_XRHandTracker_HandTrackingSource>] **HAND_TRACKING_SOURCE_MAX** = `4`

Represents the size of the [HandTrackingSource<enum_XRHandTracker_HandTrackingSource>] enum.


----



enum **HandJoint**: [🔗<enum_XRHandTracker_HandJoint>]



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_PALM** = `0`

Palm joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_WRIST** = `1`

Wrist joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_THUMB_METACARPAL** = `2`

Thumb metacarpal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_THUMB_PHALANX_PROXIMAL** = `3`

Thumb phalanx proximal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_THUMB_PHALANX_DISTAL** = `4`

Thumb phalanx distal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_THUMB_TIP** = `5`

Thumb tip joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_INDEX_FINGER_METACARPAL** = `6`

Index finger metacarpal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_INDEX_FINGER_PHALANX_PROXIMAL** = `7`

Index finger phalanx proximal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_INDEX_FINGER_PHALANX_INTERMEDIATE** = `8`

Index finger phalanx intermediate joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_INDEX_FINGER_PHALANX_DISTAL** = `9`

Index finger phalanx distal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_INDEX_FINGER_TIP** = `10`

Index finger tip joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_MIDDLE_FINGER_METACARPAL** = `11`

Middle finger metacarpal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_MIDDLE_FINGER_PHALANX_PROXIMAL** = `12`

Middle finger phalanx proximal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_MIDDLE_FINGER_PHALANX_INTERMEDIATE** = `13`

Middle finger phalanx intermediate joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_MIDDLE_FINGER_PHALANX_DISTAL** = `14`

Middle finger phalanx distal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_MIDDLE_FINGER_TIP** = `15`

Middle finger tip joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_RING_FINGER_METACARPAL** = `16`

Ring finger metacarpal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_RING_FINGER_PHALANX_PROXIMAL** = `17`

Ring finger phalanx proximal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_RING_FINGER_PHALANX_INTERMEDIATE** = `18`

Ring finger phalanx intermediate joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_RING_FINGER_PHALANX_DISTAL** = `19`

Ring finger phalanx distal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_RING_FINGER_TIP** = `20`

Ring finger tip joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_PINKY_FINGER_METACARPAL** = `21`

Pinky finger metacarpal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_PINKY_FINGER_PHALANX_PROXIMAL** = `22`

Pinky finger phalanx proximal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_PINKY_FINGER_PHALANX_INTERMEDIATE** = `23`

Pinky finger phalanx intermediate joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_PINKY_FINGER_PHALANX_DISTAL** = `24`

Pinky finger phalanx distal joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_PINKY_FINGER_TIP** = `25`

Pinky finger tip joint.



[HandJoint<enum_XRHandTracker_HandJoint>] **HAND_JOINT_MAX** = `26`

Represents the size of the [HandJoint<enum_XRHandTracker_HandJoint>] enum.


----



flags **HandJointFlags**: [🔗<enum_XRHandTracker_HandJointFlags>]



[HandJointFlags<enum_XRHandTracker_HandJointFlags>] **HAND_JOINT_FLAG_ORIENTATION_VALID** = `1`

The hand joint's orientation data is valid.



[HandJointFlags<enum_XRHandTracker_HandJointFlags>] **HAND_JOINT_FLAG_ORIENTATION_TRACKED** = `2`

The hand joint's orientation is actively tracked. May not be set if tracking has been temporarily lost.



[HandJointFlags<enum_XRHandTracker_HandJointFlags>] **HAND_JOINT_FLAG_POSITION_VALID** = `4`

The hand joint's position data is valid.



[HandJointFlags<enum_XRHandTracker_HandJointFlags>] **HAND_JOINT_FLAG_POSITION_TRACKED** = `8`

The hand joint's position is actively tracked. May not be set if tracking has been temporarily lost.



[HandJointFlags<enum_XRHandTracker_HandJointFlags>] **HAND_JOINT_FLAG_LINEAR_VELOCITY_VALID** = `16`

The hand joint's linear velocity data is valid.



[HandJointFlags<enum_XRHandTracker_HandJointFlags>] **HAND_JOINT_FLAG_ANGULAR_VELOCITY_VALID** = `32`

The hand joint's angular velocity data is valid.


----


## Property Descriptions



[HandTrackingSource<enum_XRHandTracker_HandTrackingSource>] **hand_tracking_source** = `0` [🔗<class_XRHandTracker_property_hand_tracking_source>]


- |void| **set_hand_tracking_source**\ (\ value\: [HandTrackingSource<enum_XRHandTracker_HandTrackingSource>]\ )
- [HandTrackingSource<enum_XRHandTracker_HandTrackingSource>] **get_hand_tracking_source**\ (\ )

The source of the hand tracking data.


----



[bool<class_bool>] **has_tracking_data** = `false` [🔗<class_XRHandTracker_property_has_tracking_data>]


- |void| **set_has_tracking_data**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_has_tracking_data**\ (\ )

If `true`, the hand tracking data is valid.


----


## Method Descriptions



[Vector3<class_Vector3>] **get_hand_joint_angular_velocity**\ (\ joint\: [HandJoint<enum_XRHandTracker_HandJoint>]\ ) |const| [🔗<class_XRHandTracker_method_get_hand_joint_angular_velocity>]

Returns the angular velocity for the given hand joint.


----



|bitfield|\[[HandJointFlags<enum_XRHandTracker_HandJointFlags>]\] **get_hand_joint_flags**\ (\ joint\: [HandJoint<enum_XRHandTracker_HandJoint>]\ ) |const| [🔗<class_XRHandTracker_method_get_hand_joint_flags>]

Returns flags about the validity of the tracking data for the given hand joint.


----



[Vector3<class_Vector3>] **get_hand_joint_linear_velocity**\ (\ joint\: [HandJoint<enum_XRHandTracker_HandJoint>]\ ) |const| [🔗<class_XRHandTracker_method_get_hand_joint_linear_velocity>]

Returns the linear velocity for the given hand joint.


----



[float<class_float>] **get_hand_joint_radius**\ (\ joint\: [HandJoint<enum_XRHandTracker_HandJoint>]\ ) |const| [🔗<class_XRHandTracker_method_get_hand_joint_radius>]

Returns the radius of the given hand joint.


----



[Transform3D<class_Transform3D>] **get_hand_joint_transform**\ (\ joint\: [HandJoint<enum_XRHandTracker_HandJoint>]\ ) |const| [🔗<class_XRHandTracker_method_get_hand_joint_transform>]

Returns the transform for the given hand joint.


----



|void| **set_hand_joint_angular_velocity**\ (\ joint\: [HandJoint<enum_XRHandTracker_HandJoint>], angular_velocity\: [Vector3<class_Vector3>]\ ) [🔗<class_XRHandTracker_method_set_hand_joint_angular_velocity>]

Sets the angular velocity for the given hand joint.


----



|void| **set_hand_joint_flags**\ (\ joint\: [HandJoint<enum_XRHandTracker_HandJoint>], flags\: |bitfield|\[[HandJointFlags<enum_XRHandTracker_HandJointFlags>]\]\ ) [🔗<class_XRHandTracker_method_set_hand_joint_flags>]

Sets flags about the validity of the tracking data for the given hand joint.


----



|void| **set_hand_joint_linear_velocity**\ (\ joint\: [HandJoint<enum_XRHandTracker_HandJoint>], linear_velocity\: [Vector3<class_Vector3>]\ ) [🔗<class_XRHandTracker_method_set_hand_joint_linear_velocity>]

Sets the linear velocity for the given hand joint.


----



|void| **set_hand_joint_radius**\ (\ joint\: [HandJoint<enum_XRHandTracker_HandJoint>], radius\: [float<class_float>]\ ) [🔗<class_XRHandTracker_method_set_hand_joint_radius>]

Sets the radius of the given hand joint.


----



|void| **set_hand_joint_transform**\ (\ joint\: [HandJoint<enum_XRHandTracker_HandJoint>], transform\: [Transform3D<class_Transform3D>]\ ) [🔗<class_XRHandTracker_method_set_hand_joint_transform>]

Sets the transform for the given hand joint.

