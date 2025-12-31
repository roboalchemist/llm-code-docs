# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/GoogleAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GoogleAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GoogleAuthProvider.md.txt

# GoogleAuthProvider

# GoogleAuthProvider


```
class GoogleAuthProvider
```

<br />

*** ** * ** ***

Represents the Google Sign-In authentication provider. Use this class to obtain s.

## Summary

|                                        ### Constants                                        |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [GOOGLE_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GoogleAuthProvider#GOOGLE_SIGN_IN_METHOD())` = "google.com"` Unique string identifier for Google sign-in method. |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [PROVIDER_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GoogleAuthProvider#PROVIDER_ID())` = "google.com"` Unique string identifier for this provider type.                        |

|                                                   ### Public functions                                                    |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) | [getCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GoogleAuthProvider#getCredential(java.lang.String,java.lang.String))`(idToken: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?, accessToken: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Returns a new instance of [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) that wraps Google Sign-In ID or access tokens. |

## Constants

### GOOGLE_SIGN_IN_METHOD

```
constÂ valÂ GOOGLE_SIGN_IN_METHOD = "google.com":Â String!
```

Unique string identifier for Google sign-in method.  

### PROVIDER_ID

```
constÂ valÂ PROVIDER_ID = "google.com":Â String!
```

Unique string identifier for this provider type.  

## Public functions

### getCredential

```
java-staticÂ funÂ getCredential(idToken:Â String?,Â accessToken:Â String?):Â AuthCredential
```

Returns a new instance of [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) that wraps Google Sign-In ID or access tokens. Used when calling [signInWithCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)) or [linkWithCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)).

Both parameters are optional but at least one must be present.  

|                                             Parameters                                             |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `idToken: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`     | a valid Google Sign-In id token, obtained from the Google Sign-In SDK     |
| `accessToken: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | a valid Google Sign-In access token, obtained from the Google Sign-In SDK |