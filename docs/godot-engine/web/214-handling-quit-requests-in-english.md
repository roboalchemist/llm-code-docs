# Handling quit requests in English

# Handling quit requests

## Quitting

Most platforms have the option to request the application to quit. On
desktops, this is usually done with the "x" icon on the window title bar.
On mobile devices, the app can quit at any time while it is suspended
to the background.

## Handling the notification

On desktop and web platforms,Nodereceives a specialNOTIFICATION_WM_CLOSE_REQUESTnotification when quitting is requested from
the window manager.
Handling the notification is done as follows (on any node):

```
func _notification(what):
    if what == NOTIFICATION_WM_CLOSE_REQUEST:
        get_tree().quit() # default behavior
```

```
public override void _Notification(int what)
{
    if (what == NotificationWMCloseRequest)
    {
        GetTree().Quit(); // default behavior
    }
}
```

It is important to note that by default, Godot apps have the built-in
behavior to quit when quit is requested from the window manager. This
can be changed, so that the user can take care of the complete quitting
procedure:

```
get_tree().set_auto_accept_quit(false)
```

```
GetTree().AutoAcceptQuit = false;
```

## On mobile devices

There is no direct equivalent toNOTIFICATION_WM_CLOSE_REQUESTon mobile
platforms. Due to the nature of mobile operating systems, the only place
that you can run code prior to quitting is when the app is being suspended to
the background. On both Android and iOS, the app can be killed while suspended
at any time by either the user or the OS. A way to plan ahead for this
possibility is to utilizeNOTIFICATION_APPLICATION_PAUSEDin order to
perform any needed actions as the app is being suspended.
Note
On iOS, you only have approximately 5 seconds to finish a task started by this signal. If you go over this allotment, iOS will kill the app instead of pausing it.
On Android, pressing the Back button will exit the application ifApplication > Config > Quit On Go Backis checked in the Project Settings
(which is the default). This will fireNOTIFICATION_WM_GO_BACK_REQUEST.

## Sending your own quit notification

While forcing the application to close can be done by callingSceneTree.quit, doing so will not send
theNOTIFICATION_WM_CLOSE_REQUESTto the nodes in the scene tree.
Quitting by callingSceneTree.quitwill
not allow custom actions to complete (such as saving, confirming the quit,
or debugging), even if you try to delay the line that forces the quit.
Instead, if you want to notify the nodes in the scene tree about the upcoming
program termination, you should send the notification yourself:

```
get_tree().root.propagate_notification(NOTIFICATION_WM_CLOSE_REQUEST)
```

```
GetTree().Root.PropagateNotification((int)NotificationWMCloseRequest);
```

Sending this notification will inform all nodes about the program termination,
but will not terminate the program itselfunlike in 3.X. In order to achieve
the previous behavior,SceneTree.quitshould
be called after the notification.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
