# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/FirebaseDynamicLinks.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks.md.txt

# FirebaseDynamicLinks

# FirebaseDynamicLinks


```
abstract class FirebaseDynamicLinks
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Provides access to dynamic links that are received by an app at launch.

When a dynamic link is clicked, the app is launched, or if the app is not yet installed, the user is directed to the Play Store to install and launch the app. In both cases the dynamic link made available to the app using [getDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent)). An [android.content.IntentFilter](https://developer.android.com/reference/kotlin/android/content/IntentFilter.html) for the deeplink can also be used to launch the app directly into a targeted [android.app.Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html) or otherwise will start in the main launch Activity.

Dynamic link data returned from [getDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent)) can be accessed using the [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData) class.

[Android App Links](https://developer.android.com/training/app-links/index.html) can also be used to launch the app with dynamic links by registering to handle your Dynamic Links in your app. The guide for setting up your app to receive Firebase Dynamic Links as an App Link can be found on the Android [Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links/android/receive#app_links) site.

Dynamic link data is available from the app launch intent. This data may include data for dynamic link extensions such as app invites.

## Summary

|                                                                  ### Public constructors                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseDynamicLinks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#FirebaseDynamicLinks())`()` |

|                                                                                                                ### Public functions                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract `[DynamicLink.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder)                                                                                                            | ~~[createDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#createDynamicLink())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                                                                                                                   |
| `abstract `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData)`!>` | ~~[getDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.net.Uri))~~`(dynamicLinkUri: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                              |
| `abstract `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData)`!>` | ~~[getDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent))~~`(intent: `[Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)`?)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                    |
| `synchronized java-static `[FirebaseDynamicLinks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks)                                                                                          | ~~[getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getInstance())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                                                                                                                               |
| `synchronized java-static `[FirebaseDynamicLinks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks)                                                                                          | ~~[getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getInstance(com.google.firebase.FirebaseApp))~~`(firebaseApp: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

|                                                                                                   ### Extension functions                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink)                                                                                                               | [FirebaseDynamicLinks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks)`.`~~[dynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1))~~`(init: `[DynamicLink.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder)`.() `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)` Creates a [DynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink) object initialized using the [init](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1)) function.                                                                                                                                |
| [DynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink)                                                                                                               | [FirebaseDynamicLinks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks)`.`~~[dynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1))~~`(init: `[DynamicLink.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder)`.() `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.                                                                                                                                                                                                                                                                                                                                                   |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink)`>` | [FirebaseDynamicLinks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks)`.`~~[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1))~~`(init: `[DynamicLink.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder)`.() `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)` Creates a [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) object initialized using the [init](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1)) function.                                                                                                             |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink)`>` | [FirebaseDynamicLinks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks)`.`~~[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1))~~`(suffix: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`, init: `[DynamicLink.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder)`.() `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)` Creates a [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) object initialized using the [init](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1)) function. |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink)`>` | [FirebaseDynamicLinks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks)`.`~~[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1))~~`(init: `[DynamicLink.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder)`.() `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.                                                                                                                                                                                                                                                                                                                                             |
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink)`>` | [FirebaseDynamicLinks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks)`.`~~[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1))~~`(suffix: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`, init: `[DynamicLink.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder)`.() `->` `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)`)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.                                                                                                                                                                                                                                            |

## Public constructors

### FirebaseDynamicLinks

```
FirebaseDynamicLinks()
```  

## Public functions

### createDynamicLink

```
abstractÂ funÂ [createDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#createDynamicLink())():Â DynamicLink.Builder
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Create a long or short Dynamic Link.  

|                                                            Returns                                                            |
|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| [DynamicLink.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder) | Builder to create the Dynamic Link. |

### getDynamicLink

```
abstractÂ funÂ [getDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.net.Uri))(dynamicLinkUri:Â Uri):Â Task<PendingDynamicLinkData!>
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Determine if the app has a pending dynamic link and provide access to the dynamic link parameters. A pending dynamic link may have been previously captured when a user clicked on a dynamic link, or may be present in the dynamicLinkUri parameter. If both are present, the previously captured dynamic link will take precedence. The captured data will be removed after first access.

This method provides the same functionality as [getDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent)) except the Uri is provided in place of the [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html).  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|-------------------------------------|
| `dynamicLinkUri: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html) | - A uri that may be a dynamic link. |

|                                                                                                                 Returns                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData)`!>` | Task where [isSuccessful](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isSuccessful--) is true when processing is completed successfully and either a dynamic link is returned, or null if a dynamic link is not previously captured or is in the Uri. [isSuccessful](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isSuccessful--) will only be false when a processing error occurs. |

