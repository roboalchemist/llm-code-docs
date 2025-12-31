# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder.md.txt

# DynamicLink.AndroidParameters.Builder

# DynamicLink.AndroidParameters.Builder


```
class DynamicLink.AndroidParameters.Builder
```

<br />

*** ** * ** ***

| **This class is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Builder for Android parameters.

## Summary

|                                                                                                                                                                                  ### Public constructors                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ~~[Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#Builder())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                                                                                                |
| ~~[Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#Builder(java.lang.String))~~`(packageName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |

|                                                                       ### Public functions                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DynamicLink.AndroidParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters)                 | ~~[build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#build())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                                                                                                           |
| [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)                                                                                        | ~~[getFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#getFallbackUrl())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                                                                                         |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                        | ~~[getMinimumVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#getMinimumVersion())~~`()` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />                                                                                                   |
| [DynamicLink.AndroidParameters.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder) | ~~[setFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#setFallbackUrl(android.net.Uri))~~`(fallbackUrl: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html)`)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br /> |
| [DynamicLink.AndroidParameters.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder) | ~~[setMinimumVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#setMinimumVersion(int))~~`(minimumVersion: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` **This function is deprecated.** Firebase Dynamic Links is deprecated and should not be used in new projects. <br />    |

## Public constructors

### Builder

```
[Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#Builder())()
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Create Android parameters builder, using the package name of the calling app. The app must be connected to your project from the Overview page of the Firebase console.  

|                                                                          Throws                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| `java.lang.IllegalStateException: `[java.lang.IllegalStateException](https://developer.android.com/reference/kotlin/java/lang/IllegalStateException.html) | if FirebaseApp has not been initialized correctly. |

### Builder

```
[Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#Builder(java.lang.String))(packageName:Â String)
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Create Android parameters builder.  

|                                           Parameters                                            |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `packageName: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The package name of the Android app to use to open the link. The app must be connected to your project from the Overview page of the Firebase console. |

## Public functions

### build

```
funÂ [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#build())():Â DynamicLink.AndroidParameters
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Build AndroidParameters for use with [setAndroidParameters](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.Builder#setAndroidParameters(com.google.firebase.dynamiclinks.DynamicLink.AndroidParameters)).  

### getFallbackUrl

```
funÂ [getFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#getFallbackUrl())():Â Uri
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the link to open on Android if the app isn't installed.  

|                                  Returns                                   |
|----------------------------------------------------------------------------|---------------------------------------------------------|
| [Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html) | the link to open on Android if the app isn't installed. |

### getMinimumVersion

```
funÂ [getMinimumVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#getMinimumVersion())():Â Int
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Returns the minimum version of your app that can open the link.  

|                                  Returns                                   |
|----------------------------------------------------------------------------|---------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | the minimum version of your app that can open the link. |

### setFallbackUrl

```
funÂ [setFallbackUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#setFallbackUrl(android.net.Uri))(fallbackUrl:Â Uri):Â DynamicLink.AndroidParameters.Builder
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the link to open when the app isn't installed. Specify this to do something other than install your app from the Play Store when the app isn't installed, such as open the mobile web version of the content, or display a promotional page for your app.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------|
| `fallbackUrl: `[Uri](https://developer.android.com/reference/kotlin/android/net/Uri.html) | The link to open on Android if the app is not installed. |

### setMinimumVersion

```
funÂ [setMinimumVersion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dynamiclinks/DynamicLink.AndroidParameters.Builder#setMinimumVersion(int))(minimumVersion:Â Int):Â DynamicLink.AndroidParameters.Builder
```
| **This function is deprecated.**   
|
| Firebase Dynamic Links is deprecated and should not be used in new projects. The service will shut down on August 25, 2025. For more information, see [Dynamic Links deprecation documentation](https://firebase.google.com/support/dynamic-links-faq).

Sets the versionCode of the minimum version of your app that can open the link.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|----------------------|
| `minimumVersion: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | The minimum version. |