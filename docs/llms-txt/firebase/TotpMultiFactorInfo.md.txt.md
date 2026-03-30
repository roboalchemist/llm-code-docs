# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorInfo.md.txt

# TotpMultiFactorInfo

# TotpMultiFactorInfo


```
public class TotpMultiFactorInfo extends MultiFactorInfo
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||
| ↳ | [com.google.firebase.auth.MultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo) ||
|   | ↳ | [com.google.firebase.auth.TotpMultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorInfo) |

*** ** * ** ***

Represents the information for a TOTP (time-based one-time password) second factor.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorInfo#displayName()` |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorInfo#enrollmentTimestamp()` |
| `final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorInfo#uid()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorInfo#getDisplayName()()` Returns the user-given display name for this second factor. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorInfo#getEnrollmentTimestamp()()` Returns the enrollment timestamp for this second factor in seconds since epoch (UTC midnight on January 1, 1970). |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorInfo#getFactorId()()` Returns `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorGenerator#FACTOR_ID()`, identifying this as a TotpMultiFactorInfo. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorInfo#getUid()()` Returns the unique identifier for this second factor. |

| ### Inherited Constants |
|---|
| From [com.google.firebase.auth.MultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo) |---|---| | `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo#FACTOR_ID_KEY() = "factorIdKey"` | |
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Public fields

### displayName

```
public final @Nullable String displayName
```

### enrollmentTimestamp

```
public final long enrollmentTimestamp
```

### uid

```
public final String uid
```

## Public methods

### getDisplayName

```
public @Nullable String getDisplayName()
```

Returns the user-given display name for this second factor.

### getEnrollmentTimestamp

```
public long getEnrollmentTimestamp()
```

Returns the enrollment timestamp for this second factor in seconds since epoch (UTC midnight on January 1, 1970).

### getFactorId

```
public @NonNull String getFactorId()
```

Returns `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/TotpMultiFactorGenerator#FACTOR_ID()`, identifying this as a TotpMultiFactorInfo.

### getUid

```
public @NonNull String getUid()
```

Returns the unique identifier for this second factor.