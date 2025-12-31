# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata.md.txt

# AndroidAppMetadata

public class **AndroidAppMetadata** extends Object  
Contains detailed information about an Android App. Instances of this class are immutable.  

### Public Method Summary

|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata#equals(java.lang.Object))(Object o)                                                                                          |
| String  | [getAppId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata#getAppId())() Returns the globally unique, Firebase-assigned identifier of this Android App.                               |
| String  | [getDisplayName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata#getDisplayName())() Returns the user-assigned display name of this Android App.                                      |
| String  | [getPackageName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata#getPackageName())() Returns the canonical package name of this Android app as it would appear in Play store.         |
| String  | [getProjectId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata#getProjectId())() Returns the permanent, globally unique, user-assigned ID of the parent Project for this Android App. |
| int     | [hashCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata#hashCode())()                                                                                                              |
| String  | [toString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/AndroidAppMetadata#toString())()                                                                                                              |

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

Returns the globally unique, Firebase-assigned identifier of this Android App. This ID is
unique even across Apps of different platforms, such as iOS Apps.  

#### public String
**getDisplayName**
()

Returns the user-assigned display name of this Android App. Returns `null` if it has
never been set.  

#### public String
**getPackageName**
()

Returns the canonical package name of this Android app as it would appear in Play store.  

#### public String
**getProjectId**
()

Returns the permanent, globally unique, user-assigned ID of the parent Project for this Android
App.  

#### public int
**hashCode**
()

<br />

#### public String
**toString**
()

<br />