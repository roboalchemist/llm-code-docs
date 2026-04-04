# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary.md.txt

# com.google.firebase.dataconnect

# com.google.firebase.dataconnect

## Interfaces

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse` | The data and errors provided by the backend in the response message. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationFailureResponse.ErrorInfo` | Information about the error, as provided in the response payload from the backend. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectPathSegment` | The "segment" of a path to a field in the response data. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue` | Stores the value of an `enum` or a string if the string does not correspond to one of the enum's values. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` | Firebase Data Connect is Firebase's first relational database solution for app developers to build mobile and web applications using a fully managed PostgreSQL database powered by Cloud SQL. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.MutationRefOptionsBuilder` | Options that can be specified when creating a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationRef` via the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect#mutation(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,kotlin.Function1)` method. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.QueryRefOptionsBuilder` | Options that can be specified when creating a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef` via the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect#query(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,kotlin.Function1)` method. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationRef` | A specialization of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef` for *mutation* operations. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationResult` | A specialization of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationResult` for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationRef`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef` | Information about a Firebase Data Connect "operation" (a query or a mutation). |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationResult` | The result of a successful execution of an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` | An optional variable to a query or a mutation. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef` | A specialization of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef` for *query* operations. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryResult` | A specialization of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationResult` for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription` | A facility to subscribe to a query to be notified of updates to the query's data when the query is executed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscriptionResult` | The result of a query's execution, as notified to a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription`. |

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` | Represents a variable or field of the Data Connect custom scalar type `Any`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` | Information about a Firebase Data Connect "connector" that is used by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` to connect to the correct Google Cloud resources. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectPathSegment.Field` | A named field in a path to a field in the response data. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectPathSegment.ListIndex` | An index of a list in a path to a field in the response data. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings` | Settings that control the behavior of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` instances. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Known` | Represents a known enum value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/EnumValue.Unknown` | Represents an unknown enum value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` | A date without a time-zone in the ISO-8601 calendar system, such as `2007-12-03`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Serializer` | The `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html` implementation for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value` | An implementation of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` representing a "defined" value. |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectException` | The exception thrown when an error occurs in Firebase Data Connect. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectOperationException` | The exception thrown when an error occurs in the execution of a Firebase Data Connect operation (that is, a query or mutation). |

## Objects

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined` | An implementation of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` representing an "undefined" value. |

## Annotations

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ExperimentalFirebaseDataConnect` | Marks declarations in the Firebase Data Connect SDK that are **experimental**. |

## Enums

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.CallerSdkType` | A tag used for analytics purposes to track the source of usages of the Firebase Data Connect product. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel` | The log levels supported by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect`. |

## Extension functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.ConnectorConfig).copy(kotlin.String,kotlin.String,kotlin.String)( connector: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, location: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, serviceId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html )` Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` instance with the given property values. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.DataConnectSettings).copy(kotlin.String,kotlin.Boolean)(host: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, sslEnabled: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings` instance with the given property values. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).copy(kotlin.Int,kotlin.Int,kotlin.Int)(year: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, month: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, day: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)` Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` instance with the given property values. |
| `inline T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.AnyValue).decode()()` Decodes the encapsulated value using the *default* serializer for the return type, as computed by `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/index.html`. |
| `T` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.AnyValue).decode(kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.modules.SerializersModule)( deserializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-deserialization-strategy/index.html<T>, serializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html? )` Decodes the encapsulated value using the given deserializer. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue.Companion.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.AnyValue.Companion).encode(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)( value: T, serializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serialization-strategy/index.html<T>, serializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html? )` Encodes the given value using the given serializer to an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` object, and returns it. |
| `inline https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue.Companion.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.AnyValue.Companion).encode(kotlin.Any)(value: T)` Encodes the given value using the given *default* serializer for the given object, as computed by `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/index.html`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue.Companion.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.AnyValue.Companion).fromAny(kotlin.Any)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Creates and returns an `AnyValue` object created using the `AnyValue` constructor that corresponds to the runtime type of the given value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue.Companion.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.AnyValue.Companion).fromAny(kotlin.Any)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Creates and returns an `AnyValue` object created using the `AnyValue` constructor that corresponds to the runtime type of the given value, or returns `null` if the given value is `null`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.Companion.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.FirebaseDataConnect.Companion).getInstance(com.google.firebase.FirebaseApp,com.google.firebase.dataconnect.ConnectorConfig,com.google.firebase.dataconnect.DataConnectSettings)( app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp, config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig, settings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings )` Returns the instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` associated with the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig`, creating the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` instance if necessary. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.Companion.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.FirebaseDataConnect.Companion).getInstance(com.google.firebase.dataconnect.ConnectorConfig,com.google.firebase.dataconnect.DataConnectSettings)( config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig, settings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings )` Returns the instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` associated with the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig`, creating the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` instance if necessary. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` | `https://developer.android.com/reference/kotlin/java/time/LocalDate.html.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(java.time.LocalDate).toDataConnectLocalDate()()` Creates and returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` object that represents the same date as this `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` object. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` | `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(kotlinx.datetime.LocalDate).toDataConnectLocalDate()()` Creates and returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` object that represents the same date as the given `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate` object. |
| `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toJavaLocalDate()()` Creates and returns a `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` object that represents the same date as this object. |
| `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toKotlinxLocalDate()()` Creates and returns a `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate` object that represents the same date as this object. |

## Extension properties summary

|---|---|
| `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-mutable-state-flow/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.Companion.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.FirebaseDataConnect.Companion).logLevel()` The log level used by all `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` instances. |

## Extension functions

### copy

```
fun ConnectorConfig.copy(
    connector: String = this.connector,
    location: String = this.location,
    serviceId: String = this.serviceId
): ConnectorConfig
```

Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` instance with the given property values.

