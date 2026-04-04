# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType.md.txt

# BinaryType

# BinaryType


```
enum BinaryType
```

<br />

*** ** * ** ***

Enum of Android app binary types, used in `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease`.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType#AAB` | Android App Bundle. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType#APK` | Android Application Package. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### AAB

```
val BinaryType.AAB: BinaryType
```

Android App Bundle.

### APK

```
val BinaryType.APK: BinaryType
```

Android Application Package.

## Public functions

### valueOf

```
java-static fun valueOf(name: String!): BinaryType!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType!` | the enum constant with the specified name |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<BinaryType!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType!>!` | an array containing the constants of this enum type, in the order they're declared |