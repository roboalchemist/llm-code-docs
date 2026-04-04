# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/AnyValueSerializer.md.txt

# AnyValueSerializer

# AnyValueSerializer


```
object AnyValueSerializer : KSerializer
```

<br />

*** ** * ** ***

An implementation of `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html` for serializing and deserializing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` objects.

Note that this is *not* a generic serializer, but is only useful in the Data Connect SDK.

## Summary

| ### Public functions |
|---|---|
| `open https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/AnyValueSerializer#deserialize(kotlinx.serialization.encoding.Decoder)(decoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-decoder/index.html)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/AnyValueSerializer#serialize(kotlinx.serialization.encoding.Encoder,com.google.firebase.dataconnect.AnyValue)(encoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-encoder/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue)` |

| ### Public properties |
|---|---|
| `open https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.descriptors/-serial-descriptor/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/AnyValueSerializer#descriptor()` |

## Public functions

### deserialize

```
open fun deserialize(decoder: Decoder): AnyValue
```

### serialize

```
open fun serialize(encoder: Encoder, value: AnyValue): Unit
```

## Public properties

### descriptor

```
open val descriptor: SerialDescriptor
```