cursive
# Module event 
Source 
## Structs§
CallbackCallback is a function that can be triggered by an event.
It has a mutable access to the cursive root.EventTriggerA trigger that only selects some types of events.
## Enums§
EventRepresents an event as seen by the application.EventResultAnswer to an event notification.
The event can be consumed or ignored.KeyA non-character key on the keyboardMouseButtonOne of the buttons present on the mouseMouseEventRepresents a possible event sent by the mouse.
## Type Aliases§
AnyCbA callback that can be run on `&mut dyn View`.