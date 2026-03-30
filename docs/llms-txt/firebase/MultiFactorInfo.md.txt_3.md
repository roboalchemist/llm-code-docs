# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo.md.txt

# MultiFactorInfo

# MultiFactorInfo


```
abstract class MultiFactorInfo : Parcelable
```

<br />

Known direct subclasses [PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo), [TotpMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo` | Represents the information for a phone second factor. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo` | Represents the information for a TOTP (time-based one-time password) second factor. |

*** ** * ** ***

Represents a single second factor meant for the user. See direct subclasses for type-specific information.

## Summary

| ### Constants |
|---|---|
| `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#FACTOR_ID_KEY() = "factorIdKey"` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#MultiFactorInfo()()` |

| ### Public functions |
|---|---|
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#getDisplayName()()` Returns the user-given display name for this second factor. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#getEnrollmentTimestamp()()` Returns the enrollment timestamp for this second factor in seconds since epoch (UTC midnight on January 1, 1970). |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#getFactorId()()` Returns the factor id of this second factor. |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#getUid()()` Returns the unique identifier for this second factor. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int)(p: https://developer.android.com/reference/android/os/Parcel.html!, p1: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | |

## Constants

### FACTOR_ID_KEY

```
const val FACTOR_ID_KEY = "factorIdKey": String!
```

## Public constructors

### MultiFactorInfo

```
MultiFactorInfo()
```

## Public functions

### getDisplayName

```
abstract fun getDisplayName(): String?
```

Returns the user-given display name for this second factor.

### getEnrollmentTimestamp

```
abstract fun getEnrollmentTimestamp(): Long
```

Returns the enrollment timestamp for this second factor in seconds since epoch (UTC midnight on January 1, 1970).

### getFactorId

```
abstract fun getFactorId(): String
```

Returns the factor id of this second factor. You can match this with a generator factor id (e.g. `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID()`) to determine to which direct subclass this can be cast.

### getUid

```
abstract fun getUid(): String
```

Returns the unique identifier for this second factor.