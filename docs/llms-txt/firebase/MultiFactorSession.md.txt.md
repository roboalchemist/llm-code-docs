# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorSession.md.txt

# MultiFactorSession

# MultiFactorSession


```
public abstract class MultiFactorSession implements Parcelable
```

<br />

*** ** * ** ***

Identifies the current session to enroll a second factor or to complete sign in when previously enrolled. It contains additional context on the existing user, notably the confirmation that the user passed the first factor challenge.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorSession#MultiFactorSession()()` |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | | `abstract void` | `https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int)(https://developer.android.com/reference/android/os/Parcel.html p, int p1)` | |

## Public constructors

### MultiFactorSession

```
public MultiFactorSession()
```