# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result.md.txt

# Transaction.Result

public static class **Transaction.Result** extends Object  
Instances of this class represent the desired outcome of a single run of a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler`'s
doTransaction method. The options are:

- Set the data to the new value (success)
- abort the transaction

Instances are created using `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction#success(com.google.firebase.database.MutableData)` or `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction#abort()`.

### Public Method Summary

|---|---|
| boolean | [isSuccess](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result#isSuccess())() |

### Inherited Method Summary

From class java.lang.Object

|---|---|
| Object | clone() |
| boolean | equals(Object arg0) |
| void | finalize() |
| final Class\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| String | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Methods

#### public boolean
**isSuccess**
()

<br />

##### Returns

- Whether or not this result is a success