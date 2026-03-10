# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.md.txt

# UnnestStage

# UnnestStage


```
@Beta
public final class UnnestStage extends Stage
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.UnnestStage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage) |

*** ** * ** ***

Takes a specified array from the input documents and outputs a document for each element with the element stored in a field with name specified by the alias.

## Summary

| ### Nested types |
|---|
| `public static class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage#equals(kotlin.Any)(https://developer.android.com/reference/kotlin/java/lang/Object.html other)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage#hashCode()()` |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(com.google.firebase.firestore.pipeline.Selectable)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Selectable arrayWithAlias)` Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified. |
| `static final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html arrayField, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html alias)` Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage#withIndexField(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html indexField)` Adds an index field to the output documents. |

| ### Inherited methods |
|---|
| From [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage) |---|---| | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,[Error type: Unresolved type for Value])( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/[JVM root]/<Error class: unknown class> value )` | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Boolean)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, boolean value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Double)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, double value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,com.google.firebase.firestore.pipeline.Field)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field value)` Specify named `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Long)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, long value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` parameter | | `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html key, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html value)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` parameter | |

## Public methods

### equals

```
public boolean equals(Object other)
```

### hashCode

```
public int hashCode()
```

### withField

```
public static final @NonNull UnnestStage withField(@NonNull Selectable arrayWithAlias)
```

Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified.

For each document emitted by the prior stage, this stage will emit zero or more augmented documents. The input array is found in parameter `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(com.google.firebase.firestore.pipeline.Selectable)`, which can be an `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression` with an alias specified via `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Expression#alias(kotlin.String)`, or a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` that can also have alias specified. For each element of the input array, an augmented document will be produced. The element of input array will be stored in a field with name specified by the alias of the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(com.google.firebase.firestore.pipeline.Selectable)` parameter. If the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(com.google.firebase.firestore.pipeline.Selectable)` is a `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Field` with no alias, then the original array field will be replaced with the individual element.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/Selectable arrayWithAlias` | The input array with field alias to store output element of array. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified. |

### withField

```
public static final @NonNull UnnestStage withField(@NonNull String arrayField, @NonNull String alias)
```

Creates `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified.

For each document emitted by the prior stage, this stage will emit zero or more augmented documents. The input array found in the previous stage document field specified by the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(kotlin.String,kotlin.String)` parameter, will for each element of the input array produce an augmented document. The element of the input array will be stored in a field with name specified by `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage.Companion#withField(kotlin.String,kotlin.String)` parameter on the augmented document.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` with input array and alias specified. |

### withIndexField

```
public final @NonNull UnnestStage withIndexField(@NonNull String indexField)
```

Adds an index field to the output documents.

A field with the name specified in `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage#withIndexField(kotlin.String)` will be added to each output document. The value of this field is a numeric value that corresponds to the array index of the element from the input array.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html indexField` | The name of the index field. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/UnnestStage` | A new `UnnestStage` that includes the specified index field. |