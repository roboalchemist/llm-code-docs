# Source: https://firebase.google.com/docs/crashlytics.md.txt

# Source: https://firebase.google.com/docs/reference/unity/namespace/firebase/crashlytics.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics.md.txt

# Source: https://firebase.google.com/docs/reference/unity/namespace/firebase/crashlytics.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics.md.txt

# Firebase.Crashlytics.Crashlytics Class Reference

# Firebase.Crashlytics.Crashlytics

[Firebase](https://firebase.google.com/docs/reference/unity/namespace/firebase#namespace_firebase)[Crashlytics](https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics#class_firebase_1_1_crashlytics_1_1_crashlytics) API

## Summary

|                                                                                                                                                                                                                        ### Properties                                                                                                                                                                                                                         ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IsCrashlyticsCollectionEnabled](https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics#class_firebase_1_1_crashlytics_1_1_crashlytics_1a822df76a8df6def2be982e1bbe9b3995)` = false` | `static bool` Checks whether the [Crashlytics](https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics#class_firebase_1_1_crashlytics_1_1_crashlytics) specific data collection flag has been enabled. |
| [ReportUncaughtExceptionsAsFatal](https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics#class_firebase_1_1_crashlytics_1_1_crashlytics_1a7e4f3f31fd881ddc9fda119b85344f4c)          | `static bool` Whether [Crashlytics](https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics#class_firebase_1_1_crashlytics_1_1_crashlytics) is set to report uncaught exceptions as fatal.             |

|                                                                                                                                                            ### Public static functions                                                                                                                                                             ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [Log](https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics#class_firebase_1_1_crashlytics_1_1_crashlytics_1a81dec5c9ec6ac5ea0c175d0994a013fe)`(string message)`                    | `void` Add text logs that will be sent with the next crash report.                                                          |
| [LogException](https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics#class_firebase_1_1_crashlytics_1_1_crashlytics_1a98c881e11c769cd6bf723d0b749da364)`(Exception exception)`      | `void` Record a non-fatal exception.                                                                                        |
| [SetCustomKey](https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics#class_firebase_1_1_crashlytics_1_1_crashlytics_1ac8d9e5d544fdfaf97de1fee8ee615acd)`(string key, string value)` | `void` Set a key/value pair to be sent with the next crash report.                                                          |
| [SetUserId](https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics#class_firebase_1_1_crashlytics_1_1_crashlytics_1af38d4266cfccb6dd3787b6af32877f4f)`(string identifier)`           | `void` Optionally set an end-user's ID number, token, or other unique value to be associated with subsequent crash reports. |

## Properties

### IsCrashlyticsCollectionEnabled

```c#
static bool IsCrashlyticsCollectionEnabled = false
```  
Checks whether the [Crashlytics](https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics#class_firebase_1_1_crashlytics_1_1_crashlytics) specific data collection flag has been enabled.

<br />

|                                              Details                                              ||
|-------------|--------------------------------------------------------------------------------------|
| **Returns** | true if the platform level data collection flag is enabled or unset, false otherwise |

### ReportUncaughtExceptionsAsFatal

```c#
static bool ReportUncaughtExceptionsAsFatal
```  
Whether [Crashlytics](https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics#class_firebase_1_1_crashlytics_1_1_crashlytics) is set to report uncaught exceptions as fatal.

Fatal exceptions count towards Crash Free Users and Velocity Alerts. It is recommended to enable this for new apps.

|                                                                                                                  Details                                                                                                                   ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | true if [Crashlytics](https://firebase.google.com/docs/reference/unity/class/firebase/crashlytics/crashlytics#class_firebase_1_1_crashlytics_1_1_crashlytics) is set to report uncaught exceptions as fatal, false otherwise. |

## Public static functions

### Log

```c#
void Log(
  string message
)
```  
Add text logs that will be sent with the next crash report.

<br />

|                                       Details                                       ||
|------------|-------------------------------------------------------------------------|
| Parameters | |-----------|---------------------| | `message` | The message to log. | |

### LogException

```c#
void LogException(
  Exception exception
)
```  
Record a non-fatal exception.

<br />

|                                           Details                                           ||
|------------|---------------------------------------------------------------------------------|
| Parameters | |-------------|-----------------------| | `exception` | The exception to log. | |

### SetCustomKey

```c#
void SetCustomKey(
  string key,
  string value
)
```  
Set a key/value pair to be sent with the next crash report.

<br />

|                                                                                                                                                                                                                                                                                                                                              Details                                                                                                                                                                                                                                                                                                                                               ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `key`   | Key to associate with a given value. If the key already exists, the new value will overwrite the existing value. When crash reports are recorded, the current value associated with each key will be captured. | | `value` | The value to associate with the given key.                                                                                                                                                                     | |

### SetUserId

```c#
void SetUserId(
  string identifier
)
```  
Optionally set an end-user's ID number, token, or other unique value to be associated with subsequent crash reports.

<br />

|                                                                                Details                                                                                ||
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parameters | |--------------|-----------------------------------------------------------| | `identifier` | The user identifier to associate with subsequent crashes. | |