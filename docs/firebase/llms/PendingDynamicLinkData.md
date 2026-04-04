# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/PendingDynamicLinkData.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData.md.txt

# PendingDynamicLinkData

# PendingDynamicLinkData


```
class PendingDynamicLinkData
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Provides accessor methods to dynamic links data.

## Summary

|                                                                                                                                                                                                                                                                                                                         ### Protected constructors                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#PendingDynamicLinkData(java.lang.String,int,long,android.net.Uri))`(` ` deepLink: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?,` ` minVersion: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`,` ` clickTimestamp: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`,` ` redirectUrl: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?` `)` Create a PendingDynamicLinkData which can be used for testing. |

|                                  ### Public functions                                   |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)            | ~~[getClickTimestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getClickTimestamp())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                                                                                                           |
| [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?`           | ~~[getLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getLink())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                                                                                                                               |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)              | ~~[getMinimumAppVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getMinimumAppVersion())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                                                                                                     |
| [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)`?` | ~~[getUpdateAppIntent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUpdateAppIntent(android.content.Context))~~`(context: `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)`)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html)         | ~~[getUtmParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUtmParameters())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                                                                                                             |

|                                 ### Extension functions                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `operator `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?` | [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData)`.`~~[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component1())~~`()` Destructuring declaration for [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData) to provide link.              |
| `operator `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?` | [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData)`.`~~[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component1())~~`()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.                                                    |
| `operator `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)    | [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData)`.`~~[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component2())~~`()` Destructuring declaration for [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData) to provide minimumAppVersion. |
| `operator `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)    | [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData)`.`~~[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component2())~~`()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.                                                    |
| `operator `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)  | [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData)`.`~~[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component3())~~`()` Destructuring declaration for [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData) to provide clickTimestamp.    |
| `operator `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)  | [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData)`.`~~[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component3())~~`()` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.                                                    |

## Protected constructors

### PendingDynamicLinkData

```
protectedÂ PendingDynamicLinkData(
Â Â Â Â deepLink:Â String?,
Â Â Â Â minVersion:Â Int,
Â Â Â Â clickTimestamp:Â Long,
Â Â Â Â redirectUrl:Â Uri?
)
```

Create a PendingDynamicLinkData which can be used for testing.  

|                                           Parameters                                            |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| `deepLink: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | dynamic link deep link, can be null.                                           |
| `minVersion: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)        | app minimum version. 0 if no minimum version required.                         |
| `clickTimestamp: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)  | timestamp of when the dynamic link was clicked. If zero, will be current time. |

## Public functions

### getClickTimestamp

```
funÂ [getClickTimestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getClickTimestamp())():Â Long
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the time that the user clicked on the Firebase Dynamic Link. This can be used to determine the amount of time that has passed since the user selected the link until the app is launched.  

|                                   Returns                                    |
|------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html) | The number of milliseconds that have elapsed since January 1, 1970. |

### getLink

```
funÂ [getLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getLink())():Â Uri?
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the link parameter of the Firebase Dynamic Link.

This link will be set as data in the launch Intent, see [setData](https://developer.android.com/reference/kotlin/android/content/Intent.html#setData-android.net.Uri-), which will match [android.content.IntentFilter](https://developer.android.com/reference/kotlin/android/content/IntentFilter.html) to deep link into the app.  

|                                    Returns                                    |
|-------------------------------------------------------------------------------|---------------------------------------------|
| [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`?` | The deep link if it exists, null otherwise. |

### getMinimumAppVersion

```
funÂ [getMinimumAppVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getMinimumAppVersion())():Â Int
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the minimum app version requested to process the Firebase Dynamic Link that can be compared directly with [versionCode](https://developer.android.com/reference/kotlin/android/content/pm/PackageInfo.html#versionCode--). If the minimum version code is higher than the installed app version code, the app can upgrade using [getUpdateAppIntent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUpdateAppIntent(android.content.Context)).  

|                                  Returns                                   |
|----------------------------------------------------------------------------|----------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | minimum version code set on the dynamic link, or 0 if not specified. |

### getUpdateAppIntent

```
funÂ [getUpdateAppIntent](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUpdateAppIntent(android.content.Context))(context:Â Context):Â Intent?
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Gets the intent to update the app to the version in the Play Store.

An intent is returned to be used as a parameter to startActivity to launch the Play Store update flow for the app. After update, if the user re-launches the app from the Play Store by selecting the displayed Continue button then the deep link will be set as the data in the re-launch intent and will launch any Activity with an [android.content.IntentFilter](https://developer.android.com/reference/kotlin/android/content/IntentFilter.html) that matches the deeplink. This is the same as the new install flow. The dynamic link returned during initial launch will not be available from [getDynamicLink](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/FirebaseDynamicLinks#getDynamicLink(android.content.Intent)) during the update re-launch.

If the minimum version required by the dynamic link is not greater than the currently installed version, then null is returned.  

|                                         Returns                                         |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html)`?` | - An [Intent](https://developer.android.com/reference/kotlin/android/content/Intent.html) that will launch the Play Store to update the app, or null if the dynamic link minimum version code is not greater than the installed version. |

### getUtmParameters

```
funÂ [getUtmParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#getUtmParameters())():Â Bundle
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html) which contains utm parameters associated with the Firebase Dynamic Link.  

|                                     Returns                                     |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------|
| [Bundle](https://developer.android.com/reference/kotlin/android/os/Bundle.html) | Bundle of utm parameters associated with firebase dynamic link. |

## Extension functions

### component1

```
operatorÂ funÂ PendingDynamicLinkData.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component1())():Â Uri?
```

Destructuring declaration for [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData) to provide link.  

### component1

```
operatorÂ funÂ PendingDynamicLinkData.[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component1())():Â Uri?
```
| **This function is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData) to provide link.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

### component2

```
operatorÂ funÂ PendingDynamicLinkData.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component2())():Â Int
```

Destructuring declaration for [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData) to provide minimumAppVersion.  

### component2

```
operatorÂ funÂ PendingDynamicLinkData.[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component2())():Â Int
```
| **This function is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData) to provide minimumAppVersion.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)  

### component3

```
operatorÂ funÂ PendingDynamicLinkData.[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component3())():Â Long
```

Destructuring declaration for [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData) to provide clickTimestamp.  

### component3

```
operatorÂ funÂ PendingDynamicLinkData.[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData#(com.google.firebase.dynamiclinks.PendingDynamicLinkData).component3())():Â Long
```
| **This function is deprecated.**   
| Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Destructuring declaration for [PendingDynamicLinkData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/PendingDynamicLinkData) to provide clickTimestamp.

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to their respective main modules, and the Kotlin extension (KTX) APIs in `com.google.firebase.firebase-dynamic-links-ktx` are now deprecated. As early as April 2024, we'll no longer release KTX modules. For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)