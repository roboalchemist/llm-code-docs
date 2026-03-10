# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType.md.txt

# BinaryType

# BinaryType


```
public enum BinaryType
```

<br />

*** ** * ** ***

Enum of Android app binary types, used in `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/AppDistributionRelease`.

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType#AAB` | Android App Bundle. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType#APK` | Android Application Package. |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static BinaryType[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### AAB

```
BinaryType BinaryType.AAB
```

Android App Bundle.

### APK

```
BinaryType BinaryType.APK
```

Android Application Package.

## Public methods

### valueOf

```
public static BinaryType valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/appdistribution/BinaryType` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static BinaryType[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `BinaryType[]` | an array containing the constants of this enum type, in the order they're declared |