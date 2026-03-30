# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck.md.txt

# FirebaseAppCheck

# FirebaseAppCheck


```
public abstract class FirebaseAppCheck implements InteropAppCheckTokenProvider
```

<br />

*** ** * ** ***

## Summary

| ### Nested types |
|---|
| `public interface https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#FirebaseAppCheck()()` |

| ### Public methods |
|---|---|
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#addAppCheckListener(com.google.firebase.appcheck.FirebaseAppCheck.AppCheckListener)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener listener)` Registers an `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener` to changes in the token state. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#getAppCheckToken(boolean)(boolean forceRefresh)` Requests a Firebase App Check token. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#getInstance()()` Gets the default instance of `FirebaseAppCheck`. |
| `static @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#getInstance(com.google.firebase.FirebaseApp)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp firebaseApp)` Gets the instance of `FirebaseAppCheck` associated with the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#getLimitedUseAppCheckToken()()` Requests a Firebase App Check token. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#installAppCheckProviderFactory(com.google.firebase.appcheck.AppCheckProviderFactory)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProviderFactory factory)` Installs the given `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProviderFactory`, overwriting any that were previously associated with this `FirebaseAppCheck` instance. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#installAppCheckProviderFactory(com.google.firebase.appcheck.AppCheckProviderFactory,boolean)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProviderFactory factory, boolean isTokenAutoRefreshEnabled )` Installs the given `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProviderFactory`, overwriting any that were previously associated with this `FirebaseAppCheck` instance. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#removeAppCheckListener(com.google.firebase.appcheck.FirebaseAppCheck.AppCheckListener)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener listener )` Unregisters an `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener` to changes in the token state. |
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#setTokenAutoRefreshEnabled(boolean)(boolean isTokenAutoRefreshEnabled)` Sets the `isTokenAutoRefreshEnabled` flag. |

| ### Inherited methods |
|---|
| From [com.google.firebase.appcheck.interop.InteropAppCheckTokenProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider) |---|---| | `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider#addAppCheckTokenListener(com.google.firebase.appcheck.interop.AppCheckTokenListener)(https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/interop/AppCheckTokenListener p)` | | `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckTokenResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider#getLimitedUseToken()()` | | `abstract https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckTokenResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider#getToken(boolean)(boolean p)` | | `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/interop/InteropAppCheckTokenProvider#removeAppCheckTokenListener(com.google.firebase.appcheck.interop.AppCheckTokenListener)(https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/interop/AppCheckTokenListener p)` | |

## Public constructors

### FirebaseAppCheck

```
public FirebaseAppCheck()
```

## Public methods

### addAppCheckListener

```
public abstract void addAppCheckListener(@NonNull FirebaseAppCheck.AppCheckListener listener)
```

Registers an `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener` to changes in the token state. This method should be used ONLY if you need to authorize requests to a non-Firebase backend. Requests to Firebase backends are authorized automatically if configured.

### getAppCheckToken

```
public abstract @NonNull Task<AppCheckToken> getAppCheckToken(boolean forceRefresh)
```

Requests a Firebase App Check token. This method should be used ONLY if you need to authorize requests to a non-Firebase backend. Requests to Firebase backends are authorized automatically if configured.

If your non-Firebase backend exposes a sensitive or expensive endpoint that has low traffic volume, consider protecting it with [Replay Protection](https://firebase.google.com/docs/app-check/custom-resource-backend#replay-protection). In this case, use `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#getLimitedUseAppCheckToken()` instead to obtain a limited-use token.

### getInstance

```
public static @NonNull FirebaseAppCheck getInstance()
```

Gets the default instance of `FirebaseAppCheck`.

### getInstance

```
public static @NonNull FirebaseAppCheck getInstance(@NonNull FirebaseApp firebaseApp)
```

Gets the instance of `FirebaseAppCheck` associated with the given `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance.

### getLimitedUseAppCheckToken

```
public abstract @NonNull Task<AppCheckToken> getLimitedUseAppCheckToken()
```

Requests a Firebase App Check token. This method should be used ONLY if you need to authorize requests to a non-Firebase backend.

Returns limited-use tokens that are intended for use with your non-Firebase backend endpoints that are protected with [Replay Protection](https://firebase.google.com/docs/app-check/custom-resource-backend#replay-protection). This method does not affect the token generation behavior of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#getAppCheckToken(boolean)` method.

### installAppCheckProviderFactory

```
public abstract void installAppCheckProviderFactory(@NonNull AppCheckProviderFactory factory)
```

Installs the given `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProviderFactory`, overwriting any that were previously associated with this `FirebaseAppCheck` instance. Any `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/interop/AppCheckTokenListener`s attached to this `FirebaseAppCheck` instance will be transferred from existing factories to the newly installed one.

Automatic token refreshing will only occur if the global `
isDataCollectionDefaultEnabled` flag is set to true. To allow automatic token refreshing for Firebase App Check without changing the `isDataCollectionDefaultEnabled` flag for other Firebase SDKs, use `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#installAppCheckProviderFactory(com.google.firebase.appcheck.AppCheckProviderFactory,boolean)` instead or call `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#setTokenAutoRefreshEnabled(boolean)` after installing the `
factory`.

### installAppCheckProviderFactory

```
public abstract void installAppCheckProviderFactory(
    @NonNull AppCheckProviderFactory factory,
    boolean isTokenAutoRefreshEnabled
)
```

Installs the given `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckProviderFactory`, overwriting any that were previously associated with this `FirebaseAppCheck` instance. Any `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/interop/AppCheckTokenListener`s attached to this `FirebaseAppCheck` instance will be transferred from existing factories to the newly installed one.

Automatic token refreshing will only occur if the `isTokenAutoRefreshEnabled` field is set to true. To use the global `isDataCollectionDefaultEnabled` flag for determining automatic token refreshing, call `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck#installAppCheckProviderFactory(com.google.firebase.appcheck.AppCheckProviderFactory)` instead.

### removeAppCheckListener

```
public abstract void removeAppCheckListener(
    @NonNull FirebaseAppCheck.AppCheckListener listener
)
```

Unregisters an `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheck.AppCheckListener` to changes in the token state.

### setTokenAutoRefreshEnabled

```
public abstract void setTokenAutoRefreshEnabled(boolean isTokenAutoRefreshEnabled)
```

Sets the `isTokenAutoRefreshEnabled` flag.