### copy

```
fun DataConnectSettings.copy(
    host: String = this.host,
    sslEnabled: Boolean = this.sslEnabled
): DataConnectSettings
```

Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings` instance with the given property values.

### copy

```
fun LocalDate.copy(year: Int = this.year, month: Int = this.month, day: Int = this.day): LocalDate
```

Creates and returns a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` instance with the given property values.

### decode

```
inline fun <T : Any?> AnyValue.decode(): T
```

Decodes the encapsulated value using the *default* serializer for the return type, as computed by `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/index.html`.

| Returns |
|---|---|
| `T` | the object of type `T` created by decoding the encapsulated value using the *default* serializer for the return type, as computed by `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/index.html`. |

### decode

```
fun <T : Any?> AnyValue.decode(
    deserializer: DeserializationStrategy<T>,
    serializersModule: SerializersModule? = null
): T
```

Decodes the encapsulated value using the given deserializer.

| Parameters |
|---|---|
| `deserializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-deserialization-strategy/index.html<T>` | The deserializer for the decoder to use. |
| `serializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html? = null` | a `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use during deserialization; may be `null` (the default) to *not* use a `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use during deserialization. |

| Returns |
|---|---|
| `T` | the object of type `T` created by decoding the encapsulated value using the given deserializer. |

### encode

```
fun <T : Any?> AnyValue.Companion.encode(
    value: T,
    serializer: SerializationStrategy<T>,
    serializersModule: SerializersModule? = null
): AnyValue
```

Encodes the given value using the given serializer to an `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` object, and returns it.

| Parameters |
|---|---|
| `value: T` | the value to serialize. |
| `serializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serialization-strategy/index.html<T>` | the serializer for the encoder to use. |
| `serializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html? = null` | a `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use during serialization; may be `null` (the default) to *not* use a `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use during serialization. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` | a new `AnyValue` object whose encapsulated value is the encoding of the given value when decoded with the given serializer. |

### encode

```
inline fun <T : Any?> AnyValue.Companion.encode(value: T): AnyValue
```

Encodes the given value using the given *default* serializer for the given object, as computed by `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/index.html`.

| Parameters |
|---|---|
| `value: T` | the value to serialize. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/AnyValue` | a new `AnyValue` object whose encapsulated value is the encoding of the given value when decoded with the *default* serializer for the given object, as computed by `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/index.html`. |

### fromAny

```
fun AnyValue.Companion.fromAny(value: Any): AnyValue
```

Creates and returns an `AnyValue` object created using the `AnyValue` constructor that corresponds to the runtime type of the given value.

| Throws |
|---|---|
| `kotlin.IllegalArgumentException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html` | if the given value is not supported by `AnyValue`; see the `AnyValue` constructor for details. |

### fromAny

```
fun AnyValue.Companion.fromAny(value: Any?): AnyValue?
```

Creates and returns an `AnyValue` object created using the `AnyValue` constructor that corresponds to the runtime type of the given value, or returns `null` if the given value is `null`.

| Throws |
|---|---|
| `kotlin.IllegalArgumentException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html` | if the given value is not supported by `AnyValue`; see the `AnyValue` constructor for details. |

### getInstance

```
fun FirebaseDataConnect.Companion.getInstance(
    app: FirebaseApp,
    config: ConnectorConfig,
    settings: DataConnectSettings = DataConnectSettings()
): FirebaseDataConnect
```

Returns the instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` associated with the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig`, creating the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` instance if necessary.

The instances of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` are keyed from the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`, using the identity comparison operator `===`, and the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig`, using the equivalence operator `==`. That is, the first invocation of this method with a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` will create and return a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` instance that is associated with those objects. A subsequent invocation with the same `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` object and an equal `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` will return the same `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` instance that was returned from the previous invocation.

