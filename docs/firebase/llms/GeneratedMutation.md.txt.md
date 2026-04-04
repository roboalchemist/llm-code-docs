# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation.md.txt

# GeneratedMutation

# GeneratedMutation


```
interface GeneratedMutation<Connector : GeneratedConnector<Connector>, Data : Any?, Variables : Any?> : GeneratedOperation
```

<br />

*** ** * ** ***

The specialization of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedOperation` for mutations.

### Safe for concurrent use

All methods and properties of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation` are thread-safe and may be safely called and/or accessed concurrently from multiple threads and/or coroutines.

### Stable for inheritance

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation` interface *is* stable for inheritance in third-party libraries, as new methods will not be added to this interface and contracts of the existing methods will not be changed, except possibly during major version number changes.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation<Connector, Data, Variables>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ExperimentalFirebaseDataConnect https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#copy(com.google.firebase.dataconnect.generated.GeneratedConnector,kotlin.String,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy)( connector: Connector, operationName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, dataDeserializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-deserialization-strategy/index.html<Data>, variablesSerializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serialization-strategy/index.html<Variables> )` Creates and returns a new object that is a *copy* of this object, but with the properties whose names corresponding to the given arguments changed to the respective argument's value. |
| `open https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationRef<Data, Variables>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#ref(kotlin.Any)(variables: Variables)` Returns a OperationRef that can be used to execute this operation with the given variables. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation<Connector, NewData, Variables>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ExperimentalFirebaseDataConnect <NewData : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#withDataDeserializer(kotlinx.serialization.DeserializationStrategy)( dataDeserializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-deserialization-strategy/index.html<NewData> )` Creates and returns a new object that is a *copy* of this object, just like `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#copy(com.google.firebase.dataconnect.generated.GeneratedConnector,kotlin.String,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy)`, except that the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#withDataDeserializer(kotlinx.serialization.DeserializationStrategy)` can be a different type than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation<Connector, Data, NewVariables>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ExperimentalFirebaseDataConnect <NewVariables : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#withVariablesSerializer(kotlinx.serialization.SerializationStrategy)( variablesSerializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serialization-strategy/index.html<NewVariables> )` Creates and returns a new object that is a *copy* of this object, just like `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#copy(com.google.firebase.dataconnect.generated.GeneratedConnector,kotlin.String,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy)`, except that the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#withVariablesSerializer(kotlinx.serialization.SerializationStrategy)` can be a different type than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation`. |

| ### Inherited functions |
|---|
| From [com.google.firebase.dataconnect.generated.GeneratedOperation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedOperation) |---|---| | `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedOperation#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedOperation#hashCode()()` Calculates and returns the hash code for this object. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedOperation#toString()()` Returns a string representation of this object, useful for debugging. | |

| ### Inherited properties |
|---|
| From [com.google.firebase.dataconnect.generated.GeneratedOperation](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedOperation) |---|---| | `Connector` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedOperation#connector()` The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedConnector` with which this object is associated. | | `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-deserialization-strategy/index.html<Data>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedOperation#dataDeserializer()` The deserializer to use to deserialize the response data for this operation. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedOperation#operationName()` The name of the operation, as defined in GraphQL. | | `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serialization-strategy/index.html<Variables>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedOperation#variablesSerializer()` The serializer to use to serialize the variables for this operation. | |

## Public functions

### copy

```
@ExperimentalFirebaseDataConnect
fun copy(
    connector: Connector,
    operationName: String,
    dataDeserializer: DeserializationStrategy<Data>,
    variablesSerializer: SerializationStrategy<Variables>
): GeneratedMutation<Connector, Data, Variables>
```

Creates and returns a new object that is a *copy* of this object, but with the properties whose names corresponding to the given arguments changed to the respective argument's value.

This function is essentially the same as the `copy()` method that is generated by the Kotlin compiler for `data class` classes.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#withDataDeserializer(kotlinx.serialization.DeserializationStrategy)` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#withVariablesSerializer(kotlinx.serialization.SerializationStrategy)` |   |

### ref

```
open fun ref(variables: Variables): MutationRef<Data, Variables>
```

Returns a OperationRef that can be used to execute this operation with the given variables.

### withDataDeserializer

```
@ExperimentalFirebaseDataConnect
fun <NewData : Any?> withDataDeserializer(
    dataDeserializer: DeserializationStrategy<NewData>
): GeneratedMutation<Connector, NewData, Variables>
```

Creates and returns a new object that is a *copy* of this object, just like `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#copy(com.google.firebase.dataconnect.generated.GeneratedConnector,kotlin.String,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy)`, except that the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#withDataDeserializer(kotlinx.serialization.DeserializationStrategy)` can be a different type than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#copy(com.google.firebase.dataconnect.generated.GeneratedConnector,kotlin.String,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy)` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#withVariablesSerializer(kotlinx.serialization.SerializationStrategy)` |   |

### withVariablesSerializer

```
@ExperimentalFirebaseDataConnect
fun <NewVariables : Any?> withVariablesSerializer(
    variablesSerializer: SerializationStrategy<NewVariables>
): GeneratedMutation<Connector, Data, NewVariables>
```

Creates and returns a new object that is a *copy* of this object, just like `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#copy(com.google.firebase.dataconnect.generated.GeneratedConnector,kotlin.String,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy)`, except that the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#withVariablesSerializer(kotlinx.serialization.SerializationStrategy)` can be a different type than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#copy(com.google.firebase.dataconnect.generated.GeneratedConnector,kotlin.String,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy)` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/generated/GeneratedMutation#withDataDeserializer(kotlinx.serialization.DeserializationStrategy)` |   |