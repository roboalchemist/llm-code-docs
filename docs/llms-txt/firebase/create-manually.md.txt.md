# Source: https://firebase.google.com/docs/dynamic-links/create-manually.md.txt

> [!NOTE]
> **Note:** Firebase Dynamic Links is *deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the [migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service) and see the [Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq) for more information.

You can create a Dynamic Link by manually constructing a URL with the following form:

```
https://your_subdomain.page.link/?link=your_deep_link&apn=package_name[&amv=minimum_version][&afl=fallback_link]
```

## Dynamic Link parameters

| Deep link parameter (Payload parameter) ||
|---|---|
| link | The link your app will open. Specify a URL that your app can handle, typically the app's content or payload, which initiates app-specific logic (such as crediting the user with a coupon or displaying a welcome screen). This link must be a well-formatted URL, be properly URL-encoded, use either HTTP or HTTPS, and cannot be another Dynamic Link. > [!NOTE] > When users open a Dynamic Link on a desktop web browser, they will load this URL (unless the `ofl` parameter is specified). If you don't have a web equivalent to the linked content, the URL doesn't need to point to a valid web resource. In this situation, you should set up a redirect from this URL to, for example, your home page. |

| Android parameters ||
|---|---|
| apn | The package name of the Android app to use to open the link. The app must be connected to your project from the Overview page of the Firebase console. Required for the Dynamic Link to open an Android app. |
| afl | The link to open when the app isn't installed. Specify this to do something other than install your app from the Play Store when the app isn't installed, such as open the mobile web version of the content, or display a promotional page for your app. |
| amv | The [`versionCode`](http://developer.android.com/tools/publishing/versioning.html#appversioning) of the minimum version of your app that can open the link. If the installed app is an older version, the user is taken to the Play Store to upgrade the app. |

| iOS parameters ||
|---|---|
| ibi | The bundle ID of the iOS app to use to open the link. The app must be connected to your project from the Overview page of the Firebase console. Required for the Dynamic Link to open an iOS app. |
| ifl | The link to open when the app isn't installed. Specify this to do something other than install your app from the App Store when the app isn't installed, such as open the mobile web version of the content, or display a promotional page for your app. |
| ius | Your app's custom URL scheme, if defined to be something other than your app's bundle ID |
| ipfl | The link to open on iPads when the app isn't installed. Specify this to do something other than install your app from the App Store when the app isn't installed, such as open the web version of the content, or display a promotional page for your app. |
| ipbi | The bundle ID of the iOS app to use on iPads to open the link. The app must be connected to your project from the Overview page of the Firebase console. |
| isi | Your app's App Store ID, used to send users to the App Store when the app isn't installed |
| imv | The [version number](https://developer.apple.com/library/content/technotes/tn2420/_index.html) of the minimum version of your app that can open the link. This flag is passed to your app when it is opened, and your app must decide what to do with it. |
| efr | If set to '1', skip the app preview page when the Dynamic Link is opened, and instead redirect to the app or store. The app preview page (enabled by default) can more reliably send users to the most appropriate destination when they open Dynamic Links in apps; however, if you expect a Dynamic Link to be opened only in apps that can open Dynamic Links reliably without this page, you can disable it with this parameter. This parameter will affect the behavior of the Dynamic Link only on iOS. |

| Other platform parameters ||
|---|---|
| ofl | The link to open on platforms beside Android and iOS. This is useful to specify a different behavior on desktop, like displaying a full web page of the app content/payload (as specified by param link) with another dynamic link to install the app. |

| Social Meta Tag parameters ||
|---|---|
| st | The title to use when the Dynamic Link is shared in a social post. |
| sd | The description to use when the Dynamic Link is shared in a social post. |
| si | The URL to an image related to this link. The image should be at least 300x200 px, and less than 300 KB. |

| Analytics parameters ||
|---|---|
| utm_source utm_medium utm_campaign utm_term utm_content | Google Play analytics parameters. |
| at ct mt pt | iTunes Connect analytics parameters. |

> [!NOTE]
> **Note:** You can combine parameters for Android and iOS to create a Dynamic Link that can be used on both platforms. For example:
>
> ```
> https://example.page.link/?link=https://www.example.com/someresource&apn=com.example.android&amv=3&ibi=com.example.ios&isi=1234567&ius=exampleapp
> ```

## Debugging a URL

You can debug a Dynamic Link by taking a long or short URL and attaching a debug parameter.

```
https://example.page.link/?link=https://www.example.com&d=1
https://example.page.link/WXYZ?d=1
```

| Debug parameter ||
|---|---|
| d | Instead of loading the Dynamic Link, generate a flowchart you can use to preview your Dynamic Links' behavior on different platforms and configurations. |

## Next steps

After you create a Dynamic Link, you need to set up your app to receive Dynamic Links and
send users to the right place in your app after a user opens them.

To receive Dynamic Links in your app, see the documentation for
[iOS](https://firebase.google.com/docs/dynamic-links/ios/receive), [Android](https://firebase.google.com/docs/dynamic-links/android/receive),
[C++](https://firebase.google.com/docs/dynamic-links/cpp/receive), and [Unity](https://firebase.google.com/docs/dynamic-links/unity/receive).