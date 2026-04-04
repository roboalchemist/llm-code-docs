# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Result.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result.md.txt

# Transaction.Result

# Transaction.Result


```
class Transaction.Result
```

<br />

*** ** * ** ***

Instances of this class represent the desired outcome of a single run of a [Handler](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler)'s doTransaction method. The options are:

- Set the data to the new value (success)
- abort the transaction

Instances are created using [success](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction#success(com.google.firebase.database.MutableData)) or [abort](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction#abort()).

## Summary

|                                ### Public functions                                |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | [isSuccess](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Result#isSuccess())`()` |

## Public functions

### isSuccess

```
funÂ isSuccess():Â Boolean
```  

|                                      Returns                                       |
|------------------------------------------------------------------------------------|-----------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html) | Whether or not this result is a success |