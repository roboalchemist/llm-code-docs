# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Transaction.Function.md.txt

# Transaction.Function

# Transaction.Function


```
public interface Transaction.Function<TResult>
```

<br />

*** ** * ** ***

An interface for providing code to be executed within a transaction context.

| See also |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#runTransaction(com.google.firebase.firestore.Transaction.Function<TResult>)` |   |

## Summary

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html TResult` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Transaction.Function#apply(com.google.firebase.firestore.Transaction)(@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Transaction transaction)` |

## Public methods

### apply

```
abstract @Nullable TResult apply(@NonNull Transaction transaction)
```

| Throws |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestoreException com.google.firebase.firestore.FirebaseFirestoreException` |   |