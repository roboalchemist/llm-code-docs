# Source: https://firebase.google.com/docs/reference/js/app.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/app.md.txt

# firebase::App Class Reference

# firebase::App


`#include <app.h>`

Firebase application object.

## Summary

[firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) acts as a conduit for communication between all Firebase services used by an application.

For example:  

```c++
#if defined(__ANDROID__)
firebase::App::Create(firebase::AppOptions(), jni_env, activity);
#else
firebase::App::Create(firebase::AppOptions());
#endif  // defined(__ANDROID__)
```

<br />

| ### Constructors and Destructors ||
|---|---|
| [~App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1ab8a98ea2e01cf6fbba67ecf1a1bd6a9e)`()` ||

|                                                                                                                                                                                                  ### Public functions                                                                                                                                                                                                  ||
|----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GetJNIEnv](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1a1126e4e052022bfe90775e34dd8f6657)`() const ` | `JNIEnv *` Get JNI environment, needed for performing JNI calls, set on creation.                                                                                                                                                                                  |
| [activity](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1a9b2a4d637c1119d6de41b7bdad71ff16)`() const `  | `jobject` Get a global reference to the Android activity provided to the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) on creation.                                                                               |
| [java_vm](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1ae6832ba43305b94236f32816a8749fe8)`() const `   | `JavaVM *` Get Java virtual machine, retrieved from the initial JNI environment.                                                                                                                                                                                   |
| [name](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1a3c9091d46ee6dd5c3b58a52848c96d55)`() const `      | `const char *` Get the name of this [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance.                                                                                                                       |
| [options](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1adf8db5ccbd2d0e6425de9d2539e9567d)`() const `   | `const `[AppOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options)` &` Get options the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) was created with. |

