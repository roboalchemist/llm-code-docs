:github_url: hide



# XRNode3D

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [XRAnchor3D<class_XRAnchor3D>], [XRController3D<class_XRController3D>]

A 3D node that has its position automatically updated by the [XRServer<class_XRServer>].


## Description

This node can be bound to a specific pose of an [XRPositionalTracker<class_XRPositionalTracker>] and will automatically have its [Node3D.transform<class_Node3D_property_transform>] updated by the [XRServer<class_XRServer>]. Nodes of this type must be added as children of the [XROrigin3D<class_XROrigin3D>] node.


## Tutorials

- [../tutorials/xr/index](XR documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`PhysicsInterpolationMode<enum_Node_PhysicsInterpolationMode>` | physics_interpolation_mode                                          | ``2`` (overrides :ref:`Node<class_Node_property_physics_interpolation_mode>`) |
> +---------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                                 | :ref:`pose<class_XRNode3D_property_pose>`                           | ``&"default"``                                                                |
> +---------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                             | :ref:`show_when_tracked<class_XRNode3D_property_show_when_tracked>` | ``false``                                                                     |
> +---------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                                 | :ref:`tracker<class_XRNode3D_property_tracker>`                     | ``&""``                                                                       |
> +---------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`get_has_tracking_data<class_XRNode3D_method_get_has_tracking_data>`\ (\ ) |const|                                                                                                                                                                                                 |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`get_is_active<class_XRNode3D_method_get_is_active>`\ (\ ) |const|                                                                                                                                                                                                                 |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`XRPose<class_XRPose>` | :ref:`get_pose<class_XRNode3D_method_get_pose>`\ (\ )                                                                                                                                                                                                                                   |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`trigger_haptic_pulse<class_XRNode3D_method_trigger_haptic_pulse>`\ (\ action_name\: :ref:`String<class_String>`, frequency\: :ref:`float<class_float>`, amplitude\: :ref:`float<class_float>`, duration_sec\: :ref:`float<class_float>`, delay_sec\: :ref:`float<class_float>`\ ) |
> +-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**tracking_changed**\ (\ tracking\: [bool<class_bool>]\ ) [🔗<class_XRNode3D_signal_tracking_changed>]

Emitted when the [tracker<class_XRNode3D_property_tracker>] starts or stops receiving updated tracking data for the [pose<class_XRNode3D_property_pose>] being tracked. The `tracking` argument indicates whether the tracker is getting updated tracking data.


----


## Property Descriptions



[StringName<class_StringName>] **pose** = `&"default"` [🔗<class_XRNode3D_property_pose>]


- |void| **set_pose_name**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_pose_name**\ (\ )

The name of the pose we're bound to. Which poses a tracker supports is not known during design time.

Godot defines number of standard pose names such as `aim` and `grip` but other may be configured within a given [XRInterface<class_XRInterface>].


----



[bool<class_bool>] **show_when_tracked** = `false` [🔗<class_XRNode3D_property_show_when_tracked>]


- |void| **set_show_when_tracked**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_show_when_tracked**\ (\ )

Enables showing the node when tracking starts, and hiding the node when tracking is lost.


----



[StringName<class_StringName>] **tracker** = `&""` [🔗<class_XRNode3D_property_tracker>]


- |void| **set_tracker**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_tracker**\ (\ )

The name of the tracker we're bound to. Which trackers are available is not known during design time.

Godot defines a number of standard trackers such as `left_hand` and `right_hand` but others may be configured within a given [XRInterface<class_XRInterface>].


----


## Method Descriptions



[bool<class_bool>] **get_has_tracking_data**\ (\ ) |const| [🔗<class_XRNode3D_method_get_has_tracking_data>]

Returns `true` if the [tracker<class_XRNode3D_property_tracker>] has current tracking data for the [pose<class_XRNode3D_property_pose>] being tracked.


----



[bool<class_bool>] **get_is_active**\ (\ ) |const| [🔗<class_XRNode3D_method_get_is_active>]

Returns `true` if the [tracker<class_XRNode3D_property_tracker>] has been registered and the [pose<class_XRNode3D_property_pose>] is being tracked.


----



[XRPose<class_XRPose>] **get_pose**\ (\ ) [🔗<class_XRNode3D_method_get_pose>]

Returns the [XRPose<class_XRPose>] containing the current state of the pose being tracked. This gives access to additional properties of this pose.


----



|void| **trigger_haptic_pulse**\ (\ action_name\: [String<class_String>], frequency\: [float<class_float>], amplitude\: [float<class_float>], duration_sec\: [float<class_float>], delay_sec\: [float<class_float>]\ ) [🔗<class_XRNode3D_method_trigger_haptic_pulse>]

Triggers a haptic pulse on a device associated with this interface.

\ `action_name` is the name of the action for this pulse.

\ `frequency` is the frequency of the pulse, set to `0.0` to have the system use a default frequency.

\ `amplitude` is the amplitude of the pulse between `0.0` and `1.0`.

\ `duration_sec` is the duration of the pulse in seconds.

\ `delay_sec` is a delay in seconds before the pulse is given.

