:github_url: hide

> **META**
	:keywords: gamepad, controller



# InputEventJoypadButton

**Inherits:** [InputEvent<class_InputEvent>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a gamepad button being pressed or released.


## Description

Input event type for gamepad buttons. For gamepad analog sticks and joysticks, see [InputEventJoypadMotion<class_InputEventJoypadMotion>].


## Tutorials

- [../tutorials/inputs/inputevent](Using InputEvent .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`JoyButton<enum_@GlobalScope_JoyButton>` | :ref:`button_index<class_InputEventJoypadButton_property_button_index>` | ``0``     |
> +-----------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                       | :ref:`pressed<class_InputEventJoypadButton_property_pressed>`           | ``false`` |
> +-----------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                     | :ref:`pressure<class_InputEventJoypadButton_property_pressure>`         | ``0.0``   |
> +-----------------------------------------------+-------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[JoyButton<enum_@GlobalScope_JoyButton>] **button_index** = `0` [🔗<class_InputEventJoypadButton_property_button_index>]


- |void| **set_button_index**\ (\ value\: [JoyButton<enum_@GlobalScope_JoyButton>]\ )
- [JoyButton<enum_@GlobalScope_JoyButton>] **get_button_index**\ (\ )

Button identifier. One of the [JoyButton<enum_@GlobalScope_JoyButton>] button constants.


----



[bool<class_bool>] **pressed** = `false` [🔗<class_InputEventJoypadButton_property_pressed>]


- |void| **set_pressed**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_pressed**\ (\ )

If `true`, the button's state is pressed. If `false`, the button's state is released.


----



[float<class_float>] **pressure** = `0.0` [🔗<class_InputEventJoypadButton_property_pressure>]


- |void| **set_pressure**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_pressure**\ (\ )

**Deprecated:** This property is never set by the engine and is always `0`.

