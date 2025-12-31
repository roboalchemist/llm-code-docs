# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/type/ExecutableCodePart.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ExecutableCodePart.md.txt

# ExecutableCodePart


```
public final class ExecutableCodePart implements Part
```

<br />

*** ** * ** ***

Represents the code that was executed by the model.

## Summary

|                                                                                  ### Public fields                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | [code](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ExecutableCodePart#code()) The source code to be executed.                        |
| `boolean`                                                                                                                                                                            | [isThought](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ExecutableCodePart#isThought()) Indicates whether the response is a thought. |
| `final @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html) | [language](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ExecutableCodePart#language()) The programming language of the code.          |

|                                                                                                                                                                                                                                                                                                ### Public constructors                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ~~[ExecutableCodePart](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ExecutableCodePart#ExecutableCodePart(kotlin.String,kotlin.String))~~`(@`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` language, @`[NonNull](https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html)` `[String](https://developer.android.com/reference/kotlin/java/lang/String.html)` code)` **This method is deprecated.** Part of the model response. |

## Public fields

### code

```
publicÂ finalÂ @NonNull StringÂ code
```

The source code to be executed.  

### isThought

```
publicÂ booleanÂ isThought
```

Indicates whether the response is a thought.  

### language

```
publicÂ finalÂ @NonNull StringÂ language
```

The programming language of the code.  

## Public constructors

### ExecutableCodePart

```
publicÂ [ExecutableCodePart](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/type/ExecutableCodePart#ExecutableCodePart(kotlin.String,kotlin.String))(@NonNull StringÂ language,Â @NonNull StringÂ code)
```
| **This method is deprecated.**   
| Part of the model response. Do not instantiate directly.