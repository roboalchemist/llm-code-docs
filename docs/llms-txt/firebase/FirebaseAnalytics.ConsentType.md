# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType.md.txt

# FirebaseAnalytics.ConsentType

# FirebaseAnalytics.ConsentType


```
enum FirebaseAnalytics.ConsentType
```

<br />

*** ** * ** ***

The type of consent to set. Supported consent types are `AD_STORAGE`, `
ANALYTICS_STORAGE`, `AD_USER_DATA` and `AD_PERSONALIZATION`. Omitting a type retains its previous status.

## Summary

|                                                                    ### Enum Values                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [AD_PERSONALIZATION](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_PERSONALIZATION) | Sets consent for personalized advertising.                                           |
| [AD_STORAGE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_STORAGE)                 | Enables storage (such as device identifiers) related to advertising.                 |
| [AD_USER_DATA](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_USER_DATA)             | Sets consent for sending user data to Google for advertising purposes.               |
| [ANALYTICS_STORAGE](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE)   | Enables storage (such as app identifiers) related to analytics, e.g. visit duration. |

|                                                                                                                ### Public functions                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[FirebaseAnalytics.ConsentType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType)`!`                                                                                    | [valueOf](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#valueOf(java.lang.String))`(name: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!)` Returns the enum constant of this type with the specified name. |
| `java-static `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[FirebaseAnalytics.ConsentType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType)`!>!` | [values](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                                |

## Enum Values

### AD_PERSONALIZATION

```
valÂ FirebaseAnalytics.ConsentType.AD_PERSONALIZATION:Â FirebaseAnalytics.ConsentType
```

Sets consent for personalized advertising.  

### AD_STORAGE

```
valÂ FirebaseAnalytics.ConsentType.AD_STORAGE:Â FirebaseAnalytics.ConsentType
```

Enables storage (such as device identifiers) related to advertising.  

### AD_USER_DATA

```
valÂ FirebaseAnalytics.ConsentType.AD_USER_DATA:Â FirebaseAnalytics.ConsentType
```

Sets consent for sending user data to Google for advertising purposes.  

### ANALYTICS_STORAGE

```
valÂ FirebaseAnalytics.ConsentType.ANALYTICS_STORAGE:Â FirebaseAnalytics.ConsentType
```

Enables storage (such as app identifiers) related to analytics, e.g. visit duration.  

## Public functions

### valueOf

```
java-staticÂ funÂ valueOf(name:Â String!):Â FirebaseAnalytics.ConsentType!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                                      Returns                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [FirebaseAnalytics.ConsentType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType)`!` | the enum constant with the specified name |

|                                                        Throws                                                         |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [java.lang.IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException.html) | if this enum type has no constant with the specified name |

### values

```
java-staticÂ funÂ values():Â Array<FirebaseAnalytics.ConsentType!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|                                                                                                               Returns                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[FirebaseAnalytics.ConsentType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentType)`!>!` | an array containing the constants of this enum type, in the order they're declared |