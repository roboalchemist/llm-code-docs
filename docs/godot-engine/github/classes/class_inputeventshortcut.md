:github_url: hide



# InputEventShortcut

**Inherits:** [InputEvent<class_InputEvent>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a triggered keyboard [Shortcut<class_Shortcut>].


## Description

InputEventShortcut is a special event that can be received in [Node._input()<class_Node_private_method__input>], [Node._shortcut_input()<class_Node_private_method__shortcut_input>], and [Node._unhandled_input()<class_Node_private_method__unhandled_input>]. It is typically sent by the editor's Command Palette to trigger actions, but can also be sent manually using [Viewport.push_input()<class_Viewport_method_push_input>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+-------------------------------------------------------------+
> | :ref:`Shortcut<class_Shortcut>` | :ref:`shortcut<class_InputEventShortcut_property_shortcut>` |
> +---------------------------------+-------------------------------------------------------------+
>

----


## Property Descriptions



[Shortcut<class_Shortcut>] **shortcut** [🔗<class_InputEventShortcut_property_shortcut>]


- |void| **set_shortcut**\ (\ value\: [Shortcut<class_Shortcut>]\ )
- [Shortcut<class_Shortcut>] **get_shortcut**\ (\ )

The [Shortcut<class_Shortcut>] represented by this event. Its [Shortcut.matches_event()<class_Shortcut_method_matches_event>] method will always return `true` for this event.

