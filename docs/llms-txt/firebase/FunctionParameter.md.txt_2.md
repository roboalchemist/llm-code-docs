# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionParameter.md.txt

# FunctionParameter

# FunctionParameter


```
class FunctionParameter<T : Any?>
```

<br />

*** ** * ** ***

## Summary

| ### Public constructors |
|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionParameter#FunctionParameter(kotlin.String,kotlin.String,com.google.firebase.vertexai.type.FunctionType)( name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, description: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, type: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType<T> )` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionParameter#description()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionParameter#name()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType<T>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionParameter#type()` |

## Public constructors

### FunctionParameter

```
<T : Any?> FunctionParameter(
    name: String,
    description: String,
    type: FunctionType<T>
)
```

## Public properties

### description

```
val description: String
```

### name

```
val name: String
```

### type

```
val type: FunctionType<T>
```