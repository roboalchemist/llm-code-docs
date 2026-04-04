:github_url: hide



# XRTracker

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [XRFaceTracker<class_XRFaceTracker>], [XRPositionalTracker<class_XRPositionalTracker>]

A tracked object.


## Description

This object is the base of all XR trackers.


## Tutorials

- [../tutorials/xr/index](XR documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+----------------------------------------------------------+----------------+
> | :ref:`String<class_String>`                   | :ref:`description<class_XRTracker_property_description>` | ``""``         |
> +-----------------------------------------------+----------------------------------------------------------+----------------+
> | :ref:`StringName<class_StringName>`           | :ref:`name<class_XRTracker_property_name>`               | ``&"Unknown"`` |
> +-----------------------------------------------+----------------------------------------------------------+----------------+
> | :ref:`TrackerType<enum_XRServer_TrackerType>` | :ref:`type<class_XRTracker_property_type>`               | ``128``        |
> +-----------------------------------------------+----------------------------------------------------------+----------------+
>

----


## Property Descriptions



[String<class_String>] **description** = `""` [🔗<class_XRTracker_property_description>]


- |void| **set_tracker_desc**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_tracker_desc**\ (\ )

The description of this tracker.


----



[StringName<class_StringName>] **name** = `&"Unknown"` [🔗<class_XRTracker_property_name>]


- |void| **set_tracker_name**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_tracker_name**\ (\ )

The unique name of this tracker. The trackers that are available differ between various XR runtimes and can often be configured by the user. Godot maintains a number of reserved names that it expects the [XRInterface<class_XRInterface>] to implement if applicable:

- `"head"` identifies the [XRPositionalTracker<class_XRPositionalTracker>] of the player's head

- `"left_hand"` identifies the [XRControllerTracker<class_XRControllerTracker>] in the player's left hand

- `"right_hand"` identifies the [XRControllerTracker<class_XRControllerTracker>] in the player's right hand

- `"/user/hand_tracker/left"` identifies the [XRHandTracker<class_XRHandTracker>] for the player's left hand

- `"/user/hand_tracker/right"` identifies the [XRHandTracker<class_XRHandTracker>] for the player's right hand

- `"/user/body_tracker"` identifies the [XRBodyTracker<class_XRBodyTracker>] for the player's body

- `"/user/face_tracker"` identifies the [XRFaceTracker<class_XRFaceTracker>] for the player's face


----



[TrackerType<enum_XRServer_TrackerType>] **type** = `128` [🔗<class_XRTracker_property_type>]


- |void| **set_tracker_type**\ (\ value\: [TrackerType<enum_XRServer_TrackerType>]\ )
- [TrackerType<enum_XRServer_TrackerType>] **get_tracker_type**\ (\ )

The type of tracker.

