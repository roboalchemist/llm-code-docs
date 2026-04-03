# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.md.txt

# ActivityLifecycleManager

public class **ActivityLifecycleManager** extends Object  
This is a convenience class that wraps the ActivityLifecycleCallbacks registration. It provides
an abstract Callbacks class that reduces required boilerplate code in your callbacks as well as
OS Version checks that make it compatible with Android versions less than Ice Cream Sandwich.  

### Nested Class Summary

|-------|---|---|-----------------------------------------------------|
| class | [ActivityLifecycleManager.Callbacks](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.Callbacks) || Override the methods corresponding to the activity. |

### Public Constructor Summary

|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [ActivityLifecycleManager](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager#ActivityLifecycleManager(android.content.Context))(Context context) |

### Public Method Summary

|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean | [registerCallbacks](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager#registerCallbacks(io.fabric.sdk.android.ActivityLifecycleManager.Callbacks))([ActivityLifecycleManager.Callbacks](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.Callbacks) callbacks) |
| void    | [resetCallbacks](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager#resetCallbacks())() Unregisters all previously registered callbacks on the application context.                                                                                                                                                     |

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

## Public Constructors

#### public
**ActivityLifecycleManager**
(Context context)

<br />

##### Parameters

|---------|--------------------------------------|
| context | Any context object, it is not stored |

## Public Methods

#### public boolean
**registerCallbacks**
([ActivityLifecycleManager.Callbacks](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.Callbacks) callbacks)

<br />

##### Parameters

|-----------|---------------|
| callbacks | The callbacks |

##### Returns

- true if the version of the application context supports registering lifecycle callbacks  

#### public void
**resetCallbacks**
()

Unregisters all previously registered callbacks on the application context.