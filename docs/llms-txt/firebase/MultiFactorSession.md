# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/auth/MultiFactorSession.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession.md.txt

# MultiFactorSession

# MultiFactorSession


```
abstract class MultiFactorSession : Parcelable
```

<br />

*** ** * ** ***

Identifies the current session to enroll a second factor or to complete sign in when previously enrolled. It contains additional context on the existing user, notably the confirmation that the user passed the first factor challenge.

## Summary

|                                                           ### Public constructors                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------|
| [MultiFactorSession](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/auth/MultiFactorSession#MultiFactorSession())`()` |

|                                                                                                                                                                                                                                                                                                                                                                                          ### Inherited Constants                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------| | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [CONTENTS_FILE_DESCRIPTOR](https://developer.android.com/reference/android/os/Parcelable.html#CONTENTS_FILE_DESCRIPTOR())` = 1`           | | `const `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html) | [PARCELABLE_WRITE_RETURN_VALUE](https://developer.android.com/reference/android/os/Parcelable.html#PARCELABLE_WRITE_RETURN_VALUE())` = 1` | |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ### Inherited functions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| From [android.os.Parcelable](https://developer.android.com/reference/android/os/Parcelable.html) |-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `abstract `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)   | [describeContents](https://developer.android.com/reference/android/os/Parcelable.html#describeContents())`()`                                                                                                                                                                                 | | `abstract `[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html) | [writeToParcel](https://developer.android.com/reference/android/os/Parcelable.html#writeToParcel(android.os.Parcel, int))`(p: `[Parcel](https://developer.android.com/reference/android/os/Parcel.html)`!, p1: `[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)`)` | |

## Public constructors

### MultiFactorSession

```
MultiFactorSession()
```