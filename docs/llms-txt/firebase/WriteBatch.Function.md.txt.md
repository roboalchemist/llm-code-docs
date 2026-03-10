# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch.Function.md.txt

# WriteBatch.Function

# WriteBatch.Function


```
public interface WriteBatch.Function
```

<br />

*** ** * ** ***

An interface for providing code to be executed within a `WriteBatch` context.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#runBatch(com.google.firebase.firestore.WriteBatch.Function)` |   |

## Summary

| ### Public methods |
|---|---|
| `abstract void` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch.Function#apply(com.google.firebase.firestore.WriteBatch)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/WriteBatch batch)` |

## Public methods

### apply

```
abstract void apply(@NonNull WriteBatch batch)
```