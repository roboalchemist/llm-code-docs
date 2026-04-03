:github_url: hide



# InputEventScreenTouch

**Inherits:** [InputEventFromWindow<class_InputEventFromWindow>] **<** [InputEvent<class_InputEvent>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a screen touch event.


## Description

Stores information about multi-touch press/release input events. Supports touch press, touch release and [index<class_InputEventScreenTouch_property_index>] for multi-touch count and order.


## Tutorials

- [../tutorials/inputs/inputevent](Using InputEvent .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+--------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`       | :ref:`canceled<class_InputEventScreenTouch_property_canceled>`     | ``false``         |
> +-------------------------------+--------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`       | :ref:`double_tap<class_InputEventScreenTouch_property_double_tap>` | ``false``         |
> +-------------------------------+--------------------------------------------------------------------+-------------------+
> | :ref:`int<class_int>`         | :ref:`index<class_InputEventScreenTouch_property_index>`           | ``0``             |
> +-------------------------------+--------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`position<class_InputEventScreenTouch_property_position>`     | ``Vector2(0, 0)`` |
> +-------------------------------+--------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`       | :ref:`pressed<class_InputEventScreenTouch_property_pressed>`       | ``false``         |
> +-------------------------------+--------------------------------------------------------------------+-------------------+
>

----


## Property Descriptions



[bool<class_bool>] **canceled** = `false` [🔗<class_InputEventScreenTouch_property_canceled>]


- |void| **set_canceled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_canceled**\ (\ )

If `true`, the touch event has been canceled.


----



[bool<class_bool>] **double_tap** = `false` [🔗<class_InputEventScreenTouch_property_double_tap>]


- |void| **set_double_tap**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_double_tap**\ (\ )

If `true`, the touch's state is a double tap.


----



[int<class_int>] **index** = `0` [🔗<class_InputEventScreenTouch_property_index>]


- |void| **set_index**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_index**\ (\ )

The touch index in the case of a multi-touch event. One index = one finger.


----



[Vector2<class_Vector2>] **position** = `Vector2(0, 0)` [🔗<class_InputEventScreenTouch_property_position>]


- |void| **set_position**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_position**\ (\ )

The touch position in the viewport the node is in, using the coordinate system of this viewport.


----



[bool<class_bool>] **pressed** = `false` [🔗<class_InputEventScreenTouch_property_pressed>]


- |void| **set_pressed**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_pressed**\ (\ )

If `true`, the touch's state is pressed. If `false`, the touch's state is released.

