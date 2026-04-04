# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource.md.txt

# PipelineSource

# PipelineSource


```
@Beta
public final class PipelineSource
```

<br />

*** ** * ** ***

Start of a Firestore Pipeline

## Summary

| ### Public methods |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#collection(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html path)` Set the pipeline's source to the collection specified by the given path. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#collection(com.google.firebase.firestore.CollectionReference)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference ref)` Set the pipeline's source to the collection specified by the given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#collection(com.google.firebase.firestore.CollectionReference,com.google.firebase.firestore.pipeline.CollectionSourceOptions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference ref, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionSourceOptions options )` Set the pipeline's source to the collection specified by the given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference`. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#collectionGroup(kotlin.String)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html collectionId)` Set the pipeline's source to the collection group with the given id. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#collectionGroup(kotlin.String,com.google.firebase.firestore.pipeline.CollectionGroupOptions)( @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html collectionId, @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionGroupOptions options )` Set the pipeline's source to the collection group with the given id. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#createFrom(com.google.firebase.firestore.AggregateQuery)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery aggregateQuery)` Convert the given Aggregate Query into an equivalent Pipeline. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#createFrom(com.google.firebase.firestore.Query)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query query)` Convert the given Query into an equivalent Pipeline. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#database()()` Set the pipeline's source to be all documents in this database. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#documents(kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documents)` Set the pipeline's source to the documents specified by the given DocumentReferences. |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#documents(kotlin.Array)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html documents)` Set the pipeline's source to the documents specified by the given paths. |

## Public methods

### collection

```
public final @NonNull Pipeline collection(@NonNull String path)
```

Set the pipeline's source to the collection specified by the given path.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html path` | A path to a collection that will be the source of this pipeline. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` object with documents from target collection. |

### collection

```
public final @NonNull Pipeline collection(@NonNull CollectionReference ref)
```

Set the pipeline's source to the collection specified by the given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference ref` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference` for a collection that will be the source of this pipeline. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` object with documents from target collection. |

| Throws |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html kotlin.IllegalArgumentException` | Thrown if the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#collection(com.google.firebase.firestore.CollectionReference)` provided targets a different project or database than the pipeline. |

### collection

```
public final @NonNull Pipeline collection(
    @NonNull CollectionReference ref,
    @NonNull CollectionSourceOptions options
)
```

Set the pipeline's source to the collection specified by the given `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference`.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference ref` | A `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/CollectionReference` for a collection that will be the source of this pipeline. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionSourceOptions options` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionSourceOptions` for the collection. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` object with documents from target collection. |

| Throws |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html kotlin.IllegalArgumentException` | Thrown if the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#collection(com.google.firebase.firestore.CollectionReference,com.google.firebase.firestore.pipeline.CollectionSourceOptions)` provided targets a different project or database than the pipeline. |

### collectionGroup

```
public final @NonNull Pipeline collectionGroup(@NonNull String collectionId)
```

Set the pipeline's source to the collection group with the given id.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html collectionId` | The id of a collection group that will be the source of this pipeline. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` object with documents from target collection group. |

### collectionGroup

```
public final @NonNull Pipeline collectionGroup(
    @NonNull String collectionId,
    @NonNull CollectionGroupOptions options
)
```

Set the pipeline's source to the collection group with the given id.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html collectionId` | The id of a collection group that will be the source of this pipeline. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionGroupOptions options` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/pipeline/CollectionGroupOptions` for the collection group. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` object with documents from target collection group. |

### createFrom

```
public final @NonNull Pipeline createFrom(@NonNull AggregateQuery aggregateQuery)
```

Convert the given Aggregate Query into an equivalent Pipeline.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateQuery aggregateQuery` | An Aggregate Query to be converted into a Pipeline. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` object that is equivalent to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#createFrom(com.google.firebase.firestore.AggregateQuery)` |

| Throws |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html kotlin.IllegalArgumentException` | Thrown if the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#createFrom(com.google.firebase.firestore.AggregateQuery)` provided targets a different project or database than the pipeline. |

### createFrom

```
public final @NonNull Pipeline createFrom(@NonNull Query query)
```

Convert the given Query into an equivalent Pipeline.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Query query` | A Query to be converted into a Pipeline. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` object that is equivalent to `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#createFrom(com.google.firebase.firestore.Query)` |

| Throws |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html kotlin.IllegalArgumentException` | Thrown if the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#createFrom(com.google.firebase.firestore.Query)` provided targets a different project or database than the pipeline. |

### database

```
public final @NonNull Pipeline database()
```

Set the pipeline's source to be all documents in this database.

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` object with all documents in this database. |

### documents

```
public final @NonNull Pipeline documents(@NonNull DocumentReference documents)
```

Set the pipeline's source to the documents specified by the given DocumentReferences.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/DocumentReference documents` | DocumentReferences specifying the individual documents that will be the source of this pipeline. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | Pipeline with `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#documents(kotlin.Array)`. |

| Throws |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html kotlin.IllegalArgumentException` | Thrown if the `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#documents(kotlin.Array)` provided targets a different project or database than the pipeline. |

### documents

```
public final @NonNull Pipeline documents(@NonNull String documents)
```

Set the pipeline's source to the documents specified by the given paths.

| Parameters |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html documents` | Paths specifying the individual documents that will be the source of this pipeline. |

| Returns |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Pipeline` object with `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/PipelineSource#documents(kotlin.Array)`. |