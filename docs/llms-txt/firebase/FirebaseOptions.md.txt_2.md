# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.md.txt

# FirebaseOptions

public final class **FirebaseOptions** extends Object  
Configurable Firebase options.

### Nested Class Summary

|---|---|---|---|
| class | [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) || Builder for constructing `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions`. |

### Public Method Summary

|---|---|
| static [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#builder())() Creates an empty builder. |
| int | [getConnectTimeout](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#getConnectTimeout())() Returns the connect timeout in milliseconds, which is applied to outgoing REST calls made by the SDK. |
| Map\<String, Object\> | [getDatabaseAuthVariableOverride](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#getDatabaseAuthVariableOverride())() Returns the `auth` variable to be used in Security Rules. |
| String | [getDatabaseUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#getDatabaseUrl())() Returns the Realtime Database URL to use for data storage. |
| HttpTransport | [getHttpTransport](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#getHttpTransport())() Returns the `HttpTransport` used to call remote HTTP endpoints. |
| JsonFactory | [getJsonFactory](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#getJsonFactory())() Returns the `JsonFactory` used to parse JSON when calling remote HTTP endpoints. |
| String | [getProjectId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#getProjectId())() Returns the Google Cloud project ID. |
| int | [getReadTimeout](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#getReadTimeout())() Returns the read timeout applied to outgoing REST calls in milliseconds. |
| String | [getServiceAccountId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#getServiceAccountId())() Returns the client email address of the service account. |
| String | [getStorageBucket](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#getStorageBucket())() Returns the name of the Google Cloud Storage bucket used for storing application data. |
| int | [getWriteTimeout](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#getWriteTimeout())() Returns the write timeout applied to outgoing REST calls in milliseconds. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [toBuilder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#toBuilder())() Creates a new `Builder` from the options object. |

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

#### public static [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**builder**
()

Creates an empty builder.

##### Returns

- A new builder instance.

#### public int
**getConnectTimeout**
()

Returns the connect timeout in milliseconds, which is applied to outgoing REST calls
made by the SDK.

##### Returns

- Connect timeout in milliseconds. 0 indicates an infinite timeout.

#### public Map\<String, Object\>
**getDatabaseAuthVariableOverride**
()

Returns the `auth` variable to be used in Security Rules.

##### Returns

- The `auth` variable supplied via `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setDatabaseAuthVariableOverride(java.util.Map<java.lang.String, java.lang.Object>)`.

#### public String
**getDatabaseUrl**
()

Returns the Realtime Database URL to use for data storage.

##### Returns

- The Realtime Database URL supplied via `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setDatabaseUrl(java.lang.String)`.

#### public HttpTransport
**getHttpTransport**
()

Returns the `HttpTransport` used to call remote HTTP endpoints. This transport is
used by all services of the SDK, except for FirebaseDatabase.

##### Returns

- A Google API client `HttpTransport` instance.

#### public JsonFactory
**getJsonFactory**
()

Returns the `JsonFactory` used to parse JSON when calling remote HTTP endpoints.

##### Returns

- A Google API client `JsonFactory` instance.

#### public String
**getProjectId**
()

Returns the Google Cloud project ID.

##### Returns

- The project ID set via `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setProjectId(java.lang.String)`

#### public int
**getReadTimeout**
()

Returns the read timeout applied to outgoing REST calls in milliseconds.

##### Returns

- Read timeout in milliseconds. 0 indicates an infinite timeout.

#### public String
**getServiceAccountId**
()

Returns the client email address of the service account.

##### Returns

- The client email of the service account set via `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setServiceAccountId(java.lang.String)`

#### public String
**getStorageBucket**
()

Returns the name of the Google Cloud Storage bucket used for storing application data.

##### Returns

- The cloud storage bucket name set via `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setStorageBucket(java.lang.String)`

#### public int
**getWriteTimeout**
()

Returns the write timeout applied to outgoing REST calls in milliseconds.

##### Returns

- Write timeout in milliseconds. 0 indicates an infinite timeout.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**toBuilder**
()

Creates a new `Builder` from the options object.

The new builder is not backed by this object's values; that is, changes made to the new
builder don't change the values of the origin object.