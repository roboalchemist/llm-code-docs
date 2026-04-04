# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus.md.txt

# FirebaseAnalytics.ConsentStatus

# FirebaseAnalytics.ConsentStatus


```
public enum FirebaseAnalytics.ConsentStatus
```

<br />

*** ** * ** ***

The status value of the consent type. Supported statuses are `GRANTED` and `
DENIED`.

## Summary

|                                                           ### Enum Values                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| [DENIED](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED)   | Consent status indicating consent is denied.  |
| [GRANTED](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#GRANTED) | Consent status indicating consent is granted. |

|                                                                      ### Public methods                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static `[FirebaseAnalytics.ConsentStatus](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus) | [valueOf](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#valueOf(java.lang.String))`(`[String](https://developer.android.com/reference/java/lang/String.html)` name)` Returns the enum constant of this type with the specified name. |
| `static FirebaseAnalytics.ConsentStatus[]`                                                                                                                   | [values](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                     |

## Enum Values

### DENIED

```
FirebaseAnalytics.ConsentStatusÂ FirebaseAnalytics.ConsentStatus.DENIED
```

Consent status indicating consent is denied. For an overview of which data is sent when consent is denied, see [SDK behavior with consent mode](https://developers.google.com/tag-platform/security/concepts/consent-mode#tag-behavior).  

### GRANTED

```
FirebaseAnalytics.ConsentStatusÂ FirebaseAnalytics.ConsentStatus.GRANTED
```

Consent status indicating consent is granted.  

## Public methods

### valueOf

```
publicÂ staticÂ FirebaseAnalytics.ConsentStatusÂ valueOf(StringÂ name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                                       Returns                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [FirebaseAnalytics.ConsentStatus](https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus) | the enum constant with the specified name |

|                                                        Throws                                                         |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [java.lang.IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException.html) | if this enum type has no constant with the specified name |

### values

```
publicÂ staticÂ FirebaseAnalytics.ConsentStatus[]Â values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|               Returns               |
|-------------------------------------|------------------------------------------------------------------------------------|
| `FirebaseAnalytics.ConsentStatus[]` | an array containing the constants of this enum type, in the order they're declared |