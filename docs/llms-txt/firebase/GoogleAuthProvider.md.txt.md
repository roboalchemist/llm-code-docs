# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GoogleAuthProvider.md.txt

# GoogleAuthProvider

# GoogleAuthProvider


```
public class GoogleAuthProvider
```

<br />

*** ** * ** ***

Represents the Google Sign-In authentication provider. Use this class to obtain s.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GoogleAuthProvider#GOOGLE_SIGN_IN_METHOD() = "google.com"` Unique string identifier for Google sign-in method. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GoogleAuthProvider#PROVIDER_ID() = "google.com"` Unique string identifier for this provider type. |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GoogleAuthProvider#getCredential(java.lang.String,java.lang.String)(@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html idToken, @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html accessToken)` Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that wraps Google Sign-In ID or access tokens. |

## Constants

### GOOGLE_SIGN_IN_METHOD

```
public static final String GOOGLE_SIGN_IN_METHOD = "google.com"
```

Unique string identifier for Google sign-in method.

### PROVIDER_ID

```
public static final String PROVIDER_ID = "google.com"
```

Unique string identifier for this provider type.

## Public methods

### getCredential

```
public static @NonNull AuthCredential getCredential(@Nullable String idToken, @Nullable String accessToken)
```

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that wraps Google Sign-In ID or access tokens. Used when calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` or `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

Both parameters are optional but at least one must be present.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html idToken` | a valid Google Sign-In id token, obtained from the Google Sign-In SDK |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html accessToken` | a valid Google Sign-In access token, obtained from the Google Sign-In SDK |