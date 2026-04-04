:github_url: hide



# OpenXRBindingModifierEditor

**Inherits:** [PanelContainer<class_PanelContainer>] **<** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Binding modifier editor.


## Description

This is the default binding modifier editor used in the OpenXR action map.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------+
> | |bitfield|\[:ref:`SizeFlags<enum_Control_SizeFlags>`\] | size_flags_horizontal | ``3`` (overrides :ref:`Control<class_Control_property_size_flags_horizontal>`) |
> +--------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`OpenXRBindingModifier<class_OpenXRBindingModifier>` | :ref:`get_binding_modifier<class_OpenXRBindingModifierEditor_method_get_binding_modifier>`\ (\ ) |const|                                                                                                     |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`setup<class_OpenXRBindingModifierEditor_method_setup>`\ (\ action_map\: :ref:`OpenXRActionMap<class_OpenXRActionMap>`, binding_modifier\: :ref:`OpenXRBindingModifier<class_OpenXRBindingModifier>`\ ) |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**binding_modifier_removed**\ (\ binding_modifier_editor\: [Object<class_Object>]\ ) [🔗<class_OpenXRBindingModifierEditor_signal_binding_modifier_removed>]

Signal emitted when the user presses the delete binding modifier button for this modifier.


----


## Method Descriptions



[OpenXRBindingModifier<class_OpenXRBindingModifier>] **get_binding_modifier**\ (\ ) |const| [🔗<class_OpenXRBindingModifierEditor_method_get_binding_modifier>]

Returns the [OpenXRBindingModifier<class_OpenXRBindingModifier>] currently being edited.


----



|void| **setup**\ (\ action_map\: [OpenXRActionMap<class_OpenXRActionMap>], binding_modifier\: [OpenXRBindingModifier<class_OpenXRBindingModifier>]\ ) [🔗<class_OpenXRBindingModifierEditor_method_setup>]

Setup this editor for the provided `action_map` and `binding_modifier`.

