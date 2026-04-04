:github_url: hide



# InputEventMouse

**Inherits:** [InputEventWithModifiers<class_InputEventWithModifiers>] **<** [InputEventFromWindow<class_InputEventFromWindow>] **<** [InputEvent<class_InputEvent>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [InputEventMouseButton<class_InputEventMouseButton>], [InputEventMouseMotion<class_InputEventMouseMotion>]

Base input event type for mouse events.


## Description

Stores general information about mouse events.


## Tutorials

- [../tutorials/inputs/inputevent](Using InputEvent .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------------+------------------------------------------------------------------------+-------------------+
> | |bitfield|\[:ref:`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>`\] | :ref:`button_mask<class_InputEventMouse_property_button_mask>`         | ``0``             |
> +-------------------------------------------------------------------------+------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>`                                           | :ref:`global_position<class_InputEventMouse_property_global_position>` | ``Vector2(0, 0)`` |
> +-------------------------------------------------------------------------+------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>`                                           | :ref:`position<class_InputEventMouse_property_position>`               | ``Vector2(0, 0)`` |
> +-------------------------------------------------------------------------+------------------------------------------------------------------------+-------------------+
>

----


## Property Descriptions



|bitfield|\[[MouseButtonMask<enum_@GlobalScope_MouseButtonMask>]\] **button_mask** = `0` [🔗<class_InputEventMouse_property_button_mask>]


- |void| **set_button_mask**\ (\ value\: |bitfield|\[[MouseButtonMask<enum_@GlobalScope_MouseButtonMask>]\]\ )
- |bitfield|\[[MouseButtonMask<enum_@GlobalScope_MouseButtonMask>]\] **get_button_mask**\ (\ )

The mouse button mask identifier, one of or a bitwise combination of the [MouseButton<enum_@GlobalScope_MouseButton>] button masks.


----



[Vector2<class_Vector2>] **global_position** = `Vector2(0, 0)` [🔗<class_InputEventMouse_property_global_position>]


- |void| **set_global_position**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_global_position**\ (\ )

When received in [Node._input()<class_Node_private_method__input>] or [Node._unhandled_input()<class_Node_private_method__unhandled_input>], returns the mouse's position in the root [Viewport<class_Viewport>] using the coordinate system of the root [Viewport<class_Viewport>].

When received in [Control._gui_input()<class_Control_private_method__gui_input>], returns the mouse's position in the [CanvasLayer<class_CanvasLayer>] that the [Control<class_Control>] is in using the coordinate system of the [CanvasLayer<class_CanvasLayer>].


----



[Vector2<class_Vector2>] **position** = `Vector2(0, 0)` [🔗<class_InputEventMouse_property_position>]


- |void| **set_position**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_position**\ (\ )

When received in [Node._input()<class_Node_private_method__input>] or [Node._unhandled_input()<class_Node_private_method__unhandled_input>], returns the mouse's position in the [Viewport<class_Viewport>] this [Node<class_Node>] is in using the coordinate system of this [Viewport<class_Viewport>].

When received in [Control._gui_input()<class_Control_private_method__gui_input>], returns the mouse's position in the [Control<class_Control>] using the local coordinate system of the [Control<class_Control>].

