# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PlayGamesAuthProvider.md.txt

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

|                                        ### Constants                                        |
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [PLAY_GAMES_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PlayGamesAuthProvider#PLAY_GAMES_SIGN_IN_METHOD())` = "playgames.google.com"` Unique string identifier for Google Play Games Service sign-in method. |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [PROVIDER_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PlayGamesAuthProvider#PROVIDER_ID())` = "playgames.google.com"` Unique string identifier for this provider type.                                                   |

|                                                   ### Public functions                                                    |
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) | [getCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PlayGamesAuthProvider#getCredential(java.lang.String))`(serverAuthCode: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns a new instance of [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) that wraps a Play Games Server Auth Code. |

## Constants

### PLAY_GAMES_SIGN_IN_METHOD

```
constÂ valÂ PLAY_GAMES_SIGN_IN_METHOD = "playgames.google.com":Â String!
```

Unique string identifier for Google Play Games Service sign-in method.  

### PROVIDER_ID

```
constÂ valÂ PROVIDER_ID = "playgames.google.com":Â String!
```

Unique string identifier for this provider type.  

## Public functions

### getCredential

```
java-staticÂ funÂ getCredential(serverAuthCode:Â String):Â AuthCredential
```

Returns a new instance of [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) that wraps a Play Games Server Auth Code. Used when calling [signInWithCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)) or [linkWithCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)).  

|                                             Parameters                                             |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| `serverAuthCode: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | a valid Google Play Games server auth code, obtained from Google Play Games Sign In SDK. |