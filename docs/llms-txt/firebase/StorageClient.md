# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/StorageClient.md.txt

# StorageClient

public class **StorageClient** extends Object  
StorageClient provides access to Google Cloud Storage APIs. You can specify a default cloud
storage bucket via [FirebaseOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions), and then get a reference to this
default bucket by calling [bucket()](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/StorageClient#bucket()). Or you can get a reference to a
specific bucket at any time by calling [bucket(String)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/StorageClient#bucket(java.lang.String)).

This class requires Google Cloud Storage libraries for Java. Make sure the artifact
google-cloud-storage is in the classpath along with its transitive dependencies.  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bucket                                                                                                                                       | [bucket](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/StorageClient#bucket())() Returns the default cloud storage bucket associated with the current app.                                                                                  |
| Bucket                                                                                                                                       | [bucket](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/StorageClient#bucket(java.lang.String))(String name) Returns a cloud storage Bucket instance for the specified bucket name.                                                          |
| static [StorageClient](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/StorageClient)              | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/StorageClient#getInstance())()                                                                                                                                                  |
| synchronized static [StorageClient](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/StorageClient) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/StorageClient#getInstance(com.google.firebase.FirebaseApp))([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app) |

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

#### public Bucket
**bucket**
()

Returns the default cloud storage bucket associated with the current app. This is the bucket
configured via [FirebaseOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions) when initializing the app. If
no bucket was configured via options, this method throws an exception.  

##### Returns

- a cloud storage [`Bucket`](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket) instance.  

##### Throws

| IllegalArgumentException | If no bucket is configured via `FirebaseOptions`, or if the bucket does not exist. |
|--------------------------|------------------------------------------------------------------------------------|

#### public Bucket
**bucket**
(String name)

Returns a cloud storage Bucket instance for the specified bucket name.  

##### Parameters

| name | a non-null, non-empty bucket name. |
|------|------------------------------------|

##### Returns

- a cloud storage [`Bucket`](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket) instance.  

##### Throws

| IllegalArgumentException | If the bucket name is null, empty, or if the specified bucket does not exist. |
|--------------------------|-------------------------------------------------------------------------------|

#### public static [StorageClient](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/StorageClient)
**getInstance**
()

<br />

#### public static synchronized [StorageClient](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/StorageClient)
**getInstance**
([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app)

<br />