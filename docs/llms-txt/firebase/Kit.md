# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit.md.txt

# Kit

public abstract class **Kit** extends Object  
implements Comparable\<[Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit)\>  

|---|---|---|
| Known Direct Subclasses [Answers](https://firebase.google.com/docs/reference/android/com/crashlytics/sdk/android/answers/Answers), [Beta](https://firebase.google.com/docs/reference/android/com/crashlytics/sdk/android/beta/Beta), [Crashlytics](https://firebase.google.com/docs/reference/android/com/crashlytics/sdk/android/crashlytics/Crashlytics), [CrashlyticsCore](https://firebase.google.com/docs/reference/android/com/crashlytics/sdk/android/crashlytics-core/CrashlyticsCore) |------------------------------------------------------------------------------------------------------------------------------------|---| | [Answers](https://firebase.google.com/docs/reference/android/com/crashlytics/sdk/android/answers/Answers)                          |   | | [Beta](https://firebase.google.com/docs/reference/android/com/crashlytics/sdk/android/beta/Beta)                                   |   | | [Crashlytics](https://firebase.google.com/docs/reference/android/com/crashlytics/sdk/android/crashlytics/Crashlytics)              |   | | [CrashlyticsCore](https://firebase.google.com/docs/reference/android/com/crashlytics/sdk/android/crashlytics-core/CrashlyticsCore) |   | |||

The base class to extend from for classes needing initialization with
[with(android.content.Context, Kit[])](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#with(android.content.Context, io.fabric.sdk.android.Kit...))  

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------|
|   | [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#Kit())() |

### Public Method Summary

|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int                                                                                              | [compareTo](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#compareTo(io.fabric.sdk.android.Kit))([Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit) another) Compares [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit)'s using [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency) |
| Context                                                                                          | [getContext](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#getContext())()                                                                                                                                                                                                                                                                                                                                                                    |
| [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric) | [getFabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#getFabric())()                                                                                                                                                                                                                                                                                                                                                                      |
| abstract String                                                                                  | [getIdentifier](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#getIdentifier())() Must be implemented by Kit to allow plugin on-boarding                                                                                                                                                                                                                                                                                                       |
| String                                                                                           | [getPath](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#getPath())()                                                                                                                                                                                                                                                                                                                                                                          |
| abstract String                                                                                  | [getVersion](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#getVersion())()                                                                                                                                                                                                                                                                                                                                                                    |

### Protected Method Summary

|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract Result                                                                                                                 | [doInBackground](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#doInBackground())() For heavy work to be done in initialization process on a background thread.                                                                                                       |
| Collection\<[Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\> | [getDependencies](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#getDependencies())()                                                                                                                                                                                 |
| IdManager                                                                                                                       | [getIdManager](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#getIdManager())()                                                                                                                                                                                       |
| void                                                                                                                            | [onCancelled](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#onCancelled(Result))(Result result) Called after [doInBackground()](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#doInBackground()) is cancelled on the UI thread  |
| void                                                                                                                            | [onPostExecute](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#onPostExecute(Result))(Result result) Called after [doInBackground()](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#doInBackground()) completes on the UI thread |
| boolean                                                                                                                         | [onPreExecute](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#onPreExecute())() Called before initialization on the UI thread                                                                                                                                         |

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

From interface java.lang.Comparable  

|--------------|------------------------------------------------------------------------------------------------------------|
| abstract int | compareTo([Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit) arg0) |

## Public Constructors

#### public
**Kit**
()

<br />

## Public Methods

#### public int
**compareTo**
([Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit) another)

Compares [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit)'s using [Dependency](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Dependency)  

##### Parameters

|---------|---|
| another |   |

#### public Context
**getContext**
()

<br />

##### Returns

- Application [Context](https://developer.android.com/reference/android/content/Context.html)  

#### public [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric)
**getFabric**
()

<br />

##### Returns

- Primary [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric) instance  

#### public abstract String
**getIdentifier**
()

Must be implemented by Kit to allow plugin on-boarding  

##### Returns

- unique identifier  

#### public String
**getPath**
()

<br />

##### Returns

- relative path for Kit  

#### public abstract String
**getVersion**
()

<br />

##### Returns

- Kit Version

## Protected Methods

#### protected abstract Result
**doInBackground**
()

For heavy work to be done in initialization process on a background thread.
The thread is run on the [ExecutorService](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#executorService(java.util.concurrent.ExecutorService))  

#### protected Collection\<[Task](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/Task)\>
**getDependencies**
()

<br />

#### protected IdManager
**getIdManager**
()

<br />

##### Returns

- the IdManager provided for use by this Kit  

#### protected void
**onCancelled**
(Result result)

Called after [doInBackground()](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#doInBackground()) is cancelled on the UI thread  

#### protected void
**onPostExecute**
(Result result)

Called after [doInBackground()](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit#doInBackground()) completes on the UI thread  

#### protected boolean
**onPreExecute**
()

Called before initialization on the UI thread  

##### Throws

|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [UnmetDependencyException](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/UnmetDependencyException) | if there's a missing dependency that causes kit to fail initialization. |