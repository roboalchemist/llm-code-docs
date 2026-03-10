# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Serializer.md.txt

# OptionalVariable.Serializer

# OptionalVariable.Serializer


```
class OptionalVariable.Serializer<T : Any?> : KSerializer
```

<br />

*** ** * ** ***

The `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html` implementation for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable`.

Note that this serializer *only* supports `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Serializer#serialize(kotlinx.serialization.encoding.Encoder,com.google.firebase.dataconnect.OptionalVariable)`; `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Serializer#deserialize(kotlinx.serialization.encoding.Decoder)` unconditionally throws an exception.

## Summary

| ### Public constructors |
|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Serializer#Serializer(kotlinx.serialization.KSerializer)(elementSerializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html<T>)` |

| ### Public functions |
|---|---|
| `open https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable<T>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Serializer#deserialize(kotlinx.serialization.encoding.Decoder)(decoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-decoder/index.html)` Unconditionally throws `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unsupported-operation-exception/index.html`. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Serializer#serialize(kotlinx.serialization.encoding.Encoder,com.google.firebase.dataconnect.OptionalVariable)(encoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-encoder/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable<T>)` Serializes the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` to the given encoder. |

| ### Public properties |
|---|---|
| `open https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.descriptors/-serial-descriptor/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Serializer#descriptor()` |

## Public constructors

### Serializer

```
<T : Any?> Serializer(elementSerializer: KSerializer<T>)
```

| Parameters |
|---|---|
| `elementSerializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html<T>` | The `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html` to use to serialize the encapsulated value. |

## Public functions

### deserialize

```
open fun deserialize(decoder: Decoder): OptionalVariable<T>
```

Unconditionally throws `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unsupported-operation-exception/index.html`.

### serialize

```
open fun serialize(encoder: Encoder, value: OptionalVariable<T>): Unit
```

Serializes the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` to the given encoder.

This method does nothing if the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined`; otherwise, it serializes the encapsulated value in the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value` using the serializer given to this object's constructor.

## Public properties

### descriptor

```
open val descriptor: SerialDescriptor
```