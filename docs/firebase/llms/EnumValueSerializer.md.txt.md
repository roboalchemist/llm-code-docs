# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/EnumValueSerializer.md.txt

# EnumValueSerializer

# EnumValueSerializer


```
open class EnumValueSerializer<T : Enum<T>> : KSerializer
```

<br />

*** ** * ** ***

A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html` implementation for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue`.

## Summary

| ### Public constructors |
|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/index.html<T>> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/EnumValueSerializer#EnumValueSerializer(kotlin.collections.Iterable)(values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html<T>)` |

| ### Public functions |
|---|---|
| `open https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue<T>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/EnumValueSerializer#deserialize(kotlinx.serialization.encoding.Decoder)(decoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-decoder/index.html)` Deserializes an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue` from the given decoder. |
| `open https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/EnumValueSerializer#serialize(kotlinx.serialization.encoding.Encoder,com.google.firebase.dataconnect.EnumValue)(encoder: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.encoding/-encoder/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue<T>)` Serializes the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue` to the given encoder. |

| ### Public properties |
|---|---|
| `open https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.descriptors/-serial-descriptor/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/serializers/EnumValueSerializer#descriptor()` |

## Public constructors

### EnumValueSerializer

```
<T : Enum<T>> EnumValueSerializer(values: Iterable<T>)
```

| Parameters |
|---|---|
| `values: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html<T>` | The values of the enum to deserialize; for example, for an enum named `Foo` this value should be `Foo.entries` or `Foo.values()`. |

## Public functions

### deserialize

```
open fun deserialize(decoder: Decoder): EnumValue<T>
```

Deserializes an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue` from the given decoder.

If the decoded string is equal to the `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-enum/name.html` of one of the values given to the constructor then `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known` is returned with that value; otherwise, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown` is returned.

### serialize

```
open fun serialize(encoder: Encoder, value: EnumValue<T>): Unit
```

Serializes the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue` to the given encoder.

## Public properties

### descriptor

```
open val descriptor: SerialDescriptor
```