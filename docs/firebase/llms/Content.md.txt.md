# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content.md.txt

# Content

# Content


```
public final class Content
```

<br />

*** ** * ** ***

Represents content sent to and received from the model.

`Content` is composed of a one or more heterogeneous parts that can be represent data in different formats, like text or images.

## Summary

| ### Nested types |
|---|
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content.Builder` Builder class to facilitate constructing complex `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` objects. |

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content#parts()` An ordered list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part` that constitute this content. |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content#role()` The producer of the content. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content#Content(kotlin.String,kotlin.collections.List)(https://developer.android.com/reference/kotlin/java/lang/String.html role, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part> parts)` |

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Content#copy(kotlin.String,kotlin.collections.List)(https://developer.android.com/reference/kotlin/java/lang/String.html role, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part> parts)` Returns a copy of this object, with the provided parameters overwriting the originals. |

## Public fields

### parts

```
public final @NonNull List<@NonNull Part> parts
```

An ordered list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part` that constitute this content.

### role

```
public final String role
```

The producer of the content. Must be either `"user"` or `"model"`. By default, it's `"user"`.

## Public constructors

### Content

```
public Content(String role, @NonNull List<@NonNull Part> parts)
```

| Parameters |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html role` | The producer of the content. Must be either `"user"` or `"model"`. By default, it's `"user"`. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part> parts` | An ordered list of `https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/Part` that constitute this content. |

## Public methods

### copy

```
public final @NonNull Content copy(String role, @NonNull List<@NonNull Part> parts)
```

Returns a copy of this object, with the provided parameters overwriting the originals.