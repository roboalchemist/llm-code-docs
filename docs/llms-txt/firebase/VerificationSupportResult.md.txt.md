# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult.md.txt

# VerificationSupportResult

# VerificationSupportResult


```
public final class VerificationSupportResult implements Parcelable
```

<br />

*** ** * ** ***

Represents the result of a verification support check.

## Summary

| ### Public fields |
|---|---|
| `static final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/os/Parcelable.Creator.html<@https://developer.android.com/reference/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult#CREATOR()` Parcelable.Creator for `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult`. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult#VerificationSupportResult(kotlin.Int,kotlin.String,kotlin.Int)( int simSlotIndex, @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html carrierId, int reason )` |

| ### Public methods |
|---|---|
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult#describeContents()()` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult#equals(kotlin.Any)(https://developer.android.com/reference/java/lang/Object.html other)` |
| `final @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult#getCarrierId()()` Returns the operator name of the SIM card. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult#getReason()()` Returns the capability status of the SIM card. |
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult#getSimSlot()()` Returns the index of the SIM slot. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult#hashCode()()` |
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult#isSupported()()` Indicates whether the verification capability is supported. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult#writeToParcel(android.os.Parcel,kotlin.Int)(@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/os/Parcel.html dest, int flags)` Writes the object's data to a `https://developer.android.com/reference/android/os/Parcel.html`. |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `int` | `https://developer.android.com/reference/android/os/Parcelable.html#getStability()()` | |

## Public fields

### CREATOR

```
public static final @NonNull Parcelable.Creator<@NonNull VerificationSupportResult> CREATOR
```

Parcelable.Creator for `https://firebase.google.com/docs/reference/android/com/google/firebase/pnv/VerificationSupportResult`.

## Public constructors

### VerificationSupportResult

```
public VerificationSupportResult(
    int simSlotIndex,
    @NonNull String carrierId,
    int reason
)
```

## Public methods

### describeContents

```
public final int describeContents()
```

### equals

```
public boolean equals(Object other)
```

### getCarrierId

```
public final @NonNull String getCarrierId()
```

Returns the operator name of the SIM card.

| Returns |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | The operator name of the SIM card. |

### getReason

```
public final int getReason()
```

Returns the capability status of the SIM card.

| Returns |
|---|---|
| `int` | The capability status of the SIM card. |

### getSimSlot

```
public final int getSimSlot()
```

Returns the index of the SIM slot.

| Returns |
|---|---|
| `int` | The index of the SIM slot. |

### hashCode

```
public int hashCode()
```

### isSupported

```
public final boolean isSupported()
```

Indicates whether the verification capability is supported.

| Returns |
|---|---|
| `boolean` | `true` if the capability is supported, `false` otherwise. |

### writeToParcel

```
public void writeToParcel(@NonNull Parcel dest, int flags)
```

Writes the object's data to a `https://developer.android.com/reference/android/os/Parcel.html`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/android/os/Parcel.html dest` | The `https://developer.android.com/reference/android/os/Parcel.html` in which the object should be written. |
| `int flags` | Additional flags about how the object should be written. |