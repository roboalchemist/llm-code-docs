# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType.md.txt

# DownloadType

# DownloadType


```
enum DownloadType
```

<br />

*** ** * ** ***

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType#LATEST_MODEL` | Always return latest model, check for latest model and download new model (when needed) before returning. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType#LOCAL_MODEL` | Use local model when present, otherwise download and return latest model |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType#LOCAL_MODEL_UPDATE_IN_BACKGROUND` | When local model present, use local model and download latest model in background. |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType#valueOf(java.lang.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!)` Returns the enum constant of this type with the specified name. |
| `java-static https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType!>!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### LATEST_MODEL

```
val DownloadType.LATEST_MODEL: DownloadType
```

Always return latest model, check for latest model and download new model (when needed) before returning.

### LOCAL_MODEL

```
val DownloadType.LOCAL_MODEL: DownloadType
```

Use local model when present, otherwise download and return latest model

### LOCAL_MODEL_UPDATE_IN_BACKGROUND

```
val DownloadType.LOCAL_MODEL_UPDATE_IN_BACKGROUND: DownloadType
```

When local model present, use local model and download latest model in background. Otherwise, download and return latest model.

## Public functions

### valueOf

```
java-static fun valueOf(name: String!): DownloadType!
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType!` | the enum constant with the specified name |

| Throws |
|---|---|
| `java.lang.IllegalArgumentException: https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html` | if this enum type has no constant with the specified name |

### values

```
java-static fun values(): Array<DownloadType!>!
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-array/index.html<https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType!>!` | an array containing the constants of this enum type, in the order they're declared |