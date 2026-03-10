# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AdditionalUserInfo.md.txt

# AdditionalUserInfo

# AdditionalUserInfo


```
public interface AdditionalUserInfo extends Parcelable
```

<br />

*** ** * ** ***

Object that contains additional user information as a result of a successful sign-in, link, or re-authentication operation.

Available information contained within depends on the provider with which a sign-in, link, or re-authenticate operation was most recently done.

## Summary

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/util/Map.html<https://developer.android.com/reference/java/lang/String.html, https://developer.android.com/reference/java/lang/Object.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AdditionalUserInfo#getProfile()()` Returns a `https://developer.android.com/reference/java/util/Map.html` containing IDP-specific user data if the provider is one of Facebook, GitHub, Google, Twitter, Microsoft, or Yahoo. |
| `abstract @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AdditionalUserInfo#getProviderId()()` Returns the provider ID for specifying which provider the information in `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AdditionalUserInfo#getProfile()` is for. |
| `abstract @https://developer.android.com/reference/androidx/annotation/Nullable.html https://developer.android.com/reference/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AdditionalUserInfo#getUsername()()` Returns the username if the provider is GitHub or Twitter |
| `abstract boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AdditionalUserInfo#isNewUser()()` Returns whether the user is new or existing |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `default static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `default static final int` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited methods |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `abstract int` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | | `abstract void` | `https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int)(https://developer.android.com/reference/android/os/Parcel.html p, int p1)` | |

## Public methods

### getProfile

```
abstract @Nullable Map<String, Object> getProfile()
```

Returns a `https://developer.android.com/reference/java/util/Map.html` containing IDP-specific user data if the provider is one of Facebook, GitHub, Google, Twitter, Microsoft, or Yahoo.

### getProviderId

```
abstract @Nullable String getProviderId()
```

Returns the provider ID for specifying which provider the information in `https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AdditionalUserInfo#getProfile()` is for.

### getUsername

```
abstract @Nullable String getUsername()
```

Returns the username if the provider is GitHub or Twitter

### isNewUser

```
abstract boolean isNewUser()
```

Returns whether the user is new or existing