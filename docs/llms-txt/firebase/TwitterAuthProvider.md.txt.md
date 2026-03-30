# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TwitterAuthProvider.md.txt

# TwitterAuthProvider

# TwitterAuthProvider


```
public class TwitterAuthProvider
```

<br />

*** ** * ** ***

Represents the Twitter authentication provider. Use this class to obtain s.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TwitterAuthProvider#PROVIDER_ID() = "twitter.com"` Unique string identifier for this provider type. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TwitterAuthProvider#TWITTER_SIGN_IN_METHOD() = "twitter.com"` Unique string identifier for Twitter sign-in method. |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TwitterAuthProvider#getCredential(java.lang.String,java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html token, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html secret)` Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that wraps a Log in with Twitter token. |

## Constants

### PROVIDER_ID

```
public static final String PROVIDER_ID = "twitter.com"
```

Unique string identifier for this provider type.

### TWITTER_SIGN_IN_METHOD

```
public static final String TWITTER_SIGN_IN_METHOD = "twitter.com"
```

Unique string identifier for Twitter sign-in method.

## Public methods

### getCredential

```
public static @NonNull AuthCredential getCredential(@NonNull String token, @NonNull String secret)
```

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that wraps a Log in with Twitter token. Used when calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` or `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html token` | a valid Log in with Twitter token (`TwitterAuthToken.token`), obtained from the Twitter Fabric SDK |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html secret` | a valid Log in with Twitter secret (`TwitterAuthToken.secret`), obtained from the Twitter Fabric SDK |