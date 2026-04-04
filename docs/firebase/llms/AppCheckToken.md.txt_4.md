# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken.md.txt

# AppCheckToken

# AppCheckToken


```
abstract class AppCheckToken
```

<br />

*** ** * ** ***

Class to hold tokens emitted by the Firebase App Check service which are minted upon a successful application verification. These tokens are the federated output of a verification flow, the structure of which is independent of the mechanism by which the application was verified.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken#AppCheckToken()()` |

| ### Public functions |
|---|---|
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken#getExpireTimeMillis()()` Returns the time at which the token will expire in milliseconds since epoch. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken#getToken()()` Returns the raw JWT attesting to this application's identity. |

| ### Extension functions |
|---|---|
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken#(com.google.firebase.appcheck.AppCheckToken).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` to provide token. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken#(com.google.firebase.appcheck.AppCheckToken).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` to provide expireTimeMillis. |

## Public constructors

### AppCheckToken

```
AppCheckToken()
```

## Public functions

### getExpireTimeMillis

```
abstract fun getExpireTimeMillis(): Long
```

Returns the time at which the token will expire in milliseconds since epoch.

### getToken

```
abstract fun getToken(): String
```

Returns the raw JWT attesting to this application's identity.

## Extension functions

### component1

```
operator fun AppCheckToken.component1(): String
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` to provide token.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the token of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` |

### component2

```
operator fun AppCheckToken.component2(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` to provide expireTimeMillis.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the expireTimeMillis of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appcheck/AppCheckToken` |