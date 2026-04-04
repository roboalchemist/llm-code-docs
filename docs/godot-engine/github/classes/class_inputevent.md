:github_url: hide



# InputEvent

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [InputEventAction<class_InputEventAction>], [InputEventFromWindow<class_InputEventFromWindow>], [InputEventJoypadButton<class_InputEventJoypadButton>], [InputEventJoypadMotion<class_InputEventJoypadMotion>], [InputEventMIDI<class_InputEventMIDI>], [InputEventShortcut<class_InputEventShortcut>]

Abstract base class for input events.


## Description

Abstract base class of all types of input events. See [Node._input()<class_Node_private_method__input>].


## Tutorials

- [../tutorials/inputs/inputevent](Using InputEvent .md)

- [../tutorials/2d/2d_transforms](Viewport and canvas transforms .md)

- [2D Dodge The Creeps Demo ](https://godotengine.org/asset-library/asset/2712)_

- [3D Voxel Demo ](https://godotengine.org/asset-library/asset/2755)_


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+-------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`device<class_InputEvent_property_device>` | ``0`` |
> +-----------------------+-------------------------------------------------+-------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`accumulate<class_InputEvent_method_accumulate>`\ (\ with_event\: :ref:`InputEvent<class_InputEvent>`\ )                                                                                                                |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`         | :ref:`as_text<class_InputEvent_method_as_text>`\ (\ ) |const|                                                                                                                                                                |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`           | :ref:`get_action_strength<class_InputEvent_method_get_action_strength>`\ (\ action\: :ref:`StringName<class_StringName>`, exact_match\: :ref:`bool<class_bool>` = false\ ) |const|                                           |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_action<class_InputEvent_method_is_action>`\ (\ action\: :ref:`StringName<class_StringName>`, exact_match\: :ref:`bool<class_bool>` = false\ ) |const|                                                               |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_action_pressed<class_InputEvent_method_is_action_pressed>`\ (\ action\: :ref:`StringName<class_StringName>`, allow_echo\: :ref:`bool<class_bool>` = false, exact_match\: :ref:`bool<class_bool>` = false\ ) |const| |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_action_released<class_InputEvent_method_is_action_released>`\ (\ action\: :ref:`StringName<class_StringName>`, exact_match\: :ref:`bool<class_bool>` = false\ ) |const|                                             |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_action_type<class_InputEvent_method_is_action_type>`\ (\ ) |const|                                                                                                                                                  |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_canceled<class_InputEvent_method_is_canceled>`\ (\ ) |const|                                                                                                                                                        |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_echo<class_InputEvent_method_is_echo>`\ (\ ) |const|                                                                                                                                                                |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_match<class_InputEvent_method_is_match>`\ (\ event\: :ref:`InputEvent<class_InputEvent>`, exact_match\: :ref:`bool<class_bool>` = true\ ) |const|                                                                   |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_pressed<class_InputEvent_method_is_pressed>`\ (\ ) |const|                                                                                                                                                          |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_released<class_InputEvent_method_is_released>`\ (\ ) |const|                                                                                                                                                        |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`InputEvent<class_InputEvent>` | :ref:`xformed_by<class_InputEvent_method_xformed_by>`\ (\ xform\: :ref:`Transform2D<class_Transform2D>`, local_ofs\: :ref:`Vector2<class_Vector2>` = Vector2(0, 0)\ ) |const|                                                |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Constants



**DEVICE_ID_EMULATION** = `-1` [🔗<class_InputEvent_constant_DEVICE_ID_EMULATION>]

Device ID used for emulated mouse input from a touchscreen, or for emulated touch input from a mouse. This can be used to distinguish emulated mouse input from physical mouse input, or emulated touch input from physical touch input.


----


## Property Descriptions



[int<class_int>] **device** = `0` [🔗<class_InputEvent_property_device>]


- |void| **set_device**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_device**\ (\ )

The event's device ID.

\ **Note:** [device<class_InputEvent_property_device>] can be negative for special use cases that don't refer to devices physically present on the system. See [DEVICE_ID_EMULATION<class_InputEvent_constant_DEVICE_ID_EMULATION>].


----


## Method Descriptions



[bool<class_bool>] **accumulate**\ (\ with_event\: [InputEvent<class_InputEvent>]\ ) [🔗<class_InputEvent_method_accumulate>]

Returns `true` if the given input event and this input event can be added together (only for events of type [InputEventMouseMotion<class_InputEventMouseMotion>]).

The given input event's position, global position and speed will be copied. The resulting `relative` is a sum of both events. Both events' modifiers have to be identical.


----



[String<class_String>] **as_text**\ (\ ) |const| [🔗<class_InputEvent_method_as_text>]

Returns a [String<class_String>] representation of the event.


----



[float<class_float>] **get_action_strength**\ (\ action\: [StringName<class_StringName>], exact_match\: [bool<class_bool>] = false\ ) |const| [🔗<class_InputEvent_method_get_action_strength>]

Returns a value between 0.0 and 1.0 depending on the given actions' state. Useful for getting the value of events of type [InputEventJoypadMotion<class_InputEventJoypadMotion>].

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey<class_InputEventKey>] and [InputEventMouseButton<class_InputEventMouseButton>] events, and the direction for [InputEventJoypadMotion<class_InputEventJoypadMotion>] events.


----



[bool<class_bool>] **is_action**\ (\ action\: [StringName<class_StringName>], exact_match\: [bool<class_bool>] = false\ ) |const| [🔗<class_InputEvent_method_is_action>]

Returns `true` if this input event matches a pre-defined action of any type.

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey<class_InputEventKey>] and [InputEventMouseButton<class_InputEventMouseButton>] events, and the direction for [InputEventJoypadMotion<class_InputEventJoypadMotion>] events.


----



[bool<class_bool>] **is_action_pressed**\ (\ action\: [StringName<class_StringName>], allow_echo\: [bool<class_bool>] = false, exact_match\: [bool<class_bool>] = false\ ) |const| [🔗<class_InputEvent_method_is_action_pressed>]

Returns `true` if the given action matches this event and is being pressed (and is not an echo event for [InputEventKey<class_InputEventKey>] events, unless `allow_echo` is `true`). Not relevant for events of type [InputEventMouseMotion<class_InputEventMouseMotion>] or [InputEventScreenDrag<class_InputEventScreenDrag>].

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey<class_InputEventKey>] and [InputEventMouseButton<class_InputEventMouseButton>] events, and the direction for [InputEventJoypadMotion<class_InputEventJoypadMotion>] events.

\ **Note:** Due to keyboard ghosting, [is_action_pressed()<class_InputEvent_method_is_action_pressed>] may return `false` even if one of the action's keys is pressed. See [Input examples ](../tutorials/inputs/input_examples.html#keyboard-events)_ in the documentation for more information.


----



[bool<class_bool>] **is_action_released**\ (\ action\: [StringName<class_StringName>], exact_match\: [bool<class_bool>] = false\ ) |const| [🔗<class_InputEvent_method_is_action_released>]

Returns `true` if the given action matches this event and is released (i.e. not pressed). Not relevant for events of type [InputEventMouseMotion<class_InputEventMouseMotion>] or [InputEventScreenDrag<class_InputEventScreenDrag>].

If `exact_match` is `false`, it ignores additional input modifiers for [InputEventKey<class_InputEventKey>] and [InputEventMouseButton<class_InputEventMouseButton>] events, and the direction for [InputEventJoypadMotion<class_InputEventJoypadMotion>] events.


----



[bool<class_bool>] **is_action_type**\ (\ ) |const| [🔗<class_InputEvent_method_is_action_type>]

Returns `true` if this input event's type is one that can be assigned to an input action: [InputEventKey<class_InputEventKey>], [InputEventMouseButton<class_InputEventMouseButton>], [InputEventJoypadButton<class_InputEventJoypadButton>], [InputEventJoypadMotion<class_InputEventJoypadMotion>], [InputEventAction<class_InputEventAction>]. Returns `false` for all other input event types.


----



[bool<class_bool>] **is_canceled**\ (\ ) |const| [🔗<class_InputEvent_method_is_canceled>]

Returns `true` if this input event has been canceled.


----



[bool<class_bool>] **is_echo**\ (\ ) |const| [🔗<class_InputEvent_method_is_echo>]

Returns `true` if this input event is an echo event (only for events of type [InputEventKey<class_InputEventKey>]). An echo event is a repeated key event sent when the user is holding down the key. Any other event type returns `false`.

\ **Note:** The rate at which echo events are sent is typically around 20 events per second (after holding down the key for roughly half a second). However, the key repeat delay/speed can be changed by the user or disabled entirely in the operating system settings. To ensure your project works correctly on all configurations, do not assume the user has a specific key repeat configuration in your project's behavior.


----



[bool<class_bool>] **is_match**\ (\ event\: [InputEvent<class_InputEvent>], exact_match\: [bool<class_bool>] = true\ ) |const| [🔗<class_InputEvent_method_is_match>]

Returns `true` if the specified `event` matches this event. Only valid for action events, which include key ([InputEventKey<class_InputEventKey>]), button ([InputEventMouseButton<class_InputEventMouseButton>] or [InputEventJoypadButton<class_InputEventJoypadButton>]), axis [InputEventJoypadMotion<class_InputEventJoypadMotion>], and action ([InputEventAction<class_InputEventAction>]) events.

If `exact_match` is `false`, the check ignores additional input modifiers for [InputEventKey<class_InputEventKey>] and [InputEventMouseButton<class_InputEventMouseButton>] events, and the direction for [InputEventJoypadMotion<class_InputEventJoypadMotion>] events.

\ **Note:** This method only considers the event configuration (such as the keyboard key or the joypad axis), not state information like [is_pressed()<class_InputEvent_method_is_pressed>], [is_released()<class_InputEvent_method_is_released>], [is_echo()<class_InputEvent_method_is_echo>], or [is_canceled()<class_InputEvent_method_is_canceled>].


----



[bool<class_bool>] **is_pressed**\ (\ ) |const| [🔗<class_InputEvent_method_is_pressed>]

Returns `true` if this input event is pressed. Not relevant for events of type [InputEventMouseMotion<class_InputEventMouseMotion>] or [InputEventScreenDrag<class_InputEventScreenDrag>].

\ **Note:** Due to keyboard ghosting, [is_pressed()<class_InputEvent_method_is_pressed>] may return `false` even if one of the action's keys is pressed. See [Input examples ](../tutorials/inputs/input_examples.html#keyboard-events)_ in the documentation for more information.


----



[bool<class_bool>] **is_released**\ (\ ) |const| [🔗<class_InputEvent_method_is_released>]

Returns `true` if this input event is released. Not relevant for events of type [InputEventMouseMotion<class_InputEventMouseMotion>] or [InputEventScreenDrag<class_InputEventScreenDrag>].


----



[InputEvent<class_InputEvent>] **xformed_by**\ (\ xform\: [Transform2D<class_Transform2D>], local_ofs\: [Vector2<class_Vector2>] = Vector2(0, 0)\ ) |const| [🔗<class_InputEvent_method_xformed_by>]

Returns a copy of the given input event which has been offset by `local_ofs` and transformed by `xform`. Relevant for events of type [InputEventMouseButton<class_InputEventMouseButton>], [InputEventMouseMotion<class_InputEventMouseMotion>], [InputEventScreenTouch<class_InputEventScreenTouch>], [InputEventScreenDrag<class_InputEventScreenDrag>], [InputEventMagnifyGesture<class_InputEventMagnifyGesture>] and [InputEventPanGesture<class_InputEventPanGesture>].

