# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/ktx/package-summary.md.txt

# com.google.firebase.ml.modeldownloader.ktx

# com.google.firebase.ml.modeldownloader.ktx

## Top-level functions summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions` | `[customModelDownloadConditions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/ktx/package-summary#customModelDownloadConditions(kotlin.Function1))(init: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions.Builder.() -> https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)` **This function is deprecated.** Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration. |

## Extension functions summary

|---|---|
| `operator https://developer.android.com/reference/kotlin/java/io/File.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/ktx/package-summary#(com.google.firebase.ml.modeldownloader.CustomModel).component1()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/ktx/package-summary#(com.google.firebase.ml.modeldownloader.CustomModel).component2()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/ktx/package-summary#(com.google.firebase.ml.modeldownloader.CustomModel).component3()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/ktx/package-summary#(com.google.firebase.ml.modeldownloader.CustomModel).component4()()` |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/ktx/package-summary#(com.google.firebase.ml.modeldownloader.CustomModel).component5()()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/ktx/package-summary#(com.google.firebase.ktx.Firebase).modelDownloader(com.google.firebase.FirebaseApp)(app: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp)` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Extension properties summary

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ktx/Firebase.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/ktx/package-summary#(com.google.firebase.ktx.Firebase).modelDownloader()` Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration). |

## Top-level functions

### customModelDownloadConditions

```
fun [customModelDownloadConditions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/ktx/package-summary#customModelDownloadConditions(kotlin.Function1))(init: CustomModelDownloadConditions.Builder.() -> Unit): CustomModelDownloadConditions
```

> [!CAUTION]
> **This function is deprecated.**   
> Migrate to use the KTX API from the main module: https://firebase.google.com/docs/android/kotlin-migration.

Returns a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModelDownloadConditions` initialized using the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/ktx/package-summary#customModelDownloadConditions(kotlin.Function1)` function.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

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

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` instance of a given `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)

## Extension properties

### modelDownloader

```
val Firebase.modelDownloader: FirebaseModelDownloader
```

Accessing this object for Kotlin apps has changed; see the [migration guide](https://firebase.google.com/docs/android/kotlin-migration).

Returns the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/FirebaseModelDownloader` instance of the default `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseApp`.

**Important** In July 2025, we stopped releasing KTX modules and removed the KTX libraries from the Firebase Android BoM (v34.0.0). **If you use KTX APIs from the KTX modules, we recommend that you migrate your app to use KTX APIs from the main modules instead** . For details, see the [FAQ about this initiative.](https://firebase.google.com/docs/android/kotlin-migration)