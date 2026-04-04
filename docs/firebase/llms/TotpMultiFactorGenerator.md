# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorGenerator.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator.md.txt

# TotpMultiFactorGenerator

# TotpMultiFactorGenerator


```
class TotpMultiFactorGenerator
```

<br />

*** ** * ** ***

Helper class used to generate a [TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorAssertion).

## Summary

|                                        ### Constants                                        |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [FACTOR_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#FACTOR_ID())` = "totp"` |

|                                                                                                  ### Public functions                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)`<`[TotpSecret](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret)`!>` | [generateSecret](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#generateSecret(com.google.firebase.auth.MultiFactorSession))`(session: `[MultiFactorSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession)`)` Creates a TOTP secret as part of enrolling a TOTP (time-based one-time password) second factor.                                                                 |
| `java-static `[TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorAssertion)                                                                          | [getAssertionForEnrollment](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#getAssertionForEnrollment(com.google.firebase.auth.TotpSecret,java.lang.String))`(secret: `[TotpSecret](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret)`, otp: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Creates an assertion for completing the enrollment flow. |
| `java-static `[TotpMultiFactorAssertion](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorAssertion)                                                                          | [getAssertionForSignIn](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#getAssertionForSignIn(java.lang.String,java.lang.String))`(enrollmentId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, otp: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Creates an assertion for the sign-in flow.                                                       |

## Constants

### FACTOR_ID

```
constÂ valÂ FACTOR_ID = "totp":Â String!
```  

## Public functions

### generateSecret

```
java-staticÂ funÂ generateSecret(session:Â MultiFactorSession):Â Task<TotpSecret!>
```

Creates a TOTP secret as part of enrolling a TOTP (time-based one-time password) second factor. This method uses the auth instance corresponding to the user in the [MultiFactorSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession).  

|                                                           Parameters                                                           |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| `session: `[MultiFactorSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession) | [MultiFactorSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession). |

### getAssertionForEnrollment

```
java-staticÂ funÂ getAssertionForEnrollment(secret:Â TotpSecret,Â otp:Â String):Â TotpMultiFactorAssertion
```

Creates an assertion for completing the enrollment flow.  

|                                                  Parameters                                                   |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `secret: `[TotpSecret](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpSecret) | obtained from the [generateSecret](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#generateSecret(com.google.firebase.auth.MultiFactorSession)) step. |
| `otp: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                       | one-time password obtained from the TOTP App.                                                                                                                                                             |

### getAssertionForSignIn

```
java-staticÂ funÂ getAssertionForSignIn(enrollmentId:Â String,Â otp:Â String):Â TotpMultiFactorAssertion
```

Creates an assertion for the sign-in flow.  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `enrollmentId: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | identifies the TOTP second factor being used. |
| `otp: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)          | one-time password obtained from the TOTP App. |