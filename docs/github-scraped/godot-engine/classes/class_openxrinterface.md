:github_url: hide



# OpenXRInterface

**Inherits:** [XRInterface<class_XRInterface>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Our OpenXR interface.


## Description

The OpenXR interface allows Godot to interact with OpenXR runtimes and make it possible to create XR experiences and games.

Due to the needs of OpenXR this interface works slightly different than other plugin based XR interfaces. It needs to be initialized when Godot starts. You need to enable OpenXR, settings for this can be found in your games project settings under the XR heading. You do need to mark a viewport for use with XR in order for Godot to know which render result should be output to the headset.


## Tutorials

- [../tutorials/xr/setting_up_xr](Setting up XR .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`display_refresh_rate<class_OpenXRInterface_property_display_refresh_rate>`                   | ``0.0``   |
> +---------------------------+----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`foveation_dynamic<class_OpenXRInterface_property_foveation_dynamic>`                         | ``false`` |
> +---------------------------+----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`     | :ref:`foveation_level<class_OpenXRInterface_property_foveation_level>`                             | ``0``     |
> +---------------------------+----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`render_target_size_multiplier<class_OpenXRInterface_property_render_target_size_multiplier>` | ``1.0``   |
> +---------------------------+----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`vrs_min_radius<class_OpenXRInterface_property_vrs_min_radius>`                               | ``20.0``  |
> +---------------------------+----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`vrs_strength<class_OpenXRInterface_property_vrs_strength>`                                   | ``1.0``   |
> +---------------------------+----------------------------------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                                                | :ref:`get_action_sets<class_OpenXRInterface_method_get_action_sets>`\ (\ ) |const|                                                                                                                                            |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                                                | :ref:`get_available_display_refresh_rates<class_OpenXRInterface_method_get_available_display_refresh_rates>`\ (\ ) |const|                                                                                                    |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                            | :ref:`get_hand_joint_angular_velocity<class_OpenXRInterface_method_get_hand_joint_angular_velocity>`\ (\ hand\: :ref:`Hand<enum_OpenXRInterface_Hand>`, joint\: :ref:`HandJoints<enum_OpenXRInterface_HandJoints>`\ ) |const| |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |bitfield|\[:ref:`HandJointFlags<enum_OpenXRInterface_HandJointFlags>`\] | :ref:`get_hand_joint_flags<class_OpenXRInterface_method_get_hand_joint_flags>`\ (\ hand\: :ref:`Hand<enum_OpenXRInterface_Hand>`, joint\: :ref:`HandJoints<enum_OpenXRInterface_HandJoints>`\ ) |const|                       |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                            | :ref:`get_hand_joint_linear_velocity<class_OpenXRInterface_method_get_hand_joint_linear_velocity>`\ (\ hand\: :ref:`Hand<enum_OpenXRInterface_Hand>`, joint\: :ref:`HandJoints<enum_OpenXRInterface_HandJoints>`\ ) |const|   |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                            | :ref:`get_hand_joint_position<class_OpenXRInterface_method_get_hand_joint_position>`\ (\ hand\: :ref:`Hand<enum_OpenXRInterface_Hand>`, joint\: :ref:`HandJoints<enum_OpenXRInterface_HandJoints>`\ ) |const|                 |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                                | :ref:`get_hand_joint_radius<class_OpenXRInterface_method_get_hand_joint_radius>`\ (\ hand\: :ref:`Hand<enum_OpenXRInterface_Hand>`, joint\: :ref:`HandJoints<enum_OpenXRInterface_HandJoints>`\ ) |const|                     |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Quaternion<class_Quaternion>`                                      | :ref:`get_hand_joint_rotation<class_OpenXRInterface_method_get_hand_joint_rotation>`\ (\ hand\: :ref:`Hand<enum_OpenXRInterface_Hand>`, joint\: :ref:`HandJoints<enum_OpenXRInterface_HandJoints>`\ ) |const|                 |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`HandTrackedSource<enum_OpenXRInterface_HandTrackedSource>`         | :ref:`get_hand_tracking_source<class_OpenXRInterface_method_get_hand_tracking_source>`\ (\ hand\: :ref:`Hand<enum_OpenXRInterface_Hand>`\ ) |const|                                                                           |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`HandMotionRange<enum_OpenXRInterface_HandMotionRange>`             | :ref:`get_motion_range<class_OpenXRInterface_method_get_motion_range>`\ (\ hand\: :ref:`Hand<enum_OpenXRInterface_Hand>`\ ) |const|                                                                                           |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`SessionState<enum_OpenXRInterface_SessionState>`                   | :ref:`get_session_state<class_OpenXRInterface_method_get_session_state>`\ (\ )                                                                                                                                                |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                  | :ref:`is_action_set_active<class_OpenXRInterface_method_is_action_set_active>`\ (\ name\: :ref:`String<class_String>`\ ) |const|                                                                                              |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                  | :ref:`is_eye_gaze_interaction_supported<class_OpenXRInterface_method_is_eye_gaze_interaction_supported>`\ (\ )                                                                                                                |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                  | :ref:`is_foveation_supported<class_OpenXRInterface_method_is_foveation_supported>`\ (\ ) |const|                                                                                                                              |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                  | :ref:`is_hand_interaction_supported<class_OpenXRInterface_method_is_hand_interaction_supported>`\ (\ ) |const|                                                                                                                |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                  | :ref:`is_hand_tracking_supported<class_OpenXRInterface_method_is_hand_tracking_supported>`\ (\ )                                                                                                                              |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                   | :ref:`set_action_set_active<class_OpenXRInterface_method_set_action_set_active>`\ (\ name\: :ref:`String<class_String>`, active\: :ref:`bool<class_bool>`\ )                                                                  |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                   | :ref:`set_cpu_level<class_OpenXRInterface_method_set_cpu_level>`\ (\ level\: :ref:`PerfSettingsLevel<enum_OpenXRInterface_PerfSettingsLevel>`\ )                                                                              |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                   | :ref:`set_gpu_level<class_OpenXRInterface_method_set_gpu_level>`\ (\ level\: :ref:`PerfSettingsLevel<enum_OpenXRInterface_PerfSettingsLevel>`\ )                                                                              |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                   | :ref:`set_motion_range<class_OpenXRInterface_method_set_motion_range>`\ (\ hand\: :ref:`Hand<enum_OpenXRInterface_Hand>`, motion_range\: :ref:`HandMotionRange<enum_OpenXRInterface_HandMotionRange>`\ )                      |
> +--------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**cpu_level_changed**\ (\ sub_domain\: [int<class_int>], from_level\: [int<class_int>], to_level\: [int<class_int>]\ ) [🔗<class_OpenXRInterface_signal_cpu_level_changed>]

Informs the device CPU performance level has changed in the specified subdomain.


----



**gpu_level_changed**\ (\ sub_domain\: [int<class_int>], from_level\: [int<class_int>], to_level\: [int<class_int>]\ ) [🔗<class_OpenXRInterface_signal_gpu_level_changed>]

Informs the device GPU performance level has changed in the specified subdomain.


----



**instance_exiting**\ (\ ) [🔗<class_OpenXRInterface_signal_instance_exiting>]

Informs our OpenXR instance is exiting.


----



**pose_recentered**\ (\ ) [🔗<class_OpenXRInterface_signal_pose_recentered>]

Informs the user queued a recenter of the player position.


----



**refresh_rate_changed**\ (\ refresh_rate\: [float<class_float>]\ ) [🔗<class_OpenXRInterface_signal_refresh_rate_changed>]

Informs the user the HMD refresh rate has changed.

\ **Note:** Only emitted if XR runtime supports the refresh rate extension.


----



**session_begun**\ (\ ) [🔗<class_OpenXRInterface_signal_session_begun>]

Informs our OpenXR session has been started.


----



**session_focussed**\ (\ ) [🔗<class_OpenXRInterface_signal_session_focussed>]

Informs our OpenXR session now has focus, for example output is sent to the HMD and we're receiving XR input.


----



**session_loss_pending**\ (\ ) [🔗<class_OpenXRInterface_signal_session_loss_pending>]

Informs our OpenXR session is in the process of being lost.


----



**session_stopping**\ (\ ) [🔗<class_OpenXRInterface_signal_session_stopping>]

Informs our OpenXR session is stopping.


----



**session_synchronized**\ (\ ) [🔗<class_OpenXRInterface_signal_session_synchronized>]

Informs our OpenXR session has been synchronized.


----



**session_visible**\ (\ ) [🔗<class_OpenXRInterface_signal_session_visible>]

Informs our OpenXR session is now visible, for example output is sent to the HMD but we don't receive XR input.


----


## Enumerations



enum **SessionState**: [🔗<enum_OpenXRInterface_SessionState>]



[SessionState<enum_OpenXRInterface_SessionState>] **SESSION_STATE_UNKNOWN** = `0`

The state of the session is unknown, we haven't tried setting up OpenXR yet.



[SessionState<enum_OpenXRInterface_SessionState>] **SESSION_STATE_IDLE** = `1`

The initial state after the OpenXR session is created or after the session is destroyed.



[SessionState<enum_OpenXRInterface_SessionState>] **SESSION_STATE_READY** = `2`

OpenXR is ready to begin our session. [session_begun<class_OpenXRInterface_signal_session_begun>] is emitted when we change to this state.



[SessionState<enum_OpenXRInterface_SessionState>] **SESSION_STATE_SYNCHRONIZED** = `3`

The application has synched its frame loop with the runtime but we're not rendering anything. [session_synchronized<class_OpenXRInterface_signal_session_synchronized>] is emitted when we change to this state.



[SessionState<enum_OpenXRInterface_SessionState>] **SESSION_STATE_VISIBLE** = `4`

The application has synched its frame loop with the runtime and we're rendering output to the user, however we receive no user input. [session_visible<class_OpenXRInterface_signal_session_visible>] is emitted when we change to this state.

\ **Note:** This is the current state just before we get the focused state, whenever the user opens a system menu, switches to another application, or takes off their headset.



[SessionState<enum_OpenXRInterface_SessionState>] **SESSION_STATE_FOCUSED** = `5`

The application has synched its frame loop with the runtime, we're rendering output to the user and we're receiving XR input. [session_focussed<class_OpenXRInterface_signal_session_focussed>] is emitted when we change to this state.

\ **Note:** This is the state OpenXR will be in when the user can fully interact with your game.



[SessionState<enum_OpenXRInterface_SessionState>] **SESSION_STATE_STOPPING** = `6`

Our session is being stopped. [session_stopping<class_OpenXRInterface_signal_session_stopping>] is emitted when we change to this state.



[SessionState<enum_OpenXRInterface_SessionState>] **SESSION_STATE_LOSS_PENDING** = `7`

The session is about to be lost. [session_loss_pending<class_OpenXRInterface_signal_session_loss_pending>] is emitted when we change to this state.



[SessionState<enum_OpenXRInterface_SessionState>] **SESSION_STATE_EXITING** = `8`

The OpenXR instance is about to be destroyed and we're exiting. [instance_exiting<class_OpenXRInterface_signal_instance_exiting>] is emitted when we change to this state.


----



enum **Hand**: [🔗<enum_OpenXRInterface_Hand>]



[Hand<enum_OpenXRInterface_Hand>] **HAND_LEFT** = `0`

Left hand.



[Hand<enum_OpenXRInterface_Hand>] **HAND_RIGHT** = `1`

Right hand.



[Hand<enum_OpenXRInterface_Hand>] **HAND_MAX** = `2`

Maximum value for the hand enum.


----



enum **HandMotionRange**: [🔗<enum_OpenXRInterface_HandMotionRange>]



[HandMotionRange<enum_OpenXRInterface_HandMotionRange>] **HAND_MOTION_RANGE_UNOBSTRUCTED** = `0`

Full hand range, if user closes their hands, we make a full fist.



[HandMotionRange<enum_OpenXRInterface_HandMotionRange>] **HAND_MOTION_RANGE_CONFORM_TO_CONTROLLER** = `1`

Conform to controller, if user closes their hands, the tracked data conforms to the shape of the controller.



[HandMotionRange<enum_OpenXRInterface_HandMotionRange>] **HAND_MOTION_RANGE_MAX** = `2`

Maximum value for the motion range enum.


----



enum **HandTrackedSource**: [🔗<enum_OpenXRInterface_HandTrackedSource>]



[HandTrackedSource<enum_OpenXRInterface_HandTrackedSource>] **HAND_TRACKED_SOURCE_UNKNOWN** = `0`

The source of hand tracking data is unknown (the extension is likely unsupported).



[HandTrackedSource<enum_OpenXRInterface_HandTrackedSource>] **HAND_TRACKED_SOURCE_UNOBSTRUCTED** = `1`

The source of hand tracking is unobstructed, this means that an accurate method of hand tracking is used, e.g. optical hand tracking, data gloves, etc.



[HandTrackedSource<enum_OpenXRInterface_HandTrackedSource>] **HAND_TRACKED_SOURCE_CONTROLLER** = `2`

The source of hand tracking is a controller, bone positions are inferred from controller inputs.



[HandTrackedSource<enum_OpenXRInterface_HandTrackedSource>] **HAND_TRACKED_SOURCE_MAX** = `3`

Represents the size of the [HandTrackedSource<enum_OpenXRInterface_HandTrackedSource>] enum.


----



enum **HandJoints**: [🔗<enum_OpenXRInterface_HandJoints>]



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_PALM** = `0`

Palm joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_WRIST** = `1`

Wrist joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_THUMB_METACARPAL** = `2`

Thumb metacarpal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_THUMB_PROXIMAL** = `3`

Thumb proximal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_THUMB_DISTAL** = `4`

Thumb distal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_THUMB_TIP** = `5`

Thumb tip joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_INDEX_METACARPAL** = `6`

Index finger metacarpal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_INDEX_PROXIMAL** = `7`

Index finger phalanx proximal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_INDEX_INTERMEDIATE** = `8`

Index finger phalanx intermediate joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_INDEX_DISTAL** = `9`

Index finger phalanx distal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_INDEX_TIP** = `10`

Index finger tip joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_MIDDLE_METACARPAL** = `11`

Middle finger metacarpal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_MIDDLE_PROXIMAL** = `12`

Middle finger phalanx proximal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_MIDDLE_INTERMEDIATE** = `13`

Middle finger phalanx intermediate joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_MIDDLE_DISTAL** = `14`

Middle finger phalanx distal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_MIDDLE_TIP** = `15`

Middle finger tip joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_RING_METACARPAL** = `16`

Ring finger metacarpal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_RING_PROXIMAL** = `17`

Ring finger phalanx proximal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_RING_INTERMEDIATE** = `18`

Ring finger phalanx intermediate joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_RING_DISTAL** = `19`

Ring finger phalanx distal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_RING_TIP** = `20`

Ring finger tip joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_LITTLE_METACARPAL** = `21`

Pinky finger metacarpal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_LITTLE_PROXIMAL** = `22`

Pinky finger phalanx proximal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_LITTLE_INTERMEDIATE** = `23`

Pinky finger phalanx intermediate joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_LITTLE_DISTAL** = `24`

Pinky finger phalanx distal joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_LITTLE_TIP** = `25`

Pinky finger tip joint.



[HandJoints<enum_OpenXRInterface_HandJoints>] **HAND_JOINT_MAX** = `26`

Represents the size of the [HandJoints<enum_OpenXRInterface_HandJoints>] enum.


----



enum **PerfSettingsLevel**: [🔗<enum_OpenXRInterface_PerfSettingsLevel>]



[PerfSettingsLevel<enum_OpenXRInterface_PerfSettingsLevel>] **PERF_SETTINGS_LEVEL_POWER_SAVINGS** = `0`

The application has entered a non-XR section (head-locked / static screen), during which power savings are to be prioritized.



[PerfSettingsLevel<enum_OpenXRInterface_PerfSettingsLevel>] **PERF_SETTINGS_LEVEL_SUSTAINED_LOW** = `1`

The application has entered a low and stable complexity section, during which reducing power is more important than occasional late rendering frames.



[PerfSettingsLevel<enum_OpenXRInterface_PerfSettingsLevel>] **PERF_SETTINGS_LEVEL_SUSTAINED_HIGH** = `2`

The application has entered a high or dynamic complexity section, during which the XR Runtime strives for consistent XR compositing and frame rendering within a thermally sustainable range.



[PerfSettingsLevel<enum_OpenXRInterface_PerfSettingsLevel>] **PERF_SETTINGS_LEVEL_BOOST** = `3`

The application has entered a section with very high complexity, during which the XR Runtime is allowed to step up beyond the thermally sustainable range.


----



enum **PerfSettingsSubDomain**: [🔗<enum_OpenXRInterface_PerfSettingsSubDomain>]



[PerfSettingsSubDomain<enum_OpenXRInterface_PerfSettingsSubDomain>] **PERF_SETTINGS_SUB_DOMAIN_COMPOSITING** = `0`

The compositing performance within the runtime has reached a new level.



[PerfSettingsSubDomain<enum_OpenXRInterface_PerfSettingsSubDomain>] **PERF_SETTINGS_SUB_DOMAIN_RENDERING** = `1`

The application rendering performance has reached a new level.



[PerfSettingsSubDomain<enum_OpenXRInterface_PerfSettingsSubDomain>] **PERF_SETTINGS_SUB_DOMAIN_THERMAL** = `2`

The temperature of the device has reached a new level.


----



enum **PerfSettingsNotificationLevel**: [🔗<enum_OpenXRInterface_PerfSettingsNotificationLevel>]



[PerfSettingsNotificationLevel<enum_OpenXRInterface_PerfSettingsNotificationLevel>] **PERF_SETTINGS_NOTIF_LEVEL_NORMAL** = `0`

The sub-domain has reached a level where no further actions other than currently applied are necessary.



[PerfSettingsNotificationLevel<enum_OpenXRInterface_PerfSettingsNotificationLevel>] **PERF_SETTINGS_NOTIF_LEVEL_WARNING** = `1`

The sub-domain has reached an early warning level where the application should start proactive mitigation actions.



[PerfSettingsNotificationLevel<enum_OpenXRInterface_PerfSettingsNotificationLevel>] **PERF_SETTINGS_NOTIF_LEVEL_IMPAIRED** = `2`

The sub-domain has reached a critical level where the application should start drastic mitigation actions.


----



flags **HandJointFlags**: [🔗<enum_OpenXRInterface_HandJointFlags>]



[HandJointFlags<enum_OpenXRInterface_HandJointFlags>] **HAND_JOINT_NONE** = `0`

No flags are set.



[HandJointFlags<enum_OpenXRInterface_HandJointFlags>] **HAND_JOINT_ORIENTATION_VALID** = `1`

If set, the orientation data is valid, otherwise, the orientation data is unreliable and should not be used.



[HandJointFlags<enum_OpenXRInterface_HandJointFlags>] **HAND_JOINT_ORIENTATION_TRACKED** = `2`

If set, the orientation data comes from tracking data, otherwise, the orientation data contains predicted data.



[HandJointFlags<enum_OpenXRInterface_HandJointFlags>] **HAND_JOINT_POSITION_VALID** = `4`

If set, the positional data is valid, otherwise, the positional data is unreliable and should not be used.



[HandJointFlags<enum_OpenXRInterface_HandJointFlags>] **HAND_JOINT_POSITION_TRACKED** = `8`

If set, the positional data comes from tracking data, otherwise, the positional data contains predicted data.



[HandJointFlags<enum_OpenXRInterface_HandJointFlags>] **HAND_JOINT_LINEAR_VELOCITY_VALID** = `16`

If set, our linear velocity data is valid, otherwise, the linear velocity data is unreliable and should not be used.



[HandJointFlags<enum_OpenXRInterface_HandJointFlags>] **HAND_JOINT_ANGULAR_VELOCITY_VALID** = `32`

If set, our angular velocity data is valid, otherwise, the angular velocity data is unreliable and should not be used.


----


## Property Descriptions



[float<class_float>] **display_refresh_rate** = `0.0` [🔗<class_OpenXRInterface_property_display_refresh_rate>]


- |void| **set_display_refresh_rate**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_display_refresh_rate**\ (\ )

The display refresh rate for the current HMD. Only functional if this feature is supported by the OpenXR runtime and after the interface has been initialized.


----



[bool<class_bool>] **foveation_dynamic** = `false` [🔗<class_OpenXRInterface_property_foveation_dynamic>]


- |void| **set_foveation_dynamic**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_foveation_dynamic**\ (\ )

If `true`, enables dynamic foveation adjustment. The interface must be initialized before this is accessible. If enabled, foveation will automatically be adjusted between low and [foveation_level<class_OpenXRInterface_property_foveation_level>].

\ **Note:** Only works on the Compatibility renderer.


----



[int<class_int>] **foveation_level** = `0` [🔗<class_OpenXRInterface_property_foveation_level>]


- |void| **set_foveation_level**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_foveation_level**\ (\ )

The foveation level, from `0` (off) to `3` (high). The interface must be initialized before this is accessible.

\ **Note:** Only works on the Compatibility renderer.


----



[float<class_float>] **render_target_size_multiplier** = `1.0` [🔗<class_OpenXRInterface_property_render_target_size_multiplier>]


- |void| **set_render_target_size_multiplier**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_render_target_size_multiplier**\ (\ )

The render size multiplier for the current HMD. Must be set before the interface has been initialized.


----



[float<class_float>] **vrs_min_radius** = `20.0` [🔗<class_OpenXRInterface_property_vrs_min_radius>]


- |void| **set_vrs_min_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_vrs_min_radius**\ (\ )

The minimum radius around the focal point where full quality is guaranteed if VRS is used as a percentage of screen size.

\ **Note:** Mobile and Forward+ renderers only. Requires [Viewport.vrs_mode<class_Viewport_property_vrs_mode>] to be set to [Viewport.VRS_XR<class_Viewport_constant_VRS_XR>].


----



[float<class_float>] **vrs_strength** = `1.0` [🔗<class_OpenXRInterface_property_vrs_strength>]


- |void| **set_vrs_strength**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_vrs_strength**\ (\ )

The strength used to calculate the VRS density map. The greater this value, the more noticeable VRS is. This improves performance at the cost of quality.

\ **Note:** Mobile and Forward+ renderers only. Requires [Viewport.vrs_mode<class_Viewport_property_vrs_mode>] to be set to [Viewport.VRS_XR<class_Viewport_constant_VRS_XR>].


----


## Method Descriptions



[Array<class_Array>] **get_action_sets**\ (\ ) |const| [🔗<class_OpenXRInterface_method_get_action_sets>]

Returns a list of action sets registered with Godot (loaded from the action map at runtime).


----



[Array<class_Array>] **get_available_display_refresh_rates**\ (\ ) |const| [🔗<class_OpenXRInterface_method_get_available_display_refresh_rates>]

Returns a list of display refresh rates supported by the current HMD. Only returned if this feature is supported by the OpenXR runtime and after the interface has been initialized.


----



[Vector3<class_Vector3>] **get_hand_joint_angular_velocity**\ (\ hand\: [Hand<enum_OpenXRInterface_Hand>], joint\: [HandJoints<enum_OpenXRInterface_HandJoints>]\ ) |const| [🔗<class_OpenXRInterface_method_get_hand_joint_angular_velocity>]

**Deprecated:** Use [XRHandTracker.get_hand_joint_angular_velocity()<class_XRHandTracker_method_get_hand_joint_angular_velocity>] obtained from [XRServer.get_tracker()<class_XRServer_method_get_tracker>] instead.

If handtracking is enabled, returns the angular velocity of a joint (`joint`) of a hand (`hand`) as provided by OpenXR. This is relative to [XROrigin3D<class_XROrigin3D>]!


----



|bitfield|\[[HandJointFlags<enum_OpenXRInterface_HandJointFlags>]\] **get_hand_joint_flags**\ (\ hand\: [Hand<enum_OpenXRInterface_Hand>], joint\: [HandJoints<enum_OpenXRInterface_HandJoints>]\ ) |const| [🔗<class_OpenXRInterface_method_get_hand_joint_flags>]

**Deprecated:** Use [XRHandTracker.get_hand_joint_flags()<class_XRHandTracker_method_get_hand_joint_flags>] obtained from [XRServer.get_tracker()<class_XRServer_method_get_tracker>] instead.

If handtracking is enabled, returns flags that inform us of the validity of the tracking data.


----



[Vector3<class_Vector3>] **get_hand_joint_linear_velocity**\ (\ hand\: [Hand<enum_OpenXRInterface_Hand>], joint\: [HandJoints<enum_OpenXRInterface_HandJoints>]\ ) |const| [🔗<class_OpenXRInterface_method_get_hand_joint_linear_velocity>]

**Deprecated:** Use [XRHandTracker.get_hand_joint_linear_velocity()<class_XRHandTracker_method_get_hand_joint_linear_velocity>] obtained from [XRServer.get_tracker()<class_XRServer_method_get_tracker>] instead.

If handtracking is enabled, returns the linear velocity of a joint (`joint`) of a hand (`hand`) as provided by OpenXR. This is relative to [XROrigin3D<class_XROrigin3D>] without worldscale applied!


----



[Vector3<class_Vector3>] **get_hand_joint_position**\ (\ hand\: [Hand<enum_OpenXRInterface_Hand>], joint\: [HandJoints<enum_OpenXRInterface_HandJoints>]\ ) |const| [🔗<class_OpenXRInterface_method_get_hand_joint_position>]

**Deprecated:** Use [XRHandTracker.get_hand_joint_transform()<class_XRHandTracker_method_get_hand_joint_transform>] obtained from [XRServer.get_tracker()<class_XRServer_method_get_tracker>] instead.

If handtracking is enabled, returns the position of a joint (`joint`) of a hand (`hand`) as provided by OpenXR. This is relative to [XROrigin3D<class_XROrigin3D>] without worldscale applied!


----



[float<class_float>] **get_hand_joint_radius**\ (\ hand\: [Hand<enum_OpenXRInterface_Hand>], joint\: [HandJoints<enum_OpenXRInterface_HandJoints>]\ ) |const| [🔗<class_OpenXRInterface_method_get_hand_joint_radius>]

**Deprecated:** Use [XRHandTracker.get_hand_joint_radius()<class_XRHandTracker_method_get_hand_joint_radius>] obtained from [XRServer.get_tracker()<class_XRServer_method_get_tracker>] instead.

If handtracking is enabled, returns the radius of a joint (`joint`) of a hand (`hand`) as provided by OpenXR. This is without worldscale applied!


----



[Quaternion<class_Quaternion>] **get_hand_joint_rotation**\ (\ hand\: [Hand<enum_OpenXRInterface_Hand>], joint\: [HandJoints<enum_OpenXRInterface_HandJoints>]\ ) |const| [🔗<class_OpenXRInterface_method_get_hand_joint_rotation>]

**Deprecated:** Use [XRHandTracker.get_hand_joint_transform()<class_XRHandTracker_method_get_hand_joint_transform>] obtained from [XRServer.get_tracker()<class_XRServer_method_get_tracker>] instead.

If handtracking is enabled, returns the rotation of a joint (`joint`) of a hand (`hand`) as provided by OpenXR.


----



[HandTrackedSource<enum_OpenXRInterface_HandTrackedSource>] **get_hand_tracking_source**\ (\ hand\: [Hand<enum_OpenXRInterface_Hand>]\ ) |const| [🔗<class_OpenXRInterface_method_get_hand_tracking_source>]

**Deprecated:** Use [XRHandTracker.hand_tracking_source<class_XRHandTracker_property_hand_tracking_source>] obtained from [XRServer.get_tracker()<class_XRServer_method_get_tracker>] instead.

If handtracking is enabled and hand tracking source is supported, gets the source of the hand tracking data for `hand`.


----



[HandMotionRange<enum_OpenXRInterface_HandMotionRange>] **get_motion_range**\ (\ hand\: [Hand<enum_OpenXRInterface_Hand>]\ ) |const| [🔗<class_OpenXRInterface_method_get_motion_range>]

If handtracking is enabled and motion range is supported, gets the currently configured motion range for `hand`.


----



[SessionState<enum_OpenXRInterface_SessionState>] **get_session_state**\ (\ ) [🔗<class_OpenXRInterface_method_get_session_state>]

Returns the current state of our OpenXR session.


----



[bool<class_bool>] **is_action_set_active**\ (\ name\: [String<class_String>]\ ) |const| [🔗<class_OpenXRInterface_method_is_action_set_active>]

Returns `true` if the given action set is active.


----



[bool<class_bool>] **is_eye_gaze_interaction_supported**\ (\ ) [🔗<class_OpenXRInterface_method_is_eye_gaze_interaction_supported>]

Returns the capabilities of the eye gaze interaction extension.

\ **Note:** This only returns a valid value after OpenXR has been initialized.


----



[bool<class_bool>] **is_foveation_supported**\ (\ ) |const| [🔗<class_OpenXRInterface_method_is_foveation_supported>]

Returns `true` if OpenXR's foveation extension is supported. The interface must be initialized before this returns a valid value.

\ **Note:** When using the Vulkan rendering driver, [Viewport.vrs_mode<class_Viewport_property_vrs_mode>] must be set to [Viewport.VRS_XR<class_Viewport_constant_VRS_XR>] to support foveation.


----



[bool<class_bool>] **is_hand_interaction_supported**\ (\ ) |const| [🔗<class_OpenXRInterface_method_is_hand_interaction_supported>]

Returns `true` if OpenXR's hand interaction profile is supported and enabled.

\ **Note:** This only returns a valid value after OpenXR has been initialized.


----



[bool<class_bool>] **is_hand_tracking_supported**\ (\ ) [🔗<class_OpenXRInterface_method_is_hand_tracking_supported>]

Returns `true` if OpenXR's hand tracking is supported and enabled.

\ **Note:** This only returns a valid value after OpenXR has been initialized.


----



|void| **set_action_set_active**\ (\ name\: [String<class_String>], active\: [bool<class_bool>]\ ) [🔗<class_OpenXRInterface_method_set_action_set_active>]

Sets the given action set as active or inactive.


----



|void| **set_cpu_level**\ (\ level\: [PerfSettingsLevel<enum_OpenXRInterface_PerfSettingsLevel>]\ ) [🔗<class_OpenXRInterface_method_set_cpu_level>]

Sets the CPU performance level of the OpenXR device.


----



|void| **set_gpu_level**\ (\ level\: [PerfSettingsLevel<enum_OpenXRInterface_PerfSettingsLevel>]\ ) [🔗<class_OpenXRInterface_method_set_gpu_level>]

Sets the GPU performance level of the OpenXR device.


----



|void| **set_motion_range**\ (\ hand\: [Hand<enum_OpenXRInterface_Hand>], motion_range\: [HandMotionRange<enum_OpenXRInterface_HandMotionRange>]\ ) [🔗<class_OpenXRInterface_method_set_motion_range>]

If handtracking is enabled and motion range is supported, sets the currently configured motion range for `hand` to `motion_range`.

