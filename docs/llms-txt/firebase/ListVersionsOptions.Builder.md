# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder.md.txt

# ListVersionsOptions.Builder

public static class **ListVersionsOptions.Builder** extends Object  

### Public Method Summary

|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ListVersionsOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder#build())() Builds a new [ListVersionsOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions) instance from the fields set on this builder. |
| [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder) | [setEndTimeMillis](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder#setEndTimeMillis(long))(long endTimeMillis) Sets the latest update time to include in the results.                                                                                                     |
| [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder) | [setEndVersionNumber](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder#setEndVersionNumber(java.lang.String))(String endVersionNumber) Sets the newest version number to include in the results.                                                                           |
| [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder) | [setEndVersionNumber](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder#setEndVersionNumber(long))(long endVersionNumber) Sets the newest version number to include in the results.                                                                                         |
| [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder) | [setPageSize](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder#setPageSize(int))(int pageSize) Sets the page size.                                                                                                                                                         |
| [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder) | [setPageToken](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder#setPageToken(java.lang.String))(String pageToken) Sets the page token.                                                                                                                                     |
| [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder) | [setStartTimeMillis](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder#setStartTimeMillis(long))(long startTimeMillis) Sets the earliest update time to include in the results.                                                                                             |

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

#### public [ListVersionsOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions)
**build**
()

Builds a new [ListVersionsOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions) instance from the fields set on this builder.  

##### Returns

- A non-null [ListVersionsOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions).  

#### public [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder)
**setEndTimeMillis**
(long endTimeMillis)

Sets the latest update time to include in the results.  

##### Parameters

| endTimeMillis | Specify the latest update time to include in the results. Any entries updated on or after this time are omitted. |
|---------------|------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder)
**setEndVersionNumber**
(String endVersionNumber)

Sets the newest version number to include in the results.  

##### Parameters

| endVersionNumber | Specify the newest version number to include in the results. If specified, must be greater than zero. Defaults to the newest version. |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder)
**setEndVersionNumber**
(long endVersionNumber)

Sets the newest version number to include in the results.  

##### Parameters

| endVersionNumber | Specify the newest version number to include in the results. If specified, must be greater than zero. Defaults to the newest version. |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder)
**setPageSize**
(int pageSize)

Sets the page size.  

##### Parameters

| pageSize | The maximum number of items to return per page. |
|----------|-------------------------------------------------|

##### Returns

- This builder.  

#### public [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder)
**setPageToken**
(String pageToken)

Sets the page token.  

##### Parameters

| pageToken | The `nextPageToken` value returned from a previous List request, if any. |
|-----------|--------------------------------------------------------------------------|

##### Returns

- This builder.  

#### public [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder)
**setStartTimeMillis**
(long startTimeMillis)

Sets the earliest update time to include in the results.  

##### Parameters

| startTimeMillis | Specify the earliest update time to include in the results. Any entries updated before this time are omitted. |
|-----------------|---------------------------------------------------------------------------------------------------------------|

##### Returns

- This builder.