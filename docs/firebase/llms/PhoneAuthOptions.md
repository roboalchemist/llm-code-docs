# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.md.txt

# PhoneAuthOptions

# PhoneAuthOptions


```
class PhoneAuthOptions
```

<br />

*** ** * ** ***

Options object for configuring phone validation flows in [PhoneAuthProvider](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider).

## Summary

|                                                                                                                               ### Nested types                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) A Builder class for [PhoneAuthOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions). |

|                                                             ### Public functions                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) | [newBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions#newBuilder())`()` Returns a new instance of [PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) tied to the default instance of [FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth).                                        |
| `java-static `[PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) | [newBuilder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions#newBuilder(com.google.firebase.auth.FirebaseAuth))`(auth: `[FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth)`)` Returns a new instance of [PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) tied to given instance of . |

## Public functions

### newBuilder

```
java-staticÂ funÂ newBuilder():Â PhoneAuthOptions.Builder
```

Returns a new instance of [PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) tied to the default instance of [FirebaseAuth](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth).  

### newBuilder

```
java-staticÂ funÂ newBuilder(auth:Â FirebaseAuth):Â PhoneAuthOptions.Builder
```

Returns a new instance of [PhoneAuthOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder) tied to given instance of .