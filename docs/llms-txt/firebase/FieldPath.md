# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FieldPath.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath.md.txt

# FieldPath

# FieldPath


```
class FieldPath
```

<br />

*** ** * ** ***

A `FieldPath` refers to a field in a document. The path may consist of a single field name (referring to a top level field in the document), or a list of field names (referring to a nested field in the document).

## Summary

|                                                 ### Public functions                                                 |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath) | [documentId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath#documentId())`()` Returns A special sentinel `FieldPath` to refer to the ID of a document.                                                                                                                                                                  |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                   | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath#equals(java.lang.Object))`(o: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!)`                                                                                                                                                   |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                           | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath#hashCode())`()`                                                                                                                                                                                                                                               |
| `java-static `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath) | [of](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath#of(java.lang.String...))`(fieldNames: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>!)` Creates a `FieldPath` from the provided field names. |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                  | [toString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath#toString())`()`                                                                                                                                                                                                                                               |

## Public functions

### documentId

```
java-staticÂ funÂ documentId():Â FieldPath
```

Returns A special sentinel `FieldPath` to refer to the ID of a document. It can be used in queries to sort or filter by the document ID.  

### equals

```
funÂ equals(o:Â Any!):Â Boolean
```  

### hashCode

```
funÂ hashCode():Â Int
```  

### of

```
java-staticÂ funÂ of(fieldNames:Â Array<String!>!):Â FieldPath
```

Creates a `FieldPath` from the provided field names. If more than one field name is provided, the path will point to a nested field in a document.  

|                                                                                      Parameters                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| `fieldNames: `[Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>!` | A list of field names. |

|                                                Returns                                                 |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath) | A `FieldPath` that points to a field location in a document. |

### toString

```
funÂ toString():Â String!
```