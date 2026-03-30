# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PlayGamesAuthProvider.md.txt

# PlayGamesAuthProvider

# PlayGamesAuthProvider


```
class PlayGamesAuthProvider
```

<br />

*** ** * ** ***

Represents the Google Play Games authentication provider. Use this class to obtain s.

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PlayGamesAuthProvider#PLAY_GAMES_SIGN_IN_METHOD() = "playgames.google.com"` Unique string identifier for Google Play Games Service sign-in method. |
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PlayGamesAuthProvider#PROVIDER_ID() = "playgames.google.com"` Unique string identifier for this provider type. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PlayGamesAuthProvider#getCredential(java.lang.String)(serverAuthCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that wraps a Play Games Server Auth Code. |

## Constants

### PLAY_GAMES_SIGN_IN_METHOD

```
const val PLAY_GAMES_SIGN_IN_METHOD = "playgames.google.com": String!
```

Unique string identifier for Google Play Games Service sign-in method.

### PROVIDER_ID

```
const val PROVIDER_ID = "playgames.google.com": String!
```

Unique string identifier for this provider type.

## Public functions

### getCredential

```
java-static fun getCredential(serverAuthCode: String): AuthCredential
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential` that wraps a Play Games Server Auth Code. Used when calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)`.

| Parameters |
|---|---|
| `serverAuthCode: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a valid Google Play Games server auth code, obtained from Google Play Games Sign In SDK. |