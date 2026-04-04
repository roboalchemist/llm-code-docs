:github_url: hide



# XRController3D

**Inherits:** [XRNode3D<class_XRNode3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A 3D node representing a spatially-tracked controller.


## Description

This is a helper 3D node that is linked to the tracking of controllers. It also offers several handy passthroughs to the state of buttons and such on the controllers.

Controllers are linked by their ID. You can create controller nodes before the controllers are available. If your game always uses two controllers (one for each hand), you can predefine the controllers with ID 1 and 2; they will become active as soon as the controllers are identified. If you expect additional controllers to be used, you should react to the signals and add XRController3D nodes to your scene.

The position of the controller node is automatically updated by the [XRServer<class_XRServer>]. This makes this node ideal to add child nodes to visualize the controller.

The current [XRInterface<class_XRInterface>] defines the names of inputs. In the case of OpenXR, these are the names of actions in the current action set from the OpenXR action map.


## Tutorials

- [../tutorials/xr/index](XR documentation index .md)


## Methods

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                | :ref:`get_float<class_XRController3D_method_get_float>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                 |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                            | :ref:`get_input<class_XRController3D_method_get_input>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                 |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TrackerHand<enum_XRPositionalTracker_TrackerHand>` | :ref:`get_tracker_hand<class_XRController3D_method_get_tracker_hand>`\ (\ ) |const|                                               |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                            | :ref:`get_vector2<class_XRController3D_method_get_vector2>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|             |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                  | :ref:`is_button_pressed<class_XRController3D_method_is_button_pressed>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const| |
> +----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**button_pressed**\ (\ name\: [String<class_String>]\ ) [🔗<class_XRController3D_signal_button_pressed>]

Emitted when a button on this controller is pressed.


----



**button_released**\ (\ name\: [String<class_String>]\ ) [🔗<class_XRController3D_signal_button_released>]

Emitted when a button on this controller is released.


----



**input_float_changed**\ (\ name\: [String<class_String>], value\: [float<class_float>]\ ) [🔗<class_XRController3D_signal_input_float_changed>]

Emitted when a trigger or similar input on this controller changes value.


----



**input_vector2_changed**\ (\ name\: [String<class_String>], value\: [Vector2<class_Vector2>]\ ) [🔗<class_XRController3D_signal_input_vector2_changed>]

Emitted when a thumbstick or thumbpad on this controller is moved.


----



**profile_changed**\ (\ role\: [String<class_String>]\ ) [🔗<class_XRController3D_signal_profile_changed>]

Emitted when the interaction profile on this controller is changed.


----


## Method Descriptions



[float<class_float>] **get_float**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_XRController3D_method_get_float>]

Returns a numeric value for the input with the given `name`. This is used for triggers and grip sensors.

\ **Note:** The current [XRInterface<class_XRInterface>] defines the `name` for each input. In the case of OpenXR, these are the names of actions in the current action set.


----



[Variant<class_Variant>] **get_input**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_XRController3D_method_get_input>]

Returns a [Variant<class_Variant>] for the input with the given `name`. This works for any input type, the variant will be typed according to the actions configuration.

\ **Note:** The current [XRInterface<class_XRInterface>] defines the `name` for each input. In the case of OpenXR, these are the names of actions in the current action set.


----



[TrackerHand<enum_XRPositionalTracker_TrackerHand>] **get_tracker_hand**\ (\ ) |const| [🔗<class_XRController3D_method_get_tracker_hand>]

Returns the hand holding this controller, if known.


----



[Vector2<class_Vector2>] **get_vector2**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_XRController3D_method_get_vector2>]

Returns a [Vector2<class_Vector2>] for the input with the given `name`. This is used for thumbsticks and thumbpads found on many controllers.

\ **Note:** The current [XRInterface<class_XRInterface>] defines the `name` for each input. In the case of OpenXR, these are the names of actions in the current action set.


----



[bool<class_bool>] **is_button_pressed**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_XRController3D_method_is_button_pressed>]

Returns `true` if the button with the given `name` is pressed.

\ **Note:** The current [XRInterface<class_XRInterface>] defines the `name` for each input. In the case of OpenXR, these are the names of actions in the current action set.

