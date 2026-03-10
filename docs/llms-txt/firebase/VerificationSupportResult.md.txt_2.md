# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult.md.txt

# VerificationSupportResult

# VerificationSupportResult


```
class VerificationSupportResult : Parcelable
```

<br />

*** ** * ** ***

Represents the result of a verification support check.

## Summary

| ### Public companion properties |
|---|---|
| `https://developer.android.com/reference/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult#CREATOR()` Parcelable.Creator for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult`. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult#VerificationSupportResult(kotlin.Int,kotlin.String,kotlin.Int)( simSlotIndex: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, carrierId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, reason: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html )` |

| ### Public functions |
|---|---|
| `final https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult#describeContents()()` |
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult#getCarrierId()()` Returns the operator name of the SIM card. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult#getReason()()` Returns the capability status of the SIM card. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult#getSimSlot()()` Returns the index of the SIM slot. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult#hashCode()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult#isSupported()()` Indicates whether the verification capability is supported. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult#writeToParcel(android.os.Parcel,kotlin.Int)(dest: https://developer.android.com/reference/android/os/Parcel.html, flags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Writes the object's data to a `https://developer.android.com/reference/android/os/Parcel.html`. |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#getStability()()` | |

## Public companion properties

### CREATOR

```
val CREATOR: Parcelable.Creator<VerificationSupportResult>
```

Parcelable.Creator for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/pnv/VerificationSupportResult`.

## Public constructors

### VerificationSupportResult

```
VerificationSupportResult(
    simSlotIndex: Int,
    carrierId: String,
    reason: Int
)
```

## Public functions

### describeContents

```
final fun describeContents(): Int
```

### equals

```
open operator fun equals(other: Any?): Boolean
```

### getCarrierId

```
fun getCarrierId(): String
```

Returns the operator name of the SIM card.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The operator name of the SIM card. |

### getReason

```
fun getReason(): Int
```

Returns the capability status of the SIM card.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The capability status of the SIM card. |

### getSimSlot

```
fun getSimSlot(): Int
```

Returns the index of the SIM slot.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | The index of the SIM slot. |

### hashCode

```
open fun hashCode(): Int
```

### isSupported

```
fun isSupported(): Boolean
```

Indicates whether the verification capability is supported.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `true` if the capability is supported, `false` otherwise. |

### writeToParcel

```
open fun writeToParcel(dest: Parcel, flags: Int): Unit
```

Writes the object's data to a `https://developer.android.com/reference/android/os/Parcel.html`.

| Parameters |
|---|---|
| `dest: https://developer.android.com/reference/android/os/Parcel.html` | The `https://developer.android.com/reference/android/os/Parcel.html` in which the object should be written. |
| `flags: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | Additional flags about how the object should be written. |