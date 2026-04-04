:github_url: hide



# ConfirmationDialog

**Inherits:** [AcceptDialog<class_AcceptDialog>] **<** [Window<class_Window>] **<** [Viewport<class_Viewport>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [EditorCommandPalette<class_EditorCommandPalette>], [FileDialog<class_FileDialog>], [ScriptCreateDialog<class_ScriptCreateDialog>]

A dialog used for confirmation of actions.


## Description

A dialog used for confirmation of actions. This window is similar to [AcceptDialog<class_AcceptDialog>], but pressing its Cancel button can have a different outcome from pressing the OK button. The order of the two buttons varies depending on the host OS.

To get cancel action, you can use:


> **TABS**
>

    get_cancel_button().pressed.connect(_on_canceled)


    GetCancelButton().Pressed += OnCanceled;



\ **Note:** [AcceptDialog<class_AcceptDialog>] is invisible by default. To make it visible, call one of the `popup_*` methods from [Window<class_Window>] on the node, such as [Window.popup_centered_clamped()<class_Window_method_popup_centered_clamped>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
> | :ref:`String<class_String>`     | :ref:`cancel_button_text<class_ConfirmationDialog_property_cancel_button_text>` | ``"Cancel"``                                                                    |
> +---------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>` | min_size                                                                        | ``Vector2i(200, 70)`` (overrides :ref:`Window<class_Window_property_min_size>`) |
> +---------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>` | size                                                                            | ``Vector2i(200, 100)`` (overrides :ref:`Window<class_Window_property_size>`)    |
> +---------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
> | :ref:`String<class_String>`     | title                                                                           | ``"Please Confirm..."`` (overrides :ref:`Window<class_Window_property_title>`)  |
> +---------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------+-----------------------------------------------------------------------------------+
> | :ref:`Button<class_Button>` | :ref:`get_cancel_button<class_ConfirmationDialog_method_get_cancel_button>`\ (\ ) |
> +-----------------------------+-----------------------------------------------------------------------------------+
>

----


## Property Descriptions



[String<class_String>] **cancel_button_text** = `"Cancel"` [🔗<class_ConfirmationDialog_property_cancel_button_text>]


- |void| **set_cancel_button_text**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_cancel_button_text**\ (\ )

The text displayed by the cancel button (see [get_cancel_button()<class_ConfirmationDialog_method_get_cancel_button>]).


----


## Method Descriptions



[Button<class_Button>] **get_cancel_button**\ (\ ) [🔗<class_ConfirmationDialog_method_get_cancel_button>]

Returns the cancel button.

\ **Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their [CanvasItem.visible<class_CanvasItem_property_visible>] property.

