# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/database/Transaction.Handler.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/database/Transaction.Handler.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler.md.txt

# Transaction.Handler

public static interface **Transaction.Handler**  
An object implementing this interface is used to run a transaction, and will be notified of the
results of the transaction.  

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract [Transaction.Result](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result) | [doTransaction](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler#doTransaction(com.google.firebase.database.MutableData))([MutableData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData) currentData) This method will be called, *possibly multiple times*, with the current data at this location.                                                                                                                                                                               |
| abstract void                                                                                                                                  | [onComplete](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Handler#onComplete(com.google.firebase.database.DatabaseError, boolean, com.google.firebase.database.DataSnapshot))([DatabaseError](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError) error, boolean committed, [DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) currentData) This method will be called once with the results of the transaction. |

## Public Methods

#### public abstract [Transaction.Result](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result)
**doTransaction**
([MutableData](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/MutableData) currentData)

This method will be called, *possibly multiple times* , with the current data at this
location. It is responsible for inspecting that data and returning a [Transaction.Result](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/Transaction.Result)
specifying either the desired new data at the location or that the transaction should be
aborted.   

<br />


Since this method may be called repeatedly for the same transaction, be extremely careful of
any side effects that may be triggered by this method. In addition, this method is called
from within the Firebase Database library's run loop, so care is also required when accessing
data that may be in use by other threads in your application.   

<br />


Best practices for this method are to rely only on the data that is passed in.  

##### Parameters

| currentData | The current data at the location. Update this to the desired data at the location |
|-------------|-----------------------------------------------------------------------------------|

##### Returns

- Either the new data, or an indication to abort the transaction  

#### public abstract void
**onComplete**
([DatabaseError](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DatabaseError) error, boolean committed, [DataSnapshot](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/DataSnapshot) currentData)

This method will be called once with the results of the transaction.  

##### Parameters

|    error    |         null if no errors occurred, otherwise it contains a description of the error         |
|  committed  | True if the transaction successfully completed, false if it was aborted or an error occurred |
| currentData |                               The current data at the location                               |
|-------------|----------------------------------------------------------------------------------------------|