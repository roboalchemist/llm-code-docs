# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef.md.txt

# QueryRef

# QueryRef


```
interface QueryRef<Data : Any?, Variables : Any?> : OperationRef
```

<br />

*** ** * ** ***

A specialization of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef` for *query* operations.

### Safe for concurrent use

All methods and properties of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef` are thread-safe and may be safely called and/or accessed concurrently from multiple threads and/or coroutines.

### Not stable for inheritance

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef` interface is *not* stable for inheritance in third-party libraries, as new methods might be added to this interface or contracts of the existing methods can be changed.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef<Data, Variables>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ExperimentalFirebaseDataConnect https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)( operationName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, variables: Variables, dataDeserializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-deserialization-strategy/index.html<Data>, variablesSerializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serialization-strategy/index.html<Variables>, callerSdkType: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.CallerSdkType, dataSerializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html?, variablesSerializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html? )` Creates and returns a new object that is a *copy* of this object, but with the properties whose names corresponding to the given arguments changed to the respective argument's value. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryResult<Data, Variables>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#execute()()` Executes this operation and returns the result. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription<Data, Variables>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#subscribe()()` Subscribes to a query to be notified of updates to the query's data when the query is executed. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef<NewData, Variables>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ExperimentalFirebaseDataConnect <NewData : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#withDataDeserializer(kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.modules.SerializersModule)( dataDeserializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-deserialization-strategy/index.html<NewData>, dataSerializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html? )` Creates and returns a new object that is a *copy* of this object, just like `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)`, except that the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#withDataDeserializer(kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.modules.SerializersModule)` can be a different type than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef<Data, NewVariables>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ExperimentalFirebaseDataConnect <NewVariables : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)( variables: NewVariables, variablesSerializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serialization-strategy/index.html<NewVariables>, variablesSerializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html? )` Creates and returns a new object that is a *copy* of this object, just like `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)`, except that the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)` can be a different type than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef`. |

| ### Inherited functions |
|---|
| From [com.google.firebase.dataconnect.OperationRef](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef) |---|---| | `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#hashCode()()` Calculates and returns the hash code for this object. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#toString()()` Returns a string representation of this object, useful for debugging. | |

| ### Inherited properties |
|---|
| From [com.google.firebase.dataconnect.OperationRef](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.CallerSdkType` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#callerSdkType()` The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.CallerSdkType` that will be associated with all operations performed by this object for analytics purposes. | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#dataConnect()` The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` with which this object is associated. | | `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-deserialization-strategy/index.html<Data>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#dataDeserializer()` The deserializer to use to deserialize the response data for this operation. | | `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#dataSerializersModule()` A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when decoding the response data using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#dataDeserializer()`. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#operationName()` The name of the operation, as defined in GraphQL. | | `Variables` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#variables()` The variables for the operation. | | `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serialization-strategy/index.html<Variables>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#variablesSerializer()` The serializer to use to serialize the variables for this operation. | | `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#variablesSerializersModule()` A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when encoding the variables using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#variablesSerializer()`. | |

## Public functions

### copy

```
@ExperimentalFirebaseDataConnect
fun copy(
    operationName: String,
    variables: Variables,
    dataDeserializer: DeserializationStrategy<Data>,
    variablesSerializer: SerializationStrategy<Variables>,
    callerSdkType: FirebaseDataConnect.CallerSdkType,
    dataSerializersModule: SerializersModule?,
    variablesSerializersModule: SerializersModule?
): QueryRef<Data, Variables>
```

Creates and returns a new object that is a *copy* of this object, but with the properties whose names corresponding to the given arguments changed to the respective argument's value.

This function is essentially the same as the `copy()` method that is generated by the Kotlin compiler for `data class` classes.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#withDataDeserializer(kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.modules.SerializersModule)` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)` |   |

### execute

```
suspend fun execute(): QueryResult<Data, Variables>
```

Executes this operation and returns the result.

An exception is thrown if the operation fails for any reason, including

- The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` object has been closed.

- The Firebase Data Connect server is unreachable.

- Authentication with the Firebase Data Connect server fails.

- The variables are rejected by the Firebase Data Connect server.

- The data response sent by the Firebase Data Connect server cannot be deserialized.

### subscribe

```
fun subscribe(): QuerySubscription<Data, Variables>
```

Subscribes to a query to be notified of updates to the query's data when the query is executed.

At this time the notifications are *not* realtime, and are *not* pushed from the server. Instead, the notifications are sent whenever the query is explicitly executed by calling `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#execute()`.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QuerySubscription<Data, Variables>` | an object that can be used to subscribe to query results. |

### withDataDeserializer

```
@ExperimentalFirebaseDataConnect
fun <NewData : Any?> withDataDeserializer(
    dataDeserializer: DeserializationStrategy<NewData>,
    dataSerializersModule: SerializersModule?
): QueryRef<NewData, Variables>
```

Creates and returns a new object that is a *copy* of this object, just like `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)`, except that the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#withDataDeserializer(kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.modules.SerializersModule)` can be a different type than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)` |   |

### withVariablesSerializer

```
@ExperimentalFirebaseDataConnect
fun <NewVariables : Any?> withVariablesSerializer(
    variables: NewVariables,
    variablesSerializer: SerializationStrategy<NewVariables>,
    variablesSerializersModule: SerializersModule?
): QueryRef<Data, NewVariables>
```

Creates and returns a new object that is a *copy* of this object, just like `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)`, except that the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)` can be a different type than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef#withDataDeserializer(kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.modules.SerializersModule)` |   |