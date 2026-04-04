# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel.md.txt

# InterruptionLevel

# InterruptionLevel


```
public enum InterruptionLevel
```

<br />

*** ** * ** ***

An enum specifying the level of interruption of a notification when it is created.

## Summary

|                                                       ### Enum Values                                                       |
|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| [DEFAULT](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#DEFAULT) | Default interruption level. |
| [HIGH](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#HIGH)       | High interruption level.    |
| [LOW](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#LOW)         | Low interruption level.     |
| [MAX](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#MAX)         | Maximum interruption level. |
| [MIN](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#MIN)         | Minimum interruption level. |

|                                                           ### Public methods                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static `[InterruptionLevel](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel) | [valueOf](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#valueOf(java.lang.String))`(`[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` name)` Returns the enum constant of this type with the specified name. |
| `static InterruptionLevel[]`                                                                                                           | [values](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                            |

## Enum Values

### DEFAULT

```
InterruptionLevelÂ InterruptionLevel.DEFAULT
```

Default interruption level.

Translates to [IMPORTANCE_DEFAULT](https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_DEFAULT--) on Android O+ and [PRIORITY_DEFAULT](https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_DEFAULT--) on older platforms.  

### HIGH

```
InterruptionLevelÂ InterruptionLevel.HIGH
```

High interruption level.

Translates to [IMPORTANCE_HIGH](https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_HIGH--) on Android O+ and [PRIORITY_HIGH](https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_HIGH--) on older platforms.  

### LOW

```
InterruptionLevelÂ InterruptionLevel.LOW
```

Low interruption level.

Translates to [IMPORTANCE_LOW](https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_LOW--) on Android O+ and [PRIORITY_LOW](https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_LOW--) on older platforms.  

### MAX

```
InterruptionLevelÂ InterruptionLevel.MAX
```

Maximum interruption level.

Translates to [IMPORTANCE_HIGH](https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_HIGH--) on Android O+ and [PRIORITY_MAX](https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_MAX--) on older platforms.  

### MIN

```
InterruptionLevelÂ InterruptionLevel.MIN
```

Minimum interruption level.

Translates to [IMPORTANCE_MIN](https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_MIN--) on Android O+ and [PRIORITY_MIN](https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_MIN--) on older platforms.  

## Public methods

### valueOf

```
publicÂ staticÂ InterruptionLevelÂ valueOf(StringÂ name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                            Returns                                                            |
|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [InterruptionLevel](https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel) | the enum constant with the specified name |

|                                                                              Throws                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html)` java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
publicÂ staticÂ InterruptionLevel[]Â values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|        Returns        |
|-----------------------|------------------------------------------------------------------------------------|
| `InterruptionLevel[]` | an array containing the constants of this enum type, in the order they're declared |