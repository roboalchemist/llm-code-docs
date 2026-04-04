# Source: https://firebase.google.com/docs/dynamic-links/android/create.md.txt

> [!NOTE]
> **Note:** Firebase Dynamic Links is *deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the [migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service) and see the [Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq) for more information.

You can create short or long Dynamic Links with the Firebase Dynamic Links Builder API.
This API accepts either a long Dynamic Link or an object containing Dynamic Link
parameters, and returns URLs like the following examples:

```
https://example.com/link/WXYZ
https://example.page.link/WXYZ
```

## Set up Firebase and the Dynamic Links SDK

Before you can create Dynamic Links in your Android app, you must include the
Firebase SDK. If your app is set up to receive Dynamic Links, you have already
completed these steps and you can skip this section.

1. If you haven't already,
   [add Firebase to your Android project](https://firebase.google.com/docs/android/setup).

   When you register your app, specify your SHA-1 signing key. If you use
   App Links, also specify your SHA-256 key.
2.


   In your **module (app-level) Gradle file**
   (usually `<project>/<app-module>/build.gradle.kts` or
   `<project>/<app-module>/build.gradle`),
   add the dependency for the Dynamic Links library for Android. We recommend using the
   [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom)
   to control library versioning.


   For an optimal experience with Dynamic Links, we recommend
   [enabling Google Analytics](https://support.google.com/firebase/answer/9289399#linkga)
   in your Firebase project and adding the Firebase SDK for Google Analytics to your app.

   ```
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

       // Add the dependencies for the Dynamic Links and Analytics libraries
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation 'com.google.firebase:firebase-dynamic-links'
       implementation 'com.google.firebase:firebase-analytics'
   }
   ```

   By using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
   your app will always use compatible versions of Firebase Android libraries.
   *(Alternative)*
   Add Firebase library dependencies *without* using the BoM

   If you choose not to use the Firebase BoM, you must specify each Firebase library version
   in its dependency line.

   **Note that if you use *multiple* Firebase libraries in your app, we strongly
   recommend using the BoM to manage library versions, which ensures that all versions are
   compatible.**

   ```groovy
   dependencies {
       // Add the dependencies for the Dynamic Links and Analytics libraries
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation 'com.google.firebase:firebase-dynamic-links:22.1.0'
       implementation 'com.google.firebase:firebase-analytics:23.0.0'
   }
   ```
3. In the Firebase console, open the **Dynamic Links** section.
4. If you have not already accepted the terms of service and set a domain
   for your Dynamic Links, do so when prompted.

   If you already have a Dynamic Links domain, take note of it. You need to
   provide a Dynamic Links domain when you programmatically create Dynamic Links.

   ![](https://firebase.google.com/static/docs/dynamic-links/images/dynamic-links-domain.png)
5. **Recommended** : Specify the URL patterns allowed in your deep links and fallback links. By doing so, you prevent unauthorized parties from creating Dynamic Links that redirect from your domain to sites you don't control. See [Allow specific URL patterns](https://firebase.google.com/docs/dynamic-links/allow-specific-url-patterns).

## Use the Firebase console

If you want to generate a single Dynamic Link, either for testing purposes, or for your marketing team
to easily create a link that can be used in something like a social media post, the simplest way would
be to visit the [Firebase console](https://console.firebase.google.com/project/_/durablelinks/links/)
and create one manually following the step-by-step form.

## Create a Dynamic Link from parameters

To create a Dynamic Link, create a new `DynamicLink` object with its
Builder, specifying the Dynamic Link parameters with the Builder methods. Then, call
`buildDynamicLink` or `buildShortDynamicLink`.

The following minimal example creates a long Dynamic Link to
`https://www.example.com/` that opens with your Android app on Android
and the app `com.example.ios` on iOS:

### Kotlin

```kotlin
val dynamicLink = Firebase.dynamicLinks.dynamicLink {
    link = Uri.parse("https://www.example.com/")
    domainUriPrefix = "https://example.page.link"
    // Open links with this app on Android
    androidParameters { }
    // Open links with com.example.ios on iOS
    iosParameters("com.example.ios") { }
}

val dynamicLinkUri = dynamicLink.urihttps://github.com/firebase/snippets-android/blob/46a5ec5445bb166f8078895750ff5e9debc8e1dc/dynamic-links/app/src/main/java/com/google/firebase/quickstart/dynamiclinks/kotlin/MainActivity.kt#L57-L66
```

### Java

```java
DynamicLink dynamicLink = FirebaseDynamicLinks.getInstance().createDynamicLink()
        .setLink(Uri.parse("https://www.example.com/"))
        .setDomainUriPrefix("https://example.page.link")
        // Open links with this app on Android
        .setAndroidParameters(new DynamicLink.AndroidParameters.Builder().build())
        // Open links with com.example.ios on iOS
        .setIosParameters(new DynamicLink.IosParameters.Builder("com.example.ios").build())
        .buildDynamicLink();

Uri dynamicLinkUri = dynamicLink.getUri();
```

To create a short Dynamic Link, build a `DynamicLink` the same way, and
then call `buildShortDynamicLink`. Building a short link requires a
network call, so instead of directly returning the link,
`buildShortDynamicLink` returns a `Task`, which makes
the short link available when the request completes. For example:

### Kotlin

```kotlin
val shortLinkTask = Firebase.dynamicLinks.shortLinkAsync {
    link = Uri.parse("https://www.example.com/")
    domainUriPrefix = "https://example.page.link"
    // Set parameters
    // ...
}.addOnSuccessListener { (shortLink, flowchartLink) ->
    // You'll need to import com.google.firebase.dynamiclinks.component1 and
    // com.google.firebase.dynamiclinks.component2

    // Short link created
    processShortLink(shortLink, flowchartLink)
}.addOnFailureListener {
    // Error
    // ...
}
```

### Java

```java
Task<ShortDynamicLink> shortLinkTask = FirebaseDynamicLinks.getInstance().createDynamicLink()
        .setLink(Uri.parse("https://www.example.com/"))
        .setDomainUriPrefix("https://example.page.link")
        // Set parameters
        // ...
        .buildShortDynamicLink()
        .addOnCompleteListener(this, new OnCompleteListener<ShortDynamicLink>() {
            @Override
            public void onComplete(@NonNull Task<ShortDynamicLink> task) {
                if (task.isSuccessful()) {
                    // Short link created
                    Uri shortLink = task.getResult().getShortLink();
                    Uri flowchartLink = task.getResult().getPreviewLink();
                } else {
                    // Error
                    // ...
                }
            }
        });
```

By default, short Dynamic Links are generated with 17-character link suffixes that
make it extremely unlikely that someone can guess a valid Dynamic Link. If, for
your use case, there's no harm in someone successfully guessing a short link,
you might prefer to generate suffixes that are only as long as necessary to be
unique, which you can do by passing `ShortDynamicLink.Suffix.SHORT`
to the `buildShortDynamicLink` method:

### Kotlin

```kotlin
val shortLinkTask = Firebase.dynamicLinks.shortLinkAsync(ShortDynamicLink.Suffix.SHORT) {
    // Set parameters
    // ...
}
```

### Java

```java
Task<ShortDynamicLink> shortLinkTask = FirebaseDynamicLinks.getInstance().createDynamicLink()
        // ...
        .buildShortDynamicLink(ShortDynamicLink.Suffix.SHORT);
        // ...https://github.com/firebase/snippets-android/blob/46a5ec5445bb166f8078895750ff5e9debc8e1dc/dynamic-links/app/src/main/java/com/google/firebase/quickstart/dynamiclinks/MainActivity.java#L174-L177
```

### Dynamic Link parameters

You can use the Dynamic Link Builder API to create Dynamic Links with any of the
supported parameters. See the [API reference](https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink) for details.

The following example creates a Dynamic Link with several common parameters
set:

### Kotlin

```kotlin
val dynamicLink = Firebase.dynamicLinks.dynamicLink { // or Firebase.dynamicLinks.shortLinkAsync
    link = Uri.parse("https://www.example.com/")
    domainUriPrefix = "https://example.page.link"
    androidParameters("com.example.android") {
        minimumVersion = 125
    }
    iosParameters("com.example.ios") {
        appStoreId = "123456789"
        minimumVersion = "1.0.1"
    }
    googleAnalyticsParameters {
        source = "orkut"
        medium = "social"
        campaign = "example-promo"
    }
    itunesConnectAnalyticsParameters {
        providerToken = "123456"
        campaignToken = "example-promo"
    }
    socialMetaTagParameters {
        title = "Example of a Dynamic Link"
        description = "This link works whether the app is installed or not!"
    }
}
```

### Java

```java
DynamicLink dynamicLink = FirebaseDynamicLinks.getInstance().createDynamicLink()
        .setLink(Uri.parse("https://www.example.com/"))
        .setDomainUriPrefix("https://example.page.link")
        .setAndroidParameters(
                new DynamicLink.AndroidParameters.Builder("com.example.android")
                        .setMinimumVersion(125)
                        .build())
        .setIosParameters(
                new DynamicLink.IosParameters.Builder("com.example.ios")
                        .setAppStoreId("123456789")
                        .setMinimumVersion("1.0.1")
                        .build())
        .setGoogleAnalyticsParameters(
                new DynamicLink.GoogleAnalyticsParameters.Builder()
                        .setSource("orkut")
                        .setMedium("social")
                        .setCampaign("example-promo")
                        .build())
        .setItunesConnectAnalyticsParameters(
                new DynamicLink.ItunesConnectAnalyticsParameters.Builder()
                        .setProviderToken("123456")
                        .setCampaignToken("example-promo")
                        .build())
        .setSocialMetaTagParameters(
                new DynamicLink.SocialMetaTagParameters.Builder()
                        .setTitle("Example of a Dynamic Link")
                        .setDescription("This link works whether the app is installed or not!")
                        .build())
        .buildDynamicLink();  // Or buildShortDynamicLink()https://github.com/firebase/snippets-android/blob/46a5ec5445bb166f8078895750ff5e9debc8e1dc/dynamic-links/app/src/main/java/com/google/firebase/quickstart/dynamiclinks/MainActivity.java#L95-L123
```

You can set Dynamic Link parameters with the following methods:

| DynamicLink parameters ||
|---|---|
| setLink | The link your app will open. Specify a URL that your app can handle, typically the app's content or payload, which initiates app-specific logic (such as crediting the user with a coupon or displaying a welcome screen). This link must be a well-formatted URL, be properly URL-encoded, use either HTTP or HTTPS, and cannot be another Dynamic Link. > [!NOTE] > When users open a Dynamic Link on a desktop web browser, they will load this URL (unless the `ofl` parameter is specified). If you don't have a web equivalent to the linked content, the URL doesn't need to point to a valid web resource. In this situation, you should set up a redirect from this URL to, for example, your home page. |
| setDomainUriPrefix | Your Dynamic Link URL prefix, which you can find in the Firebase console. A Dynamic Link domain looks like the following examples: ``` https://example.com/link https://example.page.link ``` |

| AndroidParameters ||
|---|---|
| setFallbackUrl | The link to open when the app isn't installed. Specify this to do something other than install your app from the Play Store when the app isn't installed, such as open the mobile web version of the content, or display a promotional page for your app. |
| setMinimumVersion | The [`versionCode`](http://developer.android.com/tools/publishing/versioning.html#appversioning) of the minimum version of your app that can open the link. If the installed app is an older version, the user is taken to the Play Store to upgrade the app. |

| IosParameters ||
|---|---|
| setAppStoreId | Your app's App Store ID, used to send users to the App Store when the app isn't installed |
| setFallbackUrl | The link to open when the app isn't installed. Specify this to do something other than install your app from the App Store when the app isn't installed, such as open the mobile web version of the content, or display a promotional page for your app. |
| setCustomScheme | Your app's custom URL scheme, if defined to be something other than your app's bundle ID |
| setIpadFallbackUrl | The link to open on iPads when the app isn't installed. Specify this to do something other than install your app from the App Store when the app isn't installed, such as open the web version of the content, or display a promotional page for your app. |
| setIpadBundleId | The bundle ID of the iOS app to use on iPads to open the link. The app must be connected to your project from the Overview page of the Firebase console. |
| setMinimumVersion | The [version number](https://developer.apple.com/library/content/technotes/tn2420/_index.html) of the minimum version of your app that can open the link. This flag is passed to your app when it is opened, and your app must decide what to do with it. |

| NavigationInfoParameters ||
|---|---|
| setForcedRedirectEnabled | If set to '1', skip the app preview page when the Dynamic Link is opened, and instead redirect to the app or store. The app preview page (enabled by default) can more reliably send users to the most appropriate destination when they open Dynamic Links in apps; however, if you expect a Dynamic Link to be opened only in apps that can open Dynamic Links reliably without this page, you can disable it with this parameter. This parameter will affect the behavior of the Dynamic Link only on iOS. |

| SocialMetaTagParameters ||
|---|---|
| setTitle | The title to use when the Dynamic Link is shared in a social post. |
| setDescription | The description to use when the Dynamic Link is shared in a social post. |
| setImageUrl | The URL to an image related to this link. The image should be at least 300x200 px, and less than 300 KB. |

| GoogleAnalyticsParameters ||
|---|---|
| setSource setMedium setCampaign setTerm setContent | Google Play analytics parameters. These parameters (`utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`) are passed on to the Play Store as well as appended to the link payload. |

| ItunesConnectAnalyticsParameters ||
|---|---|
| setProviderToken setAffiliateToken setCampaignToken | iTunes Connect analytics parameters. These parameters (`pt`, `at`, `ct`) are passed to the App Store. |

## Shorten a long Dynamic Link

To shorten a long Dynamic Link, specify the URL of the Dynamic Link using
`setLongLink` instead of setting parameters with the other builder
methods:

### Kotlin

```kotlin
val shortLinkTask = Firebase.dynamicLinks.shortLinkAsync {
    longLink = Uri.parse(
        "https://example.page.link/?link=" +
            "https://www.example.com/&apn=com.example.android&ibn=com.example.ios",
    )
}.addOnSuccessListener { (shortLink, flowChartLink) ->
    // You'll need to import com.google.firebase.dynamiclinks.component1 and
    // com.google.firebase.dynamiclinks.component2

    // Short link created
    processShortLink(shortLink, flowChartLink)
}.addOnFailureListener {
    // Error
    // ...
}
```

### Java

```java
Task<ShortDynamicLink> shortLinkTask = FirebaseDynamicLinks.getInstance().createDynamicLink()
        .setLongLink(Uri.parse("https://example.page.link/?link=https://www.example.com/&apn=com.example.android&ibn=com.example.ios"))
        .buildShortDynamicLink()
        .addOnCompleteListener(this, new OnCompleteListener<ShortDynamicLink>() {
            @Override
            public void onComplete(@NonNull Task<ShortDynamicLink> task) {
                if (task.isSuccessful()) {
                    // Short link created
                    Uri shortLink = task.getResult().getShortLink();
                    Uri flowchartLink = task.getResult().getPreviewLink();
                } else {
                    // Error
                    // ...
                }
            }
        });
```