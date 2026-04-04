:github_url: hide



# EditorInspector

**Inherits:** [ScrollContainer<class_ScrollContainer>] **<** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A control used to edit properties of an object.


## Description

This is the control that implements property editing in the editor's Settings dialogs, the Inspector dock, etc. To get the **EditorInspector** used in the editor's Inspector dock, use [EditorInterface.get_inspector()<class_EditorInterface_method_get_inspector>].

\ **EditorInspector** will show properties in the same order as the array returned by [Object.get_property_list()<class_Object_method_get_property_list>].

If a property's name is path-like (i.e. if it contains forward slashes), **EditorInspector** will create nested sections for "directories" along the path. For example, if a property is named `highlighting/gdscript/node_path_color`, it will be shown as "Node Path Color" inside the "GDScript" section nested inside the "Highlighting" section.

If a property has [@GlobalScope.PROPERTY_USAGE_GROUP<class_@GlobalScope_constant_PROPERTY_USAGE_GROUP>] usage, it will group subsequent properties whose name starts with the property's hint string. The group ends when a property does not start with that hint string or when a new group starts. An empty group name effectively ends the current group. **EditorInspector** will create a top-level section for each group. For example, if a property with group usage is named `Collide With` and its hint string is `collide_with_`, a subsequent `collide_with_area` property will be shown as "Area" inside the "Collide With" section. There is also a special case: when the hint string contains the name of a property, that property is grouped too. This is mainly to help grouping properties like `font`, `font_color` and `font_size` (using the hint string `font_`).

If a property has [@GlobalScope.PROPERTY_USAGE_SUBGROUP<class_@GlobalScope_constant_PROPERTY_USAGE_SUBGROUP>] usage, a subgroup will be created in the same way as a group, and a second-level section will be created for each subgroup.

\ **Note:** Unlike sections created from path-like property names, **EditorInspector** won't capitalize the name for sections created from groups. So properties with group usage usually use capitalized names instead of snake_cased names.


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------+------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                            | draw_focus_border      | ``true`` (overrides :ref:`ScrollContainer<class_ScrollContainer_property_draw_focus_border>`)   |
> +----------------------------------------------------+------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`FocusMode<enum_Control_FocusMode>`           | focus_mode             | ``2`` (overrides :ref:`Control<class_Control_property_focus_mode>`)                             |
> +----------------------------------------------------+------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                            | follow_focus           | ``true`` (overrides :ref:`ScrollContainer<class_ScrollContainer_property_follow_focus>`)        |
> +----------------------------------------------------+------------------------+-------------------------------------------------------------------------------------------------+
> | :ref:`ScrollMode<enum_ScrollContainer_ScrollMode>` | horizontal_scroll_mode | ``0`` (overrides :ref:`ScrollContainer<class_ScrollContainer_property_horizontal_scroll_mode>`) |
> +----------------------------------------------------+------------------------+-------------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                      | :ref:`edit<class_EditorInspector_method_edit>`\ (\ object\: :ref:`Object<class_Object>`\ )                                                                                                                                                                                                                                                                                                                                    |
> +---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`                 | :ref:`get_edited_object<class_EditorInspector_method_get_edited_object>`\ (\ )                                                                                                                                                                                                                                                                                                                                                |
> +---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                 | :ref:`get_selected_path<class_EditorInspector_method_get_selected_path>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                        |
> +---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`EditorProperty<class_EditorProperty>` | :ref:`instantiate_property_editor<class_EditorInspector_method_instantiate_property_editor>`\ (\ object\: :ref:`Object<class_Object>`, type\: :ref:`Variant.Type<enum_@GlobalScope_Variant.Type>`, path\: :ref:`String<class_String>`, hint\: :ref:`PropertyHint<enum_@GlobalScope_PropertyHint>`, hint_text\: :ref:`String<class_String>`, usage\: :ref:`int<class_int>`, wide\: :ref:`bool<class_bool>` = false\ ) |static| |
> +---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**edited_object_changed**\ (\ ) [🔗<class_EditorInspector_signal_edited_object_changed>]

Emitted when the object being edited by the inspector has changed.


----



**object_id_selected**\ (\ id\: [int<class_int>]\ ) [🔗<class_EditorInspector_signal_object_id_selected>]

Emitted when the Edit button of an [Object<class_Object>] has been pressed in the inspector. This is mainly used in the remote scene tree Inspector.


----



**property_deleted**\ (\ property\: [String<class_String>]\ ) [🔗<class_EditorInspector_signal_property_deleted>]

Emitted when a property is removed from the inspector.


----



**property_edited**\ (\ property\: [String<class_String>]\ ) [🔗<class_EditorInspector_signal_property_edited>]

Emitted when a property is edited in the inspector.


----



**property_keyed**\ (\ property\: [String<class_String>], value\: [Variant<class_Variant>], advance\: [bool<class_bool>]\ ) [🔗<class_EditorInspector_signal_property_keyed>]

Emitted when a property is keyed in the inspector. Properties can be keyed by clicking the "key" icon next to a property when the Animation panel is toggled.


----



**property_selected**\ (\ property\: [String<class_String>]\ ) [🔗<class_EditorInspector_signal_property_selected>]

Emitted when a property is selected in the inspector.


----



**property_toggled**\ (\ property\: [String<class_String>], checked\: [bool<class_bool>]\ ) [🔗<class_EditorInspector_signal_property_toggled>]

Emitted when a boolean property is toggled in the inspector.

\ **Note:** This signal is never emitted if the internal `autoclear` property enabled. Since this property is always enabled in the editor inspector, this signal is never emitted by the editor itself.


----



**resource_selected**\ (\ resource\: [Resource<class_Resource>], path\: [String<class_String>]\ ) [🔗<class_EditorInspector_signal_resource_selected>]

Emitted when a resource is selected in the inspector.


----



**restart_requested**\ (\ ) [🔗<class_EditorInspector_signal_restart_requested>]

Emitted when a property that requires a restart to be applied is edited in the inspector. This is only used in the Project Settings and Editor Settings.


----


## Method Descriptions



|void| **edit**\ (\ object\: [Object<class_Object>]\ ) [🔗<class_EditorInspector_method_edit>]

Shows the properties of the given `object` in this inspector for editing. To clear the inspector, call this method with `null`.

\ **Note:** If you want to edit an object in the editor's main inspector, use the `edit_*` methods in [EditorInterface<class_EditorInterface>] instead.


----



[Object<class_Object>] **get_edited_object**\ (\ ) [🔗<class_EditorInspector_method_get_edited_object>]

Returns the object currently selected in this inspector.


----



[String<class_String>] **get_selected_path**\ (\ ) |const| [🔗<class_EditorInspector_method_get_selected_path>]

Gets the path of the currently selected property.


----



[EditorProperty<class_EditorProperty>] **instantiate_property_editor**\ (\ object\: [Object<class_Object>], type\: [Variant.Type<enum_@GlobalScope_Variant.Type>], path\: [String<class_String>], hint\: [PropertyHint<enum_@GlobalScope_PropertyHint>], hint_text\: [String<class_String>], usage\: [int<class_int>], wide\: [bool<class_bool>] = false\ ) |static| [🔗<class_EditorInspector_method_instantiate_property_editor>]

Creates a property editor that can be used by plugin UI to edit the specified property of an `object`.

