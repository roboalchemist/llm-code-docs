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

| ### Nested types |
|---|
| `public class https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest.Builder` The request builder. |

| ### Public fields |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest#displayName()` |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest#photoUri()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest#getDisplayName()()` Returns the displayName for this change request. |
| `@https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/android/net/Uri.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/UserProfileChangeRequest#getPhotoUri()()` Returns the photoUri for this change request. |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | |

## Public fields

### displayName

```
public @Nullable String displayName
```

### photoUri

```
public @Nullable Uri photoUri
```

## Public methods

### getDisplayName

```
public @Nullable String getDisplayName()
```

Returns the displayName for this change request.

### getPhotoUri

```
public @Nullable Uri getPhotoUri()
```

Returns the photoUri for this change request.