# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult.md.txt

# GetTokenResult

# GetTokenResult


```
public class GetTokenResult
```

<br />

*** ** * ** ***

Result object that contains a Firebase Auth ID Token.

## Summary

|                                                                                                     ### Public fields                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [Map](https://developer.android.com/reference/java/util/Map.html)`<`[String](https://developer.android.com/reference/java/lang/String.html)`, `[Object](https://developer.android.com/reference/java/lang/Object.html)`>` | [claims](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult#claims()) |
| `@`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                        | [token](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult#token())   |

|                                                                                                                                                 ### Public methods                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `long`                                                                                                                                                                                                                                                                                                             | [getAuthTimestamp](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult#getAuthTimestamp())`()` Returns the authentication timestamp in seconds since epoch.                                                                              |
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Map](https://developer.android.com/reference/java/util/Map.html)`<`[String](https://developer.android.com/reference/java/lang/String.html)`, `[Object](https://developer.android.com/reference/java/lang/Object.html)`>` | [getClaims](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult#getClaims())`()` Returns the entire payload claims of the ID token including the standard reserved claims as well as the custom claims (set by developer via Admin SDK). |
| `long`                                                                                                                                                                                                                                                                                                             | [getExpirationTimestamp](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult#getExpirationTimestamp())`()` Returns the time in seconds since epoch at which this ID token will expire                                                    |
| `long`                                                                                                                                                                                                                                                                                                             | [getIssuedAtTimestamp](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult#getIssuedAtTimestamp())`()` Returns the issued at timestamp in seconds since epoch.                                                                           |
| `@`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                                 | [getSignInProvider](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult#getSignInProvider())`()` Returns the sign-in provider through which the ID token was obtained (anonymous, custom, phone, password, etc).                         |
| `@`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html)                                                                                                                                                 | [getToken](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult#getToken())`()` Firebase Auth ID Token.                                                                                                                                   |

## Public fields

### claims

```
publicÂ Map<String,Â Object>Â claims
```  

### token

```
publicÂ @Nullable StringÂ token
```  

## Public methods

### getAuthTimestamp

```
publicÂ longÂ getAuthTimestamp()
```

Returns the authentication timestamp in seconds since epoch. This is the time the user authenticated (signed in) and not the time the token was refreshed.  

### getClaims

```
publicÂ @NonNull Map<String,Â Object>Â getClaims()
```

Returns the entire payload claims of the ID token including the standard reserved claims as well as the custom claims (set by developer via Admin SDK). Developers should verify the ID token and parse claims from its payload on the backend and never trust this value on the client. Returns an empty map if no claims are present.  

### getExpirationTimestamp

```
publicÂ longÂ getExpirationTimestamp()
```

Returns the time in seconds since epoch at which this ID token will expire  

### getIssuedAtTimestamp

```
publicÂ longÂ getIssuedAtTimestamp()
```

Returns the issued at timestamp in seconds since epoch. This is the time the ID token was last refreshed and not the authentication timestamp.  

### getSignInProvider

```
publicÂ @Nullable StringÂ getSignInProvider()
```

Returns the sign-in provider through which the ID token was obtained (anonymous, custom, phone, password, etc). Note, this does not map to provider IDs. For example, anonymous and custom authentications are not considered providers. We chose the name here to map the name used in the ID token.  

### getToken

```
publicÂ @Nullable StringÂ getToken()
```

Firebase Auth ID Token. Useful for authenticating calls against your own backend. Verify the integrity and validity of the token in your server either by using our server SDKs or following the documentation.