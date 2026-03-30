# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder.md.txt

# OAuthProvider.Builder

# OAuthProvider.Builder


```
public class OAuthProvider.Builder
```

<br />

*** ** * ** ***

Class used to create instances of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider`.

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder#addCustomParameter(java.lang.String,java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html paramKey, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html paramValue)` Configures custom parameters to be passed to the identity provider during the OAuth sign-in flow. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder#addCustomParameters(java.util.Map<java.lang.String,java.lang.String>)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/Map.html<https://developer.android.com/reference/java/lang/String.html, https://developer.android.com/reference/java/lang/String.html> customParameters)` Similar to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder#addCustomParameter(java.lang.String,java.lang.String)`, this takes a Map and adds each entry to the set of custom parameters to be passed. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder#build()()` Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` created from this `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder`. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder#setScopes(java.util.List<java.lang.String>)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/List.html<https://developer.android.com/reference/java/lang/String.html> scopes)` Sets the OAuth 2 scopes to be presented to the user during their sign-in flow with the identity provider. |

## Public methods

### addCustomParameter

```
public @NonNull OAuthProvider.Builder addCustomParameter(@NonNull String paramKey, @NonNull String paramValue)
```

Configures custom parameters to be passed to the identity provider during the OAuth sign-in flow. Calling this method multiple times will add to the set of custom parameters being passed, rather than overwriting them (as long as key values don't collide).

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html paramKey` | the name of the custom parameter |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html paramValue` | the value of the custom parameter |

### addCustomParameters

```
public @NonNull OAuthProvider.Builder addCustomParameters(@NonNull Map<String, String> customParameters)
```

Similar to `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder#addCustomParameter(java.lang.String,java.lang.String)`, this takes a Map and adds each entry to the set of custom parameters to be passed. Calling this method multiple times will add to the set of custom parameters being passed, rather than overwriting them (as long as key values don't collide).

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/Map.html<https://developer.android.com/reference/java/lang/String.html, https://developer.android.com/reference/java/lang/String.html> customParameters` | a dictionary of custom parameter names and values to be passed to the identity provider as part of the sign-in flow. |

### build

```
public @NonNull OAuthProvider build()
```

Returns an `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider` created from this `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/OAuthProvider.Builder`.

### setScopes

```
public @NonNull OAuthProvider.Builder setScopes(@NonNull List<String> scopes)
```

Sets the OAuth 2 scopes to be presented to the user during their sign-in flow with the identity provider.