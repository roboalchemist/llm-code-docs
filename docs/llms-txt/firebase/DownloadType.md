# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/DownloadType.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType.md.txt

# DownloadType

# DownloadType


```
public enum DownloadType
```

<br />

*** ** * ** ***

## Summary

|                                                                               ### Enum Values                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [LATEST_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType#LATEST_MODEL)                                         | Always return latest model, check for latest model and download new model (when needed) before returning. |
| [LOCAL_MODEL](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType#LOCAL_MODEL)                                           | Use local model when present, otherwise download and return latest model                                  |
| [LOCAL_MODEL_UPDATE_IN_BACKGROUND](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType#LOCAL_MODEL_UPDATE_IN_BACKGROUND) | When local model present, use local model and download latest model in background.                        |

|                                                       ### Public methods                                                        |
|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `static `[DownloadType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType) | [valueOf](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType#valueOf(java.lang.String))`(`[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` name)` Returns the enum constant of this type with the specified name. |
| `static DownloadType[]`                                                                                                         | [values](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType#values())`()` Returns an array containing the constants of this enum type, in the order they're declared.                                                                            |

## Enum Values

### LATEST_MODEL

```
DownloadTypeÂ DownloadType.LATEST_MODEL
```

Always return latest model, check for latest model and download new model (when needed) before returning.  

### LOCAL_MODEL

```
DownloadTypeÂ DownloadType.LOCAL_MODEL
```

Use local model when present, otherwise download and return latest model  

### LOCAL_MODEL_UPDATE_IN_BACKGROUND

```
DownloadTypeÂ DownloadType.LOCAL_MODEL_UPDATE_IN_BACKGROUND
```

When local model present, use local model and download latest model in background. Otherwise, download and return latest model.  

## Public methods

### valueOf

```
publicÂ staticÂ DownloadTypeÂ valueOf(StringÂ name)
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)  

|                                                        Returns                                                         |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| [DownloadType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/DownloadType) | the enum constant with the specified name |

|                                                                              Throws                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [java.lang.IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html)` java.lang.IllegalArgumentException` | if this enum type has no constant with the specified name |

### values

```
publicÂ staticÂ DownloadType[]Â values()
```

Returns an array containing the constants of this enum type, in the order they're declared. This method may be used to iterate over the constants.  

|     Returns      |
|------------------|------------------------------------------------------------------------------------|
| `DownloadType[]` | an array containing the constants of this enum type, in the order they're declared |