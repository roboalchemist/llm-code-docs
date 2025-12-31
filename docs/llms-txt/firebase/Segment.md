# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Segment.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/Segment.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Segment.md.txt

# Segment

# Segment


```
public final class Segment
```

<br />

*** ** * ** ***

Represents a specific segment within a [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content) object, often used to pinpoint the exact location of text or data that grounding information refers to.

## Summary

|                                                                                  ### Public fields                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final int`                                                                                                                                                                          | [endIndex](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Segment#endIndex()) The zero-based end index of the segment within the specified [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part), measured in UTF-8 bytes.                                                                                                |
| `final int`                                                                                                                                                                          | [partIndex](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Segment#partIndex()) The zero-based index of the [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part) object within the `parts` array of its parent [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content) object. |
| `final int`                                                                                                                                                                          | [startIndex](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Segment#startIndex()) The zero-based start index of the segment within the specified [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part), measured in UTF-8 bytes.                                                                                          |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | [text](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Segment#text()) The text corresponding to the segment from the response.                                                                                                                                                                                                                                  |

|                                                                                                                                                                                    ### Public constructors                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Segment](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Segment#Segment(kotlin.Int,kotlin.Int,kotlin.Int,kotlin.String))`(int startIndex, int endIndex, int partIndex, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` text)` |

## Public fields

### endIndex

```
publicÂ finalÂ intÂ endIndex
```

The zero-based end index of the segment within the specified [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part), measured in UTF-8 bytes. This offset is exclusive, meaning the character at this index is not included in the segment.  

### partIndex

```
publicÂ finalÂ intÂ partIndex
```

The zero-based index of the [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part) object within the `parts` array of its parent [Content](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content) object. This identifies which part of the content the segment belongs to.  

### startIndex

```
publicÂ finalÂ intÂ startIndex
```

The zero-based start index of the segment within the specified [Part](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part), measured in UTF-8 bytes. This offset is inclusive, starting from 0 at the beginning of the part's content.  

### text

```
publicÂ finalÂ @NonNull StringÂ text
```

The text corresponding to the segment from the response.  

## Public constructors

### Segment

```
publicÂ Segment(intÂ startIndex,Â intÂ endIndex,Â intÂ partIndex,Â @NonNull StringÂ text)
```