# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData.md.txt

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

|                                                                                                                                         ### Public methods                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MutableData](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData)                                                                                         | [child](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#child(java.lang.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` path)` Used to obtain a MutableData instance that encapsulates the data and priority at the given relative path.                                                                                                   |
| `boolean`                                                                                                                                                                                                                                                                                          | [equals](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#equals(java.lang.Object))`(`[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)` o)`                                                                                                                                                                                                                                                                                                            |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Iterable](https://developer.android.com/reference/kotlin/java/lang/Iterable.html)`<`[MutableData](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData)`>` | [getChildren](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getChildren())`()` Used to iterate over the immediate children at this location                                                                                                                                                                                                                                                                                                                                       |
| `long`                                                                                                                                                                                                                                                                                             | [getChildrenCount](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getChildrenCount())`()`                                                                                                                                                                                                                                                                                                                                                                                          |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                                                                                                   | [getKey](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getKey())`()`                                                                                                                                                                                                                                                                                                                                                                                                              |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)                                                                                                                   | [getPriority](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getPriority())`()` Gets the current priority at this location.                                                                                                                                                                                                                                                                                                                                                        |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)                                                                                                                   | [getValue](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getValue())`()` getValue() returns the data contained in this instance as native types.                                                                                                                                                                                                                                                                                                                                  |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` T`                                                                                                                                                                                                | `<T> `[getValue](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getValue(com.google.firebase.database.GenericTypeIndicator<T>))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenericTypeIndicator](https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator)`<T> t)` Due to the way that Java implements generics, it takes an extra step to get back a properly-typed Collection. |
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` T`                                                                                                                                                                                                | `<T> `[getValue](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#getValue(java.lang.Class<T>))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T> valueType)` This method is used to marshall the data contained in this instance into a class of your choosing.                                                                                      |
| `boolean`                                                                                                                                                                                                                                                                                          | [hasChild](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#hasChild(java.lang.String))`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` path)`                                                                                                                                                                                                       |
| `boolean`                                                                                                                                                                                                                                                                                          | [hasChildren](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#hasChildren())`()`                                                                                                                                                                                                                                                                                                                                                                                                    |
| `void`                                                                                                                                                                                                                                                                                             | [setPriority](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#setPriority(java.lang.Object))`(@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)` priority)` Sets the priority at this location                                                                                                                                                        |
| `void`                                                                                                                                                                                                                                                                                             | [setValue](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#setValue(java.lang.Object))`(@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)` value)` Set the data at this location to the given value.                                                                                                                                                  |
| [String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                                                                                                                                                                                                     | [toString](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#toString())`()`                                                                                                                                                                                                                                                                                                                                                                                                          |

| ### Extension functions |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final T`               | `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[DatabaseKt](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseKt)`.`[getValue](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData#(com.google.firebase.database.MutableData).getValue())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MutableData](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData)` receiver)` Returns the content of the MutableData converted to a POJO. |

## Public methods

### child

```
publicÂ @NonNull MutableDataÂ child(@NonNull StringÂ path)
```

Used to obtain a MutableData instance that encapsulates the data and priority at the given relative path.  

|                                                                                      Parameters                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` path` | A relative path |

|                                                                                                  Returns                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[MutableData](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData) | An instance encapsulating the data and priority at the given path |

### equals

```
publicÂ booleanÂ equals(ObjectÂ o)
```  

### getChildren

```
publicÂ @NonNull Iterable<MutableData>Â getChildren()
```

Used to iterate over the immediate children at this location  

```text
    for (MutableData child : parent.getChildren()) {
        Â Â Â Â ...
    }
```  

|                                                                                                                                              Returns                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Iterable](https://developer.android.com/reference/kotlin/java/lang/Iterable.html)`<`[MutableData](https://firebase.google.com/docs/reference/android/com/google/firebase/database/MutableData)`>` | The immediate children at this location |

### getChildrenCount

```
publicÂ longÂ getChildrenCount()
```  

| Returns |
|---------|---------------------------------------------------|
| `long`  | The number of immediate children at this location |

### getKey

```
publicÂ @Nullable StringÂ getKey()
```  

|                                                                                     Returns                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | The key name of this location, or null if it is the top-most location |

### getPriority

```
publicÂ @Nullable ObjectÂ getPriority()
```

Gets the current priority at this location. The possible return types are:

- `Double`
- `String`

Note that null is allowed  

|                                                                                     Returns                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) | The priority at this location as a native type or null if no priority was set |

### getValue

```
publicÂ @Nullable ObjectÂ getValue()
```

getValue() returns the data contained in this instance as native types. The possible types returned are:

- `Boolean`
- `Long`
- `Double`
- `String`
- `Map<String, Object>`
- `List<Object>`

This list is recursive; the possible types for [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) in the above list is given by the same list. These types correspond to the types available in JSON.  

|                                                                                     Returns                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) | The data contained in this instance as native types, or null if there is no data at this location. |

### getValue

```
publicÂ @Nullable TÂ <T> getValue(@NonNull GenericTypeIndicator<T>Â t)
```

Due to the way that Java implements generics, it takes an extra step to get back a properly-typed Collection. So, in the case where you want a [java.util.List](https://developer.android.com/reference/kotlin/java/util/List.html) of Message instances, you will need to do something like the following:  

```text
    GenericTypeIndicator<List<Message>> t =
        new GenericTypeIndicator<List<Message>>() {};
    List<Message> messages = mutableData.getValue(t);
```
It is important to use a subclass of [GenericTypeIndicator](https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator). See [GenericTypeIndicator](https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator) for more details  

|                                                                                                             Parameters                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T>`                                                                                                                                                                                                                               | The type to return. Implicitly defined from the [GenericTypeIndicator](https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator) passed in               |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[GenericTypeIndicator](https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator)`<T> t` | A subclass of [GenericTypeIndicator](https://firebase.google.com/docs/reference/android/com/google/firebase/database/GenericTypeIndicator) indicating the type of generic collection to be returned. |

|                                               Returns                                               |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` T` | A properly typed collection, populated with the data from this instance, or null if there is no data at this location. |

### getValue

```
publicÂ @Nullable TÂ <T> getValue(@NonNull Class<T>Â valueType)
```

This method is used to marshall the data contained in this instance into a class of your choosing. The class must fit 2 simple constraints:

1. The class must have a default constructor that takes no arguments
2. The class must define public getters for the properties to be assigned. Properties without a public getter will be set to their default value when an instance is deserialized

An example class might look like:  

```perl6
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

|                                                                                         Parameters                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| `<T>`                                                                                                                                                                                       | The type to return. Implicitly defined from the class passed in      |
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Class](https://developer.android.com/reference/kotlin/java/lang/Class.html)`<T> valueType` | The class into which this data in this instance should be marshalled |

|                                               Returns                                               |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` T` | An instance of the class passed in, populated with the data from this instance, or null if there is no data at this location. |

### hasChild

```
publicÂ booleanÂ hasChild(@NonNull StringÂ path)
```  

|                                                                                      Parameters                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| `@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` path` | A relative path |

|  Returns  |
|-----------|--------------------------------------------------------|
| `boolean` | True if data exists at the given path, otherwise false |

### hasChildren

```
publicÂ booleanÂ hasChildren()
```  

|  Returns  |
|-----------|-----------------------------------------------------------------|
| `boolean` | True if the data at this location has children, false otherwise |

### setPriority

```
publicÂ voidÂ setPriority(@Nullable ObjectÂ priority)
```

Sets the priority at this location  

|                                                                                         Parameters                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)` priority` | The desired priority or null to clear the existing priority |

### setValue

```
publicÂ voidÂ setValue(@Nullable ObjectÂ value)
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

|                                                                                        Parameters                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `@`[Nullable](https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html)` `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)` value` | The value to set at this location or null to delete the existing data |

|                                                                                                Throws                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [com.google.firebase.database.DatabaseException](https://firebase.google.com/docs/reference/android/com/google/firebase/database/DatabaseException)` com.google.firebase.database.DatabaseException` |   |

### toString

```
publicÂ StringÂ toString()
```  

## Extension functions

### DatabaseKt.getValue

```
publicÂ finalÂ TÂ <TÂ extendsÂ Object> DatabaseKt.getValue(@NonNull MutableDataÂ receiver)
```

Returns the content of the MutableData converted to a POJO.

Supports generics like List\<\> or Map\<\>. Use @JvmSuppressWildcards to force the compiler to use the type `T`, and not `? extends T`.