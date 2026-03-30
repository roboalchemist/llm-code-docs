# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserProfileChangeRequest.md.txt

# UserProfileChangeRequest

# UserProfileChangeRequest


```
class UserProfileChangeRequest : Parcelable
```

<br />

*** ** * ** ***

Request used to update user profile information.

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserProfileChangeRequest.Builder` The request builder. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserProfileChangeRequest#displayName()` |
| `https://developer.android.com/reference/android/net/Uri.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserProfileChangeRequest#photoUri()` |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Public properties

### displayName

```
val displayName: String?
```

### photoUri

```
val photoUri: Uri?
```