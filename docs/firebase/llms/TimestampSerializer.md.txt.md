# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/TimestampSerializer.md.txt

# TimestampSerializer

# TimestampSerializer


```
object TimestampSerializer : KSerializer
```

<br />

*** ** * ** ***

An implementation of `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html` for serializing and deserializing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp` objects in the wire format expected by the Firebase Data Connect backend.

## Summary

| ### Public functions |
|---|---|
| `open https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/TimestampSerializer#deserialize(kotlinx.serialization.encoding.Decoder)(decoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-decoder/index.html)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/TimestampSerializer#serialize(kotlinx.serialization.encoding.Encoder,com.google.firebase.Timestamp)(encoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-encoder/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Timestamp)` |

| ### Public properties |
|---|---|
| `open https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.descriptors/-serial-descriptor/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/TimestampSerializer#descriptor()` |

## Public functions

### deserialize

```
open fun deserialize(decoder: Decoder): Timestamp
```

### serialize

```
open fun serialize(encoder: Encoder, value: Timestamp): Unit
```

## Public properties

### descriptor

```
open val descriptor: SerialDescriptor
```