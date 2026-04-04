# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData.md.txt

# MutableData

# MutableData


```
class MutableData
```

<br />

*** ** * ** ***

Instances of this class encapsulate the data and priority at a location. It is used in transactions, and it is intended to be inspected and then updated to the desired data at that location. Note that changes made to a child MutableData instance will be visible to the parent and vice versa.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#child(java.lang.String)(path: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Used to obtain a MutableData instance that encapsulates the data and priority at the given relative path. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterable/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData!>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#getChildren()()` Used to iterate over the immediate children at this location |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#getChildrenCount()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#getKey()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#getPriority()()` Gets the current priority at this location. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#getValue()()` getValue() returns the data contained in this instance as native types. |
| `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#getValue(com.google.firebase.database.GenericTypeIndicator<T>)(t: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/GenericTypeIndicator<T!>)` Due to the way that Java implements generics, it takes an extra step to get back a properly-typed Collection. |
| `T?` | `<T> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#getValue(java.lang.Class<T>)(valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>)` This method is used to marshall the data contained in this instance into a class of your choosing. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#hasChild(java.lang.String)(path: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#hasChildren()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#setPriority(java.lang.Object)(priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Sets the priority at this location |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#setValue(java.lang.Object)(value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` Set the data at this location to the given value. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#toString()()` |

| ### Extension functions |
|---|---|
| `inline T?` | `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData#(com.google.firebase.database.MutableData).getValue()()` Returns the content of the MutableData converted to a POJO. |

## Public functions

### child

```
fun child(path: String): MutableData
```

Used to obtain a MutableData instance that encapsulates the data and priority at the given relative path.

| Parameters |
|---|---|
| `path: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A relative path |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData` | An instance encapsulating the data and priority at the given path |

### equals

```
fun equals(o: Any!): Boolean
```

### getChildren

```
fun getChildren(): (Mutable)Iterable<MutableData!>
```

Used to iterate over the immediate children at this location

```kotlin
    for (MutableData child : parent.getChildren()) {
            ...
    }
```

| Returns |
|---|---|
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-iterable/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-iterable/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData!>` | The immediate children at this location |

### getChildrenCount

```
fun getChildrenCount(): Long
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The number of immediate children at this location |

### getKey

```
fun getKey(): String?
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | The key name of this location, or null if it is the top-most location |

### getPriority

```
fun getPriority(): Any?
```

Gets the current priority at this location. The possible return types are:

- `Double`
- `String`

Note that null is allowed

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The priority at this location as a native type or null if no priority was set |

### getValue

```
fun getValue(): Any?
```

getValue() returns the data contained in this instance as native types. The possible types returned are:

- `Boolean`
- `Long`
- `Double`
- `String`
- `Map<String, Object>`
- `List<Object>`

This list is recursive; the possible types for `https://developer.android.com/reference/kotlin/java/lang/Object.html` in the above list is given by the same list. These types correspond to the types available in JSON.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The data contained in this instance as native types, or null if there is no data at this location. |

### getValue

```
fun <T> getValue(t: GenericTypeIndicator<T!>): T?
```

Due to the way that Java implements generics, it takes an extra step to get back a properly-typed Collection. So, in the case where you want a `https://developer.android.com/reference/kotlin/java/util/List.html` of Message instances, you will need to do something like the following:

```kotlin
    GenericTypeIndicator<List<Message>> t =
        new GenericTypeIndicator<List<Message>>() {};
    List<Message> messages = mutableData.getValue(t);
```
It is important to use a subclass of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/GenericTypeIndicator`. See `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/GenericTypeIndicator` for more details

| Parameters |
|---|---|
| `<T>` | The type to return. Implicitly defined from the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/GenericTypeIndicator` passed in |
| `t: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/GenericTypeIndicator<T!>` | A subclass of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/GenericTypeIndicator` indicating the type of generic collection to be returned. |

| Returns |
|---|---|
| `T?` | A properly typed collection, populated with the data from this instance, or null if there is no data at this location. |

### getValue

```
fun <T> getValue(valueType: Class<T!>): T?
```

This method is used to marshall the data contained in this instance into a class of your choosing. The class must fit 2 simple constraints:

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
    Message m = mutableData.getValue(Message.class);
```

| Parameters |
|---|---|
| `<T>` | The type to return. Implicitly defined from the class passed in |
| `valueType: https://developer.android.com/reference/kotlin/java/lang/Class.html<T!>` | The class into which this data in this instance should be marshalled |

| Returns |
|---|---|
| `T?` | An instance of the class passed in, populated with the data from this instance, or null if there is no data at this location. |

### hasChild

```
fun hasChild(path: String): Boolean
```

| Parameters |
|---|---|
| `path: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A relative path |

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | True if data exists at the given path, otherwise false |

### hasChildren

```
fun hasChildren(): Boolean
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | True if the data at this location has children, false otherwise |

### setPriority

```
fun setPriority(priority: Any?): Unit
```

Sets the priority at this location

| Parameters |
|---|---|
| `priority: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The desired priority or null to clear the existing priority |

### setValue

```
fun setValue(value: Any?): Unit
```

Set the data at this location to the given value. The native types accepted by this method for the value correspond to the JSON types:

- `Boolean`
- `Long`
- `Double`
- `Map<String, Object>`
- `List<Object>`

In addition, you can set instances of your own class into this location, provided they satisfy the following constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

Generic collections of objects that satisfy the above constraints are also permitted, i.e. `Map<String, MyPOJO>`, as well as null values.

Note that this overrides the priority, which must be set separately.

| Parameters |
|---|---|
| `value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?` | The value to set at this location or null to delete the existing data |

| Throws |
|---|---|
| `com.google.firebase.database.DatabaseException: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseException` |   |

### toString

```
fun toString(): String!
```

## Extension functions

### getValue

```
inline fun <T : Any?> MutableData.getValue(): T?
```

Returns the content of the MutableData converted to a POJO.

Supports generics like List\<\> or Map\<\>. Use @JvmSuppressWildcards to force the compiler to use the type `T`, and not `? extends T`.