:github_url: hide



# InputEventMouseMotion

**Inherits:** [InputEventMouse<class_InputEventMouse>] **<** [InputEventWithModifiers<class_InputEventWithModifiers>] **<** [InputEventFromWindow<class_InputEventFromWindow>] **<** [InputEvent<class_InputEvent>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a mouse or a pen movement.


## Description

Stores information about a mouse or a pen motion. This includes relative position, absolute position, and velocity. See [Node._input()<class_Node_private_method__input>].

\ **Note:** By default, this event is only emitted once per frame rendered at most. If you need more precise input reporting, set [Input.use_accumulated_input<class_Input_property_use_accumulated_input>] to `false` to make events emitted as often as possible. If you use InputEventMouseMotion to draw lines, consider using [Geometry2D.bresenham_line()<class_Geometry2D_method_bresenham_line>] as well to avoid visible gaps in lines if the user is moving the mouse quickly.

\ **Note:** This event may be emitted even when the mouse hasn't moved, either by the operating system or by Godot itself. If you really need to know if the mouse has moved (e.g. to suppress displaying a tooltip), you should check that `relative.is_zero_approx()` is `false`.


## Tutorials

- [../tutorials/inputs/inputevent](Using InputEvent .md)

- [../tutorials/inputs/mouse_and_input_coordinates](Mouse and input coordinates .md)

- [3D Voxel Demo ](https://godotengine.org/asset-library/asset/2755)_


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+------------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`       | :ref:`pen_inverted<class_InputEventMouseMotion_property_pen_inverted>`       | ``false``         |
> +-------------------------------+------------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`     | :ref:`pressure<class_InputEventMouseMotion_property_pressure>`               | ``0.0``           |
> +-------------------------------+------------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`relative<class_InputEventMouseMotion_property_relative>`               | ``Vector2(0, 0)`` |
> +-------------------------------+------------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`screen_relative<class_InputEventMouseMotion_property_screen_relative>` | ``Vector2(0, 0)`` |
> +-------------------------------+------------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`screen_velocity<class_InputEventMouseMotion_property_screen_velocity>` | ``Vector2(0, 0)`` |
> +-------------------------------+------------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`tilt<class_InputEventMouseMotion_property_tilt>`                       | ``Vector2(0, 0)`` |
> +-------------------------------+------------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`velocity<class_InputEventMouseMotion_property_velocity>`               | ``Vector2(0, 0)`` |
> +-------------------------------+------------------------------------------------------------------------------+-------------------+
>

----


## Property Descriptions



[bool<class_bool>] **pen_inverted** = `false` [🔗<class_InputEventMouseMotion_property_pen_inverted>]


- |void| **set_pen_inverted**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_pen_inverted**\ (\ )

Returns `true` when using the eraser end of a stylus pen.

\ **Note:** This property is implemented on Linux, macOS and Windows.


----



[float<class_float>] **pressure** = `0.0` [🔗<class_InputEventMouseMotion_property_pressure>]


- |void| **set_pressure**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_pressure**\ (\ )

Represents the pressure the user puts on the pen. Ranges from `0.0` to `1.0`.


----



[Vector2<class_Vector2>] **relative** = `Vector2(0, 0)` [🔗<class_InputEventMouseMotion_property_relative>]


- |void| **set_relative**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_relative**\ (\ )

The mouse position relative to the previous position (position at the last frame).

\ **Note:** Since **InputEventMouseMotion** may only be emitted when the mouse moves, it is not possible to reliably detect when the mouse has stopped moving by checking this property. A separate, short timer may be necessary.

\ **Note:** [relative<class_InputEventMouseMotion_property_relative>] is automatically scaled according to the content scale factor, which is defined by the project's stretch mode settings. This means mouse sensitivity will appear different depending on resolution when using [relative<class_InputEventMouseMotion_property_relative>] in a script that handles mouse aiming with the [Input.MOUSE_MODE_CAPTURED<class_Input_constant_MOUSE_MODE_CAPTURED>] mouse mode. To avoid this, use [screen_relative<class_InputEventMouseMotion_property_screen_relative>] instead.


----



[Vector2<class_Vector2>] **screen_relative** = `Vector2(0, 0)` [🔗<class_InputEventMouseMotion_property_screen_relative>]


- |void| **set_screen_relative**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_screen_relative**\ (\ )

The unscaled mouse position relative to the previous position in the coordinate system of the screen (position at the last frame).

\ **Note:** Since **InputEventMouseMotion** may only be emitted when the mouse moves, it is not possible to reliably detect when the mouse has stopped moving by checking this property. A separate, short timer may be necessary.

\ **Note:** This coordinate is *not* scaled according to the content scale factor or calls to [InputEvent.xformed_by()<class_InputEvent_method_xformed_by>]. This should be preferred over [relative<class_InputEventMouseMotion_property_relative>] for mouse aiming when using the [Input.MOUSE_MODE_CAPTURED<class_Input_constant_MOUSE_MODE_CAPTURED>] mouse mode, regardless of the project's stretch mode.


----



[Vector2<class_Vector2>] **screen_velocity** = `Vector2(0, 0)` [🔗<class_InputEventMouseMotion_property_screen_velocity>]


- |void| **set_screen_velocity**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_screen_velocity**\ (\ )

The unscaled mouse velocity in pixels per second in screen coordinates. This velocity is *not* scaled according to the content scale factor or calls to [InputEvent.xformed_by()<class_InputEvent_method_xformed_by>].

\ **Note:** Use [screen_relative<class_InputEventMouseMotion_property_screen_relative>] for mouse aiming using the [Input.MOUSE_MODE_CAPTURED<class_Input_constant_MOUSE_MODE_CAPTURED>] mouse mode.


----



[Vector2<class_Vector2>] **tilt** = `Vector2(0, 0)` [🔗<class_InputEventMouseMotion_property_tilt>]


- |void| **set_tilt**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_tilt**\ (\ )

Represents the angles of tilt of the pen. Positive X-coordinate value indicates a tilt to the right. Positive Y-coordinate value indicates a tilt toward the user. Ranges from `-1.0` to `1.0` for both axes.


----



[Vector2<class_Vector2>] **velocity** = `Vector2(0, 0)` [🔗<class_InputEventMouseMotion_property_velocity>]


- |void| **set_velocity**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_velocity**\ (\ )

The mouse velocity in pixels per second.

\ **Note:** [velocity<class_InputEventMouseMotion_property_velocity>] is automatically scaled according to the content scale factor, which is defined by the project's stretch mode settings. That means mouse sensitivity may appear different depending on resolution.

\ **Note:** Use [screen_relative<class_InputEventMouseMotion_property_screen_relative>] for mouse aiming using the [Input.MOUSE_MODE_CAPTURED<class_Input_constant_MOUSE_MODE_CAPTURED>] mouse mode.

