# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.md.txt

# CustomModel

# CustomModel


```
class CustomModel
```

<br />

*** ** * ** ***

Stores information about custom models that are being downloaded or are already downloaded on a device. In the case where an update is available, after the updated model file is fully downloaded, the original model file will be removed once it is safe to do so.

## Summary

| ### Public functions |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#equals(java.lang.Object)(o: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html!)` |
| `https://developer.android.com/reference/kotlin/java/io/File.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#getFile()()` The local model file. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#getSize()()` The size of the file currently associated with this model. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#hashCode()()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#toString()()` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#downloadId()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#downloadUrl()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#downloadUrlExpiry()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#localFilePath()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#modelHash()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#name()` |

| ### Extension functions |
|---|---|
| `operator https://developer.android.com/reference/kotlin/java/io/File.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#(com.google.firebase.ml.modeldownloader.CustomModel).component1()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#(com.google.firebase.ml.modeldownloader.CustomModel).component2()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#(com.google.firebase.ml.modeldownloader.CustomModel).component3()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#(com.google.firebase.ml.modeldownloader.CustomModel).component4()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel#(com.google.firebase.ml.modeldownloader.CustomModel).component5()()` |

## Public functions

### equals

```
fun equals(o: Any!): Boolean
```

### getFile

```
fun getFile(): File?
```

The local model file. If `null` is returned, use the download ID to check the download status.

| Returns |
|---|---|
| `https://developer.android.com/reference/kotlin/java/io/File.html?` | The local file associated with the model. If the original file download is still in progress, returns `null`. If a file update is in progress, returns the last fully downloaded model. |

### getSize

```
fun getSize(): Long
```

The size of the file currently associated with this model. If a download is in progress, this will be the size of the current model, not the new model currently being downloaded.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | The local model size. |

### hashCode

```
fun hashCode(): Int
```

### toString

```
fun toString(): String
```

## Public properties

### downloadId

```
val downloadId: Long
```

### downloadUrl

```
val downloadUrl: String!
```

### downloadUrlExpiry

```
val downloadUrlExpiry: Long
```

### localFilePath

```
val localFilePath: String!
```

### modelHash

```
val modelHash: String!
```

### name

```
val name: String!
```

## Extension functions

### component1

```
operator fun CustomModel.component1(): File?
```

### component2

```
operator fun CustomModel.component2(): Long
```

### component3

```
operator fun CustomModel.component3(): Long
```

### component4

```
operator fun CustomModel.component4(): String
```

### component5

```
operator fun CustomModel.component5(): String
```