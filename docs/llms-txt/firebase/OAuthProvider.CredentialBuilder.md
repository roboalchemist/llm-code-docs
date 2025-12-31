# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.CredentialBuilder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder.md.txt

# OAuthProvider.CredentialBuilder

# OAuthProvider.CredentialBuilder


```
class OAuthProvider.CredentialBuilder
```

<br />

*** ** * ** ***

Builder class to initialize [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential)'s.

## Summary

|                                                             ### Public functions                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential)                                   | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder#build())`()` Returns the [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) that this [CredentialBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder) has constructed.                                         |
| [OAuthProvider.CredentialBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder) | [setIdTokenWithRawNonce](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder#setIdTokenWithRawNonce(java.lang.String,java.lang.String))`(idToken: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, rawNonce: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Adds an ID token and raw nonce to the credential being built. |

## Public functions

### build

```
funÂ build():Â AuthCredential
```

Returns the [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) that this [CredentialBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder) has constructed.  

|                                                        Throws                                                         |
|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [java.lang.IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException.html) | if an ID token and access token were not provided. |

### setIdTokenWithRawNonce

```
funÂ setIdTokenWithRawNonce(idToken:Â String,Â rawNonce:Â String?):Â OAuthProvider.CredentialBuilder
```

Adds an ID token and raw nonce to the credential being built.

The raw nonce is required when an OIDC ID token with a nonce field is provided. The SHA-256 hash of the raw nonce must match the nonce field in the OIDC ID token.