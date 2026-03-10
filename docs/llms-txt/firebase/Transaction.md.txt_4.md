# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.md.txt

# Transaction

# Transaction


```
class Transaction
```

<br />

*** ** * ** ***

The Transaction class encapsulates the functionality needed to perform a transaction on the data at a location. To run a transaction, provide a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler` to `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/DatabaseReference#runTransaction(com.google.firebase.database.Transaction.Handler)`. That handler will be passed the current data at the location, and must return a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result`. A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result` can be created using either `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction#success(com.google.firebase.database.MutableData)` or `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction#abort()`.

## Summary

| ### Nested types |
|---|
| `interface https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler` An object implementing this interface is used to run a transaction, and will be notified of the results of the transaction. |
| `class https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result` Instances of this class represent the desired outcome of a single run of a `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler`'s doTransaction method. |

| ### Public constructors |
|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction#Transaction()()` |

| ### Public functions |
|---|---|
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction#abort()()` |
| `java-static https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction#success(com.google.firebase.database.MutableData)(resultData: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData)` |

## Public constructors

### Transaction

```
Transaction()
```

## Public functions

### abort

```
java-static fun abort(): Transaction.Result
```

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result` that aborts the transaction |

### success

```
java-static fun success(resultData: MutableData): Transaction.Result
```

| Parameters |
|---|---|
| `resultData: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/MutableData` | The desired data at the location |

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result` | A `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result` indicating the new data to be stored at the location |