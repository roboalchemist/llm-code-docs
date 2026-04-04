# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.md.txt

# Transaction

public class **Transaction** extends Object  
The Transaction class encapsulates the functionality needed to perform a transaction on the data
at a location.   

<br />


To run a transaction, provide a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler` to `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseReference#runTransaction(com.google.firebase.database.Transaction.Handler)`. That handler
will be passed the current data at the location, and must return a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result`. A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result` can be created using either `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction#success(com.google.firebase.database.MutableData)` or `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction#abort()`.

### Nested Class Summary

|---|---|---|---|
| interface | [Transaction.Handler](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler) || An object implementing this interface is used to run a transaction, and will be notified of the results of the transaction. |
| class | [Transaction.Result](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result) || Instances of this class represent the desired outcome of a single run of a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler`'s doTransaction method. |

### Public Constructor Summary

|---|---|
|   | [Transaction](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction#Transaction())() |

### Public Method Summary

|---|---|
| static [Transaction.Result](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result) | [abort](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction#abort())() |
| static [Transaction.Result](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result) | [success](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction#success(com.google.firebase.database.MutableData))([MutableData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData) resultData) |

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

## Public Constructors

#### public
**Transaction**
()

<br />

## Public Methods

#### public static [Transaction.Result](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result)
**abort**
()

<br />

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result` that aborts the transaction

#### public static [Transaction.Result](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result)
**success**
([MutableData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData) resultData)

<br />

##### Parameters

| resultData | The desired data at the location |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result` indicating the new data to be stored at the location