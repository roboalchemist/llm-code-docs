# Source: https://firebase.google.com/docs/dynamic-links/cpp/create.md.txt

> [!NOTE]
> **Note:** Firebase Dynamic Links is *deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the [migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service) and see the [Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq) for more information.

You can create short or long Dynamic Links with the Firebase Dynamic Links API. The API
takes several optional parameter structures to build links. Short links can
also be created from a previously generated long link. Firebase Dynamic Links
generates a URL like the following:

    https://example.page.link/WXYZ

The C++ SDK works for both Android and iOS, with some additional setup required
for each platform.d

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

### Android

1. In the Firebase console, open the **Dynamic Links** section.
2. If you have not already accepted the terms of service and set a URI
   prefix for your Dynamic Links, do so when prompted.

   If you already have a Dynamic Links URI prefix, take note of it. You need
   to provide a Dynamic Links URI prefix when you programmatically create
   Dynamic Links.

   ![](https://firebase.google.com/static/docs/dynamic-links/images/dynamic-links-domain.png)
3. **Recommended** : Specify the URL patterns allowed in your deep links and fallback links. By doing so, you prevent unauthorized parties from creating Dynamic Links that redirect from your domain to sites you don't control. See [Allow specific URL patterns](https://firebase.google.com/docs/dynamic-links/allow-specific-url-patterns).

### iOS

1. In the Firebase console, open the **Dynamic Links** section.
2. If you have not already accepted the terms of service and set a URI
   prefix for your Dynamic Links, do so when prompted.

   If you already have a Dynamic Links URI prefix, take note of it. You need
   to provide a Dynamic Links domain when you programmatically create
   Dynamic Links.

   ![](https://firebase.google.com/static/docs/dynamic-links/images/dynamic-links-domain.png)
3. The Firebase Dynamic Links C++ client library uses custom URL schemes on iOS to process links. You must add custom URL schemes to your app to support receiving Dynamic Links:
   1. To open your project configuration, double-click the project name in the left tree view. Select your app from the **TARGETS** section, then select the **Info** tab, and expand the **URL Types** section.
   2. Click the **+** button, and add a URL scheme for your reversed client ID. To find this value, open the `` `GoogleService-Info.plist` `` configuration file, and look for the `REVERSED_CLIENT_ID` key. Copy the value of that key, and paste it into the **URL Schemes** box on the configuration page. Leave the other fields blank.
   3. Click the **+** button, and add a second URL scheme. This one is the same as your app's bundle ID. For example, if your bundle ID is `com.example.ios`, type that value into the **URL Schemes** box. You can find your app's bundle ID in the **General** tab of the project configuration (**Identity \> Bundle Identifier**).

> [!NOTE]
> **Note:** Dynamic Links is not supported on tvOS.

## Use the Firebase console

If you want to generate a single Dynamic Link, either for testing purposes, or for your marketing team
to easily create a link that can be used in something like a social media post, the simplest way would
be to visit the [Firebase console](https://console.firebase.google.com/project/_/durablelinks/links/)
and create one manually following the step-by-step form.

### Custom domains

You can have greater control over your Dynamic Link's branding by using your own
domain instead of a `goo.gl` or `page.link` subdomain. Follow [these
instructions](https://firebase.google.com/docs/dynamic-links/custom-domains) to set up a custom domain for
your project.

> [!NOTE]
> **Note:** If you're building your project for iOS, you must edit the `Info.plist` file per the [iOS-only instructions](https://firebase.google.com/docs/dynamic-links/custom-domains#console) for setting up a custom domain.

## Using the Firebase Dynamic Links API

### Create and initialize App

Before you can create Dynamic Links, you'll need to create and initialize
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

### Initialize Dynamic Links library

Before creating a Dynamic Link, you must first
[initialize](https://firebase.google.com/docs/reference/cpp/namespace/firebase/dynamic-links#initialize)
the Dynamic Links library:

```c++
::firebase::dynamic_links::Initialize(app, null);
```

<br />

### Creating a long Dynamic Link from parameters

To create a Dynamic Link, create a DynamicLinkComponents object, setting any of
the optional members for additional configuration, and passing it to
`dynamic_links::GetShortLink` or `dynamic_links::GetLongLink`.

The following minimal example creates a long Dynamic Link to
https://www.example.com/ that opens with your Android app
com.example.android.package_name and iOS app com.example.ios:

```c++
firebase::dynamic_links::IOSParameters ios_parameters("com.example.ios");

firebase::dynamic_links::AndroidParameters android_parameters(
    "com.example.android.package_name");

firebase::dynamic_links::DynamicLinkComponents components(
    "https://www.example.com/", "example.page.link");
components.android_parameters = &android_parameters;
components.ios_parameters = &ios_parameters;

firebase::dynamic_links::GeneratedDynamicLink long_link =
    firebase::dynamic_links::GetLongLink(components);
```

> [!NOTE]
> **Note:** Long Links append all of the configuration settings as query arguments to the link and therefore do not require any network calls.

### Creating a short Dynamic Link

To create a short Dynamic Link, pass a previously generated long link to
`GetShortLink` or build `DynamicLinkComponents` the same way as above.

`GetShortLink` optionally takes an extra `DynamicLinkOptions` config
parameter with `PathLength`; this allows you to control how the link should be
generated. Generating a short link requires a network request to the Firebase
backend, so `GetShortLink` is asynchronous, returning a `Future<GeneratedLink>`.

For example:

```c++
firebase::dynamic_links::DynamicLinkOptions short_link_options;
short_link_options.path_length = firebase::dynamic_links::kPathLengthShort;

firebase::Future<firebase::dynamic_links::GeneratedDynamicLink> result =
    firebase::dynamic_links::GetShortLink(components, short_link_options);
```

If your program has an update loop that runs regularly (say at 30 or 60 times
per second), you can check the results once per update:

```c++
if (result.status() == firebase::kFutureStatusComplete) {
  if (result.error() == firebase::dynamic_links::kErrorCodeSuccess) {
    firebase::dynamic_links::GeneratedDynamicLink link = *result.result();
    printf("Create short link succeeded: %s\n", link.url.c_str());
  } else {
    printf("Created short link failed with error '%s'\n",
           result.error_message());
  }
}
```