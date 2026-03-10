# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef.md.txt

# OperationRef

# OperationRef


```
interface OperationRef<Data : Any?, Variables : Any?>
```

<br />

Known direct subclasses [MutationRef](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationRef), [QueryRef](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationRef` | A specialization of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef` for *mutation* operations. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef` | A specialization of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef` for *query* operations. |

*** ** * ** ***

Information about a Firebase Data Connect "operation" (a query or a mutation).

`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef` has two inheritors: `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/QueryRef` for queries and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/MutationRef` for mutations. `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef` merely serves to provide a common interface for the parts of queries and mutations that are shared.

### Safe for concurrent use

All methods and properties of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef` are thread-safe and may be safely called and/or accessed concurrently from multiple threads and/or coroutines.

### Not stable for inheritance

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef` interface is *not* stable for inheritance in third-party libraries, as new methods might be added to this interface or contracts of the existing methods can be changed.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef<Data, Variables>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ExperimentalFirebaseDataConnect https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)( operationName: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, variables: Variables, dataDeserializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-deserialization-strategy/index.html<Data>, variablesSerializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serialization-strategy/index.html<Variables>, callerSdkType: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.CallerSdkType, dataSerializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html?, variablesSerializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html? )` Creates and returns a new object that is a *copy* of this object, but with the properties whose names corresponding to the given arguments changed to the respective argument's value. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#equals(kotlin.Any)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Compares this object with another object for equality. |
| `suspend https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationResult<Data, Variables>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#execute()()` Executes this operation and returns the result. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#hashCode()()` Calculates and returns the hash code for this object. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#toString()()` Returns a string representation of this object, useful for debugging. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef<NewData, Variables>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ExperimentalFirebaseDataConnect <NewData : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#withDataDeserializer(kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.modules.SerializersModule)( dataDeserializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-deserialization-strategy/index.html<NewData>, dataSerializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html? )` Creates and returns a new object that is a *copy* of this object, just like `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)`, except that the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#withDataDeserializer(kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.modules.SerializersModule)` can be a different type than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef<Data, NewVariables>` | `@https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/ExperimentalFirebaseDataConnect <NewVariables : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)( variables: NewVariables, variablesSerializer: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serialization-strategy/index.html<NewVariables>, variablesSerializersModule: https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html? )` Creates and returns a new object that is a *copy* of this object, just like `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)`, except that the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)` can be a different type than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef`. |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.CallerSdkType` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#callerSdkType()` The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.CallerSdkType` that will be associated with all operations performed by this object for analytics purposes. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#dataConnect()` The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` with which this object is associated. |
| `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-deserialization-strategy/index.html<Data>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#dataDeserializer()` The deserializer to use to deserialize the response data for this operation. |
| `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#dataSerializersModule()` A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when decoding the response data using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#dataDeserializer()`. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#operationName()` The name of the operation, as defined in GraphQL. |
| `Variables` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#variables()` The variables for the operation. |
| `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serialization-strategy/index.html<Variables>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#variablesSerializer()` The serializer to use to serialize the variables for this operation. |
| `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#variablesSerializersModule()` A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when encoding the variables using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#variablesSerializer()`. |

## Public functions

### copy

```
@ExperimentalFirebaseDataConnect
fun copy(
    operationName: String = this.operationName,
    variables: Variables = this.variables,
    dataDeserializer: DeserializationStrategy<Data> = this.dataDeserializer,
    variablesSerializer: SerializationStrategy<Variables> = this.variablesSerializer,
    callerSdkType: FirebaseDataConnect.CallerSdkType = this.callerSdkType,
    dataSerializersModule: SerializersModule? = this.dataSerializersModule,
    variablesSerializersModule: SerializersModule? = this.variablesSerializersModule
): OperationRef<Data, Variables>
```

Creates and returns a new object that is a *copy* of this object, but with the properties whose names corresponding to the given arguments changed to the respective argument's value.

This function is essentially the same as the `copy()` method that is generated by the Kotlin compiler for `data class` classes.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#withDataDeserializer(kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.modules.SerializersModule)` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)` |   |

### equals

```
operator fun equals(other: Any?): Boolean
```

Compares this object with another object for equality.

| Parameters |
|---|---|
| `other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The object to compare to this for equality. |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | true if, and only if, the other object is an instance of the same implementation of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef` whose public properties compare equal using the `==` operator to the corresponding properties of this object. |

### execute

```
suspend fun execute(): OperationResult<Data, Variables>
```

Executes this operation and returns the result.

An exception is thrown if the operation fails for any reason, including

- The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` object has been closed.

- The Firebase Data Connect server is unreachable.

- Authentication with the Firebase Data Connect server fails.

- The variables are rejected by the Firebase Data Connect server.

- The data response sent by the Firebase Data Connect server cannot be deserialized.

### hashCode

```
fun hashCode(): Int
```

Calculates and returns the hash code for this object.

The hash code is *not* guaranteed to be stable across application restarts.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | the hash code for this object, that incorporates the values of this object's public properties. |

### toString

```
fun toString(): String
```

Returns a string representation of this object, useful for debugging.

The string representation is *not* guaranteed to be stable and may change without notice at any time. Therefore, the only recommended usage of the returned string is debugging and/or logging. Namely, parsing the returned string or storing the returned string in non-volatile storage should generally be avoided in order to be robust in case that the string representation changes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | a string representation of this object, which includes the class name and the values of all public properties. |

### withDataDeserializer

```
@ExperimentalFirebaseDataConnect
fun <NewData : Any?> withDataDeserializer(
    dataDeserializer: DeserializationStrategy<NewData>,
    dataSerializersModule: SerializersModule? = this.dataSerializersModule
): OperationRef<NewData, Variables>
```

Creates and returns a new object that is a *copy* of this object, just like `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)`, except that the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#withDataDeserializer(kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.modules.SerializersModule)` can be a different type than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)` |   |

### withVariablesSerializer

```
@ExperimentalFirebaseDataConnect
fun <NewVariables : Any?> withVariablesSerializer(
    variables: NewVariables,
    variablesSerializer: SerializationStrategy<NewVariables>,
    variablesSerializersModule: SerializersModule? = this.variablesSerializersModule
): OperationRef<Data, NewVariables>
```

Creates and returns a new object that is a *copy* of this object, just like `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)`, except that the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)` and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#withVariablesSerializer(kotlin.Any,kotlinx.serialization.SerializationStrategy,kotlinx.serialization.modules.SerializersModule)` can be a different type than `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef`.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#copy(kotlin.String,kotlin.Any,kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.SerializationStrategy,com.google.firebase.dataconnect.FirebaseDataConnect.CallerSdkType,kotlinx.serialization.modules.SerializersModule,kotlinx.serialization.modules.SerializersModule)` |   |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#withDataDeserializer(kotlinx.serialization.DeserializationStrategy,kotlinx.serialization.modules.SerializersModule)` |   |

