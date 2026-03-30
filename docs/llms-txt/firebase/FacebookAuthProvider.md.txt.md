# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthProvider.md.txt

# FacebookAuthProvider

# FacebookAuthProvider


```
public class FacebookAuthProvider
```

<br />

*** ** * ** ***

Represents the Facebook Login authentication provider. Use this class to obtain s.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthProvider#FACEBOOK_SIGN_IN_METHOD() = "facebook.com"` Unique string identifier for Facebook sign-in method. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthProvider#PROVIDER_ID() = "facebook.com"` Unique string identifier for this provider type. |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthProvider#getCredential(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html accessToken)` Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that wraps a Facebook Login token. |

## Constants

### FACEBOOK_SIGN_IN_METHOD

```
public static final String FACEBOOK_SIGN_IN_METHOD = "facebook.com"
```

Unique string identifier for Facebook sign-in method.

### PROVIDER_ID

```
public static final String PROVIDER_ID = "facebook.com"
```

Unique string identifier for this provider type.

## Public methods

### getCredential

```
public static @NonNull AuthCredential getCredential(@NonNull String accessToken)
```

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that wraps a Facebook Login token. Used when calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` or `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html accessToken` | a valid Facebook Login access token, obtained from the Facebook Login SDK |