# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingSupport.md.txt

# GroundingSupport

# GroundingSupport


```
class GroundingSupport
```

<br />

*** ** * ** ***

Provides information about how a specific segment of the model's response is supported by the retrieved grounding chunks.

## Summary

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingSupport#GroundingSupport(com.google.firebase.ai.type.Segment,kotlin.collections.List)(segment: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Segment, groundingChunkIndices: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html>)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingSupport#groundingChunkIndices()` A list of indices that refer to specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingChunk` classes within the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#groundingChunks()` array. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Segment` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingSupport#segment()` Specifies the segment of the model's response content that this grounding support pertains to. |

## Public constructors

### GroundingSupport

```
GroundingSupport(segment: Segment, groundingChunkIndices: List<Int>)
```

## Public properties

### groundingChunkIndices

```
val groundingChunkIndices: List<Int>
```

A list of indices that refer to specific `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingChunk` classes within the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingMetadata#groundingChunks()` array. These referenced chunks are the sources that support the claim made in the associated `segment` of the response. For example, an array `[1, 3, 4]` means that `groundingChunks[1]`, `groundingChunks[3]`, `groundingChunks[4]` are the retrieved content supporting this part of the response.

### segment

```
val segment: Segment
```

Specifies the segment of the model's response content that this grounding support pertains to.