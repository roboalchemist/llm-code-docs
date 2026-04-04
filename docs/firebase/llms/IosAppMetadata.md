# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata.md.txt

# IosAppMetadata

public class **IosAppMetadata** extends Object  
Contains detailed information about an iOS App. Instances of this class are immutable.  

### Public Method Summary

|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata#equals(java.lang.Object))(Object o)                                                                                      |
| String  | [getAppId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata#getAppId())() Returns the globally unique, Firebase-assigned identifier of this iOS App.                               |
| String  | [getBundleId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata#getBundleId())() Returns the canonical bundle ID of this iOS App as it would appear in the iOS AppStore.            |
| String  | [getDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata#getDisplayName())() Returns the user-assigned display name of this iOS App.                                      |
| String  | [getProjectId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata#getProjectId())() Returns the permanent, globally unique, user-assigned ID of the parent Project for this iOS App. |
| int     | [hashCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata#hashCode())()                                                                                                          |
| String  | [toString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/IosAppMetadata#toString())()                                                                                                          |

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

#### public boolean
**equals**
(Object o)

<br />

#### public String
**getAppId**
()

Returns the globally unique, Firebase-assigned identifier of this iOS App. This ID is unique
even across Apps of different platforms, such as Android Apps.  

#### public String
**getBundleId**
()

Returns the canonical bundle ID of this iOS App as it would appear in the iOS AppStore.  

#### public String
**getDisplayName**
()

Returns the user-assigned display name of this iOS App. Returns `null` if it has never
been set.  

#### public String
**getProjectId**
()

Returns the permanent, globally unique, user-assigned ID of the parent Project for this iOS
App.  

#### public int
**hashCode**
()

<br />

#### public String
**toString**
()

<br />