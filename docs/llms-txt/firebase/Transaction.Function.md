# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/Transaction.Function.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction.Function.md.txt

# Transaction.Function

# Transaction.Function


```
interface Transaction.Function<TResult>
```

<br />

*** ** * ** ***

An interface for providing code to be executed within a transaction context.  

|                                                                                            See also                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [runTransaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestore#runTransaction(com.google.firebase.firestore.Transaction.Function<TResult>)) |   |

## Summary

| ### Public functions |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TResult?`           | [apply](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction.Function#apply(com.google.firebase.firestore.Transaction))`(transaction: `[Transaction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/Transaction)`)` |

## Public functions

### apply

```
funÂ apply(transaction:Â Transaction):Â TResult?
```  

|                                                                                                               Throws                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| `com.google.firebase.firestore.FirebaseFirestoreException: `[com.google.firebase.firestore.FirebaseFirestoreException](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FirebaseFirestoreException) |   |