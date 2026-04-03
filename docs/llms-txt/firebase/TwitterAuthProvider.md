# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/TwitterAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TwitterAuthProvider.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TwitterAuthProvider.md.txt

# TwitterAuthProvider

# TwitterAuthProvider


```
public class TwitterAuthProvider
```

<br />

*** ** * ** ***

Represents the Twitter authentication provider. Use this class to obtain s.

## Summary

|                                     ### Constants                                      |
|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final `[String](https://developer.android.com/reference/java/lang/String.html) | [PROVIDER_ID](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TwitterAuthProvider#PROVIDER_ID())` = "twitter.com"` Unique string identifier for this provider type.                           |
| `static final `[String](https://developer.android.com/reference/java/lang/String.html) | [TWITTER_SIGN_IN_METHOD](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TwitterAuthProvider#TWITTER_SIGN_IN_METHOD())` = "twitter.com"` Unique string identifier for Twitter sign-in method. |

|                                                                                              ### Public methods                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) | [getCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TwitterAuthProvider#getCredential(java.lang.String,java.lang.String))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` token, @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` secret)` Returns a new instance of [AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) that wraps a Log in with Twitter token. |

## Constants

### PROVIDER_ID

```
publicÂ staticÂ finalÂ StringÂ PROVIDER_ID = "twitter.com"
```

Unique string identifier for this provider type.  

### TWITTER_SIGN_IN_METHOD

```
publicÂ staticÂ finalÂ StringÂ TWITTER_SIGN_IN_METHOD = "twitter.com"
```

Unique string identifier for Twitter sign-in method.  

## Public methods

### getCredential

```
publicÂ staticÂ @NonNull AuthCredentialÂ getCredential(@NonNull StringÂ token,Â @NonNull StringÂ secret)
```

Returns a new instance of [AuthCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AuthCredential) that wraps a Log in with Twitter token. Used when calling [signInWithCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth#signInWithCredential(com.google.firebase.auth.AuthCredential)) or [linkWithCredential](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser#linkWithCredential(com.google.firebase.auth.AuthCredential)).  

|                                                                                Parameters                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` token`  | a valid Log in with Twitter token (`TwitterAuthToken.token`), obtained from the Twitter Fabric SDK   |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` secret` | a valid Log in with Twitter secret (`TwitterAuthToken.secret`), obtained from the Twitter Fabric SDK |