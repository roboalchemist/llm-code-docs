# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionParameter.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionParameter.md.txt

# FunctionParameter

# FunctionParameter


```
public final class FunctionParameter<TÂ extendsÂ Object>
```

<br />

*** ** * ** ***

## Summary

|                                                                                                                                                     ### Public fields                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                                                                                                                       | [description](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionParameter#description()) |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                                                                                                                                       | [name](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionParameter#name())               |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionType](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T>` | [type](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionParameter#type())               |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ### Public constructors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FunctionParameter](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionParameter#FunctionParameter(kotlin.String,kotlin.String,com.google.firebase.vertexai.type.FunctionType))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` name,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` description,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[FunctionType](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType)`<@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` T> type` `)` |

## Public fields

### description

```
publicÂ finalÂ @NonNull StringÂ description
```  

### name

```
publicÂ finalÂ @NonNull StringÂ name
```  

### type

```
publicÂ finalÂ @NonNull FunctionType<@NonNull T>Â type
```  

## Public constructors

### FunctionParameter

```
publicÂ <TÂ extendsÂ Object> FunctionParameter(
Â Â Â Â @NonNull StringÂ name,
Â Â Â Â @NonNull StringÂ description,
Â Â Â Â @NonNull FunctionType<@NonNull T>Â type
)
```