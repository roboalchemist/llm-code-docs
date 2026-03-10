# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder.md.txt

# CustomSignals.Builder

# CustomSignals.Builder


```
class CustomSignals.Builder
```

<br />

*** ** * ** ***

Builder for constructing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals` instances.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder#Builder()()` |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder#build()()` Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals` instance with the added custom signals. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder#put(java.lang.String,java.lang.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?)` Adds a custom signal with a value that can be a string or null to the builder. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder#put(java.lang.String,long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Adds a custom signal with a long value to the builder. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder#put(java.lang.String,double)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Adds a custom signal with a double value to the builder. |

## Public constructors

### Builder

```
Builder()
```

## Public functions

### build

```
fun build(): CustomSignals
```

Creates a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals` instance with the added custom signals.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals` | The constructed `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals` instance. |

### put

```
fun put(key: String, value: String?): CustomSignals.Builder
```

Adds a custom signal with a value that can be a string or null to the builder.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The key for the custom signal. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The string value associated with the key. Can be null. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder` | This Builder instance to allow chaining of method calls. |

### put

```
fun put(key: String, value: Long): CustomSignals.Builder
```

Adds a custom signal with a long value to the builder.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The key for the custom signal. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The long value for the custom signal. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder` | This Builder instance to allow chaining of method calls. |

### put

```
fun put(key: String, value: Double): CustomSignals.Builder
```

Adds a custom signal with a double value to the builder.

| Parameters |
|---|---|
| `key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The key for the custom signal. |
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` | The double value for the custom signal. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder` | This Builder instance to allow chaining of method calls. |