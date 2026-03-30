# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo.md.txt

# PhoneMultiFactorInfo

# PhoneMultiFactorInfo


```
class PhoneMultiFactorInfo : MultiFactorInfo
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.auth.MultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo) ||
|   | ↳ | [com.google.firebase.auth.PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo) |

*** ** * ** ***

Represents the information for a phone second factor.

## Summary

| ### Constants |
|---|---|
| `const https://developer.android.com/reference/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#CREATOR()` |

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#getFactorId()()` Returns `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID()`, identifying this as a PhoneMultiFactorInfo. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#writeToParcel(android.os.Parcel,int)(dest: https://developer.android.com/reference/android/os/Parcel.html!, flags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#displayName()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#enrollmentTimestamp()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#phoneNumber()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#uid()` |

| ### Inherited Constants |
|---|
| From [com.google.firebase.auth.MultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#FACTOR_ID_KEY() = "factorIdKey"` | |
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Constants

### CREATOR

```
const val CREATOR: Parcelable.Creator<PhoneMultiFactorInfo!>!
```

## Public functions

### getFactorId

```
fun getFactorId(): String
```

Returns `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID()`, identifying this as a PhoneMultiFactorInfo.

### writeToParcel

```
fun writeToParcel(dest: Parcel!, flags: Int): Unit
```

## Public properties

### displayName

```
val displayName: String?
```

### enrollmentTimestamp

```
val enrollmentTimestamp: Long
```

### phoneNumber

```
val phoneNumber: String!
```

### uid

```
val uid: String!
```