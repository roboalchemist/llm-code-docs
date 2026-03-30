# Source: https://firebase.google.com/docs/dynamic-links/unity/receive.md.txt

> [!NOTE]
> **Note:** Firebase Dynamic Links is *deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the [migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service) and see the [Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq) for more information.

To receive the Firebase Dynamic Links that [you created](https://firebase.google.com/docs/dynamic-links/create-links),
you must include the Dynamic Links SDK in your app and register a listener to handle the
[`DynamicLinkReceived`](https://firebase.google.com/docs/reference/unity/class/firebase/dynamic-links/dynamic-links#dynamiclinkreceived)
event.

The Unity SDK works for both Android and iOS, with some additional setup required
for each platform.

## Before you begin

Before you can use
[Firebase Dynamic Links](https://firebase.google.com/docs/reference/unity/namespace/firebase/dynamic-links),
you need to:

- Register your Unity project and configure it to use Firebase.

  - If your Unity project already uses Firebase, then it's already
    registered and configured for Firebase.

  - If you don't have a Unity project, you can download a
    [sample app](https://github.com/google/mechahamster).

- Add the [Firebase Unity SDK](https://firebase.google.com/download/unity) (specifically, `FirebaseDynamicLinks.unitypackage`) to
  your Unity project.

> [!NOTE]
> **Find detailed instructions for these initial
> setup tasks in
> [Add Firebase to your Unity project](https://firebase.google.com/docs/unity/setup#prerequisites).**

Note that adding Firebase to your Unity project involves tasks both in the
[Firebase console](https://console.firebase.google.com/) and in your open Unity project
(for example, you download Firebase config files from the console, then move
them into your Unity project).

## Register to receive incoming Dynamic Links

To check for Dynamic Links, you need to register for the
[`DynamicLinkReceived`](https://firebase.google.com/docs/reference/unity/class/firebase/dynamic-links/dynamic-links#dynamiclinkreceived)
event.

```c#
void Start() {
  DynamicLinks.DynamicLinkReceived += OnDynamicLink;
}

// Display the dynamic link received by the application.
void OnDynamicLink(object sender, EventArgs args) {
  var dynamicLinkEventArgs = args as ReceivedDynamicLinkEventArgs;
  Debug.LogFormat("Received dynamic link {0}",
                  dynamicLinkEventArgs.ReceivedDynamicLink.Url.OriginalString);
}
```