# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor.md.txt

# MultiFactor

# MultiFactor


```
public abstract class MultiFactor
```

<br />

*** ** * ** ***

Defines multi-factor related properties and operations pertaining to a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser`. This class acts as the main entry point for enrolling or un-enrolling second factors for a user, and provides access to their currently enrolled factors.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#MultiFactor()()` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#enroll(com.google.firebase.auth.MultiFactorAssertion,java.lang.String)( @https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion multiFactorAssertion, @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html displayName )` Enrolls a second factor as identified by the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion` parameter for the current user. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#getEnrolledFactors()()` Returns a list of the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo` already associated with this user. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorSession>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#getSession()()` Returns a session identifier for a second factor enrollment operation. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#unenroll(java.lang.String)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html factorUid)` Unenrolls a second factor from this user. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html<https://developer.android.com/reference/java/lang/Void.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#unenroll(com.google.firebase.auth.MultiFactorInfo)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo multiFactorInfo)` Unenrolls a second factor from this user. |

## Public constructors

### MultiFactor

```
public MultiFactor()
```

## Public methods

### enroll

```
public abstract @NonNull Task<Void> enroll(
    @NonNull MultiFactorAssertion multiFactorAssertion,
    @Nullable String displayName
)
```

Enrolls a second factor as identified by the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion` parameter for the current user.

On successful enrollment, existing Firebase sessions are revoked, and an email notification is sent to the user's email. The user's must have a verified email to enroll a second factor.

A `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion` can be generated using `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorGenerator#getAssertion(com.google.firebase.auth.PhoneAuthCredential)` for enrolling phone number as a second factor or `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorGenerator#getAssertionForEnrollment(com.google.firebase.auth.TotpSecret,java.lang.String)` for enrolling TOTP as a second factor.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion multiFactorAssertion` | the assertion representing the second factor to enroll |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html displayName` | an optional name for identifying this second factor |

### getEnrolledFactors

```
public abstract @NonNull List<MultiFactorInfo> getEnrolledFactors()
```

Returns a list of the `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo` already associated with this user.

If the user does not have any enrolled factors, the list will be empty.

### getSession

```
public abstract @NonNull Task<MultiFactorSession> getSession()
```

Returns a session identifier for a second factor enrollment operation. This is used to identify the current user trying to enroll a second factor.

To be used when building a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions` instance to call `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)` for phone factor enrollment, or when generating a `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpSecret` instance for TOTP factor enrollment.

### unenroll

```
public abstract @NonNull Task<Void> unenroll(@NonNull String factorUid)
```

Unenrolls a second factor from this user.

The `factorUid` to be passed in can be retrieved from `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#getEnrolledFactors()`.

### unenroll

```
public abstract @NonNull Task<Void> unenroll(@NonNull MultiFactorInfo multiFactorInfo)
```

Unenrolls a second factor from this user.

The `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo` to be passed in can be gotten from `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#getEnrolledFactors()`.