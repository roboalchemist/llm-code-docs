# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/KotlinxDatetimeLocalDateSerializer.md.txt

# KotlinxDatetimeLocalDateSerializer

# KotlinxDatetimeLocalDateSerializer


```
object KotlinxDatetimeLocalDateSerializer : KSerializer
```

<br />

*** ** * ** ***

An implementation of `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html` for serializing and deserializing `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate` objects in the wire format expected by the Firebase Data Connect backend.

Be sure to *only* use this class if your application has a dependency on `org.jetbrains.kotlinx:kotlinx-datetime`. See the documentation for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toKotlinxLocalDate()` for details.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/LocalDateSerializer` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/JavaTimeLocalDateSerializer` |   |

## Summary

| ### Public functions |
|---|---|
| `open https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/KotlinxDatetimeLocalDateSerializer#deserialize(kotlinx.serialization.encoding.Decoder)(decoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-decoder/index.html)` |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/KotlinxDatetimeLocalDateSerializer#serialize(kotlinx.serialization.encoding.Encoder,kotlinx.datetime.LocalDate)(encoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-encoder/index.html, value: https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate)` |

| ### Public properties |
|---|---|
| `open https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.descriptors/-serial-descriptor/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/KotlinxDatetimeLocalDateSerializer#descriptor()` |

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