If a new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` instance is created, it will use the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings`. If an existing instance will be returned, then the given (or default) `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings` must be equal to the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect#settings()` of the instance about to be returned; otherwise, an exception is thrown.

| Parameters |
|---|---|
| `app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` instance with which the returned object is associated. |
| `config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` with which the returned object is associated. |
| `settings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings = DataConnectSettings()` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings` for the returned object to use. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` instance associated with the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig`, using the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings`. |

### getInstance

```
fun FirebaseDataConnect.Companion.getInstance(
    config: ConnectorConfig,
    settings: DataConnectSettings = DataConnectSettings()
): FirebaseDataConnect
```

Returns the instance of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` associated with the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig`, creating the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` instance if necessary.

This method is a shorthand for calling `FirebaseDataConnect.getInstance(Firebase.app, config)` or `FirebaseDataConnect.getInstance(Firebase.app, config, settings)`. See the documentation of that method for full details.

| Parameters |
|---|---|
| `config: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig` with which the returned object is associated. |
| `settings: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings = DataConnectSettings()` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings` for the returned object to use. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` | The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` instance associated with the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp` and the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ConnectorConfig`, using the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/DataConnectSettings`. |

### toDataConnectLocalDate

```
fun LocalDate.toDataConnectLocalDate(): LocalDate
```

Creates and returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` object that represents the same date as this `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` object. This is the inverse operation of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toJavaLocalDate()`.

Be sure to *only* call this method if `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` is available. See the documentation for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toJavaLocalDate()` for details.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toJavaLocalDate()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toKotlinxLocalDate()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(kotlinx.datetime.LocalDate).toDataConnectLocalDate()` |   |

### toDataConnectLocalDate

```
fun LocalDate.toDataConnectLocalDate(): LocalDate
```

Creates and returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LocalDate` object that represents the same date as the given `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate` object. This is the inverse operation of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toKotlinxLocalDate()`.

Be sure to *only* call this method if your application has a dependency on `org.jetbrains.kotlinx:kotlinx-datetime`. See the documentation for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toKotlinxLocalDate()` for details.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toKotlinxLocalDate()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toJavaLocalDate()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(java.time.LocalDate).toDataConnectLocalDate()` |   |

### toJavaLocalDate

```
fun LocalDate.toJavaLocalDate(): LocalDate
```

Creates and returns a `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` object that represents the same date as this object.

Be sure to *only* call this method if `https://developer.android.com/reference/kotlin/java/time/LocalDate.html` is available; otherwise the behavior is undefined. If your application's `minSdkVersion` is greater than or equal to `26`, or if you have configured ["desugaring"](https://developer.android.com/studio/write/java8-support-table) then it is guaranteed to be available. Otherwise, check `https://developer.android.com/reference/kotlin/android/os/Build.VERSION.html#SDK_INT--` at runtime and verify that its value is at least `https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES.html#O--` before calling this method.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(java.time.LocalDate).toDataConnectLocalDate()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(kotlinx.datetime.LocalDate).toDataConnectLocalDate()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toKotlinxLocalDate()` |   |

### toKotlinxLocalDate

```
fun LocalDate.toKotlinxLocalDate(): LocalDate
```

Creates and returns a `https://firebase.google.com/docs/reference/kotlin/kotlinx/datetime/LocalDate` object that represents the same date as this object.

Be sure to *only* call this method if your application has a dependency on `org.jetbrains.kotlinx:kotlinx-datetime`; otherwise, the behavior of this method is undefined. If your `minSdkVersion` is less than `26` then you *may* also need to configure ["desugaring"](https://developer.android.com/studio/write/java8-support-table).

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(kotlinx.datetime.LocalDate).toDataConnectLocalDate()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(java.time.LocalDate).toDataConnectLocalDate()` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/package-summary#(com.google.firebase.dataconnect.LocalDate).toJavaLocalDate()` |   |

## Extension properties

### logLevel

```
val FirebaseDataConnect.Companion.logLevel: MutableStateFlow<LogLevel>
```

The log level used by all `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` instances.

As a `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-mutable-state-flow/index.html`, the log level can be changed by assigning `https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-mutable-state-flow/value.html`. Also, the flow can be "collected" as a means of observing the log level, which may be useful in the case that a user interface shows a UI element, such as a checkbox, to represent whether debug logging is enabled.

The default log level is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel#WARN`. Setting this to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel#DEBUG` will enable debug logging, which is especially useful when reporting issues to Google or investigating problems yourself. Setting it to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/LogLevel#NONE` will disable all logging.