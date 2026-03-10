# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingSupport.md.txt

# GroundingSupport

# GroundingSupport


```
public final class GroundingSupport
```

<br />

*** ** * ** ***

Provides information about how a specific segment of the model's response is supported by the retrieved grounding chunks.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Integer.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingSupport#groundingChunkIndices()` A list of indices that refer to specific `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingChunk` classes within the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingMetadata#groundingChunks()` array. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Segment` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingSupport#segment()` Specifies the segment of the model's response content that this grounding support pertains to. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingSupport#GroundingSupport(com.google.firebase.ai.type.Segment,kotlin.collections.List)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Segment segment, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/Integer.html> groundingChunkIndices )` |

## Public fields

### groundingChunkIndices

```
public final @NonNull List<@NonNull Integer> groundingChunkIndices
```

A list of indices that refer to specific `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingChunk` classes within the `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingMetadata#groundingChunks()` array. These referenced chunks are the sources that support the claim made in the associated `segment` of the response. For example, an array `[1, 3, 4]` means that `groundingChunks[1]`, `groundingChunks[3]`, `groundingChunks[4]` are the retrieved content supporting this part of the response.

### segment

```
public final @NonNull Segment segment
```

Specifies the segment of the model's response content that this grounding support pertains to.

## Public constructors

### GroundingSupport

```
public GroundingSupport(
    @NonNull Segment segment,
    @NonNull List<@NonNull Integer> groundingChunkIndices
)
```