|                                                                                                                                                                                                                                                                                              ### Public static functions                                                                                                                                                                                                                                                                                               ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Create](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1a5161747a9bbed350214cb5e1c0a23503)`()`                                                                                                                                                                                             | [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)` *` Initializes the default [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with default options.                        |
| [Create](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1a8e693127f5d536c1e27f5a66631d2b22)`(JNIEnv *jni_env, jobject activity)`                                                                                                                                                            | [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)` *` Initializes the default [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with default options.                        |
| [Create](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1ad78221c68b6e2aec107a090b28a8b80e)`(const `[AppOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options)` & options)`                                                      | [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)` *` Initializes the default [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given options.                      |
| [Create](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1a202efbe04e8b763e84fe36285a4564ed)`(const `[AppOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options)` & options, JNIEnv *jni_env, jobject activity)`                   | [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)` *` Initializes the default [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given options.                      |
| [Create](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1ae375e41da28e5cb43624489d0ca2f05a)`(const `[AppOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options)` & options, const char *name)`                                    | [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)` *` Initializes a [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given options that operates on the named app. |
| [Create](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1a8762e34db0e2d3ba5f6aa36788d126f3)`(const `[AppOptions](https://firebase.google.com/docs/reference/cpp/class/firebase/app-options#classfirebase_1_1_app_options)` & options, const char *name, JNIEnv *jni_env, jobject activity)` | [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)` *` Initializes a [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given options that operates on the named app. |
| [GetApps](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1afd313706d882852defbe05dee90d000b)`()`                                                                                                                                                                                            | `std::vector< `[App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)` * >` Get all the apps, including the default one.                                                                                                                 |
| [GetInstance](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1a52b5b2208b7bd41a0f9a2940d194409f)`()`                                                                                                                                                                                        | [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)` *` Get the default [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app), or nullptr if none has been created.                          |
| [GetInstance](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1aba9b9b1246ff3aff74a01ebc6c157963)`(const char *name)`                                                                                                                                                                        | [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app)` *` Get the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given name, or nullptr if none have been created.             |

## Public functions

### GetJNIEnv

```c++
JNIEnv * GetJNIEnv() const 
```  
Get JNI environment, needed for performing JNI calls, set on creation.

This is not trivial as the correct environment needs to retrieved per thread.
| **Note:** This method is specific to the Android implementation.

<br />

|               Details                ||
|-------------|-------------------------|
| **Returns** | JNI environment object. |

### activity

```c++
jobject activity() const 
```  
Get a global reference to the Android activity provided to the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) on creation.

Also serves as the Context needed for Firebase calls.
| **Note:** This method is specific to the Android implementation.

<br />

|                                                                                                                  Details                                                                                                                  ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Global JNI reference to the Android activity used to create the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). The reference count of the returned object is not increased. |

### java_vm

```c++
JavaVM * java_vm() const 
```  
Get Java virtual machine, retrieved from the initial JNI environment.


| **Note:** This method is specific to the Android implementation.

<br />

|                    Details                    ||
|-------------|----------------------------------|
| **Returns** | JNI Java virtual machine object. |

### name

```c++
const char * name() const 
```  
Get the name of this [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance.

<br />

|                                                                                                                                                                                                                               Details                                                                                                                                                                                                                                ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The name of this [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance. If a name wasn't provided via [Create()](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1a5161747a9bbed350214cb5e1c0a23503), this returns [kDefaultAppName](https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1af14dd1b4270c2d08b327ff399ef868c9). |

### options

```c++
const AppOptions & options() const 
```  
Get options the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) was created with.

<br />

|                                                                 Details                                                                 ||
|-------------|----------------------------------------------------------------------------------------------------------------------------|
| **Returns** | Options used to create the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). |

### \~App

```c++
 ~App()
```  

## Public static functions

### Create

```c++
App * Create()
```  
Initializes the default [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with default options.


| **Note:** This method is specific to non-Android implementations.

<br />

|                                                                                                                                                                       Details                                                                                                                                                                       ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | New [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance, the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) should not be destroyed for the lifetime of the application. If default options can't be loaded this will return null. |

### Create

```c++
App * Create(
  JNIEnv *jni_env,
  jobject activity
)
```  
Initializes the default [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with default options.


| **Note:** This method is specific to the Android implementation.

<br />

|                                                                                                                                                                                                            Details                                                                                                                                                                                                             ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|----------------------------------------------------------------------------------------------------------------------| | `jni_env`  | JNI environment required to allow Firebase services to interact with the Android framework.                          | | `activity` | JNI reference to the Android activity, required to allow Firebase services to interact with the Android application. | |
| **Returns** | New [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance. The [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) should not be destroyed for the lifetime of the application. If default options can't be loaded this will return null.                                                                            |

### Create

```c++
App * Create(
  const AppOptions & options
)
```  
Initializes the default [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given options.

<br />

| **Note:** This method is specific to non-Android implementations.
Options are copied at initialization time, so changes to the object are ignored.

<br />

|                                                                                                                                                            Details                                                                                                                                                             ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|------------------------------------------------------------------------------------------------------------------------------------------| | `options` | Options that control the creation of the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). | |
| **Returns** | New [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance, the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) should not be destroyed for the lifetime of the application.                                      |

### Create

```c++
App * Create(
  const AppOptions & options,
  JNIEnv *jni_env,
  jobject activity
)
```  
Initializes the default [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given options.

<br />

| **Note:** This method is specific to the Android implementation.
Options are copied at initialization time, so changes to the object are ignored.

<br />

|                                                                                                                                                                                                                                                                                                                       Details                                                                                                                                                                                                                                                                                                                        ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|------------------------------------------------------------------------------------------------------------------------------------------| | `options`  | Options that control the creation of the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app). | | `jni_env`  | JNI environment required to allow Firebase services to interact with the Android framework.                                              | | `activity` | JNI reference to the Android activity, required to allow Firebase services to interact with the Android application.                     | |
| **Returns** | New [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance. The [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) should not be destroyed for the lifetime of the application.                                                                                                                                                                                                                                                                                                                                                            |

### Create

```c++
App * Create(
  const AppOptions & options,
  const char *name
)
```  
Initializes a [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given options that operates on the named app.

<br />

| **Note:** This method is specific to non-Android implementations.
Options are copied at initialization time, so changes to the object are ignored.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `options` | Options that control the creation of the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app).                                                                                                                                                 | | `name`    | Name of this [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance. This is only required when one application uses multiple [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instances. | |
| **Returns** | New [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance, the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) should not be destroyed for the lifetime of the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### Create

```c++
App * Create(
  const AppOptions & options,
  const char *name,
  JNIEnv *jni_env,
  jobject activity
)
```  
Initializes a [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given options that operates on the named app.

<br />

| **Note:** This method is specific to the Android implementation.
Options are copied at initialization time, so changes to the object are ignored.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             ||
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `options`  | Options that control the creation of the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app).                                                                                                                                                 | | `name`     | Name of this [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance. This is only required when one application uses multiple [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instances. | | `jni_env`  | JNI environment required to allow Firebase services to interact with the Android framework.                                                                                                                                                                                              | | `activity` | JNI reference to the Android activity, required to allow Firebase services to interact with the Android application.                                                                                                                                                                     | |
| **Returns** | New [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance. The [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) should not be destroyed for the lifetime of the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

### GetApps

```c++
std::vector< App * > GetApps()
```  
Get all the apps, including the default one.  

### GetInstance

```c++
App * GetInstance()
```  
Get the default [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app), or nullptr if none has been created.  

### GetInstance

```c++
App * GetInstance(
  const char *name
)
```  
Get the [App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) with the given name, or nullptr if none have been created.