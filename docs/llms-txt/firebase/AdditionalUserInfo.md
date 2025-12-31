# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/AdditionalUserInfo.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/AdditionalUserInfo.md.txt

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

|                                                                                                                                                                         ### Public functions                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!>?` | [getProfile](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo#getProfile())`()` Returns a [Map](https://developer.android.com/reference/java/util/Map.html) containing IDP-specific user data if the provider is one of Facebook, GitHub, Google, Twitter, Microsoft, or Yahoo.                 |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                                                                                                                                                                                                                   | [getProviderId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo#getProviderId())`()` Returns the provider ID for specifying which provider the information in [getProfile](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo#getProfile()) is for. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                                                                                                                                                                                                                   | [getUsername](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo#getUsername())`()` Returns the username if the provider is GitHub or Twitter                                                                                                                                                     |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                                                                                                                                                                                                                    | [isNewUser](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo#isNewUser())`()` Returns whether the user is new or existing                                                                                                                                                                       |

|                                                                                                                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ### Inherited functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)   | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()`                                                                                                                                                                                 | | [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [writeToParcel](https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int))`(p: `[Parcel](https://developer.android.com/reference/android/os/Parcel.html)`!, p1: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` | |

## Public functions

### getProfile

```
funÂ getProfile():Â (Mutable)Map<String!,Â Any!>?
```

Returns a [Map](https://developer.android.com/reference/java/util/Map.html) containing IDP-specific user data if the provider is one of Facebook, GitHub, Google, Twitter, Microsoft, or Yahoo.  

### getProviderId

```
funÂ getProviderId():Â String?
```

Returns the provider ID for specifying which provider the information in [getProfile](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/AdditionalUserInfo#getProfile()) is for.  

### getUsername

```
funÂ getUsername():Â String?
```

Returns the username if the provider is GitHub or Twitter  

### isNewUser

```
funÂ isNewUser():Â Boolean
```

Returns whether the user is new or existing