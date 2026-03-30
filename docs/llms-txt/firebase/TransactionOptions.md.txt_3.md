# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions.md.txt

# TransactionOptions

# TransactionOptions


```
public final class TransactionOptions
```

<br />

*** ** * ** ***

Options to customize transaction behavior for `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/FirebaseFirestore#runTransaction(com.google.firebase.firestore.TransactionOptions,com.google.firebase.firestore.Transaction.Function<TResult>)`.

## Summary

| ### Nested types |
|---|
| `public final class https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions.Builder` A Builder for creating `TransactionOptions`. |

| ### Public fields |
|---|---|
| `final int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions#maxAttempts()` |

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions#equals(java.lang.Object)(https://developer.android.com/reference/kotlin/java/lang/Object.html o)` |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions#getMaxAttempts()()` Get maximum number of attempts to commit, after which transaction fails. |
| `int` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions#hashCode()()` |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/TransactionOptions#toString()()` |

## Public fields

### maxAttempts

```
public final int maxAttempts
```

## Public methods

### equals

```
public boolean equals(Object o)
```

### getMaxAttempts

```
public int getMaxAttempts()
```

Get maximum number of attempts to commit, after which transaction fails. Default is 5.

| Returns |
|---|---|
| `int` | The maximum number of attempts |

### hashCode

```
public int hashCode()
```

### toString

```
public String toString()
```