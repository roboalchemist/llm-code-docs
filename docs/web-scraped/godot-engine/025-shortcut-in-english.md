# Shortcut in English

# Shortcut

Inherits:Resource<RefCounted<Object
A shortcut for binding input.

## Description

Shortcuts (also known as hotkeys) are containers ofInputEventresources. They are commonly used to interact with aControlelement from anInputEvent.
One shortcut can contain multipleInputEventresources, making it possible to trigger one action with multiple different inputs.
Example:Capture theCtrl+Sshortcut using aShortcutresource:

```
extends Node

var save_shortcut = Shortcut.new()
func _ready():
    var key_event = InputEventKey.new()
    key_event.keycode = KEY_S
    key_event.ctrl_pressed = true
    key_event.command_or_control_autoremap = true # Swaps Ctrl for Command on Mac.
    save_shortcut.events = [key_event]

func _input(event):
    if save_shortcut.matches_event(event) and event.is_pressed() and not event.is_echo():
        print("Save shortcut pressed!")
        get_viewport().set_input_as_handled()
```

```
using Godot;

public partial class MyNode : Node
{
    private readonly Shortcut _saveShortcut = new Shortcut();

    public override void _Ready()
    {
        InputEventKey keyEvent = new InputEventKey
        {
            Keycode = Key.S,
            CtrlPressed = true,
            CommandOrControlAutoremap = true, // Swaps Ctrl for Command on Mac.
        };

        _saveShortcut.Events = [keyEvent];
    }

    public override void _Input(InputEvent @event)
    {
        if (@event is InputEventKey keyEvent &&
            _saveShortcut.MatchesEvent(@event) &&
            keyEvent.Pressed && !keyEvent.Echo)
        {
            GD.Print("Save shortcut pressed!");
            GetViewport().SetInputAsHandled();
        }
    }
}
```

## Properties

| Array | events | [] |

Array
events

## Methods

| String | get_as_text()const |
|---|---|
| bool | has_valid_event()const |
| bool | matches_event(event:InputEvent)const |

String
get_as_text()const
bool
has_valid_event()const
bool
matches_event(event:InputEvent)const

## Property Descriptions

Arrayevents=[]🔗

- voidset_events(value:Array)
voidset_events(value:Array)
- Arrayget_events()
Arrayget_events()
The shortcut'sInputEventarray.
Generally theInputEventused is anInputEventKey, though it can be anyInputEvent, including anInputEventAction.

## Method Descriptions

Stringget_as_text()const🔗
Returns the shortcut's first validInputEventas aString.
boolhas_valid_event()const🔗
Returns whethereventscontains anInputEventwhich is valid.
boolmatches_event(event:InputEvent)const🔗
Returns whether anyInputEventineventsequalsevent. This usesInputEvent.is_match()to compare events.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