## Public properties

### callerSdkType

```
val callerSdkType: FirebaseDataConnect.CallerSdkType
```

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect.CallerSdkType` that will be associated with all operations performed by this object for analytics purposes.

### dataConnect

```
val dataConnect: FirebaseDataConnect
```

The `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/FirebaseDataConnect` with which this object is associated.

### dataDeserializer

```
val dataDeserializer: DeserializationStrategy<Data>
```

The deserializer to use to deserialize the response data for this operation.

Typically, the deserializer will be generated by Kotlin's serialization plugin for a class annotated with `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html`.

For example, a query defined as

```kotlin
query GetPersonById($id: UUID!) { person(id: $id) { name age } }
```

could define its data class as follows:

```kotlin
@Serializable
data class GetPersonByIdData(val person: Person?) {
  @Serializable
  data class Person(val name: String, val age: Int?)
}
```

and the deserializer could be retrieved by calling `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/index.html` as follows:

```kotlin
serializer<GetPersonByIdData>()
```

### dataSerializersModule

```
val dataSerializersModule: SerializersModule?
```

A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when decoding the response data using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#dataDeserializer()`. May be `null`, to not use a `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html`.

### operationName

```
val operationName: String
```

The name of the operation, as defined in GraphQL.

For example, a query defined as

```kotlin
query GetPersonById($id: UUID!) { person(id: $id) { name age } }
```

would have the operation name `"GetPersonById"` and a mutation defined as

```kotlin
mutation InsertPerson($name: String!, $age: Int) {...}
```

would have the operation name `"InsertPerson"`

### variables

```
val variables: Variables
```

The variables for the operation.

The variables will be serialized using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#variablesSerializer()` and must produce a map whose keys are strings whose values are the names of the variables as defined in GraphQL, and whose values are the corresponding values.

For example, a query defined as

```kotlin
query GetPersonById($id: UUID!) { person(id: $id) { name age } }
```

would have a variable named `"id"` whose value is a `https://developer.android.com/reference/kotlin/java/util/UUID.html` instance and a mutation defined as

```kotlin
mutation InsertPerson($name: String!, $age: Int) {...}
```

would have two variables named `"name"` and `"age"` whose values are `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` and `Int?` values, respectively.

### variablesSerializer

```
val variablesSerializer: SerializationStrategy<Variables>
```

The serializer to use to serialize the variables for this operation.

Typically, the serializer will be generated by Kotlin's serialization plugin for a class annotated with `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html`.

For example, a mutation defined as

```kotlin
mutation InsertPerson($name: String!, $age: Int) {...}
```

could define its variables class as follows:

```kotlin
@Serializable
data class InsertPersonVariables(val name: String, val age: Int?)
```

and the serializer could be retrieved by calling `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/index.html` as follows:

```kotlin
serializer<InsertPersonVariables>()
```

### variablesSerializersModule

```
val variablesSerializersModule: SerializersModule?
```

A `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html` to use when encoding the variables using `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#variablesSerializer()`. May be `null`, to not use a `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization.modules/-serializers-module/index.html`.