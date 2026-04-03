:github_url: hide

> **META**
	:keywords: radio



# ButtonGroup

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A group of buttons that doesn't allow more than one button to be pressed at a time.


## Description

A group of [BaseButton<class_BaseButton>]-derived buttons. The buttons in a **ButtonGroup** are treated like radio buttons: No more than one button can be pressed at a time. Some types of buttons (such as [CheckBox<class_CheckBox>]) may have a special appearance in this state.

Every member of a **ButtonGroup** should have [BaseButton.toggle_mode<class_BaseButton_property_toggle_mode>] set to `true`.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`allow_unpress<class_ButtonGroup_property_allow_unpress>` | ``false``                                                                             |
> +-------------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | resource_local_to_scene                                        | ``true`` (overrides :ref:`Resource<class_Resource_property_resource_local_to_scene>`) |
> +-------------------------+----------------------------------------------------------------+---------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`BaseButton<class_BaseButton>`\] | :ref:`get_buttons<class_ButtonGroup_method_get_buttons>`\ (\ )               |
> +------------------------------------------------------------------+------------------------------------------------------------------------------+
> | :ref:`BaseButton<class_BaseButton>`                              | :ref:`get_pressed_button<class_ButtonGroup_method_get_pressed_button>`\ (\ ) |
> +------------------------------------------------------------------+------------------------------------------------------------------------------+
>

----


## Signals



**pressed**\ (\ button\: [BaseButton<class_BaseButton>]\ ) [🔗<class_ButtonGroup_signal_pressed>]

Emitted when one of the buttons of the group is pressed.


----


## Property Descriptions



[bool<class_bool>] **allow_unpress** = `false` [🔗<class_ButtonGroup_property_allow_unpress>]


- |void| **set_allow_unpress**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_allow_unpress**\ (\ )

If `true`, it is possible to unpress all buttons in this **ButtonGroup**.


----


## Method Descriptions



[Array<class_Array>]\[[BaseButton<class_BaseButton>]\] **get_buttons**\ (\ ) [🔗<class_ButtonGroup_method_get_buttons>]

Returns an [Array<class_Array>] of [Button<class_Button>]\ s who have this as their **ButtonGroup** (see [BaseButton.button_group<class_BaseButton_property_button_group>]).


----



[BaseButton<class_BaseButton>] **get_pressed_button**\ (\ ) [🔗<class_ButtonGroup_method_get_pressed_button>]

Returns the current pressed button.

