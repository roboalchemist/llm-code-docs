# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/firebase-app.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app.md.txt

# Firebase.FirebaseApp Class Reference

# Firebase.FirebaseApp

[Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) application object.

## Summary

[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) acts as a conduit for communication between all [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) services used by an application. A default instance is created automatically, based on settings in your [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) configuration file, and all of the [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) APIs connect with it automatically.

### Inheritance

Inherits from: SystemIDisposable

|                                                                                                                                                                                                                                                                                 ### Properties                                                                                                                                                                                                                                                                                  ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DefaultInstance](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1abf8fab1b5c3d7a745b7d4fd933e5a0fd) | `static `[FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) Get the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance.                                                                                                                  |
| [DefaultName](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1aae471e2f5fc027f1dc98f2a2462fd5a2)     | `static string` Gets the default name for [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) objects.                                                                                                                                                                                                                              |
| [LogLevel](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1aa95be32e8c8d56783fcb16234fbe2b63)        | `static `[LogLevel](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase_1ae165d1d7bc3d85e1c0463a2a1d9ced9a) Gets or sets the minimum log verbosity level for [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) features.                                                                                                |
| [Name](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1a3eb7b11b4076c10606942a878e85b5e4)            | `string` Get the name of this App instance.                                                                                                                                                                                                                                                                                                                                                                 |
| [Options](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1a9c6608312f67ee45c0df199c43ec8e16)         | [AppOptions](https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options) Get the [AppOptions](https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options) the [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) was created with. |

|                                                                                 ### Public functions                                                                                 ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1aa0a8bb6b4dc05642bbfde00371b12474)`()`               | `void` |
| [Dispose](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1aad80ac083653e7aa43318afad2b9d7d9)`(bool disposing)` | `void` |

