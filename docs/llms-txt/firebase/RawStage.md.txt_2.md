# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage.md.txt

# RawStage

# RawStage


```
@Beta
class RawStage : Stage
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage) ||
|   | ↳ | [com.google.firebase.firestore.pipeline.RawStage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage) |

*** ** * ** ***

Adds a stage to the pipeline by specifying the stage name as an argument. This does not offer any type safety on the stage params and requires the caller to know the order (and optionally names) of parameters accepted by the stage.

This class provides a way to call stages that are supported by the Firestore backend but that are not implemented in the SDK version being used.

## Summary

| ### Public companion functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage.Companion#ofName(kotlin.String)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Specify name of stage |

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage#withArguments(kotlin.Array)(vararg arguments: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)` Specify arguments to stage. |

| ### Inherited functions |
|---|
| From [com.google.firebase.firestore.pipeline.Stage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,[Error type: Unresolved type for Value])(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/[JVM root]/<Error class: unknown class>)` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Boolean)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Double)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,com.google.firebase.firestore.pipeline.Field)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field)` Specify named `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Field` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.Long)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` parameter | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/Stage#withOption(kotlin.String,kotlin.String)(key: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, value: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)` Specify named `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` parameter | |

## Public companion functions

### ofName

```
fun ofName(name: String): RawStage
```

Specify name of stage

| Parameters |
|---|---|
| `name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | The unique name of the stage to add. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` | A new `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` for the specified stage name. |

## Public functions

### withArguments

```
fun withArguments(vararg arguments: Any): RawStage
```

Specify arguments to stage.

| Parameters |
|---|---|
| `vararg arguments: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html` | A list of ordered parameters to configure the stage's behavior. |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/pipeline/RawStage` with specified parameters. |