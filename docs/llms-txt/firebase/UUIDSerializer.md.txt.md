# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/UUIDSerializer.md.txt

# UUIDSerializer

# UUIDSerializer


```
object UUIDSerializer : KSerializer
```

<br />

*** ** * ** ***

An implementation of `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html` for serializing and deserializing `https://developer.android.com/reference/kotlin/java/util/UUID.html` objects in the wire format expected by the Firebase Data Connect backend.

## Summary

| ### Public functions |
|---|---|
| `open https://developer.android.com/reference/kotlin/java/util/UUID.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/UUIDSerializer#deserialize(kotlinx.serialization.encoding.Decoder)(decoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-decoder/index.html)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/UUIDSerializer#serialize(kotlinx.serialization.encoding.Encoder,java.util.UUID)(encoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-encoder/index.html, value: https://developer.android.com/reference/kotlin/java/util/UUID.html)` |

| ### Public properties |
|---|---|
| `open https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.descriptors/-serial-descriptor/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/UUIDSerializer#descriptor()` |

## Public functions

### deserialize

```
open fun deserialize(decoder: Decoder): UUID
```

### serialize

```
open fun serialize(encoder: Encoder, value: UUID): Unit
```

## Public properties

### descriptor

```
open val descriptor: SerialDescriptor
```