# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType.md.txt

# DownloadType

# DownloadType


```
public enum DownloadType
```

<br />

*** ** * ** ***

## Summary

| ### Enum Values |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType#LATEST_MODEL` | Always return latest model, check for latest model and download new model (when needed) before returning. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType#LOCAL_MODEL` | Use local model when present, otherwise download and return latest model |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType#LOCAL_MODEL_UPDATE_IN_BACKGROUND` | When local model present, use local model and download latest model in background. |

| ### Public methods |
|---|---|
| `static https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType#valueOf(java.lang.String)(https://developer.android.com/reference/kotlin/java/lang/String.html name)` Returns the enum constant of this type with the specified name. |
| `static DownloadType[]` | `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType#values()()` Returns an array containing the constants of this enum type, in the order they're declared. |

## Enum Values

### LATEST_MODEL

```
DownloadType DownloadType.LATEST_MODEL
```

Always return latest model, check for latest model and download new model (when needed) before returning.

### LOCAL_MODEL

```
DownloadType DownloadType.LOCAL_MODEL
```

Use local model when present, otherwise download and return latest model

### LOCAL_MODEL_UPDATE_IN_BACKGROUND

```
DownloadType DownloadType.LOCAL_MODEL_UPDATE_IN_BACKGROUND
```

When local model present, use local model and download latest model in background. Otherwise, download and return latest model.

## Public methods

### valueOf

```
public static DownloadType valueOf(String name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType` | the enum constant with the specified name |

| Throws |
|---|---|
| `https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
public static DownloadType[] values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.

| Returns |
|---|---|
| `DownloadType[]` | an array containing the constants of this enum type, in the order they're declared |