# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/package-summary.md.txt

# com.google.firebase.ml.modeldownloader

# com.google.firebase.ml.modeldownloader

## Classes

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel` | Stores information about custom models that are being downloaded or are already downloaded on a device. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions` | Conditions to allow download of custom models. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder` | Builder of `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions`. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` |   |

## Exceptions

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException` | Represents an Exception resulting from an operation on a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader`. |

## Annotations

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseMlException.Code` | The set of Firebase ML status codes. |

## Enums

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType` |   |

## Top-level functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/package-summary#customModelDownloadConditions(kotlin.Function1)(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions` initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/package-summary#customModelDownloadConditions(kotlin.Function1)` function. |

## Extension functions summary

|---|---|
| `operator https://developer.android.com/reference/kotlin/java/io/File.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/package-summary#(com.google.firebase.ml.modeldownloader.CustomModel).component1()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/package-summary#(com.google.firebase.ml.modeldownloader.CustomModel).component2()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/package-summary#(com.google.firebase.ml.modeldownloader.CustomModel).component3()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/package-summary#(com.google.firebase.ml.modeldownloader.CustomModel).component4()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/package-summary#(com.google.firebase.ml.modeldownloader.CustomModel).component5()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/package-summary#(com.google.firebase.Firebase).modelDownloader(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/package-summary#(com.google.firebase.Firebase).modelDownloader()` Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`. |

## Top-level functions

### customModelDownloadConditions

```
fun customModelDownloadConditions(init: CustomModelDownloadConditions.Builder.() -> Unit): CustomModelDownloadConditions
```

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions` initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/package-summary#customModelDownloadConditions(kotlin.Function1)` function.

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

### modelDownloader

```
fun Firebase.modelDownloader(app: FirebaseApp): FirebaseModelDownloader
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

## Extension properties

### modelDownloader

```
val Firebase.modelDownloader: FirebaseModelDownloader
```

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.