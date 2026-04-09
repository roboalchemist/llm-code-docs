crossterm
# Module event 
Source 
## Structs§
DisableBracketedPasteA command that disables bracketed paste mode.DisableFocusChangeA command that disables focus event emission.DisableMouseCaptureA command that disables mouse event capturing.EnableBracketedPasteA command that enables bracketed paste mode.EnableFocusChangeA command that enables focus event emission.EnableMouseCaptureA command that enables mouse event capturing.EventStreamA stream of `Result<Event>`.KeyEventRepresents a key event.KeyEventStateRepresents extra state about the key event.KeyModifiersRepresents key modifiers (shift, control, alt, etc.).KeyboardEnhancementFlagsRepresents special flags that tell compatible terminals to add extra information to keyboard events.MouseEventRepresents a mouse event.PopKeyboardEnhancementFlagsA command that disables extra kinds of keyboard events.PushKeyboardEnhancementFlagsA command that enables the kitty keyboard protocol, which adds extra information to keyboard events and removes ambiguity for modifier keys.
## Enums§
EventRepresents an event.KeyCodeRepresents a key.KeyEventKindRepresents a keyboard event kind.MediaKeyCodeRepresents a media key (as part of `KeyCode::Media`).ModifierKeyCodeRepresents a modifier key (as part of `KeyCode::Modifier`).MouseButtonRepresents a mouse button.MouseEventKindA mouse event kind.
## Functions§
pollChecks if there is an `Event` available.readReads a single `Event`.