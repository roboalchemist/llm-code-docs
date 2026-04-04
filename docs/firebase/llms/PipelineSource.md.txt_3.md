# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource.md.txt

# PipelineSource

# PipelineSource


```
@Beta
class PipelineSource
```

<br />

*** ** * ** ***

Start of a Firestore Pipeline

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#collection(kotlin.String)(path: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Set the pipeline's source to the collection specified by the given path. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#collection(com.google.firebase.firestore.CollectionReference)(ref: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference)` Set the pipeline's source to the collection specified by the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#collection(com.google.firebase.firestore.CollectionReference,com.google.firebase.firestore.pipeline.CollectionSourceOptions)(ref: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions)` Set the pipeline's source to the collection specified by the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#collectionGroup(kotlin.String)(collectionId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Set the pipeline's source to the collection group with the given id. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#collectionGroup(kotlin.String,com.google.firebase.firestore.pipeline.CollectionGroupOptions)(collectionId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionGroupOptions)` Set the pipeline's source to the collection group with the given id. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#createFrom(com.google.firebase.firestore.AggregateQuery)(aggregateQuery: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery)` Convert the given Aggregate Query into an equivalent Pipeline. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#createFrom(com.google.firebase.firestore.Query)(query: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query)` Convert the given Query into an equivalent Pipeline. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#database()()` Set the pipeline's source to be all documents in this database. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#documents(kotlin.Array)(vararg documents: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference)` Set the pipeline's source to the documents specified by the given DocumentReferences. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#documents(kotlin.Array)(vararg documents: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Set the pipeline's source to the documents specified by the given paths. |

## Public functions

### collection

```
fun collection(path: String): Pipeline
```

Set the pipeline's source to the collection specified by the given path.

| Parameters |
|---|---|
| `path: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | A path to a collection that will be the source of this pipeline. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with documents from target collection. |

### collection

```
fun collection(ref: CollectionReference): Pipeline
```

Set the pipeline's source to the collection specified by the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference`.

| Parameters |
|---|---|
| `ref: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference` for a collection that will be the source of this pipeline. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with documents from target collection. |

| Throws |
|---|---|
| `kotlin.IllegalArgumentException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html` | Thrown if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#collection(com.google.firebase.firestore.CollectionReference)` provided targets a different project or database than the pipeline. |

### collection

```
fun collection(ref: CollectionReference, options: CollectionSourceOptions): Pipeline
```

Set the pipeline's source to the collection specified by the given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference`.

| Parameters |
|---|---|
| `ref: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/CollectionReference` for a collection that will be the source of this pipeline. |
| `options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionSourceOptions` for the collection. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with documents from target collection. |

| Throws |
|---|---|
| `kotlin.IllegalArgumentException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html` | Thrown if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#collection(com.google.firebase.firestore.CollectionReference,com.google.firebase.firestore.pipeline.CollectionSourceOptions)` provided targets a different project or database than the pipeline. |

### collectionGroup

```
fun collectionGroup(collectionId: String): Pipeline
```

Set the pipeline's source to the collection group with the given id.

| Parameters |
|---|---|
| `collectionId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The id of a collection group that will be the source of this pipeline. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with documents from target collection group. |

### collectionGroup

```
fun collectionGroup(collectionId: String, options: CollectionGroupOptions): Pipeline
```

Set the pipeline's source to the collection group with the given id.

| Parameters |
|---|---|
| `collectionId: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The id of a collection group that will be the source of this pipeline. |
| `options: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionGroupOptions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/CollectionGroupOptions` for the collection group. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with documents from target collection group. |

### createFrom

```
fun createFrom(aggregateQuery: AggregateQuery): Pipeline
```

Convert the given Aggregate Query into an equivalent Pipeline.

| Parameters |
|---|---|
| `aggregateQuery: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateQuery` | An Aggregate Query to be converted into a Pipeline. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object that is equivalent to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#createFrom(com.google.firebase.firestore.AggregateQuery)` |

| Throws |
|---|---|
| `kotlin.IllegalArgumentException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html` | Thrown if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#createFrom(com.google.firebase.firestore.AggregateQuery)` provided targets a different project or database than the pipeline. |

### createFrom

```
fun createFrom(query: Query): Pipeline
```

Convert the given Query into an equivalent Pipeline.

| Parameters |
|---|---|
| `query: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Query` | A Query to be converted into a Pipeline. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object that is equivalent to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#createFrom(com.google.firebase.firestore.Query)` |

| Throws |
|---|---|
| `kotlin.IllegalArgumentException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html` | Thrown if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#createFrom(com.google.firebase.firestore.Query)` provided targets a different project or database than the pipeline. |

### database

```
fun database(): Pipeline
```

Set the pipeline's source to be all documents in this database.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with all documents in this database. |

### documents

```
fun documents(vararg documents: DocumentReference): Pipeline
```

Set the pipeline's source to the documents specified by the given DocumentReferences.

| Parameters |
|---|---|
| `vararg documents: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/DocumentReference` | DocumentReferences specifying the individual documents that will be the source of this pipeline. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | Pipeline with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#documents(kotlin.Array)`. |

| Throws |
|---|---|
| `kotlin.IllegalArgumentException: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-illegal-argument-exception/index.html` | Thrown if the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#documents(kotlin.Array)` provided targets a different project or database than the pipeline. |

### documents

```
fun documents(vararg documents: String): Pipeline
```

Set the pipeline's source to the documents specified by the given paths.

| Parameters |
|---|---|
| `vararg documents: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | Paths specifying the individual documents that will be the source of this pipeline. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Pipeline` object with `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/PipelineSource#documents(kotlin.Array)`. |