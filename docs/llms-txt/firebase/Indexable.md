# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.md.txt

# Indexable

public interface **Indexable**  
Represents an indexable unit.

Indexables are constructed via [Indexable.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Builder)
and indexed via [FirebaseAppIndex.update(Indexable...)](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#update(com.google.firebase.appindexing.Indexable...)). Convenience methods to construct
[Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
objects for common data types are available via [Indexables](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/builders/Indexables).

Indexables are not thread-safe. Do not create, modify, or access one Indexable from
different threads, otherwise a [ConcurrentModificationException](https://developer.android.com/reference/java/util/ConcurrentModificationException.html)
could be thrown.  

### Nested Class Summary

|-----------|---|---|-------------------------------------------------------------------------------------------------------------------------------------------|
| class     | [Indexable.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Builder) || The builder for [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable).                |
| interface | [Indexable.Metadata](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable.Metadata) || Represents the metadata for an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable). |

### Constant Summary

|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int | [MAX_BYTE_SIZE](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable#MAX_BYTE_SIZE)                                                       | The maximum byte size of an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable).                                                                                                                                                                                                                                                                                            |
| int | [MAX_INDEXABLES_TO_BE_UPDATED_IN_ONE_CALL](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable#MAX_INDEXABLES_TO_BE_UPDATED_IN_ONE_CALL) | The maximum number of arguments that can be passed to [FirebaseAppIndex.update(Indexable...)](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#update(com.google.firebase.appindexing.Indexable...)) or [FirebaseAppIndex.remove(String...)](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#remove(java.lang.String...)). |
| int | [MAX_NESTING_DEPTH](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable#MAX_NESTING_DEPTH)                                               | The maximum nesting depth of [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s.                                                                                                                                                                                                                                                                                          |
| int | [MAX_NUMBER_OF_FIELDS](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable#MAX_NUMBER_OF_FIELDS)                                         | The maximum number of fields an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) can have.                                                                                                                                                                                                                                                                               |
| int | [MAX_REPEATED_SIZE](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable#MAX_REPEATED_SIZE)                                               | The maximum number of elements in a repeatable [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) field.                                                                                                                                                                                                                                                                   |
| int | [MAX_STRING_LENGTH](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable#MAX_STRING_LENGTH)                                               | The maximum [String.length()](https://developer.android.com/reference/java/lang/String.html#length()) of a [String](https://developer.android.com/reference/java/lang/String.html) field of an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable).                                                                                                                         |
| int | [MAX_URL_LENGTH](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable#MAX_URL_LENGTH)                                                     | The maximum [String.length()](https://developer.android.com/reference/java/lang/String.html#length()) of an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable) URL string.                                                                                                                                                                                                 |

## Constants

#### public static final int
**MAX_BYTE_SIZE**

The maximum byte size of an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable).  
Constant Value: 30000  

#### public static final int
**MAX_INDEXABLES_TO_BE_UPDATED_IN_ONE_CALL**

The maximum number of arguments that can be passed to [FirebaseAppIndex.update(Indexable...)](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#update(com.google.firebase.appindexing.Indexable...)) or [FirebaseAppIndex.remove(String...)](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/FirebaseAppIndex#remove(java.lang.String...)).  
Constant Value: 1000  

#### public static final int
**MAX_NESTING_DEPTH**

The maximum nesting depth of [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)s.  
Constant Value: 5  

#### public static final int
**MAX_NUMBER_OF_FIELDS**

The maximum number of fields an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
can have.  
Constant Value: 20  

#### public static final int
**MAX_REPEATED_SIZE**

The maximum number of elements in a repeatable [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
field. Additional elements will be discarded.  
Constant Value: 100  

#### public static final int
**MAX_STRING_LENGTH**

The maximum [String.length()](https://developer.android.com/reference/java/lang/String.html#length())
of a [String](https://developer.android.com/reference/java/lang/String.html) field of an
[Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable).
[String](https://developer.android.com/reference/java/lang/String.html)s longer
than this will be truncated.  
Constant Value: 20000  

#### public static final int
**MAX_URL_LENGTH**

The maximum [String.length()](https://developer.android.com/reference/java/lang/String.html#length())
of an [Indexable](https://firebase.google.com/docs/reference/android/com/google/firebase/appindexing/Indexable)
URL string.  
Constant Value: 256