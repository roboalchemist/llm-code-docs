# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/LocalDateSerializer.md.txt

# LocalDateSerializer

# LocalDateSerializer


```
object LocalDateSerializer : KSerializer
```

<br />

*** ** * ** ***

An implementation of `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html` for serializing and deserializing `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` objects in the wire format expected by the Firebase Data Connect backend.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/JavaTimeLocalDateSerializer` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/KotlinxDatetimeLocalDateSerializer` |   |

## Summary

| ### Public functions |
|---|---|
| `open https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/LocalDateSerializer#deserialize(kotlinx.serialization.encoding.Decoder)(decoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-decoder/index.html)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/LocalDateSerializer#serialize(kotlinx.serialization.encoding.Encoder,com.google.firebase.dataconnect.LocalDate)(encoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-encoder/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate)` |

| ### Public properties |
|---|---|
| `open https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.descriptors/-serial-descriptor/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/LocalDateSerializer#descriptor()` |

## Public functions

### deserialize

```
open fun deserialize(decoder: Decoder): LocalDate
```

### serialize

```
open fun serialize(encoder: Encoder, value: LocalDate): Unit
```

## Public properties

### descriptor

```
open val descriptor: SerialDescriptor
```