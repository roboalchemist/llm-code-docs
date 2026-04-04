# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/FirestoreClient.md.txt

# FirestoreClient

public class **FirestoreClient** extends Object  
`FirestoreClient` provides access to Google Cloud Firestore. Use this API to obtain a
[`Firestore`](https://cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore)
instance, which provides methods for updating and querying data in Firestore.

A Google Cloud project ID is required to access Firestore. FirestoreClient determines the
project ID from the [FirebaseOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions) used to initialize the underlying
[FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp). If that is not available, it examines the credentials used to initialize
the app. Finally it attempts to get the project ID by looking up the GOOGLE_CLOUD_PROJECT and
GCLOUD_PROJECT environment variables. If a project ID cannot be determined by any of these
methods, this API will throw a runtime exception.  

### Public Method Summary

|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static Firestore | [getFirestore](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/FirestoreClient#getFirestore(com.google.firebase.FirebaseApp))([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app) Returns the default Firestore instance associated with the specified Firebase app.                            |
| static Firestore | [getFirestore](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/FirestoreClient#getFirestore(java.lang.String))(String database) Returns the Firestore instance associated with the default Firebase app.                                                                                                                                                        |
| static Firestore | [getFirestore](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/FirestoreClient#getFirestore())() Returns the default Firestore instance associated with the default Firebase app.                                                                                                                                                                               |
| static Firestore | [getFirestore](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/FirestoreClient#getFirestore(com.google.firebase.FirebaseApp, java.lang.String))([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app, String database) Returns the Firestore instance associated with the specified Firebase app. |

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

#### public static Firestore
**getFirestore**
([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app)

Returns the default Firestore instance associated with the specified Firebase app. For a given
app, invocation always returns the same instance. The Firestore instance and all references
obtained from it becomes unusable, once the specified app is deleted.  

##### Parameters

| app | A non-null [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp). |
|-----|----------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A non-null [`Firestore`](https://cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore) instance.  

#### public static Firestore
**getFirestore**
(String database)

Returns the Firestore instance associated with the default Firebase app. Returns the same
instance for all invocations given the same database parameter. The Firestore instance and all
references obtained from it becomes unusable, once the default app is deleted.  

##### Parameters

| database | - The name of database. |
|----------|-------------------------|

##### Returns

- A non-null [`Firestore`](https://cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore) instance.  

#### public static Firestore
**getFirestore**
()

Returns the default Firestore instance associated with the default Firebase app. Returns the
same instance for all invocations. The Firestore instance and all references obtained from it
becomes unusable, once the default app is deleted.  

##### Returns

- A non-null [`Firestore`](https://cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore) instance.  

#### public static Firestore
**getFirestore**
([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app, String database)

Returns the Firestore instance associated with the specified Firebase app. Returns the same
instance for all invocations given the same app and database parameter. The Firestore instance
and all references obtained from it becomes unusable, once the specified app is deleted.  

##### Parameters

|   app    | A non-null [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp). |
| database |                                                  - The name of database.                                                   |
|----------|----------------------------------------------------------------------------------------------------------------------------|

##### Returns

- A non-null [`Firestore`](https://cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.Firestore) instance.