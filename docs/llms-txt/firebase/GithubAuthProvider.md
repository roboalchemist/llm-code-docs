# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/GithubAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GithubAuthProvider.md.txt

# GithubAuthProvider

# GithubAuthProvider


```
public class GithubAuthProvider
```

<br />

*** ** * ** ***

Represents the Github authentication provider. Use this class to obtain s.

## Summary

|                                     ### Constants                                      |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final `[String](https://developer.android.com/reference/java/lang/String.html) | [GITHUB_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GithubAuthProvider#GITHUB_SIGN_IN_METHOD())` = "github.com"` Unique string identifier for Github sign-in method. |
| `static final `[String](https://developer.android.com/reference/java/lang/String.html) | [PROVIDER_ID](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GithubAuthProvider#PROVIDER_ID())` = "github.com"` Unique string identifier for this provider type.                        |

|                                                                                              ### Public methods                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) | [getCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GithubAuthProvider#getCredential(java.lang.String))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` token)` Returns a new instance of [AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) that wraps a Github OAuth token. |

## Constants

### GITHUB_SIGN_IN_METHOD

```
publicÂ staticÂ finalÂ StringÂ GITHUB_SIGN_IN_METHOD = "github.com"
```

Unique string identifier for Github sign-in method.  

### PROVIDER_ID

```
publicÂ staticÂ finalÂ StringÂ PROVIDER_ID = "github.com"
```

Unique string identifier for this provider type.  

## Public methods

### getCredential

```
publicÂ staticÂ @NonNull AuthCredentialÂ getCredential(@NonNull StringÂ token)
```

Returns a new instance of [AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) that wraps a Github OAuth token. Used when calling [signInWithCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)) or [linkWithCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)).  

|                                                                                Parameters                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` token` | A valid Github OAuth access token, obtained from the Github OAuth flow |