:github_url: hide

> **META**
	:keywords: dropdown



# MenuButton

**Inherits:** [Button<class_Button>] **<** [BaseButton<class_BaseButton>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A button that brings up a [PopupMenu<class_PopupMenu>] when clicked.


## Description

A button that brings up a [PopupMenu<class_PopupMenu>] when clicked. To create new items inside this [PopupMenu<class_PopupMenu>], use `get_popup().add_item("My Item Name")`. You can also create them directly from Godot editor's inspector.

See also [BaseButton<class_BaseButton>] which contains common properties and methods associated with this node.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`ActionMode<enum_BaseButton_ActionMode>` | action_mode                                                       | ``0`` (overrides :ref:`BaseButton<class_BaseButton_property_action_mode>`)    |
> +-----------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                       | flat                                                              | ``true`` (overrides :ref:`Button<class_Button_property_flat>`)                |
> +-----------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`FocusMode<enum_Control_FocusMode>`      | focus_mode                                                        | ``3`` (overrides :ref:`Control<class_Control_property_focus_mode>`)           |
> +-----------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                         | :ref:`item_count<class_MenuButton_property_item_count>`           | ``0``                                                                         |
> +-----------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                       | :ref:`switch_on_hover<class_MenuButton_property_switch_on_hover>` | ``false``                                                                     |
> +-----------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                       | toggle_mode                                                       | ``true`` (overrides :ref:`BaseButton<class_BaseButton_property_toggle_mode>`) |
> +-----------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | :ref:`PopupMenu<class_PopupMenu>` | :ref:`get_popup<class_MenuButton_method_get_popup>`\ (\ ) |const|                                                     |
> +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`set_disable_shortcuts<class_MenuButton_method_set_disable_shortcuts>`\ (\ disabled\: :ref:`bool<class_bool>`\ ) |
> +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`show_popup<class_MenuButton_method_show_popup>`\ (\ )                                                           |
> +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**about_to_popup**\ (\ ) [🔗<class_MenuButton_signal_about_to_popup>]

Emitted when the [PopupMenu<class_PopupMenu>] of this MenuButton is about to show.


----


## Property Descriptions



[int<class_int>] **item_count** = `0` [🔗<class_MenuButton_property_item_count>]


- |void| **set_item_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_item_count**\ (\ )

The number of items currently in the list.


----



[bool<class_bool>] **switch_on_hover** = `false` [🔗<class_MenuButton_property_switch_on_hover>]


- |void| **set_switch_on_hover**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_switch_on_hover**\ (\ )

If `true`, when the cursor hovers above another **MenuButton** within the same parent which also has [switch_on_hover<class_MenuButton_property_switch_on_hover>] enabled, it will close the current **MenuButton** and open the other one.


----


## Method Descriptions



[PopupMenu<class_PopupMenu>] **get_popup**\ (\ ) |const| [🔗<class_MenuButton_method_get_popup>]

Returns the [PopupMenu<class_PopupMenu>] contained in this button.

\ **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [Window.visible<class_Window_property_visible>] property.


----



|void| **set_disable_shortcuts**\ (\ disabled\: [bool<class_bool>]\ ) [🔗<class_MenuButton_method_set_disable_shortcuts>]

If `true`, shortcuts are disabled and cannot be used to trigger the button.


----



|void| **show_popup**\ (\ ) [🔗<class_MenuButton_method_show_popup>]

Adjusts popup position and sizing for the **MenuButton**, then shows the [PopupMenu<class_PopupMenu>]. Prefer this over using `get_popup().popup()`.

