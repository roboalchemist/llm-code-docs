# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUserMetadata.md.txt

# FirebaseUserMetadata

# FirebaseUserMetadata


```
interface FirebaseUserMetadata : Parcelable
```

<br />

*** ** * ** ***

Holds the user metadata for the current `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUser`

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUserMetadata#getCreationTimestamp()()` Returns the timestamp at which this account was created as dictated by the server clock in milliseconds since epoch. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUserMetadata#getLastSignInTimestamp()()` Returns the last signin timestamp as dictated by the server clock in milliseconds since epoch. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int)(p: https://developer.android.com/reference/android/os/Parcel.html!, p1: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | |

## Public functions

### getCreationTimestamp

```
fun getCreationTimestamp(): Long
```

Returns the timestamp at which this account was created as dictated by the server clock in milliseconds since epoch.

### getLastSignInTimestamp

```
fun getLastSignInTimestamp(): Long
```

Returns the last signin timestamp as dictated by the server clock in milliseconds since epoch. This is only accurate up to a granularity of 2 minutes for consecutive sign-in attempts.