# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp.md.txt

# AndroidApp

public class **AndroidApp** extends Object  
An instance of this class is a reference to an Android App within a Firebase Project; it can be
used to query detailed information about the App, modify the display name of the App, or download
the configuration file for the App.

Note: the methods in this class make RPCs.  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate)                      | [createShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp#createShaCertificate(com.google.firebase.projectmanagement.ShaCertificate))([ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) certificateToAdd) Adds the given SHA certificate to this Android app.                                  |
| ApiFuture\<[ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate)\>         | [createShaCertificateAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp#createShaCertificateAsync(com.google.firebase.projectmanagement.ShaCertificate))([ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) certificateToAdd) Asynchronously adds the given SHA certificate to this Android app.         |
| void                                                                                                                                                        | [deleteShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp#deleteShaCertificate(com.google.firebase.projectmanagement.ShaCertificate))([ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) certificateToRemove) Removes the given SHA certificate from this Android app.                          |
| ApiFuture\<Void\>                                                                                                                                           | [deleteShaCertificateAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp#deleteShaCertificateAsync(com.google.firebase.projectmanagement.ShaCertificate))([ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) certificateToRemove) Asynchronously removes the given SHA certificate from this Android app. |
| String                                                                                                                                                      | [getConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp#getConfig())() Retrieves the configuration artifact associated with this Android App.                                                                                                                                                                                                                                                |
| ApiFuture\<String\>                                                                                                                                         | [getConfigAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp#getConfigAsync())() Asynchronously retrieves the configuration artifact associated with this Android App.                                                                                                                                                                                                                       |
| [AndroidAppMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata)              | [getMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp#getMetadata())() Retrieves detailed information about this Android App.                                                                                                                                                                                                                                                            |
| ApiFuture\<[AndroidAppMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata)\> | [getMetadataAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp#getMetadataAsync())() Asynchronously retrieves information about this Android App.                                                                                                                                                                                                                                            |
| List\<[ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate)\>              | [getShaCertificates](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp#getShaCertificates())() Retrieves the entire list of SHA certificates associated with this Android app.                                                                                                                                                                                                                     |
| ApiFuture\<List\<[ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate)\>\> | [getShaCertificatesAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp#getShaCertificatesAsync())() Asynchronously retrieves the entire list of SHA certificates associated with this Android app.                                                                                                                                                                                            |
| void                                                                                                                                                        | [setDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp#setDisplayName(java.lang.String))(String newDisplayName) Updates the Display Name attribute of this Android App to the one given.                                                                                                                                                                                               |
| ApiFuture\<Void\>                                                                                                                                           | [setDisplayNameAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp#setDisplayNameAsync(java.lang.String))(String newDisplayName) Asynchronously updates the Display Name attribute of this Android App to the one given.                                                                                                                                                                      |

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

#### public [ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate)
**createShaCertificate**
([ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) certificateToAdd)

Adds the given SHA certificate to this Android app.  

##### Parameters

| certificateToAdd | the SHA certificate to be added to this Android app |
|------------------|-----------------------------------------------------|

##### Returns

- a [ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) that was created for this Android app, containing resource name, SHA hash, and certificate type  

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

#### public ApiFuture\<[ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate)\>
**createShaCertificateAsync**
([ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) certificateToAdd)

Asynchronously adds the given SHA certificate to this Android app.  

##### Parameters

| certificateToAdd | the SHA certificate to be added to this Android app |
|------------------|-----------------------------------------------------|

##### Returns

- a `ApiFuture` of a [ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) that was created for this Android app, containing resource name, SHA hash, and certificate type  

#### public void
**deleteShaCertificate**
([ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) certificateToRemove)

Removes the given SHA certificate from this Android app.  

##### Parameters

| certificateToRemove | the SHA certificate to be removed from this Android app |
|---------------------|---------------------------------------------------------|

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

#### public ApiFuture\<Void\>
**deleteShaCertificateAsync**
([ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) certificateToRemove)

Asynchronously removes the given SHA certificate from this Android app.  

##### Parameters

| certificateToRemove | the SHA certificate to be removed from this Android app |
|---------------------|---------------------------------------------------------|

#### public String
**getConfig**
()

Retrieves the configuration artifact associated with this Android App.  

##### Returns

- a modified UTF-8 encoded `String` containing the contents of the artifact  

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

#### public ApiFuture\<String\>
**getConfigAsync**
()

Asynchronously retrieves the configuration artifact associated with this Android App.  

##### Returns

- an `ApiFuture` of a UTF-8 encoded `String` containing the contents of the artifact  

#### public [AndroidAppMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata)
**getMetadata**
()

Retrieves detailed information about this Android App.  

##### Returns

- an [AndroidAppMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata) instance describing this App  

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|                                                                                   Exception                                                                                    |                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

#### public ApiFuture\<[AndroidAppMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata)\>
**getMetadataAsync**
()

Asynchronously retrieves information about this Android App.  

##### Returns

- an `ApiFuture` containing an [AndroidAppMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata) instance describing this App  

#### public List\<[ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate)\>
**getShaCertificates**
()

Retrieves the entire list of SHA certificates associated with this Android app.  

##### Returns

- a list of [ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) containing resource name, SHA hash and certificate type  

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

#### public ApiFuture\<List\<[ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate)\>\>
**getShaCertificatesAsync**
()

Asynchronously retrieves the entire list of SHA certificates associated with this Android app.  

##### Returns

- an `ApiFuture` of a list of [ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) containing resource name, SHA hash and certificate type  

#### public void
**setDisplayName**
(String newDisplayName)

Updates the Display Name attribute of this Android App to the one given.  

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

#### public ApiFuture\<Void\>
**setDisplayNameAsync**
(String newDisplayName)

Asynchronously updates the Display Name attribute of this Android App to the one given.