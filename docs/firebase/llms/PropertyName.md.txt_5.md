# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PropertyName.md.txt

# PropertyName

# PropertyName


```
@Retention(value = RetentionPolicy.RUNTIME)
@Target(value = [ElementType.METHOD, ElementType.FIELD])
annotation PropertyName
```

<br />

*** ** * ** ***

Marks a field to be renamed when serialized.

### Kotlin Note

When applying this annotation to a property of a Kotlin class, both the `@get` and `@set` use-site targets should be used.

Here is an example of a class that can both be written into and read from Firestore whose `foo` property will be stored into and read from a field named `my_foo` in the Firestore document:

```kotlin
data class Pojo(@get:PropertyName("my_foo") @set:PropertyName("my_foo") var foo: String? = null) {
  constructor() : this(null) // Used by Firestore to create new instances
}
```

If the class only needs to be *written* into Firestore (and not read from Firestore) then the class can be simplified as follows:

```kotlin
data class Pojo(@get:PropertyName("my_foo") val foo: String? = null)
```
That is, `var` can be tightened to `val`, the secondary no-argument constructor can be omitted, and the `@set` use-site target can be omitted.

## Summary

| ### Public functions |
|---|---|
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PropertyName#value()()` |

## Public functions

### value

```
abstract fun value(): String!
```