# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Result.md.txt

# Transaction.Result

# Transaction.Result


```
public class Transaction.Result
```

<br />

*** ** * ** ***

Instances of this class represent the desired outcome of a single run of a `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Handler`'s doTransaction method. The options are:

- Set the data to the new value (success)
- abort the transaction

Instances are created using `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction#success(com.google.firebase.database.MutableData)` or `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction#abort()`.

## Summary

| ### Public methods |
|---|---|
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Result#isSuccess()()` |

## Public methods

### isSuccess

```
public boolean isSuccess()
```

| Returns |
|---|---|
| `boolean` | Whether or not this result is a success |