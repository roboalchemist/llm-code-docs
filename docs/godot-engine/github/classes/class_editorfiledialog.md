:github_url: hide



# EditorFileDialog

**Inherits:** [FileDialog<class_FileDialog>] **<** [ConfirmationDialog<class_ConfirmationDialog>] **<** [AcceptDialog<class_AcceptDialog>] **<** [Window<class_Window>] **<** [Viewport<class_Viewport>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A modified version of [FileDialog<class_FileDialog>] used by the editor.


## Description

**EditorFileDialog** is a [FileDialog<class_FileDialog>] tweaked to work in the editor. It automatically handles favorite and recent directory lists, and synchronizes some properties with their corresponding editor settings.

\ **EditorFileDialog** will automatically show a native dialog based on the [EditorSettings.interface/editor/use_native_file_dialogs<class_EditorSettings_property_interface/editor/use_native_file_dialogs>] editor setting and ignores [FileDialog.use_native_dialog<class_FileDialog_property_use_native_dialog>].

\ **Note:** **EditorFileDialog** is invisible by default. To make it visible, call one of the `popup_*` methods from [Window<class_Window>] on the node, such as [Window.popup_centered_clamped()<class_Window_method_popup_centered_clamped>].


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+---------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>` | :ref:`disable_overwrite_warning<class_EditorFileDialog_property_disable_overwrite_warning>` | ``false`` |
> +-------------------------+---------------------------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`add_side_menu<class_EditorFileDialog_method_add_side_menu>`\ (\ menu\: :ref:`Control<class_Control>`, title\: :ref:`String<class_String>` = ""\ ) |
> +--------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **disable_overwrite_warning** = `false` [🔗<class_EditorFileDialog_property_disable_overwrite_warning>]


- |void| **set_disable_overwrite_warning**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_overwrite_warning_disabled**\ (\ )

**Deprecated:** Use [FileDialog.overwrite_warning_enabled<class_FileDialog_property_overwrite_warning_enabled>] instead.

If `true`, the **EditorFileDialog** will not warn the user before overwriting files.


----


## Method Descriptions



|void| **add_side_menu**\ (\ menu\: [Control<class_Control>], title\: [String<class_String>] = ""\ ) [🔗<class_EditorFileDialog_method_add_side_menu>]

**Deprecated:** This feature is no longer supported.

This method is kept for compatibility and does nothing. As an alternative, you can display another dialog after showing the file dialog.

