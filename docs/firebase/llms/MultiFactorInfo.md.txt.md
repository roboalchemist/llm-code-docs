# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo.md.txt

# MultiFactorInfo

# MultiFactorInfo


```
public abstract class MultiFactorInfo implements Parcelable
```

<br />

Known direct subclasses [PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo), [TotpMultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorInfo)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo` | Represents the information for a phone second factor. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorInfo` | Represents the information for a TOTP (time-based one-time password) second factor. |

*** ** * ** ***

Represents a single second factor meant for the user. See direct subclasses for type-specific information.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo#FACTOR_ID_KEY() = "factorIdKey"` |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo#MultiFactorInfo()()` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo#getDisplayName()()` Returns the user-given display name for this second factor. |
| `abstract long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo#getEnrollmentTimestamp()()` Returns the enrollment timestamp for this second factor in seconds since epoch (UTC midnight on January 1, 1970). |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo#getFactorId()()` Returns the factor id of this second factor. |
| `abstract @https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo#getUid()()` Returns the unique identifier for this second factor. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | | `abstract void` | `https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int)(https://developer.android.com/reference/android/os/Parcel.html p, int p1)` | |

## Constants

### FACTOR_ID_KEY

```
public static final String FACTOR_ID_KEY = "factorIdKey"
```

## Public constructors

### MultiFactorInfo

```
public MultiFactorInfo()
```

## Public methods

### getDisplayName

```
public abstract @Nullable String getDisplayName()
```

Returns the user-given display name for this second factor.

### getEnrollmentTimestamp

```
public abstract long getEnrollmentTimestamp()
```

Returns the enrollment timestamp for this second factor in seconds since epoch (UTC midnight on January 1, 1970).

### getFactorId

```
public abstract @NonNull String getFactorId()
```

Returns the factor id of this second factor. You can match this with a generator factor id (e.g. `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID()`) to determine to which direct subclass this can be cast.

### getUid

```
public abstract @NonNull String getUid()
```

Returns the unique identifier for this second factor.