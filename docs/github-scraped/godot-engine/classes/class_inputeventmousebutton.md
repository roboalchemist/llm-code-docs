:github_url: hide

> **META**
	:keywords: click, press



# InputEventMouseButton

**Inherits:** [InputEventMouse<class_InputEventMouse>] **<** [InputEventWithModifiers<class_InputEventWithModifiers>] **<** [InputEventFromWindow<class_InputEventFromWindow>] **<** [InputEvent<class_InputEvent>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a mouse button being pressed or released.


## Description

Stores information about mouse click events. See [Node._input()<class_Node_private_method__input>].

\ **Note:** On Wear OS devices, rotary input is mapped to [@GlobalScope.MOUSE_BUTTON_WHEEL_UP<class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_UP>] and [@GlobalScope.MOUSE_BUTTON_WHEEL_DOWN<class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_DOWN>]. This can be changed to [@GlobalScope.MOUSE_BUTTON_WHEEL_LEFT<class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_LEFT>] and [@GlobalScope.MOUSE_BUTTON_WHEEL_RIGHT<class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_RIGHT>] with the [ProjectSettings.input_devices/pointing/android/rotary_input_scroll_axis<class_ProjectSettings_property_input_devices/pointing/android/rotary_input_scroll_axis>] setting.


## Tutorials

- [../tutorials/inputs/inputevent](Using InputEvent .md)

- [../tutorials/inputs/mouse_and_input_coordinates](Mouse and input coordinates .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+------------------------------------------------------------------------+-----------+
> | :ref:`MouseButton<enum_@GlobalScope_MouseButton>` | :ref:`button_index<class_InputEventMouseButton_property_button_index>` | ``0``     |
> +---------------------------------------------------+------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`canceled<class_InputEventMouseButton_property_canceled>`         | ``false`` |
> +---------------------------------------------------+------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`double_click<class_InputEventMouseButton_property_double_click>` | ``false`` |
> +---------------------------------------------------+------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                         | :ref:`factor<class_InputEventMouseButton_property_factor>`             | ``1.0``   |
> +---------------------------------------------------+------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`pressed<class_InputEventMouseButton_property_pressed>`           | ``false`` |
> +---------------------------------------------------+------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[MouseButton<enum_@GlobalScope_MouseButton>] **button_index** = `0` [🔗<class_InputEventMouseButton_property_button_index>]


- |void| **set_button_index**\ (\ value\: [MouseButton<enum_@GlobalScope_MouseButton>]\ )
- [MouseButton<enum_@GlobalScope_MouseButton>] **get_button_index**\ (\ )

The mouse button identifier, one of the [MouseButton<enum_@GlobalScope_MouseButton>] button or button wheel constants.


----



[bool<class_bool>] **canceled** = `false` [🔗<class_InputEventMouseButton_property_canceled>]


- |void| **set_canceled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_canceled**\ (\ )

If `true`, the mouse button event has been canceled.


----



[bool<class_bool>] **double_click** = `false` [🔗<class_InputEventMouseButton_property_double_click>]


- |void| **set_double_click**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_double_click**\ (\ )

If `true`, the mouse button's state is a double-click.


----



[float<class_float>] **factor** = `1.0` [🔗<class_InputEventMouseButton_property_factor>]


- |void| **set_factor**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_factor**\ (\ )

The amount (or delta) of the event. When used for high-precision scroll events, this indicates the scroll amount (vertical or horizontal). This is only supported on some platforms; the reported sensitivity varies depending on the platform. May be `0` if not supported.


----



[bool<class_bool>] **pressed** = `false` [🔗<class_InputEventMouseButton_property_pressed>]


- |void| **set_pressed**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_pressed**\ (\ )

If `true`, the mouse button's state is pressed. If `false`, the mouse button's state is released.

