# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.md.txt

# PhoneAuthOptions

# PhoneAuthOptions


```
public final class PhoneAuthOptions
```

<br />

*** ** * ** ***

Options object for configuring phone validation flows in `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider`.

## Summary

| ### Nested types |
|---|
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` A Builder class for `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions`. |

| ### Public methods |
|---|---|
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions#newBuilder()()` Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` tied to the default instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth`. |
| `static @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions#newBuilder(com.google.firebase.auth.FirebaseAuth)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth auth)` Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` tied to given instance of . |

## Public methods

### newBuilder

```
public static @NonNull PhoneAuthOptions.Builder newBuilder()
```

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` tied to the default instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseAuth`.

### newBuilder

```
public static @NonNull PhoneAuthOptions.Builder newBuilder(@NonNull FirebaseAuth auth)
```

Returns a new instance of `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions.Builder` tied to given instance of .