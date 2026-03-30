# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData.md.txt

# MutableData

# MutableData


```
public class MutableData
```

<br />

*** ** * ** ***

Instances of this class encapsulate the data and priority at a location. It is used in transactions, and it is intended to be inspected and then updated to the desired data at that location. Note that changes made to a child MutableData instance will be visible to the parent and vice versa.

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#child(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html path)` Used to obtain a MutableData instance that encapsulates the data and priority at the given relative path. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Iterable.html<https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getChildren()()` Used to iterate over the immediate children at this location |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getChildrenCount()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getKey()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getPriority()()` Gets the current priority at this location. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getValue()()` getValue() returns the data contained in this instance as native types. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getValue(com.google.firebase.database.GenericTypeIndicator<T>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator<T> t)` Due to the way that Java implements generics, it takes an extra step to get back a properly-typed Collection. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getValue(java.lang.Class<T>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType)` This method is used to marshall the data contained in this instance into a class of your choosing. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#hasChild(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html path)` |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#hasChildren()()` |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#setPriority(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html priority)` Sets the priority at this location |
| `void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#setValue(java.lang.Object)(@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value)` Set the data at this location to the given value. |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#toString()()` |

| ### Extension functions |
|---|---|
| `final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#(com.google.firebase.database.MutableData).getValue()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData receiver)` Returns the content of the MutableData converted to a POJO. |

## Public methods

### child

```
public @NonNull MutableData child(@NonNull String path)
```

Used to obtain a MutableData instance that encapsulates the data and priority at the given relative path.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html path` | A relative path |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData` | An instance encapsulating the data and priority at the given path |

### equals

```
public boolean equals(Object o)
```

### getChildren

```
public @NonNull Iterable<MutableData> getChildren()
```

Used to iterate over the immediate children at this location

```
    for (MutableData child : parent.getChildren()) {
            ...
    }
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Iterable.html<https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData>` | The immediate children at this location |

### getChildrenCount

```
public long getChildrenCount()
```

| Returns |
|---|---|
| `long` | The number of immediate children at this location |

### getKey

```
public @Nullable String getKey()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | The key name of this location, or null if it is the top-most location |

### getPriority

```
public @Nullable Object getPriority()
```

Gets the current priority at this location. The possible return types are:

- `Double`
- `String`

Note that null is allowed

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | The priority at this location as a native type or null if no priority was set |

### getValue

```
public @Nullable Object getValue()
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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | The data contained in this instance as native types, or null if there is no data at this location. |

### getValue

```
public @Nullable T <T> getValue(@NonNull GenericTypeIndicator<T> t)
```

Due to the way that Java implements generics, it takes an extra step to get back a properly-typed Collection. So, in the case where you want a `https://developer.android.com/reference/kotlin/java/util/List.html` of Message instances, you will need to do something like the following:

```
    GenericTypeIndicator<List<Message>> t =
        new GenericTypeIndicator<List<Message>>() {};
    List<Message> messages = mutableData.getValue(t);
```
It is important to use a subclass of `https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator`. See `https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator` for more details

| Parameters |
|---|---|
| `<T>` | The type to return. Implicitly defined from the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator` passed in |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator<T> t` | A subclass of `https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator` indicating the type of generic collection to be returned. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | A properly typed collection, populated with the data from this instance, or null if there is no data at this location. |

### getValue

```
public @Nullable T <T> getValue(@NonNull Class<T> valueType)
```

This method is used to marshall the data contained in this instance into a class of your choosing. The class must fit 2 simple constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

An example class might look like:

```
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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType` | The class into which this data in this instance should be marshalled |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | An instance of the class passed in, populated with the data from this instance, or null if there is no data at this location. |

### hasChild

```
public boolean hasChild(@NonNull String path)
```

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html path` | A relative path |

| Returns |
|---|---|
| `boolean` | True if data exists at the given path, otherwise false |

### hasChildren

```
public boolean hasChildren()
```

| Returns |
|---|---|
| `boolean` | True if the data at this location has children, false otherwise |

### setPriority

```
public void setPriority(@Nullable Object priority)
```

Sets the priority at this location

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html priority` | The desired priority or null to clear the existing priority |

### setValue

```
public void setValue(@Nullable Object value)
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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html value` | The value to set at this location or null to delete the existing data |

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseException com.google.firebase.database.DatabaseException` |   |

### toString

```
public String toString()
```

## Extension functions

### DatabaseKt.getValue

```
public final T <T extends Object> DatabaseKt.getValue(@NonNull MutableData receiver)
```

Returns the content of the MutableData converted to a POJO.

Supports generics like List\<\> or Map\<\>. Use @JvmSuppressWildcards to force the compiler to use the type `T`, and not `? extends T`.