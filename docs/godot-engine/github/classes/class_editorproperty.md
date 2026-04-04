:github_url: hide



# EditorProperty

**Inherits:** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Custom control for editing properties that can be added to the [EditorInspector<class_EditorInspector>].


## Description

A custom control for editing properties that can be added to the [EditorInspector<class_EditorInspector>]. It is added via [EditorInspectorPlugin<class_EditorInspectorPlugin>].


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                  | :ref:`checkable<class_EditorProperty_property_checkable>`               | ``false``                                                           |
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                  | :ref:`checked<class_EditorProperty_property_checked>`                   | ``false``                                                           |
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                  | :ref:`deletable<class_EditorProperty_property_deletable>`               | ``false``                                                           |
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                  | :ref:`draw_background<class_EditorProperty_property_draw_background>`   | ``true``                                                            |
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                  | :ref:`draw_label<class_EditorProperty_property_draw_label>`             | ``true``                                                            |
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                  | :ref:`draw_warning<class_EditorProperty_property_draw_warning>`         | ``false``                                                           |
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`FocusMode<enum_Control_FocusMode>` | focus_mode                                                              | ``3`` (overrides :ref:`Control<class_Control_property_focus_mode>`) |
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                  | :ref:`keying<class_EditorProperty_property_keying>`                     | ``false``                                                           |
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`String<class_String>`              | :ref:`label<class_EditorProperty_property_label>`                       | ``""``                                                              |
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`float<class_float>`                | :ref:`name_split_ratio<class_EditorProperty_property_name_split_ratio>` | ``0.5``                                                             |
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                  | :ref:`read_only<class_EditorProperty_property_read_only>`               | ``false``                                                           |
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                  | :ref:`selectable<class_EditorProperty_property_selectable>`             | ``true``                                                            |
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                  | :ref:`use_folding<class_EditorProperty_property_use_folding>`           | ``false``                                                           |
> +------------------------------------------+-------------------------------------------------------------------------+---------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`_set_read_only<class_EditorProperty_private_method__set_read_only>`\ (\ read_only\: :ref:`bool<class_bool>`\ ) |virtual|                                                                                                                            |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`_update_property<class_EditorProperty_private_method__update_property>`\ (\ ) |virtual|                                                                                                                                                             |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`add_focusable<class_EditorProperty_method_add_focusable>`\ (\ control\: :ref:`Control<class_Control>`\ )                                                                                                                                            |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`deselect<class_EditorProperty_method_deselect>`\ (\ )                                                                                                                                                                                               |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`emit_changed<class_EditorProperty_method_emit_changed>`\ (\ property\: :ref:`StringName<class_StringName>`, value\: :ref:`Variant<class_Variant>`, field\: :ref:`StringName<class_StringName>` = &"", changing\: :ref:`bool<class_bool>` = false\ ) |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`         | :ref:`get_edited_object<class_EditorProperty_method_get_edited_object>`\ (\ )                                                                                                                                                                             |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>` | :ref:`get_edited_property<class_EditorProperty_method_get_edited_property>`\ (\ ) |const|                                                                                                                                                                 |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_selected<class_EditorProperty_method_is_selected>`\ (\ ) |const|                                                                                                                                                                                 |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`select<class_EditorProperty_method_select>`\ (\ focusable\: :ref:`int<class_int>` = -1\ )                                                                                                                                                           |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`set_bottom_editor<class_EditorProperty_method_set_bottom_editor>`\ (\ editor\: :ref:`Control<class_Control>`\ )                                                                                                                                     |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`set_label_reference<class_EditorProperty_method_set_label_reference>`\ (\ control\: :ref:`Control<class_Control>`\ )                                                                                                                                |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`set_object_and_property<class_EditorProperty_method_set_object_and_property>`\ (\ object\: :ref:`Object<class_Object>`, property\: :ref:`StringName<class_StringName>`\ )                                                                           |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`update_property<class_EditorProperty_method_update_property>`\ (\ )                                                                                                                                                                                 |
> +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**multiple_properties_changed**\ (\ properties\: [PackedStringArray<class_PackedStringArray>], value\: [Array<class_Array>]\ ) [🔗<class_EditorProperty_signal_multiple_properties_changed>]

Emit it if you want multiple properties modified at the same time. Do not use if added via [EditorInspectorPlugin._parse_property()<class_EditorInspectorPlugin_private_method__parse_property>].


----



**object_id_selected**\ (\ property\: [StringName<class_StringName>], id\: [int<class_int>]\ ) [🔗<class_EditorProperty_signal_object_id_selected>]

Used by sub-inspectors. Emit it if what was selected was an Object ID.


----



**property_can_revert_changed**\ (\ property\: [StringName<class_StringName>], can_revert\: [bool<class_bool>]\ ) [🔗<class_EditorProperty_signal_property_can_revert_changed>]

Emitted when the revertability (i.e., whether it has a non-default value and thus is displayed with a revert icon) of a property has changed.


----



**property_changed**\ (\ property\: [StringName<class_StringName>], value\: [Variant<class_Variant>], field\: [StringName<class_StringName>], changing\: [bool<class_bool>]\ ) [🔗<class_EditorProperty_signal_property_changed>]

Do not emit this manually, use the [emit_changed()<class_EditorProperty_method_emit_changed>] method instead.


----



**property_checked**\ (\ property\: [StringName<class_StringName>], checked\: [bool<class_bool>]\ ) [🔗<class_EditorProperty_signal_property_checked>]

Emitted when a property was checked. Used internally.


----



**property_deleted**\ (\ property\: [StringName<class_StringName>]\ ) [🔗<class_EditorProperty_signal_property_deleted>]

Emitted when a property was deleted. Used internally.


----



**property_favorited**\ (\ property\: [StringName<class_StringName>], favorited\: [bool<class_bool>]\ ) [🔗<class_EditorProperty_signal_property_favorited>]

Emit it if you want to mark a property as favorited, making it appear at the top of the inspector.


----



**property_keyed**\ (\ property\: [StringName<class_StringName>]\ ) [🔗<class_EditorProperty_signal_property_keyed>]

Emit it if you want to add this value as an animation key (check for keying being enabled first).


----



**property_keyed_with_value**\ (\ property\: [StringName<class_StringName>], value\: [Variant<class_Variant>]\ ) [🔗<class_EditorProperty_signal_property_keyed_with_value>]

Emit it if you want to key a property with a single value.


----



**property_overridden**\ (\ ) [🔗<class_EditorProperty_signal_property_overridden>]

Emitted when a setting override for the current project is requested.


----



**property_pinned**\ (\ property\: [StringName<class_StringName>], pinned\: [bool<class_bool>]\ ) [🔗<class_EditorProperty_signal_property_pinned>]

Emit it if you want to mark (or unmark) the value of a property for being saved regardless of being equal to the default value.

The default value is the one the property will get when the node is just instantiated and can come from an ancestor scene in the inheritance/instantiation chain, a script or a builtin class.


----



**resource_selected**\ (\ path\: [String<class_String>], resource\: [Resource<class_Resource>]\ ) [🔗<class_EditorProperty_signal_resource_selected>]

If you want a sub-resource to be edited, emit this signal with the resource.


----



**selected**\ (\ path\: [String<class_String>], focusable_idx\: [int<class_int>]\ ) [🔗<class_EditorProperty_signal_selected>]

Emitted when selected. Used internally.


----


## Property Descriptions



[bool<class_bool>] **checkable** = `false` [🔗<class_EditorProperty_property_checkable>]


- |void| **set_checkable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_checkable**\ (\ )

Used by the inspector, set to `true` when the property is checkable.


----



[bool<class_bool>] **checked** = `false` [🔗<class_EditorProperty_property_checked>]


- |void| **set_checked**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_checked**\ (\ )

Used by the inspector, set to `true` when the property is checked.


----



[bool<class_bool>] **deletable** = `false` [🔗<class_EditorProperty_property_deletable>]


- |void| **set_deletable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_deletable**\ (\ )

Used by the inspector, set to `true` when the property can be deleted by the user.


----



[bool<class_bool>] **draw_background** = `true` [🔗<class_EditorProperty_property_draw_background>]


- |void| **set_draw_background**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_draw_background**\ (\ )

Used by the inspector, set to `true` when the property background is drawn.


----



[bool<class_bool>] **draw_label** = `true` [🔗<class_EditorProperty_property_draw_label>]


- |void| **set_draw_label**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_draw_label**\ (\ )

Used by the inspector, set to `true` when the property label is drawn.


----



[bool<class_bool>] **draw_warning** = `false` [🔗<class_EditorProperty_property_draw_warning>]


- |void| **set_draw_warning**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_draw_warning**\ (\ )

Used by the inspector, set to `true` when the property is drawn with the editor theme's warning color. This is used for editable children's properties.


----



[bool<class_bool>] **keying** = `false` [🔗<class_EditorProperty_property_keying>]


- |void| **set_keying**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_keying**\ (\ )

Used by the inspector, set to `true` when the property can add keys for animation.


----



[String<class_String>] **label** = `""` [🔗<class_EditorProperty_property_label>]


- |void| **set_label**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_label**\ (\ )

Set this property to change the label (if you want to show one).


----



[float<class_float>] **name_split_ratio** = `0.5` [🔗<class_EditorProperty_property_name_split_ratio>]


- |void| **set_name_split_ratio**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_name_split_ratio**\ (\ )

Space distribution ratio between the label and the editing field.


----



[bool<class_bool>] **read_only** = `false` [🔗<class_EditorProperty_property_read_only>]


- |void| **set_read_only**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_read_only**\ (\ )

Used by the inspector, set to `true` when the property is read-only.


----



[bool<class_bool>] **selectable** = `true` [🔗<class_EditorProperty_property_selectable>]


- |void| **set_selectable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_selectable**\ (\ )

Used by the inspector, set to `true` when the property is selectable.


----



[bool<class_bool>] **use_folding** = `false` [🔗<class_EditorProperty_property_use_folding>]


- |void| **set_use_folding**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_folding**\ (\ )

Used by the inspector, set to `true` when the property is using folding.


----


## Method Descriptions



|void| **_set_read_only**\ (\ read_only\: [bool<class_bool>]\ ) |virtual| [🔗<class_EditorProperty_private_method__set_read_only>]

Called when the read-only status of the property is changed. It may be used to change custom controls into a read-only or modifiable state.


----



|void| **_update_property**\ (\ ) |virtual| [🔗<class_EditorProperty_private_method__update_property>]

When this virtual function is called, you must update your editor.


----



|void| **add_focusable**\ (\ control\: [Control<class_Control>]\ ) [🔗<class_EditorProperty_method_add_focusable>]

If any of the controls added can gain keyboard focus, add it here. This ensures that focus will be restored if the inspector is refreshed.


----



|void| **deselect**\ (\ ) [🔗<class_EditorProperty_method_deselect>]

Draw property as not selected. Used by the inspector.


----



|void| **emit_changed**\ (\ property\: [StringName<class_StringName>], value\: [Variant<class_Variant>], field\: [StringName<class_StringName>] = &"", changing\: [bool<class_bool>] = false\ ) [🔗<class_EditorProperty_method_emit_changed>]

If one or several properties have changed, this must be called. `field` is used in case your editor can modify fields separately (as an example, Vector3.x). The `changing` argument avoids the editor requesting this property to be refreshed (leave as `false` if unsure).


----



[Object<class_Object>] **get_edited_object**\ (\ ) [🔗<class_EditorProperty_method_get_edited_object>]

Returns the edited object.

\ **Note:** This method could return `null` if the editor has not yet been associated with a property. However, in [_update_property()<class_EditorProperty_private_method__update_property>] and [_set_read_only()<class_EditorProperty_private_method__set_read_only>], this value is *guaranteed* to be non-`null`.


----



[StringName<class_StringName>] **get_edited_property**\ (\ ) |const| [🔗<class_EditorProperty_method_get_edited_property>]

Returns the edited property. If your editor is for a single property (added via [EditorInspectorPlugin._parse_property()<class_EditorInspectorPlugin_private_method__parse_property>]), then this will return the property.

\ **Note:** This method could return `null` if the editor has not yet been associated with a property. However, in [_update_property()<class_EditorProperty_private_method__update_property>] and [_set_read_only()<class_EditorProperty_private_method__set_read_only>], this value is *guaranteed* to be non-`null`.


----



[bool<class_bool>] **is_selected**\ (\ ) |const| [🔗<class_EditorProperty_method_is_selected>]

Returns `true` if property is drawn as selected. Used by the inspector.


----



|void| **select**\ (\ focusable\: [int<class_int>] = -1\ ) [🔗<class_EditorProperty_method_select>]

Draw property as selected. Used by the inspector.


----



|void| **set_bottom_editor**\ (\ editor\: [Control<class_Control>]\ ) [🔗<class_EditorProperty_method_set_bottom_editor>]

Puts the `editor` control below the property label. The control must be previously added using [Node.add_child()<class_Node_method_add_child>].


----



|void| **set_label_reference**\ (\ control\: [Control<class_Control>]\ ) [🔗<class_EditorProperty_method_set_label_reference>]

Used by the inspector, set to a control that will be used as a reference to calculate the size of the label.


----



|void| **set_object_and_property**\ (\ object\: [Object<class_Object>], property\: [StringName<class_StringName>]\ ) [🔗<class_EditorProperty_method_set_object_and_property>]

Assigns object and property to edit.


----



|void| **update_property**\ (\ ) [🔗<class_EditorProperty_method_update_property>]

Forces a refresh of the property display.

