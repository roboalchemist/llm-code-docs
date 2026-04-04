# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/PhoneMultiFactorInfo.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorInfo.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/PhoneMultiFactorInfo.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo.md.txt

# PhoneMultiFactorInfo

# PhoneMultiFactorInfo


```
class PhoneMultiFactorInfo : MultiFactorInfo
```

<br />

|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)                                                                      |||
| â³ | [com.google.firebase.auth.MultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo)              ||
|   | â³ | [com.google.firebase.auth.PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo) |

*** ** * ** ***

Represents the information for a phone second factor.

## Summary

|                                                                                                              ### Constants                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| `const `[Parcelable.Creator](https://developer.android.com/reference/android/os/Parcelable.Creator.html)`<`[PhoneMultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo)`!>!` | [CREATOR](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#CREATOR()) |

|                               ### Public functions                               |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [getFactorId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#getFactorId())`()` Returns [FACTOR_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID()), identifying this as a PhoneMultiFactorInfo.             |
| [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)     | [writeToParcel](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#writeToParcel(android.os.Parcel,int))`(dest: `[Parcel](https://developer.android.com/reference/android/os/Parcel.html)`!, flags: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` |

|                                ### Public properties                                |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | [displayName](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#displayName())                 |
| [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)        | [enrollmentTimestamp](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#enrollmentTimestamp()) |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [phoneNumber](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#phoneNumber())                 |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [uid](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorInfo#uid())                                 |

|                                                                                                                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [com.google.firebase.auth.MultiFactorInfo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo) |---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------| | `const `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [FACTOR_ID_KEY](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorInfo#FACTOR_ID_KEY())` = "factorIdKey"` |                                                                                                                                                               |
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                                                                                               ### Inherited functions                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------| | `abstract `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()` | |

## Constants

### CREATOR

```
constÂ valÂ CREATOR:Â Parcelable.Creator<PhoneMultiFactorInfo!>!
```  

## Public functions

### getFactorId

```
funÂ getFactorId():Â String
```

Returns [FACTOR_ID](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/PhoneMultiFactorGenerator#FACTOR_ID()), identifying this as a PhoneMultiFactorInfo.  

### writeToParcel

```
funÂ writeToParcel(dest:Â Parcel!,Â flags:Â Int):Â Unit
```  

## Public properties

### displayName

```
valÂ displayName:Â String?
```  

### enrollmentTimestamp

```
valÂ enrollmentTimestamp:Â Long
```  

### phoneNumber

```
valÂ phoneNumber:Â String!
```  

### uid

```
valÂ uid:Â String!
```