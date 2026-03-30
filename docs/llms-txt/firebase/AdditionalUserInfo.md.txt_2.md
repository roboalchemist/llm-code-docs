# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo.md.txt

# AdditionalUserInfo

# AdditionalUserInfo


```
interface AdditionalUserInfo : Parcelable
```

<br />

*** ** * ** ***

Object that contains additional user information as a result of a successful sign-in, link, or re-authentication operation.

Available information contained within depends on the provider with which a sign-in, link, or re-authenticate operation was most recently done.

## Summary

| ### Public functions |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo#getProfile()()` Returns a `https://developer.android.com/reference/java/util/Map.html` containing IDP-specific user data if the provider is one of Facebook, GitHub, Google, Twitter, Microsoft, or Yahoo. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo#getProviderId()()` Returns the provider ID for specifying which provider the information in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo#getProfile()` is for. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo#getUsername()()` Returns the username if the provider is GitHub or Twitter |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo#isNewUser()()` Returns whether the user is new or existing |

| ### Inherited Constants |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR() = 1` | | `const https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE() = 1` | |

| ### Inherited functions |
|---|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---|---| | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#describeContents()()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int)(p: https://developer.android.com/reference/android/os/Parcel.html!, p1: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` | |

## Public functions

### getProfile

```
fun getProfile(): (Mutable)Map<String!, Any!>?
```

Returns a `https://developer.android.com/reference/java/util/Map.html` containing IDP-specific user data if the provider is one of Facebook, GitHub, Google, Twitter, Microsoft, or Yahoo.

### getProviderId

```
fun getProviderId(): String?
```

Returns the provider ID for specifying which provider the information in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo#getProfile()` is for.

### getUsername

```
fun getUsername(): String?
```

Returns the username if the provider is GitHub or Twitter

### isNewUser

```
fun isNewUser(): Boolean
```

Returns whether the user is new or existing