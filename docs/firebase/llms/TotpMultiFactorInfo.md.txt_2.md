# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo.md.txt

# TotpMultiFactorInfo

# TotpMultiFactorInfo


```
class TotpMultiFactorInfo : MultiFactorInfo
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.auth.MultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo) ||
|   | ↳ | [com.google.firebase.auth.TotpMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo) |

*** ** * ** ***

Represents the information for a TOTP (time-based one-time password) second factor.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo#getFactorId()()` Returns `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#FACTOR_ID()`, identifying this as a TotpMultiFactorInfo. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo#displayName()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo#enrollmentTimestamp()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo#uid()` |

| ### Inherited Constants |
|---|
| From [com.google.firebase.auth.MultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#FACTOR_ID_KEY() = "factorIdKey"` | |
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Public functions

### getFactorId

```
fun getFactorId(): String
```

Returns `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorGenerator#FACTOR_ID()`, identifying this as a TotpMultiFactorInfo.

## Public properties

### displayName

```
val displayName: String?
```

### enrollmentTimestamp

```
val enrollmentTimestamp: Long
```

### uid

```
val uid: String!
```