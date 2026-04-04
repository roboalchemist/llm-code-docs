# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.md.txt

# FirebaseAppCheck

# FirebaseAppCheck


```
abstract class FirebaseAppCheck : InteropAppCheckTokenProvider
```

<br />

*** ** * ** ***

## Summary

| ### Nested types |
|---|
| `interface https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#FirebaseAppCheck()()` |

| ### Public functions |
|---|---|
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#addAppCheckListener(com.google.firebase.appcheck.FirebaseAppCheck.AppCheckListener)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener)` Registers an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener` to changes in the token state. |
| `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#getAppCheckToken(boolean)(forceRefresh: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Requests a Firebase App Check token. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#getInstance()()` Gets the default instance of `FirebaseAppCheck`. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#getInstance(com.google.firebase.FirebaseApp)(firebaseApp: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Gets the instance of `FirebaseAppCheck` associated with the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` instance. |
| `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#getLimitedUseAppCheckToken()()` Requests a Firebase App Check token. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#installAppCheckProviderFactory(com.google.firebase.appcheck.AppCheckProviderFactory)(factory: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory)` Installs the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory`, overwriting any that were previously associated with this `FirebaseAppCheck` instance. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#installAppCheckProviderFactory(com.google.firebase.appcheck.AppCheckProviderFactory,boolean)( factory: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory, isTokenAutoRefreshEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html )` Installs the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory`, overwriting any that were previously associated with this `FirebaseAppCheck` instance. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#removeAppCheckListener(com.google.firebase.appcheck.FirebaseAppCheck.AppCheckListener)(listener: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener)` Unregisters an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener` to changes in the token state. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#setTokenAutoRefreshEnabled(boolean)(isTokenAutoRefreshEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Sets the `isTokenAutoRefreshEnabled` flag. |

| ### Inherited functions |
|---|
| From [com.google.firebase.appcheck.interop.InteropAppCheckTokenProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider#addAppCheckTokenListener(com.google.firebase.appcheck.interop.AppCheckTokenListener)(p: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/AppCheckTokenListener!)` | | `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckTokenResult!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider#getLimitedUseToken()()` | | `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckTokenResult!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider#getToken(boolean)(p: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider#removeAppCheckTokenListener(com.google.firebase.appcheck.interop.AppCheckTokenListener)(p: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/AppCheckTokenListener!)` | |

## Public constructors

### FirebaseAppCheck

```
FirebaseAppCheck()
```

## Public functions

### addAppCheckListener

```
abstract fun addAppCheckListener(listener: FirebaseAppCheck.AppCheckListener): Unit
```

Registers an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener` to changes in the token state. This method should be used ONLY if you need to authorize requests to a non-Firebase backend. Requests to Firebase backends are authorized automatically if configured.

### getAppCheckToken

```
abstract fun getAppCheckToken(forceRefresh: Boolean): Task<AppCheckToken!>
```

Requests a Firebase App Check token. This method should be used ONLY if you need to authorize requests to a non-Firebase backend. Requests to Firebase backends are authorized automatically if configured.

If your non-Firebase backend exposes a sensitive or expensive endpoint that has low traffic volume, consider protecting it with [Replay Protection](https://firebase.google.com/docs/app-check/custom-resource-backend#replay-protection). In this case, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#getLimitedUseAppCheckToken()` instead to obtain a limited-use token.

### getInstance

```
java-static fun getInstance(): FirebaseAppCheck
```

Gets the default instance of `FirebaseAppCheck`.

### getInstance

```
java-static fun getInstance(firebaseApp: FirebaseApp): FirebaseAppCheck
```

Gets the instance of `FirebaseAppCheck` associated with the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` instance.

### getLimitedUseAppCheckToken

```
abstract fun getLimitedUseAppCheckToken(): Task<AppCheckToken!>
```

Requests a Firebase App Check token. This method should be used ONLY if you need to authorize requests to a non-Firebase backend.

Returns limited-use tokens that are intended for use with your non-Firebase backend endpoints that are protected with [Replay Protection](https://firebase.google.com/docs/app-check/custom-resource-backend#replay-protection). This method does not affect the token generation behavior of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#getAppCheckToken(boolean)` method.

### installAppCheckProviderFactory

```
abstract fun installAppCheckProviderFactory(factory: AppCheckProviderFactory): Unit
```

Installs the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory`, overwriting any that were previously associated with this `FirebaseAppCheck` instance. Any `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/AppCheckTokenListener`s attached to this `FirebaseAppCheck` instance will be transferred from existing factories to the newly installed one.

Automatic token refreshing will only occur if the global `
isDataCollectionDefaultEnabled` flag is set to true. To allow automatic token refreshing for Firebase App Check without changing the `isDataCollectionDefaultEnabled` flag for other Firebase SDKs, use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#installAppCheckProviderFactory(com.google.firebase.appcheck.AppCheckProviderFactory,boolean)` instead or call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#setTokenAutoRefreshEnabled(boolean)` after installing the `
factory`.

### installAppCheckProviderFactory

```
abstract fun installAppCheckProviderFactory(
    factory: AppCheckProviderFactory,
    isTokenAutoRefreshEnabled: Boolean
): Unit
```

Installs the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckProviderFactory`, overwriting any that were previously associated with this `FirebaseAppCheck` instance. Any `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/interop/AppCheckTokenListener`s attached to this `FirebaseAppCheck` instance will be transferred from existing factories to the newly installed one.

Automatic token refreshing will only occur if the `isTokenAutoRefreshEnabled` field is set to true. To use the global `isDataCollectionDefaultEnabled` flag for determining automatic token refreshing, call `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck#installAppCheckProviderFactory(com.google.firebase.appcheck.AppCheckProviderFactory)` instead.

### removeAppCheckListener

```
abstract fun removeAppCheckListener(listener: FirebaseAppCheck.AppCheckListener): Unit
```

Unregisters an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener` to changes in the token state.

### setTokenAutoRefreshEnabled

```
abstract fun setTokenAutoRefreshEnabled(isTokenAutoRefreshEnabled: Boolean): Unit
```

Sets the `isTokenAutoRefreshEnabled` flag.