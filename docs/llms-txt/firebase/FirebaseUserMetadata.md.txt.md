# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUserMetadata.md.txt

# FirebaseUserMetadata

# FirebaseUserMetadata


```
public interface FirebaseUserMetadata extends Parcelable
```

<br />

*** ** * ** ***

Holds the user metadata for the current `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser`

## Summary

| ### Public methods |
|---|---|
| `abstract long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUserMetadata#getCreationTimestamp()()` Returns the timestamp at which this account was created as dictated by the server clock in milliseconds since epoch. |
| `abstract long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUserMetadata#getLastSignInTimestamp()()` Returns the last signin timestamp as dictated by the server clock in milliseconds since epoch. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `default static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `default static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | | `abstract void` | `https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int)(https://developer.android.com/reference/android/os/Parcel.html p, int p1)` | |

## Public methods

### getCreationTimestamp

```
abstract long getCreationTimestamp()
```

Returns the timestamp at which this account was created as dictated by the server clock in milliseconds since epoch.

### getLastSignInTimestamp

```
abstract long getLastSignInTimestamp()
```

Returns the last signin timestamp as dictated by the server clock in milliseconds since epoch. This is only accurate up to a granularity of 2 minutes for consecutive sign-in attempts.