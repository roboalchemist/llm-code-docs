:github_url: hide



# InputEventAction

**Inherits:** [InputEvent<class_InputEvent>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

An input event type for actions.


## Description

Contains a generic action which can be targeted from several types of inputs. Actions and their events can be set in the **Input Map** tab in **Project > Project Settings**, or with the [InputMap<class_InputMap>] class.

\ **Note:** Unlike the other [InputEvent<class_InputEvent>] subclasses which map to unique physical events, this virtual one is not emitted by the engine. This class is useful to emit actions manually with [Input.parse_input_event()<class_Input_method_parse_input_event>], which are then received in [Node._input()<class_Node_private_method__input>]. To check if a physical event matches an action from the Input Map, use [InputEvent.is_action()<class_InputEvent_method_is_action>] and [InputEvent.is_action_pressed()<class_InputEvent_method_is_action_pressed>].


## Tutorials

- [Using InputEvent: Actions ](../tutorials/inputs/inputevent.html#actions)_

- [2D Dodge The Creeps Demo ](https://godotengine.org/asset-library/asset/2712)_

- [3D Voxel Demo ](https://godotengine.org/asset-library/asset/2755)_


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------+-----------------------------------------------------------------+-----------+
> | :ref:`StringName<class_StringName>` | :ref:`action<class_InputEventAction_property_action>`           | ``&""``   |
> +-------------------------------------+-----------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`               | :ref:`event_index<class_InputEventAction_property_event_index>` | ``-1``    |
> +-------------------------------------+-----------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`             | :ref:`pressed<class_InputEventAction_property_pressed>`         | ``false`` |
> +-------------------------------------+-----------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`           | :ref:`strength<class_InputEventAction_property_strength>`       | ``1.0``   |
> +-------------------------------------+-----------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[StringName<class_StringName>] **action** = `&""` [🔗<class_InputEventAction_property_action>]


- |void| **set_action**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_action**\ (\ )

The action's name. This is usually the name of an existing action in the [InputMap<class_InputMap>] which you want this custom event to match.


----



[int<class_int>] **event_index** = `-1` [🔗<class_InputEventAction_property_event_index>]


- |void| **set_event_index**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_event_index**\ (\ )

The real event index in action this event corresponds to (from events defined for this action in the [InputMap<class_InputMap>]). If `-1`, a unique ID will be used and actions pressed with this ID will need to be released with another **InputEventAction**.


----



[bool<class_bool>] **pressed** = `false` [🔗<class_InputEventAction_property_pressed>]


- |void| **set_pressed**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_pressed**\ (\ )

If `true`, the action's state is pressed. If `false`, the action's state is released.


----



[float<class_float>] **strength** = `1.0` [🔗<class_InputEventAction_property_strength>]


- |void| **set_strength**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_strength**\ (\ )

The action's strength between 0 and 1. This value is considered as equal to 0 if pressed is `false`. The event strength allows faking analog joypad motion events, by specifying how strongly the joypad axis is bent or pressed.

