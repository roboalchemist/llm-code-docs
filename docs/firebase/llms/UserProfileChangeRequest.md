# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/UserProfileChangeRequest.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/UserProfileChangeRequest.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest.md.txt

# UserProfileChangeRequest

# UserProfileChangeRequest


```
public class UserProfileChangeRequest implements Parcelable
```

<br />

*** ** * ** ***

Request used to update user profile information.

## Summary

|                                                                                   ### Nested types                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `public class `[UserProfileChangeRequest.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest.Builder) The request builder. |

|                                                                         ### Public fields                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html) | [displayName](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest#displayName()) |
| `@`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[Uri](https://developer.android.com/reference/android/net/Uri.html)     | [photoUri](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest#photoUri())       |

|                                                                         ### Public methods                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/java/lang/String.html) | [getDisplayName](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest#getDisplayName())`()` Returns the displayName for this change request. |
| `@`[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html)` `[Uri](https://developer.android.com/reference/android/net/Uri.html)     | [getPhotoUri](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest#getPhotoUri())`()` Returns the photoUri for this change request.          |

|                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |--------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `static final int` | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `static final int` | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                         ### Inherited methods                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |----------------|---------------------------------------------------------------------------------------------------------------| | `abstract int` | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()` | |

## Public fields

### displayName

```
publicÂ @Nullable StringÂ displayName
```  

### photoUri

```
publicÂ @Nullable UriÂ photoUri
```  

## Public methods

### getDisplayName

```
publicÂ @Nullable StringÂ getDisplayName()
```

Returns the displayName for this change request.  

### getPhotoUri

```
publicÂ @Nullable UriÂ getPhotoUri()
```

Returns the photoUri for this change request.