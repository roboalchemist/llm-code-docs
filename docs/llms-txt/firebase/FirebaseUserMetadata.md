# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/FirebaseUserMetadata.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUserMetadata.md.txt

# FirebaseUserMetadata

# FirebaseUserMetadata


```
public interface FirebaseUserMetadata extends Parcelable
```

<br />

*** ** * ** ***

Holds the user metadata for the current [FirebaseUser](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUser)

## Summary

| ### Public methods |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract long`    | [getCreationTimestamp](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUserMetadata#getCreationTimestamp())`()` Returns the timestamp at which this account was created as dictated by the server clock in milliseconds since epoch. |
| `abstract long`    | [getLastSignInTimestamp](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/FirebaseUserMetadata#getLastSignInTimestamp())`()` Returns the last signin timestamp as dictated by the server clock in milliseconds since epoch.                   |

|                                                                                                                                                                                                                                                                                                      ### Inherited Constants                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `default static final int` | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `default static final int` | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                                                                                                                                                                                                                                                  ### Inherited methods                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `abstract int`  | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()`                                                                                                     | | `abstract void` | [writeToParcel](https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int))`(`[Parcel](https://developer.android.com/reference/android/os/Parcel.html)` p, int p1)` | |

## Public methods

### getCreationTimestamp

```
abstractÂ longÂ getCreationTimestamp()
```

Returns the timestamp at which this account was created as dictated by the server clock in milliseconds since epoch.  

### getLastSignInTimestamp

```
abstractÂ longÂ getLastSignInTimestamp()
```

Returns the last signin timestamp as dictated by the server clock in milliseconds since epoch. This is only accurate up to a granularity of 2 minutes for consecutive sign-in attempts.