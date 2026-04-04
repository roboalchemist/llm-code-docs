# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/AddTrace.md.txt

# AddTrace

# AddTrace


```
@Retention(value = RetentionPolicy.CLASS)
public annotation AddTrace
```

<br />

*** ** * ** ***

An annotation when applied to a method will create a `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace` object with given name and insert `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#start()` at the start of the method and `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/Trace#stop()` at the end.

## Summary

| ### Public methods |
|---|---|
| `abstract boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/AddTrace#enabled()()` |
| `abstract https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/perf/metrics/AddTrace#name()()` |

## Public methods

### enabled

```
public abstract boolean enabled()
```

### name

```
public abstract String name()
```