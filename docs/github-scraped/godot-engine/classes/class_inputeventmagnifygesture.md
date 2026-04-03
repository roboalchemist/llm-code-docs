:github_url: hide



# InputEventMagnifyGesture

**Inherits:** [InputEventGesture<class_InputEventGesture>] **<** [InputEventWithModifiers<class_InputEventWithModifiers>] **<** [InputEventFromWindow<class_InputEventFromWindow>] **<** [InputEvent<class_InputEvent>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a magnifying touch gesture.


## Description

Stores the factor of a magnifying touch gesture. This is usually performed when the user pinches the touch screen and used for zooming in/out.

\ **Note:** On Android, this requires the [ProjectSettings.input_devices/pointing/android/enable_pan_and_scale_gestures<class_ProjectSettings_property_input_devices/pointing/android/enable_pan_and_scale_gestures>] project setting to be enabled.


## Tutorials

- [../tutorials/inputs/inputevent](Using InputEvent .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`factor<class_InputEventMagnifyGesture_property_factor>` | ``1.0`` |
> +---------------------------+---------------------------------------------------------------+---------+
>

----


## Property Descriptions



[float<class_float>] **factor** = `1.0` [🔗<class_InputEventMagnifyGesture_property_factor>]


- |void| **set_factor**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_factor**\ (\ )

The amount (or delta) of the event. This value is closer to `1.0` the slower the gesture is performed.

