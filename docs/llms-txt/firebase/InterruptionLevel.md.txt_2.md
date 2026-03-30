# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel.md.txt

# InterruptionLevel

# InterruptionLevel


```
enum InterruptionLevel
```

<br />

*** ** * ** ***

An enum specifying the level of interruption of a notification when it is created.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel#DEFAULT` | Default interruption level. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel#HIGH` | High interruption level. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel#LOW` | Low interruption level. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel#MAX` | Maximum interruption level. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel#MIN` | Minimum interruption level. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### DEFAULT

```
val InterruptionLevel.DEFAULT: InterruptionLevel
```

Default interruption level.

Translates to `https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_DEFAULT--` on Android O+ and `https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_DEFAULT--` on older platforms.

### HIGH

```
val InterruptionLevel.HIGH: InterruptionLevel
```

High interruption level.

Translates to `https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_HIGH--` on Android O+ and `https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_HIGH--` on older platforms.

### LOW

```
val InterruptionLevel.LOW: InterruptionLevel
```

Low interruption level.

Translates to `https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_LOW--` on Android O+ and `https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_LOW--` on older platforms.

### MAX

```
val InterruptionLevel.MAX: InterruptionLevel
```

Maximum interruption level.

Translates to `https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_HIGH--` on Android O+ and `https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_MAX--` on older platforms.

### MIN

```
val InterruptionLevel.MIN: InterruptionLevel
```

Minimum interruption level.

Translates to `https://developer.android.com/reference/kotlin/android/app/NotificationManager.html#IMPORTANCE_MIN--` on Android O+ and `https://developer.android.com/reference/kotlin/androidx/core/app/NotificationCompat.html#PRIORITY_MIN--` on older platforms.

## Public functions

### valueOf

```
java-static fun valueOf(name: String!): InterruptionLevel!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel!` | the enum constant with the specified name |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<InterruptionLevel!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/InterruptionLevel!>!` | an array containing the constants of this enum type, in the order they're declared |