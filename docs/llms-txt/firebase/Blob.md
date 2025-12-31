# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Blob.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob.md.txt

# Blob

# Blob


```
class Blob : Comparable
```

<br />

*** ** * ** ***

Immutable class representing an array of bytes in Cloud Firestore.

## Summary

|                                                                           ### Public functions                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                | [compareTo](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob#compareTo(com.google.firebase.firestore.Blob))`(other: `[Blob](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob)`)`                       |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                        | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob#equals(java.lang.Object))`(other: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`?)`                                                                |
| `java-static `[Blob](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob)                                                                | [fromBytes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob#fromBytes(byte[]))`(bytes: `[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)`)` Creates a new `Blob` instance from the provided bytes. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob#hashCode())`()`                                                                                                                                                                |
| [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)`<`[Byte](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html)`>` | [toBytes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob#toBytes())`()`                                                                                                                                                                  |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)                                                                                          | [toString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob#toString())`()`                                                                                                                                                                |

## Public functions

### compareTo

```
funÂ compareTo(other:Â Blob):Â Int
```  

### equals

```
funÂ equals(other:Â Any?):Â Boolean
```  

### fromBytes

```
java-staticÂ funÂ fromBytes(bytes:Â ByteArray):Â Blob
```

Creates a new `Blob` instance from the provided bytes. Will make a copy of the bytes passed in.  

|                                            Parameters                                            |
|--------------------------------------------------------------------------------------------------|--------------------------------------------|
| `bytes: `[ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html) | The bytes to use for this `Blob` instance. |

|                                           Returns                                            |
|----------------------------------------------------------------------------------------------|-------------------------|
| [Blob](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob) | The new `Blob` instance |

### hashCode

```
funÂ hashCode():Â Int
```  

### toBytes

```
funÂ toBytes():Â ByteArray<Byte>
```  

|                                                                                  Returns                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)`<`[Byte](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html)`>` | The bytes of this blob as a new byte\[\] array. |

### toString

```
funÂ toString():Â String
```