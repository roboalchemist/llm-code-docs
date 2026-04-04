# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder.md.txt

# FirebaseOptions.Builder

public static final class **FirebaseOptions.Builder** extends Object  
Builder for constructing `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions`.

### Public Constructor Summary

|---|---|
|   | [Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#Builder())() *This constructor is deprecated. Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#builder()` instead.* |
|   | [Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#Builder(com.google.firebase.FirebaseOptions))([FirebaseOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions) options) *This constructor is deprecated. Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#toBuilder()` instead.* |

### Public Method Summary

|---|---|
| [FirebaseOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions) | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#build())() Builds the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions` instance from the previously set options. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [setConnectTimeout](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setConnectTimeout(int))(int connectTimeout) Sets the connect timeout for outgoing HTTP (REST) connections made by the SDK. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [setCredentials](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setCredentials(com.google.auth.oauth2.GoogleCredentials))(GoogleCredentials credentials) Sets the `GoogleCredentials` to use to authenticate the SDK. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [setDatabaseAuthVariableOverride](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setDatabaseAuthVariableOverride(java.util.Map<java.lang.String, java.lang.Object>))(Map\<String, Object\> databaseAuthVariableOverride) Sets the `auth` variable to be used by the Realtime Database rules. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [setDatabaseUrl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setDatabaseUrl(java.lang.String))(String databaseUrl) Sets the Realtime Database URL to use for data storage. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [setFirestoreOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setFirestoreOptions(com.google.cloud.firestore.FirestoreOptions))(FirestoreOptions firestoreOptions) Sets the `FirestoreOptions` used to initialize Firestore in the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/FirestoreClient` API. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [setHttpTransport](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setHttpTransport(com.google.api.client.http.HttpTransport))(HttpTransport httpTransport) Sets the `HttpTransport` used to make remote HTTP calls. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [setJsonFactory](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setJsonFactory(com.google.api.client.json.JsonFactory))(JsonFactory jsonFactory) Sets the `JsonFactory` used to parse JSON when making remote HTTP calls. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [setProjectId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setProjectId(java.lang.String))(String projectId) Sets the Google Cloud project ID that should be associated with an app. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [setReadTimeout](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setReadTimeout(int))(int readTimeout) Sets the read timeout for outgoing HTTP (REST) calls made by the SDK. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [setServiceAccountId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setServiceAccountId(java.lang.String))(String serviceAccountId) Sets the client email address of the service account that should be associated with an app. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [setStorageBucket](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setStorageBucket(java.lang.String))(String storageBucket) Sets the name of the Google Cloud Storage bucket for reading and writing application data. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [setThreadManager](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setThreadManager(com.google.firebase.ThreadManager))([ThreadManager](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ThreadManager) threadManager) Sets the `ThreadManager` used to initialize thread pools and thread factories for Firebase apps. |
| [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder) | [setWriteTimeout](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setWriteTimeout(int))(int writeTimeout) Sets the write timeout for outgoing HTTP (REST) calls made by the SDK. |

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

## Public Constructors

#### public
**Builder**
()


**This constructor is deprecated.**   
Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#builder()` instead.

Constructs an empty builder.

#### public
**Builder**
([FirebaseOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions) options)


**This constructor is deprecated.**   
Use `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions#toBuilder()` instead.

Initializes the builder's values from the options object.

The new builder is not backed by this object's values, that is changes made to the new
builder don't change the values of the origin object.

## Public Methods

#### public [FirebaseOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions)
**build**
()

Builds the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions` instance from the previously set options.

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions` instance created from the previously set options.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**setConnectTimeout**
(int connectTimeout)

Sets the connect timeout for outgoing HTTP (REST) connections made by the SDK. This is used
when opening a communication link to a remote HTTP endpoint. This setting does not
affect the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase` and
`https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/FirestoreClient` APIs.

##### Parameters

| connectTimeout | Connect timeout in milliseconds. Must not be negative. |
|---|---|

##### Returns

- This `Builder` instance is returned so subsequent calls can be chained.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**setCredentials**
(GoogleCredentials credentials)

Sets the `GoogleCredentials` to use to authenticate the SDK. This parameter
must be specified when creating a new instance of `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions`.

See [Initialize the SDK](https://firebase.google.com/docs/admin/setup#initialize_the_sdk) for code samples and detailed documentation.

##### Parameters

| credentials | A [`GoogleCredentials`](https://googleapis.dev/java/google-auth-library/latest/index.html?com/google/auth/oauth2/GoogleCredentials.html) instance used to authenticate the SDK. |
|---|---|

##### Returns

- This `Builder` instance is returned so subsequent calls can be chained.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**setDatabaseAuthVariableOverride**
(Map\<String, Object\> databaseAuthVariableOverride)

Sets the `auth` variable to be used by the Realtime Database rules.

When set, security rules for Realtime Database actions are evaluated using the provided
auth object. During evaluation the object is available on the `auth` variable. Use
this option to enforce schema validation and additional security for this app instance.

If this option is not provided, security rules are bypassed entirely for this app
instance. If this option is set to `null`, security rules are evaluated against an
unauthenticated user. That is, the `auth` variable is `null`.

See [Authenticate with limited privileges](https://firebase.google.com/docs/database/admin/start#authenticate-with-limited-privileges) for code samples and detailed documentation.

##### Parameters

| databaseAuthVariableOverride | The value to use for the `auth` variable in the security rules for Realtime Database actions. |
|---|---|

##### Returns

- This `Builder` instance is returned so subsequent calls can be chained.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**setDatabaseUrl**
(String databaseUrl)

Sets the Realtime Database URL to use for data storage.

See [Initialize the SDK](https://firebase.google.com/docs/admin/setup#initialize_the_sdk) for code samples and detailed documentation.

##### Parameters

| databaseUrl | The Realtime Database URL to use for data storage. |
|---|---|

##### Returns

- This `Builder` instance is returned so subsequent calls can be chained.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**setFirestoreOptions**
(FirestoreOptions firestoreOptions)

Sets the `FirestoreOptions` used to initialize Firestore in the
`https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/FirestoreClient` API. This can be used to customize
low-level transport (GRPC) parameters, and timestamp handling behavior.

If credentials or a project ID is set in `FirestoreOptions`, they will get
overwritten by the corresponding parameters in `FirebaseOptions`.

##### Parameters

| firestoreOptions | A `FirestoreOptions` instance. |
|---|---|

##### Returns

- This `Builder` instance is returned so subsequent calls can be chained.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**setHttpTransport**
(HttpTransport httpTransport)

Sets the `HttpTransport` used to make remote HTTP calls. A reasonable default
is used if not explicitly set. The transport specified by calling this method is
used by all services of the SDK, except for `FirebaseDatabase`.

##### Parameters

| httpTransport | An `HttpTransport` instance |
|---|---|

##### Returns

- This `Builder` instance is returned so subsequent calls can be chained.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**setJsonFactory**
(JsonFactory jsonFactory)

Sets the `JsonFactory` used to parse JSON when making remote HTTP calls. A
reasonable default is used if not explicitly set.

##### Parameters

| jsonFactory | A `JsonFactory` instance. |
|---|---|

##### Returns

- This `Builder` instance is returned so subsequent calls can be chained.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**setProjectId**
(String projectId)

Sets the Google Cloud project ID that should be associated with an app.

##### Parameters

| projectId | A non-null, non-empty project ID string. |
|---|---|

##### Returns

- This `Builder` instance is returned so subsequent calls can be chained.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**setReadTimeout**
(int readTimeout)

Sets the read timeout for outgoing HTTP (REST) calls made by the SDK. This does not affect
the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase` and
`https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/FirestoreClient` APIs.

##### Parameters

| readTimeout | Read timeout in milliseconds. Must not be negative. |
|---|---|

##### Returns

- This `Builder` instance is returned so subsequent calls can be chained.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**setServiceAccountId**
(String serviceAccountId)

Sets the client email address of the service account that should be associated with an app.

This is used to [create custom auth tokens](https://firebase.google.com/docs/auth/admin/create-custom-tokens) when service account credentials are not available. The client
email address of a service account can be found in the `client_email` field of the
service account JSON.

##### Parameters

| serviceAccountId | A service account email address string. |
|---|---|

##### Returns

- This `Builder` instance is returned so subsequent calls can be chained.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**setStorageBucket**
(String storageBucket)

Sets the name of the Google Cloud Storage bucket for reading and writing application data.
This should be the full name of the bucket as listed in the
[Google Cloud Platform Console](https://console.cloud.google.com), and must not
include `gs://` or any other protocol prefixes.
The same credential used to initialize the SDK (see `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder#setCredentials(com.google.auth.oauth2.GoogleCredentials)`) is
used to access the bucket.

See [Introduction to the Admin Cloud Storage API](https://firebase.google.com/docs/storage/admin/start) for code samples and detailed documentation.

##### Parameters

| storageBucket | The full name of an existing Google Cloud Storage bucket, excluding any protocol prefixes. |
|---|---|

##### Returns

- This `Builder` instance is returned so subsequent calls can be chained.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**setThreadManager**
([ThreadManager](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/ThreadManager) threadManager)

Sets the `ThreadManager` used to initialize thread pools and thread factories
for Firebase apps.

##### Parameters

| threadManager | A `ThreadManager` instance. |
|---|---|

##### Returns

- This `Builder` instance is returned so subsequent calls can be chained.

#### public [FirebaseOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.Builder)
**setWriteTimeout**
(int writeTimeout)

Sets the write timeout for outgoing HTTP (REST) calls made by the SDK. This does not affect
the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/database/FirebaseDatabase` and
`https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/cloud/FirestoreClient` APIs.

##### Parameters

| writeTimeout | Write timeout in milliseconds. Must not be negative. |
|---|---|

##### Returns

- This `Builder` instance is returned so subsequent calls can be chained.