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

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob#compareTo(com.google.firebase.firestore.Blob)(other: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob)` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob#equals(java.lang.Object)(other: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?)` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob#fromBytes(byte[])(bytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html)` Creates a new `Blob` instance from the provided bytes. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob#hashCode()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob#toBytes()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob#toString()()` |

## Public functions

### compareTo

```
fun compareTo(other: Blob): Int
```

### equals

```
fun equals(other: Any?): Boolean
```

### fromBytes

```
java-static fun fromBytes(bytes: ByteArray): Blob
```

Creates a new `Blob` instance from the provided bytes. Will make a copy of the bytes passed in.

| Parameters |
|---|---|
| `bytes: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html` | The bytes to use for this `Blob` instance. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Blob` | The new `Blob` instance |

### hashCode

```
fun hashCode(): Int
```

### toBytes

```
fun toBytes(): ByteArray<Byte>
```

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte-array/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-byte/index.html>` | The bytes of this blob as a new byte\[\] array. |

### toString

```
fun toString(): String
```