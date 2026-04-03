# EditorCommandPalette in English

# EditorCommandPalette

Inherits:ConfirmationDialog<AcceptDialog<Window<Viewport<Node<Object
Godot editor's command palette.

## Description

Object that holds all the available Commands and their shortcuts text. These Commands can be accessed throughEditor > Command Palettemenu.
Command key names use slash delimiters to distinguish sections, for example:"example/command1"thenexamplewill be the section name.

```
var command_palette = EditorInterface.get_command_palette()
# external_command is a function that will be called with the command is executed.
var command_callable = Callable(self, "external_command").bind(arguments)
command_palette.add_command("command", "test/command",command_callable)
```

```
EditorCommandPalette commandPalette = EditorInterface.Singleton.GetCommandPalette();
// ExternalCommand is a function that will be called with the command is executed.
Callable commandCallable = new Callable(this, MethodName.ExternalCommand);
commandPalette.AddCommand("command", "test/command", commandCallable)
```

Note:This class shouldn't be instantiated directly. Instead, access the singleton usingEditorInterface.get_command_palette().

## Properties

| bool | dialog_hide_on_ok | false(overridesAcceptDialog) |

bool
dialog_hide_on_ok
false(overridesAcceptDialog)

## Methods

| void | add_command(command_name:String, key_name:String, binded_callable:Callable, shortcut_text:String= "None") |
|---|---|
| void | remove_command(key_name:String) |

void
add_command(command_name:String, key_name:String, binded_callable:Callable, shortcut_text:String= "None")
void
remove_command(key_name:String)

## Method Descriptions

voidadd_command(command_name:String, key_name:String, binded_callable:Callable, shortcut_text:String= "None")🔗
Adds a custom command to EditorCommandPalette.

- command_name:String(Name of theCommand. This is displayed to the user.)
command_name:String(Name of theCommand. This is displayed to the user.)
- key_name:String(Name of the key for a particularCommand. This is used to uniquely identify theCommand.)
key_name:String(Name of the key for a particularCommand. This is used to uniquely identify theCommand.)
- binded_callable:Callable(Callable of theCommand. This will be executed when theCommandis selected.)
binded_callable:Callable(Callable of theCommand. This will be executed when theCommandis selected.)
- shortcut_text:String(Shortcut text of theCommandif available.)
shortcut_text:String(Shortcut text of theCommandif available.)
voidremove_command(key_name:String)🔗
Removes the custom command from EditorCommandPalette.
- key_name:String(Name of the key for a particularCommand.)
key_name:String(Name of the key for a particularCommand.)

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
