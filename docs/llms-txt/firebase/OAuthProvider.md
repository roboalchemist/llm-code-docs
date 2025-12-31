# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/OAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.md.txt

# OAuthProvider

# OAuthProvider


```
class OAuthProvider : FederatedAuthProvider
```

<br />

|---|---|------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                        |||
| â³ | [com.google.firebase.auth.FederatedAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FederatedAuthProvider) ||
|   | â³ | [com.google.firebase.auth.OAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider) |

*** ** * ** ***

Represents the login authentication provider for a generic OAuth2 provider. Use this class to obtain [AuthCredentials](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential).

## Summary

|                                                                                                                                         ### Nested types                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[OAuthProvider.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder) Class used to create instances of [OAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider).                   |
| `class `[OAuthProvider.CredentialBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder) Builder class to initialize [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential)'s. |

|                                                                    ### Public functions                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential)                                   | `@`[InlineMe](https://errorprone.info/api/latest/com/google/errorprone/annotations/InlineMe.html)`(replacement = "DefaultOAuthCredential.createDefaultOAuthCredential(providerId, idToken, accessToken)", imports = "com.google.firebase.auth.DefaultOAuthCredential")` ~~[getCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#getCredential(java.lang.String,java.lang.String,java.lang.String))~~`(providerId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, idToken: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, accessToken: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` **This function is deprecated.** use [newCredentialBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#newCredentialBuilder(java.lang.String)) instead <br /> |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                         | [getProviderId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#getProviderId())`()` Returns the provider ID with which this OAuthProvider is associated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `java-static `[OAuthProvider.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder)                     | [newBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#newBuilder(java.lang.String))`(providerId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Returns a [OAuthProvider.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder) used to construct a [OAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider) instantiated with the given `providerId`.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `java-static `[OAuthProvider.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder)                     | [newBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#newBuilder(java.lang.String,com.google.firebase.auth.FirebaseAuth))`(providerId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, firebaseAuth: `[FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth)`)` Returns a [OAuthProvider.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder) used to construct a [OAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider) instantiated with the given `providerId`.                                                                                                                                                                                                                                                    |
| `java-static `[OAuthProvider.CredentialBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder) | [newCredentialBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#newCredentialBuilder(java.lang.String))`(providerId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Creates an [CredentialBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder) for the specified provider ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Public functions

### getCredential

```
@InlineMe(replacementÂ =Â "DefaultOAuthCredential.createDefaultOAuthCredential(providerId, idToken, accessToken)",Â importsÂ =Â "com.google.firebase.auth.DefaultOAuthCredential")
java-staticÂ funÂ [getCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#getCredential(java.lang.String,java.lang.String,java.lang.String))(providerId:Â String,Â idToken:Â String,Â accessToken:Â String):Â AuthCredential
```
| **This function is deprecated.**   
|
| use [newCredentialBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider#newCredentialBuilder(java.lang.String)) instead

Returns a new instance of [AuthCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AuthCredential) that wraps a login token. Used when calling [signInWithCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)) or [linkWithCredential](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)).  

|                                           Parameters                                            |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `accessToken: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | a valid Facebook Login access token, obtained from the Facebook Login SDK |

### getProviderId

```
funÂ getProviderId():Â String?
```

Returns the provider ID with which this OAuthProvider is associated.  

### newBuilder

```
java-staticÂ funÂ newBuilder(providerId:Â String):Â OAuthProvider.Builder
```

Returns a [OAuthProvider.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder) used to construct a [OAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider) instantiated with the given `providerId`.  

### newBuilder

```
java-staticÂ funÂ newBuilder(providerId:Â String,Â firebaseAuth:Â FirebaseAuth):Â OAuthProvider.Builder
```

Returns a [OAuthProvider.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder) used to construct a [OAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider) instantiated with the given `providerId`. Uses the specified [FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth) instance.  

### newCredentialBuilder

```
java-staticÂ funÂ newCredentialBuilder(providerId:Â String):Â OAuthProvider.CredentialBuilder
```

Creates an [CredentialBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.CredentialBuilder) for the specified provider ID.  

|                                                        Throws                                                         |
|-----------------------------------------------------------------------------------------------------------------------|----------------------------------|
| [java.lang.IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException.html) | if `providerId` is null or empty |