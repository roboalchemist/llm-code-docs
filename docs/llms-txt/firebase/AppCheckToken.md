# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1beta/AppCheckToken.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseappcheck/api/reference/Classes/AppCheckToken.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken.md.txt

# Source: https://firebase.google.com/docs/reference/appcheck/rest/v1/AppCheckToken.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken.md.txt

# AppCheckToken

# AppCheckToken


```
public abstract class AppCheckToken
```

<br />

*** ** * ** ***

Class to hold tokens emitted by the Firebase App Check service which are minted upon a successful application verification. These tokens are the federated output of a verification flow, the structure of which is independent of the mechanism by which the application was verified.

## Summary

|                                                      ### Public constructors                                                       |
|------------------------------------------------------------------------------------------------------------------------------------|
| [AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken#AppCheckToken())`()` |

|                                                                                   ### Public methods                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract long`                                                                                                                                                                         | [getExpireTimeMillis](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken#getExpireTimeMillis())`()` Returns the time at which the token will expire in milliseconds since epoch. |
| `abstract @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | [getToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken#getToken())`()` Returns the raw JWT attesting to this application's identity.                                      |

|                                                                               ### Extension functions                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | [FirebaseAppCheckKt](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt)`.`[component1](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken#(com.google.firebase.appcheck.AppCheckToken).component1())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken)` receiver)` Destructuring declaration for [AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken) to provide token.            |
| `final long`                                                                                                                                                                         | [FirebaseAppCheckKt](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/FirebaseAppCheckKt)`.`[component2](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken#(com.google.firebase.appcheck.AppCheckToken).component2())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken)` receiver)` Destructuring declaration for [AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken) to provide expireTimeMillis. |

## Public constructors

### AppCheckToken

```
publicÂ AppCheckToken()
```  

## Public methods

### getExpireTimeMillis

```
publicÂ abstractÂ longÂ getExpireTimeMillis()
```

Returns the time at which the token will expire in milliseconds since epoch.  

### getToken

```
publicÂ abstractÂ @NonNull StringÂ getToken()
```

Returns the raw JWT attesting to this application's identity.  

## Extension functions

### FirebaseAppCheckKt.component1

```
publicÂ finalÂ @NonNull StringÂ FirebaseAppCheckKt.component1(@NonNull AppCheckTokenÂ receiver)
```

Destructuring declaration for [AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken) to provide token.  

|                                                                                    Returns                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | the token of the [AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken) |

### FirebaseAppCheckKt.component2

```
publicÂ finalÂ longÂ FirebaseAppCheckKt.component2(@NonNull AppCheckTokenÂ receiver)
```

Destructuring declaration for [AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken) to provide expireTimeMillis.  

| Returns |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `long`  | the expireTimeMillis of the [AppCheckToken](https://firebase.google.com/docs/reference/android/com/google/firebase/appcheck/AppCheckToken) |