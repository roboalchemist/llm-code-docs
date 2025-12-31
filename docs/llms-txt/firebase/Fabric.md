# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.md.txt

# Fabric

public class **Fabric** extends Object  
Fabric initializes and stores the provided [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit)'s.  

### Nested Class Summary

|-------|---|---|-------------------------------------------------------------------------------------------------------------------------------------|
| class | [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder) || Fluent API for creating [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric) instances. |

### Constant Summary

|--------|---------------------------------------------------------------------------------------------------|--------------|
| String | [TAG](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#TAG) | Logging tag. |

### Public Method Summary

|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ActivityLifecycleManager](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager) | [getActivityLifecycleManager](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#getActivityLifecycleManager())()                                                                                                                                                                                |
| String                                                                                                                               | [getAppIdentifier](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#getAppIdentifier())() The value for the Application Identifier (defaults to package name).                                                                                                                                 |
| String                                                                                                                               | [getAppInstallIdentifier](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#getAppInstallIdentifier())() The overridden value for the Application Install Identifier, or a generated value.                                                                                                     |
| Activity                                                                                                                             | [getCurrentActivity](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#getCurrentActivity())()                                                                                                                                                                                                  |
| ExecutorService                                                                                                                      | [getExecutorService](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#getExecutorService())()                                                                                                                                                                                                  |
| String                                                                                                                               | [getIdentifier](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#getIdentifier())()                                                                                                                                                                                                            |
| static \<T extends [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit)\> T                    | [getKit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#getKit(java.lang.Class<T>))(Class\<T\> cls)                                                                                                                                                                                          |
| Collection\<[Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit)\>                             | [getKits](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#getKits())() Returns the [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit)s registered with SDK.                                                                                           |
| static [Logger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger)                              | [getLogger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#getLogger())() Returns the global [Logger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger).                                                                                               |
| Handler                                                                                                                              | [getMainHandler](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#getMainHandler())()                                                                                                                                                                                                          |
| String                                                                                                                               | [getVersion](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#getVersion())()                                                                                                                                                                                                                  |
| static boolean                                                                                                                       | [isDebuggable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#isDebuggable())() Returns the global value for debug mode.                                                                                                                                                                     |
| static boolean                                                                                                                       | [isInitialized](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#isInitialized())() Returns true when all kits have finished asynchronous initialization.                                                                                                                                      |
| [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric)                                     | [setCurrentActivity](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#setCurrentActivity(android.app.Activity))(Activity activity) Used for Fabric to Display UI components.                                                                                                                   |
| static [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric)                              | [with](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#with(io.fabric.sdk.android.Fabric))([Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric) fabric) Entry point to initialize Fabric and contained Kits.                                      |
| static [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric)                              | [with](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#with(android.content.Context, io.fabric.sdk.android.Kit...))(Context context, [Kit...](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit) kits) Entry point to initialize Fabric and contained Kits. |

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

## Constants

#### public static final String
**TAG**

Logging tag.  
Constant Value: "Fabric"

## Public Methods

#### public [ActivityLifecycleManager](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager)
**getActivityLifecycleManager**
()

<br />

#### public String
**getAppIdentifier**
()

The value for the Application Identifier (defaults to package name).  

#### public String
**getAppInstallIdentifier**
()

The overridden value for the Application Install Identifier, or a generated value.  

#### public Activity
**getCurrentActivity**
()

<br />

##### Returns

- the current foreground [Activity](https://firebase.google.com/docs/reference/androidreference/android/app/Activity) if available, may be `null`. Caller is expected to check lifecycle state before using, see [isFinishing()](https://firebase.google.com/docs/reference/androidreference/android/app/Activity#isFinishing()).  

#### public ExecutorService
**getExecutorService**
()

<br />

#### public String
**getIdentifier**
()

<br />

##### Returns

- identifier of Sdk  

#### public static T
**getKit**
(Class\<T\> cls)

<br />

##### Parameters

|-----|------------------------------------------------------------------------------------------------------------|
| cls | Class extending [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit) |

##### Returns

- [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit) instance Will return null if Component not initialized with SDK.  

##### Throws

|-----------------------|---------------------------------------------|
| IllegalStateException | if @{link Fabric} has not been initialized. |

#### public Collection\<[Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit)\>
**getKits**
()

Returns the [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit)s registered with SDK.  

#### public static [Logger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger)
**getLogger**
()

Returns the global [Logger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger).  

#### public Handler
**getMainHandler**
()

<br />

#### public String
**getVersion**
()

<br />

##### Returns

- version for Sdk  

#### public static boolean
**isDebuggable**
()

Returns the global value for debug mode.  

#### public static boolean
**isInitialized**
()

Returns true when all kits have finished asynchronous initialization.  

#### public [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric)
**setCurrentActivity**
(Activity activity)

Used for Fabric to Display UI components.  

##### Parameters

|----------|---|
| activity |   |

#### public static [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric)
**with**
([Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric) fabric)

Entry point to initialize Fabric and contained Kits.
Subsequent calls to this method will return the original instance.
Only the Application context is retained.
See http://developer.android.com/resources/articles/avoiding-memory-leaks.html  

##### Parameters

|--------|-------------------------------------------|
| fabric | instance to initialize and set as primary |

#### public static [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric)
**with**
(Context context, [Kit...](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit) kits)

Entry point to initialize Fabric and contained Kits.
Only the Application context is retained.
See http://developer.android.com/resources/articles/avoiding-memory-leaks.html.  

##### Parameters

|---------|-----------------------------------------------------------------------------------------------------------------------------------|
| context | Android context used for initialization                                                                                           |
| kits    | List of [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit) to be built, must not be empty |

##### See Also

- [for more verbose controls.](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder)