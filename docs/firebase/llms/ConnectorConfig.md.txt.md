# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig.md.txt

# ConnectorConfig

# ConnectorConfig


```
class ConnectorConfig
```

<br />

*** ** * ** ***

Information about a Firebase Data Connect "connector" that is used by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` to connect to the correct Google Cloud resources.

### Safe for concurrent use

All methods and properties of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` are thread-safe and may be safely called and/or accessed concurrently from multiple threads and/or coroutines.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig#ConnectorConfig(kotlin.String,kotlin.String,kotlin.String)(connector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, location: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, serviceId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |

| ### Public functions |
|---|---|
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig#hashCode()()` Calculates and returns the hash code for this object. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig#toString()()` Returns a string representation of this object, useful for debugging. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig#connector()` The ID of the Firebase Data Connect "connector". |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig#location()` The location where the connector is located (for example, `"us-central1"`). |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig#serviceId()` The ID of the Firebase Data Connect service. |

| ### Extension functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig#(com.google.firebase.dataconnect.ConnectorConfig).copy(kotlin.String,kotlin.String,kotlin.String)( connector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, location: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, serviceId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html )` Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` instance with the given property values. |

## Public constructors

### ConnectorConfig

```
ConnectorConfig(connector: String, location: String, serviceId: String)
```

## Public functions

### equals

```
open operator fun equals(other: Any?): Boolean
```

Compares this object with another object for equality.

| Parameters |
|---|---|
| `other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The object to compare to this for equality. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if, and only if, the other object is an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` whose public properties compare equal using the `==` operator to the corresponding properties of this object. |

### hashCode

```
open fun hashCode(): Int
```

Calculates and returns the hash code for this object.

The hash code is *not* guaranteed to be stable across application restarts.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the hash code for this object, that incorporates the values of this object's public properties. |

### toString

```
open fun toString(): String
```

Returns a string representation of this object, useful for debugging.

The string representation is *not* guaranteed to be stable and may change without notice at any time. Therefore, the only recommended usage of the returned string is debugging and/or logging. Namely, parsing the returned string or storing the returned string in non-volatile storage should generally be avoided in order to be robust in case that the string representation changes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a string representation of this object, which includes the class name and the values of all public properties. |

## Public properties

### connector

```
val connector: String
```

The ID of the Firebase Data Connect "connector".

### location

```
val location: String
```

The location where the connector is located (for example, `"us-central1"`).

### serviceId

```
val serviceId: String
```

The ID of the Firebase Data Connect service.

## Extension functions

### copy

```
fun ConnectorConfig.copy(
    connector: String = this.connector,
    location: String = this.location,
    serviceId: String = this.serviceId
): ConnectorConfig
```

Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` instance with the given property values.