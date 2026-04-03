# Source: https://firebase.google.com/docs/reference/js/performance.md.txt

# performance package

The Firebase Performance Monitoring Web SDK. This SDK does not work in a Node.js environment.

## Functions

|                                                              Function                                                              |                                                                                             Description                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **function(app, ...)**                                                                                                             |                                                                                                                                                                                                      |
| [getPerformance(app)](https://firebase.google.com/docs/reference/js/performance.md#getperformance_cf608e1)                         | Returns a [FirebasePerformance](https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md#firebaseperformance_interface) instance for the given app.                          |
| [initializePerformance(app, settings)](https://firebase.google.com/docs/reference/js/performance.md#initializeperformance_980350e) | Returns a [FirebasePerformance](https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md#firebaseperformance_interface) instance for the given app. Can only be called once. |
| **function(performance, ...)**                                                                                                     |                                                                                                                                                                                                      |
| [trace(performance, name)](https://firebase.google.com/docs/reference/js/performance.md#trace_62e4b7e)                             | Returns a new `PerformanceTrace` instance.                                                                                                                                                           |

## Interfaces

|                                                               Interface                                                               |                            Description                            |
|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [FirebasePerformance](https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md#firebaseperformance_interface) | The Firebase Performance Monitoring service interface.            |
| [PerformanceSettings](https://firebase.google.com/docs/reference/js/performance.performancesettings.md#performancesettings_interface) | Defines configuration options for the Performance Monitoring SDK. |
| [PerformanceTrace](https://firebase.google.com/docs/reference/js/performance.performancetrace.md#performancetrace_interface)          | The interface representing a `Trace`.                             |

## function(app, ...)

### getPerformance(app)

Returns a [FirebasePerformance](https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md#firebaseperformance_interface) instance for the given app.

**Signature:**  

    export declare function getPerformance(app?: FirebaseApp): FirebasePerformance;

#### Parameters

| Parameter |                                                 Type                                                  |                                                    Description                                                    |
|-----------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| app       | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) to use. |

**Returns:**

[FirebasePerformance](https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md#firebaseperformance_interface)

### initializePerformance(app, settings)

Returns a [FirebasePerformance](https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md#firebaseperformance_interface) instance for the given app. Can only be called once.

**Signature:**  

    export declare function initializePerformance(app: FirebaseApp, settings?: PerformanceSettings): FirebasePerformance;

#### Parameters

| Parameter |                                                                 Type                                                                  |                                                                                Description                                                                                |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| app       | [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface)                                 | The [FirebaseApp](https://firebase.google.com/docs/reference/js/app.firebaseapp.md#firebaseapp_interface) to use.                                                         |
| settings  | [PerformanceSettings](https://firebase.google.com/docs/reference/js/performance.performancesettings.md#performancesettings_interface) | Optional settings for the [FirebasePerformance](https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md#firebaseperformance_interface) instance. |

**Returns:**

[FirebasePerformance](https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md#firebaseperformance_interface)

## function(performance, ...)

### trace(performance, name)

Returns a new `PerformanceTrace` instance.

**Signature:**  

    export declare function trace(performance: FirebasePerformance, name: string): PerformanceTrace;

#### Parameters

|  Parameter  |                                                                 Type                                                                  |                                                                        Description                                                                         |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| performance | [FirebasePerformance](https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md#firebaseperformance_interface) | The [FirebasePerformance](https://firebase.google.com/docs/reference/js/performance.firebaseperformance.md#firebaseperformance_interface) instance to use. |
| name        | string                                                                                                                                | The name of the trace.                                                                                                                                     |

**Returns:**

[PerformanceTrace](https://firebase.google.com/docs/reference/js/performance.performancetrace.md#performancetrace_interface)