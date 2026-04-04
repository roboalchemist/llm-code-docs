:github_url: hide



# EditorToaster

**Inherits:** [HBoxContainer<class_HBoxContainer>] **<** [BoxContainer<class_BoxContainer>] **<** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Manages toast notifications within the editor.


## Description

This object manages the functionality and display of toast notifications within the editor, ensuring immediate and informative alerts are presented to the user.

\ **Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_editor_toaster()<class_EditorInterface_method_get_editor_toaster>].


## Methods

> **TABLE**
> :widths: auto
>
> +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`push_toast<class_EditorToaster_method_push_toast>`\ (\ message\: :ref:`String<class_String>`, severity\: :ref:`Severity<enum_EditorToaster_Severity>` = 0, tooltip\: :ref:`String<class_String>` = ""\ ) |
> +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Severity**: [🔗<enum_EditorToaster_Severity>]



[Severity<enum_EditorToaster_Severity>] **SEVERITY_INFO** = `0`

Toast will display with an INFO severity.



[Severity<enum_EditorToaster_Severity>] **SEVERITY_WARNING** = `1`

Toast will display with a WARNING severity and have a corresponding color.



[Severity<enum_EditorToaster_Severity>] **SEVERITY_ERROR** = `2`

Toast will display with an ERROR severity and have a corresponding color.


----


## Method Descriptions



|void| **push_toast**\ (\ message\: [String<class_String>], severity\: [Severity<enum_EditorToaster_Severity>] = 0, tooltip\: [String<class_String>] = ""\ ) [🔗<class_EditorToaster_method_push_toast>]

Pushes a toast notification to the editor for display.

