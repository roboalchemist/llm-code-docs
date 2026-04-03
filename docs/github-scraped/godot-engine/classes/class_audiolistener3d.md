:github_url: hide

> **META**
	:keywords: sound



# AudioListener3D

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Overrides the location sounds are heard from.


## Description

Once added to the scene tree and enabled using [make_current()<class_AudioListener3D_method_make_current>], this node will override the location sounds are heard from. This can be used to listen from a location different from the [Camera3D<class_Camera3D>].


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-------+
> | :ref:`DopplerTracking<enum_AudioListener3D_DopplerTracking>` | :ref:`doppler_tracking<class_AudioListener3D_property_doppler_tracking>` | ``0`` |
> +--------------------------------------------------------------+--------------------------------------------------------------------------+-------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+--------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`clear_current<class_AudioListener3D_method_clear_current>`\ (\ )                           |
> +---------------------------------------+--------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>` | :ref:`get_listener_transform<class_AudioListener3D_method_get_listener_transform>`\ (\ ) |const| |
> +---------------------------------------+--------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`is_current<class_AudioListener3D_method_is_current>`\ (\ ) |const|                         |
> +---------------------------------------+--------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`make_current<class_AudioListener3D_method_make_current>`\ (\ )                             |
> +---------------------------------------+--------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **DopplerTracking**: [🔗<enum_AudioListener3D_DopplerTracking>]



[DopplerTracking<enum_AudioListener3D_DopplerTracking>] **DOPPLER_TRACKING_DISABLED** = `0`

Disables [Doppler effect ](https://en.wikipedia.org/wiki/Doppler_effect)_ simulation (default).



[DopplerTracking<enum_AudioListener3D_DopplerTracking>] **DOPPLER_TRACKING_IDLE_STEP** = `1`

Simulate [Doppler effect ](https://en.wikipedia.org/wiki/Doppler_effect)_ by tracking positions of objects that are changed in `_process`. Changes in the relative velocity of this listener compared to those objects affect how audio is perceived (changing the audio's [AudioStreamPlayer3D.pitch_scale<class_AudioStreamPlayer3D_property_pitch_scale>]).



[DopplerTracking<enum_AudioListener3D_DopplerTracking>] **DOPPLER_TRACKING_PHYSICS_STEP** = `2`

Simulate [Doppler effect ](https://en.wikipedia.org/wiki/Doppler_effect)_ by tracking positions of objects that are changed in `_physics_process`. Changes in the relative velocity of this listener compared to those objects affect how audio is perceived (changing the audio's [AudioStreamPlayer3D.pitch_scale<class_AudioStreamPlayer3D_property_pitch_scale>]).


----


## Property Descriptions



[DopplerTracking<enum_AudioListener3D_DopplerTracking>] **doppler_tracking** = `0` [🔗<class_AudioListener3D_property_doppler_tracking>]


- |void| **set_doppler_tracking**\ (\ value\: [DopplerTracking<enum_AudioListener3D_DopplerTracking>]\ )
- [DopplerTracking<enum_AudioListener3D_DopplerTracking>] **get_doppler_tracking**\ (\ )

If not [DOPPLER_TRACKING_DISABLED<class_AudioListener3D_constant_DOPPLER_TRACKING_DISABLED>], this listener will simulate the [Doppler effect ](https://en.wikipedia.org/wiki/Doppler_effect)_ for objects changed in particular `_process` methods.

\ **Note:** The Doppler effect will only be heard on [AudioStreamPlayer3D<class_AudioStreamPlayer3D>]\ s if [AudioStreamPlayer3D.doppler_tracking<class_AudioStreamPlayer3D_property_doppler_tracking>] is not set to [AudioStreamPlayer3D.DOPPLER_TRACKING_DISABLED<class_AudioStreamPlayer3D_constant_DOPPLER_TRACKING_DISABLED>].


----


## Method Descriptions



|void| **clear_current**\ (\ ) [🔗<class_AudioListener3D_method_clear_current>]

Disables the listener to use the current camera's listener instead.


----



[Transform3D<class_Transform3D>] **get_listener_transform**\ (\ ) |const| [🔗<class_AudioListener3D_method_get_listener_transform>]

Returns the listener's global orthonormalized [Transform3D<class_Transform3D>].


----



[bool<class_bool>] **is_current**\ (\ ) |const| [🔗<class_AudioListener3D_method_is_current>]

Returns `true` if the listener was made current using [make_current()<class_AudioListener3D_method_make_current>], `false` otherwise.

\ **Note:** There may be more than one AudioListener3D marked as "current" in the scene tree, but only the one that was made current last will be used.


----



|void| **make_current**\ (\ ) [🔗<class_AudioListener3D_method_make_current>]

Enables the listener. This will override the current camera's listener.

