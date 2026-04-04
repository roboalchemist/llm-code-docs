# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.MutationRefOptionsBuilder.md.txt

# FirebaseDataConnect.MutationRefOptionsBuilder

# FirebaseDataConnect.MutationRefOptionsBuilder


```
interface FirebaseDataConnect.MutationRefOptionsBuilder<Data : Any?, Variables : Any?>
```

<br />

*** ** * ** ***

Options that can be specified when creating a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationRef` via the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect#mutation(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,kotlin.Function1)` method.

## Summary

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.CallerSdkType?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.MutationRefOptionsBuilder#callerSdkType()` The calling SDK information to apply to all operations executed by the corresponding `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationRef` object. |
| `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.MutationRefOptionsBuilder#dataSerializersModule()` A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when decoding the mutation's response data. |
| `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.MutationRefOptionsBuilder#variablesSerializersModule()` A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when encoding the mutation's variables. |

## Public properties

### callerSdkType

```
var callerSdkType: FirebaseDataConnect.CallerSdkType?
```

The calling SDK information to apply to all operations executed by the corresponding `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationRef` object. May be `null` (the default) in which case `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.CallerSdkType#Base` will be used.

### dataSerializersModule

```
var dataSerializersModule: SerializersModule?
```

A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when decoding the mutation's response data. May be `null` (the default) to *not* use a `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` when decoding the response data.

### variablesSerializersModule

```
var variablesSerializersModule: SerializersModule?
```

A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when encoding the mutation's variables. May be `null` (the default) to use some unspecified `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` when encoding the variables.