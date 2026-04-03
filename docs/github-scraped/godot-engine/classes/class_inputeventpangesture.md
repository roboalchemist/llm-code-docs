:github_url: hide



# InputEventPanGesture

**Inherits:** [InputEventGesture<class_InputEventGesture>] **<** [InputEventWithModifiers<class_InputEventWithModifiers>] **<** [InputEventFromWindow<class_InputEventFromWindow>] **<** [InputEvent<class_InputEvent>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a panning touch gesture.


## Description

Stores information about pan gestures. A pan gesture is performed when the user swipes the touch screen with two fingers. It's typically used for panning/scrolling.

\ **Note:** On Android, this requires the [ProjectSettings.input_devices/pointing/android/enable_pan_and_scale_gestures<class_ProjectSettings_property_input_devices/pointing/android/enable_pan_and_scale_gestures>] project setting to be enabled.


## Tutorials

- [../tutorials/inputs/inputevent](Using InputEvent .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+---------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`delta<class_InputEventPanGesture_property_delta>` | ``Vector2(0, 0)`` |
> +-------------------------------+---------------------------------------------------------+-------------------+
>

----


## Property Descriptions



[Vector2<class_Vector2>] **delta** = `Vector2(0, 0)` [🔗<class_InputEventPanGesture_property_delta>]


- |void| **set_delta**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_delta**\ (\ )

Panning amount since last pan event.

