:github_url: hide



# EditorCommandPalette

**Inherits:** [ConfirmationDialog<class_ConfirmationDialog>] **<** [AcceptDialog<class_AcceptDialog>] **<** [Window<class_Window>] **<** [Viewport<class_Viewport>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Godot editor's command palette.


## Description

Object that holds all the available Commands and their shortcuts text. These Commands can be accessed through **Editor > Command Palette** menu.

Command key names use slash delimiters to distinguish sections, for example: `"example/command1"` then `example` will be the section name.


> **TABS**
>

    var command_palette = EditorInterface.get_command_palette()
    # external_command is a function that will be called with the command is executed.
    var command_callable = Callable(self, "external_command").bind(arguments)
    command_palette.add_command("command", "test/command",command_callable)


    EditorCommandPalette commandPalette = EditorInterface.Singleton.GetCommandPalette();
    // ExternalCommand is a function that will be called with the command is executed.
    Callable commandCallable = new Callable(this, MethodName.ExternalCommand);
    commandPalette.AddCommand("command", "test/command", commandCallable)



\ **Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_command_palette()<class_EditorInterface_method_get_command_palette>].


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+-------------------+------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | dialog_hide_on_ok | ``false`` (overrides :ref:`AcceptDialog<class_AcceptDialog_property_dialog_hide_on_ok>`) |
> +-------------------------+-------------------+------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`add_command<class_EditorCommandPalette_method_add_command>`\ (\ command_name\: :ref:`String<class_String>`, key_name\: :ref:`String<class_String>`, binded_callable\: :ref:`Callable<class_Callable>`, shortcut_text\: :ref:`String<class_String>` = "None"\ ) |
> +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`remove_command<class_EditorCommandPalette_method_remove_command>`\ (\ key_name\: :ref:`String<class_String>`\ )                                                                                                                                                |
> +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **add_command**\ (\ command_name\: [String<class_String>], key_name\: [String<class_String>], binded_callable\: [Callable<class_Callable>], shortcut_text\: [String<class_String>] = "None"\ ) [🔗<class_EditorCommandPalette_method_add_command>]

Adds a custom command to EditorCommandPalette.

- `command_name`: [String<class_String>] (Name of the **Command**. This is displayed to the user.)

- `key_name`: [String<class_String>] (Name of the key for a particular **Command**. This is used to uniquely identify the **Command**.)

- `binded_callable`: [Callable<class_Callable>] (Callable of the **Command**. This will be executed when the **Command** is selected.)

- `shortcut_text`: [String<class_String>] (Shortcut text of the **Command** if available.)


----



|void| **remove_command**\ (\ key_name\: [String<class_String>]\ ) [🔗<class_EditorCommandPalette_method_remove_command>]

Removes the custom command from EditorCommandPalette.

- `key_name`: [String<class_String>] (Name of the key for a particular **Command**.)

