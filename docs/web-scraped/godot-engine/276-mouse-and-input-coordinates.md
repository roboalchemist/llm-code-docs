# Mouse and input coordinates

# Mouse and input coordinates

## About
The reason for this small tutorial is to clear up many common mistakes
about input coordinates, obtaining mouse position and screen resolution,
etc.

## Hardware display coordinates
Using hardware coordinates makes sense in the case of writing complex
UIs meant to run on PC, such as editors, MMOs, tools, etc. However, it does
not make as much sense outside of that scope.

## Viewport display coordinates
Godot uses viewports to display content, and viewports can be scaled by
several options (seeMultiple resolutionstutorial). Use, then, the
functions in nodes to obtain the mouse coordinates and viewport size,
for example:
```
func _input(event):
    # Mouse in viewport coordinates.
    if event is InputEventMouseButton:
        print("Mouse Click/Unclick at: ", event.position)
    elif event is InputEventMouseMotion:
        print("Mouse Motion at: ", event.position)

    # Print the size of the viewport.
    print("Viewport Resolution is: ", get_viewport().get_visible_rect().size)
```
```
public override void _Input(InputEvent @event)
{
    // Mouse in viewport coordinates.
    if (@event is InputEventMouseButton eventMouseButton)
    {
        GD.Print("Mouse Click/Unclick at: ", eventMouseButton.Position);
    }
    else if (@event is InputEventMouseMotion eventMouseMotion)
    {
        GD.Print("Mouse Motion at: ", eventMouseMotion.Position);
    }

    // Print the size of the viewport.
    GD.Print("Viewport Resolution is: ", GetViewport().GetVisibleRect().Size);
}
```
Alternatively, it's possible to ask the viewport for the mouse position:
```
get_viewport().get_mouse_position()
```
```
GetViewport().GetMousePosition();
```
Note
When the mouse mode is set toInput.MOUSE_MODE_CAPTURED, theevent.positionvalue fromInputEventMouseMotionis the center of the screen.
Useevent.relativeinstead ofevent.positionandevent.velocityto process mouse movement and position changes.
When implementing features such as mouselook, it's recommended to useevent.screen_relativeandevent.screen_velocityinstead ofevent.relativeandevent.velocityso that mouse movement behaves the same acrossmultiple resolutions.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.