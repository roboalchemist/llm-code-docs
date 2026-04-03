# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/AddTrace.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/AddTrace.md.txt

# AddTrace

# AddTrace


```
@Retention(valueÂ =Â RetentionPolicy.CLASS)
annotation AddTrace
```

<br />

*** ** * ** ***

An annotation when applied to a method will create a [Trace](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace) object with given name and insert [start](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#start()) at the start of the method and [stop](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/Trace#stop()) at the end.

## Summary

|                                      ### Public functions                                      |
|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| `abstract `[Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)  | [enabled](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/AddTrace#enabled())`()` |
| `abstract `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [name](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/perf/metrics/AddTrace#name())`()`       |

## Public functions

### enabled

```
abstractÂ funÂ enabled():Â Boolean
```  

### name

```
abstractÂ funÂ name():Â String!
```