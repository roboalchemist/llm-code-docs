# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GroundingMetadata/GroundingSupport.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/GroundingSupport.md.txt

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

|                                                                                                                                                                          ### Public fields                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html)`>` | [groundingChunkIndices](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingSupport#groundingChunkIndices()) A list of indices that refer to specific [GroundingChunk](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingChunk) classes within the [GroundingMetadata.groundingChunks](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingMetadata#groundingChunks()) array. |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Segment](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Segment)                                                                                                                                                              | [segment](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingSupport#segment()) Specifies the segment of the model's response content that this grounding support pertains to.                                                                                                                                                                                                                                                                         |

|                                                                                                                                                                                                                                                                                                                                                                                           ### Public constructors                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GroundingSupport](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingSupport#GroundingSupport(com.google.firebase.ai.type.Segment,kotlin.collections.List))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Segment](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Segment)` segment,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[List](https://developer.android.com/reference/kotlin/java/util/List.html)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Integer](https://developer.android.com/reference/kotlin/java/lang/Integer.html)`> groundingChunkIndices` `)` |

## Public fields

### groundingChunkIndices

```
publicÂ finalÂ @NonNull List<@NonNull Integer>Â groundingChunkIndices
```

A list of indices that refer to specific [GroundingChunk](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingChunk) classes within the [GroundingMetadata.groundingChunks](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/GroundingMetadata#groundingChunks()) array. These referenced chunks are the sources that support the claim made in the associated `segment` of the response. For example, an array `[1, 3, 4]` means that `groundingChunks[1]`, `groundingChunks[3]`, `groundingChunks[4]` are the retrieved content supporting this part of the response.  

### segment

```
publicÂ finalÂ @NonNull SegmentÂ segment
```

Specifies the segment of the model's response content that this grounding support pertains to.  

## Public constructors

### GroundingSupport

```
publicÂ GroundingSupport(
Â Â Â Â @NonNull SegmentÂ segment,
Â Â Â Â @NonNull List<@NonNull Integer>Â groundingChunkIndices
)
```