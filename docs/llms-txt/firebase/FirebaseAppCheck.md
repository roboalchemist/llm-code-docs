# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.md.txt

# FirebaseAppCheck

# FirebaseAppCheck


```
abstract class FirebaseAppCheck : InteropAppCheckTokenProvider
```

<br />

*** ** * ** ***

## Summary

|                                                                         ### Nested types                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `interface `[FirebaseAppCheck.AppCheckListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener) |

|                                                          ### Public constructors                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------|
| [FirebaseAppCheck](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#FirebaseAppCheck())`()` |

|                                                                                                     ### Public functions                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                       | [addAppCheckListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#addAppCheckListener(com.google.firebase.appcheck.FirebaseAppCheck.AppCheckListener))`(listener: `[FirebaseAppCheck.AppCheckListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener)`)` Registers an [AppCheckListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener) to changes in the token state.                                                                                                                                                                                     |
| `abstract `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AppCheckToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken)`!>` | [getAppCheckToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#getAppCheckToken(boolean))`(forceRefresh: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Requests a Firebase App Check token.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `java-static `[FirebaseAppCheck](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck)                                                                                             | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#getInstance())`()` Gets the default instance of `FirebaseAppCheck`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `java-static `[FirebaseAppCheck](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck)                                                                                             | [getInstance](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#getInstance(com.google.firebase.FirebaseApp))`(firebaseApp: `[FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)`)` Gets the instance of `FirebaseAppCheck` associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) instance.                                                                                                                                                                                                                                                                                          |
| `abstract `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AppCheckToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken)`!>` | [getLimitedUseAppCheckToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#getLimitedUseAppCheckToken())`()` Requests a Firebase App Check token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `abstract `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                       | [installAppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#installAppCheckProviderFactory(com.google.firebase.appcheck.AppCheckProviderFactory))`(factory: `[AppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory)`)` Installs the given [AppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory), overwriting any that were previously associated with this `FirebaseAppCheck` instance.                                                                                                                                  |
| `abstract `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                       | [installAppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#installAppCheckProviderFactory(com.google.firebase.appcheck.AppCheckProviderFactory,boolean))`(` ` factory: `[AppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory)`,` ` isTokenAutoRefreshEnabled: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) `)` Installs the given [AppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory), overwriting any that were previously associated with this `FirebaseAppCheck` instance. |
| `abstract `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                       | [removeAppCheckListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#removeAppCheckListener(com.google.firebase.appcheck.FirebaseAppCheck.AppCheckListener))`(listener: `[FirebaseAppCheck.AppCheckListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener)`)` Unregisters an [AppCheckListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener) to changes in the token state.                                                                                                                                                                             |
| `abstract `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                       | [setTokenAutoRefreshEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#setTokenAutoRefreshEnabled(boolean))`(isTokenAutoRefreshEnabled: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)` Sets the `isTokenAutoRefreshEnabled` flag.                                                                                                                                                                                                                                                                                                                                                                                                                      |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ### Inherited functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.appcheck.interop.InteropAppCheckTokenProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider) |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `abstract `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                                    | [addAppCheckTokenListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider#addAppCheckTokenListener(com.google.firebase.appcheck.interop.AppCheckTokenListener))`(p: `[AppCheckTokenListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/AppCheckTokenListener)`!)`       | | `abstract `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AppCheckTokenResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckTokenResult)`!>!` | [getLimitedUseToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider#getLimitedUseToken())`()`                                                                                                                                                                                                                        | | `abstract `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[AppCheckTokenResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckTokenResult)`!>!` | [getToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider#getToken(boolean))`(p: `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`)`                                                                                                                                              | | `abstract `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)                                                                                                                                                    | [removeAppCheckTokenListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider#removeAppCheckTokenListener(com.google.firebase.appcheck.interop.AppCheckTokenListener))`(p: `[AppCheckTokenListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/AppCheckTokenListener)`!)` | |

## Public constructors

### FirebaseAppCheck

```
FirebaseAppCheck()
```  

## Public functions

### addAppCheckListener

```
abstractÂ funÂ addAppCheckListener(listener:Â FirebaseAppCheck.AppCheckListener):Â Unit
```

Registers an [AppCheckListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener) to changes in the token state. This method should be used ONLY if you need to authorize requests to a non-Firebase backend. Requests to Firebase backends are authorized automatically if configured.  

### getAppCheckToken

```
abstractÂ funÂ getAppCheckToken(forceRefresh:Â Boolean):Â Task<AppCheckToken!>
```

Requests a Firebase App Check token. This method should be used ONLY if you need to authorize requests to a non-Firebase backend. Requests to Firebase backends are authorized automatically if configured.

If your non-Firebase backend exposes a sensitive or expensive endpoint that has low traffic volume, consider protecting it with [Replay Protection](https://firebase.google.com/docs/app-check/custom-resource-backend#replay-protection). In this case, use [getLimitedUseAppCheckToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#getLimitedUseAppCheckToken()) instead to obtain a limited-use token.  

### getInstance

```
java-staticÂ funÂ getInstance():Â FirebaseAppCheck
```

Gets the default instance of `FirebaseAppCheck`.  

### getInstance

```
java-staticÂ funÂ getInstance(firebaseApp:Â FirebaseApp):Â FirebaseAppCheck
```

Gets the instance of `FirebaseAppCheck` associated with the given [FirebaseApp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp) instance.  

### getLimitedUseAppCheckToken

```
abstractÂ funÂ getLimitedUseAppCheckToken():Â Task<AppCheckToken!>
```

Requests a Firebase App Check token. This method should be used ONLY if you need to authorize requests to a non-Firebase backend.

Returns limited-use tokens that are intended for use with your non-Firebase backend endpoints that are protected with [Replay Protection](https://firebase.google.com/docs/app-check/custom-resource-backend#replay-protection). This method does not affect the token generation behavior of the [getAppCheckToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#getAppCheckToken(boolean)) method.  

### installAppCheckProviderFactory

```
abstractÂ funÂ installAppCheckProviderFactory(factory:Â AppCheckProviderFactory):Â Unit
```

Installs the given [AppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory), overwriting any that were previously associated with this `FirebaseAppCheck` instance. Any [AppCheckTokenListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/AppCheckTokenListener)s attached to this `FirebaseAppCheck` instance will be transferred from existing factories to the newly installed one.

Automatic token refreshing will only occur if the global `
isDataCollectionDefaultEnabled` flag is set to true. To allow automatic token refreshing for Firebase App Check without changing the `isDataCollectionDefaultEnabled` flag for other Firebase SDKs, use [installAppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#installAppCheckProviderFactory(com.google.firebase.appcheck.AppCheckProviderFactory,boolean)) instead or call [setTokenAutoRefreshEnabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#setTokenAutoRefreshEnabled(boolean)) after installing the `
factory`.  

### installAppCheckProviderFactory

```
abstractÂ funÂ installAppCheckProviderFactory(
Â Â Â Â factory:Â AppCheckProviderFactory,
Â Â Â Â isTokenAutoRefreshEnabled:Â Boolean
):Â Unit
```

Installs the given [AppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory), overwriting any that were previously associated with this `FirebaseAppCheck` instance. Any [AppCheckTokenListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/AppCheckTokenListener)s attached to this `FirebaseAppCheck` instance will be transferred from existing factories to the newly installed one.

Automatic token refreshing will only occur if the `isTokenAutoRefreshEnabled` field is set to true. To use the global `isDataCollectionDefaultEnabled` flag for determining automatic token refreshing, call [installAppCheckProviderFactory](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#installAppCheckProviderFactory(com.google.firebase.appcheck.AppCheckProviderFactory)) instead.  

### removeAppCheckListener

```
abstractÂ funÂ removeAppCheckListener(listener:Â FirebaseAppCheck.AppCheckListener):Â Unit
```

Unregisters an [AppCheckListener](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener) to changes in the token state.  

### setTokenAutoRefreshEnabled

```
abstractÂ funÂ setTokenAutoRefreshEnabled(isTokenAutoRefreshEnabled:Â Boolean):Â Unit
```

Sets the `isTokenAutoRefreshEnabled` flag.