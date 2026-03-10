# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp.md.txt

# FirebaseApp

public class **FirebaseApp** extends Object  
The entry point of Firebase SDKs. It holds common configuration and state for Firebase APIs. Most
applications don't need to directly interact with FirebaseApp.

Firebase APIs use the default FirebaseApp by default, unless a different one is explicitly
passed to the API via FirebaseFoo.getInstance(firebaseApp).

`https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#initializeApp(com.google.firebase.FirebaseOptions)` initializes the default app instance. This
method should be invoked at startup.

### Constant Summary

|---|---|---|
| String | [DEFAULT_APP_NAME](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#DEFAULT_APP_NAME) |   |

### Public Method Summary

|---|---|
| void | [delete](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#delete())() Deletes this `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` object, and releases any local state and managed resources associated with it. |
| boolean | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#equals(java.lang.Object))(Object o) |
| static List\<[FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp)\> | [getApps](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#getApps())() Returns a list of all FirebaseApps. |
| static [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#getInstance(java.lang.String))(String name) Returns the instance identified by the unique name, or throws if it does not exist. |
| static [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) | [getInstance](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#getInstance())() Returns the default (first initialized) instance of the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`. |
| String | [getName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#getName())() Returns the unique name of this app. |
| [FirebaseOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions) | [getOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#getOptions())() Returns the specified `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions`. |
| int | [hashCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#hashCode())() |
| static [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) | [initializeApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#initializeApp(java.lang.String))(String name) Initializes a named `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` instance using Google Application Default Credentials. |
| static [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) | [initializeApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#initializeApp(com.google.firebase.FirebaseOptions, java.lang.String))([FirebaseOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions) options, String name) Initializes a named `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` instance using the given options. |
| static [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) | [initializeApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#initializeApp())() Initializes the default `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` instance using Google Application Default Credentials. |
| static [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp) | [initializeApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#initializeApp(com.google.firebase.FirebaseOptions))([FirebaseOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions) options) Initializes the default `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` instance using the given options. |
| String | [toString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#toString())() |

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

## Constants

#### public static final String
**DEFAULT_APP_NAME**

<br />

Constant Value: "\[DEFAULT\]"

## Public Methods

#### public void
**delete**
()

Deletes this `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` object, and releases any local state and managed resources
associated with it. All calls to this `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` instance will throw once this method
has been called. This also releases any managed resources allocated by other services
attached to this object instance (e.g. `FirebaseAuth`).

A no-op if delete was called before.

#### public boolean
**equals**
(Object o)

<br />

#### public static List\<[FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp)\>
**getApps**
()

Returns a list of all FirebaseApps.

#### public static [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp)
**getInstance**
(String name)

Returns the instance identified by the unique name, or throws if it does not exist.

##### Parameters

| name | represents the name of the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` instance. |
|---|---|

##### Returns

- the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` corresponding to the name.

##### Throws

| IllegalStateException | if the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` was not initialized, either via `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#initializeApp(com.google.firebase.FirebaseOptions, java.lang.String)` or `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#getApps()`. |
|---|---|

#### public static [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp)
**getInstance**
()

Returns the default (first initialized) instance of the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`.

##### Throws

| IllegalStateException | if the default app was not initialized. |
|---|---|

#### public String
**getName**
()

Returns the unique name of this app.

#### public [FirebaseOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions)
**getOptions**
()

Returns the specified `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions`.

#### public int
**hashCode**
()

<br />

#### public static [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp)
**initializeApp**
(String name)

Initializes a named `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` instance using Google Application Default Credentials.
Loads additional `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions` from the environment in the same way as the
`https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp#initializeApp()` method.

##### Throws

| IllegalStateException | if an app with the same name has already been initialized. |
| IllegalArgumentException | if an error occurs while loading options from the environment. |
|---|---|

#### public static [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp)
**initializeApp**
([FirebaseOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions) options, String name)

Initializes a named `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` instance using the given options.

##### Parameters

| options | represents the global `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions` |
| name | unique name for the app. It is an error to initialize an app with an already existing name. Starting and ending whitespace characters in the name are ignored (trimmed). |
|---|---|

##### Returns

- an instance of `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp`

##### Throws

| IllegalStateException | if an app with the same name has already been initialized. |
|---|---|

#### public static [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp)
**initializeApp**
()

Initializes the default `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` instance using Google Application Default
Credentials. Also attempts to load additional `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions` from the environment
by looking up the `FIREBASE_CONFIG` environment variable. If the value of
the variable starts with `'{'`, it is parsed as a JSON object. Otherwise it is
treated as a file name and the JSON content is read from the corresponding file.

##### Throws

| IllegalStateException | if the default app has already been initialized. |
| IllegalArgumentException | if an error occurs while loading options from the environment. |
|---|---|

#### public static [FirebaseApp](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp)
**initializeApp**
([FirebaseOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions) options)

Initializes the default `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseApp` instance using the given options.

##### Throws

| IllegalStateException | if the default app has already been initialized. |
|---|---|

#### public String
**toString**
()

<br />