# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorInfo.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/MultiFactorInfo.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo.md.txt

# MultiFactorInfo

# MultiFactorInfo


```
abstract class MultiFactorInfo : Parcelable
```

<br />

Known direct subclasses  
[PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo), [TotpMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo)  

|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo) | Represents the information for a phone second factor.                               |
| [TotpMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/TotpMultiFactorInfo)   | Represents the information for a TOTP (time-based one-time password) second factor. |

*** ** * ** ***

Represents a single second factor meant for the user. See direct subclasses for type-specific information.

## Summary

|                                        ### Constants                                        |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [FACTOR_ID_KEY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#FACTOR_ID_KEY())` = "factorIdKey"` |

|                                                       ### Public constructors                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------|
| [MultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#MultiFactorInfo())`()` |

|                                      ### Public functions                                      |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [getDisplayName](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#getDisplayName())`()` Returns the user-given display name for this second factor.                                                                       |
| `abstract `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)        | [getEnrollmentTimestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#getEnrollmentTimestamp())`()` Returns the enrollment timestamp for this second factor in seconds since epoch (UTC midnight on January 1, 1970). |
| `abstract `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)    | [getFactorId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#getFactorId())`()` Returns the factor id of this second factor.                                                                                            |
| `abstract `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)    | [getUid](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#getUid())`()` Returns the unique identifier for this second factor.                                                                                             |

|                                                                                                                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ### Inherited functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `abstract `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)   | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()`                                                                                                                                                                                 | | `abstract `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [writeToParcel](https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int))`(p: `[Parcel](https://developer.android.com/reference/android/os/Parcel.html)`!, p1: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` | |

## Constants

### FACTOR_ID_KEY

```
constÂ valÂ FACTOR_ID_KEY = "factorIdKey":Â String!
```  

## Public constructors

### MultiFactorInfo

```
MultiFactorInfo()
```  

## Public functions

### getDisplayName

```
abstractÂ funÂ getDisplayName():Â String?
```

Returns the user-given display name for this second factor.  

### getEnrollmentTimestamp

```
abstractÂ funÂ getEnrollmentTimestamp():Â Long
```

Returns the enrollment timestamp for this second factor in seconds since epoch (UTC midnight on January 1, 1970).  

### getFactorId

```
abstractÂ funÂ getFactorId():Â String
```

Returns the factor id of this second factor. You can match this with a generator factor id (e.g. [FACTOR_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID())) to determine to which direct subclass this can be cast.  

### getUid

```
abstractÂ funÂ getUid():Â String
```

Returns the unique identifier for this second factor.