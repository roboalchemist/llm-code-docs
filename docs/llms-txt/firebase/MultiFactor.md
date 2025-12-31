# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactor.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactor.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor.md.txt

# MultiFactor

# MultiFactor


```
public abstract class MultiFactor
```

<br />

*** ** * ** ***

Defines multi-factor related properties and operations pertaining to a [FirebaseUser](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser). This class acts as the main entry point for enrolling or un-enrolling second factors for a user, and provides access to their currently enrolled factors.

## Summary

|                                                 ### Public constructors                                                  |
|--------------------------------------------------------------------------------------------------------------------------|
| [MultiFactor](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#MultiFactor())`()` |

|                                                                                                                                                     ### Public methods                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                                  | [enroll](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#enroll(com.google.firebase.auth.MultiFactorAssertion,java.lang.String))`(` ` @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[MultiFactorAssertion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion)` multiFactorAssertion,` ` @`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` displayName` `)` Enrolls a second factor as identified by the [MultiFactorAssertion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion) parameter for the current user. |
| `abstract @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/java/util/List.html)`<`[MultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo)`>`                                  | [getEnrolledFactors](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#getEnrolledFactors())`()` Returns a list of the [MultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo) already associated with this user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `abstract @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[MultiFactorSession](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorSession)`>` | [getSession](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#getSession())`()` Returns a session identifier for a second factor enrollment operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `abstract @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                                  | [unenroll](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#unenroll(java.lang.String))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` factorUid)` Unenrolls a second factor from this user.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `abstract @`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[Void](https://developer.android.com/reference/java/lang/Void.html)`>`                                                  | [unenroll](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#unenroll(com.google.firebase.auth.MultiFactorInfo))`(@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[MultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo)` multiFactorInfo)` Unenrolls a second factor from this user.                                                                                                                                                                                                                                                                                                                                                                                        |

## Public constructors

### MultiFactor

```
publicÂ MultiFactor()
```  

## Public methods

### enroll

```
publicÂ abstractÂ @NonNull Task<Void>Â enroll(
Â Â Â Â @NonNull MultiFactorAssertionÂ multiFactorAssertion,
Â Â Â Â @Nullable StringÂ displayName
)
```

Enrolls a second factor as identified by the [MultiFactorAssertion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion) parameter for the current user.

On successful enrollment, existing Firebase sessions are revoked, and an email notification is sent to the user's email. The user's must have a verified email to enroll a second factor.

A [MultiFactorAssertion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion) can be generated using [getAssertion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorGenerator#getAssertion(com.google.firebase.auth.PhoneAuthCredential)) for enrolling phone number as a second factor or [getAssertionForEnrollment](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorGenerator#getAssertionForEnrollment(com.google.firebase.auth.TotpSecret,java.lang.String)) for enrolling TOTP as a second factor.  

|                                                                                                                Parameters                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)` `[MultiFactorAssertion](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorAssertion)` multiFactorAssertion` | the assertion representing the second factor to enroll |
| `@`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html)` displayName`                                                         | an optional name for identifying this second factor    |

### getEnrolledFactors

```
publicÂ abstractÂ @NonNull List<MultiFactorInfo>Â getEnrolledFactors()
```

Returns a list of the [MultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo) already associated with this user.

If the user does not have any enrolled factors, the list will be empty.  

### getSession

```
publicÂ abstractÂ @NonNull Task<MultiFactorSession>Â getSession()
```

Returns a session identifier for a second factor enrollment operation. This is used to identify the current user trying to enroll a second factor.

To be used when building a [PhoneAuthOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthOptions) instance to call [verifyPhoneNumber](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneAuthProvider#verifyPhoneNumber(com.google.firebase.auth.PhoneAuthOptions)) for phone factor enrollment, or when generating a [TotpSecret](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpSecret) instance for TOTP factor enrollment.  

### unenroll

```
publicÂ abstractÂ @NonNull Task<Void>Â unenroll(@NonNull StringÂ factorUid)
```

Unenrolls a second factor from this user.

The `factorUid` to be passed in can be retrieved from [getEnrolledFactors](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#getEnrolledFactors()).  

### unenroll

```
publicÂ abstractÂ @NonNull Task<Void>Â unenroll(@NonNull MultiFactorInfoÂ multiFactorInfo)
```

Unenrolls a second factor from this user.

The [MultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo) to be passed in can be gotten from [getEnrolledFactors](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactor#getEnrolledFactors()).