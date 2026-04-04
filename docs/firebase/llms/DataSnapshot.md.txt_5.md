# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot.md.txt

# DataSnapshot

# DataSnapshot


```
class DataSnapshot
```

<br />

*** ** * ** ***

A DataSnapshot instance contains data from a Firebase Database location. Any time you read Database data, you receive the data as a DataSnapshot. DataSnapshots are passed to the methods in listeners that you attach with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#addValueEventListener(com.google.firebase.database.ValueEventListener)`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#addChildEventListener(com.google.firebase.database.ChildEventListener)`, or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Query#addListenerForSingleValueEvent(com.google.firebase.database.ValueEventListener)`. They are efficiently-generated immutable copies of the data at a Firebase Database location. They can't be modified and will never change. To modify data at a location, use a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` reference (e.g. with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#setValue(java.lang.Object)`).

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#child(java.lang.String)(path: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Get a DataSnapshot for the location at the specified relative path. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#exists()()` Returns true if the snapshot contains a non-null value. |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterable/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#getChildren()()` Gives access to all of the immediate children of this snapshot. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#getChildrenCount()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#getKey()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#getPriority()()` Returns the priority of the data contained in this snapshot as a native type. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#getRef()()` Used to obtain a reference to the source location for this snapshot. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#getValue()()` getValue() returns the data contained in this snapshot as native types. |
| `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#getValue(com.google.firebase.database.GenericTypeIndicator<T>)(t: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/GenericTypeIndicator<T!>)` Due to the way that Java implements generics, it takes an extra step to get back a properly-typed Collection. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#getValue(boolean)(useExportFormat: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` getValue() returns the data contained in this snapshot as native types. |
| `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#getValue(java.lang.Class<T>)(valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>)` This method is used to marshall the data contained in this snapshot into a class of your choosing. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#hasChild(java.lang.String)(path: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Can be used to determine if this DataSnapshot has data at a particular location |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#hasChildren()()` Indicates whether this snapshot has any children |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#toString()()` |

| ### Extension functions |
|---|---|
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot#(com.google.firebase.database.DataSnapshot).getValue()()` Returns the content of the DataSnapshot converted to a POJO. |

## Public functions

### child

```
fun child(path: String): DataSnapshot
```

Get a DataSnapshot for the location at the specified relative path. The relative path can either be a simple child key (e.g. 'fred') or a deeper slash-separated path (e.g. 'fred/name/first'). If the child location has no data, an empty DataSnapshot is returned.

| Parameters |
|---|---|
| `path: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A relative path to the location of child data |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot` | The DataSnapshot for the child location |

### exists

```
fun exists(): Boolean
```

Returns true if the snapshot contains a non-null value.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | True if the snapshot contains a non-null value, otherwise false |

### getChildren

```
fun getChildren(): (Mutable)Iterable<DataSnapshot!>
```

Gives access to all of the immediate children of this snapshot. Can be used in native for loops:

```kotlin
for (DataSnapshot child : parent.getChildren()) {
      ...
}
```

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterable/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DataSnapshot!>` | The immediate children of this snapshot |

### getChildrenCount

```
fun getChildrenCount(): Long
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The number of immediate children in the this snapshot |

### getKey

```
fun getKey(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The key name for the source location of this snapshot or null if this snapshot points to the database root. |

### getPriority

```
fun getPriority(): Any?
```

Returns the priority of the data contained in this snapshot as a native type. Possible return types:

- `Double`
- `String`

Note that null is also allowed

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | the priority of the data contained in this snapshot as a native type |

### getRef

```
fun getRef(): DatabaseReference
```

Used to obtain a reference to the source location for this snapshot.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference` | A DatabaseReference corresponding to the location that this snapshot came from |

### getValue

```
fun getValue(): Any?
```

getValue() returns the data contained in this snapshot as native types. The possible types returned are:

- `Boolean`
- `String`
- `Long`
- `Double`
- `Map<String, Object>`
- `List<Object>`

This list is recursive; the possible types for `https://developer.android.com/reference/kotlin/java/lang/Object.html` in the above list is given by the same list. These types correspond to the types available in JSON.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The data contained in this snapshot as native types or null if there is no data at this location. |

### getValue

```
fun <T> getValue(t: GenericTypeIndicator<T!>): T?
```

Due to the way that Java implements generics, it takes an extra step to get back a properly-typed Collection. So, in the case where you want a `https://developer.android.com/reference/kotlin/java/util/List.html` of Message instances, you will need to do something like the following:

```kotlin
    GenericTypeIndicator<List<Message>> t = new GenericTypeIndicator<List<Message>>() {};
    List<Message> messages = snapshot.getValue(t);
```
It is important to use a subclass of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/GenericTypeIndicator`. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/GenericTypeIndicator` for more details

| Parameters |
|---|---|
| `<T>` | The type to return. Implicitly defined from the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/GenericTypeIndicator` passed in |
| `t: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/GenericTypeIndicator<T!>` | A subclass of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/GenericTypeIndicator` indicating the type of generic collection to be returned. |

| Returns |
|---|---|
| `T?` | A properly typed collection, populated with the data from this snapshot, or null if there is no data at this location. |

### getValue

```
fun getValue(useExportFormat: Boolean): Any?
```

getValue() returns the data contained in this snapshot as native types. The possible types returned are:

- `Boolean`
- `String`
- `Long`
- `Double`
- `Map<String, Object>`
- `List<Object>`

This list is recursive; the possible types for `https://developer.android.com/reference/kotlin/java/lang/Object.html` in the above list is given by the same list. These types correspond to the types available in JSON.

If useExportFormat is set to true, priority information will be included in the output. Priority information shows up as a .priority key in a map. For data that would not otherwise be a map, the map will also include a .value key with the data.

| Parameters |
|---|---|
| `useExportFormat: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | Whether or not to include priority information |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The data in native types, along with its priority, or null if there is no data at this location. |

### getValue

```
fun <T> getValue(valueType: Class<T!>): T?
```

This method is used to marshall the data contained in this snapshot into a class of your choosing. The class must fit 2 simple constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

An example class might look like:

```kotlin
    class Message {
        private String author;
        private String text;

        private Message() {}

        public Message(String author, String text) {
            this.author = author;
            this.text = text;
        }

        public String getAuthor() {
            return author;
        }

        public String getText() {
            return text;
        }
    }


    // Later
    Message m = snapshot.getValue(Message.class);
```

| Parameters |
|---|---|
| `<T>` | The type to return. Implicitly defined from the class passed in |
| `valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>` | The class into which this snapshot should be marshalled |

| Returns |
|---|---|
| `T?` | An instance of the class passed in, populated with the data from this snapshot, or null if there is no data at this location. |

### hasChild

```
fun hasChild(path: String): Boolean
```

Can be used to determine if this DataSnapshot has data at a particular location

| Parameters |
|---|---|
| `path: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A relative path to the location of child data |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | Whether or not the specified child location has data |

### hasChildren

```
fun hasChildren(): Boolean
```

Indicates whether this snapshot has any children

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | True if the snapshot has any children, otherwise false |

### toString

```
fun toString(): String!
```

## Extension functions

### getValue

```
inline fun <T : Any?> DataSnapshot.getValue(): T?
```

Returns the content of the DataSnapshot converted to a POJO.

Supports generics like List\<\> or Map\<\>. Use @JvmSuppressWildcards to force the compiler to use the type `T`, and not `? extends T`.