# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PartKt.md.txt

# PartKt

# PartKt


```
public final class PartKt
```

<br />

*** ** * ** ***

## Summary

| ### Public methods |
|---|---|
| `static final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FileDataPart` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PartKt.https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PartKt#(com.google.firebase.ai.type.Part).asFileDataOrNull()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part receiver)` Returns the part as a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FileDataPart` if it represents a file, and null otherwise |
| `static final https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PartKt.https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PartKt#(com.google.firebase.ai.type.Part).asImageOrNull()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part receiver)` Returns the part as a `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` if it represents an image, and null otherwise |
| `static final https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineDataPart` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PartKt.https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PartKt#(com.google.firebase.ai.type.Part).asInlineDataPartOrNull()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part receiver)` Returns the part as a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineDataPart` if it represents inline data, and null otherwise |
| `static final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PartKt.https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/PartKt#(com.google.firebase.ai.type.Part).asTextOrNull()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part receiver)` Returns the part as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` if it represents text, and null otherwise |

## Public methods

### PartKt.asFileDataOrNull

```
public static final FileDataPart PartKt.asFileDataOrNull(@NonNull Part receiver)
```

Returns the part as a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/FileDataPart` if it represents a file, and null otherwise

### PartKt.asImageOrNull

```
public static final Bitmap PartKt.asImageOrNull(@NonNull Part receiver)
```

Returns the part as a `https://developer.android.com/reference/kotlin/android/graphics/Bitmap.html` if it represents an image, and null otherwise

### PartKt.asInlineDataPartOrNull

```
public static final InlineDataPart PartKt.asInlineDataPartOrNull(@NonNull Part receiver)
```

Returns the part as a `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/InlineDataPart` if it represents inline data, and null otherwise

### PartKt.asTextOrNull

```
public static final String PartKt.asTextOrNull(@NonNull Part receiver)
```

Returns the part as a `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` if it represents text, and null otherwise