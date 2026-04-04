# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.md.txt

# PhoneAuthOptions

# PhoneAuthOptions


```
class PhoneAuthOptions
```

<br />

*** ** * ** ***

Options object for configuring phone validation flows in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthProvider`.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` A Builder class for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions`. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions#newBuilder()()` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` tied to the default instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth`. |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions#newBuilder(com.google.firebase.auth.FirebaseAuth)(auth: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth)` Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` tied to given instance of . |

## Public functions

### newBuilder

```
java-static fun newBuilder(): PhoneAuthOptions.Builder
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` tied to the default instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseAuth`.

### newBuilder

```
java-static fun newBuilder(auth: FirebaseAuth): PhoneAuthOptions.Builder
```

Returns a new instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneAuthOptions.Builder` tied to given instance of .