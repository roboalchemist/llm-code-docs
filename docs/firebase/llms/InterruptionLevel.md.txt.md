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

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#DEFAULT` | Default interruption level. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#HIGH` | High interruption level. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#LOW` | Low interruption level. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#MAX` | Maximum interruption level. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#MIN` | Minimum interruption level. |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static InterruptionLevel[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### DEFAULT

```
InterruptionLevel InterruptionLevel.DEFAULT
```

Default interruption level.

Translates to `https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_DEFAULT--` on Android O+ and `https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_DEFAULT--` on older platforms.

### HIGH

```
InterruptionLevel InterruptionLevel.HIGH
```

High interruption level.

Translates to `https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_HIGH--` on Android O+ and `https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_HIGH--` on older platforms.

### LOW

```
InterruptionLevel InterruptionLevel.LOW
```

Low interruption level.

Translates to `https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_LOW--` on Android O+ and `https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_LOW--` on older platforms.

### MAX

```
InterruptionLevel InterruptionLevel.MAX
```

Maximum interruption level.

Translates to `https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_HIGH--` on Android O+ and `https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_MAX--` on older platforms.

### MIN

```
InterruptionLevel InterruptionLevel.MIN
```

Minimum interruption level.

Translates to `https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_MIN--` on Android O+ and `https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_MIN--` on older platforms.

## Public methods

### valueOf

```
public static InterruptionLevel valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/InterruptionLevel` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static InterruptionLevel[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `InterruptionLevel[]` | an array containing the constants of this enum type, in the order they're declared |