# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PlayGamesAuthProvider.md.txt

# PlayGamesAuthProvider

# PlayGamesAuthProvider


```
public class PlayGamesAuthProvider
```

<br />

*** ** * ** ***

Represents the Google Play Games authentication provider. Use this class to obtain s.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PlayGamesAuthProvider#PLAY_GAMES_SIGN_IN_METHOD() = "playgames.google.com"` Unique string identifier for Google Play Games Service sign-in method. |
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PlayGamesAuthProvider#PROVIDER_ID() = "playgames.google.com"` Unique string identifier for this provider type. |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PlayGamesAuthProvider#getCredential(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html serverAuthCode)` Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that wraps a Play Games Server Auth Code. |

## Constants

### PLAY_GAMES_SIGN_IN_METHOD

```
public static final String PLAY_GAMES_SIGN_IN_METHOD = "playgames.google.com"
```

Unique string identifier for Google Play Games Service sign-in method.

### PROVIDER_ID

```
public static final String PROVIDER_ID = "playgames.google.com"
```

Unique string identifier for this provider type.

## Public methods

### getCredential

```
public static @NonNull AuthCredential getCredential(@NonNull String serverAuthCode)
```

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential` that wraps a Play Games Server Auth Code. Used when calling `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` or `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html serverAuthCode` | a valid Google Play Games server auth code, obtained from Google Play Games Sign In SDK. |