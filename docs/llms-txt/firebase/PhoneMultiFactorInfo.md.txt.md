# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo.md.txt

# PhoneMultiFactorInfo

# PhoneMultiFactorInfo


```
public class PhoneMultiFactorInfo extends MultiFactorInfo
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object.html) |||
| ↳ | [com.google.firebase.auth.MultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo) ||
|   | ↳ | [com.google.firebase.auth.PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo) |

*** ** * ** ***

Represents the information for a phone second factor.

## Summary

| ### Constants |
|---|---|
| `static final https://developer.android.com/reference/android/os/Parcelable.Creator.html<https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo#CREATOR()` |

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo#displayName()` |
| `final long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo#enrollmentTimestamp()` |
| `final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo#phoneNumber()` |
| `final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo#uid()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo#getDisplayName()()` Returns the user-given display name for this second factor. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo#getEnrollmentTimestamp()()` Returns the enrollment timestamp for this second factor in seconds since epoch (UTC midnight on January 1, 1970). |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo#getFactorId()()` Returns `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID()`, identifying this as a PhoneMultiFactorInfo. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo#getPhoneNumber()()` Returns the phone number associated with this second factor verification method. |
| `@https://developer.android.com/reference/androidx/annotation/NonNull.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo#getUid()()` Returns the unique identifier for this second factor. |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo#writeToParcel(android.os.Parcel,int)(https://developer.android.com/reference/android/os/Parcel.html dest, int flags)` |

| ### Inherited Constants |
|---|
| From [com.google.firebase.auth.MultiFactorInfo](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo) |---|---| | `static final https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo#FACTOR_ID_KEY() = "factorIdKey"` | |
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Constants

### CREATOR

```
public static final Parcelable.Creator<PhoneMultiFactorInfo> CREATOR
```

## Public fields

### displayName

```
public final @Nullable String displayName
```

### enrollmentTimestamp

```
public final long enrollmentTimestamp
```

### phoneNumber

```
public final String phoneNumber
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

Returns `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID()`, identifying this as a PhoneMultiFactorInfo.

### getPhoneNumber

```
public @NonNull String getPhoneNumber()
```

Returns the phone number associated with this second factor verification method.

### getUid

```
public @NonNull String getUid()
```

Returns the unique identifier for this second factor.

### writeToParcel

```
public void writeToParcel(Parcel dest, int flags)
```