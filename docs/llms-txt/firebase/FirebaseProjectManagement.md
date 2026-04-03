# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement.md.txt

# FirebaseProjectManagement

public class **FirebaseProjectManagement** extends Object  
This class is the entry point for all Firebase Project Management actions.

You can get an instance of FirebaseProjectManagement via [getInstance(FirebaseApp)](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#getInstance(com.google.firebase.FirebaseApp)),
and then use it to modify or retrieve information about your Firebase project, as well as create,
modify, or retrieve information about the Android or iOS Apps in your Firebase project.  

### Public Method Summary

|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)                                      | [createAndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#createAndroidApp(java.lang.String))(String packageName) Creates a new Android App in the associated Firebase project and returns an [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp) reference to it.                                                                                                                                                                                           |
| [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)                                      | [createAndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#createAndroidApp(java.lang.String, java.lang.String))(String packageName, String displayName) Creates a new Android App in the associated Firebase project and returns an [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp) reference to it.                                                                                                                                                     |
| ApiFuture\<[AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)\>                         | [createAndroidAppAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#createAndroidAppAsync(java.lang.String))(String packageName) Asynchronously creates a new Android App in the associated Firebase project and returns an `ApiFuture` that will eventually contain the [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp) reference to it.                                                                                                                     |
| ApiFuture\<[AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)\>                         | [createAndroidAppAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#createAndroidAppAsync(java.lang.String, java.lang.String))(String packageName, String displayName) Asynchronously creates a new Android App in the associated Firebase project and returns an `ApiFuture` that will eventually contain the [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp) reference to it.                                                                               |
| [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)                                              | [createIosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#createIosApp(java.lang.String, java.lang.String))(String bundleId, String displayName) Creates a new iOS App in the associated Firebase project and returns an [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp) reference to it.                                                                                                                                                                            |
| [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)                                              | [createIosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#createIosApp(java.lang.String))(String bundleId) Creates a new iOS App in the associated Firebase project and returns an [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp) reference to it.                                                                                                                                                                                                                  |
| ApiFuture\<[IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)\>                                 | [createIosAppAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#createIosAppAsync(java.lang.String, java.lang.String))(String bundleId, String displayName) Asynchronously creates a new iOS App in the associated Firebase project and returns an `ApiFuture` that will eventually contain the [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp) reference to it.                                                                                                      |
| ApiFuture\<[IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)\>                                 | [createIosAppAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#createIosAppAsync(java.lang.String))(String bundleId) Asynchronously creates a new iOS App in the associated Firebase project and returns an `ApiFuture` that will eventually contain the [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp) reference to it.                                                                                                                                            |
| [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)                                      | [getAndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#getAndroidApp(java.lang.String))(String appId) Obtains an [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp) reference to an Android App in the associated Firebase project.                                                                                                                                                                                                                         |
| static [FirebaseProjectManagement](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#getInstance())() Gets the [FirebaseProjectManagement](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp).                                                                                                                                                    |
| static [FirebaseProjectManagement](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#getInstance(com.google.firebase.FirebaseApp))([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app) Gets the [FirebaseProjectManagement](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement) instance for the specified [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp). |
| [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)                                              | [getIosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#getIosApp(java.lang.String))(String appId) Obtains an [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp) reference to an iOS App in the associated Firebase project.                                                                                                                                                                                                                                             |
| List\<[AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)\>                              | [listAndroidApps](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#listAndroidApps())() Lists all Android Apps in the associated Firebase project, returning a list of [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp) references to each.                                                                                                                                                                                                                         |
| ApiFuture\<List\<[AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)\>\>                 | [listAndroidAppsAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#listAndroidAppsAsync())() Asynchronously lists all Android Apps in the associated Firebase project, returning an `ApiFuture` of a list of [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp) references to each.                                                                                                                                                                              |
| List\<[IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)\>                                      | [listIosApps](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#listIosApps())() Lists all iOS Apps in the associated Firebase project, returning a list of [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp) references to each.                                                                                                                                                                                                                                             |
| ApiFuture\<List\<[IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)\>\>                         | [listIosAppsAsync](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement#listIosAppsAsync())() Asynchronously lists all iOS Apps in the associated Firebase project, returning an `ApiFuture` of a list of [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp) references to each.                                                                                                                                                                                                  |

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

#### public [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)
**createAndroidApp**
(String packageName)

Creates a new Android App in the associated Firebase project and returns an [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)
reference to it.  

##### Parameters

| packageName | the package name of the Android App to be created |
|-------------|---------------------------------------------------|

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

##### See Also

- [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)  

#### public [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)
**createAndroidApp**
(String packageName, String displayName)

Creates a new Android App in the associated Firebase project and returns an [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)
reference to it.  

##### Parameters

| packageName | the package name of the Android App to be created |
| displayName |          a nickname for this Android App          |
|-------------|---------------------------------------------------|

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

##### See Also

- [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)  

#### public ApiFuture\<[AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)\>
**createAndroidAppAsync**
(String packageName)

Asynchronously creates a new Android App in the associated Firebase project and returns an
`ApiFuture` that will eventually contain the [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp) reference to it.  

##### Parameters

| packageName | the package name of the Android App to be created |
|-------------|---------------------------------------------------|

##### See Also

- [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)  

#### public ApiFuture\<[AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)\>
**createAndroidAppAsync**
(String packageName, String displayName)

Asynchronously creates a new Android App in the associated Firebase project and returns an
`ApiFuture` that will eventually contain the [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp) reference to it.  

##### Parameters

| packageName | the package name of the Android App to be created |
| displayName |          a nickname for this Android App          |
|-------------|---------------------------------------------------|

##### See Also

- [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)  

#### public [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)
**createIosApp**
(String bundleId, String displayName)

Creates a new iOS App in the associated Firebase project and returns an [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)
reference to it.  

##### Parameters

|  bundleId   | the bundle ID of the iOS App to be created |
| displayName |        a nickname for this iOS App         |
|-------------|--------------------------------------------|

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

##### See Also

- [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)  

#### public [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)
**createIosApp**
(String bundleId)

Creates a new iOS App in the associated Firebase project and returns an [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)
reference to it.  

##### Parameters

| bundleId | the bundle ID of the iOS App to be created |
|----------|--------------------------------------------|

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

##### See Also

- [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)  

#### public ApiFuture\<[IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)\>
**createIosAppAsync**
(String bundleId, String displayName)

Asynchronously creates a new iOS App in the associated Firebase project and returns an `ApiFuture` that will eventually contain the [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp) reference to it.  

##### Parameters

|  bundleId   | the bundle ID of the iOS App to be created |
| displayName |        a nickname for this iOS App         |
|-------------|--------------------------------------------|

##### See Also

- [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)  

#### public ApiFuture\<[IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)\>
**createIosAppAsync**
(String bundleId)

Asynchronously creates a new iOS App in the associated Firebase project and returns an `ApiFuture` that will eventually contain the [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp) reference to it.  

##### Parameters

| bundleId | the bundle ID of the iOS App to be created |
|----------|--------------------------------------------|

##### See Also

- [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)  

#### public [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)
**getAndroidApp**
(String appId)

Obtains an [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp) reference to an Android App in the associated Firebase project.  

##### Parameters

| appId | the App ID that identifies this Android App. |
|-------|----------------------------------------------|

##### See Also

- [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)  

#### public static [FirebaseProjectManagement](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement)
**getInstance**
()

Gets the [FirebaseProjectManagement](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp).  

##### Returns

- the [FirebaseProjectManagement](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement) instance for the default [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp)  

#### public static [FirebaseProjectManagement](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement)
**getInstance**
([FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) app)

Gets the [FirebaseProjectManagement](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement) instance for the specified [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp).  

##### Returns

- the [FirebaseProjectManagement](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagement) instance for the specified [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp)  

#### public [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)
**getIosApp**
(String appId)

Obtains an [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp) reference to an iOS App in the associated Firebase project.  

##### Parameters

| appId | the App ID that identifies this iOS App. |
|-------|------------------------------------------|

##### See Also

- [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)  

#### public List\<[AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)\>
**listAndroidApps**
()

Lists all Android Apps in the associated Firebase project, returning a list of [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp) references to each. This returned list is read-only and cannot be modified.  

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

##### See Also

- [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)  

#### public ApiFuture\<List\<[AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)\>\>
**listAndroidAppsAsync**
()

Asynchronously lists all Android Apps in the associated Firebase project, returning an `ApiFuture` of a list of [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp) references to each. This returned list is read-only
and cannot be modified.  

##### See Also

- [AndroidApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidApp)  

#### public List\<[IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)\>
**listIosApps**
()

Lists all iOS Apps in the associated Firebase project, returning a list of [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)
references to each. This returned list is read-only and cannot be modified.  

##### Throws

| [FirebaseProjectManagementException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/FirebaseProjectManagementException) | if there was an error during the RPC |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|

##### See Also

- [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)  

#### public ApiFuture\<List\<[IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)\>\>
**listIosAppsAsync**
()

Asynchronously lists all iOS Apps in the associated Firebase project, returning an `ApiFuture` of a list of [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp) references to each. This returned list is read-only and
cannot be modified.  

##### See Also

- [IosApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosApp)