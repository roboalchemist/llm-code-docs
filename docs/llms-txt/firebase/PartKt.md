# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PartKt.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PartKt.md.txt

# PartKt

# PartKt


```
public final class PartKt
```

<br />

*** ** * ** ***

## Summary

|                                                          ### Public methods                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static final `[FileDataPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart)     | [PartKt](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PartKt)`.`[asFileDataOrNull](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PartKt#(com.google.firebase.vertexai.type.Part).asFileDataOrNull())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part)` receiver)` Returns the part as a [FileDataPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart) if it represents a file, and null otherwise                      |
| `static final `[Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html)                                 | [PartKt](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PartKt)`.`[asImageOrNull](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PartKt#(com.google.firebase.vertexai.type.Part).asImageOrNull())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part)` receiver)` Returns the part as a [Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html) if it represents an image, and null otherwise                                                      |
| `static final `[InlineDataPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InlineDataPart) | [PartKt](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PartKt)`.`[asInlineDataPartOrNull](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PartKt#(com.google.firebase.vertexai.type.Part).asInlineDataPartOrNull())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part)` receiver)` Returns the part as a [InlineDataPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InlineDataPart) if it represents inline data, and null otherwise |
| `static final `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                        | [PartKt](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PartKt)`.`[asTextOrNull](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/PartKt#(com.google.firebase.vertexai.type.Part).asTextOrNull())`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[Part](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/Part)` receiver)` Returns the part as a [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) if it represents text, and null otherwise                                                                 |

## Public methods

### PartKt.asFileDataOrNull

```
publicÂ staticÂ finalÂ FileDataPartÂ PartKt.asFileDataOrNull(@NonNull PartÂ receiver)
```

Returns the part as a [FileDataPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FileDataPart) if it represents a file, and null otherwise  

### PartKt.asImageOrNull

```
publicÂ staticÂ finalÂ BitmapÂ PartKt.asImageOrNull(@NonNull PartÂ receiver)
```

Returns the part as a [Bitmap](https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html) if it represents an image, and null otherwise  

### PartKt.asInlineDataPartOrNull

```
publicÂ staticÂ finalÂ InlineDataPartÂ PartKt.asInlineDataPartOrNull(@NonNull PartÂ receiver)
```

Returns the part as a [InlineDataPart](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/InlineDataPart) if it represents inline data, and null otherwise  

### PartKt.asTextOrNull

```
publicÂ staticÂ finalÂ StringÂ PartKt.asTextOrNull(@NonNull PartÂ receiver)
```

Returns the part as a [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) if it represents text, and null otherwise