:github_url: hide



# XRPositionalTracker

**Inherits:** [XRTracker<class_XRTracker>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [OpenXRSpatialEntityTracker<class_OpenXRSpatialEntityTracker>], [XRBodyTracker<class_XRBodyTracker>], [XRControllerTracker<class_XRControllerTracker>], [XRHandTracker<class_XRHandTracker>]

A tracked object.


## Description

An instance of this object represents a device that is tracked, such as a controller or anchor point. HMDs aren't represented here as they are handled internally.

As controllers are turned on and the [XRInterface<class_XRInterface>] detects them, instances of this object are automatically added to this list of active tracking objects accessible through the [XRServer<class_XRServer>].

The [XRNode3D<class_XRNode3D>] and [XRAnchor3D<class_XRAnchor3D>] both consume objects of this type and should be used in your project. The positional trackers are just under-the-hood objects that make this all work. These are mostly exposed so that GDExtension-based interfaces can interact with them.


## Tutorials

- [../tutorials/xr/index](XR documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------+------------------------------------------------------------+--------+
> | :ref:`TrackerHand<enum_XRPositionalTracker_TrackerHand>` | :ref:`hand<class_XRPositionalTracker_property_hand>`       | ``0``  |
> +----------------------------------------------------------+------------------------------------------------------------+--------+
> | :ref:`String<class_String>`                              | :ref:`profile<class_XRPositionalTracker_property_profile>` | ``""`` |
> +----------------------------------------------------------+------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`get_input<class_XRPositionalTracker_method_get_input>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                                                                                              |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`XRPose<class_XRPose>`   | :ref:`get_pose<class_XRPositionalTracker_method_get_pose>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                                                                                                |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`has_pose<class_XRPositionalTracker_method_has_pose>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                                                                                                |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`invalidate_pose<class_XRPositionalTracker_method_invalidate_pose>`\ (\ name\: :ref:`StringName<class_StringName>`\ )                                                                                                                                                                                                                          |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_input<class_XRPositionalTracker_method_set_input>`\ (\ name\: :ref:`StringName<class_StringName>`, value\: :ref:`Variant<class_Variant>`\ )                                                                                                                                                                                               |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_pose<class_XRPositionalTracker_method_set_pose>`\ (\ name\: :ref:`StringName<class_StringName>`, transform\: :ref:`Transform3D<class_Transform3D>`, linear_velocity\: :ref:`Vector3<class_Vector3>`, angular_velocity\: :ref:`Vector3<class_Vector3>`, tracking_confidence\: :ref:`TrackingConfidence<enum_XRPose_TrackingConfidence>`\ ) |
> +-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**button_pressed**\ (\ name\: [String<class_String>]\ ) [🔗<class_XRPositionalTracker_signal_button_pressed>]

Emitted when a button on this tracker is pressed. Note that many XR runtimes allow other inputs to be mapped to buttons.


----



**button_released**\ (\ name\: [String<class_String>]\ ) [🔗<class_XRPositionalTracker_signal_button_released>]

Emitted when a button on this tracker is released.


----



**input_float_changed**\ (\ name\: [String<class_String>], value\: [float<class_float>]\ ) [🔗<class_XRPositionalTracker_signal_input_float_changed>]

Emitted when a trigger or similar input on this tracker changes value.


----



**input_vector2_changed**\ (\ name\: [String<class_String>], vector\: [Vector2<class_Vector2>]\ ) [🔗<class_XRPositionalTracker_signal_input_vector2_changed>]

Emitted when a thumbstick or thumbpad on this tracker moves.


----



**pose_changed**\ (\ pose\: [XRPose<class_XRPose>]\ ) [🔗<class_XRPositionalTracker_signal_pose_changed>]

Emitted when the state of a pose tracked by this tracker changes.


----



**pose_lost_tracking**\ (\ pose\: [XRPose<class_XRPose>]\ ) [🔗<class_XRPositionalTracker_signal_pose_lost_tracking>]

Emitted when a pose tracked by this tracker stops getting updated tracking data.


----



**profile_changed**\ (\ role\: [String<class_String>]\ ) [🔗<class_XRPositionalTracker_signal_profile_changed>]

Emitted when the profile of our tracker changes.


----


## Enumerations



enum **TrackerHand**: [🔗<enum_XRPositionalTracker_TrackerHand>]



[TrackerHand<enum_XRPositionalTracker_TrackerHand>] **TRACKER_HAND_UNKNOWN** = `0`

The hand this tracker is held in is unknown or not applicable.



[TrackerHand<enum_XRPositionalTracker_TrackerHand>] **TRACKER_HAND_LEFT** = `1`

This tracker is the left hand controller.



[TrackerHand<enum_XRPositionalTracker_TrackerHand>] **TRACKER_HAND_RIGHT** = `2`

This tracker is the right hand controller.



[TrackerHand<enum_XRPositionalTracker_TrackerHand>] **TRACKER_HAND_MAX** = `3`

Represents the size of the [TrackerHand<enum_XRPositionalTracker_TrackerHand>] enum.


----


## Property Descriptions



[TrackerHand<enum_XRPositionalTracker_TrackerHand>] **hand** = `0` [🔗<class_XRPositionalTracker_property_hand>]


- |void| **set_tracker_hand**\ (\ value\: [TrackerHand<enum_XRPositionalTracker_TrackerHand>]\ )
- [TrackerHand<enum_XRPositionalTracker_TrackerHand>] **get_tracker_hand**\ (\ )

Defines which hand this tracker relates to.


----



[String<class_String>] **profile** = `""` [🔗<class_XRPositionalTracker_property_profile>]


- |void| **set_tracker_profile**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_tracker_profile**\ (\ )

The profile associated with this tracker, interface dependent but will indicate the type of controller being tracked.


----


## Method Descriptions



[Variant<class_Variant>] **get_input**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_XRPositionalTracker_method_get_input>]

**Deprecated:** Use through [XRControllerTracker<class_XRControllerTracker>].

Returns an input for this tracker. It can return a boolean, float or [Vector2<class_Vector2>] value depending on whether the input is a button, trigger or thumbstick/thumbpad.


----



[XRPose<class_XRPose>] **get_pose**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_XRPositionalTracker_method_get_pose>]

Returns the current [XRPose<class_XRPose>] state object for the bound `name` pose.


----



[bool<class_bool>] **has_pose**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_XRPositionalTracker_method_has_pose>]

Returns `true` if the tracker is available and is currently tracking the bound `name` pose.


----



|void| **invalidate_pose**\ (\ name\: [StringName<class_StringName>]\ ) [🔗<class_XRPositionalTracker_method_invalidate_pose>]

Marks this pose as invalid, we don't clear the last reported state but it allows users to decide if trackers need to be hidden if we lose tracking or just remain at their last known position.


----



|void| **set_input**\ (\ name\: [StringName<class_StringName>], value\: [Variant<class_Variant>]\ ) [🔗<class_XRPositionalTracker_method_set_input>]

**Deprecated:** Use through [XRControllerTracker<class_XRControllerTracker>].

Changes the value for the given input. This method is called by an [XRInterface<class_XRInterface>] implementation and should not be used directly.


----



|void| **set_pose**\ (\ name\: [StringName<class_StringName>], transform\: [Transform3D<class_Transform3D>], linear_velocity\: [Vector3<class_Vector3>], angular_velocity\: [Vector3<class_Vector3>], tracking_confidence\: [TrackingConfidence<enum_XRPose_TrackingConfidence>]\ ) [🔗<class_XRPositionalTracker_method_set_pose>]

Sets the transform, linear velocity, angular velocity and tracking confidence for the given pose. This method is called by an [XRInterface<class_XRInterface>] implementation and should not be used directly.

