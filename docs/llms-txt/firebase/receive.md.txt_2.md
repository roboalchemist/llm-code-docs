# Source: https://firebase.google.com/docs/dynamic-links/cpp/receive.md.txt

> [!NOTE]
> **Note:** Firebase Dynamic Links is *deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the [migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service) and see the [Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq) for more information.

To receive the Firebase Dynamic Links that [you created](https://firebase.google.com/docs/dynamic-links/create-links),
you must include the Dynamic Links SDK in your app and create a
[`firebase::dynamic_links::Listener`](https://firebase.google.com/docs/reference/cpp/class/firebase/dynamic-links/listener)
object that implements the
[`OnDynamicLinkReceived`](https://firebase.google.com/docs/reference/cpp/class/firebase/dynamic-links/listener#ondynamiclinkreceived)
virtual function.

The C++ SDK works for both Android and iOS, with some additional setup required
for each platform.

## Before you begin

Before you can use
[Firebase Dynamic Links](https://firebase.google.com/docs/reference/unity/namespace/firebase/dynamic-links),
you need to:

- Register your C++ project and configure it to use Firebase.

  If your C++ project already uses Firebase, then it's already registered and
  configured for Firebase.
- Add the [Firebase C++ SDK](https://firebase.google.com/download/cpp) to your C++ project.

> [!NOTE]
> **Find detailed instructions for these initial
> setup tasks in
> [Add Firebase to your C++
> project](https://firebase.google.com/docs/cpp/setup#note-select-platform).**

Note that adding Firebase to your C++ project involves tasks both in the
[Firebase console](https://console.firebase.google.com/) and in your open C++ project (for example, you download
Firebase config files from the console, then move them into your C++ project).

## Add custom URL schemes (for iOS only)

The Firebase Dynamic Links C++ client library uses custom URL schemes on iOS to
process links. You must add custom URL schemes to your app to support receiving
Dynamic Links.

1. To open your project configuration, double-click the project name in the left
   tree view.

2. Select your app from the **TARGETS** section, then select the **Info** tab,
   then expand the **URL Types** section.

3. Click the **+** button, then add a URL scheme for your reversed client ID. To
   find this value:

   1. Open the `` `GoogleService-Info.plist` `` configuration file, then look for the
      `REVERSED_CLIENT_ID` key.

   2. Copy the value of that key, then paste it into the **URL Schemes** box on
      the configuration page.

   3. Leave the other fields blank.

4. Click the **+** button, then add a second URL scheme. This one is the same as
   your app's bundle ID.

   For example, if your bundle ID is `com.example.ios`, type that value into the
   **URL Schemes** box.

   You can find your app's bundle ID in the **General** tab of the project
   configuration (**Identity \> Bundle Identifier**).

## Receiving a Dynamic Link

### Create and initialize App

Before you can check for received Dynamic Links, you'll need to create and initialize
a [`firebase::App`](https://firebase.google.com/docs/reference/cpp/class/firebase/app) object.

> [!NOTE]
> You only need to initialize firebase::App once, no matter how many Firebase C++ features you use.

Include the header file for `firebase::App`:

```c++
#include "firebase/app.h"
```

The next part varies depending on your platform:

### Android


Create the `firebase::App`, passing the JNI environment and a `jobject`
reference to the Java Activity as arguments:

```c++
app = ::firebase::App::Create(::firebase::AppOptions("APPLICATION NAME"), jni_env, activity);
```

### iOS


Create the `firebase::App`:

```c++
app = ::firebase::App::Create(::firebase::AppOptions("APPLICATION NAME"));
```

### Implement Listener to check for Dynamic Links

To check for a received Dynamic Link, implement and use the
[`firebase::dynamic_links::Listener`](https://firebase.google.com/docs/reference/cpp/class/firebase/dynamic-links/listener)
class.

Include the header file for receiving Dynamic Links:

```c++
#include "firebase/dynamic_links.h"
```

<br />

[Initialize](https://firebase.google.com/docs/reference/cpp/namespace/firebase/dynamic-links#initialize) the Dynamic Links library:

```c++
::firebase::dynamic_links::Initialize(app, null);
```

<br />

Create an object that implements
[`firebase::dynamic_links::Listener`](https://firebase.google.com/docs/reference/cpp/class/firebase/dynamic-links/listener),
and supply it to the Dynamic Links library with
[`SetListener()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/dynamic-links#setlistener),
or pass it as the second argument to
[Initialize](https://firebase.google.com/docs/reference/cpp/namespace/firebase/dynamic-links#initialize).

To receive Dynamic Links, your Listener class must implement the
[`OnDynamicLinkReceived`](https://firebase.google.com/docs/reference/cpp/class/firebase/dynamic-links/listener#ondynamiclinkreceived)
virtual function. By overriding the method, you can receive a deep link, if
one was received.

```c++
class Listener : public firebase::dynamic_links::Listener {
 public:
  // Called on the client when a dynamic link arrives.
  void OnDynamicLinkReceived(
      const firebase::dynamic_links::DynamicLink* dynamic_link) override {
    printf("Received link: %s", dynamic_link->url.c_str());
  }
};
```

> [!NOTE]
> **Note:** On Android you must also call [`Fetch()`](https://firebase.google.com/docs/reference/cpp/namespace/firebase/dynamic-links#fetch) when the application gains focus in order for the listener to be triggered.