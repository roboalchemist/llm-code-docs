# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType.md.txt

# FunctionType

# FunctionType


```
public final class FunctionType<TÂ extendsÂ Object>
```

<br />

*** ** * ** ***

Represents and passes the type information for an automated function call.

## Summary

|                                                                      ### Nested types                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `public static class `[FunctionType.Companion](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType.Companion) |

|                                                                                          ### Public fields                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)                 | [name](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType#name()) : the enum name of the type      |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<`[String](https://developer.android.com/reference/kotlin/java/lang/String.html)`, T>` | [parse](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType#parse()) : the deserialization function |

|                                                                                                                                                                                                                                                                                                                      ### Public constructors                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<T extends `[Object](https://developer.android.com/reference/kotlin/java/lang/Object.html)`> `[FunctionType](https://firebase.google.com/docs/reference/android/com/google/firebase/vertexai/type/FunctionType#FunctionType(kotlin.String,kotlin.Function1))`(` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` name,` ` @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` Function1<`[String](https://developer.android.com/reference/kotlin/java/lang/String.html)`, T> parse` `)` |

## Public fields

### name

```
publicÂ finalÂ @NonNull StringÂ name
```

: the enum name of the type  

### parse

```
publicÂ finalÂ @NonNull Function1<String,Â T>Â parse
```

: the deserialization function  

## Public constructors

### FunctionType

```
publicÂ <TÂ extendsÂ Object> FunctionType(
Â Â Â Â @NonNull StringÂ name,
Â Â Â Â @NonNull Function1<String,Â T>Â parse
)
```