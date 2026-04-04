# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentId.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentId.md.txt

# DocumentId

# DocumentId


```
@Retention(valueÂ =Â RetentionPolicy.RUNTIME)
@Target(valueÂ =Â [ElementType.FIELD,Â ElementType.METHOD])
annotation DocumentId
```

<br />

*** ** * ** ***

Annotation used to mark a POJO property to be automatically populated with the document's ID when the POJO is created from a Cloud Firestore document (for example, via [toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#toObject(java.lang.Class<T>))).

Any of the following will throw a runtime exception:

- This annotation is applied to a property of a type other than String or [DocumentReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference).
- This annotation is applied to a property that is not writable (for example, a Java Bean getter without a backing field).
- This annotation is applied to a property with a name that conflicts with a read document field. For example, if a POJO has a field \`firstName\` annotated by `@DocumentId`, and there is a property from the document named \`firstName\` as well, an exception is thrown when you try to read the document into the POJO via [toObject](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentSnapshot#toObject(java.lang.Class<T>)) or [get](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#get()).
- 

When using a POJO to write to a document (via [set](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference#set(java.lang.Object)) or @[set](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/WriteBatch#set(com.google.firebase.firestore.DocumentReference,java.lang.Object))), the property annotated by `@DocumentId` is ignored, which allows writing the POJO back to any document, even if it's not the origin of the POJO.

### Kotlin Note

When applying this annotation to a property of a Kotlin class, the `@set` use-site target should always be used. There is no need to use the `@get` use-site target as this annotation is *only* considered when *reading* instances from Firestore, and is ignored when *writing* instances into Firestore.

Here is an example of a class that can both be written into and read from Firestore whose `foo` property will be populated with the Document ID when being read and will be ignored when being written into Firestore:  

```kotlin
data class Pojo(@set:DocumentId var foo: String? = null) {
  constructor() : this(null) // Used by Firestore to create new instances
}
```