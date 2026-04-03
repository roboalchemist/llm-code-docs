:github_url: hide



# OpenXRInteractionProfileEditorBase

**Inherits:** [HBoxContainer<class_HBoxContainer>] **<** [BoxContainer<class_BoxContainer>] **<** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [OpenXRInteractionProfileEditor<class_OpenXRInteractionProfileEditor>]

Base class for editing interaction profiles.


## Description

This is a base class for interaction profile editors used by the OpenXR action map editor. It can be used to create bespoke editors for specific interaction profiles.


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------+
> | |bitfield|\[:ref:`SizeFlags<enum_Control_SizeFlags>`\] | size_flags_horizontal | ``3`` (overrides :ref:`Control<class_Control_property_size_flags_horizontal>`) |
> +--------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------+
> | |bitfield|\[:ref:`SizeFlags<enum_Control_SizeFlags>`\] | size_flags_vertical   | ``3`` (overrides :ref:`Control<class_Control_property_size_flags_vertical>`)   |
> +--------------------------------------------------------+-----------------------+--------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`setup<class_OpenXRInteractionProfileEditorBase_method_setup>`\ (\ action_map\: :ref:`OpenXRActionMap<class_OpenXRActionMap>`, interaction_profile\: :ref:`OpenXRInteractionProfile<class_OpenXRInteractionProfile>`\ ) |
> +--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **setup**\ (\ action_map\: [OpenXRActionMap<class_OpenXRActionMap>], interaction_profile\: [OpenXRInteractionProfile<class_OpenXRInteractionProfile>]\ ) [🔗<class_OpenXRInteractionProfileEditorBase_method_setup>]

Setup this editor for the provided `action_map` and `interaction_profile`.

