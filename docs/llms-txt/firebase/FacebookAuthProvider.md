# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FacebookAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/FacebookAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FacebookAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/FacebookAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FacebookAuthProvider.md.txt

# FacebookAuthProvider

# FacebookAuthProvider


```
class FacebookAuthProvider
```

<br />

*** ** * ** ***

Represents the Facebook Login authentication provider. Use this class to obtain s.

## Summary

|                                        ### Constants                                        |
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [FACEBOOK_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FacebookAuthProvider#FACEBOOK_SIGN_IN_METHOD())` = "facebook.com"` Unique string identifier for Facebook sign-in method. |
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [PROVIDER_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FacebookAuthProvider#PROVIDER_ID())` = "facebook.com"` Unique string identifier for this provider type.                              |

|                                                   ### Public functions                                                    |
|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) | [getCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FacebookAuthProvider#getCredential(java.lang.String))`(accessToken: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns a new instance of [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) that wraps a Facebook Login token. |

## Constants

### FACEBOOK_SIGN_IN_METHOD

```
constÂ valÂ FACEBOOK_SIGN_IN_METHOD = "facebook.com":Â String!
```

Unique string identifier for Facebook sign-in method.  

### PROVIDER_ID

```
constÂ valÂ PROVIDER_ID = "facebook.com":Â String!
```

Unique string identifier for this provider type.  

## Public functions

### getCredential

```
java-staticÂ funÂ getCredential(accessToken:Â String):Â AuthCredential
```

Returns a new instance of [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) that wraps a Facebook Login token. Used when calling [signInWithCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)) or [linkWithCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)).  

|                                           Parameters                                            |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `accessToken: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | a valid Facebook Login access token, obtained from the Facebook Login SDK |