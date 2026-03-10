# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ServerTimestamp.md.txt

# ServerTimestamp

# ServerTimestamp


```
@Retention(value = RetentionPolicy.RUNTIME)
@Target(value = [ElementType.METHOD, ElementType.FIELD])
public annotation ServerTimestamp
```

<br />

*** ** * ** ***

Annotation used to mark a timestamp field to be populated with a server timestamp. If a POJO being written contains `null` for a @ServerTimestamp-annotated field, it will be replaced with a server-generated timestamp.

### Kotlin Note

When applying this annotation to a property of a Kotlin class, the `@get` use-site target should always be used. There is no need to use the `@set` use-site target as this annotation is *only* considered when *writing* instances into Firestore, and is ignored when *reading* instances from Firestore.

Here is an example of a class that can both be written into and read from Firestore whose `foo` property will be populated with the server timestamp in Firestore if its value is null:

```
data class Pojo(@get:ServerTimestamp var foo: Timestamp? = null) {
  constructor() : this(null) // Used by Firestore to create new instances
}
```

If the class only needs to be *written* into Firestore (and not read from Firestore) then the class can be simplified as follows:

```
data class Pojo(@get:ServerTimestamp val foo: Timestamp? = null)
```
That is, `var` can be tightened to `val` and the secondary no-argument constructor can be omitted.