# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder.md.txt

# OAuthProvider.Builder

# OAuthProvider.Builder


```
public class OAuthProvider.Builder
```

<br />

*** ** * ** ***

Class used to create instances of [OAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider).

## Summary

|                                                                                                 ### Public methods                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[OAuthProvider.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder) | [addCustomParameter](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder#addCustomParameter(java.lang.String,java.lang.String))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` paramKey, @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` paramValue)` Configures custom parameters to be passed to the identity provider during the OAuth sign-in flow.                                                                                                                                                                        |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[OAuthProvider.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder) | [addCustomParameters](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder#addCustomParameters(java.util.Map<java.lang.String,java.lang.String>))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Map](https://developer.android.com/reference/java/util/Map.html)`<`[String](https://developer.android.com/reference/java/lang/String.html)`, `[String](https://developer.android.com/reference/java/lang/String.html)`> customParameters)` Similar to [addCustomParameter](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder#addCustomParameter(java.lang.String,java.lang.String)), this takes a Map and adds each entry to the set of custom parameters to be passed. |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[OAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider)                 | [build](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder#build())`()` Returns an [OAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider) created from this [Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder).                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[OAuthProvider.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder) | [setScopes](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder#setScopes(java.util.List<java.lang.String>))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/java/util/List.html)`<`[String](https://developer.android.com/reference/java/lang/String.html)`> scopes)` Sets the OAuth 2 scopes to be presented to the user during their sign-in flow with the identity provider.                                                                                                                                                                                                                                                                                           |

## Public methods

### addCustomParameter

```
publicÂ @NonNull OAuthProvider.BuilderÂ addCustomParameter(@NonNull StringÂ paramKey,Â @NonNull StringÂ paramValue)
```

Configures custom parameters to be passed to the identity provider during the OAuth sign-in flow. Calling this method multiple times will add to the set of custom parameters being passed, rather than overwriting them (as long as key values don't collide).  

|                                                                                  Parameters                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` paramKey`   | the name of the custom parameter  |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` paramValue` | the value of the custom parameter |

### addCustomParameters

```
publicÂ @NonNull OAuthProvider.BuilderÂ addCustomParameters(@NonNull Map<String,Â String>Â customParameters)
```

Similar to [addCustomParameter](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder#addCustomParameter(java.lang.String,java.lang.String)), this takes a Map and adds each entry to the set of custom parameters to be passed. Calling this method multiple times will add to the set of custom parameters being passed, rather than overwriting them (as long as key values don't collide).  

|                                                                                                                                                             Parameters                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Map](https://developer.android.com/reference/java/util/Map.html)`<`[String](https://developer.android.com/reference/java/lang/String.html)`, `[String](https://developer.android.com/reference/java/lang/String.html)`> customParameters` | a dictionary of custom parameter names and values to be passed to the identity provider as part of the sign-in flow. |

### build

```
publicÂ @NonNull OAuthProviderÂ build()
```

Returns an [OAuthProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider) created from this [Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder).  

### setScopes

```
publicÂ @NonNull OAuthProvider.BuilderÂ setScopes(@NonNull List<String>Â scopes)
```

Sets the OAuth 2 scopes to be presented to the user during their sign-in flow with the identity provider.