|                                                                                                                                                                                                                                                                                                                                                                   ### Public static functions                                                                                                                                                                                                                                                                                                                                                                    ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CheckAndFixDependenciesAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1a330d32bf55497c14bb1393a0a8936868)`()`                                                                                                                          | `System.Threading.Tasks.Task< `[DependencyStatus](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase_1a738891954687d6d8243a285eee9ffb04)` >` Asynchronously checks if all of the necessary dependencies for [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) are present on the system, and in the necessary state and attempts to fix them if they are not. |
| [CheckDependenciesAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1a90547699a136786b85b0929968d7f38f)`()`                                                                                                                                | `System.Threading.Tasks.Task< `[DependencyStatus](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase_1a738891954687d6d8243a285eee9ffb04)` >` Asynchronously checks if all of the necessary dependencies for [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) are present on the system, and in the necessary state.                                          |
| [Create](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1adc52b81c47e472234af52e44c8e9d696)`()`                                                                                                                                                | [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) Initializes the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with default options.                                                                                                                                              |
| [Create](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1aaeb3418d9c118fcb63a409ee05a5e4aa)`(`[AppOptions](https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options)` options)`              | [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) Initializes the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with the given options.                                                                                                                                            |
| [Create](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1a39a702e1912ab6b708600b03bd955f4d)`(`[AppOptions](https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options)` options, string name)` | [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) Initializes a [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with the given options that operate on the named app.                                                                                                                        |
| [FixDependenciesAsync](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1ac590e3e129eec9a2ac1ebc6dca231271)`()`                                                                                                                                  | `System.Threading.Tasks.Task` Attempts to fix any missing dependencies that would prevent [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) from working on the system.                                                                                                                                                                                                                           |
| [GetInstance](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1a1de9428973366a520ef87a914569cbbc)`(string name)`                                                                                                                                | [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) Get an instance of an app by name.                                                                                                                                                                                                                                                                                     |

|                                                                   ### Classes                                                                   ||
|----------------------------------------------------------------------------------------------------------------------------------------------|---|
| [Firebase.FirebaseApp.EnableModuleParams](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app/enable-module-params) |   |

## Properties

### DefaultInstance

```c#
static FirebaseApp DefaultInstance
```  
Get the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance.

<br />

|                                             Details                                              ||
|-------------|-------------------------------------------------------------------------------------|
| **Returns** | Reference to the default app, if it hasn't been created this method will create it. |

### DefaultName

```c#
static string DefaultName
```  
Gets the default name for [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) objects.  

### LogLevel

```c#
static LogLevel LogLevel
```  
Gets or sets the minimum log verbosity level for [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) features.


- LogLevel.Verbose allows all log messages to be displayed.
- LogLevel.Assert prevents displaying all but fatal errors.

<br />


| **Note:** Some [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) plugins may require you to set their LogLevel separately.

<br />

|              Details               ||
|-------------|-----------------------|
| **Returns** | The current LogLevel. |

### Name

```c#
string Name
```  
Get the name of this App instance.

<br />

|                                                                                                                                                                                                       Details                                                                                                                                                                                                       ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The name of this App instance. If a name wasn't provided via [Create()](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1adc52b81c47e472234af52e44c8e9d696), this returns [DefaultName](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app_1aae471e2f5fc027f1dc98f2a2462fd5a2). |

### Options

```c#
AppOptions Options
```  
Get the [AppOptions](https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options) the [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) was created with.

<br />

|                                                                                                                                        Details                                                                                                                                        ||
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | [AppOptions](https://firebase.google.com/docs/reference/unity/class/firebase/app-options#class_firebase_1_1_app_options) used to create the [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app). |

## Public functions

### Dispose

```c#
void Dispose()
```  

### Dispose

```c#
void Dispose(
  bool disposing
)
```  

## Public static functions

### CheckAndFixDependenciesAsync

```c#
System.Threading.Tasks.Task< DependencyStatus > CheckAndFixDependenciesAsync()
```  
Asynchronously checks if all of the necessary dependencies for [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) are present on the system, and in the necessary state and attempts to fix them if they are not.

<br />

| **Note:** In some cases, this operation can take a long time and in some cases may prompt the user to update other services on the device. It's recommended to perform other application specific tasks in parallel while checking and potentially fixing dependencies for [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase).
If it's appropriate for your app to handle checking and fixing dependencies separately, you can. Here's effectively what CheckAndFixDependenciesAsync does:

<br />


```c#
using System.Threading.Tasks;  // Needed for the Unwrap extension method.

// ...

Firebase.FirebaseApp.CheckDependenciesAsync().ContinueWith(checkTask => {
  // Peek at the status and see if we need to try to fix dependencies.
  Firebase.DependencyStatus status = checkTask.Result;
  if (status != Firebase.DependencyStatus.Available) {
    return Firebase.FirebaseApp.FixDependenciesAsync().ContinueWith(t => {
      return Firebase.FirebaseApp.CheckDependenciesAsync();
    }).Unwrap();
  } else {
    return checkTask;
  }
}).Unwrap().ContinueWith(task => {
  dependencyStatus = task.Result;
  if (dependencyStatus == Firebase.DependencyStatus.Available) {
    // TODO: Continue with Firebase initialization.
  } else {
    Debug.LogError(
      "Could not resolve all Firebase dependencies: " + dependencyStatus);
  }
});
```

<br />

<br />

|                                                                 Details                                                                 ||
|-------------|----------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A Task that on completion will contain the DependencyStatus enum value, indicating the state of the required dependencies. |

### CheckDependenciesAsync

```c#
System.Threading.Tasks.Task< DependencyStatus > CheckDependenciesAsync()
```  
Asynchronously checks if all of the necessary dependencies for [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) are present on the system, and in the necessary state.


| **Note:** In some cases, this operation can take a long time. It's recommended to perform other application specific tasks in parallel while checking dependencies for [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase).

<br />

|                                                                 Details                                                                 ||
|-------------|----------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A Task that on completion will contain the DependencyStatus enum value, indicating the state of the required dependencies. |

### Create

```c#
FirebaseApp Create()
```  
Initializes the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with default options.

<br />

|                                                                        Details                                                                         ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | New [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance. |

### Create

```c#
FirebaseApp Create(
  AppOptions options
)
```  
Initializes the default [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with the given options.

<br />

|                                                                                                                                                                                         Details                                                                                                                                                                                          ||
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `options` | Options that control the creation of the [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app). | |
| **Returns** | New [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance.                                                                                                                                                                                                                                   |

### Create

```c#
FirebaseApp Create(
  AppOptions options,
  string name
)
```  
Initializes a [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) with the given options that operate on the named app.

<br />

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters  | |-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `options` | Options that control the creation of the [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app).                                                                                                                                                                              | | `name`    | Name of this [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance. This is only required when one application uses multiple [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instances. | |
| **Returns** | New [FirebaseApp](https://firebase.google.com/docs/reference/unity/class/firebase/firebase-app#class_firebase_1_1_firebase_app) instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### FixDependenciesAsync

```c#
System.Threading.Tasks.Task FixDependenciesAsync()
```  
Attempts to fix any missing dependencies that would prevent [Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase) from working on the system.

Since this function is asynchronous, the returned Task must be monitored in order to tell when it has completed. Also note, that depending on the fixes necessary, the user may be prompted for additional input.

<br />

|                                       Details                                        ||
|-------------|-------------------------------------------------------------------------|
| **Returns** | System.Threading.Tasks.Task A task that tracks the progress of the fix. |

### GetInstance

```c#
FirebaseApp GetInstance(
  string name
)
```  
Get an instance of an app by name.

<br />

|                                             Details                                              ||
|-------------|-------------------------------------------------------------------------------------|
| Parameters  | |--------|------------------------------| | `name` | Name of the app to retrieve. | |
| **Returns** | Reference to the app if it was previously created, null otherwise.                  |