# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/JavaTimeLocalDateSerializer.md.txt

# JavaTimeLocalDateSerializer

# JavaTimeLocalDateSerializer


```
object JavaTimeLocalDateSerializer : KSerializer
```

<br />

*** ** * ** ***

An implementation of `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html` for serializing and deserializing `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` objects in the wire format expected by the Firebase Data Connect backend.

Be sure to *only* call this method if `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` is available. See the documentation for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toJavaLocalDate()` for details.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/LocalDateSerializer` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/KotlinxDatetimeLocalDateSerializer` |   |

## Summary

| ### Public functions |
|---|---|
| `open https://developer.android.com/reference/kotlin/java/time/LocalDate.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/JavaTimeLocalDateSerializer#deserialize(kotlinx.serialization.encoding.Decoder)(decoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-decoder/index.html)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/JavaTimeLocalDateSerializer#serialize(kotlinx.serialization.encoding.Encoder,java.time.LocalDate)(encoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-encoder/index.html, value: https://developer.android.com/reference/kotlin/java/time/LocalDate.html)` |

| ### Public properties |
|---|---|
| `open https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.descriptors/-serial-descriptor/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/JavaTimeLocalDateSerializer#descriptor()` |

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