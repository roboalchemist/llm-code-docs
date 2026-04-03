# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp.md.txt

# IosApp

public class **IosApp** extends Object  
An instance of this class is a reference to an iOS App within a Firebase Project; it can be used
to query detailed information about the App, modify the display name of the App, or download the
configuration file for the App.

Note: the methods in this class make RPCs.  

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| String                                                                                                                                              | [getConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp#getConfig())() Retrieves the configuration artifact associated with this iOS App.                                                                           |
| ApiFuture\<String\>                                                                                                                                 | [getConfigAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp#getConfigAsync())() Asynchronously retrieves the configuration artifact associated with this iOS App.                                                  |
| [IosAppMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata)              | [getMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp#getMetadata())() Retrieves detailed information about this iOS App.                                                                                       |
| ApiFuture\<[IosAppMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata)\> | [getMetadataAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp#getMetadataAsync())() Asynchronously retrieves information about this iOS App.                                                                       |
| void                                                                                                                                                | [setDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp#setDisplayName(java.lang.String))(String newDisplayName) Updates the Display Name attribute of this iOS App to the one given.                          |
| ApiFuture\<Void\>                                                                                                                                   | [setDisplayNameAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp#setDisplayNameAsync(java.lang.String))(String newDisplayName) Asynchronously updates the Display Name attribute of this iOS App to the one given. |
| String                                                                                                                                              | [toString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp#toString())()                                                                                                                                                |

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

#### public String
**getConfig**
()

Retrieves the configuration artifact associated with this iOS App.  

##### Returns

- a modified UTF-8 encoded `String` containing the contents of the artifact  

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

#### public ApiFuture\<String\>
**getConfigAsync**
()

Asynchronously retrieves the configuration artifact associated with this iOS App.  

##### Returns

- an `ApiFuture` of a UTF-8 encoded `String` containing the contents of the artifact  

#### public [IosAppMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata)
**getMetadata**
()

Retrieves detailed information about this iOS App.  

##### Returns

- an [IosAppMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata) instance describing this App  

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

#### public ApiFuture\<[IosAppMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata)\>
**getMetadataAsync**
()

Asynchronously retrieves information about this iOS App.  

##### Returns

- an `ApiFuture` containing an [IosAppMetadata](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata) instance describing this App  

#### public void
**setDisplayName**
(String newDisplayName)

Updates the Display Name attribute of this iOS App to the one given.  

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

#### public ApiFuture\<Void\>
**setDisplayNameAsync**
(String newDisplayName)

Asynchronously updates the Display Name attribute of this iOS App to the one given.  

#### public String
**toString**
()

<br />