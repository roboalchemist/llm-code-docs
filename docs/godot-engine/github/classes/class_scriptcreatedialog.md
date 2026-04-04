:github_url: hide



# ScriptCreateDialog

**Inherits:** [ConfirmationDialog<class_ConfirmationDialog>] **<** [AcceptDialog<class_AcceptDialog>] **<** [Window<class_Window>] **<** [Viewport<class_Viewport>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Godot editor's popup dialog for creating new [Script<class_Script>] files.


## Description

The **ScriptCreateDialog** creates script files according to a given template for a given scripting language. The standard use is to configure its fields prior to calling one of the [Window.popup()<class_Window_method_popup>] methods.


> **TABS**
>

    func _ready():
        var dialog = ScriptCreateDialog.new();
        dialog.config("Node", "res://new_node.gd") # For in-engine types.
        dialog.config("\"res://base_node.gd\"", "res://derived_node.gd") # For script types.
        dialog.popup_centered()


    public override void _Ready()
    {
        var dialog = new ScriptCreateDialog();
        dialog.Config("Node", "res://NewNode.cs"); // For in-engine types.
        dialog.Config("\"res://BaseNode.cs\"", "res://DerivedNode.cs"); // For script types.
        dialog.PopupCentered();
    }




## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+-------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | dialog_hide_on_ok | ``false`` (overrides :ref:`AcceptDialog<class_AcceptDialog_property_dialog_hide_on_ok>`) |
> +-----------------------------+-------------------+------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | ok_button_text    | ``"Create"`` (overrides :ref:`AcceptDialog<class_AcceptDialog_property_ok_button_text>`) |
> +-----------------------------+-------------------+------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | title             | ``"Attach Node Script"`` (overrides :ref:`Window<class_Window_property_title>`)          |
> +-----------------------------+-------------------+------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`config<class_ScriptCreateDialog_method_config>`\ (\ inherits\: :ref:`String<class_String>`, path\: :ref:`String<class_String>`, built_in_enabled\: :ref:`bool<class_bool>` = true, load_enabled\: :ref:`bool<class_bool>` = true\ ) |
> +--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**script_created**\ (\ script\: [Script<class_Script>]\ ) [🔗<class_ScriptCreateDialog_signal_script_created>]

Emitted when the user clicks the OK button.


----


## Method Descriptions



|void| **config**\ (\ inherits\: [String<class_String>], path\: [String<class_String>], built_in_enabled\: [bool<class_bool>] = true, load_enabled\: [bool<class_bool>] = true\ ) [🔗<class_ScriptCreateDialog_method_config>]

Prefills required fields to configure the ScriptCreateDialog for use.

