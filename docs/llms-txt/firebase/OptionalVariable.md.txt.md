# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.md.txt

# OptionalVariable

# OptionalVariable


```
@Serializable(with = OptionalVariable.Serializer)
interface OptionalVariable<T : Any?>
```

<br />

Known direct subclasses [OptionalVariable.Undefined](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined), [OptionalVariable.Value](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined` | An implementation of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` representing an "undefined" value. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value` | An implementation of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` representing a "defined" value. |

*** ** * ** ***

An optional variable to a query or a mutation.

The typical use case of this class is as a property of a class used as the variables of a query or mutation (`https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OperationRef#variables()`). This allows omitting a variable altogether from the request, in the case of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined`, allowing the variable to take on its default value as defined in the GraphQL schema or operation, or an explicit value in the case of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value`, which may be `null` if the type parameter is nullable.

Here is an example of such a variables class:

```kotlin
@Serializable
data class UpdatePersonVariables(
  val key: PersonKey,
  val name: OptionalVariable<String>,
  val age: OptionalVariable<Int?>,
)
```

with this "variables" class, to clear a person's age but not modify their name, the instance could be created as follows

```kotlin
val variables = UpdatePersonVariables(
  key=key,
  name=OptionalVariable.Undefined,
  age=OptionalVariable.Value(42),
)
```

## Summary

| ### Nested types |
|---|
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Serializer<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> : https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html` The `https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-k-serializer/index.html` implementation for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable`. |
| `object https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` An implementation of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` representing an "undefined" value. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> : https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` An implementation of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable` representing a "defined" value. |

| ### Public functions |
|---|---|
| `T?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable#valueOrNull()()` Returns the value encapsulated by this object if the runtime type is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value`, or `null` if this object is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined`. |
| `T` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable#valueOrThrow()()` Returns the value encapsulated by this object if the runtime type is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value`, or throws an exception if this object is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined`. |

## Public functions

### valueOrNull

```
fun valueOrNull(): T?
```

Returns the value encapsulated by this object if the runtime type is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value`, or `null` if this object is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined`.

### valueOrThrow

```
fun valueOrThrow(): T
```

Returns the value encapsulated by this object if the runtime type is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Value`, or throws an exception if this object is `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/dataconnect/OptionalVariable.Undefined`.