# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder.md.txt

# OAuthProvider.Builder

# OAuthProvider.Builder


```
class OAuthProvider.Builder
```

<br />

*** ** * ** ***

Class used to create instances of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider`.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder#addCustomParameter(java.lang.String,java.lang.String)(paramKey: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, paramValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Configures custom parameters to be passed to the identity provider during the OAuth sign-in flow. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder#addCustomParameters(java.util.Map<java.lang.String,java.lang.String>)(customParameters: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>)` Similar to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder#addCustomParameter(java.lang.String,java.lang.String)`, this takes a Map and adds each entry to the set of custom parameters to be passed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder#build()()` Returns an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider` created from this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder#setScopes(java.util.List<java.lang.String>)(scopes: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>)` Sets the OAuth 2 scopes to be presented to the user during their sign-in flow with the identity provider. |

## Public functions

### addCustomParameter

```
fun addCustomParameter(paramKey: String, paramValue: String): OAuthProvider.Builder
```

Configures custom parameters to be passed to the identity provider during the OAuth sign-in flow. Calling this method multiple times will add to the set of custom parameters being passed, rather than overwriting them (as long as key values don't collide).

| Parameters |
|---|---|
| `paramKey: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the name of the custom parameter |
| `paramValue: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the value of the custom parameter |

### addCustomParameters

```
fun addCustomParameters(customParameters: (Mutable)Map<String!, String!>): OAuthProvider.Builder
```

Similar to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder#addCustomParameter(java.lang.String,java.lang.String)`, this takes a Map and adds each entry to the set of custom parameters to be passed. Calling this method multiple times will add to the set of custom parameters being passed, rather than overwriting them (as long as key values don't collide).

| Parameters |
|---|---|
| `customParameters: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>` | a dictionary of custom parameter names and values to be passed to the identity provider as part of the sign-in flow. |

### build

```
fun build(): OAuthProvider
```

Returns an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider` created from this `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/OAuthProvider.Builder`.

### setScopes

```
fun setScopes(scopes: (Mutable)List<String!>): OAuthProvider.Builder
```

Sets the OAuth 2 scopes to be presented to the user during their sign-in flow with the identity provider.