# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType.md.txt

# BinaryType

# BinaryType


```
enum BinaryType
```

<br />

*** ** * ** ***

Enum of Android app binary types, used in [AppDistributionRelease](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease).

## Summary

|                                               ### Enum Values                                               |
|-------------------------------------------------------------------------------------------------------------|------------------------------|
| [AAB](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType#AAB) | Android App Bundle.          |
| [APK](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType#APK) | Android Application Package. |

|                                                                                                ### Public functions                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[BinaryType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType)`!`                                                                                    | [valueOf](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType#valueOf(java.lang.String))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!)` Returns the enum constant of this type with the specified name. |
| `java-static `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[BinaryType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType)`!>!` | [values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                                |

## Enum Values

### AAB

```
valÂ BinaryType.AAB:Â BinaryType
```

Android App Bundle.  

### APK

```
valÂ BinaryType.APK:Â BinaryType
```

Android Application Package.  

## Public functions

### valueOf

```
java-staticÂ funÂ valueOf(name:Â String!):Â BinaryType!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                      Returns                                                      |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [BinaryType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType)`!` | the enum constant with the specified name |

|                                                                               Throws                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `java.lang.IllegalArgumentException: `[java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html) | if this enum type has no constant with the specified name |

### values

```
java-staticÂ funÂ values():Â Array<BinaryType!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|                                                                                               Returns                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[BinaryType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType)`!>!` | an array containing the constants of this enum type, in the order they're declared |