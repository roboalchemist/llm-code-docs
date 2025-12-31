# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorInfo.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo.md.txt

# TotpMultiFactorInfo

# TotpMultiFactorInfo


```
class TotpMultiFactorInfo : MultiFactorInfo
```

<br />

|---|---|------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                    |||
| â³ | [com.google.firebase.auth.MultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo)            ||
|   | â³ | [com.google.firebase.auth.TotpMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo) |

*** ** * ** ***

Represents the information for a TOTP (time-based one-time password) second factor.

## Summary

|                               ### Public functions                               |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getFactorId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo#getFactorId())`()` Returns [FACTOR_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#FACTOR_ID()), identifying this as a TotpMultiFactorInfo. |

|                                ### Public properties                                |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [displayName](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo#displayName())                 |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)        | [enrollmentTimestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo#enrollmentTimestamp()) |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [uid](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo#uid())                                 |

|                                                                                                                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.auth.MultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo) |---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------| | `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [FACTOR_ID_KEY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#FACTOR_ID_KEY())` = "factorIdKey"` |                                                                                                                                                               |
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                                                                                               ### Inherited functions                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------| | `abstract `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()` | |

## Public functions

### getFactorId

```
funÂ getFactorId():Â String
```

Returns [FACTOR_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#FACTOR_ID()), identifying this as a TotpMultiFactorInfo.  

## Public properties

### displayName

```
valÂ displayName:Â String?
```  

### enrollmentTimestamp

```
valÂ enrollmentTimestamp:Â Long
```  

### uid

```
valÂ uid:Â String!
```