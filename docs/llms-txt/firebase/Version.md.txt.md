# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version.md.txt

# Version

public final class **Version** extends Object  
Represents a Remote Config template version.
Output only, except for the version description. Contains metadata about a particular
version of the Remote Config template. All fields are set at the time the specified Remote
Config template is published. A version's description field may be specified when
publishing a template.

### Public Method Summary

|---|---|
| boolean | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version#equals(java.lang.Object))(Object o) |
| String | [getDescription](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version#getDescription())() Gets the user-provided description of the corresponding Remote Config template. |
| String | [getRollbackSource](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version#getRollbackSource())() Gets the rollback source of the template. |
| String | [getUpdateOrigin](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version#getUpdateOrigin())() Gets the origin of the template update action. |
| long | [getUpdateTime](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version#getUpdateTime())() Gets the update time of the version. |
| String | [getUpdateType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version#getUpdateType())() Gets the type of the template update action. |
| [User](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/User) | [getUpdateUser](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version#getUpdateUser())() Gets the update user of the template. |
| String | [getVersionNumber](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version#getVersionNumber())() Gets the version number of the template. |
| int | [hashCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version#hashCode())() |
| boolean | [isLegacy](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version#isLegacy())() Indicates whether this Remote Config template was published before version history was supported. |
| [Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version) | [setDescription](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version#setDescription(java.lang.String))(String description) Sets the user-provided description of the template. |
| static [Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version) | [withDescription](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version#withDescription(java.lang.String))(String description) Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version` with a description. |

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

## Public Methods

#### public boolean
**equals**
(Object o)

<br />

#### public String
**getDescription**
()

Gets the user-provided description of the corresponding Remote Config template.

##### Returns

- The description of the template or null.

#### public String
**getRollbackSource**
()

Gets the rollback source of the template.

The version number of the Remote Config template that has become the current version
due to a rollback. Only present if this version is the result of a rollback.

##### Returns

- The rollback source of the template or null.

#### public String
**getUpdateOrigin**
()

Gets the origin of the template update action.

##### Returns

- The origin of the template update action or null.

#### public long
**getUpdateTime**
()

Gets the update time of the version. The timestamp of when this version of the Remote Config
template was written to the Remote Config backend.

##### Returns

- The update time of the version or null.

#### public String
**getUpdateType**
()

Gets the type of the template update action.

##### Returns

- The type of the template update action or null.

#### public [User](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/User)
**getUpdateUser**
()

Gets the update user of the template.
An aggregation of all metadata fields about the account that performed the update.

##### Returns

- The update user of the template or null.

#### public String
**getVersionNumber**
()

Gets the version number of the template.

##### Returns

- The version number or null.

#### public int
**hashCode**
()

<br />

#### public boolean
**isLegacy**
()

Indicates whether this Remote Config template was published before version history was
supported.

##### Returns

- true if the template was published before version history was supported, and false otherwise.

#### public [Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version)
**setDescription**
(String description)

Sets the user-provided description of the template.

##### Parameters

| description | The description of the template. |
|---|---|

##### Returns

- This `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version`.

#### public static [Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version)
**withDescription**
(String description)

Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version` with a description.