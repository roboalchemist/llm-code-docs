# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/iid/FirebaseInstanceId.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId.md.txt

# FirebaseInstanceId

public class **FirebaseInstanceId** extends Object  
This class is the entry point for all server-side Firebase Instance ID actions.

Enables deleting instance IDs associated with Firebase projects.  

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                                 | [deleteInstanceId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId(java.lang.String))(String instanceId) Deletes the specified instance ID and the associated data from Firebase.                                                                                                                                                                                                                                                                                                                   |
| ApiFuture\<Void\>                                                                                                                                    | [deleteInstanceIdAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceIdAsync(java.lang.String))(String instanceId) Similar to [deleteInstanceId(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId(java.lang.String)) but performs the operation asynchronously.                                                                                                                                                  |
| static [FirebaseInstanceId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId)              | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId#getInstance())() Gets the [FirebaseInstanceId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp).                                                                                                                                                    |
| synchronized static [FirebaseInstanceId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId#getInstance(com.google.firebase.FirebaseApp))([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app) Gets the [FirebaseInstanceId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId) instance for the specified [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp). |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Methods

#### public void
**deleteInstanceId**
(String instanceId)

Deletes the specified instance ID and the associated data from Firebase.

Note that Google Analytics for Firebase uses its own form of Instance ID to keep track of
analytics data. Therefore deleting a regular Instance ID does not delete Analytics data.
See [Delete an Instance ID](https://firebase.google.com/support/privacy/manage-iids#delete_an_instance_id) for more information.  

##### Parameters

| instanceId | A non-null, non-empty instance ID string. |
|------------|-------------------------------------------|

##### Throws

|                                                              IllegalArgumentException                                                              |        If the instance ID is null or empty.        |
| [FirebaseInstanceIdException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceIdException) | If an error occurs while deleting the instance ID. |
|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|

#### public ApiFuture\<Void\>
**deleteInstanceIdAsync**
(String instanceId)

Similar to [deleteInstanceId(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId#deleteInstanceId(java.lang.String)) but performs the operation asynchronously.  

##### Parameters

| instanceId | A non-null, non-empty instance ID string. |
|------------|-------------------------------------------|

##### Returns

- An `ApiFuture` which will complete successfully when the instance ID is deleted, or unsuccessfully with the failure Exception.  

##### Throws

| IllegalArgumentException | If the instance ID is null or empty. |
|--------------------------|--------------------------------------|

#### public static [FirebaseInstanceId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId)
**getInstance**
()

Gets the [FirebaseInstanceId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp).  

##### Returns

- The [FirebaseInstanceId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp).  

#### public static synchronized [FirebaseInstanceId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId)
**getInstance**
([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app)

Gets the [FirebaseInstanceId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId) instance for the specified [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp).  

##### Returns

- The [FirebaseInstanceId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/iid/FirebaseInstanceId) instance for the specified [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp).