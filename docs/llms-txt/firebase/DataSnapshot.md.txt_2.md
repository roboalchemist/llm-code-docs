# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot.md.txt

# DataSnapshot

# DataSnapshot


```
public class DataSnapshot
```

<br />

*** ** * ** ***

A DataSnapshot instance contains data from a Firebase Database location. Any time you read Database data, you receive the data as a DataSnapshot. DataSnapshots are passed to the methods in listeners that you attach with `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#addValueEventListener(com.google.firebase.database.ValueEventListener)`, `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#addChildEventListener(com.google.firebase.database.ChildEventListener)`, or `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Query#addListenerForSingleValueEvent(com.google.firebase.database.ValueEventListener)`. They are efficiently-generated immutable copies of the data at a Firebase Database location. They can't be modified and will never change. To modify data at a location, use a `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` reference (e.g. with `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference#setValue(java.lang.Object)`).

## Summary

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#child(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html path)` Get a DataSnapshot for the location at the specified relative path. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#exists()()` Returns true if the snapshot contains a non-null value. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Iterable.html<https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#getChildren()()` Gives access to all of the immediate children of this snapshot. |
| `long` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#getChildrenCount()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#getKey()()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#getPriority()()` Returns the priority of the data contained in this snapshot as a native type. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#getRef()()` Used to obtain a reference to the source location for this snapshot. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#getValue()()` getValue() returns the data contained in this snapshot as native types. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#getValue(com.google.firebase.database.GenericTypeIndicator<T>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator<T> t)` Due to the way that Java implements generics, it takes an extra step to get back a properly-typed Collection. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#getValue(boolean)(boolean useExportFormat)` getValue() returns the data contained in this snapshot as native types. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | `<T> https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#getValue(java.lang.Class<T>)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType)` This method is used to marshall the data contained in this snapshot into a class of your choosing. |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#hasChild(java.lang.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html path)` Can be used to determine if this DataSnapshot has data at a particular location |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#hasChildren()()` Indicates whether this snapshot has any children |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#toString()()` |

| ### Extension functions |
|---|---|
| `final T` | `<T extends https://developer.android.com/reference/kotlin/java/lang/Object.html> https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt.https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot#(com.google.firebase.database.DataSnapshot).getValue()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot receiver)` Returns the content of the DataSnapshot converted to a POJO. |

## Public methods

### child

```
public @NonNull DataSnapshot child(@NonNull String path)
```

Get a DataSnapshot for the location at the specified relative path. The relative path can either be a simple child key (e.g. 'fred') or a deeper slash-separated path (e.g. 'fred/name/first'). If the child location has no data, an empty DataSnapshot is returned.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html path` | A relative path to the location of child data |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot` | The DataSnapshot for the child location |

### exists

```
public boolean exists()
```

Returns true if the snapshot contains a non-null value.

| Returns |
|---|---|
| `boolean` | True if the snapshot contains a non-null value, otherwise false |

### getChildren

```
public @NonNull Iterable<DataSnapshot> getChildren()
```

Gives access to all of the immediate children of this snapshot. Can be used in native for loops:

```
for (DataSnapshot child : parent.getChildren()) {
      ...
}
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Iterable.html<https://firebase.google.com/docs/reference/android/com/google/firebase/database/DataSnapshot>` | The immediate children of this snapshot |

### getChildrenCount

```
public long getChildrenCount()
```

| Returns |
|---|---|
| `long` | The number of immediate children in the this snapshot |

### getKey

```
public @Nullable String getKey()
```

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | The key name for the source location of this snapshot or null if this snapshot points to the database root. |

### getPriority

```
public @Nullable Object getPriority()
```

Returns the priority of the data contained in this snapshot as a native type. Possible return types:

- `Double`
- `String`

Note that null is also allowed

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | the priority of the data contained in this snapshot as a native type |

### getRef

```
public @NonNull DatabaseReference getRef()
```

Used to obtain a reference to the source location for this snapshot.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseReference` | A DatabaseReference corresponding to the location that this snapshot came from |

### getValue

```
public @Nullable Object getValue()
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
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | The data contained in this snapshot as native types or null if there is no data at this location. |

### getValue

```
public @Nullable T <T> getValue(@NonNull GenericTypeIndicator<T> t)
```

Due to the way that Java implements generics, it takes an extra step to get back a properly-typed Collection. So, in the case where you want a `https://developer.android.com/reference/kotlin/java/util/List.html` of Message instances, you will need to do something like the following:

```
    GenericTypeIndicator<List<Message>> t = new GenericTypeIndicator<List<Message>>() {};
    List<Message> messages = snapshot.getValue(t);
```
It is important to use a subclass of `https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator`. See `https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator` for more details

| Parameters |
|---|---|
| `<T>` | The type to return. Implicitly defined from the `https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator` passed in |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator<T> t` | A subclass of `https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator` indicating the type of generic collection to be returned. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | A properly typed collection, populated with the data from this snapshot, or null if there is no data at this location. |

### getValue

```
public @Nullable Object getValue(boolean useExportFormat)
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
| `boolean useExportFormat` | Whether or not to include priority information |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Object.html` | The data in native types, along with its priority, or null if there is no data at this location. |

### getValue

```
public @Nullable T <T> getValue(@NonNull Class<T> valueType)
```

This method is used to marshall the data contained in this snapshot into a class of your choosing. The class must fit 2 simple constraints:

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
    Message m = snapshot.getValue(Message.class);
```

| Parameters |
|---|---|
| `<T>` | The type to return. Implicitly defined from the class passed in |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Class.html<T> valueType` | The class into which this snapshot should be marshalled |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html T` | An instance of the class passed in, populated with the data from this snapshot, or null if there is no data at this location. |

### hasChild

```
public boolean hasChild(@NonNull String path)
```

Can be used to determine if this DataSnapshot has data at a particular location

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html path` | A relative path to the location of child data |

| Returns |
|---|---|
| `boolean` | Whether or not the specified child location has data |

### hasChildren

```
public boolean hasChildren()
```

Indicates whether this snapshot has any children

| Returns |
|---|---|
| `boolean` | True if the snapshot has any children, otherwise false |

### toString

```
public String toString()
```

## Extension functions

### DatabaseKt.getValue

```
public final T <T extends Object> DatabaseKt.getValue(@NonNull DataSnapshot receiver)
```

Returns the content of the DataSnapshot converted to a POJO.

Supports generics like List\<\> or Map\<\>. Use @JvmSuppressWildcards to force the compiler to use the type `T`, and not `? extends T`.