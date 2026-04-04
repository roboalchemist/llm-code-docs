# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Exclude.md.txt

# Exclude

# Exclude


```
@Retention(value = RetentionPolicy.RUNTIME)
@Target(value = [ElementType.METHOD, ElementType.FIELD])
annotation Exclude
```

<br />

*** ** * ** ***

Marks a field as excluded from the database instance.

### Kotlin Note

When applying this annotation to a property of a Kotlin class, the `@get` use-site target should always be used. There is no need to use the `@set` use-site target as this annotation is *only* considered when *writing* instances into Firestore, and is ignored when *reading* instances from Firestore.

Here is an example of a class that can both be written into and read from Firestore whose `bar` property will never be written into Firestore:

```kotlin
data class Pojo(var foo: String? = null, @get:Exclude var bar: String? = null) {
  constructor() : this(null, null) // Used by Firestore to create new instances
}
```

If the class only needs to be *written* into Firestore (and not read from Firestore) then the class can be simplified as follows:

```kotlin
data class Pojo(val foo: String? = null, @get:Exclude val bar: String? = null)
```
That is, `var` can be tightened to `val` and the secondary no-argument constructor can be omitted.