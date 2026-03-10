# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/AddTrace.md.txt

# AddTrace

# AddTrace


```
@Retention(value = RetentionPolicy.CLASS)
annotation AddTrace
```

<br />

*** ** * ** ***

An annotation when applied to a method will create a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace` object with given name and insert `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#start()` at the start of the method and `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#stop()` at the end.

## Summary

| ### Public functions |
|---|---|
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/AddTrace#enabled()()` |
| `abstract https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/AddTrace#name()()` |

## Public functions

### enabled

```
abstract fun enabled(): Boolean
```

### name

```
abstract fun name(): String!
```