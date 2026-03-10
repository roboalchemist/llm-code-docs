# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Segment.md.txt

# Segment

# Segment


```
class Segment
```

<br />

*** ** * ** ***

Represents a specific segment within a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` object, often used to pinpoint the exact location of text or data that grounding information refers to.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Segment#Segment(kotlin.Int,kotlin.Int,kotlin.Int,kotlin.String)(startIndex: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, endIndex: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, partIndex: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html, text: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Segment#endIndex()` The zero-based end index of the segment within the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part`, measured in UTF-8 bytes. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Segment#partIndex()` The zero-based index of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part` object within the `parts` array of its parent `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` object. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Segment#startIndex()` The zero-based start index of the segment within the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part`, measured in UTF-8 bytes. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Segment#text()` The text corresponding to the segment from the response. |

## Public constructors

### Segment

```
Segment(startIndex: Int, endIndex: Int, partIndex: Int, text: String)
```

## Public properties

### endIndex

```
val endIndex: Int
```

The zero-based end index of the segment within the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part`, measured in UTF-8 bytes. This offset is exclusive, meaning the character at this index is not included in the segment.

### partIndex

```
val partIndex: Int
```

The zero-based index of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part` object within the `parts` array of its parent `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Content` object. This identifies which part of the content the segment belongs to.

### startIndex

```
val startIndex: Int
```

The zero-based start index of the segment within the specified `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Part`, measured in UTF-8 bytes. This offset is inclusive, starting from 0 at the beginning of the part's content.

### text

```
val text: String
```

The text corresponding to the segment from the response.