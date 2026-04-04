:github_url: hide



# EditorResourcePicker

**Inherits:** [HBoxContainer<class_HBoxContainer>] **<** [BoxContainer<class_BoxContainer>] **<** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [EditorScriptPicker<class_EditorScriptPicker>]

Godot editor's control for selecting [Resource<class_Resource>] type properties.


## Description

This [Control<class_Control>] node is used in the editor's Inspector dock to allow editing of [Resource<class_Resource>] type properties. It provides options for creating, loading, saving and converting resources. Can be used with [EditorInspectorPlugin<class_EditorInspectorPlugin>] to recreate the same behavior.

\ **Note:** This [Control<class_Control>] does not include any editor for the resource, as editing is controlled by the Inspector dock itself or sub-Inspectors.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`String<class_String>`     | :ref:`base_type<class_EditorResourcePicker_property_base_type>`             | ``""``    |
> +---------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`         | :ref:`editable<class_EditorResourcePicker_property_editable>`               | ``true``  |
> +---------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`Resource<class_Resource>` | :ref:`edited_resource<class_EditorResourcePicker_property_edited_resource>` |           |
> +---------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`         | :ref:`toggle_mode<class_EditorResourcePicker_property_toggle_mode>`         | ``false`` |
> +---------------------------------+-----------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                           | :ref:`_handle_menu_selected<class_EditorResourcePicker_private_method__handle_menu_selected>`\ (\ id\: :ref:`int<class_int>`\ ) |virtual|          |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`_set_create_options<class_EditorResourcePicker_private_method__set_create_options>`\ (\ menu_node\: :ref:`Object<class_Object>`\ ) |virtual| |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`get_allowed_types<class_EditorResourcePicker_method_get_allowed_types>`\ (\ ) |const|                                                        |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`set_toggle_pressed<class_EditorResourcePicker_method_set_toggle_pressed>`\ (\ pressed\: :ref:`bool<class_bool>`\ )                           |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**resource_changed**\ (\ resource\: [Resource<class_Resource>]\ ) [🔗<class_EditorResourcePicker_signal_resource_changed>]

Emitted when the value of the edited resource was changed.


----



**resource_selected**\ (\ resource\: [Resource<class_Resource>], inspect\: [bool<class_bool>]\ ) [🔗<class_EditorResourcePicker_signal_resource_selected>]

Emitted when the resource value was set and user clicked to edit it. When `inspect` is `true`, the signal was caused by the context menu "Edit" or "Inspect" option.


----


## Property Descriptions



[String<class_String>] **base_type** = `""` [🔗<class_EditorResourcePicker_property_base_type>]


- |void| **set_base_type**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_base_type**\ (\ )

The base type of allowed resource types. Can be a comma-separated list of several options.


----



[bool<class_bool>] **editable** = `true` [🔗<class_EditorResourcePicker_property_editable>]


- |void| **set_editable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_editable**\ (\ )

If `true`, the value can be selected and edited.


----



[Resource<class_Resource>] **edited_resource** [🔗<class_EditorResourcePicker_property_edited_resource>]


- |void| **set_edited_resource**\ (\ value\: [Resource<class_Resource>]\ )
- [Resource<class_Resource>] **get_edited_resource**\ (\ )

The edited resource value.


----



[bool<class_bool>] **toggle_mode** = `false` [🔗<class_EditorResourcePicker_property_toggle_mode>]


- |void| **set_toggle_mode**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_toggle_mode**\ (\ )

If `true`, the main button with the resource preview works in the toggle mode. Use [set_toggle_pressed()<class_EditorResourcePicker_method_set_toggle_pressed>] to manually set the state.


----


## Method Descriptions



[bool<class_bool>] **_handle_menu_selected**\ (\ id\: [int<class_int>]\ ) |virtual| [🔗<class_EditorResourcePicker_private_method__handle_menu_selected>]

This virtual method can be implemented to handle context menu items not handled by default. See [_set_create_options()<class_EditorResourcePicker_private_method__set_create_options>].


----



|void| **_set_create_options**\ (\ menu_node\: [Object<class_Object>]\ ) |virtual| [🔗<class_EditorResourcePicker_private_method__set_create_options>]

This virtual method is called when updating the context menu of **EditorResourcePicker**. Implement this method to override the "New ..." items with your own options. `menu_node` is a reference to the [PopupMenu<class_PopupMenu>] node.

\ **Note:** Implement [_handle_menu_selected()<class_EditorResourcePicker_private_method__handle_menu_selected>] to handle these custom items.


----



[PackedStringArray<class_PackedStringArray>] **get_allowed_types**\ (\ ) |const| [🔗<class_EditorResourcePicker_method_get_allowed_types>]

Returns a list of all allowed types and subtypes corresponding to the [base_type<class_EditorResourcePicker_property_base_type>]. If the [base_type<class_EditorResourcePicker_property_base_type>] is empty, an empty list is returned.


----



|void| **set_toggle_pressed**\ (\ pressed\: [bool<class_bool>]\ ) [🔗<class_EditorResourcePicker_method_set_toggle_pressed>]

Sets the toggle mode state for the main button. Works only if [toggle_mode<class_EditorResourcePicker_property_toggle_mode>] is set to `true`.

