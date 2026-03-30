# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings.md.txt

# DataConnectSettings

# DataConnectSettings


```
class DataConnectSettings
```

<br />

*** ** * ** ***

Settings that control the behavior of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` instances.

### Safe for concurrent use

All methods and properties of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings` are thread-safe and may be safely called and/or accessed concurrently from multiple threads and/or coroutines.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings#DataConnectSettings(kotlin.String,kotlin.Boolean)(host: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, sslEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` |

| ### Public functions |
|---|---|
| `open operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings#hashCode()()` Calculates and returns the hash code for this object. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings#toString()()` Returns a string representation of this object, useful for debugging. |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings#host()` The host of the Firebase Data Connect service to which to connect (for example, `"myproxy.foo.com"`, `"myproxy.foo.com:9987"`). |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings#sslEnabled()` Whether to use SSL for the connection; if `true`, then the connection will be encrypted using SSL and, if false, the connection will *not* be encrypted and all network transmission will happen in plaintext. |

| ### Extension functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings#(com.google.firebase.dataconnect.DataConnectSettings).copy(kotlin.String,kotlin.Boolean)(host: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, sslEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings` instance with the given property values. |

## Public constructors

### DataConnectSettings

```
DataConnectSettings(
    host: String = "firebasedataconnect.googleapis.com",
    sslEnabled: Boolean = true
)
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
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if, and only if, the other object is an instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings` whose public properties compare equal using the `==` operator to the corresponding properties of this object. |

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

### host

```
val host: String
```

The host of the Firebase Data Connect service to which to connect (for example, `"myproxy.foo.com"`, `"myproxy.foo.com:9987"`).

### sslEnabled

```
val sslEnabled: Boolean
```

Whether to use SSL for the connection; if `true`, then the connection will be encrypted using SSL and, if false, the connection will *not* be encrypted and all network transmission will happen in plaintext.

## Extension functions

### copy

```
fun DataConnectSettings.copy(
    host: String = this.host,
    sslEnabled: Boolean = this.sslEnabled
): DataConnectSettings
```

Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings` instance with the given property values.