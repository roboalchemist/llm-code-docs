# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.QueryRefOptionsBuilder.md.txt

# FirebaseDataConnect.QueryRefOptionsBuilder

# FirebaseDataConnect.QueryRefOptionsBuilder


```
interface FirebaseDataConnect.QueryRefOptionsBuilder<Data : Any?, Variables : Any?>
```

<br />

*** ** * ** ***

Options that can be specified when creating a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef` via the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect#query(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,kotlin.Function1)` method.

## Summary

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.CallerSdkType?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.QueryRefOptionsBuilder#callerSdkType()` The calling SDK information to apply to all operations executed by the corresponding `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef` object. |
| `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.QueryRefOptionsBuilder#dataSerializersModule()` A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when decoding the query's response data. |
| `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.QueryRefOptionsBuilder#variablesSerializersModule()` A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when encoding the query's variables. |

## Public properties

### callerSdkType

```
var callerSdkType: FirebaseDataConnect.CallerSdkType?
```

The calling SDK information to apply to all operations executed by the corresponding `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef` object. May be `null` (the default) in which case `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.CallerSdkType#Base` will be used.

### dataSerializersModule

```
var dataSerializersModule: SerializersModule?
```

A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when decoding the query's response data. May be `null` (the default) to *not* use a `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` when decoding the response data.

### variablesSerializersModule

```
var variablesSerializersModule: SerializersModule?
```

A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when encoding the query's variables. May be `null` (the default) to *not* use a `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` when encoding the variables.