### getDynamicLink

```
abstractÂ funÂ [getDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent))(intent:Â Intent?):Â Task<PendingDynamicLinkData!>
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Determine if the app has a pending dynamic link and provide access to the dynamic link parameters. A pending dynamic link may have been previously captured when a user clicked on a dynamic link, or may be present in the intent.

When a dynamic link is clicked by the user, in most cases it is captured when clicked and stored until accessed by [getDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent)) and returned as the of the [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html). If the dynamic link was not captured, as is the case when App Links launches the app, then the dynamic link is provided in the [getData](https://developer.android.com/reference/kotlin/android/content/Intent.html#getData--). The intent data is then processed to retrieve the dynamic link data. If the dynamic links is both captured and is present in the intent, then the captured data will take precedence. The captured data will be removed after first access.

The intent parameter should be the intent that launched the application, or can be null if the intent does not include the dynamic link. A non-null intent is necessary only when the app is launched directly using the dynamic link, such as when using [App Links](https://developer.android.com/training/app-links/index.html). The app must configure an [android.content.IntentFilter](https://developer.android.com/reference/kotlin/android/content/IntentFilter.html) to override the default capture processing when the link is clicked.

In the callback the [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData) is returned in [addOnSuccessListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnSuccessListener-com.google.android.gms.tasks.OnSuccessListener&lt;? super TResult&gt;-) or [addOnCompleteListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#addOnCompleteListener-android.app.Activity-com.google.android.gms.tasks.OnCompleteListener&lt;TResult&gt;-) which returns the most recently clicked dynamic link, or null if a dynamic link was not pending as captured data or in the intent.

If processing could not be completed due to an error, then [OnFailureListener](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnFailureListener.html) will be called. Notice that in the case a pending dynamic link is not present, then [isSuccessful](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html#isSuccessful--) will be true and the returned [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData) will be null as this is normal processing and not an error condition.

If a dynamic link, the call will also send FirebaseAnalytics dynamic link event.  

### getInstance

```
synchronizedÂ java-staticÂ funÂ [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getInstance())():Â FirebaseDynamicLinks
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns an instance of [FirebaseDynamicLinks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks).

The default [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) instance must have been initialized before this function is called. See [FirebaseApp](https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp).  

### getInstance

```
synchronizedÂ java-staticÂ funÂ [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getInstance(com.google.firebase.FirebaseApp))(firebaseApp:Â FirebaseApp):Â FirebaseDynamicLinks
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns an instance of [FirebaseDynamicLinks](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks) for the provided firebaseApp.  

## Extension functions

### dynamicLink

```
funÂ FirebaseDynamicLinks.[dynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1))(init:Â DynamicLink.Builder.() -> Unit):Â DynamicLink
```

Creates a [DynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink) object initialized using the [init](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1)) function.  

### dynamicLink

```
funÂ FirebaseDynamicLinks.[dynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1))(init:Â DynamicLink.Builder.() -> Unit):Â DynamicLink
```
| **This function is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a [DynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink) object initialized using the [init](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).dynamicLink(kotlin.Function1)) function.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

### shortLinkAsync

```
funÂ FirebaseDynamicLinks.[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1))(init:Â DynamicLink.Builder.() -> Unit):Â Task<ShortDynamicLink>
```

Creates a [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) object initialized using the [init](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1)) function.  

### shortLinkAsync

```
funÂ FirebaseDynamicLinks.[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1))(suffix:Â Int,Â init:Â DynamicLink.Builder.() -> Unit):Â Task<ShortDynamicLink>
```

Creates a [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) object initialized using the [init](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1)) function.  

### shortLinkAsync

```
funÂ FirebaseDynamicLinks.[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1))(init:Â DynamicLink.Builder.() -> Unit):Â Task<ShortDynamicLink>
```
| **This function is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) object initialized using the [init](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Function1)) function.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

### shortLinkAsync

```
funÂ FirebaseDynamicLinks.[shortLinkAsync](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1))(suffix:Â Int,Â init:Â DynamicLink.Builder.() -> Unit):Â Task<ShortDynamicLink>
```
| **This function is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Creates a [ShortDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ShortDynamicLink) object initialized using the [init](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/ktx/package-summary#(com.google.firebase.dynamiclinks.FirebaseDynamicLinks).shortLinkAsync(kotlin.Int,kotlin.Function1)) function.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)