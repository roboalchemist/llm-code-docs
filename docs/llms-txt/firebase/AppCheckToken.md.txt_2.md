# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken.md.txt

# AppCheckToken

# AppCheckToken


```
public abstract class AppCheckToken
```

<br />

*** ** * ** ***

Class to hold tokens emitted by the Firebase App Check service which are minted upon a successful application verification. These tokens are the federated output of a verification flow, the structure of which is independent of the mechanism by which the application was verified.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken#AppCheckToken()()` |

| ### Public methods |
|---|---|
| `abstract long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken#getExpireTimeMillis()()` Returns the time at which the token will expire in milliseconds since epoch. |
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken#getToken()()` Returns the raw JWT attesting to this application's identity. |

| ### Extension functions |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt.https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken#(com.google.firebase.appcheck.AppCheckToken).component1()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` to provide token. |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt.https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken#(com.google.firebase.appcheck.AppCheckToken).component2()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` to provide expireTimeMillis. |

## Public constructors

### AppCheckToken

```
public AppCheckToken()
```

## Public methods

### getExpireTimeMillis

```
public abstract long getExpireTimeMillis()
```

Returns the time at which the token will expire in milliseconds since epoch.

### getToken

```
public abstract @NonNull String getToken()
```

Returns the raw JWT attesting to this application's identity.

## Extension functions

### FirebaseAppCheckKt.component1

```
public final @NonNull String FirebaseAppCheckKt.component1(@NonNull AppCheckToken receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` to provide token.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | the token of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` |

### FirebaseAppCheckKt.component2

```
public final long FirebaseAppCheckKt.component2(@NonNull AppCheckToken receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` to provide expireTimeMillis.

| Returns |
|---|---|
| `long` | the expireTimeMillis of the `https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken` |