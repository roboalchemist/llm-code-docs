# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.Callbacks.md.txt

# ActivityLifecycleManager.Callbacks

public static abstract class **ActivityLifecycleManager.Callbacks** extends Object  
Override the methods corresponding to the activity.  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [ActivityLifecycleManager.Callbacks](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.Callbacks#ActivityLifecycleManager.Callbacks())() |

### Public Method Summary

|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void | [onActivityCreated](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.Callbacks#onActivityCreated(android.app.Activity, android.os.Bundle))(Activity activity, Bundle bundle)                     |
| void | [onActivityDestroyed](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.Callbacks#onActivityDestroyed(android.app.Activity))(Activity activity)                                                   |
| void | [onActivityPaused](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.Callbacks#onActivityPaused(android.app.Activity))(Activity activity)                                                         |
| void | [onActivityResumed](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.Callbacks#onActivityResumed(android.app.Activity))(Activity activity)                                                       |
| void | [onActivitySaveInstanceState](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.Callbacks#onActivitySaveInstanceState(android.app.Activity, android.os.Bundle))(Activity activity, Bundle bundle) |
| void | [onActivityStarted](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.Callbacks#onActivityStarted(android.app.Activity))(Activity activity)                                                       |
| void | [onActivityStopped](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/ActivityLifecycleManager.Callbacks#onActivityStopped(android.app.Activity))(Activity activity)                                                       |

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
**ActivityLifecycleManager.Callbacks**
()

<br />

## Public Methods

#### public void
**onActivityCreated**
(Activity activity, Bundle bundle)

<br />

##### Parameters

|----------|---|
| activity |   |
| bundle   |   |

#### public void
**onActivityDestroyed**
(Activity activity)

<br />

##### Parameters

|----------|---|
| activity |   |

#### public void
**onActivityPaused**
(Activity activity)

<br />

##### Parameters

|----------|---|
| activity |   |

#### public void
**onActivityResumed**
(Activity activity)

<br />

##### Parameters

|----------|---|
| activity |   |

#### public void
**onActivitySaveInstanceState**
(Activity activity, Bundle bundle)

<br />

##### Parameters

|----------|---|
| activity |   |
| bundle   |   |

#### public void
**onActivityStarted**
(Activity activity)

<br />

##### Parameters

|----------|---|
| activity |   |

#### public void
**onActivityStopped**
(Activity activity)

<br />

##### Parameters

|----------|---|
| activity |   |