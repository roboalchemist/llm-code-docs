:github_url: hide

> **META**
	:keywords: gamepad, controller



# InputEventJoypadMotion

**Inherits:** [InputEvent<class_InputEvent>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents axis motions (such as joystick or analog triggers) from a gamepad.


## Description

Stores information about joystick motions. One **InputEventJoypadMotion** represents one axis at a time. For gamepad buttons, see [InputEventJoypadButton<class_InputEventJoypadButton>].


## Tutorials

- [../tutorials/inputs/inputevent](Using InputEvent .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------+---------------------------------------------------------------------+---------+
> | :ref:`JoyAxis<enum_@GlobalScope_JoyAxis>` | :ref:`axis<class_InputEventJoypadMotion_property_axis>`             | ``0``   |
> +-------------------------------------------+---------------------------------------------------------------------+---------+
> | :ref:`float<class_float>`                 | :ref:`axis_value<class_InputEventJoypadMotion_property_axis_value>` | ``0.0`` |
> +-------------------------------------------+---------------------------------------------------------------------+---------+
>

----


## Property Descriptions



[JoyAxis<enum_@GlobalScope_JoyAxis>] **axis** = `0` [🔗<class_InputEventJoypadMotion_property_axis>]


- |void| **set_axis**\ (\ value\: [JoyAxis<enum_@GlobalScope_JoyAxis>]\ )
- [JoyAxis<enum_@GlobalScope_JoyAxis>] **get_axis**\ (\ )

Axis identifier.


----



[float<class_float>] **axis_value** = `0.0` [🔗<class_InputEventJoypadMotion_property_axis_value>]


- |void| **set_axis_value**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_axis_value**\ (\ )

Current position of the joystick on the given axis. The value ranges from `-1.0` to `1.0`. A value of `0` means the axis is in its resting position.

