# Source: https://firebase.google.com/docs/dynamic-links/unity/create.md.txt

> [!NOTE]
> **Note:** Firebase Dynamic Links is *deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the [migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service) and see the [Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq) for more information.

You can create short or long Dynamic Links with the Firebase Dynamic Links API. The API
takes several optional parameter structures to build links. Short links can
also be created from a previously generated long link. The Dynamic Links API
will generate a URL like the following:

    https://example.page.link/aSDf

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

> [!NOTE]
> **Note:** Dynamic Links is not supported on tvOS.

## Set a Dynamic Links URI prefix

1. In the Firebase console, open the **Dynamic Links** section.

2. If you have not already accepted the terms of service and set a URI prefix for
   your Dynamic Links, do so when prompted.

   If you already have a Dynamic Links URI prefix, take note of it. You need to
   provide a Dynamic Links URI prefix when you programmatically create Dynamic Links.

   ![](https://firebase.google.com/static/docs/dynamic-links/images/dynamic-links-domain.png)
3. **Recommended** : Specify the URL patterns allowed in your deep links and
   fallback links. By doing so, you prevent unauthorized parties from
   creating Dynamic Links that redirect from your domain to sites you don't
   control. See
   [Allow specific URL patterns](https://firebase.google.com/docs/dynamic-links/allow-specific-url-patterns).

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

### Creating a long Dynamic Link from parameters

To create a Dynamic Link, create a `DynamicLinkComponents` object, setting any
of the optional members for additional configuration, and then access the
`LongDynamicLink` property to get the link URL.

The following minimal example creates a long Dynamic Link to
https://www.example.com/ that opens with your Android app
com.example.android on Android and the app com.example.ios on iOS:

```c#
var components = new Firebase.DynamicLinks.DynamicLinkComponents(
    // The base Link.
    new System.Uri("https://www.example.com/"),
    // The dynamic link URI prefix.
    "https://example.page.link") {
      IOSParameters = new Firebase.DynamicLinks.IOSParameters("com.example.ios"),
      AndroidParameters = new Firebase.DynamicLinks.AndroidParameters(
        "com.example.android.package_name"),
    };
// do something with: components.LongDynamicLink
```

> [!NOTE]
> **Note:** Long links append all of the configuration settings as query arguments to the link and therefore do not require any network calls.

### Creating a short Dynamic Link

To create a short Dynamic Link, pass a previously generated long link to
`Firebase.DynamicLinks.GetShortLinkAsync` or build `DynamicLinkComponents` in
the same way as above.

`GetShortLinkAsync` optionally takes an extra `DynamicLinkOptions` config
parameter with the `PathLength` property, allowing you to control how the link
should be generated. Short link generation requires a network request to the
Firebase backend, so the `GetShortLinkAsync` method is executed asynchronously.
`GetShortLinkAsync` returns a `Task<Firebase.DynamicLinks.ShortDynamicLink>`.

For example:

```c#
var options = new Firebase.DynamicLinks.DynamicLinkOptions {
  PathLength = DynamicLinkPathLength.Unguessable
};

Firebase.DynamicLinks.DynamicLinks.GetShortLinkAsync(components, options).ContinueWith(task => {
  if (task.IsCanceled) {
    Debug.LogError("GetShortLinkAsync was canceled.");
    return;
  }
  if (task.IsFaulted) {
    Debug.LogError("GetShortLinkAsync encountered an error: " + task.Exception);
    return;
  }

  // Short Link has been created.
  Firebase.DynamicLinks.ShortDynamicLink link = task.Result;
  Debug.LogFormat("Generated short link {0}", link.Url);

  var warnings = new System.Collections.Generic.List<string>(link.Warnings);
  if (warnings.Count > 0) {
    // Debug logging for warnings generating the short link.
  }
});
```

The example above uses a lambda expression that is triggered when the task is
completed.