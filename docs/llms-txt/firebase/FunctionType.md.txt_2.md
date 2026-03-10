# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType.md.txt

# FunctionType

# FunctionType


```
class FunctionType<T : Any?>
```

<br />

*** ** * ** ***

Represents and passes the type information for an automated function call.

## Summary

| ### Public companion properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType.Companion#ARRAY()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType.Companion#BOOLEAN()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType.Companion#INTEGER()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType.Companion#LONG()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType.Companion#NUMBER()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType<https://developer.android.com/reference/kotlin/org/json/JSONObject.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType.Companion#OBJECT()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html>` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType.Companion#STRING()` |

| ### Public constructors |
|---|
| `<T : https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html?> https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType#FunctionType(kotlin.String,kotlin.Function1)(name: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html, parse: (https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?) -> T?)` |

| ### Public properties |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType#name()` : the enum name of the type |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?) -> T?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/vertexai/type/FunctionType#parse()` : the deserialization function |

## Public companion properties

### ARRAY

```
val ARRAY: FunctionType<List<String>>
```

### BOOLEAN

```
val BOOLEAN: FunctionType<Boolean>
```

### INTEGER

```
val INTEGER: FunctionType<Int>
```

### LONG

```
val LONG: FunctionType<Long>
```

### NUMBER

```
val NUMBER: FunctionType<Double>
```

### OBJECT

```
val OBJECT: FunctionType<JSONObject>
```

### STRING

```
val STRING: FunctionType<String>
```

## Public constructors

### FunctionType

```
<T : Any?> FunctionType(name: String, parse: (String?) -> T?)
```

## Public properties

### name

```
val name: String
```

: the enum name of the type

### parse

```
val parse: (String?) -> T?
```

: the deserialization function