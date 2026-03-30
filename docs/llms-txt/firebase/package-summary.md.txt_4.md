# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/package-summary.md.txt

# com.google.firebase.database

### Annotations

|---|---|
| [Exclude](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Exclude) | Marks a field as excluded from the Database. |
| [IgnoreExtraProperties](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/IgnoreExtraProperties) | Properties that don't map to class fields are ignored when serializing to a class annotated with this annotation. |
| [PropertyName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/PropertyName) | Marks a field to be renamed when serialized. |
| [ThrowOnExtraProperties](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ThrowOnExtraProperties) | Properties that don't map to class fields when serializing to a class annotated with this annotation cause an exception to be thrown. |

### Interfaces

|---|---|
| [ChildEventListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ChildEventListener) | Classes implementing this interface can be used to receive events about changes in the child locations of a given `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference` ref. |
| [DatabaseReference.CompletionListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference.CompletionListener) | This interface is used as a method of being notified when an operation has been acknowledged by the Database servers and can be considered complete |
| [Transaction.Handler](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler) | An object implementing this interface is used to run a transaction, and will be notified of the results of the transaction. |
| [ValueEventListener](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ValueEventListener) | Classes implementing this interface can be used to receive events about data changes at a location. |

### Classes

|---|---|
| [DatabaseError](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError) | Instances of DatabaseError are passed to callbacks when an operation failed. |
| [DatabaseReference](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference) | A Firebase reference represents a particular location in your Database and can be used for reading or writing data to that Database location. |
| [DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) | A DataSnapshot instance contains data from a Firebase Database location. |
| [FirebaseDatabase](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase) | The entry point for accessing a Firebase Database. |
| [GenericTypeIndicator](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/GenericTypeIndicator)\<T\> | Due to the way that Java implements generics (type-erasure), it is necessary to use a slightly more complicated method to properly resolve types for generic collections at runtime. |
| [MutableData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData) | Instances of this class encapsulate the data and priority at a location. |
| [OnDisconnect](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/OnDisconnect) | The OnDisconnect class is used to manage operations that will be run on the server when this client disconnects. |
| [Query](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Query) | The Query class (and its subclass, `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference`) are used for reading data. |
| [ServerValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/ServerValue) | Contains placeholder values to use when writing data to the Firebase Database. |
| [Transaction](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction) | The Transaction class encapsulates the functionality needed to perform a transaction on the data at a location. |
| [Transaction.Result](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result) | Instances of this class represent the desired outcome of a single run of a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler`'s doTransaction method. |

### Exceptions

|---|---|
| [DatabaseException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseException) | This error is thrown when the Firebase Database library is unable to operate on the input it has been given. |