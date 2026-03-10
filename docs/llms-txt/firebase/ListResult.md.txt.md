# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult.md.txt

# ListResult

# ListResult


```
public final class ListResult
```

<br />

*** ** * ** ***

Contains the prefixes and items returned by a `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference#list(int)` call.

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult#items()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult#pageToken()` |
| `final https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult#prefixes()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult#getItems()()` The items (files) returned by the `list()` operation. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult#getPageToken()()` Returns a token that can be used to resume a previous `list()` operation. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult#getPrefixes()()` The prefixes (folders) returned by the `list()` operation. |

| ### Extension functions |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult#(com.google.firebase.storage.ListResult).component1()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` to provide its items. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult#(com.google.firebase.storage.ListResult).component2()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` to provide its prefixes. |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageKt.https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult#(com.google.firebase.storage.ListResult).component3()(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult receiver)` Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` to provide its pageToken. |

## Public fields

### items

```
public final List<StorageReference> items
```

### pageToken

```
public final @Nullable String pageToken
```

### prefixes

```
public final List<StorageReference> prefixes
```

## Public methods

### getItems

```
public @NonNull List<StorageReference> getItems()
```

The items (files) returned by the `list()` operation.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | A list of items (files). |

### getPageToken

```
public @Nullable String getPageToken()
```

Returns a token that can be used to resume a previous `list()` operation. `null` indicates that there are no more results.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | A page token if more results are available. |

### getPrefixes

```
public @NonNull List<StorageReference> getPrefixes()
```

The prefixes (folders) returned by the `list()` operation.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | A list of prefixes (folders). |

## Extension functions

### StorageKt.component1

```
public final @NonNull List<@NonNull StorageReference> StorageKt.component1(@NonNull ListResult receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` to provide its items.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | the items of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` |

### StorageKt.component2

```
public final @NonNull List<@NonNull StorageReference> StorageKt.component2(@NonNull ListResult receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` to provide its prefixes.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/util/List.html<@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/storage/StorageReference>` | the prefixes of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` |

### StorageKt.component3

```
public final String StorageKt.component3(@NonNull ListResult receiver)
```

Destructuring declaration for `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` to provide its pageToken.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | the pageToken of the `https://firebase.google.com/docs/reference/android/com/google/firebase/storage/ListResult` |